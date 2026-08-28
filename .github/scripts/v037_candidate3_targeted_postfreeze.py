#!/usr/bin/env python3
"""Targeted post-freeze revalidation for frozen ENA v0.3.7 candidate.3.

This deliberately replays the six material candidate.2 Phase-B repair classes
against the exact frozen candidate.3 bytes. It is prior-falsifier/project-side
repair verification, NOT a fresh search-space-independent A-S/A-P cycle.
"""
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
from typing import Any

import yaml

FROZEN_SOURCE = "b7e88d7adb70396bd671ca97066daf2c120e0adc"
FROZEN_TREE = "e3a9a20d16cecd78df7f32f19fca56e21159e810"
CURRENT_TREE = "7dcbb3934883ffa6cc5292a662588cafc1533cff"
PREDECESSOR_SOURCE = "bda470e0a6b170cec61225a905957a501454a2fe"
PREDECESSOR_TREE = "d5fefc8c786d7e40b3e9a59211ee7045bccee5bf"


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


def closure_authority(root: Path) -> int:
    mod = load_module("postfreeze_authority", root / "tools/validate_contracts.py")
    corpus = json.loads((root / "tools/contract-fixtures.v2.1.json").read_text(encoding="utf-8"))
    base = copy.deepcopy(next(c for c in corpus["cases"] if c["id"] == "P25")["input"])

    def result(payload: dict) -> dict:
        return mod.validate_case(payload)

    checks = 0
    assert result(copy.deepcopy(base))["verdict"] == "OK"; checks += 1

    variants: list[tuple[str, dict, str]] = []
    p = copy.deepcopy(base); p["authority_registry"]["g1"].update(status="REVOKED", revoked_at="2025-12-31"); variants.append(("revoked", p, "BLOCK"))
    p = copy.deepcopy(base); p["authority_registry"]["g1"].update(status="ACTIVE", valid_from="2027-01-01"); variants.append(("not-yet-valid", p, "BLOCK"))
    p = copy.deepcopy(base); p["authority_registry"]["g1"].update(status="ACTIVE", valid_from="2025-01-01", allowed_actions=["other"]); variants.append(("action", p, "BLOCK"))
    p = copy.deepcopy(base); p["authority_registry"]["g1"].update(status="ACTIVE", valid_from="2025-01-01", host_scopes=["other"]); variants.append(("host", p, "BLOCK"))
    p = copy.deepcopy(base); p["authority_registry"]["g1"].update(status="ACTIVE", valid_from="2025-01-01", protected_subject_refs=["subject:X"]); p["binding"]["protected_subject_ref"]="subject:Y"; variants.append(("subject", p, "BLOCK"))
    p = copy.deepcopy(base); p["authority_registry"]["g1"].update(status="ACTIVE", valid_from="2025-01-01", task_scopes=["task:X"]); p["binding"]["task_scope"]="task:Y"; variants.append(("task", p, "BLOCK"))
    p = copy.deepcopy(base); p["authority_registry"]["g1"].update(status="ACTIVE", valid_from="2025-01-01", grantee_epoch_scopes=["epoch:X"]); p["binding"]["grantee_epoch"]="epoch:Y"; variants.append(("epoch", p, "BLOCK"))
    p = copy.deepcopy(base); p["authority_registry"]["g1"].update(status="ACTIVE", valid_from="2025-01-01", credential_ref="cred:X"); p["binding"]["credential_ref"]="cred:Y"; variants.append(("credential", p, "BLOCK"))
    p = copy.deepcopy(base); p["authority_registry"]["g1"].update(status="ACTIVE", valid_from="2025-01-01", allowed_actions=["env"], host_scopes=["h1"], protected_subject_refs=["*"], task_scopes=["*"], grantee_epoch_scopes=["*"], credential_ref="cred:X"); p["binding"]["credential_ref"]="cred:X"; variants.append(("rich-valid", p, "OK"))

    for name, payload, expected in variants:
        actual = result(payload)
        assert actual["verdict"] == expected, (name, expected, actual)
        checks += 1
    print("POSTFREEZE_A_S_01_AUTHORITY=CLOSED", checks)
    return checks


