#!/usr/bin/env python3
"""Reference behavior for intentionally monolithic-hot ENA adoption."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class HotProjection:
    injected: bool
    source_identity_match: bool
    projection_revision_known: bool
    resident_tokens: int
    context_budget_tokens: int


def availability(proj: HotProjection) -> str:
    if not proj.injected:
        return "MISSING_INJECTION"
    if not proj.projection_revision_known:
        return "UNKNOWN_PROJECTION_REVISION"
    if not proj.source_identity_match:
        return "STALE_PROJECTION"
    return "HOT_AVAILABLE"


def context_fraction(proj: HotProjection) -> float:
    if proj.context_budget_tokens <= 0:
        raise ValueError("context budget must be positive")
    return proj.resident_tokens / proj.context_budget_tokens


def material_posture(proj: HotProjection, max_fraction: float = 0.35) -> str:
    state = availability(proj)
    if state == "HOT_AVAILABLE":
        # High resident cost is not invalid; it becomes an explicit local economics signal.
        if context_fraction(proj) > max_fraction:
            return "USE_HOT_BUT_MEASURE_CONTEXT_PRESSURE"
        return "USE_HOT_PROJECTION"
    if state == "STALE_PROJECTION":
        return "REFRESH_OR_USE_CANONICAL_SOURCE_FOR_CHANGED_DIMENSIONS"
    return "RECOVER_INJECTION_OR_CANONICAL_SOURCE"
