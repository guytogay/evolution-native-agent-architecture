#!/usr/bin/env python3
"""Phase A independent probe (revised). Author verdict corpus NOT read.
We execute the frozen candidate + shipped baseline against OUR fixtures only.
Corrections vs v1: support registries are list-flattened (canonical by inner id),
so dict-key/inner-id divergence only bites evidence/root/obligation/authority
registries (normalized directly as dicts). IND-01/IND-16 fixed to actually
exercise the obligation path.
"""
import sys, json
from pathlib import Path
from datetime import date

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "shipped-baseline"))
sys.path.insert(0, str(HERE))
import successor_contract as sc
from successor_contract import evaluate

EVAL = date(2026, 8, 21)

CASES = []
def add(cid, pred, note, payload):
    CASES.append((cid, pred, note, {"payload": payload}))

# --- INDEPENDENT FINDING #1: obligation status vocabulary gap (shared baseline
# blind spot). Material+observed+OPEN obligation bound to completion claim. ---
add("IND-01", "BLOCK (independent) / actual likely OK",
    "Material observed OPEN obligation bound to completion claim: baseline+succeeder accept (status vocabulary not closed; OPEN not blocking).",
    {
        "claim": {"claim_id":"C1","claim_type":"TASK_COMPLETION","status":"SUPPORTED",
                  "support_relation_refs":["S1"],"required_obligation_refs":["O1"]},
        "support_registry": {"S1":{"support_id":"S1","claim_ref":"C1",
                              "support_status":"SUPPORTS","evidence_refs":["E1"]}},
        "evidence_registry": {"E1":{"evidence_id":"E1"}},
        "obligations": {"O1":{"obligation_id":"O1","materiality":"MATERIAL",
                     "trigger":{"observed":True},"status":"OPEN",
                     "required_before_claim_refs":["C1"]}}
    })

# --- INDEPENDENT FINDING #2: dict-key vs inner-id divergence for the 4
# directly-normalized registries. Evidence registry keyed E1 but inner id E2;
# support references declared id E2 -> unreachable (FALSE BLOCK). ---
add("IND-02E", "Resolve E2 (OK) or REGISTRY_MALFORMED; NOT silent false-block",
    "Evidence registry dict key 'E1' != inner evidence_id 'E2'; referenced by declared id -> FALSE BLOCK (artifact exists but unreachable).",
    {
        "claim": {"claim_id":"C1","claim_type":"SUPPORT","status":"SUPPORTED",
                  "support_relation_refs":["S1"]},
        "support_registry": {"S1":{"support_id":"S1","claim_ref":"C1",
                              "support_status":"SUPPORTS","evidence_refs":["E2"]}},
        "evidence_registry": {"E1":{"evidence_id":"E2","root_provenance":"X"}}
    })

# reverse: reference the KEY 'E1' -> resolves to artifact whose inner id is E2 (identity confusion).
add("IND-02E-rev", "OK but artifact identity confused (declared E2, resolved as E1)",
    "Resolving by dict key returns artifact whose inner id disagrees with the ref (identity confusion).",
    {
        "claim": {"claim_id":"C1","claim_type":"SUPPORT","status":"SUPPORTED",
                  "support_relation_refs":["S1"]},
        "support_registry": {"S1":{"support_id":"S1","claim_ref":"C1",
                              "support_status":"SUPPORTS","evidence_refs":["E1"]}},
        "evidence_registry": {"E1":{"evidence_id":"E2","root_provenance":"X"}}
    })

# control: evidence dict key == inner id -> OK.
add("IND-02E-ctrl", "OK (control: key==id works)",
    "Evidence registry key==id resolves correctly.",
    {
        "claim": {"claim_id":"C1","claim_type":"SUPPORT","status":"SUPPORTED",
                  "support_relation_refs":["S1"]},
        "support_registry": {"S1":{"support_id":"S1","claim_ref":"C1",
                              "support_status":"SUPPORTS","evidence_refs":["E1"]}},
        "evidence_registry": {"E1":{"evidence_id":"E1"}}
    })

