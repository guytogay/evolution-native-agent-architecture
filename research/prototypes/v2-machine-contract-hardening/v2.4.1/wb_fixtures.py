#!/usr/bin/env python3
"""V2.4.1 Workbuddy independent probes — preserved verbatim.

These are the 26 Phase-A cases authored by the WorkBuddy Independent Validator
(ENA-IV-WB, PR #30, merged 371e983) against the frozen V2.4 successor. Payloads
are byte-for-byte the validator's (from
collaboration/inbox/2026-08-21-ena-v24-independent-validation-wb.probe.py);
provenance preserved. `wb_expect` is the DSH-RECONCILED expected verdict under
the V2.4.1 closure semantics, cross-checked against the validator's own
prediction text in the runner:
  - F1 findings (IND-02E/O/R/A, IND-02E-rev): the validator recommended either
    reject-key!=inner-id-as-malformed or normalize-by-inner-id; V2.4.1 adopts
    REJECT-AS-MALFORMED (Host-preferred default), so these become BLOCK
    REGISTRY_MALFORMED (explicit machine verdict, NOT a silent false BLOCK).
  - IND-01 (F2, OPEN obligation): schema-valid-input precondition machine-
    enforced at the semantic boundary -> BLOCK (vocabulary unchanged).
  - IND-04/05/06/09: documented residual boundaries, unchanged.
  - IND-07/08: conceded by the validator as defensible; unchanged.
"""
import copy

WB_CASES = []

def add(cid, wb_expect, wb_predicted, note, payload):
    WB_CASES.append({
        "id": cid,
        "kind": "WB_PROBE",
        "provenance": "WorkBuddy Independent Validator (ENA-IV-WB), PR #30, merged 371e983",
        "wb_expect": wb_expect,
        "wb_predicted": wb_predicted,
        "rationale": note,
        "payload": payload,
    })

# --- F2: obligation status vocabulary gap (OPEN not in shipped schema enum) ---
add("IND-01", "BLOCK",
    "BLOCK (independent) / actual likely OK",
    "Material observed OPEN obligation bound to completion claim; shipped triggered-obligation.v1.schema.json status enum has no OPEN -> F2 closure: schema-valid-input precondition machine-enforced -> BLOCK.",
    {
        "claim": {"claim_id": "C1", "claim_type": "TASK_COMPLETION", "status": "SUPPORTED",
                  "support_relation_refs": ["S1"], "required_obligation_refs": ["O1"]},
        "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C1",
                                    "support_status": "SUPPORTS", "evidence_refs": ["E1"]}},
        "evidence_registry": {"E1": {"evidence_id": "E1"}},
        "obligations": {"O1": {"obligation_id": "O1", "materiality": "MATERIAL",
                               "trigger": {"observed": True}, "status": "OPEN",
                               "required_before_claim_refs": ["C1"]}}
    })

# --- F1: dict-key vs inner-id divergence (evidence) ---
add("IND-02E", "BLOCK",
    "Resolve E2 (OK) or REGISTRY_MALFORMED; NOT silent false-block",
    "Evidence registry dict key 'E1' != inner evidence_id 'E2'; referenced by declared id. F1 closure: reject key!=inner-id as REGISTRY_MALFORMED (explicit verdict).",
    {
        "claim": {"claim_id": "C1", "claim_type": "SUPPORT", "status": "SUPPORTED",
                  "support_relation_refs": ["S1"]},
        "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C1",
                                    "support_status": "SUPPORTS", "evidence_refs": ["E2"]}},
        "evidence_registry": {"E1": {"evidence_id": "E2", "root_provenance": "X"}}
    })

add("IND-02E-rev", "BLOCK",
    "OK but artifact identity confused (declared E2, resolved as E1)",
    "Resolving by dict key returns artifact whose inner id disagrees. F1 closure: divergence is rejected as REGISTRY_MALFORMED, eliminating identity confusion.",
    {
        "claim": {"claim_id": "C1", "claim_type": "SUPPORT", "status": "SUPPORTED",
                  "support_relation_refs": ["S1"]},
        "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C1",
                                    "support_status": "SUPPORTS", "evidence_refs": ["E1"]}},
        "evidence_registry": {"E1": {"evidence_id": "E2", "root_provenance": "X"}}
    })

