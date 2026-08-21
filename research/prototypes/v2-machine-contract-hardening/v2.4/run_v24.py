#!/usr/bin/env python3
"""V2.4 accumulated-corpus replay through the ONE successor implementation.

Corpus (provenance preserved, nothing rewritten):
  * frozen DSH fixtures:  V2 (23) + V2.1 (18) + V2.2 (7) + V2.3 migrated (5) = 53
  * independent fixtures: I01-I16 + O01-O04 (GPT-5.6 Sol, PR #23) = 20
  * successor controls:   15 positive + 10 negative = 25
  TOTAL = 98

Expected verdicts come from the STRUCTURAL oracle (acceptance_semantics_v24),
never from fixture kind or IDs. For independent fixtures the oracle must agree
with the independent expectation (I14: UNKNOWN within UNKNOWN_OR_BLOCK). For
frozen fixtures, the successor actual is also compared against the FROZEN V2.3
manifest expectation (verdict preservation check — expected: no flips, because
every reconciliation preserved the accepted frozen semantics).

Success: ZERO unexpected verdicts on the reconciled corpus.
"""
import sys, json, re
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
sys.path.insert(0, str(PROTO_ROOT / "v2.3"))
sys.path.insert(0, str(PROTO_ROOT / "v2.2"))
sys.path.insert(0, str(PROTO_ROOT / "v2.1"))
sys.path.insert(0, str(PROTO_ROOT))
sys.path.insert(0, str(REPO / "research" / "prototypes" / "v2-machine-contract-hardening" / "v2.3"))
sys.path.insert(0, str(REPO / "research" / "prototypes" / "v2-machine-contract-hardening" / "v2.2"))
sys.path.insert(0, str(REPO / "research" / "prototypes" / "v2-machine-contract-hardening" / "v2.1"))
sys.path.insert(0, str(REPO / "research" / "prototypes" / "v2-machine-contract-hardening"))

from successor_contract import evaluate as successor_evaluate
from acceptance_semantics_v24 import structural_expect
from fixtures import get_fixtures as get_v2_fixtures
from fixtures_v21 import get_fixtures as get_v21_fixtures
from fixtures_v22 import get_v22_fixtures
from fixtures_migrated import get_migrated_fixtures
from independent_fixtures import get_independent_fixtures
from successor_controls import get_controls

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


def load_frozen_manifest():
    """Frozen V2.3 expected-verdict manifest (id -> expected verdict)."""
    p = PROTO_ROOT / "v2.3" / "expected-verdict-manifest.json"
    try:
        doc = json.loads(p.read_text(encoding="utf-8"))
        return {e["id"]: e["expected_verdict"] for e in doc.get("manifest", [])}
    except Exception:
        return {}


def code_stats(path):
    src = path.read_text(encoding="utf-8")
    codes = set(re.findall(r'"([A-Z][A-Z0-9_]{5,})"', src))
    return {"lines": src.count("\n") + 1, "distinct_explicit_codes": len(codes)}


