#!/usr/bin/env python3
"""V0.3.3-candidate build tool: generate tools/contract-fixtures.v2.json.

Build-time migration tool (NOT a runtime dependency of the candidate). Reads the
FROZEN research regression corpus (committed, provenance intact) plus the
shipped v0.3.2 selftests and new implementation controls, and emits the
implementation-level regression corpus as one self-contained JSON fixture file.

The runtime regression suite (tools/regression_suite.py) exercises ONLY the
candidate validator against this JSON; it does not import research modules.

Provenance is preserved per case:
  DSH_HISTORICAL_V2 / _V21 / _V22 / _V23_MIGRATED  (DSH-authored historical)
  GPT56SOL_INDEPENDENT                             (GPT-5.6 Sol probes I01-I16/O01-O04, PR #23)
  WORKBUDDY_INDEPENDENT                            (WorkBuddy probes IND-01..17, PR #30)
  DSH_V24_CONTROLS / DSH_V241_CONTROLS             (successor regression controls)
  DSH_MIGRATED_V032                                (shipped v0.3.2 selftests, intentionally migrated)
  DSH_IMPLEMENTATION_CONTROLS                      (new implementation-level controls)
No historical fixture is rewritten; payloads are carried byte-for-byte.
"""
import sys, json
from pathlib import Path

HERE = Path(__file__).resolve().parent                  # .../v0.3.3-candidate/tools
CANDIDATE = HERE.parent                                 # .../v0.3.3-candidate
REPO_CAND = CANDIDATE.parent                            # .../releases
REPO = REPO_CAND.parent                                 # repo root

def _find_repo(start):
    cur = start
    for _ in range(8):
        if (cur / "releases" / "current" / "tools").exists():
            return cur
        cur = cur.parent
    return start

REPO = _find_repo(HERE)
PROTO = REPO / "research" / "prototypes" / "v2-machine-contract-hardening"

for p in (PROTO, PROTO / "v2.1", PROTO / "v2.2", PROTO / "v2.3", PROTO / "v2.4", PROTO / "v2.4.1"):
    sys.path.insert(0, str(p))

from fixtures import get_fixtures as g_v2
from fixtures_v21 import get_fixtures as g_v21
from fixtures_v22 import get_v22_fixtures as g_v22
from fixtures_migrated import get_migrated_fixtures as g_mig
from independent_fixtures import get_independent_fixtures as g_ind
from successor_controls import get_controls as g_ctrl
from wb_fixtures import get_wb_fixtures as g_wb
from f1_controls import get_f1_controls as g_f1

EVAL_DEFAULT = "2026-08-20"

SOURCES = [
    (g_v2(),  "DSH_HISTORICAL_V2"),
    (g_v21(), "DSH_HISTORICAL_V21"),
    (g_v22(), "DSH_HISTORICAL_V22"),
    (g_mig(), "DSH_HISTORICAL_V23_MIGRATED"),
    (g_ind(), "GPT56SOL_INDEPENDENT"),
    (g_ctrl(),"DSH_V24_CONTROLS"),
    (g_wb(),  "WORKBUDDY_INDEPENDENT"),
    (g_f1(),  "DSH_V241_CONTROLS"),
]

def load_frozen_expectations():
    p = PROTO / "v2.4.1" / "results-v241.json"
    doc = json.loads(p.read_text(encoding="utf-8"))
    return {r["id"]: r["expected"] for r in doc.get("results", [])}

