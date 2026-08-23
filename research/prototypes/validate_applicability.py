#!/usr/bin/env python3
"""Validate NON-NORMATIVE ENA research prototype examples.

A PASS means only that each registered prototype example conforms to its intended
research schema. It does not promote the prototype into ENA Current or prove
semantic correctness.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parent
EXAMPLE_DIR = ROOT / "examples"

EXAMPLE_SCHEMA_MAP = {
    "HAR-006-evidence-applicability.example.yaml": ROOT / "evidence-applicability-envelope.schema.json",
    "HAR-010-temporal-applicability.example.yaml": ROOT / "evidence-applicability-envelope.schema.json",
    "HAR-011-triggered-bridge-obligation.example.yaml": ROOT / "triggered-obligation-state.schema.json",
}


def main() -> int:
    paths = sorted(EXAMPLE_DIR.glob("*.yaml"))
    if not paths:
        print("ERROR: no research prototype examples found", file=sys.stderr)
        return 2

    failures = 0
    validators: dict[Path, jsonschema.Draft202012Validator] = {}

    for path in paths:
        schema_path = EXAMPLE_SCHEMA_MAP.get(path.name)
        if schema_path is None:
            print(f"FAIL {path}")
            print("  - <root>: no explicit research-schema mapping registered for this example")
            failures += 1
            continue

        if schema_path not in validators:
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
            validators[schema_path] = jsonschema.Draft202012Validator(schema)

        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except Exception as exc:
            print(f"FAIL {path}: parse error: {exc}")
            failures += 1
            continue

        validator = validators[schema_path]
        errors = sorted(validator.iter_errors(data), key=lambda err: list(err.path))
        if errors:
            print(f"FAIL {path} [{schema_path.name}]")
            failures += 1
            for error in errors:
                location = ".".join(str(part) for part in error.path) or "<root>"
                print(f"  - {location}: {error.message}")
        else:
            print(f"PASS {path} [{schema_path.name}]")

    if failures:
        print(f"\nRESULT: FAIL ({failures} invalid or unmapped prototype example(s))")
        return 1

    print(f"\nRESULT: PASS ({len(paths)} prototype example(s) structurally valid)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
