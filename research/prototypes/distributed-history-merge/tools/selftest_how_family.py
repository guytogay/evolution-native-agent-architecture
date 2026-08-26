#!/usr/bin/env python3
"""Machine selftest for the four plural Distributed History Merge HOWs.

This test keeps HOW-specific behavior separate. It does not rank a universal
winner and does not treat shared passing behavior as implementation equivalence.
"""

from __future__ import annotations

from causal_sibling_reference import compare, reconciled_context
from crdt_reference import merge as crdt_merge
from event_stream_reference import Event, EventStream
from git_dag_reference import Dag, Node


def expect_raises(exc_type, fn, label: str) -> None:
    try:
        fn()
    except exc_type:
        return
    except Exception as exc:  # pragma: no cover - diagnostic path
        raise AssertionError(f"{label}: expected {exc_type.__name__}, got {type(exc).__name__}: {exc}") from exc
    raise AssertionError(f"{label}: expected {exc_type.__name__}")


def test_git_dag() -> None:
    dag = Dag([
        Node("A"),
        Node("B", ("A",)),
        Node("C", ("A",)),
        Node("D", ("B",)),
    ])
    assert dag.relation("B", "D") == "INCOMING_DESCENDS_FROM_LOCAL"
    assert dag.relation("D", "B") == "INCOMING_IS_STALE_ANCESTOR"
    assert dag.relation("B", "C") == "DIVERGED_WITH_COMMON_ANCESTOR"
    merge = dag.merge_node("M", "B", "C")
    assert merge.parents == ("B", "C")
    expect_raises(ValueError, lambda: dag.merge_node("BAD", "B", "B"), "git distinct merge parents")
    print("PASS HOW-A Git/Merkle-DAG: ancestry, divergence, multi-parent merge")


def test_causal_siblings() -> None:
    base = {"A": 4, "B": 2}
    left = {"A": 5, "B": 2}
    right = {"A": 4, "B": 3}
    assert compare(base, base) == "EQUIVALENT"
    assert compare(left, base) == "LEFT_DESCENDS"
    assert compare(base, left) == "RIGHT_DESCENDS"
    assert compare(left, right) == "CONCURRENT"
    merged = reconciled_context(left, right, "R")
    assert compare(merged, left) == "LEFT_DESCENDS"
    assert compare(merged, right) == "LEFT_DESCENDS"
    print("PASS HOW-B causal siblings: descendant/stale/concurrent/reconciled frontier")


def test_event_sourcing() -> None:
    stream = EventStream()
    e1 = Event("E1", "PROPOSED", "sha256:p1")
    assert stream.append(e1, expected_version=0) == 1
    expect_raises(
        RuntimeError,
        lambda: stream.append(Event("E2", "OTHER", "sha256:p2"), expected_version=0),
        "event optimistic concurrency",
    )
    expect_raises(
        ValueError,
        lambda: stream.append(Event("E1", "PROPOSED", "sha256:changed"), expected_version=1),
        "event occurrence identity",
    )
    assert stream.append(Event("E2", "ALTERNATIVE", "sha256:p2"), expected_version=1) == 2
    assert stream.append_reconciliation(
        "E3", ("E1", "E2"), "sha256:merged", expected_version=2
    ) == 3
    assert stream.by_id["E3"].refs == ("E1", "E2")
    expect_raises(
        ValueError,
        lambda: stream.append_reconciliation("BAD", ("E1",), "sha256:x", expected_version=3),
        "event reconciliation input plurality",
    )
    print("PASS HOW-C event sourcing: optimistic concurrency, identity, reconciliation refs")


def test_crdt() -> None:
    a = {"filesystem", "shell"}
    b = {"filesystem", "browser"}
    ab = crdt_merge("G_SET_UNION", a, b)
    ba = crdt_merge("G_SET_UNION", b, a)
    assert ab == ba == {"filesystem", "shell", "browser"}
    assert crdt_merge("G_SET_UNION", ab, ab) == ab

    left = {"A": 2, "B": 1}
    right = {"A": 1, "B": 3}
    assert crdt_merge("G_COUNTER_MAX", left, right) == {"A": 2, "B": 3}

    expect_raises(
        ValueError,
        lambda: crdt_merge("PURPOSE_TEXT", "protect autonomy", "maximize compliance"),
        "CRDT semantic-surface rejection",
    )
    print("PASS HOW-D CRDT: convergence/idempotence + non-CRDT surface rejection")


def main() -> int:
    test_git_dag()
    test_causal_siblings()
    test_event_sourcing()
    test_crdt()
    print("PASS: plural Distributed History Merge HOW family selftest")
    print("how_ranking=NOT_PERFORMED")
    print("local_winner=NOT_INFERRED")
    print("function_parity_between_hows=NOT_CLAIMED")
    print("current_change=NO")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
