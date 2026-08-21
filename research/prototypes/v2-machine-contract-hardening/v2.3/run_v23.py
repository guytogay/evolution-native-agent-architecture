#!/usr/bin/env python3
"""V2.3 Acceptance Semantics & Verdict-Correctness Replay — research prototype.

Replays the ENTIRE cumulative fixture corpus through the SAME composed
candidate implementation (v2.2/cumulative_contract.py — zero candidate changes):

  corpus = V2 (23) + V2.1 (18) + V2.2 (7) historical + V2.3 migrated (5) = 53

For EVERY fixture the runner derives its EXPECTED verdict from the acceptance
semantics (acceptance_semantics.py) and compares it with the ACTUAL verdict of
the composed candidate. The report is about VERDICT CORRECTNESS, not green
count: adversarial -> BLOCK, sufficient-positive -> OK, uncertainty-positive ->
UNKNOWN, mandatory-unresolvable -> BLOCK, migrated-positive -> OK.

Success criterion: every fixture receives its semantically expected verdict,
with ZERO unexpected outcomes.

Repo-relative + portable; calls actual implementations only.
"""
import sys, json
from pathlib import Path
from datetime import date

HERE = Path(__file__).resolve().parent            # .../v2.3
PROTO_ROOT = HERE.parent                          # .../v2-machine-contract-hardening

def _find_repo(start):
    cur = start
    for _ in range(8):
        if (cur / "releases" / "current" / "tools").exists():
            return cur
        cur = cur.parent
    return start.parent / "repo"

REPO = _find_repo(HERE)

# ---- import order: REPO's committed copies win (candidate is immutable) ----
sys.path.insert(0, str(HERE))                                        # v2.3 (acceptance_semantics, fixtures_migrated)
sys.path.insert(0, str(PROTO_ROOT / "v2.2"))                         # workspace fallback
sys.path.insert(0, str(PROTO_ROOT / "v2.1"))
sys.path.insert(0, str(PROTO_ROOT))                                  # fixtures.py / hardened_rules.py fallback
sys.path.insert(0, str(REPO / "releases" / "current" / "tools"))     # base v0.3.2 validator
sys.path.insert(0, str(REPO / "research" / "prototypes" / "v2-machine-contract-hardening" / "v2.2"))
sys.path.insert(0, str(REPO / "research" / "prototypes" / "v2-machine-contract-hardening" / "v2.1"))
sys.path.insert(0, str(REPO / "research" / "prototypes" / "v2-machine-contract-hardening"))

from cumulative_contract import evaluate, EVAL_TIME_DEFAULT, VState
from acceptance_semantics import classify, expected_verdict, build_expected_manifest, CATEGORY_VERDICT
from fixtures import get_fixtures as get_v2_fixtures
from fixtures_v21 import get_fixtures as get_v21_fixtures
from fixtures_v22 import get_v22_fixtures
from fixtures_migrated import get_migrated_fixtures


def per_fixture_eval_time(fx):
    """Per-fixture explicit eval time override (no hardcoded dev date)."""
    et = fx.get("payload", {}).get("eval_time")
    if et:
        y, m, d = et.split("-")
        return date(int(y), int(m), int(d))
    return EVAL_TIME_DEFAULT


