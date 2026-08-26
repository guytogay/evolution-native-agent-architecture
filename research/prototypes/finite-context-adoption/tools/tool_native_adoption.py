#!/usr/bin/env python3
"""Reference behavior for tool-native semantic retrieval ENA adoption."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RetrievalObservation:
    attempted: bool
    tool_available: bool
    source_identity_match: bool
    candidate_count: int
    exact_fallback_available: bool
    exact_fallback_succeeded: bool = False


def retrieval_status(obs: RetrievalObservation) -> str:
    if not obs.attempted:
        return "NOT_ATTEMPTED"
    if not obs.tool_available:
        if obs.exact_fallback_available and obs.exact_fallback_succeeded:
            return "SUCCESS_VIA_EXACT_FALLBACK"
        return "FAILED"
    if not obs.source_identity_match:
        return "STALE_OR_WRONG_SOURCE"
    if obs.candidate_count <= 0:
        if obs.exact_fallback_available and obs.exact_fallback_succeeded:
            return "SUCCESS_VIA_EXACT_FALLBACK"
        return "NO_HIT"
    if obs.candidate_count == 1:
        return "SUCCESS"
    return "PARTIAL_AMBIGUOUS"


def material_posture(obs: RetrievalObservation) -> str:
    status = retrieval_status(obs)
    if status in {"SUCCESS", "SUCCESS_VIA_EXACT_FALLBACK"}:
        return "USE_RETRIEVED_CANONICAL_MATERIAL"
    if status == "PARTIAL_AMBIGUOUS":
        return "BROADEN_OR_DISAMBIGUATE"
    return "NARROW_WAIT_OR_RECOVER_SOURCE"
