#!/usr/bin/env python3
"""Portable adversarial selftest for Distributed History Merge prototype."""

from __future__ import annotations

import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(raw) for raw in path.read_text(encoding="utf-8").splitlines() if raw.strip()]


def by_id(rows: list[dict], case_id: str) -> dict:
    for row in rows:
        if row.get("case_id") == case_id:
            return copy.deepcopy(row)
    raise KeyError(case_id)


def write_one(path: Path, row: dict) -> None:
    path.write_text(json.dumps(row) + "\n", encoding="utf-8")


def run(cmd: list[str], expect: int) -> None:
    print("+", " ".join(cmd))
    proc = subprocess.run(cmd, text=True, capture_output=True)
    if proc.stdout:
        print(proc.stdout, end="")
    if proc.stderr:
        print(proc.stderr, end="", file=sys.stderr)
    if proc.returncode != expect:
        raise SystemExit(f"expected exit {expect}, got {proc.returncode}: {' '.join(cmd)}")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    validator = root / "tools" / "validate_distributed_history_merge.py"
    fixtures = root / "fixtures" / "distributed-history-merge-cases.jsonl"

    run([sys.executable, str(validator)], expect=0)
    rows = load_jsonl(fixtures)
    assert rows, "adversarial fixture corpus must not be empty"
    ids = [row.get("case_id") for row in rows]
    assert len(ids) == len(set(ids)), "duplicate case_id"

    # These IDs are targeted regression dependencies of the mutations below.
    # Their presence is normative for this selftest version; the total fixture
    # count is not.
    required_ids = {"DHM-002", "DHM-008", "DHM-010", "DHM-011", "DHM-012"}
    assert required_ids <= set(ids), f"missing targeted regression fixtures: {sorted(required_ids - set(ids))}"

    with tempfile.TemporaryDirectory(prefix="ena-dhm-") as tmp:
        tmpdir = Path(tmp)

        # Mutation 1: hide one surviving concurrent head.
        row = by_id(rows, "DHM-002")
        row["history"]["heads"] = ["E3"]
        path = tmpdir / "hide-head.jsonl"
        write_one(path, row)
        run([sys.executable, str(validator), "--fixtures", str(path)], expect=1)

        # Mutation 2: a material resolution stops descending from one conflicting sibling.
        row = by_id(rows, "DHM-008")
        merge = next(e for e in row["history"]["events"] if e["event_id"] == "E4")
        merge["parents"] = ["E2", "E1"]
        row["history"]["state"] = "DIVERGED"
        row["history"]["closure_claim"] = "NONE"
        row["history"]["heads"] = ["E3", "E4"]
        path = tmpdir / "lost-merge-parent.jsonl"
        write_one(path, row)
        run([sys.executable, str(validator), "--fixtures", str(path)], expect=1)

        # Mutation 3: material semantic conflict is downgraded to wall-clock latest.
        row = by_id(rows, "DHM-008")
        merge = next(e for e in row["history"]["events"] if e["event_id"] == "E4")
        merge["merge_strategy"] = "WALL_CLOCK_LWW"
        path = tmpdir / "material-lww.jsonl"
        write_one(path, row)
        run([sys.executable, str(validator), "--fixtures", str(path)], expect=1)

        # Mutation 4: a stale restore claims current closure while a known remote head is absent.
        row = by_id(rows, "DHM-010")
        row["history"]["closure_claim"] = "CURRENT_CLOSED"
        path = tmpdir / "stale-closed.jsonl"
        write_one(path, row)
        run([sys.executable, str(validator), "--fixtures", str(path)], expect=1)

        # False-BLOCK control 1: deterministic non-material CRDT merge remains valid.
        row = by_id(rows, "DHM-011")
        path = tmpdir / "crdt-auto.jsonl"
        write_one(path, row)
        run([sys.executable, str(validator), "--fixtures", str(path)], expect=0)

        # False-BLOCK control 2: cheap single-writer append-only history remains valid.
        row = by_id(rows, "DHM-012")
        path = tmpdir / "linear-cheap.jsonl"
        write_one(path, row)
        run([sys.executable, str(validator), "--fixtures", str(path)], expect=0)

    print("PASS: distributed-history-merge portable adversarial selftest")
    print(f"observed_fixture_count={len(rows)}")
    print("fixture_cardinality=OPEN")
    print("verification_scope=CAUSAL_HEAD_CONFLICT_STALE_RECONCILIATION_MUTATIONS_ONLY")
    print("false_block_controls=CRDT_AUTO_NONMATERIAL,SINGLE_WRITER_LINEAR")
    print("currently_implemented_hows=GIT_DAG,CAUSAL_SIBLING,CRDT,EVENT_SOURCING")
    print("implemented_how_count_is_not_ontology=true")
    print("semantic_merge_correctness=UNPROVEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
