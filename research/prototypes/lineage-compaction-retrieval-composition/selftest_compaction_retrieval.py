#!/usr/bin/env python3
from __future__ import annotations

from validate_compaction_retrieval import (
    assess_material_use,
    build_sufficiency_resolution,
    lineage_digest,
)

COLD_REF = "lineage:cold:1"


def base_source(*, unresolved_obligation: bool = False) -> dict:
    nodes = [
        {
            "node_id": "evidence:1",
            "kind": "EVIDENCE",
            "decision_material": True,
            "source_roots": ["source:A"],
            "derived_from": [],
        },
        {
            "node_id": "negative:1",
            "kind": "NEGATIVE_EVIDENCE",
            "decision_material": True,
            "source_roots": ["source:A"],
            "derived_from": ["evidence:1"],
        },
    ]
    if unresolved_obligation:
        nodes.append(
            {
                "node_id": "obligation-node:1",
                "kind": "OBLIGATION",
                "subject_ref": "commitment:C1",
                "state": "OPEN",
                "decision_material": True,
            }
        )
    return {"lineage_nodes": nodes}


def inline_compact(source: dict, *, unresolved_obligation: bool = False) -> dict:
    inline = {
        "negative_lineage_refs": ["negative:1"],
        "evidence_dependency_summary": {
            "source_roots": ["source:A"],
            "derived_edges": [
                {
                    "observation_id": "negative:1",
                    "derived_from": "evidence:1",
                }
            ],
        },
    }
    if unresolved_obligation:
        inline["unresolved_obligations"] = ["commitment:C1"]
    return {
        "source_lineage_digest": lineage_digest(source["lineage_nodes"]),
        "inline_summary": inline,
        "receiver_authority_granted": False,
    }


def cold_compact(source: dict) -> dict:
    digest_value = lineage_digest(source["lineage_nodes"])
    return {
        "source_lineage_digest": digest_value,
        "inline_summary": {},
        "cold_lineage_ref": {
            "ref": COLD_REF,
            "digest": digest_value,
        },
        "receiver_authority_granted": False,
    }


def retrieval_hit_doc(record_ref: str, content_identity_ref: str) -> dict:
    doc = {
        "schema_version": "memory-retrieval-obligation-research-0.5",
        "decisions": [
            {
                "decision_id": "d1",
                "consequence": "MATERIAL",
                "disposition": "READY",
                "uncertainty_declared": False,
            }
        ],
        "trigger_events": [
            {
                "trigger_id": "t1",
                "decision_id": "d1",
                "basis": "KNOWN_GAP",
                "resolver_ref": "resolver:lineage",
            }
        ],
        "retrieval_intents": [
            {
                "intent_id": "i1",
                "decision_id": "d1",
                "trigger_ids": ["t1"],
                "resolver_ref": "resolver:lineage",
                "decision_context_snapshot_ref": "ctx:material-use:v1",
                "need_basis": "DURABLE_STATE_MAY_CHANGE_DECISION",
            }
        ],
        "obligations": [
            {
                "obligation_id": "o1",
                "decision_id": "d1",
                "intent_id": "i1",
                "resolver_ref": "resolver:lineage",
                "state": "CLOSED",
                "closure": {
                    "disposition": "RETRIEVAL_SUFFICIENCY_RESOLVED",
                    "basis_discovery_id": "sd1",
                    "basis_attempt_ids": ["a1"],
                    "sufficiency_resolution_ref": "suff:1",
                },
            }
        ],
        "scope_discoveries": [
            {
                "discovery_id": "sd1",
                "obligation_id": "o1",
                "sequence": 1,
                "resolver_ref": "resolver:lineage",
                "registry_snapshot_ref": "registry:lineage:v1",
                "selected_scope_refs": ["scope:lineage"],
                "outcome": "SCOPES_SELECTED",
                "coverage": "PARTIAL",
                "subject_relevance": "DECISION_MATERIAL",
                "receipt_ref": "disc:1",
            }
        ],
        "attempts": [
            {
                "attempt_id": "a1",
                "obligation_id": "o1",
                "discovery_id": "sd1",
                "scope_ref": "scope:lineage",
                "sequence": 1,
                "resolver_ref": "resolver:lineage",
                "outcome": "HIT",
                "coverage": "PARTIAL",
                "subject_relevance": "DECISION_MATERIAL",
                "returned_results": [
                    {
                        "record_ref": record_ref,
                        "content_identity_ref": content_identity_ref,
                    }
                ],
                "receipt_ref": "ret:1",
            }
        ],
        "sufficiency_resolutions": [],
    }
    doc["sufficiency_resolutions"] = [build_sufficiency_resolution(doc, "o1")]
    return doc