# obligation registry dict key 'O1' != inner obligation_id 'O2'; claim references O2 -> FALSE BLOCK.
add("IND-02O", "Resolve O2 (OK) or REGISTRY_MALFORMED; NOT silent false-block",
    "Obligation registry key 'O1' != inner id 'O2'; referenced by declared id -> FALSE BLOCK.",
    {
        "claim": {"claim_id":"C1","claim_type":"TASK_COMPLETION","status":"SUPPORTED",
                  "support_relation_refs":["S1"],"required_obligation_refs":["O2"]},
        "support_registry": {"S1":{"support_id":"S1","claim_ref":"C1",
                              "support_status":"SUPPORTS","evidence_refs":["E1"]}},
        "evidence_registry": {"E1":{"evidence_id":"E1"}},
        "obligations": {"O1":{"obligation_id":"O2","materiality":"MATERIAL",
                     "trigger":{"observed":True},"status":"SATISFIED",
                     "closure_evidence_refs":["E1"],"required_before_claim_refs":["C1"]}}
    })

# root registry dict key 'R1' != inner root_id 'R2'; independence references R2 -> FALSE BLOCK.
add("IND-02R", "Resolve R2 (OK) or REGISTRY_MALFORMED; NOT silent false-block",
    "Root registry key 'R1' != inner root_id 'R2'; referenced by declared id -> FALSE BLOCK.",
    {
        "support": {"support_id":"S1","claim_ref":"C1","support_status":"SUPPORTS",
                    "evidence_refs":["E1"],
                    "independence_basis":{"claimed_independent_count":1,
                        "root_provenance":["R2"]}},
        "evidence_registry":{"E1":{"evidence_id":"E1"}},
        "root_registry":{"R1":{"root_id":"R2"}}
    })

# authority registry dict key 'G1' != inner grant_id 'G2'; mandate source G2 -> FALSE BLOCK.
add("IND-02A", "Resolve G2 (OK) or REGISTRY_MALFORMED; NOT silent false-block",
    "Authority registry key 'G1' != inner grant_id 'G2'; mandate references G2 -> FALSE BLOCK.",
    {
        "binding": {"authority_envelope":["x"],
                    "mandate":{"source":"G2","expires_at":"2099-01-01"}},
        "authority_registry":{"G1":{"grant_id":"G2","agent":None,"host":None,
                              "expires_at":"2099-01-01"}},
        "evidence_registry":{"E1":{"evidence_id":"E1"}}
    })

# --- INDEPENDENT FINDING #3: dict missing-id tolerated vs list missing-id malformed
# (representation inconsistency) for directly-normalized registries. ---
add("IND-03Ea", "OK (dict tolerates missing id via key backfill)",
    "Evidence registry DICT with missing id -> backfilled from key -> OK.",
    {
        "claim": {"claim_id":"C1","claim_type":"SUPPORT","status":"SUPPORTED",
                  "support_relation_refs":["S1"]},
        "support_registry": {"S1":{"support_id":"S1","claim_ref":"C1",
                              "support_status":"SUPPORTS","evidence_refs":["E1"]}},
        "evidence_registry": {"E1":{}}
    })
add("IND-03Eb", "BLOCK REGISTRY_MALFORMED (list rejects missing id)",
    "Same 'no id' as LIST -> malformed. Dict vs list diverge (non-canonical).",
    {
        "claim": {"claim_id":"C1","claim_type":"SUPPORT","status":"SUPPORTED",
                  "support_relation_refs":["S1"]},
        "support_registry": {"S1":{"support_id":"S1","claim_ref":"C1",
                              "support_status":"SUPPORTS","evidence_refs":["E1"]}},
        "evidence_registry": [{}]
    })

# --- INDEPENDENT FINDING #4: registry omission evades evidence existence. ---
add("IND-04", "OK but UNVERIFIED (residual: omission evades existence check)",
    "Support asserts evidence_refs but no evidence registry -> no existence verification (false confidence).",
    {
        "claim": {"claim_id":"C1","claim_type":"SUPPORT","status":"SUPPORTED",
                  "support_relation_refs":["S1"]},
        "support_registry": {"S1":{"support_id":"S1","claim_ref":"C1",
                              "support_status":"SUPPORTS","evidence_refs":["E1","E2"]}}
    })

# --- INDEPENDENT FINDING #5: binding capability asserted without authority envelope. ---
add("IND-05", "BLOCK or UNKNOWN (independent) / actual likely OK",
    "Authority envelope absent -> no authorization check; capabilities asserted without mandate -> false OK.",
    {
        "binding": {"capabilities":[{"status":"VERIFIED_AVAILABLE",
                    "evidence_refs":[{"grade":"E3","ref":"E1"}]}]},
        "evidence_registry":{"E1":{"evidence_id":"E1"}}
    })

