#!/usr/bin/env python3
"""Validate non-normative ENA Historical Adversarial Replay case files.

This validator checks research-record structure only. Passing validation does not
promote a research claim, prove an incident, or modify ENA MAINLINE semantics.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml
try:
    import jsonschema
except Exception as exc:
    print(f"ERROR: jsonschema unavailable: {exc}", file=sys.stderr)
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schema" / "case.schema.json"
CASES_DIR = ROOT / "cases"


def load_case(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema)

    paths = [Path(arg) for arg in sys.argv[1:]] if len(sys.argv) > 1 else sorted(CASES_DIR.glob("HAR-*.yaml"))
    if not paths:
        print("ERROR: no HAR case files found", file=sys.stderr)
        return 2

    failures = 0
    seen_ids: set[str] = set()

    for path in paths:
        try:
            data = load_case(path)
        except Exception as exc:
            failures += 1
            print(f"FAIL {path}: parse error: {exc}")
            continue

        errors = sorted(validator.iter_errors(data), key=lambda err: list(err.path))
        case_id = data.get("case_id") if isinstance(data, dict) else None

        if case_id in seen_ids:
            failures += 1
            print(f"FAIL {path}: duplicate case_id {case_id}")
        elif case_id:
            seen_ids.add(case_id)

        if errors:
            failures += 1
            print(f"FAIL {path}")
            for err in errors:
                location = ".".join(str(part) for part in err.path) or "<root>"
                print(f"  - {location}: {err.message}")
        else:
            print(f"PASS {path} ({case_id})")

    if failures:
        print(f"\nRESULT: FAIL ({failures} case file(s) invalid)")
        return 1

    print(f"\nRESULT: PASS ({len(paths)} case file(s) structurally valid)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
