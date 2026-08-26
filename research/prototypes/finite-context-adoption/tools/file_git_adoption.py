#!/usr/bin/env python3
"""Reference behavior for file/Git tiny-resident + exact cold ENA adoption."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SourceIdentity:
    ena_version: str
    current_tree: str
    merge_commit: str


@dataclass(frozen=True)
class ColdRead:
    requested_target: str
    source_identity: SourceIdentity | None
    target_found: bool


def source_state(expected: SourceIdentity, actual: SourceIdentity | None) -> str:
    if actual is None:
        return "SOURCE_UNAVAILABLE"
    if actual != expected:
        return "SOURCE_IDENTITY_MISMATCH"
    return "SOURCE_CURRENT"


def decide_material_lookup(expected: SourceIdentity, read: ColdRead) -> str:
    state = source_state(expected, read.source_identity)
    if state != "SOURCE_CURRENT":
        return "RECOVER_EXACT_SOURCE_OR_WAIT"
    if not read.target_found:
        return "BROADEN_EXACT_CANONICAL_READ"
    return "USE_COLD_TARGET"


def decide_nonmaterial_lookup(expected: SourceIdentity, read: ColdRead) -> str:
    if source_state(expected, read.source_identity) != "SOURCE_CURRENT" or not read.target_found:
        return "PROCEED_WITH_DECLARED_SEMANTIC_UNCERTAINTY"
    return "USE_COLD_TARGET"
