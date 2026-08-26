#!/usr/bin/env python3
"""Author-side adversarial checks for ENA v0.3.7 candidate.0.

These checks target decision-changing packaging/operational failure shapes. They
are not independent semantic validation and do not establish external truth.
The attack set is intentionally open: a passing run means these attacks did not
falsify the exact candidate bytes, not that the possible attack space is closed.
"""
from __future__ import annotations

import copy
import importlib.util
import re
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parents[2]
ROOT = REPO / "releases" / "v0.3.7-candidate"
OP = ROOT / "operational"
ZH = ROOT / "language-projections" / "zh-CN"

failures: list[str] = []
observed: list[str] = []


def check(condition: bool, message: str) -> None:
    if condition:
        observed.append(message)
    else:
        failures.append(message)


def load_yaml(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise AssertionError(f"expected mapping: {path}")
    return value


def route_ids(text: str) -> set[str]:
    return set(re.findall(r"^## (OA-[A-Z]+-\d+)\b", text, flags=re.MULTILINE))


def all_route_mentions(text: str) -> set[str]:
    return set(re.findall(r"\bOA-[A-Z]+-\d+\b", text))


def validate_manifest_policy(manifest: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    policy = manifest.get("policy", {})
    if policy.get("required_for_complete_adoption_default") is not False:
        errors.append("manifest default must not require bundled references")
    if policy.get("default_activation_default") is not False:
        errors.append("manifest default must not activate bundled references")
    if policy.get("package_inclusion_implies_applicability") is not False:
        errors.append("package inclusion must not imply applicability")
    if policy.get("package_inclusion_implies_activation") is not False:
        errors.append("package inclusion must not imply activation")
    if policy.get("host_native_equivalent_allowed") is not True:
        errors.append("Host-native equivalent must remain allowed")
    for ref in manifest.get("references", []):
        if ref.get("required_for_complete_adoption") is not False:
            errors.append(f"{ref.get('id')}: required_for_complete_adoption drift")
        if ref.get("default_activation") is not False:
            errors.append(f"{ref.get('id')}: default_activation drift")
    return errors


def resolve_primary_path(value: str) -> Path | None:
    # Descriptive entries such as "general retrieval reference via OA-RET-01"
    # are not filesystem paths.
    base = value.split("#", 1)[0]
    if base.startswith("../") or base.startswith("procedures/") or base.startswith("patterns/"):
        return (OP / base).resolve()
    if base in {"CUE-INDEX.md", "HOW-MAP.md", "REFERENCE-INDEX.yaml"}:
        return (OP / base).resolve()
    return None


def attack_stale_state() -> None:
    stale_markers = [
        "ASSEMBLY_PENDING_STAGE_3",
        "MANIFEST_SELECTED_CONTENT_ASSEMBLY_PENDING",
        "CANDIDATE_PRIMARY_TOOL_ASSEMBLY_PENDING",
        "OPERATIONAL_PROJECTION_ASSEMBLY_PENDING",
        "STAGE_1_SHELL",
        "Stage 1 creates only this entry surface",
        "inherited_files_may_still_contain_v036_current_identity_during_assembly: true",
        "candidate identity/status reconciliation across inherited adopter-facing files",
    ]
    text_suffixes = {".md", ".yaml", ".yml", ".json", ".py"}
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file() or p.suffix.lower() not in text_suffixes:
            continue
        text = p.read_text(encoding="utf-8")
        for marker in stale_markers:
            check(marker not in text, f"no stale marker {marker!r} in {p.relative_to(ROOT)}")

    index = load_yaml(OP / "REFERENCE-INDEX.yaml")
    check(
        index["routes"]["OA-EVO-01"].get("tool_state") == "ASSEMBLED_MACHINE_CHECKED_STAGE_3",
        "OA-EVO-01 tool_state reflects assembled machine-checked v2 helper",
    )

    key_paths = [
        "README.md",
        "00-READ-ME-FIRST.md",
        "RUNTIME-ADOPTION-KERNEL.md",
        "AGENT-ADOPTION-INSTRUCTION.md",
        "LITE-ADOPTION-INSTRUCTION.md",
        "09-EVOLUTION-METABOLISM.md",
        "operational/CUE-INDEX.md",
        "operational/HOW-MAP.md",
        "language-projections/zh-CN/00-READ-ME-FIRST.md",
        "language-projections/zh-CN/RUNTIME-ADOPTION-KERNEL.md",
        "language-projections/zh-CN/09-EVOLUTION-METABOLISM.md",
    ]
    for rel in key_paths:
        text = (ROOT / rel).read_text(encoding="utf-8")
        check("`tools/ena_evolve.py`" not in text, f"no old default ena_evolve.py path in {rel}")


def attack_route_graph() -> None:
    index = load_yaml(OP / "REFERENCE-INDEX.yaml")
    routes = index.get("routes", {})
    route_set = set(routes)
    en_how_text = (OP / "HOW-MAP.md").read_text(encoding="utf-8")
    en_cue_text = (OP / "CUE-INDEX.md").read_text(encoding="utf-8")
    zh_how_text = (ZH / "operational" / "HOW-MAP.md").read_text(encoding="utf-8")
    zh_cue_text = (ZH / "operational" / "CUE-INDEX.md").read_text(encoding="utf-8")

    en_how = route_ids(en_how_text)
    zh_how = route_ids(zh_how_text)
    check(route_set == en_how, f"REFERENCE-INDEX route set equals English HOW-MAP route set: {sorted(route_set)}")
    check(route_set == zh_how, "zh-CN HOW-MAP carries the complete operational route set")
    check(route_set <= all_route_mentions(en_cue_text), "English Cue Index can mention every operational route")
    check(route_set <= all_route_mentions(zh_cue_text), "zh-CN Cue Index can mention every operational route")

    root_resolved = ROOT.resolve()
    for rid, route in routes.items():
        for value in route.get("primary", []) or []:
            if not isinstance(value, str):
                failures.append(f"{rid}: primary entry is not a string")
                continue
            p = resolve_primary_path(value)
            if p is None:
                continue
            try:
                p.relative_to(root_resolved)
                inside = True
            except ValueError:
                inside = False
            check(inside, f"{rid}: primary path stays inside candidate subtree: {value}")
            check(p.exists(), f"{rid}: primary path exists: {value}")
            if "#" in value and p.name == "HOW-MAP.md":
                anchor_route = re.search(r"oa-[a-z]+-\d+", value.lower())
                check(anchor_route is not None, f"{rid}: HOW-MAP anchor identifies an OA route")
                if anchor_route:
                    check(anchor_route.group(0).upper() in en_how, f"{rid}: HOW-MAP anchor resolves to an existing route")

        for dep in route.get("composition", []) or []:
            check(dep in route_set, f"{rid}: composition route exists: {dep}")

    manifest = load_yaml(ROOT / "references" / "REFERENCE-MANIFEST.yaml")
    bundled = {r.get("id") for r in manifest.get("references", [])}
    deferred = {r.get("id") for r in manifest.get("deferred_not_bundled_first_candidate", [])}
    com = routes["OA-COM-01"]
    check(com.get("deferred_reference") not in bundled, "deferred Commitment/Settlement is not accidentally bundled")
    check(com.get("deferred_reference") in deferred, "deferred Commitment/Settlement remains represented in durable manifest lineage")

    # Mutation sensitivity: a broken composition edge must be detectable.
    mutant = copy.deepcopy(routes)
    mutant["OA-COM-01"]["composition"] = ["OA-NOT-REAL-99"]
    mutant_errors = [
        f"{rid}->{dep}"
        for rid, route in mutant.items()
        for dep in (route.get("composition", []) or [])
        if dep not in mutant
    ]
    check(bool(mutant_errors), "route-graph oracle detects a deliberately broken composition edge")


def attack_reference_optionality() -> None:
    manifest = load_yaml(ROOT / "references" / "REFERENCE-MANIFEST.yaml")
    check(not validate_manifest_policy(manifest), "original reference manifest preserves optional/default-off Host-native policy")

    for ref in manifest.get("references", []):
        wrapper = ROOT / str(ref["path"]) / "README.md"
        check(wrapper.is_file(), f"reference wrapper exists: {ref.get('id')}")
        if wrapper.is_file():
            text = wrapper.read_text(encoding="utf-8")
            check("OPTIONAL_REFERENCE" in text, f"{ref.get('id')}: wrapper declares OPTIONAL_REFERENCE")
            check("DEFAULT_OFF" in text, f"{ref.get('id')}: wrapper declares DEFAULT_OFF")
            check("NOT_NORMATIVE_ONTOLOGY" in text, f"{ref.get('id')}: wrapper rejects ontology promotion")

    # Mutation sensitivity for the packaging oracle. These are not new ENA rules;
    # they prove the author gate would reject the exact overclaim classes it guards.
    mutants: list[dict[str, Any]] = []
    m1 = copy.deepcopy(manifest)
    m1["policy"]["package_inclusion_implies_applicability"] = True
    mutants.append(m1)
    m2 = copy.deepcopy(manifest)
    m2["references"][0]["required_for_complete_adoption"] = True
    mutants.append(m2)
    m3 = copy.deepcopy(manifest)
    m3["references"][0]["default_activation"] = True
    mutants.append(m3)
    for i, mutant in enumerate(mutants, 1):
        check(bool(validate_manifest_policy(mutant)), f"manifest oracle rejects overclaim mutation {i}")


def attack_false_block_escape_routes() -> None:
    index = load_yaml(OP / "REFERENCE-INDEX.yaml")
    rules = index["rules"]
    check(rules.get("reference_exists_implies_applicable") is False, "reference existence does not force applicability")
    check(rules.get("reference_exists_implies_required") is False, "reference existence does not force requirement")
    check(rules.get("host_native_equivalent_allowed") is True, "Host-native HOW remains first-class")
    check(rules.get("missing_reference_may_route_to_host_pattern_or_honest_residual") is True, "missing reference may route to Host HOW or honest residual")

    routes = index["routes"]
    check(routes["OA-AUTH-01"].get("non_applicable_route") == "NOT_REQUIRED", "Authority exposes NOT_REQUIRED")
    check(routes["OA-AUTHOR-01"].get("non_applicable_route") == "OUT_OF_SCOPE_FOR_CONTESTED_AUTHORSHIP", "Contested Authorship exposes out-of-scope")
    check(routes["OA-STAND-01"].get("non_applicable_route") == "NO_FORMAL_STANDING", "Standing exposes NO_FORMAL_STANDING")

    continuity = (OP / "procedures" / "PURPOSE-RELATIVE-CONTINUITY.md").read_text(encoding="utf-8")
    standing = (OP / "procedures" / "STANDING-INPUT.md").read_text(encoding="utf-8")
    retirement = (OP / "procedures" / "CONTROL-RETIREMENT.md").read_text(encoding="utf-8")
    guide = (ZH / "REFERENCE-GUIDE.md").read_text(encoding="utf-8")
    how = (OP / "HOW-MAP.md").read_text(encoding="utf-8")

    check("NOT_REQUIRED" in continuity, "Purpose-relative continuity can stop as NOT_REQUIRED")
    check("NO_FORMAL_STANDING" in standing, "Standing can decline formal machinery")
    check("KEEP_ACTIVE" in retirement and "UNKNOWN_WAIT" in retirement, "Control retirement can preserve or wait rather than force deletion")
    check("BUNDLED != REQUIRED" in guide and "BUNDLED != DEFAULT_ACTIVE" in guide, "zh-CN guide preserves bundled-reference optionality")
    check("Composition does not allow one organ to inherit another organ's evidence maturity." in how, "composition cannot launder evidence maturity")


def attack_language_projection() -> None:
    en_how = route_ids((OP / "HOW-MAP.md").read_text(encoding="utf-8"))
    zh_how = route_ids((ZH / "operational" / "HOW-MAP.md").read_text(encoding="utf-8"))
    check(en_how == zh_how, "English and zh-CN HOW maps expose the same route identities")

    projection = load_yaml(ZH / "projection-manifest.yaml")
    check(projection.get("not_current") is True, "zh-CN projection cannot self-promote candidate to Current")
    check(projection.get("source_semantic_version") == "v0.3.7-candidate.0", "zh-CN projection binds to candidate semantic identity")
    machine_policy = projection.get("machine_artifact_policy", {})
    check(machine_policy.get("translate_machine_reference_files_one_by_one") is False, "zh-CN projection does not fork machine canonical bytes")

    fixtures = load_yaml(ROOT / "language-projections" / "semantic-fixtures.v3.yaml")
    cases = fixtures.get("cases", [])
    check(bool(cases), "operational bilingual fixture corpus is non-empty")
    expected_routes = set(fixtures.get("coverage", {}).get("routes_expected", []))
    actual_routes = {case.get("expected_route") for case in cases}
    check(expected_routes == actual_routes, "fixture coverage declaration equals represented route corpus")
    check(actual_routes <= en_how, "every bilingual fixture route exists in canonical HOW map")
    for case in cases:
        check(bool(str(case.get("en", "")).strip()), f"{case.get('id')}: English scenario present")
        check(bool(str(case.get("zh-CN", "")).strip()), f"{case.get('id')}: zh-CN scenario present")
        check(bool(case.get("expected_properties")), f"{case.get('id')}: decision properties represented")
    evidence_boundary = "\n".join(str(x) for x in fixtures.get("evidence_boundary", []))
    check("cardinality is open" in evidence_boundary.lower(), "bilingual fixture count remains an open corpus fact")


def load_v2_helper():
    path = ROOT / "tools" / "ena_evolve_v2.py"
    spec = importlib.util.spec_from_file_location("ena_v037_author_attack_helper", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load candidate v2 helper")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def attack_v2_migration_boundaries() -> None:
    try:
        mod = load_v2_helper()
        source = mod.build_latent_record(
            "author-supported-source",
            "A bounded source experiment improves quality.",
            "Synthetic source-only improvement.",
            variation_space="sandbox",
        )
        source["lifecycle_state"] = "EXPERIMENTED"
        source["experiments"] = [{
            "experiment_id": "exp-supported",
            "time": "2026-08-27T00:10:00Z",
            "provenance": "LOCAL",
            "variation_space": "sandbox",
            "actual_change": "synthetic source-only improvement",
        }]
        source["selection_state"] = "SUPPORTED"
        source["evaluations"] = [{
            "evaluation_id": "eval-supported",
            "time": "2026-08-27T00:11:00Z",
            "provenance": "LOCAL",
            "outcomes": {"quality": "IMPROVED"},
            "selection": "SUPPORTED",
            "evidence_refs": ["trace:source-supported"],
            "negative_evidence": [],
        }]
        source_errors = mod.validate_record_v2(source)
        check(not source_errors, f"synthetic locally SUPPORTED source is valid: {source_errors}")
        if source_errors:
            return

        packet = mod.export_packet_v2(source)
        check(packet["packet_purpose"] == "ADAPTATION_CANDIDATE", "SUPPORTED source exports as adaptation candidate")
        check(packet["source_selection_state"] == "SUPPORTED", "packet preserves source selection truth")
        check(packet["source_authentication"] == "NOT_AUTHENTICATED_BY_THIS_PACKET", "packet digest does not become source authentication")

        imported = mod.import_packet_v2(packet, "author-receiver")
        check(imported["origin"] == "MIGRATION_CANDIDATE", "receiver record remains a migration candidate")
        check(imported["selection_state"] == "UNASSESSED", "source SUPPORTED does not become receiver-local SUPPORTED")
        check(imported["expression_state"] == "LATENT", "import does not silently express source adaptation")
        check(imported["variation_space"] is None, "import does not force premature receiver Variation Space")
        check(imported["migration"]["source_selection_state"] == "SUPPORTED", "receiver preserves source selection separately")
        check(imported["migration"]["transfer_status"] == "TRANSFERRED_NOT_LOCALLY_VALIDATED", "receiver transfer status remains explicitly unvalidated")

        laundered = copy.deepcopy(imported)
        laundered["selection_state"] = "SUPPORTED"
        check(bool(mod.validate_record_v2(laundered)), "record validator rejects receiver-local selection laundering without local evidence")

        tampered = copy.deepcopy(packet)
        tampered["change"] = "changed after digest"
        check(bool(mod.validate_packet_v2(tampered)), "packet validator detects post-digest content tampering")
    except Exception as exc:  # preserve the exact failure as an attack result
        failures.append(f"v2 migration attack raised unexpected exception: {exc!r}")


def attack_candidate_status() -> None:
    baseline = load_yaml(ROOT / "CANDIDATE-BASELINE.yaml")
    check(baseline.get("current") is False, "candidate baseline current=false")
    check(baseline.get("frozen") is False, "candidate baseline frozen=false before freeze record")
    check(baseline.get("released") is False, "candidate baseline released=false")
    check(baseline.get("must_not_be_adopted_as_current") is True, "candidate baseline prohibits self-adoption as Current")
    check(baseline.get("maturity") == "PREFREEZE_AUTHOR_FALSIFICATION", "baseline maturity matches author-falsification phase")
    check(baseline.get("assembly", {}).get("state") == "IDENTITY_RECONCILED_MACHINE_CHECKED_AWAITING_AUTHOR_FALSIFICATION", "baseline phase matches reconciled candidate reality")


def main() -> None:
    attack_stale_state()
    attack_route_graph()
    attack_reference_optionality()
    attack_false_block_escape_routes()
    attack_language_projection()
    attack_v2_migration_boundaries()
    attack_candidate_status()

    if failures:
        print("AUTHOR_ATTACK_VERDICT=FAIL")
        print(f"observed_pass_conditions={len(observed)}")
        print(f"failures={len(failures)}")
        for item in failures:
            print(f"FAIL: {item}")
        raise SystemExit(1)

    print("AUTHOR_ATTACK_VERDICT=PASS")
    print(f"observed_pass_conditions={len(observed)}")
    print("attack_cardinality=OPEN")
    print("evidence_scope=AUTHOR_SIDE_DETERMINISTIC_AND_REPRESENTED_SEMANTIC_ATTACKS_ONLY")
    print("independent_semantic_support=NOT_ESTABLISHED")
    print("external_truth=NOT_ESTABLISHED")


if __name__ == "__main__":
    main()
