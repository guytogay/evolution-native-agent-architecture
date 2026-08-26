#!/usr/bin/env python3
"""Deterministic corpus for progressive_projector.py.

The present case count is only the size of this frozen local corpus. It is not an
architectural threshold, ontology, maturity score, or evidence-independence claim.
"""
from __future__ import annotations

import copy

from progressive_projector import ProjectionError, project


def created_event(
    seq: int = 1,
    *,
    variation_space=None,
    extensions=None,
):
    event = {
        "event_id": f"evt-{seq}",
        "event_seq": seq,
        "type": "CANDIDATE_CREATED",
        "occurred_at": "2026-08-26T00:00:00Z",
        "payload": {
            "origin": "LOCAL_VARIATION",
            "hypothesis": "test hypothesis",
            "change": "test change",
            "lifecycle_state": "PROPOSED",
            "expression_state": "LATENT",
            "selection_state": "UNASSESSED",
            "variation_space": variation_space,
            "environment": {"host": "selftest"},
            "signal_refs": [],
        },
    }
    if extensions is not None:
        event["extensions"] = extensions
    return event


def expect_projection_error(fn, contains: str):
    try:
        fn()
    except ProjectionError as exc:
        if contains not in str(exc):
            raise AssertionError(
                f"expected error containing {contains!r}; got {str(exc)!r}"
            ) from exc
        return
    raise AssertionError(f"expected ProjectionError containing {contains!r}")


def case_latent_without_variation_space():
    result = project(
        {
            "candidate_id": "var-latent",
            "events": [created_event(variation_space=None)],
        }
    )
    assert result["projection"]["variation_space"] is None
    assert result["projection"]["lifecycle_state"] == "PROPOSED"
    assert result["projection"]["selection_state"] == "UNASSESSED"


def case_extension_sidecar_does_not_change_core_projection():
    plain = project(
        {"candidate_id": "var-ext", "events": [created_event()]}
    )
    extended = project(
        {
            "candidate_id": "var-ext",
            "events": [
                created_event(
                    extensions={"host.example/retrieval-cache": {"ttl": 30}}
                )
            ],
        }
    )
    assert plain["projection_digest"] == extended["projection_digest"]
    assert plain["history_digest"] != extended["history_digest"]
    assert len(extended["extension_sidecar"]) == 1


def case_unknown_non_core_event_is_retained_as_residual():
    result = project(
        {
            "candidate_id": "var-note",
            "events": [
                created_event(1),
                {
                    "event_id": "evt-2",
                    "event_seq": 2,
                    "type": "HOST_NOTE",
                    "occurred_at": "2026-08-26T00:01:00Z",
                    "payload": {"note": "Host-local observation"},
                },
            ],
        }
    )
    assert result["projection_residuals"] == [
        {
            "event_id": "evt-2",
            "event_type": "HOST_NOTE",
            "reason": "UNMAPPED_NON_CORE_EVENT",
        }
    ]


def case_unknown_core_affecting_event_is_rejected():
    document = {
        "candidate_id": "var-unknown-core",
        "events": [
            created_event(1),
            {
                "event_id": "evt-2",
                "event_seq": 2,
                "type": "HOST_MAGIC_SELECTION",
                "occurred_at": "2026-08-26T00:01:00Z",
                "payload": {"selection": "SUPPORTED"},
                "affects_core_projection": True,
            },
        ],
    }
    expect_projection_error(
        lambda: project(document),
        "unknown event type cannot affect Core projection",
    )


def case_duplicate_event_identity_is_rejected():
    document = {
        "candidate_id": "var-duplicate",
        "events": [
            created_event(1),
            {
                "event_id": "evt-1",
                "event_seq": 2,
                "type": "HOST_NOTE",
                "occurred_at": "2026-08-26T00:01:00Z",
                "payload": {},
            },
        ],
    }
    expect_projection_error(lambda: project(document), "duplicate event_id")


