#!/usr/bin/env python3
"""Deterministic lineage compaction contract cases. Count is descriptive only."""
from __future__ import annotations

import copy

from validate_lineage_compaction import digest, validate_compaction


def source():
    return {
        "lineage_nodes": [
            {
                "node_id": "obs-1",
                "kind": "EVIDENCE",
                "decision_material": True,
                "source_roots": ["root:A"],
                "derived_from": [],
            },
            {
                "node_id": "obs-2",
                "kind": "EVIDENCE",
                "decision_material": True,
                "source_roots": ["root:A"],
                "derived_from": ["obs-1"],
            },
            {
                "node_id": "neg-1",
                "kind": "NEGATIVE_EVIDENCE",
                "decision_material": True,
                "source_roots": ["root:B"],
                "derived_from": [],
            },
            {
                "node_id": "obl-open",
                "kind": "OBLIGATION",
                "subject_ref": "commitment:c-open",
                "state": "OPEN",
                "decision_material": True,
            },
            {
                "node_id": "obl-done",
                "kind": "OBLIGATION",
                "subject_ref": "commitment:c-done",
                "state": "SETTLED",
                "decision_material": False,
                "evidence_refs": ["receipt:r1"],
            },
            {
                "node_id": "auth-1",
                "kind": "AUTHORITY_HISTORY",
                "subject_ref": "auth:source",
                "state": "VALID_AT_SOURCE_TIME",
                "decision_material": True,
            },
        ]
    }


def base_compact(src):
    nodes = src["lineage_nodes"]
    return {
        "source_lineage_digest": digest(nodes),
        "inline_summary": {
            "negative_lineage_refs": ["neg-1"],
            "unresolved_obligations": ["commitment:c-open"],
            "settled_obligations": [
                {
                    "subject_ref": "commitment:c-done",
                    "state": "SETTLED",
                    "evidence_refs": ["receipt:r1"],
                }
            ],
            "evidence_dependency_summary": {
                "source_roots": ["root:A", "root:B"],
                "derived_edges": [
                    {"observation_id": "obs-2", "derived_from": "obs-1"}
                ],
            },
        },
        "receiver_authority_granted": False,
    }


def expect_reject(src, compact, needle):
    errors, action = validate_compaction(src, compact)
    assert errors, "expected rejection"
    assert any(needle in error for error in errors), (needle, errors)
    assert action == "REJECT_COMPACTION"


def case_full_inline_summary_valid_but_obligation_blocks():
    src = source()
    compact = base_compact(src)
    errors, action = validate_compaction(src, compact)
    assert not errors, errors
    assert action == "VALID_COMPACTION_WITH_UNRESOLVED_OBLIGATION_BLOCKER"


def case_latest_only_drops_negative_rejected():
    src = source()
    compact = base_compact(src)
    compact["inline_summary"]["negative_lineage_refs"] = []
    expect_reject(src, compact, "negative lineage omitted")


def case_latest_only_drops_open_obligation_rejected():
    src = source()
    compact = base_compact(src)
    compact["inline_summary"]["unresolved_obligations"] = []
    expect_reject(src, compact, "unresolved obligation omitted")


def case_terminal_obligation_requires_evidence():
    src = source()
    compact = base_compact(src)
    compact["inline_summary"]["settled_obligations"][0]["evidence_refs"] = []
    expect_reject(src, compact, "requires evidence_refs")


def case_dependency_root_omission_rejected():
    src = source()
    compact = base_compact(src)
    compact["inline_summary"]["evidence_dependency_summary"]["source_roots"] = [
        "root:B"
    ]
    expect_reject(src, compact, "omits known source roots")


def case_derived_edge_omission_rejected():
    src = source()
    compact = base_compact(src)
    compact["inline_summary"]["evidence_dependency_summary"]["derived_edges"] = []
    expect_reject(src, compact, "omits known derived_from edges")