# --- INDEPENDENT FINDING #6: wildcard authority grant (no agent/host scope). ---
add("IND-06", "OK but wildcard grant = unnecessary trust boundary",
    "Grant with no agent/host scope authorizes every binding; broad trust.",
    {
        "binding": {"authority_envelope":["x"],
                    "mandate":{"source":"G1","expires_at":"2099-01-01"},
                    "capabilities":[{"status":"VERIFIED_AVAILABLE",
                        "evidence_refs":[{"grade":"E3","ref":"E1"}]}]},
        "authority_registry":{"G1":{"grant_id":"G1","agent":None,"host":None,
                              "expires_at":"2099-01-01"}},
        "evidence_registry":{"E1":{"evidence_id":"E1"}}
    })

# --- INDEPENDENT FINDING #7: concrete independence strings misread as registry refs. ---
add("IND-07", "OK/UNKNOWN (independent) / actual likely BLOCK (false)",
    "Concrete provenance strings misread as registry refs when registry present -> false BLOCK.",
    {
        "support": {"support_id":"S1","claim_ref":"C1","support_status":"SUPPORTS",
                    "evidence_refs":["E1"],
                    "independence_basis":{"claimed_independent_count":2,
                        "root_provenance":["provA","provB"]}},
        "evidence_registry":{"E1":{"evidence_id":"E1"}},
        "root_registry":{"R1":{"root_id":"R1"}}
    })

# --- INDEPENDENT FINDING #8: concrete strings + absent registry -> UNKNOWN (possibly unnecessary). ---
add("IND-08", "OK (independent: provenance self-contained) / actual likely UNKNOWN",
    "Concrete strings fully satisfy independence yet absent registry yields UNKNOWN (possibly unnecessary).",
    {
        "support": {"support_id":"S1","claim_ref":"C1","support_status":"SUPPORTS",
                    "evidence_refs":["E1"],
                    "independence_basis":{"claimed_independent_count":2,
                        "root_provenance":["provA","provB"]}},
        "evidence_registry":{"E1":{"evidence_id":"E1"}}
    })

# --- INDEPENDENT FINDING #9: recovery evidence asserted but no registry -> UNKNOWN (residual). ---
add("IND-09", "BLOCK (fail-closed, independent) / actual likely UNKNOWN",
    "Recovery evidence asserted but unverifiable (no registry) -> UNKNOWN not BLOCK (false confidence).",
    {
        "transition": {"recovery_claim":{"scope":"STATE_AND_HISTORY"},
            "state_restore":{"result":"SUCCESS","evidence_refs":["E1"]},
            "history_continuity":{"status":"PRESERVED",
                "post_checkpoint_occurrence_delta_captured":True,
                "evidence_refs":["E2"]}}
    })

# --- controls (expected to match) ---
add("IND-10", "BLOCK HISTORY_EVIDENCE_SHARED_ROOT (control/correct)",
    "Legitimate BLOCK: history and state evidence share a root.",
    {
        "transition": {"recovery_claim":{"scope":"STATE_AND_HISTORY"},
            "state_restore":{"result":"SUCCESS","evidence_refs":["E1"]},
            "history_continuity":{"status":"PRESERVED",
                "post_checkpoint_occurrence_delta_captured":True,
                "evidence_refs":["E2"]}},
        "evidence_registry":{"E1":{"evidence_id":"E1","root_provenance":"RT"},
                             "E2":{"evidence_id":"E2","root_provenance":"RT"}}
    })
add("IND-11", "BLOCK REGISTRY_MALFORMED, no exception (control: exception safety)",
    "Malformed registry shape fails closed, never raises.",
    {
        "claim": {"claim_id":"C1","claim_type":"SUPPORT","status":"SUPPORTED",
                  "support_relation_refs":["S1"]},
        "support_registry": {"S1":{"support_id":"S1","claim_ref":"C1",
                              "support_status":"SUPPORTS","evidence_refs":["E1"]}},
        "evidence_registry":"i-am-a-string"
    })
add("IND-12a", "OK (dedup byte-identical, control)", "Byte-identical duplicate ids allowed.",
    {
        "claim": {"claim_id":"C1","claim_type":"SUPPORT","status":"SUPPORTED",
                  "support_relation_refs":["S1"]},
        "support_registry":[{"support_id":"S1","claim_ref":"C1",
                              "support_status":"SUPPORTS","evidence_refs":["E1"]},
                             {"support_id":"S1","claim_ref":"C1",
                              "support_status":"SUPPORTS","evidence_refs":["E1"]}],
        "evidence_registry":{"E1":{"evidence_id":"E1"}}
    })
