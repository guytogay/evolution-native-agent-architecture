#!/usr/bin/env python3
"""Small executable reference for declared-commutative replicated state."""

from __future__ import annotations


CRDT_SAFE_CLASSES = {
    "G_SET_UNION",
    "G_COUNTER_MAX",
}


def merge_gset(left: set[str], right: set[str]) -> set[str]:
    return left | right


def merge_gcounter(left: dict[str, int], right: dict[str, int]) -> dict[str, int]:
    actors = set(left) | set(right)
    return {actor: max(left.get(actor, 0), right.get(actor, 0)) for actor in actors}


def merge(state_class: str, left, right):
    if state_class not in CRDT_SAFE_CLASSES:
        raise ValueError("NOT_CRDT_SAFE_FOR_THIS_SURFACE")
    if state_class == "G_SET_UNION":
        if not isinstance(left, set) or not isinstance(right, set):
            raise TypeError("G_SET_UNION requires set operands")
        return merge_gset(left, right)
    if state_class == "G_COUNTER_MAX":
        if not isinstance(left, dict) or not isinstance(right, dict):
            raise TypeError("G_COUNTER_MAX requires per-actor counter maps")
        return merge_gcounter(left, right)
    raise AssertionError("unreachable")
