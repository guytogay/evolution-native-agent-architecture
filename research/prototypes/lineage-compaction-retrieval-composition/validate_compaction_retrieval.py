#!/usr/bin/env python3
"""Cross-organ research harness: lineage compaction x Retrieval Obligation 0.5.

A cold lineage reference can make a compaction structurally honest without making
the material decision ready. This module composes the existing validators rather
than duplicating their rules.

Verification scope:
- represented compaction consistency;
- represented retrieval lifecycle/sufficiency;
- exact cold subject + content identity match.

It does not prove storage availability, registry completeness, source authenticity,
or real-world freshness beyond the represented retrieval subject.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
PROTOTYPES = HERE.parent
COMPACTION_DIR = PROTOTYPES / "lineage-compaction-contract"
RETRIEVAL_DIR = PROTOTYPES / "memory-metabolism" / "retrieval-obligation-0.5"


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load module {name} from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_compaction = _load_module(
    "ena_lineage_compaction_validator",
    COMPACTION_DIR / "validate_lineage_compaction.py",
)
_retrieval = _load_module(
    "ena_retrieval_obligation_05_validator",
    RETRIEVAL_DIR / "validate_retrieval_obligation.py",
)

validate_compaction = _compaction.validate_compaction
lineage_digest = _compaction.digest
validate_retrieval = _retrieval.validate_document
build_sufficiency_resolution = _retrieval.build_sufficiency_resolution


def expected_content_identity(compact: dict[str, Any]) -> str | None:
    cold = compact.get("cold_lineage_ref")
    if not isinstance(cold, dict):
        return None
    digest_value = cold.get("digest")
    if not isinstance(digest_value, str) or not digest_value:
        return None
    return f"sha256:{digest_value}"


def _material_ready_resolution_for(
    retrieval_doc: dict[str, Any],
    record_ref: str,
    content_identity_ref: str,
) -> bool:
    decisions = {
        item.get("decision_id"): item
        for item in retrieval_doc.get("decisions", [])
        if isinstance(item, dict)
    }
    obligations = {
        item.get("obligation_id"): item
        for item in retrieval_doc.get("obligations", [])
        if isinstance(item, dict)
    }
    attempts = retrieval_doc.get("attempts", [])

    matching_attempts: list[dict[str, Any]] = []
    for attempt in attempts:
        if not isinstance(attempt, dict):
            continue
        if attempt.get("subject_relevance") != "DECISION_MATERIAL":
            continue
        if attempt.get("outcome") != "HIT":
            continue
        for returned in attempt.get("returned_results") or []:
            if (
                isinstance(returned, dict)
                and returned.get("record_ref") == record_ref
                and returned.get("content_identity_ref") == content_identity_ref
            ):
                matching_attempts.append(attempt)
                break

    for attempt in matching_attempts:
        obligation = obligations.get(attempt.get("obligation_id"))
        if not isinstance(obligation, dict) or obligation.get("state") != "CLOSED":
            continue
        closure = obligation.get("closure") or {}
        if closure.get("disposition") != "RETRIEVAL_SUFFICIENCY_RESOLVED":
            continue
        if attempt.get("attempt_id") not in (closure.get("basis_attempt_ids") or []):
            continue
        decision = decisions.get(obligation.get("decision_id"))
        if (
            isinstance(decision, dict)
            and decision.get("consequence") == "MATERIAL"
            and decision.get("disposition") == "READY"
        ):
            return True
    return False


def assess_material_use(
    source: dict[str, Any],
    compact: dict[str, Any],
    retrieval_doc: dict[str, Any] | None = None,
) -> tuple[str, list[str]]:
    compaction_errors, compaction_state = validate_compaction(source, compact)
    if compaction_errors:
        return "REJECT_COMPACTION", compaction_errors

    if compaction_state == "VALID_COMPACTION_WITH_UNRESOLVED_OBLIGATION_BLOCKER":
        return "BLOCKED_BY_UNRESOLVED_OBLIGATION", []

    if compaction_state == "VALID_COMPACTION":
        return "MATERIAL_USE_READY_INLINE", []

    if compaction_state != "VALID_COMPACTION_REQUIRES_COLD_RESOLUTION_BEFORE_MATERIAL_USE":
        return "REJECT_UNKNOWN_COMPACTION_STATE", [compaction_state]

    cold = compact.get("cold_lineage_ref") or {}
    record_ref = cold.get("ref")
    content_identity_ref = expected_content_identity(compact)
    if not isinstance(record_ref, str) or not record_ref or content_identity_ref is None:
        return "REJECT_COMPACTION", ["valid cold lineage identity required"]

    if retrieval_doc is None:
        return "COLD_RESOLUTION_REQUIRED", []

    retrieval_errors = validate_retrieval(retrieval_doc)
    if retrieval_errors:
        return "RETRIEVAL_INVALID", retrieval_errors

    if not _material_ready_resolution_for(
        retrieval_doc,
        record_ref,
        content_identity_ref,
    ):
        return "COLD_SUBJECT_NOT_RESOLVED", []

    return "MATERIAL_USE_READY_AFTER_COLD_RESOLUTION", []
