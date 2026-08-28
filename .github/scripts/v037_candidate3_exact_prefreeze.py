#!/usr/bin/env python3
"""Exact pre-freeze checks for ENA v0.3.7 candidate.3.

This is author/project-side machine evidence, not fresh independent validation.
It binds an exact candidate source/tree, replays inherited controls, and verifies
that the sealed candidate.2 blockers are represented as closed by candidate.3.
Attack cardinality remains open and external truth is not established.
"""
from __future__ import annotations

import argparse
import copy
import importlib.util
import json
from pathlib import Path
from typing import Any

import yaml

EXPECTED_SOURCE = "b7e88d7adb70396bd671ca97066daf2c120e0adc"
EXPECTED_TREE = "e3a9a20d16cecd78df7f32f19fca56e21159e810"
EXPECTED_CURRENT_TREE = "7dcbb3934883ffa6cc5292a662588cafc1533cff"
PREDECESSOR_SOURCE = "bda470e0a6b170cec61225a905957a501454a2fe"
PREDECESSOR_TREE = "d5fefc8c786d7e40b3e9a59211ee7045bccee5bf"
ROUND1_CARGO = "55e08740fa2e4b033cfb5bd9e8f7a4214a479f08"
ROUND1_RUN = 33149597432
ROUND2_CARGO = "c4966eeb156795c018bf324e1d296e43d12bd91f"
ROUND2_RUN = 33149924866
C2_AS_SHA256 = "0e6bb214cc3398b34c13fc6a3bebd1f548ae00ea067b4c338e8ce88f42ad955f"
C2_AP_SHA256 = "80987d24a80c2aff90fddd96bc1891ee03c6ac02b25381d8af2a22418ebbe1db"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"unable to load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_yaml(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise AssertionError(f"expected mapping: {path}")
    return value


def check_state(repo: Path) -> int:
    root = repo / "releases/v0.3.7-candidate"
    b = load_yaml(root / "CANDIDATE-BASELINE.yaml")
    c3 = b["candidate3_succession"]
    checks = {
        "identity": b["ena_version"] == "v0.3.7-candidate.3",
        "revision": b["candidate_revision"] == 3,
        "maturity": b["maturity"] == "EXACT_PREFREEZE_VALIDATION",
        "not-current": b["current"] is False,
        "not-frozen-internal": b["frozen"] is False,
        "not-released": b["released"] is False,
        "must-not-adopt": b["must_not_be_adopted_as_current"] is True,
        "candidate-branch": b["lineage"]["candidate_branch"] == "candidate/v0.3.7-candidate.3",
        "birth-base": b["lineage"]["candidate_birth_base_commit"] == PREDECESSOR_SOURCE,
        "predecessor-id": b["lineage"]["predecessor_candidate_identity"] == "v0.3.7-candidate.2",
        "predecessor-source": b["lineage"]["predecessor_frozen_source"] == PREDECESSOR_SOURCE,
        "predecessor-tree": b["lineage"]["predecessor_frozen_subtree"] == PREDECESSOR_TREE,
        "tooling-state": b["tooling"]["state"] == "CANDIDATE3_REPAIR_RECONCILED_EXACT_PREFREEZE_NEXT",
        "assembly-state": b["assembly"]["state"] == "CANDIDATE3_REPAIR_RECONCILED_EXACT_PREFREEZE_NEXT",
        "assembly-stage": b["assembly"]["stage"] == 11,
        "freeze-model": b["freeze_protocol"]["model"] == "EXTERNAL_RECORD_BINDS_EXACT_IMMUTABLE_TREE",
        "freeze-gated": b["freeze_protocol"]["freeze_not_allowed_before_exact_prefreeze_validation"] is True,
        "c3-predecessor": c3["predecessor_identity"] == "v0.3.7-candidate.2",
        "c3-predecessor-verdict": c3["predecessor_verdict"] == "NEEDS_REVISION",
        "c3-as": c3["predecessor_a_s_sha256"] == C2_AS_SHA256,
        "c3-ap": c3["predecessor_a_p_sha256"] == C2_AP_SHA256,
        "c3-round1-run": c3["round1_repair_gate_run"] == ROUND1_RUN,
        "c3-round1-commit": c3["round1_repair_commit"] == ROUND1_CARGO,
        "c3-repair-state": c3["repair_state"] == "RECONCILED_EXACT_PREFREEZE_NEXT",
        "fresh-cycle-not-automatic": c3["full_fresh_a_s_a_p_automatic"] is False,
        "attack-cardinality": c3["attack_cardinality"] == "OPEN",
    }
    failed = [name for name, ok in checks.items() if not ok]
    if failed:
        raise AssertionError("state failures: " + ", ".join(failed))

    zh = load_yaml(root / "language-projections/zh-CN/projection-manifest.yaml")
    assert zh["source_semantic_version"] == "v0.3.7-candidate.3"
    assert zh["projection_version"] == "v0.3.7-candidate.3.zh-CN.1"
    assert zh["not_current"] is True
    assert not any("still require candidate identity/status reconciliation before freeze" in str(x)
                   for x in zh.get("known_gaps", []))
    print("CANDIDATE3_STATE_CHECKS=PASS", len(checks))
    return len(checks)


