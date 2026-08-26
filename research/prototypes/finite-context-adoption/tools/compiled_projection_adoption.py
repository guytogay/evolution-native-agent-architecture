#!/usr/bin/env python3
"""Reference behavior for hybrid compiled Local Projection ENA adoption."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ProjectionIdentity:
    source_current_tree: str
    compiler_revision: str
    host_profile_digest: str
    projection_revision: str


@dataclass(frozen=True)
class RuntimeAssumptions:
    current_tree: str
    compiler_revision: str
    host_profile_digest: str


def freshness(projection: ProjectionIdentity, runtime: RuntimeAssumptions) -> tuple[str, list[str]]:
    changed: list[str] = []
    if projection.source_current_tree != runtime.current_tree:
        changed.append("CURRENT_TREE")
    if projection.compiler_revision != runtime.compiler_revision:
        changed.append("COMPILER_REVISION")
    if projection.host_profile_digest != runtime.host_profile_digest:
        changed.append("HOST_PROFILE")
    return ("CURRENT" if not changed else "STALE", changed)


def material_posture(
    projection: ProjectionIdentity,
    runtime: RuntimeAssumptions,
    local_projection_hit: bool,
    canonical_fallback_available: bool,
) -> str:
    state, _ = freshness(projection, runtime)
    if state == "CURRENT" and local_projection_hit:
        return "USE_COMPILED_PROJECTION"
    if canonical_fallback_available:
        return "USE_CANONICAL_FALLBACK_AND_REFRESH_IF_RECURRING"
    return "NARROW_WAIT_OR_DECLARE_STALE_PROJECTION"
