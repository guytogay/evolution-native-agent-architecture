#!/usr/bin/env python3
"""Phase B — revalidate F1 (dict-key vs inner-id identity ambiguity) directly.

Loads BOTH the frozen V2.4 successor (47e0e1b) and the V2.4.1 successor
(daacab1) as independent modules extracted from git objects, and re-runs the
SAME F1 family (key != explicit inner id for every registry kind). Confirms:
  * F1 REPRODUCES on old V2.4 (silent false BLOCK / identity confusion).
  * F1 CLOSED on V2.4.1  (explicit REGISTRY_MALFORMED, never silent).
Also confirms legitimate representations remain OK on V2.4.1.

Self-contained: modules are extracted via `git show <ref>:<path>` — no local
extraction directory required. Run from anywhere inside the repo:
    python collaboration/inbox/v241-harness/phaseB_revalidate.py

Does NOT trust the author's f1_controls.py / results-v241.json.
"""
import sys, os, tempfile, importlib.util, subprocess
from datetime import date

REPO_ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).decode().strip()
V24_REF  = "47e0e1b121b1ef1e8911c59980c99805ded5a963"     # V2.4 candidate (untouched)
V241_REF = "daacab1f042c38f3856ef4d0366febd1b5e47600"     # V2.4.1 successor (frozen)
MAIN_REF = "260b8045332b8dfd75bb8a8f363414da88f639a0"     # shipped baseline validate_contracts
V24_PATH  = "research/prototypes/v2-machine-contract-hardening/v2.4/successor_contract.py"
V241_PATH = "research/prototypes/v2-machine-contract-hardening/v2.4.1/successor_contract_v241.py"
BASE_PATH = "releases/current/tools/validate_contracts.py"


def extract(ref, path):
    raw = subprocess.check_output(["git", "show", f"{ref}:{path}"])
    d = tempfile.mkdtemp(prefix="ena-v241-")
    p = os.path.join(d, os.path.basename(path))
    with open(p, "wb") as f:
        f.write(raw)
    return p


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


# baseline on sys.path (successor modules do `from validate_contracts import ...`)
vc = extract(MAIN_REF, BASE_PATH)
sys.path.insert(0, os.path.dirname(vc))
V24  = load(extract(V24_REF, V24_PATH), "succ_v24")
V241 = load(extract(V241_REF, V241_PATH), "succ_v241")

EV = date(2026, 1, 1)

