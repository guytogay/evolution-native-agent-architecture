#!/usr/bin/env python3
"""V2.4 Phase 1 — independent reproduction of the independent validator's probes.

Runs the independent validator's executable probes (I01-I16, O01-O04, from the
merged PR #23 CI evidence) against the FROZEN V2.3 candidate at exact ref
8eb5a9afa4c560645b4c50dc24af7874ed54a4f2 (detached worktree; no candidate file
is modified). Records each probe's actual frozen verdict / exception.

This reproduction is DSH's own execution of the independent probes — it does
not assume the validator's reported table is correct; it regenerates the
evidence against the frozen code.
"""
import sys, json, copy
from pathlib import Path
from datetime import date

HERE = Path(__file__).resolve().parent                 # .../v2.4
FROZEN = Path(sys.argv[1]) if len(sys.argv) > 1 else (HERE.parent.parent.parent)

# import the FROZEN candidate (cumulative_contract from the frozen worktree)
sys.path.insert(0, str(FROZEN / "releases" / "current" / "tools"))
sys.path.insert(0, str(FROZEN / "research" / "prototypes" / "v2-machine-contract-hardening"))
sys.path.insert(0, str(FROZEN / "research" / "prototypes" / "v2-machine-contract-hardening" / "v2.2"))
sys.path.insert(0, str(HERE))

from cumulative_contract import evaluate
from independent_fixtures import get_independent_fixtures

NOW = date(2026, 8, 21)

def main():
    results = []
    for fx in get_independent_fixtures():
        try:
            actual, codes = evaluate(copy.deepcopy(fx), NOW)
            exc = None
        except Exception as e:
            actual, codes = "EXCEPTION", []
            exc = f"{type(e).__name__}: {e}"
        results.append({
            "id": fx["id"],
            "provenance": fx.get("provenance"),
            "independent_expect": fx.get("independent_expect"),
            "rationale": fx.get("rationale"),
            "frozen_actual": actual,
            "codes": codes,
            "exception": exc,
        })

    print("=" * 100)
    print("V2.4 PHASE 1 — REPRODUCTION OF INDEPENDENT PROBES AGAINST FROZEN CANDIDATE")
    print("frozen ref: 8eb5a9afa4c560645b4c50dc24af7874ed54a4f2")
    print("=" * 100)
    print("%-44s %-18s %-12s %-10s %s" % ("id", "independent_expect", "actual", "match", "exc/codes"))
    for r in results:
        exp = r["independent_expect"]
        act = r["frozen_actual"]
        if exp == "NO_EXCEPTION":
            match = "PASS" if act != "EXCEPTION" else "FAIL"
        elif exp == "UNKNOWN_OR_BLOCK":
            match = "PASS" if act in ("UNKNOWN", "BLOCK") else "FAIL"
        else:
            match = "PASS" if act == exp else "FAIL"
        print("%-44s %-18s %-12s %-10s %s" % (r["id"], exp, act, match, (r["exception"] or ",".join(r["codes"]))[:40]))

    out = {"frozen_ref": "8eb5a9afa4c560645b4c50dc24af7874ed54a4f2",
           "evaluated_at": str(NOW),
           "results": results}
    with open(HERE / "reproduction-v23.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print()
    print("reproduction-v23.json written (repo-relative, v2.4/)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
