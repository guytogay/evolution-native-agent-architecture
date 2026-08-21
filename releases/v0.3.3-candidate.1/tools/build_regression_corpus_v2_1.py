#!/usr/bin/env python3
"""V0.3.3-candidate.1 build tool: generate tools/contract-fixtures.v2.1.json.

Build-time migration tool (NOT a runtime dependency). Emits the successor
closure corpus: PR #38 fresh-validator probes (43, payloads verbatim, provenance
WORKBUDDY_FRESH_VALIDATOR_PR38) + D1/D2/D3 closure controls (18, provenance
DSH_V033C1_CONTROLS). The inherited 164-case corpus (contract-fixtures.v2.json)
is carried forward UNCHANGED and is run separately by regression_suite.py.
"""
import sys, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CANDIDATE = HERE.parent
sys.path.insert(0, str(HERE))

from pr38_fixtures import get_pr38_fixtures
from d1d2d3_controls import get_d1d2d3_controls


def main():
    cases = []
    for fx in get_pr38_fixtures() + get_d1d2d3_controls():
        payload = fx["payload"]
        et = payload.get("eval_time") if isinstance(payload, dict) else None
        cases.append({"id": fx["id"], "provenance": fx["provenance"], "kind": fx.get("kind", "PR38_PROBE"),
                      "mode": "case", "eval_time": et, "input": payload,
                      "expect": {"verdict": fx["expected_verdict"]},
                      "rationale": fx.get("rationale", "")})
    doc = {
        "fixture_version": "2.1",
        "ena_version": "v0.3.3-candidate.1",
        "purpose": "Successor closure corpus: PR #38 fresh-validator probes (43) + D1/D2/D3 closure controls (18). Inherited 164-case corpus lives in contract-fixtures.v2.json (unchanged).",
        "case_count": len(cases),
        "cases": cases,
    }
    out = CANDIDATE / "tools" / "contract-fixtures.v2.1.json"
    out.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    from collections import Counter
    print("contract-fixtures.v2.1.json written:", out)
    print("total cases:", len(cases))
    for p, n in sorted(Counter(c["provenance"] for c in cases).items()):
        print("  %-32s %d" % (p, n))


if __name__ == "__main__":
    main()
