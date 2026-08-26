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

ORACLE_ONLY_KEYS = {
    "expected_trigger",
    "primary_families",
    "allowed_families",
    "notes",
}


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


def load_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        row = json.loads(raw)
        assert isinstance(row, dict), (lineno, "row must be object")
        rows.append(row)
    return rows


def load_fixtures(path: Path) -> list[dict]:
    rows = load_jsonl(path)
    for lineno, row in enumerate(rows, 1):
        assert isinstance(row.get("case_id"), str), (lineno, "case_id")
        assert isinstance(row.get("prompt"), str), (lineno, "prompt")
        assert isinstance(row.get("expected_trigger"), bool), (lineno, "expected_trigger")
        assert isinstance(row.get("primary_families"), list), (lineno, "primary_families")
        assert isinstance(row.get("allowed_families"), list), (lineno, "allowed_families")
        assert row.get("resolver_state") in {"AVAILABLE", "BROKEN"}, (lineno, "resolver_state")
    ids = [row["case_id"] for row in rows]
    assert len(ids) == len(set(ids)), "duplicate fixture case_id"
    assert len(rows) == 36, f"expected 36 fixtures, got {len(rows)}"
    return rows


def validate_blind_prompts(prompts_path: Path, fixtures: list[dict]) -> list[dict]:
    prompts = load_jsonl(prompts_path)
    assert len(prompts) == len(fixtures), (
        f"blind prompt count {len(prompts)} != oracle count {len(fixtures)}"
    )

    by_id = {row["case_id"]: row for row in fixtures}
    seen: set[str] = set()
    for lineno, prompt in enumerate(prompts, 1):
        case_id = prompt.get("case_id")
        assert isinstance(case_id, str), (lineno, "blind case_id")
        assert case_id not in seen, (lineno, f"duplicate blind case_id {case_id}")
        seen.add(case_id)
        assert case_id in by_id, (lineno, f"blind case not in oracle: {case_id}")
        assert isinstance(prompt.get("prompt"), str), (lineno, "blind prompt")
        assert prompt.get("resolver_state") in {"AVAILABLE", "BROKEN"}, (lineno, "blind resolver_state")

        leaked = ORACLE_ONLY_KEYS & set(prompt)
        assert not leaked, (lineno, f"oracle key leak in blind prompt: {sorted(leaked)}")
        unexpected = set(prompt) - {"case_id", "prompt", "resolver_state"}
        assert not unexpected, (lineno, f"unexpected blind key(s): {sorted(unexpected)}")

        oracle = by_id[case_id]
        assert prompt["prompt"] == oracle["prompt"], (case_id, "blind/oracle prompt drift")
        assert prompt["resolver_state"] == oracle["resolver_state"], (
            case_id,
            "blind/oracle resolver-state drift",
        )

    assert seen == set(by_id), "blind/oracle case-id sets differ"
    return prompts


def represented_result(fixture: dict, kernel: str = "K-A") -> dict:
    triggered = fixture["expected_trigger"]
    broken = fixture["resolver_state"] == "BROKEN"
    return {
        "case_id": fixture["case_id"],
        "kernel": kernel,
        "trigger": triggered,
        "families": fixture["primary_families"] if triggered else [],
        "matched_route_ids": [],
        "retrieval_status": ("FAILED" if broken else "SUCCESS") if triggered else "NOT_ATTEMPTED",
        "fallback_used": bool(triggered and broken),
    }


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("\n".join(json.dumps(row) for row in rows) + "\n", encoding="utf-8")


def score_cmd(scorer: Path, results: Path) -> list[str]:
    return [
        sys.executable,
        str(scorer),
        "--results",
        str(results),
        "--expected-kernel",
        "K-A",
        "--strict",
    ]


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    fixtures_path = root / "fixtures" / "tiny-kernel-cases.jsonl"
    prompts_path = root / "fixtures" / "tiny-kernel-prompts.jsonl"
    validator = root / "tools" / "validate_semantic_router.py"
    scorer = root / "tools" / "score_tiny_kernel_results.py"

    run([sys.executable, str(validator)])

    fixtures = load_fixtures(fixtures_path)
    prompts = validate_blind_prompts(prompts_path, fixtures)
    print(f"PASS: oracle fixture structure rows={len(fixtures)}")
    print(f"PASS: blinded prompt/oracle separation rows={len(prompts)} oracle_keys_leaked=0")

    with tempfile.TemporaryDirectory(prefix="ena-tiny-kernel-") as tmp:
        tmpdir = Path(tmp)

        perfect = [represented_result(f) for f in fixtures]
        perfect_path = tmpdir / "perfect.jsonl"
        write_jsonl(perfect_path, perfect)
        run(score_cmd(scorer, perfect_path))

        false_success = [represented_result(f) for f in fixtures]
        for row in false_success:
            if row["case_id"] == "TK-033":
                row["retrieval_status"] = "SUCCESS"
                row["fallback_used"] = False
                row["families"] = []
        false_success_path = tmpdir / "false-success.jsonl"
        write_jsonl(false_success_path, false_success)
        run(score_cmd(scorer, false_success_path), expect=1)

        false_negative = [represented_result(f) for f in fixtures]
        for row in false_negative:
            if row["case_id"] == "TK-003":
                row["trigger"] = False
                row["families"] = []
                row["retrieval_status"] = "NOT_ATTEMPTED"
        false_negative_path = tmpdir / "false-negative.jsonl"
        write_jsonl(false_negative_path, false_negative)
        run(score_cmd(scorer, false_negative_path), expect=1)

        false_positive = [represented_result(f) for f in fixtures]
        for row in false_positive:
            if row["case_id"] == "TK-011":
                row["trigger"] = True
                row["families"] = ["authority-power"]
                row["retrieval_status"] = "SUCCESS"
        false_positive_path = tmpdir / "false-positive.jsonl"
        write_jsonl(false_positive_path, false_positive)
        run(score_cmd(scorer, false_positive_path), expect=1)

        mixed_kernel = [represented_result(f) for f in fixtures]
        for row in mixed_kernel:
            if row["case_id"] == "TK-014":
                row["kernel"] = "K-B"
        mixed_kernel_path = tmpdir / "mixed-kernel.jsonl"
        write_jsonl(mixed_kernel_path, mixed_kernel)
        run(score_cmd(scorer, mixed_kernel_path), expect=2)

    print("PASS: tiny-hot-kernel deterministic selftest")
    print("verification_scope=REPRESENTED_STRUCTURE_FIXTURES_SCORER_BLINDING_AND_KERNEL_BINDING_ONLY")
    print("naturalistic_salience=UNPROVEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