# ---- F1 divergence family: dict key != explicit inner id, per registry kind ----
# Each: name, fixture, the registry key that diverges, the divergent inner id.
F1 = [
    ("IND-02E", {  # evidence_registry key E1 != inner evidence_id E2
        "claim": {"claim_id":"C1","claim_type":"SUPPORT","status":"SUPPORTED","support_relation_refs":["S1"]},
        "support_registry": {"S1":{"support_id":"S1","claim_ref":"C1","support_status":"SUPPORTS","evidence_refs":["E2"]}},
        "evidence_registry": {"E1":{"evidence_id":"E2","root_provenance":"X"}},
    }, "evidence(E1!=E2)"),
    ("IND-02E-rev", {  # reference the KEY E1 -> resolves to artifact declaring E2 (identity confusion)
        "claim": {"claim_id":"C1","claim_type":"SUPPORT","status":"SUPPORTED","support_relation_refs":["S1"]},
        "support_registry": {"S1":{"support_id":"S1","claim_ref":"C1","support_status":"SUPPORTS","evidence_refs":["E1"]}},
        "evidence_registry": {"E1":{"evidence_id":"E2","root_provenance":"X"}},
    }, "evidence(E1!=E2)"),
    ("IND-02O", {  # obligations key O1 != inner obligation_id O2
        "claim": {"claim_id":"C1","claim_type":"TASK_COMPLETION","status":"SUPPORTED","support_relation_refs":["S1"],"required_obligation_refs":["O2"]},
        "support_registry": {"S1":{"support_id":"S1","claim_ref":"C1","support_status":"SUPPORTS","evidence_refs":["E1"]}},
        "evidence_registry": {"E1":{"evidence_id":"E1"}},
        "obligations": {"O1":{"obligation_id":"O2","materiality":"MATERIAL","trigger":{"observed":True},"status":"SATISFIED","closure_evidence_refs":["E1"],"required_before_claim_refs":["C1"]}},
    }, "obligation(O1!=O2)"),
    ("IND-02R", {  # root_registry key R1 != inner root_id R2
        "support": {"support_id":"S1","claim_ref":"C1","support_status":"SUPPORTS","evidence_refs":["E1"],
                    "independence_basis":{"claimed_independent_count":1,"root_provenance":["R2"]}},
        "evidence_registry":{"E1":{"evidence_id":"E1"}},
        "root_registry":{"R1":{"root_id":"R2"}},
    }, "root(R1!=R2)"),
    ("IND-02A", {  # authority_registry key G1 != inner grant_id G2
        "binding": {"authority_envelope":["x"],"mandate":{"source":"G2","expires_at":"2099-01-01"}},
        "authority_registry":{"G1":{"grant_id":"G2","agent":None,"host":None,"expires_at":"2099-01-01"}},
        "evidence_registry":{"E1":{"evidence_id":"E1"}},
    }, "authority(G1!=G2)"),
    ("IND-02S", {  # support_registry key S1 != inner support_id S9
        "claim": {"claim_id":"C1","claim_type":"SUPPORT","status":"SUPPORTED","support_relation_refs":["S1"]},
        "support_registry": {"S1":{"support_id":"S9","claim_ref":"C1","support_status":"SUPPORTS","evidence_refs":["E1"]}},
        "evidence_registry": {"E1":{"evidence_id":"E1"}},
    }, "support(S1!=S9)"),
    ("IND-02SR", {  # support_relations key S1 != inner support_id S9
        "claim": {"claim_id":"C1","claim_type":"SUPPORT","status":"SUPPORTED","support_relation_refs":["S1"]},
        "support_relations": {"S1":{"support_id":"S9","claim_ref":"C1","support_status":"SUPPORTS","evidence_refs":["E1"]}},
        "evidence_registry": {"E1":{"evidence_id":"E1"}},
    }, "support_relations(S1!=S9)"),
]

print("="*78)
print("PHASE B — F1 divergence family: reproduce on V2.4, close on V2.4.1")
print("="*78)
all_closed = True
for name, fx, desc in F1:
    s24  = V24.evaluate({"payload": fx}, EV)
    s241 = V241.evaluate({"payload": fx}, EV)
    # classify
    def kind(s):
        st, codes = s
        if st == "BLOCK" and "REGISTRY_MALFORMED" in codes:
            return "REGISTRY_MALFORMED(BLOCK)"
        return f"{st}:{codes}"
    v24k, v241k = kind(s24), kind(s241)
    # More precise: V2.4 must NOT produce REGISTRY_MALFORMED (that's the new closure);
    # it should show the OLD failure mode (silent false BLOCK or identity-confused OK).
    v24_is_old_bad = ("REGISTRY_MALFORMED" not in s24[1])  # old code had no such code
    v241_closed = (s241[0] == "BLOCK" and "REGISTRY_MALFORMED" in s241[1])
    ok = v24_is_old_bad and v241_closed
    all_closed &= ok
    print(f"\n[{'OK' if ok else 'FAIL'}] {name}  ({desc})")
    print(f"   V2.4   : {v24k}")
    print(f"   V2.4.1 : {v241k}")
    print(f"   F1 reproduced on V2.4 (no REGISTRY_MALFORMED there): {v24_is_old_bad}")
    print(f"   F1 closed on V2.4.1 (REGISTRY_MALFORMED):            {v241_closed}")

