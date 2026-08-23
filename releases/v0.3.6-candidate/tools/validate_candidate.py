#!/usr/bin/env python3
"""Lightweight pre-freeze validator for ENA v0.3.6 working candidate.

Checks represented identity/structure and predecessor preservation only. It does
not prove external truth, future salience, ecological fitness, or acceptance.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

import yaml
from jsonschema.validators import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
EXPECTED_CURRENT_TREE = "9c928b4c99ae72e53c89978cf1d10b7ea068c182"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def check_candidate_identity() -> None:
    doc = load_yaml(ROOT / "CANDIDATE-BASELINE.yaml")
    require(doc["ena_version"] == "v0.3.6-candidate", "wrong candidate version")
    require(doc["adoption_status"] == "WORKING_CANDIDATE", "candidate must remain WORKING_CANDIDATE")
    require(doc["current"] is False and doc["frozen"] is False and doc["released"] is False, "working candidate self-promoted")
    require(doc["must_not_be_adopted_as_current"] is True, "missing do-not-adopt boundary")
    require(not (ROOT / "CURRENT-BASELINE.yaml").exists(), "candidate must not carry CURRENT-BASELINE.yaml")
    require(doc["constitution"]["inherited_stable_ids"] == 38, "unexpected Constitution count")
    require(doc["constitution"]["new_ids_added_in_current_working_candidate"] == 0, "unexpected new Constitution IDs")
    require(doc["evolution"]["evolution_record_schema"] == "schemas/evolution-record.v2.schema.json", "candidate must point to record v2")
    require(doc["evolution"]["field_experience_template"] == "templates/field-experience.v2.yaml", "candidate must point to field template v2")
    require(doc["machine_boundary"]["expression_schema_present"] is True, "expression schema missing")
    require(doc["machine_boundary"]["expression_consistency_validator_present"] is True, "expression consistency validator missing")
    require(doc["machine_boundary"]["expression_tool_implementation_present"] is False, "false expression-tool claim")
    require(doc["machine_boundary"]["mutation_pressure_tool_implementation_present"] is False, "false mutation-pressure tool claim")
    print("candidate-identity-pass")


def check_current_untouched() -> None:
    actual = subprocess.check_output(["git", "rev-parse", "HEAD:releases/current"], cwd=REPO, text=True).strip()
    require(actual == EXPECTED_CURRENT_TREE, f"releases/current tree changed: {actual}")
    current = load_yaml(REPO / "releases/current/CURRENT-BASELINE.yaml")
    require(current["ena_version"] == "v0.3.5" and current["current"] is True, "Current pointer changed")
    print("current-tree-preserved-pass", actual)


def check_constitution_ids() -> None:
    text = (ROOT / "01-CONSTITUTION.md").read_text(encoding="utf-8")
    ids = sorted(set(re.findall(r"ENA-CON-\d{3}", text)))
    require(len(ids) == 38 and ids[0] == "ENA-CON-001" and ids[-1] == "ENA-CON-038", f"bad Constitution IDs: {len(ids)}")
    print("constitution-id-pass", len(ids))


def check_active_file_identity() -> None:
    files = {
        "00": (ROOT / "00-READ-ME-FIRST.md").read_text(encoding="utf-8"),
        "04": (ROOT / "04-CAPABILITY-MAP.md").read_text(encoding="utf-8"),
        "05": (ROOT / "05-CORE-OPERATIONAL-CONTRACTS.md").read_text(encoding="utf-8"),
        "07": (ROOT / "07-ADOPTION-AND-FIELD-VALIDATION.md").read_text(encoding="utf-8"),
        "agent": (ROOT / "AGENT-ADOPTION-INSTRUCTION.md").read_text(encoding="utf-8"),
        "lite": (ROOT / "LITE-ADOPTION-INSTRUCTION.md").read_text(encoding="utf-8"),
        "zh-constitution": (ROOT / "language-projections/zh-CN/01-CONSTITUTION.md").read_text(encoding="utf-8"),
    }
    require("WORKING_CANDIDATE" in files["00"] and "NOT_CURRENT" in files["00"], "candidate entrypoint missing identity warning")
    require("v0.3.5 candidate adds" not in files["04"] and "For v0.3.5 candidate additions" not in files["04"], "capability map leaks predecessor candidate identity")
    require("single active operational-contract surface for the v0.3.5 candidate" not in files["05"], "operational contracts leak predecessor candidate identity")
    require("does not prove the entire v0.3.5 candidate correct" not in files["05"], "operational validator boundary names wrong candidate")
    require("WORKING_CANDIDATE" in files["07"] and "NOT_CURRENT" in files["07"], "candidate evaluation file missing candidate boundary")
    require("Candidate Evaluation" in files["agent"] and "not adoption" in files["agent"].lower(), "agent instruction still behaves like Current adoption")
    require("v0.3.6 Candidate" in files["lite"] and "not an adoption baseline" in files["lite"], "LITE file still behaves like released adoption instruction")
    require("v0.3.6 候选版" in files["zh-constitution"] and "v0.3.5 Current" in files["zh-constitution"], "zh-CN Constitution projection identity is ambiguous")
    print("active-file-identity-pass", len(files))


def check_expression_schema() -> None:
    schema = json.loads((ROOT / "schemas/evolution-record.v2.schema.json").read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    required = set(schema.get("required", []))
    require({"expression_state", "expression_history"}.issubset(required), "expression axis not required")
    require(set(schema["properties"]["expression_state"]["enum"]) == {"LATENT", "EXPRESSED"}, "bad expression enum")
    template = json.loads((ROOT / "templates/evolution-record.v2.json").read_text(encoding="utf-8"))
    Draft202012Validator(schema).validate(template)
    require(template["expression_state"] == "LATENT" and template["selection_state"] == "UNASSESSED", "latent template self-selects/expresses")
    require(template["variation_space"] is None, "latent template should not invent Variation Space")
    require(template["experiments"] == [] and template["evaluations"] == [], "latent template fabricates evidence")
    print("expression-schema-pass")


def check_bilingual_projection() -> None:
    manifest = load_yaml(ROOT / "language-projections/zh-CN/projection-manifest.yaml")
    require(manifest["source_semantic_version"] == "v0.3.6-candidate", "zh-CN bound to wrong semantic version")
    require(manifest["status"] == "WORKING_CANDIDATE_SEMANTIC_PROJECTION" and manifest["not_current"] is True, "zh-CN projection self-promoted")
    sets = set(manifest.get("semantic_fixture_sets", []))
    require({"../semantic-fixtures.v1.yaml", "../semantic-fixtures.v2.yaml"}.issubset(sets), "fixture sets incomplete")
    fixtures = load_yaml(ROOT / "language-projections/semantic-fixtures.v2.yaml")
    cases = fixtures.get("cases", [])
    require(len(cases) == 8, f"expected 8 v036 fixtures, got {len(cases)}")
    for case in cases:
        require(bool(str(case.get("en", "")).strip()), f"missing en: {case.get('id')}")
        require(bool(str(case.get("zh-CN", "")).strip()), f"missing zh-CN: {case.get('id')}")
        require(bool(case.get("expected_properties")), f"missing expectations: {case.get('id')}")
    require(len({c["id"] for c in cases}) == len(cases), "duplicate fixture IDs")
    print("bilingual-fixture-structure-pass", len(cases))


def check_field_templates() -> None:
    legacy_text = (ROOT / "templates/field-experience.v1.yaml").read_text(encoding="utf-8")
    require("v0.3.3" not in legacy_text, "legacy field template still defaults to v0.3.3")
    require("NOT_MAINLINE" not in legacy_text, "legacy field template still uses retired active Mainline wording")
    active = load_yaml(ROOT / "templates/field-experience.v2.yaml")
    require(active["participant"]["ena_semantic_identity"] == "v0.3.6-candidate", "field v2 wrong identity")
    require(active["status"].startswith("UNRECONCILED_CANDIDATE_EVIDENCE"), "field v2 overclaims reconciliation")
    require(active["authority_note"], "field v2 missing authority boundary")
    print("field-template-pass")


def check_semantic_boundaries() -> None:
    metabolism = (ROOT / "09-EVOLUTION-METABOLISM.md").read_text(encoding="utf-8")
    kernel = (ROOT / "RUNTIME-ADOPTION-KERNEL.md").read_text(encoding="utf-8")
    commons = (ROOT / "06-EVOLUTION-KNOWLEDGE-AND-OPEN-PARTICIPATION.md").read_text(encoding="utf-8")
    release = (ROOT / "08-RELEASE-DISCIPLINE.md").read_text(encoding="utf-8")
    checks = [
        (metabolism, "stimulus != mutation"),
        (metabolism, "stored != expressed"),
        (metabolism, "local selection != universal fitness"),
        (kernel, "lifecycle state != expression state != evidence-backed selection state"),
        (kernel, "popularity/propagation != proof"),
        (commons, "PUBLISH -> DISCOVER -> IMPORT -> EXPRESS/EXPERIMENT -> LOCALLY_SELECT"),
        (commons, "only within its legitimate publication authority and consequence boundary"),
        (commons, "Commons != sovereign"),
        (release, "The semantic requirement is the governed reproducible lineage"),
    ]
    for text, snippet in checks:
        require(snippet in text, f"missing semantic boundary: {snippet}")
    print("semantic-boundary-presence-pass", len(checks))


def check_v2_consistency_selftest() -> None:
    subprocess.run([sys.executable, str(ROOT / "tools/validate_evolution_record_v2.py"), "--selftest"], cwd=REPO, check=True)
    print("v2-consistency-selftest-pass")


def check_inherited_tool_boundary_and_selftest() -> None:
    tool = (ROOT / "tools/ena_evolve.py").read_text(encoding="utf-8")
    require('STATE_VERSION = "1.2"' in tool, "inherited tool unexpectedly changed state version")
    require("expression_state" not in tool, "candidate baseline says expression runtime absent; reconcile if tool changes")
    subprocess.run([sys.executable, str(ROOT / "tools/ena_evolve.py"), "selftest"], cwd=REPO, check=True)
    print("inherited-ena-evolve-selftest-pass")


def main() -> None:
    check_candidate_identity()
    check_current_untouched()
    check_constitution_ids()
    check_active_file_identity()
    check_expression_schema()
    check_bilingual_projection()
    check_field_templates()
    check_semantic_boundaries()
    check_v2_consistency_selftest()
    check_inherited_tool_boundary_and_selftest()
    print("V036_WORKING_CANDIDATE_PREFREEZE_VALIDATION_PASS")


if __name__ == "__main__":
    main()
