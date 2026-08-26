#!/usr/bin/env python3
"""Portable selftest for plural finite-context/LITE adoption HOWs.

This checks concrete reference behavior separately. It deliberately does not
select a universal adoption winner and does not treat the currently implemented
HOW count or fixture count as an architectural constant.
"""

from __future__ import annotations

import json
from pathlib import Path

from compiled_projection_adoption import ProjectionIdentity, RuntimeAssumptions, freshness, material_posture as compiled_posture
from file_git_adoption import ColdRead, SourceIdentity, decide_material_lookup, decide_nonmaterial_lookup
from monolithic_hot_adoption import HotProjection, availability as hot_availability, context_fraction, material_posture as hot_posture
from native_host_rebind import NativeBinding, binding_posture, mapping_posture
from tool_native_adoption import RetrievalObservation, retrieval_status, material_posture as retrieval_posture


# Registry of reference HOWs that this executable selftest currently knows how
# to validate. This is implementation coverage, not an ontology slot count.
HOW_IDS = {
    "HOW-A-FILE-GIT-TINY-COLD",
    "HOW-B-TOOL-NATIVE-RETRIEVAL",
    "HOW-C-MONOLITHIC-HOT",
    "HOW-D-HYBRID-COMPILED-PROJECTION",
    "HOW-E-NATIVE-HOST-REBIND",
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


def test_native_rebind() -> None:
    bindings = [
        NativeBinding(
            property_id="mutation_pressure",
            status="NATIVE_REALIZATION",
            native_organ="wake/metabolism scan",
            behavior_ref="host://wake-scan-v3",
        ),
        NativeBinding(
            property_id="rescue_plane",
            status="PARTIAL_NATIVE_REALIZATION",
            native_organ="recovery-root/controller",
            behavior_ref="host://recovery-root-v2",
        ),
        NativeBinding(
            property_id="expression_axis",
            status="DORMANT_NOT_DECISION_CHANGING",
            material=False,
        ),
    ]
    assert mapping_posture(CURRENT.current_tree, CURRENT.current_tree, bindings) == "NATIVE_REBIND_ACCEPTABLE"
    assert binding_posture(bindings[1]) == "USE_NATIVE_ORGAN_PLUS_MINIMAL_GAP_ADAPTER"
    assert binding_posture(bindings[2]) == "DORMANT_WITHOUT_COMPLIANCE_PENALTY"

    assert mapping_posture("old-tree", CURRENT.current_tree, bindings) == "STALE_REBIND_REQUIRED"

    unsupported_claim = [
        NativeBinding(
            property_id="local_selection",
            status="NATIVE_REALIZATION",
            native_organ="evidence ceiling",
            behavior_ref=None,
        )
    ]
    assert mapping_posture(CURRENT.current_tree, CURRENT.current_tree, unsupported_claim) == "MAPPING_EVIDENCE_INSUFFICIENT"

    material_gap = [
        NativeBinding(property_id="effect_commitment", status="GAP", material=True)
    ]
    assert mapping_posture(CURRENT.current_tree, CURRENT.current_tree, material_gap) == "MATERIAL_GAP_REQUIRES_ORGAN_OR_ADAPTER"

    redundant = [
        NativeBinding(
            property_id="mutation_pressure",
            status="NATIVE_REALIZATION",
            native_organ="wake/metabolism scan",
            behavior_ref="host://wake-scan-v3",
            duplicate_ena_organ=True,
        )
    ]
    assert mapping_posture(CURRENT.current_tree, CURRENT.current_tree, redundant) == "REDUNDANT_MIGRATION_REVIEW"
    print("PASS HOW-E: native-organ mapping + stale/gap/evidence/redundancy boundaries")


def test_host_fit(root: Path) -> None:
    path = root / "fixtures" / "host-fit-cases.jsonl"
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    assert rows, "host-fit corpus must not be empty"

    ids = [row["case_id"] for row in rows]
    assert len(ids) == len(set(ids))

    multi_fit = 0
    single_fit = 0
    referenced_hows: set[str] = set()

    for row in rows:
        acceptable = row.get("acceptable_hows")
        preferred = row.get("preferred")
        assert isinstance(acceptable, list) and acceptable
        assert set(acceptable) <= HOW_IDS
        assert preferred in acceptable
        referenced_hows.update(acceptable)
        multi_fit += int(len(acceptable) > 1)
        single_fit += int(len(acceptable) == 1)

    # These are coverage floors for the synthetic corpus, not claims about the
    # natural number of Host phenotypes.
    assert multi_fit >= 1, "corpus must exercise at least one multi-fit scenario"
    assert single_fit >= 1, "corpus must exercise at least one local single-winner scenario"
    assert "HOW-E-NATIVE-HOST-REBIND" in referenced_hows, "new reference HOW must be exercised"

    by_id = {row["case_id"]: row for row in rows}
    assert by_id["FCA-005"]["preferred"] == "HOW-C-MONOLITHIC-HOT"
    assert by_id["FCA-006"]["preferred"] == "HOW-B-TOOL-NATIVE-RETRIEVAL"
    assert by_id["FCA-009"]["preferred"] == "HOW-E-NATIVE-HOST-REBIND"

    print(
        "PASS host-fit corpus:",
        f"observed_cases={len(rows)} multi_fit={multi_fit} single_fit={single_fit}",
        f"referenced_hows={','.join(sorted(referenced_hows))}",
        "cardinality=OPEN",
    )


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    test_file_git()
    test_tool_native()
    test_monolithic_hot()
    test_compiled_projection()
    test_native_rebind()
    test_host_fit(root)
    print("PASS: finite-context adoption plural HOW selftest")
    print("verification_scope=REFERENCE_ADOPTION_BEHAVIOR_AND_HOST_FIT_ONLY")
    print("implemented_how_registry_is_coverage_not_ontology=true")
    print("how_cardinality=OPEN")
    print("universal_winner=NOT_SELECTED")
    print("naturalistic_application=UNPROVEN")
    print("current_change=NO")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
