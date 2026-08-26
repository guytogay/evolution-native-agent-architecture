#!/usr/bin/env python3
"""Gate one Host-native ENA retrieval result before material use.

The Host remains responsible for actually performing semantic search. This
script is a concrete boundary adapter: it refuses to upgrade missing/stale/
ambiguous tool output into canonical retrieval success and can verify exact
candidate paths against a local canonical fallback when supplied.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

EXPECTED_TREE = "7dcbb3934883ffa6cc5292a662588cafc1533cff"


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise SystemExit("retrieval result must be a JSON object")
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result", type=Path, required=True)
    parser.add_argument("--canonical-root", type=Path)
    parser.add_argument("--expected-current-tree", default=EXPECTED_TREE)
    args = parser.parse_args()

    result = load(args.result)
    attempted = result.get("attempted")
    tool_status = result.get("tool_status")
    source_tree = result.get("source_current_tree")
    candidates = result.get("candidates", [])

    if attempted is not True:
        print("retrieval_status=NOT_ATTEMPTED")
        print("material_posture=NARROW_WAIT_OR_USE_ANOTHER_HOW")
        return 2
    if tool_status not in {"SUCCESS", "PARTIAL", "FAILED", "UNAVAILABLE"}:
        raise SystemExit("tool_status must be SUCCESS/PARTIAL/FAILED/UNAVAILABLE")
    if source_tree != args.expected_current_tree:
        print("retrieval_status=STALE_OR_WRONG_SOURCE")
        print("material_posture=RECOVER_CANONICAL_SOURCE")
        return 2
    if not isinstance(candidates, list):
        raise SystemExit("candidates must be an array")

    exact_valid: list[dict] = []
    if args.canonical_root is not None:
        for candidate in candidates:
            if not isinstance(candidate, dict):
                continue
            rel = candidate.get("path")
            if isinstance(rel, str) and rel and (args.canonical_root / rel).is_file():
                exact_valid.append(candidate)
    else:
        exact_valid = [c for c in candidates if isinstance(c, dict)]

    if tool_status in {"FAILED", "UNAVAILABLE"}:
        print("retrieval_status=FAILED")
        print("material_posture=USE_EXACT_FALLBACK_OR_ANOTHER_HOW")
        return 2
    if not exact_valid:
        print("retrieval_status=NO_EXACT_CANDIDATE")
        print("material_posture=BROADEN_OR_USE_EXACT_FALLBACK")
        return 2
    if tool_status == "PARTIAL" or len(exact_valid) > 1:
        print(f"retrieval_status=PARTIAL_AMBIGUOUS candidates={len(exact_valid)}")
        print("material_posture=DISAMBIGUATE_BEFORE_MATERIAL_COMMITMENT")
        return 1

    chosen = exact_valid[0]
    print("retrieval_status=SUCCESS")
    print(f"canonical_path={chosen.get('path')}")
    print(f"section={chosen.get('section', '')}")
    print("material_posture=USE_RETRIEVED_CANONICAL_MATERIAL")
    print("how=HOW-B-TOOL-NATIVE-RETRIEVAL")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
