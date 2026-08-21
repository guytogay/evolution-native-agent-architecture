#!/usr/bin/env python3
"""Phase C — revalidate F2 (obligation status vocabulary gate) narrowly.

V2.4.1 adds a defense-in-depth gate: any obligation status outside the shipped
vocabulary {PENDING, SATISFIED, NOT_REQUIRED, DEFERRED_AUTHORIZED, FAILED,
UNKNOWN} -> BLOCK OBLIGATION_STATUS_OUTSIDE_VOCABULARY. Vocabulary NOT expanded.

Self-contained: modules are extracted via `git show <ref>:<path>` — no local
extraction directory required. Run from anywhere inside the repo:
    python collaboration/inbox/v241-harness/phaseC_revalidate.py

Checks:
  * OPEN / GARBAGE -> rejected (F2 closed) on V2.4.1; accepted on V2.4 (old finding).
  * In-vocabulary values NOT blocked by the gate (esp. NOT_REQUIRED,
    DEFERRED_AUTHORIZED must not be accidentally treated as blocking).
  * Claim-aware narrow completion (I07) intact: SATISFIED bound -> OK;
    FAILED bound -> BLOCK (existing semantics, NOT via vocab gate).
Does NOT trust results-v241.json / f1_controls.py.
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


def load(p, n):
    s = importlib.util.spec_from_file_location(n, p)
    m = importlib.util.module_from_spec(s); sys.modules[n] = m
    s.loader.exec_module(m); return m


vc = extract(MAIN_REF, BASE_PATH)
sys.path.insert(0, os.path.dirname(vc))
V24  = load(extract(V24_REF, V24_PATH), "c_v24")
V241 = load(extract(V241_REF, V241_PATH), "c_v241")
EV = date(2026, 1, 1)

VOCAB = {"PENDING","SATISFIED","NOT_REQUIRED","DEFERRED_AUTHORIZED","FAILED","UNKNOWN"}

def base(status, claim_type="TASK_COMPLETION", closure=True):
    fx = {
        "claim": {"claim_id":"C1","claim_type":claim_type,"status":"SUPPORTED",
                  "support_relation_refs":["S1"],"required_obligation_refs":["O1"]},
        "support_registry": {"S1":{"support_id":"S1","claim_ref":"C1",
                              "support_status":"SUPPORTS","evidence_refs":["E1"]}},
        "evidence_registry": {"E1":{"evidence_id":"E1"}},
        "obligations": {"O1":{"obligation_id":"O1","materiality":"MATERIAL",
                     "trigger":{"observed":True},"status":status,
                     "required_before_claim_refs":["C1"],
                     **({"closure_evidence_refs":["E1"]} if closure else {})}},
    }
    return fx

def wrap(fx): return {"payload": fx}

CASES = [
    # (name, status, label)
    ("F2-OPEN",      "OPEN",      "outside vocab -> must BLOCK (V2.4.1); OK on V2.4"),
    ("F2-GARBAGE",   "GARBAGE",   "outside vocab -> must BLOCK"),
    ("F2-PENDING",   "PENDING",   "in vocab -> gate passes; validate_obligation governs"),
    ("F2-SATISFIED", "SATISFIED", "in vocab -> OK if claim-aware satisfied"),
    ("F2-FAILED",    "FAILED",    "in vocab -> BLOCK via existing semantics"),
    ("F2-UNKNOWN",   "UNKNOWN",   "in vocab -> validate_obligation governs"),
    ("F2-NOT_REQ",   "NOT_REQUIRED",       "in vocab -> must NOT be blocked by gate"),
    ("F2-DEFERRED",  "DEFERRED_AUTHORIZED","in vocab -> must NOT be blocked by gate"),
]

print("="*78)
print("PHASE C — F2 vocabulary gate: V2.4 (reproduce) vs V2.4.1 (closure)")
print("="*78)
all_ok = True
for name, status, label in CASES:
    s24  = V24.evaluate(wrap(base(status)), EV)
    s241 = V241.evaluate(wrap(base(status)), EV)
    gate24  = (s24[0]=="BLOCK" and "OBLIGATION_STATUS_OUTSIDE_VOCABULARY" in s24[1])
    gate241 = (s241[0]=="BLOCK" and "OBLIGATION_STATUS_OUTSIDE_VOCABULARY" in s241[1])
    outside = status not in VOCAB
    # expectations
    if outside:
        exp_v24_open = (not gate24)        # V2.4 had no gate -> OPEN accepted
        exp_v241_block = gate241           # V2.4.1 must block via vocab gate
        ok = exp_v24_open and exp_v241_block
    else:
        # in-vocab: gate must NOT fire; semantics from validate_obligation
        ok = (not gate241)
        # sanity: NOT_REQUIRED / DEFERRED_AUTHORIZED -> must not be blocked as outside vocab
        if status in ("NOT_REQUIRED","DEFERRED_AUTHORIZED"):
            ok = ok and (not gate241)
    all_ok &= ok
    print(f"\n[{'OK' if ok else 'FAIL'}] {name} status={status!r}  ({label})")
    print(f"   V2.4   : {s24[0]}:{s24[1]}")
    print(f"   V2.4.1 : {s241[0]}:{s241[1]}")

# Claim-aware narrow completion (I07) intact on V2.4.1:
# SATISFIED bound to completion claim -> OK; FAILED -> BLOCK (existing semantics, not vocab gate)
print("\n" + "="*78)
print("PHASE C — claim-aware narrow completion (I07) intact on V2.4.1")
print("="*78)
s_sat = V241.evaluate(wrap(base("SATISFIED")), EV)
s_fail= V241.evaluate(wrap(base("FAILED")), EV)
i07_ok = (s_sat[0]=="OK") and (s_fail[0]=="BLOCK" and "OBLIGATION_STATUS_OUTSIDE_VOCABULARY" not in s_fail[1])
all_ok &= i07_ok
print(f"[{'OK' if i07_ok else 'FAIL'}] SATISFIED bound -> {s_sat[0]}:{s_sat[1]} (expect OK)")
print(f"[{'OK' if i07_ok else 'FAIL'}] FAILED bound    -> {s_fail[0]}:{s_fail[1]} (expect BLOCK, NOT vocab gate)")

# Orphan obligation (no claim) with OPEN -> gate still fires (defense-in-depth at boundary)
print("\n" + "="*78)
print("PHASE C — orphan obligation (no claim) OPEN still blocked (boundary enforcement)")
print("="*78)
orphan = {"payload":{"obligations":{"O1":{"obligation_id":"O1","status":"OPEN"}}}}
s_orph = V241.evaluate(orphan, EV)
orph_ok = (s_orph[0]=="BLOCK" and "OBLIGATION_STATUS_OUTSIDE_VOCABULARY" in s_orph[1])
all_ok &= orph_ok
print(f"[{'OK' if orph_ok else 'FAIL'}] orphan OPEN -> {s_orph[0]}:{s_orph[1]}")

print("\n" + "="*78)
print(f"PHASE C RESULT: {'PASS' if all_ok else 'FAIL'}")