def retrieval_nohit_doc() -> dict:
    return {
        "schema_version": "memory-retrieval-obligation-research-0.5",
        "decisions": [
            {
                "decision_id": "d1",
                "consequence": "MATERIAL",
                "disposition": "READY",
                "uncertainty_declared": False,
            }
        ],
        "trigger_events": [
            {
                "trigger_id": "t1",
                "decision_id": "d1",
                "basis": "KNOWN_GAP",
                "resolver_ref": "resolver:lineage",
            }
        ],
        "retrieval_intents": [
            {
                "intent_id": "i1",
                "decision_id": "d1",
                "trigger_ids": ["t1"],
                "resolver_ref": "resolver:lineage",
                "decision_context_snapshot_ref": "ctx:material-use:v1",
                "need_basis": "DURABLE_STATE_MAY_CHANGE_DECISION",
            }
        ],
        "obligations": [
            {
                "obligation_id": "o1",
                "decision_id": "d1",
                "intent_id": "i1",
                "resolver_ref": "resolver:lineage",
                "state": "CLOSED",
                "closure": {
                    "disposition": "NO_HIT_BOUNDED",
                    "basis_discovery_id": "sd1",
                    "basis_attempt_ids": ["a1"],
                },
            }
        ],
        "scope_discoveries": [
            {
                "discovery_id": "sd1",
                "obligation_id": "o1",
                "sequence": 1,
                "resolver_ref": "resolver:lineage",
                "registry_snapshot_ref": "registry:lineage:v1",
                "selected_scope_refs": ["scope:lineage"],
                "outcome": "SCOPES_SELECTED",
                "coverage": "DECLARED_DISCOVERY_COMPLETE",
                "subject_relevance": "DECISION_MATERIAL",
                "receipt_ref": "disc:1",
            }
        ],
        "attempts": [
            {
                "attempt_id": "a1",
                "obligation_id": "o1",
                "discovery_id": "sd1",
                "scope_ref": "scope:lineage",
                "sequence": 1,
                "resolver_ref": "resolver:lineage",
                "outcome": "NO_HIT",
                "coverage": "DECLARED_SCOPE_COMPLETE",
                "subject_relevance": "DECISION_MATERIAL",
                "returned_results": [],
                "receipt_ref": "ret:1",
            }
        ],
        "sufficiency_resolutions": [],
    }


def expect(name: str, source: dict, compact: dict, retrieval_doc: dict | None, expected: str) -> None:
    actual, errors = assess_material_use(source, compact, retrieval_doc)
    if actual != expected:
        raise AssertionError(f"{name}: expected={expected} actual={actual} errors={errors}")


def main() -> None:
    n = 0

    source = base_source()
    expect("inline_material_lineage_ready", source, inline_compact(source), None, "MATERIAL_USE_READY_INLINE")
    n += 1

    source = base_source()
    compact = cold_compact(source)
    expect("cold_ref_alone_not_ready", source, compact, None, "COLD_RESOLUTION_REQUIRED")
    n += 1

    identity = f"sha256:{compact['cold_lineage_ref']['digest']}"
    doc = retrieval_hit_doc(COLD_REF, identity)
    expect("correct_cold_subject_and_content_ready", source, compact, doc, "MATERIAL_USE_READY_AFTER_COLD_RESOLUTION")
    n += 1

    doc = retrieval_hit_doc(COLD_REF, "sha256:wrong-content")
    expect("fresh_but_wrong_content_not_resolved", source, compact, doc, "COLD_SUBJECT_NOT_RESOLVED")
    n += 1

    doc = retrieval_hit_doc(COLD_REF, identity)
    doc["attempts"][0]["returned_results"][0]["content_identity_ref"] = "sha256:changed-after-resolution"
    expect("stale_sufficiency_after_content_change", source, compact, doc, "RETRIEVAL_INVALID")
    n += 1

    doc = retrieval_hit_doc(COLD_REF, identity)
    doc["attempts"][0]["scope_ref"] = "scope:not-selected"
    expect("wrong_scope_retrieval_invalid", source, compact, doc, "RETRIEVAL_INVALID")
    n += 1

    expect("bounded_no_hit_is_not_cold_resolution", source, compact, retrieval_nohit_doc(), "COLD_SUBJECT_NOT_RESOLVED")
    n += 1

    doc = retrieval_hit_doc("lineage:other", identity)
    expect("wrong_record_alias_not_resolved", source, compact, doc, "COLD_SUBJECT_NOT_RESOLVED")
    n += 1

    source_with_obligation = base_source(unresolved_obligation=True)
    expect(
        "unresolved_obligation_blocks_even_with_inline_lineage",
        source_with_obligation,
        inline_compact(source_with_obligation, unresolved_obligation=True),
        None,
        "BLOCKED_BY_UNRESOLVED_OBLIGATION",
    )
    n += 1

    bad = cold_compact(source)
    bad["source_lineage_digest"] = "bad-digest"
    expect("invalid_compaction_rejected_before_retrieval", source, bad, None, "REJECT_COMPACTION")
    n += 1

    print(f"LINEAGE_COMPACTION_RETRIEVAL_COMPOSITION_PASS {n}")
    print("boundary=COLD_REF_PRESENT_NE_RETRIEVAL_SUFFICIENCY_NE_MATERIAL_USE_READY")
    print("external_retrievability=UNPROVEN")
    print("registry_completeness=UNPROVEN")
    print("real_world_freshness=UNPROVEN")


if __name__ == "__main__":
    main()