add("IND-12b", "BLOCK DUPLICATE_REF_ID (control)", "Ambiguous duplicate ids rejected.",
    {
        "claim": {"claim_id":"C1","claim_type":"SUPPORT","status":"SUPPORTED",
                  "support_relation_refs":["S1"]},
        "support_registry":[{"support_id":"S1","claim_ref":"C1",
                              "support_status":"SUPPORTS","evidence_refs":["E1"]},
                             {"support_id":"S1","claim_ref":"C2",
                              "support_status":"SUPPORTS","evidence_refs":["E1"]}],
        "evidence_registry":{"E1":{"evidence_id":"E1"}}
    })
add("IND-13a", "UNKNOWN PARTIAL_SUPPORT_ONLY (control/correct)", "Partial cannot establish full SUPPORTED.",
    {
        "claim": {"claim_id":"C1","claim_type":"SUPPORT","status":"SUPPORTED",
                  "support_claim":"SUPPORTED","support_relation_refs":["S1"]},
        "support_registry": {"S1":{"support_id":"S1","claim_ref":"C1",
                              "support_status":"PARTIAL","evidence_refs":["E1"]}},
        "evidence_registry":{"E1":{"evidence_id":"E1"}}
    })
add("IND-13b", "OK (control: narrowed PARTIAL accepted)", "Explicitly narrowed partial claim accepted.",
    {
        "claim": {"claim_id":"C1","claim_type":"SUPPORT","status":"SUPPORTED",
                  "support_claim":"PARTIAL","support_relation_refs":["S1"]},
        "support_registry": {"S1":{"support_id":"S1","claim_ref":"C1",
                              "support_status":"PARTIAL","evidence_refs":["E1"]}},
        "evidence_registry":{"E1":{"evidence_id":"E1"}}
    })
add("IND-14", "BLOCK SUPPORT_TARGET_MISMATCH (control/correct)", "Resolved support claim_ref must equal current claim.",
    {
        "claim": {"claim_id":"C1","claim_type":"SUPPORT","status":"SUPPORTED",
                  "support_relation_refs":["S1"]},
        "support_registry": {"S1":{"support_id":"S1","claim_ref":"C2",
                              "support_status":"SUPPORTS","evidence_refs":["E1"]}},
        "evidence_registry":{"E1":{"evidence_id":"E1"}}
    })
add("IND-15", "BLOCK MANDATE_EXPIRED (control/correct)", "Expired mandate blocked.",
    {
        "binding": {"authority_envelope":["x"],
                    "mandate":{"source":"USER_EXPLICIT_GRANT","expires_at":"2020-01-01"}},
        "evidence_registry":{"E1":{"evidence_id":"E1"}}
    })
add("IND-16", "BLOCK COMPLETION_CLAIM_WITHOUT_OBLIGATION_REFS (control/correct)",
    "Completion claim (status != SUPPORTED) without obligation refs -> BLOCK.",
    {
        "claim": {"claim_id":"C1","claim_type":"WORKFLOW_COMPLETION","status":"COMPLETED",
                  "required_obligation_refs":[]},
        "obligations": {}
    })
add("IND-17", "OK (control: clean happy path)", "Well-formed supported claim resolves OK.",
    {
        "claim": {"claim_id":"C1","claim_type":"SUPPORT","status":"SUPPORTED",
                  "support_relation_refs":["S1"],"scope":{"host":"h1"}},
        "support_registry": {"S1":{"support_id":"S1","claim_ref":"C1",
                              "support_status":"SUPPORTS","evidence_refs":["E1"],
                              "observed_scope":{"host":"h1"}}},
        "evidence_registry":{"E1":{"evidence_id":"E1"}}
    })

print(f"{'CASE':12} {'PREDICTED':42} {'ACTUAL':40}")
print("-"*120)
for cid, pred, note, fix in CASES:
    try:
        state, codes = evaluate(fix, EVAL)
    except Exception as e:
        state, codes = "EXCEPTION", [f"{type(e).__name__}: {e}"]
    actual = f"{state} {','.join(codes) if codes else ''}".strip()
    print(f"{cid:12} {pred[:40]:40} {actual[:38]:38}")
    with open(HERE.parent / "phaseA_results.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps({"case":cid,"predicted":pred,"actual_state":state,
                            "actual_codes":codes,"note":note}, ensure_ascii=False)+"\n")
print("-"*120)
print("wrote phaseA_results.jsonl")
