#!/usr/bin/env python3
"""V0.3.3-candidate deterministic regression suite.

Exercises the IMPLEMENTATION CANDIDATE through its real shipped validation
surface (tools/validate_contracts.py — the candidate copy of the shipped
validator) against the committed implementation-level regression corpus
(tools/contract-fixtures.v2.json). It does NOT import any research prototype
module; the corpus JSON is self-contained.

Runs:
  1. the migrated v0.3.2 semantic selftests (mode support/obligation/recovery,
     provenance DSH_MIGRATED_V032) — the shipped v0.3.2 selftests remain
     understood and intentionally migrated;
  2. the accumulated V2.x falsification corpus as composed cases (mode case,
     provenance preserved) through validate_case();
  3. implementation controls (exception safety, eval-time requirement, R12/F2
     at implementation level).

Report: verdict correctness by provenance, unexpected verdicts, uncaught
exceptions, determinism. Exit 0 iff zero unexpected verdicts AND zero
exceptions AND zero failed migrated selftests.
"""
import sys, json
from pathlib import Path

HERE = Path(__file__).resolve().parent            # .../v0.3.3-candidate/tools
sys.path.insert(0, str(HERE))

import validate_contracts as vc

FIXTURES_V1 = HERE / "contract-fixtures.v1.json"
FIXTURES_V2 = HERE / "contract-fixtures.v2.json"


def main() -> int:
    # ---- 1. migrated v0.3.2 selftests (shipped surface, unchanged) ----
    v1_result = vc.run_selftest(str(FIXTURES_V1))
    migrated = [r for r in v1_result["results"]]

    # ---- 2+3. composed corpus through validate_case via the shipped selftest path ----
    v2_result = vc.run_selftest(str(FIXTURES_V2))
    results = v2_result["results"]

    by_prov = {}
    unexpected = []
    exceptions = []
    failed_migrated = [r for r in migrated if not r["passed"]]

    corpus = json.loads(FIXTURES_V2.read_text(encoding="utf-8"))
    cases_by_id = {c["id"]: c for c in corpus["cases"]}

    for r in results:
        case = cases_by_id.get(r["id"], {})
        prov = case.get("provenance", "UNKNOWN")
        by_prov.setdefault(prov, {"total": 0, "ok": 0, "fail": 0})
        by_prov[prov]["total"] += 1
        if r["passed"]:
            by_prov[prov]["ok"] += 1
        else:
            by_prov[prov]["fail"] += 1
            unexpected.append(r)
        actual = r.get("actual") or {}
        if actual.get("verdict") == "EXCEPTION" or "EXCEPTION" in str(actual.get("codes", [])):
            exceptions.append(r["id"])
        if actual.get("code") == "EVALUATOR_FAULT":
            exceptions.append(r["id"])

    print("=" * 100)
    print("V0.3.3-CANDIDATE REGRESSION SUITE (implementation surface)")
    print("=" * 100)
    print("migrated v0.3.2 selftests : %d/%d passed (shipped surface unchanged)"
          % (len(migrated) - len(failed_migrated), len(migrated)))
    print("composed corpus total     : %d" % len(results))
    print()
    print("--- by provenance ---")
    for prov in sorted(by_prov):
        b = by_prov[prov]
        print("  %-28s %d/%d passed" % (prov, b["ok"], b["total"]))
    print()
    print("--- unexpected verdicts / failures ---")
    for r in unexpected:
        a = r.get("actual") or {}
        print("  %-46s expected=%s actual=%s codes=%s" % (
            r["id"], json.dumps(r.get("expected")), a.get("verdict"), a.get("codes")))
    if failed_migrated:
        for r in failed_migrated:
            print("  MIGRATED-FAIL %s" % r["id"])
    print()
    from collections import Counter
    verdicts = Counter((r.get("actual") or {}).get("verdict") for r in results)
    print("actual verdict counts     : %s" % dict(verdicts))
    print("unexpected verdicts       : %d" % len(unexpected))
    print("uncaught exceptions       : %d" % len(exceptions))
    print()
    ok = (not unexpected) and (not exceptions) and (not failed_migrated)
    print("RESULT: %s" % ("PASS - zero unexpected, zero exceptions, migrated selftests preserved"
                          if ok else "FAIL"))

    out = {
        "candidate": "releases/v0.3.3-candidate/tools/validate_contracts.py",
        "migrated_v032_selftest": {"total": len(migrated), "passed": len(migrated) - len(failed_migrated)},
        "composed_total": len(results),
        "by_provenance": by_prov,
        "actual_verdict_counts": dict(verdicts),
        "unexpected_verdicts": [{"id": r["id"], "expected": r.get("expected"),
                                 "actual_verdict": (r.get("actual") or {}).get("verdict"),
                                 "actual_codes": (r.get("actual") or {}).get("codes")} for r in unexpected],
        "uncaught_exceptions": exceptions,
        "passed": ok,
    }
    (HERE / "regression-results-v033candidate.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print()
    print("regression-results-v033candidate.json written")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
