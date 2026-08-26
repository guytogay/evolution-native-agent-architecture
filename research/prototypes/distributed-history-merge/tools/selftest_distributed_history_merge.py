#!/usr/bin/env python3
"""Portable selftest for plural Distributed History Merge HOWs.

The test intentionally validates different mechanisms separately and also checks
that the Host-fit corpus allows multiple acceptable HOWs where appropriate.
It does not select one universal winner.
"""

from __future__ import annotations

import json
from pathlib import Path

from causal_sibling_reference import compare, reconciled_context
from crdt_reference import merge as crdt_merge
from event_stream_reference import Event, EventStream
from git_dag_reference import Dag, Node


HOW_IDS = {
    "HOW-A-GIT-DAG",
    "HOW-B-CAUSAL-SIBLINGS",
    "HOW-C-EVENT-SOURCING",
    "HOW-D-CRDT",
}


def expect_raises(exc_type, fn, *args, **kwargs) -> None:
    try:
        fn(*args, **kwargs)
    except exc_type:
        return
    raise AssertionError(f"expected {exc_type.__name__}: {fn.__name__}")


def test_git_dag() -> None:
    dag = Dag(
        [
            Node("R"),
            Node("A", ("R",)),
            Node("B", ("A",)),
            Node("C", ("A",)),
        ]
    )
    assert dag.relation("A", "B") == "INCOMING_DESCENDS_FROM_LOCAL"
    assert dag.relation("B", "A") == "INCOMING_IS_STALE_ANCESTOR"
    assert dag.relation("B", "C") == "DIVERGED_WITH_COMMON_ANCESTOR"
    merge = dag.merge_node("M", "B", "C")
    assert set(merge.parents) == {"B", "C"}
    print("PASS HOW-A: ancestry/stale/divergence + two-parent merge preservation")


def test_causal_siblings() -> None:
    base = {"A": 4, "B": 2}
    left = {"A": 5, "B": 2}
    right = {"A": 4, "B": 3}
    assert compare(left, base) == "LEFT_DESCENDS"
    assert compare(base, left) == "RIGHT_DESCENDS"
    assert compare(left, right) == "CONCURRENT"
    merged = reconciled_context(left, right, "R")
    assert compare(merged, left) == "LEFT_DESCENDS"
    assert compare(merged, right) == "LEFT_DESCENDS"
    print("PASS HOW-B: descendant vs concurrent sibling + reconciled context contains both")


def test_event_stream() -> None:
    stream = EventStream()
    stream.append(Event("E1", "PROPOSED", "sha:a"), expected_version=0)
    # A stale writer that still believes version=0 must not overwrite/append silently.
    expect_raises(RuntimeError, stream.append, Event("E2", "PROPOSED", "sha:b"), 0)
    # Reusing one event identity with a changed payload is not a new occurrence.
    expect_raises(ValueError, stream.append, Event("E1", "PROPOSED", "sha:changed"), 1)
    stream.append(Event("E2", "COMPETING_PROPOSAL", "sha:b"), expected_version=1)
    stream.append_reconciliation("E3", ("E1", "E2"), "sha:resolved", expected_version=2)
    assert stream.rebuild_projection() == ["PROPOSED", "COMPETING_PROPOSAL", "RECONCILIATION"]
    print("PASS HOW-C: optimistic concurrency + event identity + reconciliation lineage")


def test_crdt() -> None:
    left = {"filesystem", "shell"}
    right = {"filesystem", "browser"}
    first = crdt_merge("G_SET_UNION", left, right)
    second = crdt_merge("G_SET_UNION", right, left)
    assert first == second == {"filesystem", "shell", "browser"}
    assert crdt_merge("G_SET_UNION", first, first) == first
    # Arbitrary purpose/self-definition is deliberately not in the safe type set.
    expect_raises(ValueError, crdt_merge, "PURPOSE_TEXT", "protect autonomy", "maximize compliance")
    print("PASS HOW-D: commutative convergence + non-CRDT semantic surface rejection")


def test_host_fit_corpus(root: Path) -> None:
    fixture_path = root / "fixtures" / "host-fit-cases.jsonl"
    rows = [json.loads(line) for line in fixture_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    assert len(rows) == 8
    ids = [row["case_id"] for row in rows]
    assert len(ids) == len(set(ids))

    multi_fit = 0
    single_fit = 0
    crdt_forbidden_material = 0
    for row in rows:
        acceptable = row.get("acceptable_hows")
        forbidden = row.get("forbidden_hows")
        assert isinstance(acceptable, list) and acceptable
        assert isinstance(forbidden, list)
        assert set(acceptable) <= HOW_IDS
        assert set(forbidden) <= HOW_IDS
        assert not (set(acceptable) & set(forbidden))
        assert row.get("preferred_evidence_questions")
        multi_fit += int(len(acceptable) > 1)
        single_fit += int(len(acceptable) == 1)
        if "purpose/refusal" in row.get("host_shape", "") and "HOW-D-CRDT" in forbidden:
            crdt_forbidden_material += 1

    assert multi_fit >= 4, "corpus must preserve genuine HOW plurality"
    assert single_fit >= 2, "plurality must not forbid legitimate local winners"
    assert crdt_forbidden_material >= 1, "material semantic conflict must not be auto-CRDT by default"
    print(
        "PASS host-fit corpus:",
        f"cases={len(rows)} multi_fit={multi_fit} local_single_fit={single_fit}"
    )


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    test_git_dag()
    test_causal_siblings()
    test_event_stream()
    test_crdt()
    test_host_fit_corpus(root)
    print("PASS: distributed-history-merge plural HOW selftest")
    print("verification_scope=REFERENCE_MECHANISM_BEHAVIOR_AND_HOST_FIT_CORPUS_ONLY")
    print("universal_winner=NOT_SELECTED")
    print("semantic_truth=UNPROVEN")
    print("current_change=NO")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