def main():
    v2_fx = get_v2_fixtures()
    v21_fx = get_v21_fixtures()
    v22_fx = get_v22_fixtures()
    mig_fx = get_migrated_fixtures()
    all_fx = v2_fx + v21_fx + v22_fx + mig_fx

    print("=" * 110)
    print("V2.3 ACCEPTANCE SEMANTICS & VERDICT-CORRECTNESS REPLAY")
    print("=" * 110)
    print("fixture counts: V2=%d  V2.1=%d  V2.2=%d  MIGRATED=%d  TOTAL=%d"
          % (len(v2_fx), len(v21_fx), len(v22_fx), len(mig_fx), len(all_fx)))
    print("candidate: cumulative_contract.evaluate (SAME composed implementation; zero candidate changes)")
    print("REPO =", REPO)
    print()

    results = []
    for fx in all_fx:
        et = per_fixture_eval_time(fx)
        actual, codes = evaluate(fx, et)
        cat = classify(fx)
        exp = expected_verdict(fx)
        results.append({
            "id": fx["id"], "kind": fx.get("kind"), "vector": fx.get("vector"),
            "case": fx.get("case", ""), "category": cat,
            "expected": exp, "actual": actual, "codes": codes,
            "verdict_matched": (actual == exp),
            "migrated_from": fx.get("migrated_from"),
        })

    unexpected = [r for r in results if not r["verdict_matched"]]

    print("--- per-fixture verdict correctness ---")
    print("%-42s %-14s %-22s %-9s %-9s %s" % ("id", "kind", "category", "expected", "actual", "match"))
    for r in results:
        mark = "OK" if r["verdict_matched"] else "MISMATCH"
        print("%-42s %-14s %-22s %-9s %-9s %s" % (
            r["id"], r["kind"], r["category"], r["expected"], r["actual"], mark))
    print()

    print("=" * 110)
    print("VERDICT-CORRECTNESS RESULT")
    print("=" * 110)
    by_cat = {}
    for r in results:
        by_cat.setdefault(r["category"], []).append(r)
    for cat in ("adversarial", "mandatory_unresolvable", "uncertainty_positive",
                "sufficient_positive", "migrated_positive"):
        grp = by_cat.get(cat, [])
        exp = CATEGORY_VERDICT[cat]
        matched = sum(1 for r in grp if r["verdict_matched"])
        print("  %-24s expect=%-7s %d/%d matched" % (cat, exp, matched, len(grp)))
        for r in grp:
            if not r["verdict_matched"]:
                print("      MISMATCH %s expected=%s actual=%s codes=%s" % (r["id"], r["expected"], r["actual"], r["codes"]))

    print()
    summary = {
        "TOTAL_FIXTURES": len(all_fx),
        "HISTORICAL": len(v2_fx) + len(v21_fx) + len(v22_fx),
        "MIGRATED": len(mig_fx),
        "UNEXPECTED_VERDICTS": len(unexpected),
        "by_category": {cat: {"count": len(by_cat.get(cat, [])),
                              "expected": CATEGORY_VERDICT[cat],
                              "matched": sum(1 for r in by_cat.get(cat, []) if r["verdict_matched"])}
                        for cat in CATEGORY_VERDICT},
    }
    print("TOTAL_FIXTURES       : %d" % summary["TOTAL_FIXTURES"])
    print("UNEXPECTED_VERDICTS  : %d  (success criterion: 0)" % len(unexpected))
    if unexpected:
        print("UNEXPECTED:")
        for r in unexpected:
            print("  %-42s expected=%s actual=%s codes=%s" % (r["id"], r["expected"], r["actual"], r["codes"]))
    print()
    print("VERDICT: %s" % ("ZERO UNEXPECTED — acceptance semantics satisfied" if not unexpected
                           else "UNEXPECTED VERDICTS PRESENT — acceptance semantics NOT satisfied"))

    # ---- outputs (repo-relative) ----
    manifest = build_expected_manifest(all_fx)
    out = {
        "acceptance_semantics": {
            "BLOCK": "materially false/invalid claim OR claim requiring mandatory support whose references cannot be resolved",
            "OK": "legitimate claim with sufficient resolvable support",
            "UNKNOWN": "legitimate but materially unverifiable claim where uncertainty is allowed (deliberately distinct from BLOCK)",
        },
        "candidate": "v2.2/cumulative_contract.py evaluate() — UNCHANGED (same composed candidate as V2.2)",
        "corpus": {
            "v2": len(v2_fx), "v21": len(v21_fx), "v22": len(v22_fx),
            "migrated": len(mig_fx), "total": len(all_fx),
        },
        "summary": summary,
        "expected_verdict_manifest": manifest,
        "results": results,
    }
    with open(HERE / "results-v23.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    with open(HERE / "expected-verdict-manifest.json", "w", encoding="utf-8") as f:
        json.dump({"acceptance_semantics": out["acceptance_semantics"],
                   "fixture_counts": out["corpus"],
                   "manifest": manifest}, f, ensure_ascii=False, indent=2)
    print()
    print("results-v23.json written")
    print("expected-verdict-manifest.json written")

    return 1 if unexpected else 0


if __name__ == "__main__":
    sys.exit(main())
