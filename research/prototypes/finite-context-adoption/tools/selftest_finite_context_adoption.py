#!/usr/bin/env python3
"""Portable selftest for plural finite-context/LITE adoption HOWs.

This checks concrete reference behavior separately. It deliberately does not
select a universal adoption winner.
"""

from __future__ import annotations

import json
from pathlib import Path

from compiled_projection_adoption import ProjectionIdentity, RuntimeAssumptions, freshness, material_posture as compiled_posture
from file_git_adoption import ColdRead, SourceIdentity, decide_material_lookup, decide_nonmaterial_lookup
from monolithic_hot_adoption import HotProjection, availability as hot_availability, context_fraction, material_posture as hot_posture
from tool_native_adoption import RetrievalObservation, retrieval_status, material_posture as retrieval_posture


HOW_IDS = {
    "HOW-A-FILE-GIT-TINY-COLD",
    "HOW-B-TOOL-NATIVE-RETRIEVAL",
    "HOW-C-MONOLITHIC-HOT",
    "HOW-D-HYBRID-COMPILED-PROJECTION",
}

CURRENT = SourceIdentity(
    ena_version="v0.3.6",
    current_tree="7dcbb3934883ffa6cc5292a662588cafc1533cff",
    merge_commit="74b790741653286e0f01a1483723cdeb065ec3df",
)


def test_file_git() -> None:
    good = ColdRead("05#5.5", CURRENT, True)
    assert decide_material_lookup(CURRENT, good) == "USE_COLD_TARGET"

    stale = ColdRead(
        "05#5.5",
        SourceIdentity("v0.3.5", "old-tree", "old-merge"),
        True,
    )
    assert decide_material_lookup(CURRENT, stale) == "RECOVER_EXACT_SOURCE_OR_WAIT"
    assert decide_nonmaterial_lookup(CURRENT, stale) == "PROCEED_WITH_DECLARED_SEMANTIC_UNCERTAINTY"

    missing_target = ColdRead("missing", CURRENT, False)
    assert decide_material_lookup(CURRENT, missing_target) == "BROADEN_EXACT_CANONICAL_READ"
    print("PASS HOW-A: exact source identity + material/non-material fallback")


def test_tool_native() -> None:
    good = RetrievalObservation(True, True, True, 1, True, False)
    assert retrieval_status(good) == "SUCCESS"
    assert retrieval_posture(good) == "USE_RETRIEVED_CANONICAL_MATERIAL"

    broken_with_fallback = RetrievalObservation(True, False, True, 0, True, True)
    assert retrieval_status(broken_with_fallback) == "SUCCESS_VIA_EXACT_FALLBACK"

    broken_no_fallback = RetrievalObservation(True, False, True, 0, False, False)
    assert retrieval_status(broken_no_fallback) == "FAILED"
    assert retrieval_posture(broken_no_fallback) == "NARROW_WAIT_OR_RECOVER_SOURCE"

    ambiguous = RetrievalObservation(True, True, True, 3, True, False)
    assert retrieval_status(ambiguous) == "PARTIAL_AMBIGUOUS"
    assert retrieval_posture(ambiguous) == "BROADEN_OR_DISAMBIGUATE"
    print("PASS HOW-B: native retrieval + exact fallback + honest ambiguity/failure")


def test_monolithic_hot() -> None:
    normal = HotProjection(True, True, True, 6000, 128000)
    assert hot_availability(normal) == "HOT_AVAILABLE"
    assert hot_posture(normal) == "USE_HOT_PROJECTION"

    large_but_valid = HotProjection(True, True, True, 70000, 100000)
    assert context_fraction(large_but_valid) == 0.7
    assert hot_posture(large_but_valid) == "USE_HOT_BUT_MEASURE_CONTEXT_PRESSURE"

    stale = HotProjection(True, False, True, 6000, 128000)
    assert hot_posture(stale) == "REFRESH_OR_USE_CANONICAL_SOURCE_FOR_CHANGED_DIMENSIONS"

    missing = HotProjection(False, True, True, 0, 128000)
    assert hot_availability(missing) == "MISSING_INJECTION"
    print("PASS HOW-C: monolithic hot remains valid while cost/freshness stay explicit")


def test_compiled_projection() -> None:
    projection = ProjectionIdentity(
        source_current_tree=CURRENT.current_tree,
        compiler_revision="compiler-3",
        host_profile_digest="host-A",
        projection_revision="proj-18",
    )
    runtime = RuntimeAssumptions(CURRENT.current_tree, "compiler-3", "host-A")
    assert freshness(projection, runtime) == ("CURRENT", [])
    assert compiled_posture(projection, runtime, True, True) == "USE_COMPILED_PROJECTION"

    changed_host = RuntimeAssumptions(CURRENT.current_tree, "compiler-3", "host-B")
    state, changed = freshness(projection, changed_host)
    assert state == "STALE" and "HOST_PROFILE" in changed
    assert compiled_posture(projection, changed_host, True, True) == "USE_CANONICAL_FALLBACK_AND_REFRESH_IF_RECURRING"

    changed_current = RuntimeAssumptions("new-current-tree", "compiler-3", "host-A")
    assert compiled_posture(projection, changed_current, True, False) == "NARROW_WAIT_OR_DECLARE_STALE_PROJECTION"
    print("PASS HOW-D: compiled projection source/Host/compiler invalidation + canonical fallback")


def test_host_fit(root: Path) -> None:
    path = root / "fixtures" / "host-fit-cases.jsonl"
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    assert len(rows) == 8
    ids = [row["case_id"] for row in rows]
    assert len(ids) == len(set(ids))

    multi_fit = 0
    single_fit = 0
    hot_preferred = 0
    tool_preferred = 0
    compiled_preferred = 0
    file_preferred = 0

    for row in rows:
        acceptable = row.get("acceptable_hows")
        preferred = row.get("preferred")
        assert isinstance(acceptable, list) and acceptable
        assert set(acceptable) <= HOW_IDS
        assert preferred in acceptable
        multi_fit += int(len(acceptable) > 1)
        single_fit += int(len(acceptable) == 1)
        hot_preferred += int(preferred == "HOW-C-MONOLITHIC-HOT")
        tool_preferred += int(preferred == "HOW-B-TOOL-NATIVE-RETRIEVAL")
        compiled_preferred += int(preferred == "HOW-D-HYBRID-COMPILED-PROJECTION")
        file_preferred += int(preferred == "HOW-A-FILE-GIT-TINY-COLD")

    assert multi_fit >= 5, "corpus must retain genuine cross-Host HOW plurality"
    assert single_fit >= 2, "plurality must still permit real local single winners"
    assert hot_preferred >= 1, "monolithic-hot must remain a possible local winner"
    assert tool_preferred >= 1 and compiled_preferred >= 1 and file_preferred >= 1
    print(
        "PASS host-fit corpus:",
        f"cases={len(rows)} multi_fit={multi_fit} single_fit={single_fit}",
        f"preferred[file={file_preferred},tool={tool_preferred},hot={hot_preferred},compiled={compiled_preferred}]",
    )


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    test_file_git()
    test_tool_native()
    test_monolithic_hot()
    test_compiled_projection()
    test_host_fit(root)
    print("PASS: finite-context adoption plural HOW selftest")
    print("verification_scope=REFERENCE_ADOPTION_BEHAVIOR_AND_HOST_FIT_ONLY")
    print("universal_winner=NOT_SELECTED")
    print("naturalistic_application=UNPROVEN")
    print("current_change=NO")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