def closure_effect(root: Path) -> int:
    mod = load_module("postfreeze_effect", root / "references/general/effect-lifecycle/tools/validate_effect_lifecycle.py")
    rows = [json.loads(line) for line in (root / "references/general/effect-lifecycle/fixtures/effect-lifecycle-cases.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
    by = {r["case_id"]: r for r in rows}
    checks = 0
    for cid in ["EL-C3-01", "EL-C3-02"]:
        errors = mod.validate_record(by[cid]["record"])
        assert errors, (cid, errors)
        assert mod.next_action(by[cid]["record"], errors) == "REJECT_INCONSISTENT_RECORD"
        checks += 1
    errors = mod.validate_record(by["EL-020"]["record"])
    assert not errors, errors
    assert mod.next_action(by["EL-020"]["record"], errors) == "NO_EFFECT_NEEDED"
    checks += 1
    print("POSTFREEZE_A_S_02_EFFECT=CLOSED", checks)
    return checks


def _source_supported_record(rv, root: Path) -> dict:
    base = json.loads((root / "templates/evolution-record.v2.json").read_text(encoding="utf-8"))
    base["created_at"] = "2026-08-28T00:00:00Z"
    base["origin"] = "MIGRATION_CANDIDATE"
    base["source_candidate_id"] = "source-A"
    base["source_packet_sha256"] = "a" * 64
    base["migration"] = {
        "source_candidate_id": "source-A",
        "source_selection_state": "SUPPORTED",
        "source_lifecycle_state": "INTEGRATED",
        "packet_purpose": "ADAPTATION_CANDIDATE",
        "transfer_status": "TRANSFERRED_NOT_LOCALLY_VALIDATED",
        "source_authentication": "NOT_AUTHENTICATED_BY_THIS_PACKET",
        "packet_sha256": "a" * 64,
        "source_negative_lineage_refs": [],
        "source_experiments": [{
            "experiment_id": "source-exp-1", "time": "2026-08-20T00:00:00Z",
            "actual_change": "source test", "provenance": "LOCAL",
        }],
        "source_evaluations": [{
            "evaluation_id": "source-eval-1", "time": "2026-08-20T01:00:00Z",
            "outcomes": {"quality": "IMPROVED"}, "selection": "SUPPORTED",
            "evidence_refs": ["source:trace"], "provenance": "LOCAL",
        }],
        "source_integration_history": [{
            "integration_id": "source-int-1", "time": "2026-08-20T02:00:00Z",
            "target": "source-runtime", "result": "COMMITTED",
            "selection_state_at_commit": "SUPPORTED",
        }],
    }
    return base


def closure_migration(root: Path) -> int:
    rv = load_module("postfreeze_record", root / "tools/validate_evolution_record_v2.py")
    valid = _source_supported_record(rv, root)
    assert valid["selection_state"] == "UNASSESSED"
    assert not rv.validate_record(valid), rv.validate_record(valid)
    checks = 1

    early = copy.deepcopy(valid)
    early["migration"]["source_integration_history"][0]["time"] = "2026-08-19T23:00:00Z"
    assert rv.validate_record(early); checks += 1

    bad_selection = copy.deepcopy(valid)
    bad_selection["migration"]["source_integration_history"][0]["selection_state_at_commit"] = "UNKNOWN"
    assert rv.validate_record(bad_selection); checks += 1

    bad_expr = copy.deepcopy(valid)
    bad_expr["migration"]["source_expression_history"] = [{
        "expression_id": "source-expr-1", "time": "2026-08-20T01:30:00Z",
        "state": "EXPRESSED", "trigger": "source trigger", "effect_materiality": "NON_MATERIAL",
    }]
    bad_expr["migration"]["source_integration_history"][0]["expression_state_at_commit"] = "LATENT"
    assert rv.validate_record(bad_expr); checks += 1

    print("POSTFREEZE_A_S_03_MIGRATION=CLOSED", checks)
    return checks


def closure_regression_provenance(root: Path) -> int:
    suite = (root / "tools/regression_suite.py").read_text(encoding="utf-8")
    results = json.loads((root / "tools/regression-results-v033.json").read_text(encoding="utf-8"))
    checks = 0
    assert "candidate-local `validate_contracts.py`" in suite; checks += 1
    assert '"implementation_surface": "releases/v0.3.7-candidate/tools/validate_contracts.py"' in suite; checks += 1
    assert results["implementation_surface"] == "releases/v0.3.7-candidate/tools/validate_contracts.py"; checks += 1
    assert "candidate-local successor validator" in results["implementation_lineage"]; checks += 1
    assert results["inherited_v2"] == {"total": 164, "passed": 164}; checks += 1
    assert results["closure_v21"] == {"total": 61, "passed": 61}; checks += 1
    print("POSTFREEZE_A_P_02_REGRESSION_PROVENANCE=CLOSED", checks)
    return checks


def closure_lineage_package(root: Path) -> int:
    checks = 0
    readme = (root / "README.md").read_text(encoding="utf-8")
    assert readme.startswith("# ENA v0.3.7 candidate.3"); checks += 1
    assert "Exact candidate.3 birth base / predecessor frozen source" in readme; checks += 1
    assert f"`{PREDECESSOR_SOURCE}`" in readme; checks += 1
    assert "Correct candidate birth base:" not in readme; checks += 1

    lineage = (root / "LINEAGE.md").read_text(encoding="utf-8")
    assert lineage.startswith("# ENA v0.3.7 candidate.3 Lineage"); checks += 1
    assert "## Candidate.3 succession" in lineage; checks += 1
    assert "## Preserved predecessor candidate.2 lineage" in lineage; checks += 1

    changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8")
    assert changelog.startswith("## v0.3.7 candidate.3"); checks += 1
    assert "## v0.3.7 candidate.2 — FROZEN / NEEDS_REVISION" in changelog; checks += 1

    discipline = (root / "08-RELEASE-DISCIPLINE.md").read_text(encoding="utf-8")
    assert discipline.startswith("# 8. Release and Canonical-Lineage Discipline — v0.3.7 candidate.3"); checks += 1
    assert "historical candidate.0 pre-freeze point" in discipline; checks += 1
    assert "candidate.4 is not an automatic validation step" in discipline; checks += 1
    print("POSTFREEZE_A_P_03_PACKAGE_LINEAGE=CLOSED", checks)
    return checks


def closure_zh(root: Path) -> int:
    manifest = load_yaml(root / "language-projections/zh-CN/projection-manifest.yaml")
    checks = 0
    assert manifest["projection_version"] == "v0.3.7-candidate.3.zh-CN.1"; checks += 1
    assert manifest["source_semantic_version"] == "v0.3.7-candidate.3"; checks += 1
    gaps = " ".join(map(str, manifest.get("known_gaps", [])))
    assert "still require candidate identity/status reconciliation before freeze" not in gaps; checks += 1
    assert "identity/status-bearing zh-CN surfaces are reconciled to candidate.3" in gaps; checks += 1
    assert manifest["not_current"] is True; checks += 1
    print("POSTFREEZE_A_P_04_ZH_STATUS=CLOSED", checks)
    return checks


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, required=True)
    args = parser.parse_args()
    repo = args.repo.resolve()
    root = repo / "releases/v0.3.7-candidate"
    assert root.is_dir()

    counts = {
        "authority": closure_authority(root),
        "effect": closure_effect(root),
        "migration": closure_migration(root),
        "regression_provenance": closure_regression_provenance(root),
        "package_lineage": closure_lineage_package(root),
        "zh_status": closure_zh(root),
    }
    print("CANDIDATE3_TARGETED_POSTFREEZE_REVALIDATION=PASS")
    print("frozen_source=" + FROZEN_SOURCE)
    print("frozen_tree=" + FROZEN_TREE)
    print("current_tree=" + CURRENT_TREE)
    print("closure_counts=" + json.dumps(counts, sort_keys=True))
    print("review_mode=TARGETED_PRIOR_FALSIFIER_REVALIDATION_NOT_FRESH_A_S_A_P")
    print("attack_cardinality=OPEN")
    print("external_truth=NOT_ESTABLISHED")
    print("release_authority=NOT_ASSIGNED_BY_THIS_SCRIPT")


if __name__ == "__main__":
    main()
