#!/usr/bin/env python3
"""V2.2 cumulative replay runner.

Aggregates ALL historical fixtures (never reset):
  - V2 fixtures.py: A1..A6, A6b (adversarial), S1..S6 (second-order), P1..P10 (positive)
  - V2.1 fixtures_v21.py: A21-1..A21-9 (structural attacks), P21-1..P21-7 (positive)
  - V2.2 fixtures_v22.py: composition fixtures (V22-*)
Runs them through the CUMULATIVE contract (cumulative_contract.evaluate).
Reports one cumulative result + composition failures.
Repo-relative; calls actual implementations (base v0.3.2 validator, V2
hardened_rules, V2.1/V2.2 additions).
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
sys.path.insert(0, str(HERE / "v2.1"))
sys.path.insert(0, str(REPO / "research" / "prototypes" / "v2-machine-contract-hardening"))
sys.path.insert(0, str(REPO / "research" / "prototypes" / "v2-machine-contract-hardening" / "v2.1"))

from cumulative_contract import evaluate, EVAL_TIME_DEFAULT, VState
from fixtures import get_fixtures as get_v2_fixtures
from fixtures_v21 import get_fixtures as get_v21_fixtures
from fixtures_v22 import get_v22_fixtures

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
    all_fx = v2_fx + v21_fx + v22_fx

    print("=" * 100)
    print("V2.2 CUMULATIVE CONTRACT COMPOSITION & CLOSURE — cumulative replay")
    print("=" * 100)
    print("fixture counts: V2=%d  V2.1=%d  V2.2=%d  TOTAL=%d" % (len(v2_fx), len(v21_fx), len(v22_fx), len(all_fx)))
    print()

    results = []
    for fx in all_fx:
        et = per_fixture_eval_time(fx)
        final, codes = evaluate(fx, et)
        results.append({"id": fx["id"], "kind": fx.get("kind"), "vector": fx.get("vector"),
                        "case": fx.get("case", ""), "final": final, "codes": codes,
                        "expect_block": fx.get("expect_block", []),
                        "expect_pass": fx.get("expect_pass", False)})

    adv = [r for r in results if r["kind"] in ("ADVERSARIAL", "ATTACK", "SECOND_ORDER")]
    pos = [r for r in results if r["kind"] == "POSITIVE"]
    adv_blocked = [r for r in adv if r["final"] == "BLOCK"]
    adv_unknown = [r for r in adv if r["final"] == "UNKNOWN"]
    adv_leak = [r for r in adv if r["final"] == "OK"]
    pos_ok = [r for r in pos if r["final"] == "OK"]
    pos_unknown = [r for r in pos if r["final"] == "UNKNOWN"]
    pos_fail = [r for r in pos if r["final"] == "BLOCK"]

    print("--- per-fixture cumulative results ---")
    for r in results:
        print("  %-42s %-13s %-28s %-8s %s" % (r["id"], r["kind"], (r["vector"] or "")[:28], r["final"], r["codes"]))
    print()
    print("=" * 100)
    print("CUMULATIVE RESULT")
    print("  TOTAL_ADVERSARIAL_BLOCKED : %d / %d" % (len(adv_blocked), len(adv)))
    print("  ADVERSARIAL_UNKNOWN       : %d" % len(adv_unknown))
    print("  ADVERSARIAL_LEAK          : %d" % len(adv_leak))
    print("  TOTAL_POSITIVE_PRESERVED  : %d / %d" % (len(pos_ok), len(pos)))
    print("  POSITIVE_UNKNOWN          : %d" % len(pos_unknown))
    print("  POSITIVE_BLOCKED          : %d" % len(pos_fail))
    print()

    # ---- composition failure analysis ----
    print("=" * 100)
    print("COMPOSITION FAILURE / FINDING ANALYSIS")
    print("=" * 100)
    findings = []

    # 1. positives that were OK in isolation but now UNKNOWN/BLOCK under composition
    for r in pos_fail:
        findings.append({"type": "COMPOSITION_BLOCK_ON_POSITIVE", "id": r["id"], "codes": r["codes"],
                         "note": "legitimate control blocked by a composed protection"})
        print("  [COMPOSITION_BLOCK_ON_POSITIVE] %s codes=%s" % (r["id"], r["codes"]))
    for r in pos_unknown:
        findings.append({"type": "COMPOSITION_UNKNOWN_ON_POSITIVE", "id": r["id"], "codes": r["codes"],
                         "note": "legitimate control degrades to UNKNOWN (registry unavailable)"})
        print("  [COMPOSITION_UNKNOWN_ON_POSITIVE] %s codes=%s" % (r["id"], r["codes"]))
    for r in adv_unknown:
        findings.append({"type": "COMPOSITION_UNKNOWN_ON_ADVERSARIAL", "id": r["id"], "codes": r["codes"],
                         "note": "adversarial not conclusively blocked (UNKNOWN)"})
        print("  [COMPOSITION_UNKNOWN_ON_ADVERSARIAL] %s codes=%s" % (r["id"], r["codes"]))
    for r in adv_leak:
        findings.append({"type": "ADVERSARIAL_LEAK", "id": r["id"], "codes": r["codes"],
                         "note": "false claim survived cumulative contract"})
        print("  [ADVERSARIAL_LEAK] %s codes=%s" % (r["id"], r["codes"]))

    # 2. any adversarial whose expected block code differs from actual
    for r in adv:
        if r["final"] == "BLOCK":
            matched = [c for c in r["codes"] if c in r["expect_block"]]
            if not matched:
                findings.append({"type": "BLOCK_CODE_DRIFT", "id": r["id"],
                                 "expected": r["expect_block"], "actual": r["codes"]})
                print("  [BLOCK_CODE_DRIFT] %s expected=%s actual=%s" % (r["id"], r["expect_block"], r["codes"]))

    print()
    print("findings count: %d" % len(findings))

    out = {
        "cumulative": {
            "TOTAL_ADVERSARIAL_BLOCKED": len(adv_blocked),
            "TOTAL_ADVERSARIAL": len(adv),
            "ADVERSARIAL_UNKNOWN": len(adv_unknown),
            "TOTAL_POSITIVE_PRESERVED": len(pos_ok),
            "TOTAL_POSITIVE": len(pos),
            "POSITIVE_UNKNOWN": len(pos_unknown),
            "POSITIVE_BLOCKED": len(pos_fail),
        },
        "composition_findings": findings,
        "results": results,
        "fixture_counts": {"v2": len(v2_fx), "v21": len(v21_fx), "v22": len(v22_fx), "total": len(all_fx)},
    }
    with open(HERE / "results-v22.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print()
    print("results-v22.json written (repo-relative)")

if __name__ == "__main__":
    main()
