#!/usr/bin/env python3
"""Structural validator for Naturalistic Memory Validation 0.1.

This validator checks only represented observation discipline.
It does not prove that a failure-stage classification is semantically correct,
that a missed memory really existed, or that retrieval was complete.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent
SCHEMA = ROOT / "field-observation.schema.json"


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def validate_document(doc):
    errors = []
    schema = load(SCHEMA)
    errors += [f"schema: {e.message}" for e in Draft202012Validator(schema).iter_errors(doc)]

    evidence_class = doc.get("evidence_class")
    hot_exposure = (doc.get("host_profile") or {}).get("hot_catalog_exposure")
    if evidence_class in {"PRIMARY_NATURALISTIC", "INDEPENDENT_NATURALISTIC"}:
        if hot_exposure not in {"NONE", "BOUNDED_SUMMARY"}:
            errors.append(
                f"evidence_class: {evidence_class} requires bounded hot catalog exposure, got {hot_exposure}"
            )

    trace = doc.get("retrieval_trace", []) or []
    seqs = [x.get("sequence") for x in trace if isinstance(x, dict)]
    if len(seqs) != len(set(seqs)):
        errors.append("retrieval_trace: sequence values must be unique")
    if seqs and seqs != sorted(seqs):
        errors.append("retrieval_trace: events must be stored in ascending sequence order")

    assessment = doc.get("assessment", {}) or {}
    status = assessment.get("status")
    stage = assessment.get("failure_stage")
    basis = assessment.get("basis_refs", []) or []
    challenges = doc.get("later_challenges", []) or []

    if status == "UNASSESSED":
        if stage != "UNRESOLVED":
            errors.append("assessment: UNASSESSED must use failure_stage=UNRESOLVED")
        if basis:
            errors.append("assessment: UNASSESSED must not assert failure basis refs")

    elif status == "NO_MATERIAL_FAILURE_OBSERVED":
        if stage != "NONE":
            errors.append("assessment: NO_MATERIAL_FAILURE_OBSERVED must use failure_stage=NONE")

    elif status == "MATERIAL_FAILURE_OBSERVED":
        if stage in {None, "NONE", "UNRESOLVED"}:
            errors.append("assessment: MATERIAL_FAILURE_OBSERVED requires a concrete failure stage")
        if not basis:
            errors.append("assessment: MATERIAL_FAILURE_OBSERVED requires basis_refs")
        if not challenges:
            errors.append("assessment: MATERIAL_FAILURE_OBSERVED requires at least one later challenge")
        elif not any(c.get("decision_effect") == "CHANGED_MATERIAL_DECISION" for c in challenges):
            errors.append("assessment: MATERIAL_FAILURE_OBSERVED requires a challenge that changed the material decision")

    elif status == "UNRESOLVED":
        if stage != "UNRESOLVED":
            errors.append("assessment: UNRESOLVED must use failure_stage=UNRESOLVED")
        if not basis and not challenges:
            errors.append("assessment: UNRESOLVED should cite a basis or challenge rather than manufacture uncertainty from nothing")

    utility = doc.get("utility_observation")
    if utility:
        effect = utility.get("decision_effect")
        ubasis = utility.get("basis_refs", []) or []
        if effect in {"CHANGED_MATERIAL_DECISION", "CHANGED_NONMATERIAL_DETAIL"} and not ubasis:
            errors.append("utility_observation: observed decision change requires basis_refs")

    # A trigger miss may legitimately have no retrieval trace. Downstream failure
    # stages ordinarily require some retrieval lifecycle evidence, but the validator
    # does not enforce a complete stage sequence because natural Host traces may be partial.
    if status == "MATERIAL_FAILURE_OBSERVED" and stage != "R0_TRIGGER" and not trace:
        errors.append("assessment: downstream retrieval failure requires at least one retrieval_trace event")

    return errors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    args = ap.parse_args()
    doc = load(args.path)
    errors = validate_document(doc)
    print(json.dumps({
        "valid": not errors,
        "scope": "naturalistic-validation-0.1 represented field-observation discipline only",
        "errors": errors,
    }, indent=2))
    raise SystemExit(0 if not errors else 1)


if __name__ == "__main__":
    main()
