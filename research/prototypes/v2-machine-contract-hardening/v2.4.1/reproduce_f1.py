#!/usr/bin/env python3
"""V2.4.1 Phase 0 — reproduce the WorkBuddy F1/F2 findings against the FROZEN
V2.4 successor (ref 47e0e1b; the committed v2.4/ modules, byte-identical).

Runs the WorkBuddy probes (wb_fixtures.py) through the FROZEN v2.4
successor_contract.evaluate to independently confirm:
  F1: dict-key vs inner-id divergence -> silent false BLOCK / identity confusion
      (IND-02E/O/R/A, IND-02E-rev);
  F2: OPEN obligation status reaches OK (IND-01).
Also reproduces the validator's control cases and documented boundaries.
"""
import sys, json
from pathlib import Path
from datetime import date

HERE = Path(__file__).resolve().parent                 # .../v2.4.1
PROTO_ROOT = HERE.parent                               # .../v2-machine-contract-hardening

def _find_repo(start):
    cur = start
    for _ in range(8):
        if (cur / "releases" / "current" / "tools").exists():
            return cur
        cur = cur.parent
    return start.parent / "repo"

REPO = _find_repo(HERE)

# import the FROZEN v2.4 candidate (committed, untouched)
sys.path.insert(0, str(REPO / "releases" / "current" / "tools"))
sys.path.insert(0, str(REPO / "research" / "prototypes" / "v2-machine-contract-hardening" / "v2.4"))
sys.path.insert(0, str(HERE))

from successor_contract import evaluate            # FROZEN v2.4 candidate
from wb_fixtures import get_wb_fixtures

EVAL = date(2026, 8, 21)

def main():
    results = []
    for fx in get_wb_fixtures():
        try:
            actual, codes = evaluate(fx, EVAL)
            exc = None
        except Exception as e:
            actual, codes = "EXCEPTION", []
            exc = f"{type(e).__name__}: {e}"
        results.append({"id": fx["id"], "wb_expect": fx.get("wb_expect"),
                        "wb_predicted": fx.get("wb_predicted"),
                        "frozen_actual": actual, "codes": codes, "exception": exc})

    print("=" * 108)
    print("V2.4.1 PHASE 0 — WB PROBES AGAINST FROZEN V2.4 CANDIDATE (47e0e1b)")
    print("=" * 108)
    print("%-14s %-16s %-30s %-10s %s" % ("id", "wb_expect", "predicted", "actual", "codes"))
    for r in results:
        print("%-14s %-16s %-30s %-10s %s" % (r["id"], r["wb_expect"],
              (r["wb_predicted"] or "")[:28], r["frozen_actual"], ",".join(r["codes"])[:34] or r["exception"] or ""))
    print()
    out = {"frozen_ref": "47e0e1b121b1ef1e8911c59980c99805ded5a963",
           "evaluated_at": str(EVAL), "results": results}
    with open(HERE / "reproduction-f1.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("reproduction-f1.json written (v2.4.1/)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