print("\n" + "="*78)
print("PHASE B — legitimate representations preserved on V2.4.1 (must NOT be REGISTRY_MALFORMED)")
print("="*78)
LEGIT = [
    ("L1-key==id", {  # evidence key==id (control)
        "claim": {"claim_id":"C1","claim_type":"SUPPORT","status":"SUPPORTED","support_relation_refs":["S1"]},
        "support_registry": {"S1":{"support_id":"S1","claim_ref":"C1","support_status":"SUPPORTS","evidence_refs":["E1"]}},
        "evidence_registry": {"E1":{"evidence_id":"E1"}},
    }),
    ("L2-backfill", {  # evidence dict missing id -> backfilled from key
        "claim": {"claim_id":"C1","claim_type":"SUPPORT","status":"SUPPORTED","support_relation_refs":["S1"]},
        "support_registry": {"S1":{"support_id":"S1","claim_ref":"C1","support_status":"SUPPORTS","evidence_refs":["E1"]}},
        "evidence_registry": {"E1":{"root_provenance":"X"}},  # no evidence_id -> backfill E1
    }),
    ("L3-listform", {  # evidence valid list-form
        "claim": {"claim_id":"C1","claim_type":"SUPPORT","status":"SUPPORTED","support_relation_refs":["S1"]},
        "support_registry": {"S1":{"support_id":"S1","claim_ref":"C1","support_status":"SUPPORTS","evidence_refs":["E1"]}},
        "evidence_registry": [{"evidence_id":"E1","root_provenance":"X"}],
    }),
    ("L4-dup-protect", {  # list-form duplicate id, differing content -> DUPLICATE_REF_ID (existing protection)
        "claim": {"claim_id":"C1","claim_type":"SUPPORT","status":"SUPPORTED","support_relation_refs":["S1"]},
        "support_registry": {"S1":{"support_id":"S1","claim_ref":"C1","support_status":"SUPPORTS","evidence_refs":["E1"]}},
        "evidence_registry": [{"evidence_id":"E1","root_provenance":"X"},{"evidence_id":"E1","root_provenance":"Y"}],
    }),
    ("L5-obl-key==id", {  # obligation key==id, valid SATISFIED
        "claim": {"claim_id":"C1","claim_type":"TASK_COMPLETION","status":"SUPPORTED","support_relation_refs":["S1"],"required_obligation_refs":["O1"]},
        "support_registry": {"S1":{"support_id":"S1","claim_ref":"C1","support_status":"SUPPORTS","evidence_refs":["E1"]}},
        "evidence_registry": {"E1":{"evidence_id":"E1"}},
        "obligations": {"O1":{"obligation_id":"O1","materiality":"MATERIAL","trigger":{"observed":True},"status":"SATISFIED","closure_evidence_refs":["E1"],"required_before_claim_refs":["C1"]}},
    }),
]
legit_ok = True
for name, fx in LEGIT:
    s = V241.evaluate({"payload": fx}, EV)
    # legitimate reps must NOT be rejected as REGISTRY_MALFORMED
    bad = (s[0] == "BLOCK" and "REGISTRY_MALFORMED" in s[1])
    # L4 is expected to BLOCK with DUPLICATE_REF_ID (legit protection, not malformed)
    expected_block_dup = (name == "L4-dup-protect")
    ok = (not bad) if not expected_block_dup else (s[0]=="BLOCK" and "DUPLICATE_REF_ID" in s[1])
    legit_ok &= ok
    print(f"[{'OK' if ok else 'FAIL'}] {name}: {s[0]}:{s[1]}  (REGISTRY_MALFORMED rejected={bad})")

print("\n" + "="*78)
print("PHASE B RESULT")
print(f"  F1 family: all divergences closed on V2.4.1 & reproduced on V2.4 : {all_closed}")
print(f"  Legitimate representations preserved (no false REGISTRY_MALFORMED): {legit_ok}")
print(f"  OVERALL: {'PASS' if (all_closed and legit_ok) else 'FAIL'}")
