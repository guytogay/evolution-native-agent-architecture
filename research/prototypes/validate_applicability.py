#!/usr/bin/env python3
"""Validate NON-NORMATIVE Evidence Applicability research prototypes.

A PASS means only that prototype examples conform to the research schema.
It does not promote the prototype into ENA MAINLINE or prove semantic correctness.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml
import jsonschema

ROOT = Path(__file__).resolve().parent
SCHEMA_PATH = ROOT / "evidence-applicability-envelope.schema.json"
EXAMPLE_DIR = ROOT / "examples"


def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema)
    paths = sorted(EXAMPLE_DIR.glob("*.yaml"))
    if not paths:
        print("ERROR: no applicability prototype examples found", file=sys.stderr)
        return 2

    failures = 0
    for path in paths:
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except Exception as exc:
            print(f"FAIL {path}: parse error: {exc}")
            failures += 1
            continue

        errors = sorted(validator.iter_errors(data), key=lambda err: list(err.path))
        if errors:
            print(f"FAIL {path}")
            failures += 1
            for error in errors:
                location = ".".join(str(part) for part in error.path) or "<root>"
                print(f"  - {location}: {error.message}")
        else:
            print(f"PASS {path}")

    if failures:
        print(f"\nRESULT: FAIL ({failures} invalid prototype example(s))")
        return 1

    print(f"\nRESULT: PASS ({len(paths)} prototype example(s) structurally valid)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
