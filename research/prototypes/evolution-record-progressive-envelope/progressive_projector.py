#!/usr/bin/env python3
"""Research-only progressive evolution envelope -> v2-style projection prototype.

This prototype explores a HOW family; it is not ENA Current, a release candidate,
or a replacement for releases/current/schemas/evolution-record.v2.schema.json.

Boundaries:
- occurrence history is represented input, not externally authenticated truth;
- Host extensions are preserved outside Core projection unless an explicit mapper exists;
- unknown event types may be retained as non-Core residuals but may not claim to alter Core;
- projection digest proves only canonical projected bytes;
- history digest proves only canonical represented occurrence bytes;
- this module does not prove authority, causality, effect truth, selection fitness, or completeness.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
from typing import Any

CORE_EVENT_TYPES = {
    "CANDIDATE_CREATED",
    "EXPERIMENT_RECORDED",
    "EVALUATION_RECORDED",
    "EXPRESSION_RECORDED",
    "INTEGRATION_RECORDED",
    "ARCHIVE_RECORDED",
}

CREATED_REQUIRED = {
    "origin",
    "hypothesis",
    "change",
    "lifecycle_state",
    "expression_state",
    "selection_state",
}

# Exact current v2 top-level required-key set observed during this research pass.
# This is comparison data, not a new normative schema.
V2_REQUIRED_TOP_LEVEL = [
    "candidate_id",
    "created_at",
    "origin",
    "lifecycle_state",
    "expression_state",
    "selection_state",
    "signal_refs",
    "hypothesis",
    "change",
    "variation_space",
    "environment",
    "experiments",
    "evaluations",
    "expression_history",
    "integration_history",
    "archive",
    "migration",
]


class ProjectionError(ValueError):
    pass


def _canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def digest(value: Any) -> str:
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _copy_extensions(event: dict[str, Any]) -> dict[str, Any] | None:
    extensions = event.get("extensions")
    if extensions is None:
        return None
    if not isinstance(extensions, dict):
        raise ProjectionError(f"{event['event_id']}: extensions must be an object")
    return copy.deepcopy(extensions)


def project(document: dict[str, Any]) -> dict[str, Any]:
    """Project progressive represented events into a v2-style aggregate view.

    The projector intentionally does not interpret arbitrary Host extensions.
    It returns them in a sidecar. Unknown non-Core events remain in occurrence
    history and projection residuals. If an unknown event claims it changes Core
    projection, projection fails closed until an explicit mapper exists.
    """
    if not isinstance(document, dict):
        raise ProjectionError("document must be an object")

    candidate_id = document.get("candidate_id")
    if not isinstance(candidate_id, str) or not candidate_id:
        raise ProjectionError("candidate_id is required")

    events = document.get("events")
    if not isinstance(events, list) or not events:
        raise ProjectionError("events must be a non-empty array")

    seen_ids: set[str] = set()
    previous_seq: int | None = None
    created_event: dict[str, Any] | None = None
    occurrence_ledger: list[dict[str, Any]] = []
    extension_sidecar: list[dict[str, Any]] = []
    projection_residuals: list[dict[str, Any]] = []

    for event in events:
        if not isinstance(event, dict):
            raise ProjectionError("every event must be an object")

        for key in ("event_id", "event_seq", "type", "occurred_at", "payload"):
            if key not in event:
                raise ProjectionError(f"event missing required key: {key}")

        event_id = event["event_id"]
        if not isinstance(event_id, str) or not event_id:
            raise ProjectionError("event_id must be a non-empty string")
        if event_id in seen_ids:
            raise ProjectionError(f"duplicate event_id: {event_id}")
        seen_ids.add(event_id)

        event_seq = event["event_seq"]
        if not isinstance(event_seq, int):
            raise ProjectionError(f"{event_id}: event_seq must be an integer")
        if previous_seq is not None and event_seq <= previous_seq:
            raise ProjectionError(f"{event_id}: event_seq must strictly increase")
        previous_seq = event_seq

        event_type = event["type"]
        payload = event["payload"]
        if not isinstance(payload, dict):
            raise ProjectionError(f"{event_id}: payload must be an object")

        if event_type == "CANDIDATE_CREATED":
            if created_event is not None:
                raise ProjectionError("exactly one CANDIDATE_CREATED event is allowed")
            missing = CREATED_REQUIRED - payload.keys()
            if missing:
                raise ProjectionError(
                    f"{event_id}: created payload missing {sorted(missing)}"
                )
            created_event = event
        elif event_type not in CORE_EVENT_TYPES:
            if event.get("affects_core_projection") is True:
                raise ProjectionError(
                    f"{event_id}: unknown event type cannot affect Core projection "
                    "without an explicit mapper"
                )
            projection_residuals.append(
                {
                    "event_id": event_id,
                    "event_type": event_type,
                    "reason": "UNMAPPED_NON_CORE_EVENT",
                }
            )

        extensions = _copy_extensions(event)
        if extensions:
            extension_sidecar.append(
                {"event_id": event_id, "extensions": extensions}
            )

        occurrence_ledger.append(copy.deepcopy(event))

    if created_event is None:
        raise ProjectionError("CANDIDATE_CREATED event is required")

    created = created_event["payload"]
    projection: dict[str, Any] = {
        "candidate_id": candidate_id,
        "created_at": created_event["occurred_at"],
        "origin": created["origin"],
        "lifecycle_state": created["lifecycle_state"],
        "expression_state": created["expression_state"],
        "selection_state": created["selection_state"],
        "signal_refs": copy.deepcopy(created.get("signal_refs", [])),
        "hypothesis": created["hypothesis"],
        "change": created["change"],
        "variation_space": created.get("variation_space"),
        "environment": copy.deepcopy(created.get("environment", {})),
        "experiments": [],
        "evaluations": [],
        "expression_history": [],
        "integration_history": [],
        "archive": None,
        "migration": None,
    }

    for event in events:
        event_type = event["type"]
        payload = event["payload"]

        if event_type == "EXPERIMENT_RECORDED":
            projection["experiments"].append(copy.deepcopy(payload))
            projection["lifecycle_state"] = "EXPERIMENTED"
        elif event_type == "EVALUATION_RECORDED":
            projection["evaluations"].append(copy.deepcopy(payload))
            selection = payload.get("selection")
            if selection:
                projection["selection_state"] = selection
        elif event_type == "EXPRESSION_RECORDED":
            projection["expression_history"].append(copy.deepcopy(payload))
            state = payload.get("state")
            if state:
                projection["expression_state"] = state
        elif event_type == "INTEGRATION_RECORDED":
            projection["integration_history"].append(copy.deepcopy(payload))
            if payload.get("result") == "COMMITTED":
                projection["lifecycle_state"] = "INTEGRATED"
        elif event_type == "ARCHIVE_RECORDED":
            projection["archive"] = copy.deepcopy(payload)
            target_state = payload.get("lifecycle_state")
            if target_state in {"ARCHIVED", "RETIRED"}:
                projection["lifecycle_state"] = target_state

    missing_required = [
        key for key in V2_REQUIRED_TOP_LEVEL if key not in projection
    ]
    if missing_required:
        raise ProjectionError(
            f"projection missing current-v2 comparison keys: {missing_required}"
        )

    return {
        "projection": projection,
        "occurrence_ledger": occurrence_ledger,
        "extension_sidecar": extension_sidecar,
        "projection_residuals": projection_residuals,
        "history_digest": digest(occurrence_ledger),
        "projection_digest": digest(projection),
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Project a research progressive evolution envelope"
    )
    parser.add_argument("input", help="JSON input document")
    parser.add_argument("--output", help="optional JSON output path")
    args = parser.parse_args()

    document = json.loads(Path(args.input).read_text(encoding="utf-8"))
    result = project(document)
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"

    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
