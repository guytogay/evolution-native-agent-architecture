#!/usr/bin/env python3
"""Lightweight pre-freeze validator for ENA v0.3.6 working candidate.

This validator checks represented candidate identity, structural consistency,
semantic-fixture completeness, and inherited baseline preservation. It does not
prove external evidence, moral correctness, future salience, or ecological fitness.
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
    baseline_path = ROOT / "CANDIDATE-BASELINE.yaml"
    require(baseline_path.is_file(), "missing CANDIDATE-BASELINE.yaml")
    require(not (ROOT / "CURRENT-BASELINE.yaml").exists(), "candidate must not carry CURRENT-BASELINE.yaml")
    doc = load_yaml(baseline_path)
    require(doc["ena_version"] == "v0.3.6-candidate", "wrong candidate version")
    require(doc["adoption_status"] == "WORKING_CANDIDATE", "candidate status must remain WORKING_CANDIDATE")
    require(doc["current"] is False, "candidate cannot claim current=true")
    require(doc["frozen"] is False, "working candidate cannot claim frozen=true")
    require(doc["released"] is False, "working candidate cannot claim released=true")
    require(doc["must_not_be_adopted_as_current"] is True, "missing do-not-adopt boundary")
    require(doc["constitution"]["inherited_stable_ids"] == 38, "unexpected inherited Constitution count")
    require(doc["constitution"]["new_ids_added_in_current_working_candidate"] == 0, "unexpected new Constitution IDs")
    require(doc["evolution"]["evolution_record_schema"] == "schemas/evolution-record.v2.schema.json", "candidate must point to evolution-record v2")
    require(doc["machine_boundary"]["expression_schema_present"] is True, "expression schema boundary missing")
    require(doc["machine_boundary"]["expression_tool_implementation_present"] is False, "must not falsely claim expression tool implementation")
    require(doc["machine_boundary"]["mutation_pressure_tool_implementation_present"] is False, "must not falsely claim mutation-pressure tool implementation")
    print("candidate-identity-pass")


def check_current_untouched() -> None:
    actual = subprocess.check_output(
        ["git", "rev-parse", "HEAD:releases/current"], cwd=REPO, text=True
    ).strip()
    require(actual == EXPECTED_CURRENT_TREE, f"releases/current tree changed: {actual}")
    current = load_yaml(REPO / "releases/current/CURRENT-BASELINE.yaml")
    require(current["ena_version"] == "v0.3.5", "Current version unexpectedly changed")
    require(current["current"] is True, "Current pointer unexpectedly not current")
    print("current-tree-preserved-pass", actual)


def check_constitution_ids() -> None:
    text = (ROOT / "01-CONSTITUTION.md").read_text(encoding="utf-8")
    ids = sorted(set(re.findall(r"ENA-CON-\d{3}", text)))
    require(len(ids) == 38, f"expected 38 inherited Constitution IDs, got {len(ids)}")
    require(ids[0] == "ENA-CON-001" and ids[-1] == "ENA-CON-038", "unexpected Constitution ID range")
    print("constitution-id-pass", len(ids))


def check_expression_schema() -> None:
    schema_path = ROOT / "schemas/evolution-record.v2.schema.json"
    template_path = ROOT / "templates/evolution-record.v2.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    required = set(schema.get("required", []))
    require("expression_state" in required, "expression_state must be required")
    require("expression_history" in required, "expression_history must be required")
    expr_enum = schema["properties"]["expression_state"]["enum"]
    require(set(expr_enum) == {"LATENT", "EXPRESSED"}, f"bad expression enum: {expr_enum}")
    template = json.loads(template_path.read_text(encoding="utf-8"))
    Draft202012Validator(schema).validate(template)
    require(template["expression_state"] == "LATENT", "template should default to LATENT")
    require(template["selection_state"] == "UNASSESSED", "latent template must not self-select")
    require(template["experiments"] == [], "latent template must not fabricate experiment")
    require(template["evaluations"] == [], "latent template must not fabricate evaluation")
    print("expression-schema-pass")


def check_bilingual_projection() -> None:
    manifest = load_yaml(ROOT / "language-projections/zh-CN/projection-manifest.yaml")
    require(manifest["source_semantic_version"] == "v0.3.6-candidate", "zh-CN manifest bound to wrong semantic version")
    require(manifest["status"] == "WORKING_CANDIDATE_SEMANTIC_PROJECTION", "zh-CN projection must not claim Current")
    require(manifest["not_current"] is True, "zh-CN projection must explicitly remain not Current")
    sets = set(manifest.get("semantic_fixture_sets", []))
    require("../semantic-fixtures.v1.yaml" in sets, "inherited v0.3.5 fixture set missing")
    require("../semantic-fixtures.v2.yaml" in sets, "v0.3.6 fixture set missing")

    fixtures = load_yaml(ROOT / "language-projections/semantic-fixtures.v2.yaml")
    cases = fixtures.get("cases", [])
    require(len(cases) == 8, f"expected 8 new v0.3.6 bilingual fixtures, got {len(cases)}")
    expected_ids = {f"LANG-036-{i:03d}-" for i in range(1, 9)}
    for case in cases:
        cid = case.get("id", "")
        require(any(cid.startswith(prefix) for prefix in expected_ids), f"unexpected fixture id: {cid}")
        require(bool(str(case.get("en", "")).strip()), f"missing English scenario: {cid}")
        require(bool(str(case.get("zh-CN", "")).strip()), f"missing zh-CN scenario: {cid}")
        require(bool(case.get("expected_properties")), f"missing expected properties: {cid}")
    require(len({c["id"] for c in cases}) == len(cases), "duplicate fixture IDs")
    print("bilingual-fixture-structure-pass", len(cases))


def check_semantic_boundaries() -> None:
    metabolism = (ROOT / "09-EVOLUTION-METABOLISM.md").read_text(encoding="utf-8")
    kernel = (ROOT / "RUNTIME-ADOPTION-KERNEL.md").read_text(encoding="utf-8")
    commons = (ROOT / "06-EVOLUTION-KNOWLEDGE-AND-OPEN-PARTICIPATION.md").read_text(encoding="utf-8")
    release = (ROOT / "08-RELEASE-DISCIPLINE.md").read_text(encoding="utf-8")

    required_snippets = {
        "metabolism-stimulus": (metabolism, "stimulus != mutation"),
        "metabolism-storage": (metabolism, "stored != expressed"),
        "metabolism-local": (metabolism, "local selection != universal fitness"),
        "kernel-expression": (kernel, "lifecycle state != expression state != evidence-backed selection state"),
        "kernel-popularity": (kernel, "popularity/propagation != proof"),
        "commons-separation": (commons, "PUBLISH -> DISCOVER -> IMPORT -> EXPRESS/EXPERIMENT -> LOCALLY_SELECT"),
        "commons-sovereign": (commons, "Commons != sovereign"),
        "carrier-boundary": (release, "The semantic requirement is the governed reproducible lineage"),
    }
    for name, (text, snippet) in required_snippets.items():
        require(snippet in text, f"missing semantic boundary {name}: {snippet}")
    print("semantic-boundary-presence-pass", len(required_snippets))


def check_inherited_tool_boundary_and_selftest() -> None:
    tool = (ROOT / "tools/ena_evolve.py").read_text(encoding="utf-8")
    require('STATE_VERSION = "1.2"' in tool, "inherited tool unexpectedly changed state version")
    require("expression_state" not in tool, "machine boundary metadata says expression tool absent, but tool already contains expression_state; reconcile explicitly")
    subprocess.run([sys.executable, str(ROOT / "tools/ena_evolve.py"), "selftest"], cwd=REPO, check=True)
    print("inherited-ena-evolve-selftest-pass")


def main() -> None:
    check_candidate_identity()
    check_current_untouched()
    check_constitution_ids()
    check_expression_schema()
    check_bilingual_projection()
    check_semantic_boundaries()
    check_inherited_tool_boundary_and_selftest()
    print("V036_WORKING_CANDIDATE_PREFREEZE_VALIDATION_PASS")


if __name__ == "__main__":
    main()
