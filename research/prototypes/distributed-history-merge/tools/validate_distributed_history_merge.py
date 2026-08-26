#!/usr/bin/env python3
"""Validate research-only Distributed History Merge fixtures.

Checks represented causal/history consistency and deterministic reconciliation
constraints only. It does not discover unknown remote branches, prove semantic
merge correctness, authenticate actors, or prove external-effect settlement.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise SystemExit(f"{path}: expected object")
    return value


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            value = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"{path}:{lineno}: invalid JSON: {exc}") from exc
        if not isinstance(value, dict):
            raise SystemExit(f"{path}:{lineno}: expected object")
        rows.append(value)
    return rows


def nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value)


def string_list(value: Any, label: str, errors: list[str]) -> list[str]:
    if not isinstance(value, list) or not all(nonempty_string(v) for v in value):
        errors.append(f"{label} must be array[non-empty string]")
        return []
    return value


def ancestors(event_id: str, parents_by_id: dict[str, list[str]]) -> set[str]:
    seen: set[str] = set()
    stack = list(parents_by_id.get(event_id, []))
    while stack:
        cur = stack.pop()
        if cur in seen:
            continue
        seen.add(cur)
        stack.extend(parents_by_id.get(cur, []))
    return seen


def has_cycle(parents_by_id: dict[str, list[str]]) -> bool:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> bool:
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        for parent in parents_by_id.get(node, []):
            if parent in parents_by_id and visit(parent):
                return True
        visiting.remove(node)
        visited.add(node)
        return False

    return any(visit(node) for node in parents_by_id if node not in visited)


def validate_history(history: dict[str, Any], contract: dict[str, Any]) -> tuple[list[str], dict[str, Any]]:
    errors: list[str] = []

    for key in ("history_id", "subject_ref"):
        if not nonempty_string(history.get(key)):
            errors.append(f"{key} must be a non-empty string")

    state = history.get("state")
    if state not in set(contract["history_states"]):
        errors.append(f"state invalid: {state!r}")

    closure_claim = history.get("closure_claim")
    if closure_claim not in set(contract["closure_claims"]):
        errors.append(f"closure_claim invalid: {closure_claim!r}")

    declared_heads = string_list(history.get("heads", []), "heads", errors)
    known_remote_heads = string_list(history.get("known_remote_heads", []), "known_remote_heads", errors)

    events = history.get("events")
    if not isinstance(events, list) or not events:
        errors.append("events must be a non-empty array")
        events = []

    event_by_id: dict[str, dict[str, Any]] = {}
    parents_by_id: dict[str, list[str]] = {}
    parented: set[str] = set()
    merge_count = 0

    for index, event in enumerate(events):
        if not isinstance(event, dict):
            errors.append(f"events[{index}] must be object")
            continue
        event_id = event.get("event_id")
        if not nonempty_string(event_id):
            errors.append(f"events[{index}].event_id required")
            continue
        if event_id in event_by_id:
            errors.append(f"duplicate event_id: {event_id}")
            continue
        event_by_id[event_id] = event

        for key in ("branch_ref", "epoch_ref", "actor_ref", "payload_digest"):
            if not nonempty_string(event.get(key)):
                errors.append(f"{event_id}: {key} required")

        kind = event.get("kind")
        if kind not in set(contract["event_kinds"]):
            errors.append(f"{event_id}: invalid kind {kind!r}")

        parents = string_list(event.get("parents", []), f"{event_id}.parents", errors)
        if len(parents) != len(set(parents)):
            errors.append(f"{event_id}: duplicate parent ref")
        if event_id in parents:
            errors.append(f"{event_id}: cannot parent itself")
        parents_by_id[event_id] = parents
        parented.update(parents)

        if kind == "MERGE":
            merge_count += 1
            if len(parents) < 2:
                errors.append(f"{event_id}: MERGE requires at least two parents")
            strategy = event.get("merge_strategy")
            if strategy not in set(contract["merge_strategies"]):
                errors.append(f"{event_id}: invalid merge_strategy {strategy!r}")
        elif event.get("merge_strategy") is not None:
            errors.append(f"{event_id}: merge_strategy only applies to MERGE")

    for event_id, parents in parents_by_id.items():
        for parent in parents:
            if parent not in event_by_id:
                errors.append(f"{event_id}: unknown parent {parent!r}")

    if has_cycle(parents_by_id):
        errors.append("history graph contains a causal cycle")

    computed_heads = sorted(set(event_by_id) - {p for p in parented if p in event_by_id})
    if sorted(declared_heads) != computed_heads:
        errors.append(f"declared heads {sorted(declared_heads)} != computed heads {computed_heads}")

    if state == "LINEAR" and len(computed_heads) != 1:
        errors.append("LINEAR history requires exactly one head")
    if state == "DIVERGED" and len(computed_heads) < 2:
        errors.append("DIVERGED history requires at least two heads")
    if state == "RECONCILED":
        if len(computed_heads) != 1:
            errors.append("RECONCILED history requires exactly one head")
        if merge_count < 1:
            errors.append("RECONCILED history requires at least one represented MERGE event")

    conflicts = history.get("conflicts", [])
    if not isinstance(conflicts, list):
        errors.append("conflicts must be an array")
        conflicts = []

    open_material_conflicts = 0
    seen_conflict_ids: set[str] = set()
    for index, conflict in enumerate(conflicts):
        if not isinstance(conflict, dict):
            errors.append(f"conflicts[{index}] must be object")
            continue
        conflict_id = conflict.get("conflict_id")
        if not nonempty_string(conflict_id):
            errors.append(f"conflicts[{index}].conflict_id required")
            continue
        if conflict_id in seen_conflict_ids:
            errors.append(f"duplicate conflict_id: {conflict_id}")
        seen_conflict_ids.add(conflict_id)

        event_refs = string_list(conflict.get("event_refs", []), f"{conflict_id}.event_refs", errors)
        if len(event_refs) < 2:
            errors.append(f"{conflict_id}: requires at least two event_refs")
        for event_ref in event_refs:
            if event_ref not in event_by_id:
                errors.append(f"{conflict_id}: unknown event_ref {event_ref!r}")

        material = conflict.get("material")
        if not isinstance(material, bool):
            errors.append(f"{conflict_id}: material must be boolean")
            material = False

        status = conflict.get("status")
        if status not in set(contract["conflict_status"]):
            errors.append(f"{conflict_id}: invalid status {status!r}")

        resolution_event_ref = conflict.get("resolution_event_ref")
        if status == "OPEN":
            if resolution_event_ref is not None:
                errors.append(f"{conflict_id}: OPEN conflict must not claim resolution_event_ref")
            if material:
                open_material_conflicts += 1
        else:
            if not nonempty_string(resolution_event_ref):
                errors.append(f"{conflict_id}: {status} requires resolution_event_ref")
            elif resolution_event_ref not in event_by_id:
                errors.append(f"{conflict_id}: unknown resolution_event_ref {resolution_event_ref!r}")
            else:
                resolution_event = event_by_id[resolution_event_ref]
                if resolution_event.get("kind") != "MERGE":
                    errors.append(f"{conflict_id}: resolution event must be MERGE")
                resolution_ancestors = ancestors(resolution_event_ref, parents_by_id)
                missing = sorted(set(event_refs) - resolution_ancestors)
                if missing:
                    errors.append(f"{conflict_id}: resolution event does not descend from {missing}")
                strategy = resolution_event.get("merge_strategy")
                if material and strategy == "WALL_CLOCK_LWW":
                    errors.append(f"{conflict_id}: material conflict cannot be closed by WALL_CLOCK_LWW")
                if material and status == "AUTO_MERGED":
                    errors.append(f"{conflict_id}: material conflict cannot claim AUTO_MERGED")
                if material and status == "RESOLVED" and not nonempty_string(resolution_event.get("resolution_basis_ref")):
                    errors.append(f"{conflict_id}: material resolution requires resolution_basis_ref")

    if closure_claim == "CURRENT_CLOSED" and open_material_conflicts:
        errors.append("CURRENT_CLOSED cannot coexist with unresolved material conflict")

    if closure_claim == "CURRENT_CLOSED":
        local_heads = set(computed_heads)
        for remote_head in known_remote_heads:
            if remote_head not in event_by_id:
                errors.append(
                    f"CURRENT_CLOSED cannot be claimed while known remote head {remote_head!r} is not represented locally"
                )
                continue
            integrated = any(
                remote_head == head or remote_head in ancestors(head, parents_by_id)
                for head in local_heads
            )
            if not integrated:
                errors.append(
                    f"CURRENT_CLOSED cannot be claimed while known remote head {remote_head!r} is not causally integrated"
                )

    return errors, {
        "event_count": len(event_by_id),
        "head_count": len(computed_heads),
        "computed_heads": computed_heads,
        "merge_count": merge_count,
        "represented_valid": not errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    root = Path(__file__).resolve().parents[1]
    parser.add_argument("--contract", type=Path, default=root / "distributed-history-merge.v0.1.json")
    parser.add_argument("--fixtures", type=Path, default=root / "fixtures" / "distributed-history-merge-cases.jsonl")
    parser.add_argument("--show-all", action="store_true")
    args = parser.parse_args()

    contract = load_json(args.contract)
    fixtures = load_jsonl(args.fixtures)
    seen: set[str] = set()
    mismatches: list[str] = []

    for row in fixtures:
        case_id = row.get("case_id")
        if not nonempty_string(case_id):
            raise SystemExit("every fixture requires case_id")
        if case_id in seen:
            raise SystemExit(f"duplicate fixture case_id: {case_id}")
        seen.add(case_id)
        expected_valid = row.get("expected_valid")
        if not isinstance(expected_valid, bool):
            raise SystemExit(f"{case_id}: expected_valid must be boolean")
        history = row.get("history")
        if not isinstance(history, dict):
            raise SystemExit(f"{case_id}: history must be object")

        errors, derived = validate_history(history, contract)
        actual_valid = not errors
        if actual_valid != expected_valid:
            mismatches.append(
                f"{case_id}: expected={expected_valid} actual={actual_valid} errors={errors}"
            )
        if args.show_all or actual_valid != expected_valid:
            print(
                f"{case_id}: expected_valid={expected_valid} actual_valid={actual_valid} "
                f"events={derived['event_count']} heads={derived['head_count']} merges={derived['merge_count']} errors={len(errors)}"
            )
            for error in errors:
                print(f"  - {error}")

    print(f"fixture summary: total={len(fixtures)} mismatches={len(mismatches)}")
    if mismatches:
        print("FAIL: distributed-history-merge fixture mismatch")
        for mismatch in mismatches:
            print(f"- {mismatch}")
        return 1

    print("PASS: distributed-history-merge represented causal/reconciliation fixtures")
    print("verification_scope=REPRESENTED_CAUSAL_GRAPH_HEADS_STALE_AND_CONFLICT_RECONCILIATION_ONLY")
    print("unknown_remote_history=NOT_DISCOVERED")
    print("semantic_merge_correctness=UNPROVEN")
    print("current_change=NO")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