def case_independent_support_count_rejected():
    src = source()
    compact = base_compact(src)
    compact["independent_support_count"] = 3
    expect_reject(src, compact, "independent_support_count")


def case_source_authority_cannot_become_receiver_authority():
    src = source()
    compact = base_compact(src)
    compact["receiver_authority_granted"] = True
    expect_reject(src, compact, "cannot grant receiver authority")


def case_cold_reference_can_defer_inline_history():
    src = source()
    compact = {
        "source_lineage_digest": digest(src["lineage_nodes"]),
        "inline_summary": {},
        "cold_lineage_ref": {
            "ref": "store://lineage/capsule-1",
            "digest": digest(src["lineage_nodes"]),
        },
        "receiver_authority_granted": False,
    }
    errors, action = validate_compaction(src, compact)
    assert not errors, errors
    assert (
        action
        == "VALID_COMPACTION_REQUIRES_COLD_RESOLUTION_BEFORE_MATERIAL_USE"
    )


def case_cold_reference_wrong_digest_rejected():
    src = source()
    compact = {
        "source_lineage_digest": digest(src["lineage_nodes"]),
        "inline_summary": {},
        "cold_lineage_ref": {
            "ref": "store://lineage/capsule-1",
            "digest": "deadbeef",
        },
    }
    errors, action = validate_compaction(src, compact)
    assert errors and any(
        "cold_lineage_ref.digest mismatch" in error for error in errors
    ), errors
    assert action == "REJECT_COMPACTION"


def case_source_digest_mutation_detected():
    src = source()
    compact = base_compact(src)
    mutated = copy.deepcopy(src)
    mutated["lineage_nodes"].append(
        {
            "node_id": "neg-2",
            "kind": "NEGATIVE_EVIDENCE",
            "decision_material": True,
            "source_roots": ["root:C"],
            "derived_from": [],
        }
    )
    expect_reject(mutated, compact, "source_lineage_digest mismatch")


def case_resolved_obligation_can_compact_without_active_blocker():
    src = source()
    for node in src["lineage_nodes"]:
        if node.get("subject_ref") == "commitment:c-open":
            node["state"] = "SETTLED"
            node["evidence_refs"] = ["receipt:r-open"]
            node["decision_material"] = False

    compact = {
        "source_lineage_digest": digest(src["lineage_nodes"]),
        "inline_summary": {
            "negative_lineage_refs": ["neg-1"],
            "unresolved_obligations": [],
            "settled_obligations": [
                {
                    "subject_ref": "commitment:c-open",
                    "state": "SETTLED",
                    "evidence_refs": ["receipt:r-open"],
                },
                {
                    "subject_ref": "commitment:c-done",
                    "state": "SETTLED",
                    "evidence_refs": ["receipt:r1"],
                },
            ],
            "evidence_dependency_summary": {
                "source_roots": ["root:A", "root:B"],
                "derived_edges": [
                    {"observation_id": "obs-2", "derived_from": "obs-1"}
                ],
            },
        },
        "receiver_authority_granted": False,
    }
    errors, action = validate_compaction(src, compact)
    assert not errors, errors
    assert action == "VALID_COMPACTION"


CASES = [
    case_full_inline_summary_valid_but_obligation_blocks,
    case_latest_only_drops_negative_rejected,
    case_latest_only_drops_open_obligation_rejected,
    case_terminal_obligation_requires_evidence,
    case_dependency_root_omission_rejected,
    case_derived_edge_omission_rejected,
    case_independent_support_count_rejected,
    case_source_authority_cannot_become_receiver_authority,
    case_cold_reference_can_defer_inline_history,
    case_cold_reference_wrong_digest_rejected,
    case_source_digest_mutation_detected,
    case_resolved_obligation_can_compact_without_active_blocker,
]


def main():
    for case in CASES:
        case()
        print("PASS", case.__name__)
    print(f"PASS compaction_cases={len(CASES)} (descriptive only)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