add("IND-02E-ctrl", "OK",
    "OK (control: key==id works)",
    "Evidence registry key==inner-id resolves correctly (control).",
    {
        "claim": {"claim_id": "C1", "claim_type": "SUPPORT", "status": "SUPPORTED",
                  "support_relation_refs": ["S1"]},
        "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C1",
                                    "support_status": "SUPPORTS", "evidence_refs": ["E1"]}},
        "evidence_registry": {"E1": {"evidence_id": "E1"}}
    })

# --- F1: obligation registry divergence ---
add("IND-02O", "BLOCK",
    "Resolve O2 (OK) or REGISTRY_MALFORMED; NOT silent false-block",
    "Obligation registry dict key 'O1' != inner obligation_id 'O2'; referenced by declared id. F1 closure: REGISTRY_MALFORMED.",
    {
        "claim": {"claim_id": "C1", "claim_type": "TASK_COMPLETION", "status": "SUPPORTED",
                  "support_relation_refs": ["S1"], "required_obligation_refs": ["O2"]},
        "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C1",
                                    "support_status": "SUPPORTS", "evidence_refs": ["E1"]}},
        "evidence_registry": {"E1": {"evidence_id": "E1"}},
        "obligations": {"O1": {"obligation_id": "O2", "materiality": "MATERIAL",
                               "trigger": {"observed": True}, "status": "SATISFIED",
                               "closure_evidence_refs": ["E1"], "required_before_claim_refs": ["C1"]}}
    })

# --- F1: root registry divergence ---
add("IND-02R", "BLOCK",
    "Resolve R2 (OK) or REGISTRY_MALFORMED; NOT silent false-block",
    "Root registry dict key 'R1' != inner root_id 'R2'; independence references R2. F1 closure: REGISTRY_MALFORMED.",
    {
        "support": {"support_id": "S1", "claim_ref": "C1", "support_status": "SUPPORTS",
                    "evidence_refs": ["E1"],
                    "independence_basis": {"claimed_independent_count": 1,
                                           "root_provenance": ["R2"]}},
        "evidence_registry": {"E1": {"evidence_id": "E1"}},
        "root_registry": {"R1": {"root_id": "R2"}}
    })

# --- F1: authority registry divergence ---
add("IND-02A", "BLOCK",
    "Resolve G2 (OK) or REGISTRY_MALFORMED; NOT silent false-block",
    "Authority registry dict key 'G1' != inner grant_id 'G2'; mandate references G2. F1 closure: REGISTRY_MALFORMED.",
    {
        "binding": {"authority_envelope": ["x"],
                    "mandate": {"source": "G2", "expires_at": "2099-01-01"}},
        "authority_registry": {"G1": {"grant_id": "G2", "agent": None, "host": None,
                                      "expires_at": "2099-01-01"}},
        "evidence_registry": {"E1": {"evidence_id": "E1"}}
    })

# --- representation consistency: dict missing-id backfill vs list missing-id malformed ---
add("IND-03Ea", "OK",
    "OK (dict tolerates missing id via key backfill)",
    "Evidence registry DICT with missing inner id -> backfilled from key -> OK (backfill representation remains supported).",
    {
        "claim": {"claim_id": "C1", "claim_type": "SUPPORT", "status": "SUPPORTED",
                  "support_relation_refs": ["S1"]},
        "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C1",
                                    "support_status": "SUPPORTS", "evidence_refs": ["E1"]}},
        "evidence_registry": {"E1": {}}
    })

add("IND-03Eb", "BLOCK",
    "BLOCK REGISTRY_MALFORMED (list rejects missing id)",
    "Same 'no id' as LIST -> REGISTRY_MALFORMED (representation rule: dict keys backfill; list entries must declare their id).",
    {
        "claim": {"claim_id": "C1", "claim_type": "SUPPORT", "status": "SUPPORTED",
                  "support_relation_refs": ["S1"]},
        "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C1",
                                    "support_status": "SUPPORTS", "evidence_refs": ["E1"]}},
        "evidence_registry": [{}]
    })

# --- documented residual boundaries (unchanged) ---
add("IND-04", "OK",
    "OK but UNVERIFIED (residual: omission evades existence check)",
    "Support asserts evidence_refs but no evidence registry -> no existence verification (documented boundary #1; unchanged).",
    {
        "claim": {"claim_id": "C1", "claim_type": "SUPPORT", "status": "SUPPORTED",
                  "support_relation_refs": ["S1"]},
        "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C1",
                                    "support_status": "SUPPORTS", "evidence_refs": ["E1", "E2"]}}
    })

