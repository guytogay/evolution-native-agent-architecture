#!/usr/bin/env python3
"""Issue #85 deterministic projection-composition reference evaluator.

This is not a normative ENA validator.
It asks only whether a represented retrieval-sufficiency assessment may transfer
across the represented Decision Projection transformation.

PASS/TRANSFER_OK does not prove semantic fidelity, Host truthfulness, or final
real-world decision correctness.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

PRESERVING = {"EXACT", "PRESERVES_DECISION_EFFECT"}
VALID_FIDELITY = PRESERVING | {"UNKNOWN", "LOSSY"}
VALID_CONSEQUENCE = {"MATERIAL", "NON_MATERIAL"}


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def evaluate_case(case):
    errors = []
    cid = case.get("case_id", "?")
    consequence = case.get("decision_consequence")
    if consequence not in VALID_CONSEQUENCE:
        errors.append(f"{cid}: invalid decision_consequence")

    retrieved = case.get("retrieved_results", [])
    projection = case.get("projection_items", [])
    if not isinstance(retrieved, list) or not isinstance(projection, list):
        return {
            "outcome": "REASSESS_REQUIRED",
            "reasons": [],
            "errors": [f"{cid}: invalid list shape"],
        }

    result_map = {}
    for i, record in enumerate(retrieved):
        ref = record.get("result_ref")
        if not ref:
            errors.append(f"{cid}: retrieved[{i}] missing result_ref")
        elif ref in result_map:
            errors.append(f"{cid}: duplicate result_ref {ref}")
        else:
            result_map[ref] = record
        if not isinstance(record.get("decision_material"), bool):
            errors.append(f"{cid}: {ref or i} decision_material must be boolean")

    covered = set()
    covered_by_preserving = set()
    for i, item in enumerate(projection):
        fidelity = item.get("fidelity")
        if fidelity not in VALID_FIDELITY:
            errors.append(f"{cid}: projection[{i}] invalid fidelity")
        covers = item.get("covers_result_refs", [])
        if not isinstance(covers, list):
            errors.append(f"{cid}: projection[{i}] covers_result_refs must be list")
            continue
        for ref in covers:
            if ref not in result_map:
                errors.append(f"{cid}: projection[{i}] covers unknown result {ref}")
            covered.add(ref)
            if fidelity in PRESERVING:
                covered_by_preserving.add(ref)

    assessed_subject = case.get("assessed_projection_subject_ref")
    effective_subject = case.get("effective_projection_subject_ref")
    if not assessed_subject or not effective_subject:
        errors.append(f"{cid}: projection subject refs required")

    reasons = []
    if assessed_subject != effective_subject:
        reasons.append("effective projection subject changed after assessment")

    if consequence == "MATERIAL":
        for ref, record in result_map.items():
            if record.get("decision_material") is not True:
                continue
            if ref in covered_by_preserving:
                continue
            if ref in covered:
                reasons.append(
                    f"decision-material {ref} has UNKNOWN/LOSSY projection fidelity"
                )
            else:
                reasons.append(
                    f"decision-material {ref} omitted from effective projection"
                )

    outcome = "TRANSFER_OK" if not reasons and not errors else "REASSESS_REQUIRED"
    return {"outcome": outcome, "reasons": reasons, "errors": errors}


def evaluate_document(doc):
    if doc.get("schema_version") != "projection-composition-falsification-0.1":
        return [
            {
                "case_id": "DOCUMENT",
                "outcome": "REASSESS_REQUIRED",
                "reasons": [],
                "errors": ["wrong schema_version"],
            }
        ]

    results = []
    seen = set()
    for case in doc.get("cases", []):
        cid = case.get("case_id", "?")
        result = evaluate_case(case)
        if cid in seen:
            result["errors"].append(f"duplicate case_id {cid}")
            result["outcome"] = "REASSESS_REQUIRED"
        seen.add(cid)
        results.append({"case_id": cid, **result})
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()

    results = evaluate_document(load(args.path))
    print(
        json.dumps(
            {
                "scope": "issue-85 reference composition transfer only",
                "results": results,
            },
            indent=2,
        )
    )
    raise SystemExit(0 if all(not r["errors"] for r in results) else 1)


if __name__ == "__main__":
    main()