def case_non_increasing_event_sequence_is_rejected():
    document = {
        "candidate_id": "var-reordered",
        "events": [
            created_event(2),
            {
                "event_id": "evt-3",
                "event_seq": 1,
                "type": "HOST_NOTE",
                "occurred_at": "2026-08-26T00:01:00Z",
                "payload": {},
            },
        ],
    }
    expect_projection_error(lambda: project(document), "strictly increase")


def case_snapshot_can_hide_distinct_negative_history():
    baseline = project(
        {"candidate_id": "var-history", "events": [created_event(1)]}
    )
    with_negative_occurrence = project(
        {
            "candidate_id": "var-history",
            "events": [
                created_event(1),
                {
                    "event_id": "evt-negative",
                    "event_seq": 2,
                    "type": "NEGATIVE_OBSERVATION",
                    "occurred_at": "2026-08-26T00:02:00Z",
                    "payload": {
                        "finding": "negative occurrence retained in history",
                        "evidence_ref": "ev-negative",
                    },
                },
            ],
        }
    )

    # Deliberate falsification result: the current Core projection is identical,
    # while represented occurrence history is materially different.
    assert baseline["projection_digest"] == with_negative_occurrence["projection_digest"]
    assert baseline["history_digest"] != with_negative_occurrence["history_digest"]
    assert with_negative_occurrence["projection_residuals"]


def case_progressive_lifecycle_projection():
    events = [
        created_event(1, variation_space=None),
        {
            "event_id": "evt-2",
            "event_seq": 2,
            "type": "EXPERIMENT_RECORDED",
            "occurred_at": "2026-08-26T00:03:00Z",
            "payload": {
                "experiment_id": "exp-1",
                "time": "2026-08-26T00:03:00Z",
                "actual_change": "bounded experiment",
                "variation_space": "sandbox",
            },
        },
        {
            "event_id": "evt-3",
            "event_seq": 3,
            "type": "EVALUATION_RECORDED",
            "occurred_at": "2026-08-26T00:04:00Z",
            "payload": {
                "evaluation_id": "eval-1",
                "time": "2026-08-26T00:04:00Z",
                "outcomes": {"quality": "IMPROVED"},
                "selection": "SUPPORTED",
                "evidence_refs": ["ev-1"],
            },
        },
        {
            "event_id": "evt-4",
            "event_seq": 4,
            "type": "INTEGRATION_RECORDED",
            "occurred_at": "2026-08-26T00:05:00Z",
            "payload": {
                "integration_id": "int-1",
                "time": "2026-08-26T00:05:00Z",
                "target": "host:test",
                "result": "COMMITTED",
                "selection_state_at_commit": "SUPPORTED",
            },
        },
        {
            "event_id": "evt-5",
            "event_seq": 5,
            "type": "ARCHIVE_RECORDED",
            "occurred_at": "2026-08-26T00:06:00Z",
            "payload": {
                "time": "2026-08-26T00:06:00Z",
                "reason": "retired after integration lineage retained",
                "selection_state_preserved": "SUPPORTED",
                "lifecycle_state": "RETIRED",
            },
        },
    ]
    result = project({"candidate_id": "var-lifecycle", "events": events})
    projection = result["projection"]
    assert projection["selection_state"] == "SUPPORTED"
    assert projection["lifecycle_state"] == "RETIRED"
    assert len(projection["experiments"]) == 1
    assert len(projection["evaluations"]) == 1
    assert len(projection["integration_history"]) == 1
    assert projection["archive"]["reason"].startswith("retired")


CASES = [
    case_latent_without_variation_space,
    case_extension_sidecar_does_not_change_core_projection,
    case_unknown_non_core_event_is_retained_as_residual,
    case_unknown_core_affecting_event_is_rejected,
    case_duplicate_event_identity_is_rejected,
    case_non_increasing_event_sequence_is_rejected,
    case_snapshot_can_hide_distinct_negative_history,
    case_progressive_lifecycle_projection,
]


def main() -> int:
    for case in CASES:
        case()
        print(f"PASS {case.__name__}")
    print(f"PASS corpus_cases={len(CASES)} (descriptive corpus count only)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