add("IND-05", "OK",
    "BLOCK or UNKNOWN (independent) / actual likely OK",
    "Authority envelope absent -> no authorization check (documented boundary; unchanged).",
    {
        "binding": {"capabilities": [{"status": "VERIFIED_AVAILABLE",
                                      "evidence_refs": [{"grade": "E3", "ref": "E1"}]}]},
        "evidence_registry": {"E1": {"evidence_id": "E1"}}
    })

add("IND-06", "OK",
    "OK but wildcard grant = unnecessary trust boundary",
    "Grant with no agent/host scope authorizes every binding (documented boundary #2; unchanged).",
    {
        "binding": {"authority_envelope": ["x"],
                    "mandate": {"source": "G1", "expires_at": "2099-01-01"},
                    "capabilities": [{"status": "VERIFIED_AVAILABLE",
                                      "evidence_refs": [{"grade": "E3", "ref": "E1"}]}]},
        "authority_registry": {"G1": {"grant_id": "G1", "agent": None, "host": None,
                                      "expires_at": "2099-01-01"}},
        "evidence_registry": {"E1": {"evidence_id": "E1"}}
    })

add("IND-07", "BLOCK",
    "OK/UNKNOWN (independent) / actual likely BLOCK (false)",
    "Concrete provenance strings misread as registry refs when registry present -> BLOCK (conceded by validator as defensible: roots must be registered when a registry is present; unchanged).",
    {
        "support": {"support_id": "S1", "claim_ref": "C1", "support_status": "SUPPORTS",
                    "evidence_refs": ["E1"],
                    "independence_basis": {"claimed_independent_count": 2,
                                           "root_provenance": ["provA", "provB"]}},
        "evidence_registry": {"E1": {"evidence_id": "E1"}},
        "root_registry": {"R1": {"root_id": "R1"}}
    })

add("IND-08", "UNKNOWN",
    "OK (independent: provenance self-contained) / actual likely UNKNOWN",
    "Concrete strings fully satisfy independence yet absent registry yields UNKNOWN (conceded: documented P9 posture; unchanged).",
    {
        "support": {"support_id": "S1", "claim_ref": "C1", "support_status": "SUPPORTS",
                    "evidence_refs": ["E1"],
                    "independence_basis": {"claimed_independent_count": 2,
                                           "root_provenance": ["provA", "provB"]}},
        "evidence_registry": {"E1": {"evidence_id": "E1"}}
    })

add("IND-09", "UNKNOWN",
    "BLOCK (fail-closed, independent) / actual likely UNKNOWN",
    "Recovery evidence asserted but unverifiable (no registry) -> UNKNOWN (documented boundary #1/#3; unchanged).",
    {
        "transition": {"recovery_claim": {"scope": "STATE_AND_HISTORY"},
                       "state_restore": {"result": "SUCCESS", "evidence_refs": ["E1"]},
                       "history_continuity": {"status": "PRESERVED",
                                              "post_checkpoint_occurrence_delta_captured": True,
                                              "evidence_refs": ["E2"]}}
    })

# --- controls (expected to match) ---
add("IND-10", "BLOCK",
    "BLOCK HISTORY_EVIDENCE_SHARED_ROOT (control/correct)",
    "Legitimate BLOCK: history and state evidence share a root (control).",
    {
        "transition": {"recovery_claim": {"scope": "STATE_AND_HISTORY"},
                       "state_restore": {"result": "SUCCESS", "evidence_refs": ["E1"]},
                       "history_continuity": {"status": "PRESERVED",
                                              "post_checkpoint_occurrence_delta_captured": True,
                                              "evidence_refs": ["E2"]}},
        "evidence_registry": {"E1": {"evidence_id": "E1", "root_provenance": "RT"},
                              "E2": {"evidence_id": "E2", "root_provenance": "RT"}}
    })

add("IND-11", "BLOCK",
    "BLOCK REGISTRY_MALFORMED, no exception (control: exception safety)",
    "Malformed registry shape fails closed, never raises (control; R11).",
    {
        "claim": {"claim_id": "C1", "claim_type": "SUPPORT", "status": "SUPPORTED",
                  "support_relation_refs": ["S1"]},
        "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C1",
                                    "support_status": "SUPPORTS", "evidence_refs": ["E1"]}},
        "evidence_registry": "i-am-a-string"
    })

