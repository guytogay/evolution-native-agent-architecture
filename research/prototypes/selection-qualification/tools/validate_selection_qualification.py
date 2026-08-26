#!/usr/bin/env python3
"""Resolve represented selection-scope qualification for ENA research.

Verification scope: represented durable selection qualification only.
This tool does not prove that environment metadata is complete/true, that a
scope-basis reference is externally authentic, that the selection verdict is
correct, or that source selection is receiver-local proof.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

SELECTION_STATES = {
    "UNASSESSED",
    "SUPPORTED",
    "PARTIAL",
    "NOT_SUPPORTED",
    "HARMFUL",
    "UNKNOWN",
}
QUALIFICATION_STATUSES = {"SCOPED", "UNKNOWN", "INCOMPLETE"}
RESOLUTIONS = {
    "NOT_APPLICABLE",
    "QUALIFIED_DIRECT",
    "QUALIFIED_REFERENCED",
    "QUALIFICATION_UNKNOWN",
    "UNQUALIFIED_SELECTION",
    "INVALID_RECORD",
}


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            row = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"{path}:{lineno}: invalid JSON: {exc}") from exc
        if not isinstance(row, dict):
            raise SystemExit(f"{path}:{lineno}: row must be object")
        rows.append(row)
    return rows


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _valid_refs(value: Any) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(_nonempty_string(item) for item in value)
        and len(value) == len(set(value))
    )


def _direct_scope_present(environment: Any) -> bool:
    """Represented direct scope only; semantic completeness is out of scope."""
    return isinstance(environment, dict) and bool(environment)


def validate_qualification_overlay(overlay: Any, *, direct_scope_present: bool) -> list[str]:
    if overlay is None:
        return []
    if not isinstance(overlay, dict):
        return ["qualification overlay must be object"]

    allowed = {"status", "scope_basis_refs", "note"}
    unknown_fields = sorted(set(overlay) - allowed)
    errors: list[str] = []
    if unknown_fields:
        errors.append(f"unsupported qualification fields: {unknown_fields}")

    status = overlay.get("status")
    if status not in QUALIFICATION_STATUSES:
        errors.append("qualification status must be SCOPED, UNKNOWN, or INCOMPLETE")

    refs = overlay.get("scope_basis_refs")
    if refs is not None and not _valid_refs(refs):
        errors.append("scope_basis_refs must be a non-empty unique string array when present")

    note = overlay.get("note")
    if note is not None and not _nonempty_string(note):
        errors.append("note must be non-empty string when present")

    if status == "SCOPED" and not direct_scope_present and not _valid_refs(refs):
        errors.append("SCOPED requires direct environment scope or non-empty scope_basis_refs")

    return errors


def resolve_one(selection_state: Any, environment: Any, overlay: Any) -> tuple[str, list[str]]:
    if selection_state not in SELECTION_STATES:
        return ("INVALID_RECORD", ["invalid selection_state"])
    if not isinstance(environment, dict):
        return ("INVALID_RECORD", ["environment must be object"])

    direct = _direct_scope_present(environment)
    overlay_errors = validate_qualification_overlay(overlay, direct_scope_present=direct)
    if overlay_errors:
        return ("INVALID_RECORD", overlay_errors)

    if selection_state == "UNASSESSED":
        return ("NOT_APPLICABLE", [])

    if isinstance(overlay, dict) and overlay.get("status") in {"UNKNOWN", "INCOMPLETE"}:
        return ("QUALIFICATION_UNKNOWN", [])

    if direct:
        return ("QUALIFIED_DIRECT", [])

    if isinstance(overlay, dict) and overlay.get("status") == "SCOPED":
        return ("QUALIFIED_REFERENCED", [])

    return (
        "UNQUALIFIED_SELECTION",
        ["non-UNASSESSED selection has no direct/referenced scope basis and no explicit UNKNOWN/INCOMPLETE qualification"],
    )


def resolve_case(case: Any) -> dict[str, Any]:
    if not isinstance(case, dict):
        return {
            "local_resolution": "INVALID_RECORD",
            "source_resolution": "INVALID_RECORD",
            "diagnostics": ["case must be object"],
        }

    record = case.get("record")
    if not isinstance(record, dict):
        return {
            "local_resolution": "INVALID_RECORD",
            "source_resolution": "INVALID_RECORD",
            "diagnostics": ["record must be object"],
        }

    local_resolution, local_diag = resolve_one(
        record.get("selection_state"),
        record.get("environment"),
        case.get("selection_qualification"),
    )

    migration = record.get("migration")
    if migration is None:
        source_resolution = "NOT_APPLICABLE"
        source_diag: list[str] = []
    elif not isinstance(migration, dict):
        source_resolution = "INVALID_RECORD"
        source_diag = ["migration must be object or null"]
    else:
        source_state = migration.get("source_selection_state")
        source_environment = migration.get("source_environment", {})
        source_resolution, source_diag = resolve_one(
            source_state,
            source_environment,
            case.get("source_selection_qualification"),
        )

    return {
        "local_resolution": local_resolution,
        "source_resolution": source_resolution,
        "diagnostics": [
            *(f"local: {item}" for item in local_diag),
            *(f"source: {item}" for item in source_diag),
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    default_cases = Path(__file__).resolve().parents[1] / "fixtures" / "selection-qualification-cases.jsonl"
    parser.add_argument("--cases", type=Path, default=default_cases)
    args = parser.parse_args()

    rows = load_jsonl(args.cases)
    failures: list[str] = []
    seen: set[str] = set()
    local_counts = {state: 0 for state in RESOLUTIONS}
    source_counts = {state: 0 for state in RESOLUTIONS}

    for row in rows:
        case_id = row.get("case_id")
        if not _nonempty_string(case_id):
            failures.append("case without valid case_id")
            continue
        if case_id in seen:
            failures.append(f"duplicate case_id: {case_id}")
            continue
        seen.add(case_id)

        expected_local = row.get("expected_local")
        expected_source = row.get("expected_source")
        if expected_local not in RESOLUTIONS or expected_source not in RESOLUTIONS:
            failures.append(f"{case_id}: invalid expected resolution")
            continue

        actual = resolve_case(row.get("case"))
        local = actual["local_resolution"]
        source = actual["source_resolution"]
        local_counts[local] += 1
        source_counts[source] += 1
        if local != expected_local:
            failures.append(
                f"{case_id}: local expected={expected_local} actual={local} diagnostics={actual['diagnostics']}"
            )
        if source != expected_source:
            failures.append(
                f"{case_id}: source expected={expected_source} actual={source} diagnostics={actual['diagnostics']}"
            )

    print(f"cases={len(rows)}")
    print("local=" + ",".join(f"{key}:{local_counts[key]}" for key in sorted(local_counts)))
    print("source=" + ",".join(f"{key}:{source_counts[key]}" for key in sorted(source_counts)))

    if failures:
        print(f"FAIL: {len(failures)} fixture mismatch(es)")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("PASS: all Selection Qualification fixtures matched represented reference rules")
    print("verification_scope=REPRESENTED_SELECTION_QUALIFICATION_ONLY")
    print("external_scope_completeness=UNPROVEN")
    print("selection_truth=UNPROVEN")
    print("scope_basis_reference_authenticity=UNPROVEN")
    print("source_selection_is_receiver_local_proof=FALSE")
    print("fixture_cardinality=OPEN_WITH_TARGETED_REGRESSION_DEPENDENCIES")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
