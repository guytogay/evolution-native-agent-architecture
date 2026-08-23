#!/usr/bin/env python3
"""Consistency validator for ENA v0.3.6 candidate evolution-record v2.

Checks represented internal consistency only. It does not prove external truth,
actual expression, evidence validity, authority, recovery, or universal fitness.
"""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path

from jsonschema.validators import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas/evolution-record.v2.schema.json"
TEMPLATE_PATH = ROOT / "templates/evolution-record.v2.json"
POSITIVE = {"SUPPORTED", "PARTIAL"}
NEGATIVE = {"NOT_SUPPORTED", "HARMFUL"}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate_record(record: dict) -> list[str]:
    schema = load_json(SCHEMA_PATH)
    errors = [f"schema: {e.message}" for e in Draft202012Validator(schema).iter_errors(record)]

    history = record.get("expression_history") or []
    current_expr = record.get("expression_state")
    if current_expr == "EXPRESSED" and not history:
        errors.append("consistency: EXPRESSED requires represented expression history")
    if history:
        latest_expr = history[-1]
        if latest_expr.get("state") != current_expr:
            errors.append("consistency: latest expression history state must match expression_state")
        if latest_expr.get("state") == "EXPRESSED" and not str(latest_expr.get("trigger", "")).strip():
            errors.append("consistency: EXPRESSED transition requires non-empty represented trigger")

    experiments = record.get("experiments") or []
    evaluations = record.get("evaluations") or []
    lifecycle = record.get("lifecycle_state")
    selection = record.get("selection_state")

    if lifecycle == "PROPOSED" and experiments:
        errors.append("consistency: PROPOSED cannot contain represented experiments")
    if lifecycle == "EXPERIMENTED" and not experiments:
        errors.append("consistency: EXPERIMENTED requires represented experiment")

    if selection != "UNASSESSED":
        if not experiments:
            errors.append("consistency: non-UNASSESSED selection requires represented experiment")
        if not evaluations:
            errors.append("consistency: non-UNASSESSED selection requires represented evaluation")
        else:
            latest = evaluations[-1]
            if latest.get("selection") != selection:
                errors.append("consistency: latest evaluation selection must match selection_state")
            outcomes = latest.get("outcomes") or {}
            evidence = latest.get("evidence_refs") or []
            values = set(outcomes.values())
            if selection in POSITIVE:
                if "IMPROVED" not in values:
                    errors.append("consistency: positive selection requires IMPROVED outcome")
                if not evidence:
                    errors.append("consistency: positive selection requires evidence reference")
            elif selection == "HARMFUL":
                if "DEGRADED" not in values:
                    errors.append("consistency: HARMFUL requires DEGRADED outcome")
                if not evidence:
                    errors.append("consistency: HARMFUL requires evidence reference")
            elif selection == "NOT_SUPPORTED":
                if not outcomes:
                    errors.append("consistency: NOT_SUPPORTED requires represented outcomes")
                if not evidence:
                    errors.append("consistency: NOT_SUPPORTED requires evidence reference")

    if lifecycle == "INTEGRATED":
        if not experiments or not evaluations:
            errors.append("consistency: INTEGRATED requires represented experiment and evaluation")
        if not (record.get("integration_history") or []):
            errors.append("consistency: INTEGRATED requires integration history")

    return errors


def exp_record(base: dict) -> dict:
    item = copy.deepcopy(base)
    item["lifecycle_state"] = "EXPERIMENTED"
    item["variation_space"] = "sandbox"
    item["experiments"] = [{
        "experiment_id": "exp-1", "time": "t1", "actual_change": "test change",
        "variation_space": "sandbox"
    }]
    return item


def selftest() -> None:
    base = load_json(TEMPLATE_PATH)

    # 1: legitimate dormant possibility has no current experiment surface or verdict.
    assert not validate_record(base), validate_record(base)

    # 2: false expression claim with no trace must fail.
    bad = copy.deepcopy(base)
    bad["expression_state"] = "EXPRESSED"
    assert validate_record(bad), "EXPRESSED without history unexpectedly passed"

    # 3: latest expression state contradiction must fail.
    bad = copy.deepcopy(base)
    bad["expression_history"] = [{"expression_id": "expr-1", "time": "t1", "state": "EXPRESSED", "trigger": "task cue"}]
    assert validate_record(bad), "LATENT with latest EXPRESSED history unexpectedly passed"

    # 4: represented expression with trigger may remain UNASSESSED if no selection claim is made.
    good = copy.deepcopy(base)
    good["expression_state"] = "EXPRESSED"
    good["expression_history"] = [{"expression_id": "expr-2", "time": "t2", "state": "EXPRESSED", "trigger": "relevant task cue"}]
    assert not validate_record(good), validate_record(good)

    # 5: expression can return to dormancy without manufacturing selection.
    good["expression_state"] = "LATENT"
    good["expression_history"].append({"expression_id": "expr-3", "time": "t3", "state": "LATENT", "trigger": "task ended"})
    assert not validate_record(good), validate_record(good)
    assert good["selection_state"] == "UNASSESSED"

    # 6: UNKNOWN selection without experiment is not a shortcut around reality contact.
    bad = copy.deepcopy(base)
    bad["selection_state"] = "UNKNOWN"
    bad["evaluations"] = [{"evaluation_id": "eval-0", "time": "t0", "outcomes": {}, "selection": "UNKNOWN", "evidence_refs": []}]
    assert validate_record(bad), "UNKNOWN without experiment unexpectedly passed"

    # 7: positive selection without IMPROVED evidence must fail.
    bad = exp_record(base)
    bad["selection_state"] = "SUPPORTED"
    bad["evaluations"] = [{"evaluation_id": "eval-1", "time": "t2", "outcomes": {"quality": "UNCHANGED"}, "selection": "SUPPORTED", "evidence_refs": ["e1"]}]
    assert validate_record(bad), "SUPPORTED without IMPROVED unexpectedly passed"

    # 8: positive selection without evidence ref must fail.
    bad = exp_record(base)
    bad["selection_state"] = "SUPPORTED"
    bad["evaluations"] = [{"evaluation_id": "eval-2", "time": "t2", "outcomes": {"quality": "IMPROVED"}, "selection": "SUPPORTED", "evidence_refs": []}]
    assert validate_record(bad), "SUPPORTED without evidence unexpectedly passed"

    # 9: evidence-backed local positive selection is structurally consistent.
    good2 = exp_record(base)
    good2["selection_state"] = "SUPPORTED"
    good2["evaluations"] = [{"evaluation_id": "eval-3", "time": "t2", "outcomes": {"quality": "IMPROVED"}, "selection": "SUPPORTED", "evidence_refs": ["trace:local"]}]
    assert not validate_record(good2), validate_record(good2)

    # 10: integrated state cannot self-assert without integration history.
    bad = copy.deepcopy(good2)
    bad["lifecycle_state"] = "INTEGRATED"
    assert validate_record(bad), "INTEGRATED without integration history unexpectedly passed"

    print("EVOLUTION_RECORD_V2_SELFTEST_PASS 10")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    if args.selftest:
        selftest()
        return
    if not args.path:
        parser.error("path required unless --selftest is used")
    record = load_json(Path(args.path))
    errors = validate_record(record)
    print(json.dumps({"valid": not errors, "errors": errors}, ensure_ascii=False, indent=2))
    raise SystemExit(0 if not errors else 1)


if __name__ == "__main__":
    main()
