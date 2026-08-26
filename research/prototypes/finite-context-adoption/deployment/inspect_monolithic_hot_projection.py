#!/usr/bin/env python3
"""Inspect one intentionally monolithic-hot ENA projection.

This tool does not reject a projection merely because it is large. It records
injection/freshness and footprint so local fitness can be selected by evidence.
"""

from __future__ import annotations

import argparse
from pathlib import Path


DEFAULT_TREE = "7dcbb3934883ffa6cc5292a662588cafc1533cff"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--projection", type=Path, required=True)
    parser.add_argument("--expected-current-tree", default=DEFAULT_TREE)
    parser.add_argument("--declared-source-tree", required=True)
    parser.add_argument("--projection-revision", required=True)
    parser.add_argument("--context-budget-tokens", type=int)
    parser.add_argument("--resident-tokens", type=int)
    args = parser.parse_args()

    if not args.projection.is_file():
        print("injection_status=MISSING")
        print("material_posture=RECOVER_INJECTION_OR_CANONICAL_SOURCE")
        return 2

    text = args.projection.read_text(encoding="utf-8")
    byte_count = len(text.encode("utf-8"))
    line_count = len(text.splitlines())

    if args.declared_source_tree != args.expected_current_tree:
        freshness = "STALE"
        posture = "REFRESH_OR_USE_CANONICAL_SOURCE_FOR_CHANGED_DIMENSIONS"
    else:
        freshness = "CURRENT"
        posture = "USE_HOT_PROJECTION"

    print("injection_status=PRESENT")
    print(f"freshness={freshness}")
    print(f"projection_revision={args.projection_revision}")
    print(f"bytes={byte_count}")
    print(f"lines={line_count}")

    if (args.context_budget_tokens is None) != (args.resident_tokens is None):
        raise SystemExit("provide both --context-budget-tokens and --resident-tokens, or neither")
    if args.context_budget_tokens is not None:
        if args.context_budget_tokens <= 0 or args.resident_tokens < 0:
            raise SystemExit("invalid token measurements")
        fraction = args.resident_tokens / args.context_budget_tokens
        print(f"resident_tokens={args.resident_tokens}")
        print(f"context_budget_tokens={args.context_budget_tokens}")
        print(f"context_fraction={fraction:.6f}")
        if freshness == "CURRENT" and fraction > 0.35:
            posture = "USE_HOT_BUT_MEASURE_CONTEXT_PRESSURE"

    print(f"material_posture={posture}")
    print("how=HOW-C-MONOLITHIC-HOT")
    print("size_is_not_automatic_failure=true")
    return 0 if freshness == "CURRENT" else 1


if __name__ == "__main__":
    raise SystemExit(main())