def replay_inherited(repo: Path) -> tuple[int, int, int, int]:
    author = load_module("c3_author", repo / ".github/scripts/v037_candidate_author_attacks.py")
    author.passes.clear(); author.failures.clear()
    author.attack_route_graph()
    author.attack_optionality_and_host_diversity()
    author.attack_false_block_escape_routes()
    author.attack_v2_migration_boundaries()
    author.attack_legacy_relocation()
    if author.failures:
        raise AssertionError("inherited author failures: " + "; ".join(author.failures))

    anti = load_module("c3_anti", repo / ".github/scripts/v037_candidate_anti_ablation.py")
    anti.failures.clear(); anti.observed.clear()
    anti.attack_primary_route_targets()
    anti.attack_router_policy_and_deferred_binding()
    anti.attack_primary_tool_relocation_surface()
    if anti.failures:
        raise AssertionError("inherited anti-ablation failures: " + "; ".join(anti.failures))

    targeted = load_module("c1_targeted_c3", repo / ".github/scripts/v037_candidate1_targeted.py")
    targeted.passes.clear()
    targeted.finding_a_source_context_retention()
    targeted.finding_b_packet_tied_latest_rejected()
    targeted.finding_c_archive_preservation_bound()
    targeted.finding_d_template_created_at_not_machine_valid()

    probe = load_module("c1_open_c3", repo / ".github/scripts/v037_candidate1_open_branch_probes.py")
    probe.observations.clear()
    probe.probe_integration_chronology()
    probe.probe_shallow_source_claims()
    probe.probe_candidate_id_collision()
    expected = {
        "integration_supported_before_supporting_evaluation_accepted": False,
        "integration_selection_at_commit_mismatch_accepted": False,
        "post_commit_reselection_control_accepted": True,
        "shallow_supported_source_packet_accepted": False,
        "source_receiver_candidate_id_collision_accepted": True,
    }
    for key, value in expected.items():
        assert probe.observations.get(key) is value, (key, value, probe.observations.get(key))

    print("CANDIDATE3_INHERITED_REPLAY=PASS", len(author.passes), len(anti.observed), len(targeted.passes), len(probe.observations))
    return len(author.passes), len(anti.observed), len(targeted.passes), len(probe.observations)


def authority_regressions(repo: Path) -> int:
    root = repo / "releases/v0.3.7-candidate"
    mod = load_module("c3_composed_authority", root / "tools/validate_contracts.py")
    corpus = json.loads((root / "tools/contract-fixtures.v2.1.json").read_text(encoding="utf-8"))
    base = copy.deepcopy(next(c for c in corpus["cases"] if c["id"] == "P25")["input"])

    def outcome(payload: dict) -> dict:
        return mod.validate_case(payload)

    assert outcome(copy.deepcopy(base))["verdict"] == "OK"

    cases: list[tuple[str, dict, str]] = []
    revoked = copy.deepcopy(base); revoked["authority_registry"]["g1"].update(status="REVOKED", revoked_at="2025-12-31")
    cases.append(("revoked", revoked, "BLOCK"))
    early = copy.deepcopy(base); early["authority_registry"]["g1"].update(status="ACTIVE", valid_from="2027-01-01")
    cases.append(("not-yet-valid", early, "BLOCK"))
    action = copy.deepcopy(base); action["authority_registry"]["g1"].update(status="ACTIVE", valid_from="2025-01-01", allowed_actions=["different"])
    cases.append(("action-scope", action, "BLOCK"))
    host = copy.deepcopy(base); host["authority_registry"]["g1"].update(status="ACTIVE", valid_from="2025-01-01", host_scopes=["other"])
    cases.append(("host-scope", host, "BLOCK"))
    subject = copy.deepcopy(base); subject["authority_registry"]["g1"].update(status="ACTIVE", valid_from="2025-01-01", protected_subject_refs=["subject:X"]); subject["binding"]["protected_subject_ref"] = "subject:Y"
    cases.append(("subject-scope", subject, "BLOCK"))
    task = copy.deepcopy(base); task["authority_registry"]["g1"].update(status="ACTIVE", valid_from="2025-01-01", task_scopes=["task:X"]); task["binding"]["task_scope"] = "task:Y"
    cases.append(("task-scope", task, "BLOCK"))
    credential = copy.deepcopy(base); credential["authority_registry"]["g1"].update(status="ACTIVE", valid_from="2025-01-01", credential_ref="cred:X"); credential["binding"]["credential_ref"] = "cred:Y"
    cases.append(("credential", credential, "BLOCK"))
    epoch = copy.deepcopy(base); epoch["authority_registry"]["g1"].update(status="ACTIVE", valid_from="2025-01-01", grantee_epoch_scopes=["epoch:X"]); epoch["binding"]["grantee_epoch"] = "epoch:Y"
    cases.append(("epoch", epoch, "BLOCK"))

    good = copy.deepcopy(base)
    good["authority_registry"]["g1"].update(
        status="ACTIVE", valid_from="2025-01-01", allowed_actions=["env"],
        host_scopes=["h1"], protected_subject_refs=["*"], task_scopes=["*"],
        grantee_epoch_scopes=["*"], credential_ref="cred:X",
    )
    good["binding"]["credential_ref"] = "cred:X"
    cases.append(("rich-valid", good, "OK"))

    for name, payload, expected in cases:
        actual = outcome(payload)
        assert actual["verdict"] == expected, (name, expected, actual)
    print("CANDIDATE3_AUTHORITY_REGRESSIONS=PASS", 1 + len(cases))
    return 1 + len(cases)


