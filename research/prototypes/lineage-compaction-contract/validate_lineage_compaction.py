#!/usr/bin/env python3
"""Research-only decision-material lineage compaction contract.

This validates a proposed compact representation against a represented source
lineage. It does not prescribe a compaction algorithm.

Boundary:
- represented source history may itself be incomplete/untrue;
- digest proves represented bytes only;
- cold reference presence does not prove retrievability;
- preserved source authority never grants receiver authority.
"""
from __future__ import annotations

import hashlib
import json
from typing import Any


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()


def _nodes(source: dict[str, Any]) -> list[dict[str, Any]]:
    values = source.get("lineage_nodes")
    return values if isinstance(values, list) else []


def validate_compaction(
    source: dict[str, Any], compact: dict[str, Any]
) -> tuple[list[str], str]:
    errors: list[str] = []
    nodes = _nodes(source)
    if not nodes:
        return ["source lineage_nodes required"], "REJECT_COMPACTION"

    if compact.get("source_lineage_digest") != digest(nodes):
        errors.append("source_lineage_digest mismatch")

    # Compaction may preserve/describe dependency structure but may not turn a
    # compressed graph into a universal independence scalar/count.
    for forbidden in ("independent_support_count", "independence_score"):
        if forbidden in compact:
            errors.append(f"compaction must not manufacture {forbidden}")

    negative_ids = {
        node.get("node_id")
        for node in nodes
        if node.get("kind") == "NEGATIVE_EVIDENCE"
        and node.get("decision_material") is True
    }
    negative_ids.discard(None)

    unresolved_obligations = {
        node.get("subject_ref")
        for node in nodes
        if node.get("kind") == "OBLIGATION"
        and node.get("state") in {"OPEN", "UNKNOWN", "PARTIAL", "TRANSFERRED"}
        and node.get("decision_material") is True
    }
    unresolved_obligations.discard(None)

    terminal_obligations: dict[str, dict[str, Any]] = {}
    for node in nodes:
        if (
            node.get("kind") == "OBLIGATION"
            and node.get("state") in {"SETTLED", "CANCELLED"}
            and isinstance(node.get("subject_ref"), str)
        ):
            terminal_obligations[node["subject_ref"]] = node

    source_roots: set[str] = set()
    dependency_pairs: set[tuple[str, str]] = set()
    for node in nodes:
        if node.get("kind") in {"EVIDENCE", "NEGATIVE_EVIDENCE"}:
            observation_id = node.get("node_id")
            for root in node.get("source_roots") or []:
                if isinstance(root, str) and root:
                    source_roots.add(root)
            for dependency in node.get("derived_from") or []:
                if (
                    isinstance(observation_id, str)
                    and observation_id
                    and isinstance(dependency, str)
                    and dependency
                ):
                    dependency_pairs.add((observation_id, dependency))

    inline = compact.get("inline_summary")
    cold = compact.get("cold_lineage_ref")

    if inline is not None and not isinstance(inline, dict):
        errors.append("inline_summary must be object")
        inline = {}
    if cold is not None and not isinstance(cold, dict):
        errors.append("cold_lineage_ref must be object")
        cold = {}

    inline = inline or {}
    cold = cold or {}

    cold_valid = False
    if cold:
        if not isinstance(cold.get("ref"), str) or not cold.get("ref"):
            errors.append("cold_lineage_ref.ref required")
        if cold.get("digest") != digest(nodes):
            errors.append("cold_lineage_ref.digest mismatch")
        else:
            cold_valid = True

    represented_negative = set(inline.get("negative_lineage_refs") or [])
    missing_negative = negative_ids - represented_negative
    if missing_negative and not cold_valid:
        errors.append(
            f"decision-material negative lineage omitted: {sorted(missing_negative)}"
        )

    represented_unresolved = set(inline.get("unresolved_obligations") or [])
    missing_unresolved = unresolved_obligations - represented_unresolved
    if missing_unresolved and not cold_valid:
        errors.append(
            "decision-material unresolved obligation omitted: "
            f"{sorted(missing_unresolved)}"
        )

    settled_summary = inline.get("settled_obligations") or []
    if not isinstance(settled_summary, list):
        errors.append("settled_obligations must be array")
        settled_summary = []
    summary_by_ref = {
        item.get("subject_ref"): item
        for item in settled_summary
        if isinstance(item, dict) and isinstance(item.get("subject_ref"), str)
    }
    for ref in terminal_obligations:
        if ref in summary_by_ref:
            evidence_refs = summary_by_ref[ref].get("evidence_refs")
            if not isinstance(evidence_refs, list) or not evidence_refs:
                errors.append(
                    f"terminal obligation summary {ref} requires evidence_refs"
                )
        elif not cold_valid:
            errors.append(f"terminal obligation lineage omitted: {ref}")

    # Evidence dependency structure can be summarized inline or deferred to a
    # valid cold lineage carrier. If summarized inline, known roots and
    # represented derived/copied relations cannot disappear.
    evidence_summary = inline.get("evidence_dependency_summary")
    if evidence_summary is not None:
        if not isinstance(evidence_summary, dict):
            errors.append("evidence_dependency_summary must be object")
        else:
            represented_roots = set(evidence_summary.get("source_roots") or [])
            if not source_roots.issubset(represented_roots):
                errors.append(
                    "evidence dependency summary omits known source roots"
                )
            represented_edges = {
                (item.get("observation_id"), item.get("derived_from"))
                for item in evidence_summary.get("derived_edges") or []
                if isinstance(item, dict)
            }
            if not dependency_pairs.issubset(represented_edges):
                errors.append(
                    "evidence dependency summary omits known derived_from edges"
                )
    elif (source_roots or dependency_pairs) and not cold_valid:
        errors.append("evidence dependency lineage omitted without cold reference")

    if compact.get("receiver_authority_granted") is True:
        errors.append("compaction/source authority cannot grant receiver authority")

    if errors:
        return errors, "REJECT_COMPACTION"

    inline_covers_negative = negative_ids.issubset(represented_negative)
    inline_covers_unresolved = unresolved_obligations.issubset(
        represented_unresolved
    )
    has_inline_dependencies = (
        not (source_roots or dependency_pairs)
        or isinstance(inline.get("evidence_dependency_summary"), dict)
    )
    terminal_inline = all(ref in summary_by_ref for ref in terminal_obligations)

    if cold_valid and not (
        inline_covers_negative
        and inline_covers_unresolved
        and has_inline_dependencies
        and terminal_inline
    ):
        return (
            [],
            "VALID_COMPACTION_REQUIRES_COLD_RESOLUTION_BEFORE_MATERIAL_USE",
        )

    if unresolved_obligations:
        return [], "VALID_COMPACTION_WITH_UNRESOLVED_OBLIGATION_BLOCKER"

    return [], "VALID_COMPACTION"