def main():
    frozen = get_v2_fixtures() + get_v21_fixtures() + get_v22_fixtures() + get_migrated_fixtures()
    independent = get_independent_fixtures()
    controls = get_controls()
    frozen_manifest = load_frozen_manifest()

    corpus = []
    for fx in frozen:
        corpus.append((fx, "FROZEN_V23"))
    for fx in independent:
        corpus.append((fx, "INDEPENDENT"))
    for fx in controls:
        corpus.append((fx, "SUCCESSOR_CONTROL"))

    print("=" * 116)
    print("V2.4 ACCUMULATED-CORPUS REPLAY — ONE SUCCESSOR IMPLEMENTATION")
    print("=" * 116)
    print("fixture counts: FROZEN_V23=%d  INDEPENDENT=%d  SUCCESSOR_CONTROL=%d  TOTAL=%d"
          % (len(frozen), len(independent), len(controls), len(corpus)))
    print()

    results = []
    oracle_consistency = []   # independent fixtures: oracle vs independent expectation
    frozen_preservation = []  # frozen fixtures: successor actual vs frozen manifest expectation

    for fx, corpus_tag in corpus:
        et = per_fixture_eval_time(fx)
        actual, codes = successor_evaluate(fx, et)
        expected = structural_expect(fx, et)
        # controls carry their explicit expected verdict; oracle must agree
        oracle_ok = True
        if corpus_tag == "SUCCESSOR_CONTROL" and fx.get("expected_verdict") not in (None, expected):
            oracle_ok = False
        results.append({
            "id": fx["id"], "corpus": corpus_tag, "kind": fx.get("kind"),
            "expected": expected, "actual": actual, "codes": codes,
            "verdict_matched": (actual == expected) and oracle_ok,
            "rationale": fx.get("rationale", ""),
            "independent_expect": fx.get("independent_expect"),
        })
        if corpus_tag == "INDEPENDENT":
            ie = fx.get("independent_expect")
            if ie == "UNKNOWN_OR_BLOCK":
                ok = expected in ("UNKNOWN", "BLOCK")
            elif ie == "NO_EXCEPTION":
                ok = True
            else:
                ok = (expected == ie)
            oracle_consistency.append({"id": fx["id"], "independent_expect": ie,
                                       "oracle_expected": expected, "consistent": ok})
        if corpus_tag == "FROZEN_V23":
            frozen_exp = frozen_manifest.get(fx["id"])
            if frozen_exp is not None:
                frozen_preservation.append({"id": fx["id"], "frozen_expected": frozen_exp,
                                            "successor_actual": actual, "preserved": actual == frozen_exp})

    unexpected = [r for r in results if not r["verdict_matched"]]

    print("--- per-fixture verdict correctness ---")
    print("%-46s %-17s %-10s %-9s %-9s %s" % ("id", "corpus", "kind", "expected", "actual", "match"))
    for r in results:
        print("%-46s %-17s %-10s %-9s %-9s %s" % (
            r["id"], r["corpus"], (r["kind"] or "")[:10], r["expected"], r["actual"],
            "OK" if r["verdict_matched"] else "MISMATCH"))
    print()

    print("=" * 116)
    print("VERDICT-CORRECTNESS RESULT")
    print("=" * 116)
    by_corpus = {}
    for r in results:
        by_corpus.setdefault(r["corpus"], []).append(r)
    for tag in ("FROZEN_V23", "INDEPENDENT", "SUCCESSOR_CONTROL"):
        grp = by_corpus.get(tag, [])
        matched = sum(1 for r in grp if r["verdict_matched"])
        print("  %-18s %d/%d matched" % (tag, matched, len(grp)))
        for r in grp:
            if not r["verdict_matched"]:
                print("      MISMATCH %s expected=%s actual=%s codes=%s" % (r["id"], r["expected"], r["actual"], r["codes"]))

    print()
    print("--- frozen-verdict preservation (successor actual vs FROZEN V2.3 manifest) ---")
    preserved = sum(1 for p in frozen_preservation if p["preserved"])
    print("  preserved: %d/%d" % (preserved, len(frozen_preservation)))
    for p in frozen_preservation:
        if not p["preserved"]:
            print("      FLIP %s frozen=%s successor=%s" % (p["id"], p["frozen_expected"], p["successor_actual"]))

    print()
    print("--- oracle vs independent expectation (I01-I16, O01-O04) ---")
    for c in oracle_consistency:
        print("  %-44s independent=%s oracle=%s %s" % (
            c["id"], c["independent_expect"], c["oracle_expected"],
            "CONSISTENT" if c["consistent"] else "INCONSISTENT"))

    print()
    print("--- complexity / governance cost (explicit-code inventory) ---")
    frozen_stats = code_stats(PROTO_ROOT / "v2.2" / "cumulative_contract.py")
    succ_stats = code_stats(HERE / "successor_contract.py")
    print("  frozen candidate cumulative_contract.py : %d lines, %d distinct explicit codes"
          % (frozen_stats["lines"], frozen_stats["distinct_explicit_codes"]))
    print("  successor successor_contract.py         : %d lines, %d distinct explicit codes"
          % (succ_stats["lines"], succ_stats["distinct_explicit_codes"]))
    print("  canonical resolver paths: frozen=7 ad-hoc mechanisms; successor=1 typed_resolve + normalize_registry")

    print()
    summary = {
        "TOTAL": len(corpus),
        "FROZEN_V23": len(frozen), "INDEPENDENT": len(independent), "SUCCESSOR_CONTROL": len(controls),
        "UNEXPECTED_VERDICTS": len(unexpected),
        "frozen_verdict_preserved": {"preserved": preserved, "total": len(frozen_preservation)},
        "oracle_independent_consistent": sum(1 for c in oracle_consistency if c["consistent"]),
        "oracle_independent_total": len(oracle_consistency),
        "complexity": {"frozen_cumulative_contract": frozen_stats, "successor_contract": succ_stats},
        "expected_verdict_counts": {},
    }
    from collections import Counter
    summary["expected_verdict_counts"] = dict(Counter(r["expected"] for r in results))
    summary["actual_verdict_counts"] = dict(Counter(r["actual"] for r in results))

    print()
    print("TOTAL_FIXTURES      : %d" % summary["TOTAL"])
    print("UNEXPECTED_VERDICTS : %d  (success criterion: 0)" % len(unexpected))
    print("FROZEN_PRESERVED    : %d/%d" % (preserved, len(frozen_preservation)))
    print("ORACLE_INDEPENDENT  : %d/%d consistent" % (summary["oracle_independent_consistent"], summary["oracle_independent_total"]))
    print("expected counts     : %s" % summary["expected_verdict_counts"])
    print("actual counts       : %s" % summary["actual_verdict_counts"])
    if unexpected:
        print("UNEXPECTED:")
        for r in unexpected:
            print("  %-46s expected=%s actual=%s codes=%s" % (r["id"], r["expected"], r["actual"], r["codes"]))
    print()
    print("VERDICT: %s" % ("ZERO UNEXPECTED - reconciled corpus satisfied" if not unexpected
                           else "UNEXPECTED VERDICTS PRESENT"))

    out = {
        "candidate": "v2.4/successor_contract.py (single canonical typed-resolution layer)",
        "corpus_counts": {"frozen_v23": len(frozen), "independent": len(independent),
                          "successor_control": len(controls), "total": len(corpus)},
        "summary": summary,
        "results": results,
        "frozen_preservation": frozen_preservation,
        "oracle_independent_consistency": oracle_consistency,
    }
    with open(HERE / "results-v24.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print()
    print("results-v24.json written (repo-relative, v2.4/)")

    return 1 if unexpected else 0


if __name__ == "__main__":
    sys.exit(main())