IMPLEMENTATION_CONTROLS = [
    {"id": "IMP-01-full-stack-dict-registries", "kind": "POSITIVE", "provenance": "DSH_IMPLEMENTATION_CONTROLS",
     "expected": "OK", "payload": {
         "eval_time": EVAL_DEFAULT,
         "claim": {"claim_id": "C1", "claim_type": "TASK_COMPLETION", "status": "SUPPORTED",
                   "support_relation_refs": ["S1"], "required_obligation_refs": ["O1"]},
         "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C1", "support_status": "SUPPORTS",
                                     "evidence_refs": ["E1"], "observed_scope": {"host": "H1"}}},
         "evidence_registry": {"E1": {"evidence_id": "E1"}},
         "obligations": {"O1": {"obligation_id": "O1", "materiality": "MATERIAL", "trigger": {"observed": True},
                                "status": "SATISFIED", "closure_evidence_refs": ["E1"]}}},
     "rationale": "implementation-level happy path: all dict-form registries key==id compose to OK"},
    {"id": "IMP-02-eval-time-required", "kind": "ADVERSARIAL", "provenance": "DSH_IMPLEMENTATION_CONTROLS",
     "expected": "BLOCK", "payload": {
         "claim": {"claim_id": "C1", "claim_type": "SUPPORT", "status": "SUPPORTED",
                   "support_relation_refs": ["S1"]},
         "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C1", "support_status": "SUPPORTS",
                                     "evidence_refs": ["E1"], "observed_scope": {"host": "H1"}}},
         "evidence_registry": {"E1": {"evidence_id": "E1"}}},
     "rationale": "eval_time is caller-controlled and never silently defaulted -> EVAL_TIME_REQUIRED"},
    {"id": "IMP-03-payload-not-object", "kind": "ADVERSARIAL", "provenance": "DSH_IMPLEMENTATION_CONTROLS",
     "expected": "BLOCK", "payload": "not-an-object",
     "rationale": "exception safety: non-object payload -> REGISTRY_MALFORMED, never an exception"},
    {"id": "IMP-04-evidence-registry-list-of-strings", "kind": "ADVERSARIAL", "provenance": "DSH_IMPLEMENTATION_CONTROLS",
     "expected": "BLOCK", "payload": {
         "eval_time": EVAL_DEFAULT,
         "claim": {"claim_id": "C1", "claim_type": "SUPPORT", "status": "SUPPORTED",
                   "support_relation_refs": ["S1"]},
         "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C1", "support_status": "SUPPORTS",
                                     "evidence_refs": ["E1"], "observed_scope": {"host": "H1"}}},
         "evidence_registry": ["E1", "E2"]},
     "rationale": "malformed registry shape -> REGISTRY_MALFORMED, never an exception"},
    {"id": "IMP-05-authority-key-ne-id", "kind": "ADVERSARIAL", "provenance": "DSH_IMPLEMENTATION_CONTROLS",
     "expected": "BLOCK", "payload": {
         "eval_time": EVAL_DEFAULT,
         "binding": {"authority_envelope": ["x"], "mandate": {"source": "G2", "expires_at": "2099-01-01"}},
         "authority_registry": {"G1": {"grant_id": "G2", "agent": None, "host": None, "expires_at": "2099-01-01"}}},
     "rationale": "R12 at implementation level: authority dict key!=inner grant_id -> REGISTRY_MALFORMED"},
    {"id": "IMP-06-obligation-status-open", "kind": "ADVERSARIAL", "provenance": "DSH_IMPLEMENTATION_CONTROLS",
     "expected": "BLOCK", "payload": {
         "eval_time": EVAL_DEFAULT,
         "claim": {"claim_id": "C1", "claim_type": "TASK_COMPLETION", "status": "SUPPORTED",
                   "support_relation_refs": ["S1"], "required_obligation_refs": ["O1"]},
         "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C1", "support_status": "SUPPORTS",
                                     "evidence_refs": ["E1"], "observed_scope": {"host": "H1"}}},
         "evidence_registry": {"E1": {"evidence_id": "E1"}},
         "obligations": {"O1": {"obligation_id": "O1", "materiality": "MATERIAL", "trigger": {"observed": True},
                                "status": "OPEN"}}},
     "rationale": "F2 at implementation level: OPEN outside shipped vocabulary -> OBLIGATION_STATUS_OUTSIDE_VOCABULARY"},
]

def main():
    expectations = load_frozen_expectations()
    cases = []

    # 1. migrated v0.3.2 selftests (understood & intentionally migrated; unchanged)
    v1 = json.loads((REPO / "releases" / "current" / "tools" / "contract-fixtures.v1.json").read_text(encoding="utf-8"))
    for c in v1.get("cases", []):
        cases.append({"id": c["id"], "provenance": "DSH_MIGRATED_V032", "kind": "MIGRATED",
                      "mode": c["mode"], "input": c["input"], "expect": c["expect"],
                      "rationale": "shipped v0.3.2 selftest carried forward unchanged"})

    # 2. accumulated V2.x corpus (payloads byte-for-byte; expected from frozen v2.4.1 replay)
    for fixtures, prov in SOURCES:
        for fx in fixtures:
            fid = fx["id"]
            if fid not in expectations:
                raise SystemExit(f"missing frozen expectation for {fid}")
            payload = fx.get("payload")
            if not isinstance(payload, dict):
                raise SystemExit(f"non-dict payload for {fid}")
            et = payload.get("eval_time") or EVAL_DEFAULT
            cases.append({"id": fid, "provenance": prov, "kind": fx.get("kind", ""),
                          "mode": "case", "eval_time": et, "input": payload,
                          "expect": {"verdict": expectations[fid]},
                          "rationale": fx.get("rationale", "") or fx.get("case", "")})

    # 3. implementation controls
    for c in IMPLEMENTATION_CONTROLS:
        cases.append({"id": c["id"], "provenance": c["provenance"], "kind": c["kind"],
                      "mode": "case", "input": c["payload"],
                      "expect": {"verdict": c["expected"]},
                      "rationale": c["rationale"]})

    doc = {
        "fixture_version": "2.0",
        "ena_version": "v0.3.3-candidate",
        "purpose": "Implementation-level deterministic regression corpus for validate_contracts.validate_case(): migrated v0.3.2 selftests + accumulated V2.x falsification corpus (provenance preserved) + implementation controls.",
        "case_count": len(cases),
        "cases": cases,
    }
    out = CANDIDATE / "tools" / "contract-fixtures.v2.json"
    out.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    from collections import Counter
    prov_counts = Counter(c["provenance"] for c in cases)
    print("contract-fixtures.v2.json written:", out)
    print("total cases:", len(cases))
    for p, n in sorted(prov_counts.items()):
        print("  %-28s %d" % (p, n))

if __name__ == "__main__":
    main()
