#!/usr/bin/env python3
"""Small executable reference for vector-clock-like causal history comparison."""

from __future__ import annotations


def compare(left: dict[str, int], right: dict[str, int]) -> str:
    """Return EQUIVALENT, LEFT_DESCENDS, RIGHT_DESCENDS, or CONCURRENT."""
    actors = set(left) | set(right)
    left_ge = all(left.get(a, 0) >= right.get(a, 0) for a in actors)
    right_ge = all(right.get(a, 0) >= left.get(a, 0) for a in actors)
    left_gt = any(left.get(a, 0) > right.get(a, 0) for a in actors)
    right_gt = any(right.get(a, 0) > left.get(a, 0) for a in actors)

    if left_ge and right_ge:
        return "EQUIVALENT"
    if left_ge and left_gt:
        return "LEFT_DESCENDS"
    if right_ge and right_gt:
        return "RIGHT_DESCENDS"
    return "CONCURRENT"


def reconciled_context(left: dict[str, int], right: dict[str, int], actor: str) -> dict[str, int]:
    """Create a context that causally contains both inputs plus one new reconciliation dot."""
    merged = {a: max(left.get(a, 0), right.get(a, 0)) for a in set(left) | set(right)}
    merged[actor] = merged.get(actor, 0) + 1
    return merged
