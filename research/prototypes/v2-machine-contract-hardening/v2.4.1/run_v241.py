#!/usr/bin/env python3
"""V2.4.1 accumulated-corpus replay through the ONE V2.4.1 implementation.

Corpus (provenance preserved, nothing rewritten):
  * frozen V2.4 corpus:   V2 (23) + V2.1 (18) + V2.2 (7) + migrated (5)
                          + independent I01-I16/O01-O04 (20) = 53 + 20 = 73 + 25 controls = 98
  * WorkBuddy probes:     IND-01..IND-17 (26 cases, PR #30, provenance WB)
  * V2.4.1 closure controls: F1/F2 (25 new)
  TOTAL = 149

Expected verdicts: structural oracle v2.4.1 (semantic preconditions only).
Cross-checks:
  * frozen 98: successor_v241 actual vs FROZEN V2.4 expected (results-v24.json)
    -> zero verdict flips expected;
  * WB probes: oracle expected vs reconciled wb_expect -> 26/26 expected;
  * controls: oracle expected vs declared expected_verdict -> 25/25.

Success: UNEXPECTED_VERDICTS == 0.
"""
import sys, json
from pathlib import Path
from datetime import date

HERE = Path(__file__).resolve().parent
PROTO_ROOT = HERE.parent

def _find_repo(start):
    cur = start
    for _ in range(8):
        if (cur / "releases" / "current" / "tools").exists():
            return cur
        cur = cur.parent
    return start.parent / "repo"

REPO = _find_repo(HERE)

sys.path.insert(0, str(HERE))
sys.path.insert(0, str(PROTO_ROOT / "v2.4"))
sys.path.insert(0, str(PROTO_ROOT / "v2.3"))
sys.path.insert(0, str(PROTO_ROOT / "v2.2"))
sys.path.insert(0, str(PROTO_ROOT / "v2.1"))
sys.path.insert(0, str(PROTO_ROOT))
sys.path.insert(0, str(REPO / "research" / "prototypes" / "v2-machine-contract-hardening" / "v2.4"))
sys.path.insert(0, str(REPO / "research" / "prototypes" / "v2-machine-contract-hardening" / "v2.3"))
sys.path.insert(0, str(REPO / "research" / "prototypes" / "v2-machine-contract-hardening" / "v2.2"))
sys.path.insert(0, str(REPO / "research" / "prototypes" / "v2-machine-contract-hardening" / "v2.1"))
sys.path.insert(0, str(REPO / "research" / "prototypes" / "v2-machine-contract-hardening"))

from successor_contract_v241 import evaluate as evaluate_v241
from acceptance_semantics_v241 import structural_expect as expect_v241
from fixtures import get_fixtures as get_v2_fixtures
from fixtures_v21 import get_fixtures as get_v21_fixtures
from fixtures_v22 import get_v22_fixtures
from fixtures_migrated import get_migrated_fixtures
from independent_fixtures import get_independent_fixtures
from successor_controls import get_controls
from wb_fixtures import get_wb_fixtures
from f1_controls import get_f1_controls

EVAL_TIME_DEFAULT = date(2026, 8, 20)


def per_fixture_eval_time(fx):
    et = fx.get("payload", {}).get("eval_time")
    if et:
        try:
            y, m, d = et.split("-")
            return date(int(y), int(m), int(d))
        except Exception:
            return EVAL_TIME_DEFAULT
    return EVAL_TIME_DEFAULT


def load_frozen_v24_expected():
    """Frozen V2.4 expected verdicts (results-v24.json): id -> expected."""
    p = PROTO_ROOT / "v2.4" / "results-v24.json"
    try:
        doc = json.loads(p.read_text(encoding="utf-8"))
        return {r["id"]: r["expected"] for r in doc.get("results", [])}
    except Exception:
        return {}


