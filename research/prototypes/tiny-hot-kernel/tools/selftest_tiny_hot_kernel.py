#!/usr/bin/env python3
"""Portable deterministic selftest for the Tiny Hot Kernel research prototype.

Runs only represented/static checks. It does not call an LLM and cannot prove
naturalistic trigger salience or semantic decision quality.
"""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile


def run(cmd: list[str], expect: int = 0) -> None:
    print("+", " ".join(cmd))
    proc = subprocess.run(cmd, text=True, capture_output=True)
    if proc.stdout:
        print(proc.stdout, end="")
    if proc.stderr:
        print(proc.stderr, end="", file=sys.stderr)
    if proc.returncode != expect:
        raise SystemExit(
            f"expected exit {expect}, got {proc.returncode}: {' '.join(cmd)}"
        )


def load_fixtures(path: Path) -> list[dict]:
    rows = []
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        row = json.loads(raw)
        assert isinstance(row.get("case_id"), str), (lineno, "case_id")
        assert isinstance(row.get("expected_trigger"), bool), (lineno, "expected_trigger")
        assert isinstance(row.get("primary_families"), list), (lineno, "primary_families")
        assert isinstance(row.get("allowed_families"), list), (lineno, "allowed_families")
        assert row.get("resolver_state") in {"AVAILABLE", "BROKEN"}, (lineno, "resolver_state")
        rows.append(row)
    ids = [row["case_id"] for row in rows]
    assert len(ids) == len(set(ids)), "duplicate fixture case_id"
    assert len(rows) == 36, f"expected 36 fixtures, got {len(rows)}"
    return rows


def represented_result(fixture: dict) -> dict:
    triggered = fixture["expected_trigger"]
    broken = fixture["resolver_state"] == "BROKEN"
    return {
        "case_id": fixture["case_id"],
        "trigger": triggered,
        "families": fixture["primary_families"] if triggered else [],
        "matched_route_ids": [],
        "retrieval_status": ("FAILED" if broken else "SUCCESS") if triggered else "NOT_ATTEMPTED",
        "fallback_used": bool(triggered and broken),
    }


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("\n".join(json.dumps(row) for row in rows) + "\n", encoding="utf-8")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    fixtures_path = root / "fixtures" / "tiny-kernel-cases.jsonl"
    validator = root / "tools" / "validate_semantic_router.py"
    scorer = root / "tools" / "score_tiny_kernel_results.py"

    run([sys.executable, str(validator)])

    fixtures = load_fixtures(fixtures_path)
    print(f"PASS: fixture structure rows={len(fixtures)}")

    with tempfile.TemporaryDirectory(prefix="ena-tiny-kernel-") as tmp:
        tmpdir = Path(tmp)

        perfect = [represented_result(f) for f in fixtures]
        perfect_path = tmpdir / "perfect.jsonl"
        write_jsonl(perfect_path, perfect)
        run([sys.executable, str(scorer), "--results", str(perfect_path), "--strict"])

        false_success = [represented_result(f) for f in fixtures]
        for row in false_success:
            if row["case_id"] == "TK-033":
                row["retrieval_status"] = "SUCCESS"
                row["fallback_used"] = False
        false_success_path = tmpdir / "false-success.jsonl"
        write_jsonl(false_success_path, false_success)
        run(
            [sys.executable, str(scorer), "--results", str(false_success_path), "--strict"],
            expect=1,
        )

        false_negative = [represented_result(f) for f in fixtures]
        for row in false_negative:
            if row["case_id"] == "TK-003":
                row["trigger"] = False
                row["families"] = []
                row["retrieval_status"] = "NOT_ATTEMPTED"
        false_negative_path = tmpdir / "false-negative.jsonl"
        write_jsonl(false_negative_path, false_negative)
        run(
            [sys.executable, str(scorer), "--results", str(false_negative_path), "--strict"],
            expect=1,
        )

        false_positive = [represented_result(f) for f in fixtures]
        for row in false_positive:
            if row["case_id"] == "TK-011":
                row["trigger"] = True
                row["families"] = ["authority-power"]
                row["retrieval_status"] = "SUCCESS"
        false_positive_path = tmpdir / "false-positive.jsonl"
        write_jsonl(false_positive_path, false_positive)
        run(
            [sys.executable, str(scorer), "--results", str(false_positive_path), "--strict"],
            expect=1,
        )

    print("PASS: tiny-hot-kernel deterministic selftest")
    print("verification_scope=REPRESENTED_STRUCTURE_FIXTURES_AND_SCORER_BEHAVIOR_ONLY")
    print("naturalistic_salience=UNPROVEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
