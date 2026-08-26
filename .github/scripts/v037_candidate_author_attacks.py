#!/usr/bin/env python3
"""Phase-aware author-side adversarial checks for ENA v0.3.7 candidate.0.

This harness checks current structured state and decision-changing operational
boundaries rather than counting every historical token occurrence. PASS is
not independent semantic support, external truth, freeze authority, or release
authority. Attack cardinality remains open.
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
passes: list[str] = []
failures: list[str] = []


def check(condition: bool, label: str) -> None:
    (passes if condition else failures).append(label)


def load_yaml(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise AssertionError(f"expected mapping: {path}")
    return value


def route_ids(path: Path) -> set[str]:
    return set(re.findall(r"^## (OA-[A-Z]+-\d+)\b", path.read_text(encoding="utf-8"), flags=re.MULTILINE))


def load_v2_helper():
    path = ROOT / "tools" / "ena_evolve_v2.py"
    spec = importlib.util.spec_from_file_location("ena_v037_author_attack_helper", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load candidate v2 helper")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def attack_candidate_state() -> None:
    b = load_yaml(ROOT / "CANDIDATE-BASELINE.yaml")
    check(b.get("ena_version") == "v0.3.7-candidate.0", "candidate identity remains v0.3.7-candidate.0")
    check(b.get("current") is False, "candidate current=false")
    check(b.get("frozen") is False, "candidate frozen=false before external freeze")
    check(b.get("released") is False, "candidate released=false")
    check(b.get("must_not_be_adopted_as_current") is True, "candidate cannot self-promote to Current")
    check(b.get("maturity") == "PREFREEZE_VALIDATION", "candidate is in exact pre-freeze validation phase")
    check(
        b.get("assembly", {}).get("state") == "AUTHOR_FALSIFICATION_CLOSED_AWAITING_EXACT_PREFREEZE_VALIDATION",
        "assembly state matches pre-freeze phase",
    )
    check(b.get("author_falsification", {}).get("conclusion") == "SUCCESS", "prior author-falsification occurrence remains recorded")
    check(b.get("author_falsification", {}).get("attack_cardinality") == "OPEN", "author attack space remains open")
    check(b.get("freeze_protocol", {}).get("model") == "EXTERNAL_RECORD_BINDS_EXACT_IMMUTABLE_TREE", "freeze remains external exact-tree binding")
    # Historical text is allowed to preserve occurrence truth. Only active structured
    # state is checked for staleness.
    check(b.get("references", {}).get("state") == "ASSEMBLED_MACHINE_CHECKED_STAGE_3", "reference current state is assembled")
    check(b.get("tooling", {}).get("state") == "ASSEMBLED_MACHINE_CHECKED_STAGE_3", "tool current state is assembled")
    check(b.get("language", {}).get("state") == "ZH_CN_OPERATIONAL_PROJECTION_MACHINE_CHECKED_STAGE_4", "language current state is assembled")


def attack_route_graph() -> None:
    index = load_yaml(OP / "REFERENCE-INDEX.yaml")
    routes = index.get("routes", {})
    route_set = set(routes)
    en = route_ids(OP / "HOW-MAP.md")
    zh = route_ids(ZH / "operational" / "HOW-MAP.md")
    check(route_set == en, "Reference Index and English HOW map expose same routes")
    check(route_set == zh, "English and zh-CN HOW maps expose same routes")
    en_cue = (OP / "CUE-INDEX.md").read_text(encoding="utf-8")
    zh_cue = (ZH / "operational" / "CUE-INDEX.md").read_text(encoding="utf-8")
    for rid in sorted(route_set):
        check(rid in en_cue, f"English cue surface can reach {rid}")
        check(rid in zh_cue, f"zh-CN cue surface can reach {rid}")
    for rid, route in routes.items():
        for dep in route.get("composition", []) or []:
            check(dep in route_set, f"{rid} composition target exists: {dep}")
    check(routes["OA-EVO-01"].get("tool_state") == "ASSEMBLED_MACHINE_CHECKED_STAGE_3", "OA-EVO-01 tool metadata matches reality")
    check(routes["OA-AUTH-01"].get("non_applicable_route") == "NOT_REQUIRED", "Authority preserves NOT_REQUIRED")
    check(routes["OA-AUTHOR-01"].get("non_applicable_route") == "OUT_OF_SCOPE_FOR_CONTESTED_AUTHORSHIP", "Authorship preserves out-of-scope route")
    check(routes["OA-STAND-01"].get("non_applicable_route") == "NO_FORMAL_STANDING", "Standing preserves no-formal-standing route")
    mutant = copy.deepcopy(routes)
    mutant["OA-COM-01"]["composition"] = ["OA-NOT-REAL-99"]
    bad_edges = [(rid, dep) for rid, route in mutant.items() for dep in (route.get("composition", []) or []) if dep not in mutant]
    check(bool(bad_edges), "route oracle detects a deliberately broken composition edge")


def attack_optionality_and_host_diversity() -> None:
    m = load_yaml(ROOT / "references" / "REFERENCE-MANIFEST.yaml")
    p = m.get("policy", {})
    check(p.get("required_for_complete_adoption_default") is False, "bundled references default to not required")
    check(p.get("default_activation_default") is False, "bundled references default off")
    check(p.get("package_inclusion_implies_applicability") is False, "package inclusion does not imply applicability")
    check(p.get("package_inclusion_implies_activation") is False, "package inclusion does not imply activation")
    check(p.get("host_native_equivalent_allowed") is True, "Host-native equivalent remains first-class")
    for ref in m.get("references", []):
        rid = str(ref.get("id"))
        check(ref.get("required_for_complete_adoption") is False, f"{rid} is not required for complete adoption")
        check(ref.get("default_activation") is False, f"{rid} is default-off")
        wrapper = ROOT / str(ref.get("path")) / "README.md"
        check(wrapper.is_file(), f"{rid} wrapper exists")
        if wrapper.is_file():
            text = wrapper.read_text(encoding="utf-8")
            check("OPTIONAL_REFERENCE" in text, f"{rid} wrapper says optional")
            check("DEFAULT_OFF" in text, f"{rid} wrapper says default-off")
            check("NOT_NORMATIVE_ONTOLOGY" in text, f"{rid} wrapper rejects ontology promotion")
    bundled = {r.get("id") for r in m.get("references", [])}
    deferred = {r.get("id") for r in m.get("deferred_not_bundled_first_candidate", [])}
    check("commitment-settlement-recovered" not in bundled, "Commitment/Settlement is not silently bundled")
    check("commitment-settlement-recovered" in deferred, "Commitment/Settlement remains durable deferred lineage")
    mutations = []
    for field in ("package_inclusion_implies_applicability", "package_inclusion_implies_activation"):
        mm = copy.deepcopy(m); mm["policy"][field] = True; mutations.append(mm)
    mm = copy.deepcopy(m); mm["references"][0]["required_for_complete_adoption"] = True; mutations.append(mm)
    mm = copy.deepcopy(m); mm["references"][0]["default_activation"] = True; mutations.append(mm)
    def has_overclaim(x: dict[str, Any]) -> bool:
        pp = x["policy"]
        return bool(pp["package_inclusion_implies_applicability"] or pp["package_inclusion_implies_activation"] or any(r["required_for_complete_adoption"] or r["default_activation"] for r in x["references"]))
    for i, mutation in enumerate(mutations, 1):
        check(has_overclaim(mutation), f"optionality oracle detects deliberate overclaim mutation {i}")


def attack_false_block_escape_routes() -> None:
    continuity = (OP / "procedures" / "PURPOSE-RELATIVE-CONTINUITY.md").read_text(encoding="utf-8")
    standing = (OP / "procedures" / "STANDING-INPUT.md").read_text(encoding="utf-8")
    retirement = (OP / "procedures" / "CONTROL-RETIREMENT.md").read_text(encoding="utf-8")
    guide = (ZH / "REFERENCE-GUIDE.md").read_text(encoding="utf-8")
    how = (OP / "HOW-MAP.md").read_text(encoding="utf-8")
    check("NOT_REQUIRED" in continuity, "Continuity can stop as NOT_REQUIRED")
    check("NO_FORMAL_STANDING" in standing, "Standing can decline formal machinery")
    check("KEEP_ACTIVE" in retirement, "Control retirement can keep a justified control")
    check("UNKNOWN_WAIT" in retirement, "Control retirement can remain unknown/wait")
    check("BUNDLED != REQUIRED" in guide, "zh-CN guide preserves bundled != required")
    check("BUNDLED != DEFAULT_ACTIVE" in guide, "zh-CN guide preserves bundled != default-active")
    check("Composition does not allow one organ to inherit another organ's evidence maturity." in how, "composition does not launder evidence maturity")


def attack_language_projection() -> None:
    p = load_yaml(ZH / "projection-manifest.yaml")
    check(p.get("not_current") is True, "zh-CN projection cannot self-promote candidate")
    check(p.get("source_semantic_version") == "v0.3.7-candidate.0", "zh-CN projection binds to candidate identity")
    check(p.get("machine_artifact_policy", {}).get("translate_machine_reference_files_one_by_one") is False, "zh-CN does not fork machine canonical bytes")
    fixtures = load_yaml(ROOT / "language-projections" / "semantic-fixtures.v3.yaml")
    cases = fixtures.get("cases", [])
    declared = set(fixtures.get("coverage", {}).get("routes_expected", []))
    actual = {case.get("expected_route") for case in cases}
    check(bool(cases), "paired operational fixture corpus exists")
    check(declared == actual, "fixture declared routes equal represented routes")
    check(actual <= route_ids(OP / "HOW-MAP.md"), "every fixture route exists in HOW map")
    for case in cases:
        check(bool(str(case.get("en", "")).strip()), f"{case.get('id')} has English scenario")
        check(bool(str(case.get("zh-CN", "")).strip()), f"{case.get('id')} has zh-CN scenario")
        check(bool(case.get("expected_properties")), f"{case.get('id')} has expected decision properties")
    boundary = "\n".join(str(x) for x in fixtures.get("evidence_boundary", []))
    check("cardinality is open" in boundary.lower(), "fixture count remains an open corpus fact")


def attack_v2_migration_boundaries() -> None:
    try:
        mod = load_v2_helper()
        source = mod.build_latent_record("author-supported-source", "A bounded source experiment improves quality.", "Synthetic source-only improvement.", variation_space="sandbox")
        source["lifecycle_state"] = "EXPERIMENTED"
        source["experiments"] = [{"experiment_id":"exp-supported","time":"2026-08-27T00:10:00Z","provenance":"LOCAL","variation_space":"sandbox","actual_change":"synthetic source-only improvement"}]
        source["selection_state"] = "SUPPORTED"
        source["evaluations"] = [{"evaluation_id":"eval-supported","time":"2026-08-27T00:11:00Z","provenance":"LOCAL","outcomes":{"quality":"IMPROVED"},"selection":"SUPPORTED","evidence_refs":["trace:source-supported"],"negative_evidence":[]}]
        check(not mod.validate_record_v2(source), "synthetic supported source is represented-consistent")
        packet = mod.export_packet_v2(source)
        check(packet["packet_purpose"] == "ADAPTATION_CANDIDATE", "SUPPORTED source exports as adaptation candidate")
        check(packet["source_selection_state"] == "SUPPORTED", "packet preserves source selection")
        check(packet["source_authentication"] == "NOT_AUTHENTICATED_BY_THIS_PACKET", "packet digest does not authenticate source")
        imported = mod.import_packet_v2(packet, "author-receiver")
        check(imported["origin"] == "MIGRATION_CANDIDATE", "receiver stays migration candidate")
        check(imported["selection_state"] == "UNASSESSED", "source selection does not become receiver selection")
        check(imported["expression_state"] == "LATENT", "import does not silently express adaptation")
        check(imported["variation_space"] is None, "import does not force early Variation Space")
        check(imported["migration"]["source_selection_state"] == "SUPPORTED", "source selection is preserved separately")
        check(imported["migration"]["transfer_status"] == "TRANSFERRED_NOT_LOCALLY_VALIDATED", "receiver transfer remains not locally validated")
        laundered = copy.deepcopy(imported); laundered["selection_state"] = "SUPPORTED"
        check(bool(mod.validate_record_v2(laundered)), "validator rejects receiver selection laundering without local evidence")
        tampered = copy.deepcopy(packet); tampered["change"] = "changed after digest"
        check(bool(mod.validate_packet_v2(tampered)), "packet digest detects post-export tampering")
    except Exception as exc:
        failures.append(f"v2 migration attack raised unexpected exception: {exc!r}")


def attack_legacy_relocation() -> None:
    tools = ROOT / "tools"; legacy = tools / "legacy"
    check(not (tools / "ena_evolve.py").exists(), "old v1.2 tool is absent from primary tools path")
    check(not (tools / "candidate1_adversarial.py").exists(), "old candidate1 v1.2 probe is absent from primary tools path")
    check(not (tools / "candidate2_adversarial.py").exists(), "old candidate2 v1.2 probe is absent from primary tools path")
    check((legacy / "ena_evolve_v1_2.py").is_file(), "legacy v1.2 tool exists")
    check((legacy / "candidate1_adversarial_v1_2.py").is_file(), "legacy candidate1 regression is colocated")
    check((legacy / "candidate2_adversarial_v1_2.py").is_file(), "legacy candidate2 regression is colocated")
    for name in ("candidate1_adversarial_v1_2.py", "candidate2_adversarial_v1_2.py"):
        text = (legacy / name).read_text(encoding="utf-8")
        check('TOOL = HERE / "ena_evolve_v1_2.py"' in text, f"{name} points to explicit legacy tool")


def main() -> None:
    attack_candidate_state(); attack_route_graph(); attack_optionality_and_host_diversity()
    attack_false_block_escape_routes(); attack_language_projection(); attack_v2_migration_boundaries(); attack_legacy_relocation()
    if failures:
        print("AUTHOR_ATTACK_VERDICT=FAIL"); print(f"observed_pass_conditions={len(passes)}"); print(f"failures={len(failures)}")
        for item in failures: print(f"FAIL: {item}")
        raise SystemExit(1)
    print("AUTHOR_ATTACK_VERDICT=PASS")
    print(f"observed_pass_conditions={len(passes)}")
    print("attack_cardinality=OPEN")
    print("oracle_style=STRUCTURED_CURRENT_STATE_PLUS_DECISION_BOUNDARIES")
    print("evidence_scope=AUTHOR_SIDE_DETERMINISTIC_AND_REPRESENTED_SEMANTIC_ATTACKS_ONLY")
    print("independent_semantic_support=NOT_ESTABLISHED")
    print("external_truth=NOT_ESTABLISHED")


if __name__ == "__main__":
    main()