def main():
    frozen = get_v2_fixtures() + get_v21_fixtures() + get_v22_fixtures() + get_migrated_fixtures() + get_independent_fixtures() + get_controls()
    wb = get_wb_fixtures()
    controls = get_f1_controls()
    frozen_v24_expected = load_frozen_v24_expected()

    corpus = ([(fx, "FROZEN_V24") for fx in frozen]
              + [(fx, "WB_PROBE") for fx in wb]
              + [(fx, "F1_CONTROL") for fx in controls])

    print("=" * 118)
    print("V2.4.1 ACCUMULATED-CORPUS REPLAY — ONE V2.4.1 IMPLEMENTATION (residual closure)")
    print("=" * 118)
    print("fixture counts: FROZEN_V24=%d  WB_PROBE=%d  F1_CONTROL=%d  TOTAL=%d"
          % (len(frozen), len(wb), len(controls), len(corpus)))
    print()

    results = []
    wb_consistency = []
    frozen_preservation = []

    for fx, tag in corpus:
        et = per_fixture_eval_time(fx)
        actual, codes = evaluate_v241(fx, et)
        expected = expect_v241(fx, et)
        matched = (actual == expected)
        results.append({
            "id": fx["id"], "corpus": tag, "kind": fx.get("kind"),
            "expected": expected, "actual": actual, "codes": codes,
            "verdict_matched": matched,
            "rationale": fx.get("rationale", ""),
            "wb_expect": fx.get("wb_expect"),
        })
        if tag == "WB_PROBE":
            wb_consistency.append({"id": fx["id"], "wb_expect": fx.get("wb_expect"),
                                   "oracle_expected": expected, "consistent": expected == fx.get("wb_expect")})
        if tag == "FROZEN_V24":
            fe = frozen_v24_expected.get(fx["id"])
            if fe is not None:
                frozen_preservation.append({"id": fx["id"], "frozen_expected": fe,
                                            "successor_actual": actual, "preserved": actual == fe})

    unexpected = [r for r in results if not r["verdict_matched"]]

    print("--- per-fixture verdict correctness ---")
    print("%-48s %-10s %-10s %-9s %-9s %s" % ("id", "corpus", "kind", "expected", "actual", "match"))
    for r in results:
        print("%-48s %-10s %-10s %-9s %-9s %s" % (
            r["id"], r["corpus"], (r["kind"] or "")[:10], r["expected"], r["actual"],
            "OK" if r["verdict_matched"] else "MISMATCH"))
    print()

    print("=" * 118)
    print("VERDICT-CORRECTNESS RESULT")
    print("=" * 118)
    by_tag = {}
    for r in results:
        by_tag.setdefault(r["corpus"], []).append(r)
    for tag in ("FROZEN_V24", "WB_PROBE", "F1_CONTROL"):
        grp = by_tag.get(tag, [])
        matched = sum(1 for r in grp if r["verdict_matched"])
        print("  %-10s %d/%d matched" % (tag, matched, len(grp)))
        for r in grp:
            if not r["verdict_matched"]:
                print("      MISMATCH %s expected=%s actual=%s codes=%s" % (r["id"], r["expected"], r["actual"], r["codes"]))

    print()
    print("--- frozen V2.4 verdict preservation (successor_v241 actual vs frozen V2.4 expected) ---")
    preserved = sum(1 for p in frozen_preservation if p["preserved"])
    print("  preserved: %d/%d" % (preserved, len(frozen_preservation)))
    for p in frozen_preservation:
        if not p["preserved"]:
            print("      FLIP %s frozen=%s successor=%s" % (p["id"], p["frozen_expected"], p["successor_actual"]))

    print()
    print("--- WB probes: oracle expected vs reconciled wb_expect ---")
    wb_ok = sum(1 for c in wb_consistency if c["consistent"])
    print("  consistent: %d/%d" % (wb_ok, len(wb_consistency)))
    for c in wb_consistency:
        if not c["consistent"]:
            print("      INCONSISTENT %s wb_expect=%s oracle=%s" % (c["id"], c["wb_expect"], c["oracle_expected"]))

    from collections import Counter
    summary = {
        "TOTAL": len(corpus),
        "FROZEN_V24": len(frozen), "WB_PROBE": len(wb), "F1_CONTROL": len(controls),
        "UNEXPECTED_VERDICTS": len(unexpected),
        "frozen_v24_preserved": {"preserved": preserved, "total": len(frozen_preservation)},
        "wb_oracle_consistent": {"consistent": wb_ok, "total": len(wb_consistency)},
        "expected_verdict_counts": dict(Counter(r["expected"] for r in results)),
        "actual_verdict_counts": dict(Counter(r["actual"] for r in results)),
        "exceptions": sum(1 for r in results if r["actual"] == "EXCEPTION"),
        "evaluator_fault": sum(1 for r in results if "EVALUATOR_FAULT" in r["codes"]),
    }

    print()
    print("TOTAL_FIXTURES      : %d" % summary["TOTAL"])
    print("UNEXPECTED_VERDICTS : %d  (success criterion: 0)" % len(unexpected))
    print("FROZEN_V24_PRESERVED: %d/%d" % (preserved, len(frozen_preservation)))
    print("WB_ORACLE_CONSISTENT: %d/%d" % (wb_ok, len(wb_consistency)))
    print("expected counts     : %s" % summary["expected_verdict_counts"])
    print("actual counts       : %s" % summary["actual_verdict_counts"])
    print("exceptions / faults : %d / %d" % (summary["exceptions"], summary["evaluator_fault"]))
    if unexpected:
        print("UNEXPECTED:")
        for r in unexpected:
            print("  %-48s expected=%s actual=%s codes=%s" % (r["id"], r["expected"], r["actual"], r["codes"]))
    print()
    print("VERDICT: %s" % ("ZERO UNEXPECTED - residual closure satisfied" if not unexpected
                           else "UNEXPECTED VERDICTS PRESENT"))

    out = {
        "candidate": "v2.4.1/successor_contract_v241.py (frozen V2.4 + R12 identity rule + F2 vocabulary gate)",
        "corpus_counts": {"frozen_v24": len(frozen), "wb_probe": len(wb),
                          "f1_control": len(controls), "total": len(corpus)},
        "summary": summary,
        "results": results,
        "frozen_preservation": frozen_preservation,
        "wb_oracle_consistency": wb_consistency,
    }
    with open(HERE / "results-v241.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print()
    print("results-v241.json written (repo-relative, v2.4.1/)")

    return 1 if unexpected else 0


if __name__ == "__main__":
    sys.exit(main())
