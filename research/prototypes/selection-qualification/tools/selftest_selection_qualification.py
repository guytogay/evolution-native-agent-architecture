#!/usr/bin/env python3
"""Portable adversarial/composition selftest for Selection Qualification."""

from __future__ import annotations

import copy
import importlib.util
from pathlib import Path
import subprocess
import sys

from validate_selection_qualification import load_jsonl, resolve_case


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def by_id(rows: list[dict], case_id: str) -> dict:
    for row in rows:
        if row.get("case_id") == case_id:
            return copy.deepcopy(row)
    raise KeyError(case_id)


def load_current_validator(repo_root: Path):
    path = repo_root / "releases" / "current" / "tools" / "validate_evolution_record_v2.py"
    spec = importlib.util.spec_from_file_location("current_evolution_v2_for_selection_qualification", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load Current evolution validator: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def make_supported_current_record(current) -> dict:
    base = current.load_json(current.TEMPLATE_PATH)
    record = current.exp_record(base)
    record["selection_state"] = "SUPPORTED"
    record["evaluations"] = [{
        "evaluation_id": "eval-sq-supported",
        "time": "2026-08-26T01:00:00Z",
        "outcomes": {"quality": "IMPROVED"},
        "selection": "SUPPORTED",
        "evidence_refs": ["trace:sq-supported"],
        "provenance": "LOCAL",
    }]
    return record


def make_harmful_current_record(current) -> dict:
    base = current.load_json(current.TEMPLATE_PATH)
    record = current.exp_record(base)
    record["selection_state"] = "HARMFUL"
    record["evaluations"] = [{
        "evaluation_id": "eval-sq-harmful",
        "time": "2026-08-26T01:00:00Z",
        "outcomes": {"quality": "DEGRADED"},
        "selection": "HARMFUL",
        "evidence_refs": ["trace:sq-harmful"],
        "provenance": "LOCAL",
    }]
    return record


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    repo_root = Path(__file__).resolve().parents[4]
    validator = root / "tools" / "validate_selection_qualification.py"
    fixtures_path = root / "fixtures" / "selection-qualification-cases.jsonl"

    proc = subprocess.run(
        [sys.executable, str(validator), "--cases", str(fixtures_path)],
        text=True,
        capture_output=True,
    )
    print(proc.stdout, end="")
    if proc.stderr:
        print(proc.stderr, end="", file=sys.stderr)
    require(proc.returncode == 0, "authored Selection Qualification corpus does not match resolver")

    rows = load_jsonl(fixtures_path)
    require(bool(rows), "fixture corpus must not be empty")
    ids = [row.get("case_id") for row in rows]
    require(len(ids) == len(set(ids)), "fixture case IDs must be unique")

    # These are regression dependencies, not a total fixture cardinality assertion.
    required_regressions = {
        "SQ-001",  # no ceremony for UNASSESSED
        "SQ-002",  # positive scope-free verdict
        "SQ-003",  # direct scope
        "SQ-004",  # referenced scope
        "SQ-005",  # honest unknown
        "SQ-007",  # negative symmetry
        "SQ-011",  # receiver scope cannot qualify source
        "SQ-014",  # source scope may remain explicit unknown
        "SQ-015",  # represented placeholder boundary
    }
    require(required_regressions <= set(ids), "targeted selection-qualification regression removed")

    current = load_current_validator(repo_root)

    # Reproduce #81 against exact Current semantics: Current v2 accepts a
    # represented evidence-backed positive selection while environment remains {}.
    supported = make_supported_current_record(current)
    require(supported["environment"] == {}, "Current template control no longer has empty environment")
    current_errors = current.validate_record(supported)
    require(not current_errors, f"#81 Current reachability changed unexpectedly: {current_errors}")
    print("PASS: Current v2 still accepts evidence-backed SUPPORTED with environment={}")

    # The overlay does not rewrite the old record as invalid; it narrows the
    # durable qualification claim instead.
    result = resolve_case({"record": supported})
    require(result["local_resolution"] == "UNQUALIFIED_SELECTION", f"scope-free positive verdict escaped: {result}")
    print("PASS: legacy structurally valid record no longer looks scope-qualified")

    # Honest uncertainty is a valid resolution, not a false-BLOCK.
    result = resolve_case({
        "record": supported,
        "selection_qualification": {
            "status": "UNKNOWN",
            "note": "historical material environment was not preserved",
        },
    })
    require(result["local_resolution"] == "QUALIFICATION_UNKNOWN", f"honest unknown blocked: {result}")
    print("PASS: explicit unknown qualification preserves verdict without manufacturing scope")

    # Direct represented scope qualifies without requiring a new overlay.
    direct = copy.deepcopy(supported)
    direct["environment"] = {"host": "H1", "configuration": "cfg-A"}
    require(not current.validate_record(direct), "Current direct-scope control became structurally invalid")
    result = resolve_case({"record": direct})
    require(result["local_resolution"] == "QUALIFIED_DIRECT", f"direct scope not recognized: {result}")
    print("PASS: direct represented environment qualifies without extra ceremony")

    # Scope may be carried by represented references rather than duplicated into
    # the environment object.
    result = resolve_case({
        "record": supported,
        "selection_qualification": {
            "status": "SCOPED",
            "scope_basis_refs": ["evaluation:eval-sq-supported:scope"],
        },
    })
    require(result["local_resolution"] == "QUALIFIED_REFERENCED", f"referenced qualification failed: {result}")
    print("PASS: referenced scope basis avoids mandatory environment duplication")

    # Negative verdict symmetry: Current can also accept a local HARMFUL verdict
    # with empty environment, and the qualification layer must not turn that
    # into a scope-free prohibition.
    harmful = make_harmful_current_record(current)
    require(harmful["environment"] == {}, "harmful control unexpectedly scoped")
    require(not current.validate_record(harmful), "Current HARMFUL empty-scope control became invalid")
    result = resolve_case({"record": harmful})
    require(result["local_resolution"] == "UNQUALIFIED_SELECTION", f"scope-free negative verdict escaped: {result}")
    print("PASS: local negative verdict does not become a scope-free prohibition")

    # Mutation: a formerly directly qualified result loses its only represented
    # direct scope; qualification must downgrade rather than silently survive.
    lost_scope = copy.deepcopy(direct)
    lost_scope["environment"] = {}
    result = resolve_case({"record": lost_scope})
    require(result["local_resolution"] == "UNQUALIFIED_SELECTION", f"scope-loss mutation escaped: {result}")
    print("PASS: deleting represented selection scope downgrades qualification")

    # Source and receiver/local scope are independent subjects.
    source_gap = by_id(rows, "SQ-011")["case"]
    result = resolve_case(source_gap)
    require(result["local_resolution"] == "QUALIFIED_DIRECT", "receiver/local control should be qualified")
    require(result["source_resolution"] == "UNQUALIFIED_SELECTION", "receiver scope incorrectly qualified source history")
    print("PASS: receiver/local scope cannot launder source selection qualification")

    source_unknown = by_id(rows, "SQ-014")["case"]
    result = resolve_case(source_unknown)
    require(result["source_resolution"] == "QUALIFICATION_UNKNOWN", "explicit source unknown was not preserved")
    print("PASS: migration may preserve source qualification as explicit unknown")

    # A meaningless-looking placeholder is still only represented data. The
    # generic machine cannot infer that it is semantically complete or fake.
    placeholder = by_id(rows, "SQ-015")["case"]
    result = resolve_case(placeholder)
    require(result["local_resolution"] == "QUALIFIED_DIRECT", "represented placeholder control unexpectedly rejected")
    print("PASS: represented direct scope is accepted without pretending external completeness")

    print("PASS: selection-qualification portable adversarial/composition selftest")
    print("verification_scope=REPRESENTED_SELECTION_QUALIFICATION_PLUS_CURRENT_V2_COMPOSITION_ONLY")
    print("current_v2_acceptance_of_empty_environment_supported=CONFIRMED")
    print("external_scope_completeness=UNPROVEN")
    print("selection_truth=UNPROVEN")
    print("scope_basis_reference_authenticity=UNPROVEN")
    print("source_selection_is_receiver_local_proof=FALSE")
    print("fixture_cardinality=OPEN_WITH_TARGETED_REGRESSION_DEPENDENCIES")
    print("current_change=NO")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
