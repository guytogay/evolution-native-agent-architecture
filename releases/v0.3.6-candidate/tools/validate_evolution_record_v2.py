#!/usr/bin/env python3
"""Consistency validator for ENA v0.3.6 candidate evolution-record v2.

This checks represented internal consistency only. It does not prove that an
expression trigger occurred in external reality or that evidence/authority is true.
"""
from __future__ import annotations

import argparse
import copy
import json
import tempfile
from pathlib import Path

from jsonschema.validators import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas/evolution-record.v2.schema.json"
TEMPLATE_PATH = ROOT / "templates/evolution-record.v2.json"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate_record(record: dict) -> list[str]:
    schema = load_json(SCHEMA_PATH)
    validator = Draft202012Validator(schema)
    errors = [f"schema: {e.message}" for e in validator.iter_errors(record)]

    history = record.get("expression_history") or []
    current = record.get("expression_state")
    if current == "EXPRESSED" and not history:
        errors.append("consistency: EXPRESSED requires represented expression history")
    if history:
        latest = history[-1]
        if latest.get("state") != current:
            errors.append("consistency: latest expression history state must match expression_state")
        if latest.get("state") == "EXPRESSED" and not str(latest.get("trigger", "")).strip():
            errors.append("consistency: EXPRESSED transition requires non-empty represented trigger")
    return errors


def selftest() -> None:
    base = load_json(TEMPLATE_PATH)

    # Legitimate dormant possibility: no current Variation Space, experiment, or verdict.
    assert not validate_record(base), validate_record(base)

    # False expression claim with no trace must fail.
    bad = copy.deepcopy(base)
    bad["expression_state"] = "EXPRESSED"
    assert validate_record(bad), "EXPRESSED without history unexpectedly passed"

    # Contradictory current state vs latest history must fail.
    bad = copy.deepcopy(base)
    bad["expression_history"] = [{
        "expression_id": "expr-1",
        "time": "t1",
        "state": "EXPRESSED",
        "trigger": "relevant task cue"
    }]
    assert validate_record(bad), "LATENT with latest EXPRESSED history unexpectedly passed"

    # Represented expression with trigger is structurally consistent.
    good = copy.deepcopy(base)
    good["expression_state"] = "EXPRESSED"
    good["expression_history"] = [{
        "expression_id": "expr-2",
        "time": "t2",
        "state": "EXPRESSED",
        "trigger": "relevant task cue",
        "context": "candidate selftest"
    }]
    assert not validate_record(good), validate_record(good)

    # Expression then dormancy can return to LATENT without changing selection.
    good["expression_state"] = "LATENT"
    good["expression_history"].append({
        "expression_id": "expr-3",
        "time": "t3",
        "state": "LATENT",
        "trigger": "task context ended"
    })
    assert not validate_record(good), validate_record(good)
    assert good["selection_state"] == "UNASSESSED"

    print("EVOLUTION_RECORD_V2_SELFTEST_PASS 5")


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