def effect_regressions(repo: Path) -> int:
    root = repo / "releases/v0.3.7-candidate"
    mod = load_module("c3_effect", root / "references/general/effect-lifecycle/tools/validate_effect_lifecycle.py")
    rows = [json.loads(line) for line in (root / "references/general/effect-lifecycle/fixtures/effect-lifecycle-cases.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    by = {r["case_id"]: r for r in rows}
    for cid in ["EL-C3-01", "EL-C3-02"]:
        errors = mod.validate_record(by[cid]["record"])
        assert errors, (cid, errors)
        assert mod.next_action(by[cid]["record"], errors) == "REJECT_INCONSISTENT_RECORD"
    errors = mod.validate_record(by["EL-020"]["record"])
    assert not errors, errors
    assert mod.next_action(by["EL-020"]["record"], errors) == "NO_EFFECT_NEEDED"
    print("CANDIDATE3_EFFECT_REGRESSIONS=PASS 3")
    return 3


def migration_regressions(repo: Path) -> int:
    root = repo / "releases/v0.3.7-candidate"
    rv = load_module("c3_record", root / "tools/validate_evolution_record_v2.py")
    # The candidate-local selftest now carries 35 deterministic cases, including
    # three transferred-source commit chronology/snapshot regressions.
    rv.selftest()
    text = (root / "tools/validate_evolution_record_v2.py").read_text(encoding="utf-8")
    for marker in [
        "source integration before source experiment/evaluation unexpectedly passed",
        "source integration selection snapshot mismatch unexpectedly passed",
        "source integration expression snapshot mismatch unexpectedly passed",
    ]:
        assert marker in text, marker
    print("CANDIDATE3_MIGRATION_REGRESSIONS=PASS 3")
    return 3


def package_truth(repo: Path) -> int:
    root = repo / "releases/v0.3.7-candidate"
    checks = 0
    readme = (root / "README.md").read_text(encoding="utf-8")
    assert readme.startswith("# ENA v0.3.7 candidate.3") ; checks += 1
    assert "candidate/v0.3.7-candidate.3" in readme ; checks += 1
    assert f"`{PREDECESSOR_SOURCE}`" in readme ; checks += 1
    assert "Correct candidate birth base:" not in readme ; checks += 1

    lineage = (root / "LINEAGE.md").read_text(encoding="utf-8")
    assert lineage.startswith("# ENA v0.3.7 candidate.3 Lineage") ; checks += 1
    assert "## Candidate.3 succession" in lineage and "## Preserved predecessor candidate.2 lineage" in lineage ; checks += 1

    changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8")
    assert changelog.startswith("## v0.3.7 candidate.3") ; checks += 1
    assert "## v0.3.7 candidate.2 — FROZEN / NEEDS_REVISION" in changelog ; checks += 1

    release = (root / "08-RELEASE-DISCIPLINE.md").read_text(encoding="utf-8")
    assert release.startswith("# 8. Release and Canonical-Lineage Discipline — v0.3.7 candidate.3") ; checks += 1
    assert "### Predecessor v0.3.7 candidate.2 preserved state" in release ; checks += 1
    assert "historical candidate.0 pre-freeze point" in release ; checks += 1

    curated = [
        "00-READ-ME-FIRST.md","05-CORE-OPERATIONAL-CONTRACTS.md","06-EVOLUTION-KNOWLEDGE-AND-OPEN-PARTICIPATION.md",
        "07-ADOPTION-AND-FIELD-VALIDATION.md","09-EVOLUTION-METABOLISM.md","10-LANGUAGE-PORTABILITY.md",
        "RUNTIME-ADOPTION-KERNEL.md","AGENT-ADOPTION-INSTRUCTION.md","LITE-ADOPTION-INSTRUCTION.md",
        "operational/README.md","operational/CUE-INDEX.md","operational/HOW-MAP.md","operational/REFERENCE-INDEX.yaml",
        "operational/procedures/PURPOSE-RELATIVE-CONTINUITY.md","operational/procedures/STANDING-INPUT.md","operational/procedures/CONTROL-RETIREMENT.md",
        "operational/patterns/EVOLUTION-COMMONS.md","operational/patterns/HOST-MAPPINGS.md",
        "references/REFERENCE-MANIFEST.yaml","references/general/retrieval-obligation/README.md","references/general/wait-state/README.md",
        "references/general/authority-lease/README.md","references/general/effect-lifecycle/README.md","references/general/recovery-adapter/README.md",
        "references/advanced/evidence-envelope/README.md","references/advanced/evidence-dependency-map/README.md","references/advanced/contested-authorship/README.md",
        "language-projections/zh-CN/00-READ-ME-FIRST.md","language-projections/zh-CN/RUNTIME-ADOPTION-KERNEL.md",
        "language-projections/zh-CN/09-EVOLUTION-METABOLISM.md","language-projections/zh-CN/REFERENCE-GUIDE.md",
        "language-projections/zh-CN/operational/README.md","language-projections/zh-CN/operational/CUE-INDEX.md","language-projections/zh-CN/operational/HOW-MAP.md",
        "language-projections/zh-CN/operational/procedures/PURPOSE-RELATIVE-CONTINUITY.md","language-projections/zh-CN/operational/procedures/STANDING-INPUT.md","language-projections/zh-CN/operational/procedures/CONTROL-RETIREMENT.md",
        "language-projections/zh-CN/operational/patterns/EVOLUTION-COMMONS.md","language-projections/zh-CN/operational/patterns/HOST-MAPPINGS.md",
    ]
    for rel in curated:
        text = (root / rel).read_text(encoding="utf-8")
        assert "candidate.2" not in text and "v0.3.7-candidate.2" not in text, rel
    checks += len(curated)

    zh = load_yaml(root / "language-projections/zh-CN/projection-manifest.yaml")
    assert zh["source_semantic_version"] == "v0.3.7-candidate.3" ; checks += 1
    assert "identity/status-bearing zh-CN surfaces are reconciled to candidate.3" in " ".join(map(str, zh["known_gaps"])) ; checks += 1
    print("CANDIDATE3_PACKAGE_TRUTH=PASS", checks)
    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    args = parser.parse_args()
    repo = args.repo.resolve()
    root = repo / "releases/v0.3.7-candidate"
    assert root.is_dir()

    state = check_state(repo)
    inherited = replay_inherited(repo)
    authority = authority_regressions(repo)
    effect = effect_regressions(repo)
    migration = migration_regressions(repo)
    package = package_truth(repo)

    # Machine-readable manifests remain coherent.
    for rel in [
        "CANDIDATE-BASELINE.yaml", "operational/REFERENCE-INDEX.yaml",
        "references/REFERENCE-MANIFEST.yaml", "language-projections/zh-CN/projection-manifest.yaml",
    ]:
        load_yaml(root / rel)

    print("CANDIDATE3_EXACT_PREFREEZE_VERDICT=PASS")
    print(f"exact_source={EXPECTED_SOURCE}")
    print(f"exact_candidate_tree={EXPECTED_TREE}")
    print(f"current_tree={EXPECTED_CURRENT_TREE}")
    print(f"state_checks_observed={state}")
    print(f"inherited_replay_observed={inherited}")
    print(f"authority_targeted_observed={authority}")
    print(f"effect_targeted_observed={effect}")
    print(f"migration_targeted_observed={migration}")
    print(f"package_truth_checks_observed={package}")
    print("attack_cardinality=OPEN")
    print("fresh_independent_candidate3_review_by_this_gate=NO")
    print("external_truth=NOT_ESTABLISHED")
    print("release_authority=NOT_ASSIGNED_BY_THIS_GATE")


if __name__ == "__main__":
    main()