add("IND-12a", "OK",
    "OK (dedup byte-identical, control)",
    "Byte-identical duplicate ids allowed (control; R5 dedup).",
    {
        "claim": {"claim_id": "C1", "claim_type": "SUPPORT", "status": "SUPPORTED",
                  "support_relation_refs": ["S1"]},
        "support_registry": [{"support_id": "S1", "claim_ref": "C1",
                              "support_status": "SUPPORTS", "evidence_refs": ["E1"]},
                             {"support_id": "S1", "claim_ref": "C1",
                              "support_status": "SUPPORTS", "evidence_refs": ["E1"]}],
        "evidence_registry": {"E1": {"evidence_id": "E1"}}
    })

add("IND-12b", "BLOCK",
    "BLOCK DUPLICATE_REF_ID (control)",
    "Ambiguous duplicate ids rejected (control; R5).",
    {
        "claim": {"claim_id": "C1", "claim_type": "SUPPORT", "status": "SUPPORTED",
                  "support_relation_refs": ["S1"]},
        "support_registry": [{"support_id": "S1", "claim_ref": "C1",
                              "support_status": "SUPPORTS", "evidence_refs": ["E1"]},
                             {"support_id": "S1", "claim_ref": "C2",
                              "support_status": "SUPPORTS", "evidence_refs": ["E1"]}],
        "evidence_registry": {"E1": {"evidence_id": "E1"}}
    })

add("IND-13a", "UNKNOWN",
    "UNKNOWN PARTIAL_SUPPORT_ONLY (control/correct)",
    "Partial cannot establish full SUPPORTED (control; R10).",
    {
        "claim": {"claim_id": "C1", "claim_type": "SUPPORT", "status": "SUPPORTED",
                  "support_claim": "SUPPORTED", "support_relation_refs": ["S1"]},
        "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C1",
                                    "support_status": "PARTIAL", "evidence_refs": ["E1"]}},
        "evidence_registry": {"E1": {"evidence_id": "E1"}}
    })

add("IND-13b", "OK",
    "OK (control: narrowed PARTIAL accepted)",
    "Explicitly narrowed partial claim accepted (control; R10).",
    {
        "claim": {"claim_id": "C1", "claim_type": "SUPPORT", "status": "SUPPORTED",
                  "support_claim": "PARTIAL", "support_relation_refs": ["S1"]},
        "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C1",
                                    "support_status": "PARTIAL", "evidence_refs": ["E1"]}},
        "evidence_registry": {"E1": {"evidence_id": "E1"}}
    })

add("IND-14", "BLOCK",
    "BLOCK SUPPORT_TARGET_MISMATCH (control/correct)",
    "Resolved support claim_ref must equal current claim (control; R2).",
    {
        "claim": {"claim_id": "C1", "claim_type": "SUPPORT", "status": "SUPPORTED",
                  "support_relation_refs": ["S1"]},
        "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C2",
                                    "support_status": "SUPPORTS", "evidence_refs": ["E1"]}},
        "evidence_registry": {"E1": {"evidence_id": "E1"}}
    })

add("IND-15", "BLOCK",
    "BLOCK MANDATE_EXPIRED (control/correct)",
    "Expired mandate blocked (control; R9).",
    {
        "binding": {"authority_envelope": ["x"],
                    "mandate": {"source": "USER_EXPLICIT_GRANT", "expires_at": "2020-01-01"}},
        "evidence_registry": {"E1": {"evidence_id": "E1"}}
    })

add("IND-16", "BLOCK",
    "BLOCK COMPLETION_CLAIM_WITHOUT_OBLIGATION_REFS (control/correct)",
    "Completion claim without obligation refs -> BLOCK (control; R7).",
    {
        "claim": {"claim_id": "C1", "claim_type": "WORKFLOW_COMPLETION", "status": "COMPLETED",
                  "required_obligation_refs": []},
        "obligations": {}
    })

add("IND-17", "OK",
    "OK (control: clean happy path)",
    "Well-formed supported claim resolves OK (control).",
    {
        "claim": {"claim_id": "C1", "claim_type": "SUPPORT", "status": "SUPPORTED",
                  "support_relation_refs": ["S1"], "scope": {"host": "h1"}},
        "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C1",
                                    "support_status": "SUPPORTS", "evidence_refs": ["E1"],
                                    "observed_scope": {"host": "h1"}}},
        "evidence_registry": {"E1": {"evidence_id": "E1"}}
    })


def get_wb_fixtures():
    return copy.deepcopy(WB_CASES)
