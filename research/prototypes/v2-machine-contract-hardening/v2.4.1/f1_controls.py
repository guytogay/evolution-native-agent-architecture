#!/usr/bin/env python3
"""V2.4.1 F1/F2 closure controls — new fixtures for the residual-closure round.

Coverage per the Host instruction:
  * adversarial key!=inner-id control for EVERY affected registry kind
    (evidence/root/obligation/authority are the WorkBuddy probes IND-02E/O/R/A;
    support dict-form and support_relations dict-form are added here because the
    consistent R12 identity rule now covers them too);
  * legitimate key==inner-id controls;
  * missing-inner-id/backfill controls (dict-form backfill remains supported);
  * regression controls proving the closure did NOT reopen previous false-OK
    paths (I01/I07/I08/I09/I11/I06 families) and F2 vocabulary controls.
All new fixtures; no historical fixture rewritten.
"""
import copy

CONTROLS = []

def add(pid, kind, expected, payload, rationale):
    CONTROLS.append({"id": pid, "kind": kind, "expected_verdict": expected,
                     "rationale": rationale, "payload": payload})

# ================= adversarial: key!=inner-id (every registry kind) =========
add("F1-A-SUP-support-registry-key-ne-id", "ADVERSARIAL", "BLOCK", {
    "claim": {"claim_id": "C1", "claim_type": "SUPPORT", "status": "SUPPORTED",
              "support_relation_refs": ["S2"]},
    "support_registry": {"S1": {"support_id": "S2", "claim_ref": "C1",
                                "support_status": "SUPPORTS", "evidence_refs": ["E1"]}},
    "evidence_registry": {"E1": {"evidence_id": "E1"}},
}, "R12: support_registry dict key 'S1' != inner support_id 'S2' -> REGISTRY_MALFORMED")

add("F1-A-SREL-support-relations-key-ne-id", "ADVERSARIAL", "BLOCK", {
    "claim": {"claim_id": "C1", "claim_type": "SUPPORT", "status": "SUPPORTED",
              "support_relation_refs": ["S2"]},
    "support_relations": {"S1": {"support_id": "S2", "claim_ref": "C1",
                                 "support_status": "SUPPORTS", "evidence_refs": ["E1"]}},
    "evidence_registry": {"E1": {"evidence_id": "E1"}},
}, "R12: support_relations dict key 'S1' != inner support_id 'S2' -> REGISTRY_MALFORMED")

add("F1-A-E-evidence-key-ne-id", "ADVERSARIAL", "BLOCK", {
    "claim": {"claim_id": "C1", "claim_type": "SUPPORT", "status": "SUPPORTED",
              "support_relation_refs": ["S1"]},
    "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C1",
                                "support_status": "SUPPORTS", "evidence_refs": ["E2"]}},
    "evidence_registry": {"E1": {"evidence_id": "E2", "root_provenance": "X"}},
}, "R12: evidence dict key 'E1' != inner evidence_id 'E2' -> REGISTRY_MALFORMED (WB IND-02E family)")

add("F1-A-R-root-key-ne-id", "ADVERSARIAL", "BLOCK", {
    "support": {"support_id": "S1", "claim_ref": "C1", "support_status": "SUPPORTS",
                "evidence_refs": ["E1"],
                "independence_basis": {"claimed_independent_count": 1, "root_provenance": ["R2"]}},
    "evidence_registry": {"E1": {"evidence_id": "E1"}},
    "root_registry": {"R1": {"root_id": "R2"}},
}, "R12: root dict key 'R1' != inner root_id 'R2' -> REGISTRY_MALFORMED (WB IND-02R family)")

add("F1-A-O-obligation-key-ne-id", "ADVERSARIAL", "BLOCK", {
    "claim": {"claim_id": "C1", "claim_type": "TASK_COMPLETION", "status": "SUPPORTED",
              "support_relation_refs": ["S1"], "required_obligation_refs": ["O2"]},
    "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C1",
                                "support_status": "SUPPORTS", "evidence_refs": ["E1"]}},
    "evidence_registry": {"E1": {"evidence_id": "E1"}},
    "obligations": {"O1": {"obligation_id": "O2", "materiality": "MATERIAL",
                           "trigger": {"observed": True}, "status": "SATISFIED",
                           "closure_evidence_refs": ["E1"]}},
}, "R12: obligation dict key 'O1' != inner obligation_id 'O2' -> REGISTRY_MALFORMED (WB IND-02O family)")

add("F1-A-A-authority-key-ne-id", "ADVERSARIAL", "BLOCK", {
    "binding": {"authority_envelope": ["x"], "mandate": {"source": "G2", "expires_at": "2099-01-01"}},
    "authority_registry": {"G1": {"grant_id": "G2", "agent": None, "host": None, "expires_at": "2099-01-01"}},
    "evidence_registry": {"E1": {"evidence_id": "E1"}},
}, "R12: authority dict key 'G1' != inner grant_id 'G2' -> REGISTRY_MALFORMED (WB IND-02A family)")

# ================= legitimate: key==inner-id ================
add("F1-P-SUP-support-registry-key-eq-id", "POSITIVE", "OK", {
    "claim": {"claim_id": "C1", "claim_type": "SUPPORT", "status": "SUPPORTED",
              "support_relation_refs": ["S1"]},
    "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C1",
                                "support_status": "SUPPORTS", "evidence_refs": ["E1"]}},
    "evidence_registry": {"E1": {"evidence_id": "E1"}},
}, "R12: support dict key==inner support_id resolves OK")

add("F1-P-O-obligation-key-eq-id", "POSITIVE", "OK", {
    "claim": {"claim_id": "C1", "claim_type": "TASK_COMPLETION", "status": "SUPPORTED",
              "support_relation_refs": ["S1"], "required_obligation_refs": ["O1"]},
    "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C1",
                                "support_status": "SUPPORTS", "evidence_refs": ["E1"]}},
    "evidence_registry": {"E1": {"evidence_id": "E1"}},
    "obligations": {"O1": {"obligation_id": "O1", "materiality": "MATERIAL",
                           "trigger": {"observed": True}, "status": "SATISFIED",
                           "closure_evidence_refs": ["E1"]}},
}, "R12: obligation dict key==inner obligation_id resolves OK")

add("F1-P-R-root-key-eq-id", "POSITIVE", "OK", {
    "support": {"support_id": "S1", "claim_ref": "C1", "support_status": "SUPPORTS",
                "evidence_refs": ["E1"],
                "independence_basis": {"claimed_independent_count": 1, "root_provenance": ["R1"]}},
    "evidence_registry": {"E1": {"evidence_id": "E1"}},
    "root_registry": {"R1": {"root_id": "R1", "actual_origin": "O1"}},
}, "R12: root dict key==inner root_id resolves OK")

add("F1-P-A-authority-key-eq-id", "POSITIVE", "OK", {
    "binding": {"authority_envelope": ["x"], "agent": "agent-A", "host": "H1",
                "mandate": {"source": "G1", "expires_at": "2099-01-01"}},
    "authority_registry": {"G1": {"grant_id": "G1", "agent": "agent-A", "host": "H1", "expires_at": "2099-12-31"}},
    "evidence_registry": {"E1": {"evidence_id": "E1"}},
}, "R12: authority dict key==inner grant_id resolves OK")

# ================= backfill: missing inner id (dict key is the id) =========
add("F1-B-SUP-support-registry-backfill", "POSITIVE", "OK", {
    "claim": {"claim_id": "C1", "claim_type": "SUPPORT", "status": "SUPPORTED",
              "support_relation_refs": ["S1"]},
    "support_registry": {"S1": {"claim_ref": "C1", "support_status": "SUPPORTS", "evidence_refs": ["E1"]}},
    "evidence_registry": {"E1": {"evidence_id": "E1"}},
}, "R12: support dict entry without inner id -> backfilled from key -> OK (representation remains supported)")

add("F1-B-R-root-registry-backfill", "POSITIVE", "OK", {
    "support": {"support_id": "S1", "claim_ref": "C1", "support_status": "SUPPORTS",
                "evidence_refs": ["E1"],
                "independence_basis": {"claimed_independent_count": 1, "root_provenance": ["R1"]}},
    "evidence_registry": {"E1": {"evidence_id": "E1"}},
    "root_registry": {"R1": {"actual_origin": "O1"}},
}, "R12: root dict entry without inner id -> backfilled from key -> OK")

add("F1-B-O-obligation-registry-backfill", "POSITIVE", "OK", {
    "claim": {"claim_id": "C1", "claim_type": "TASK_COMPLETION", "status": "SUPPORTED",
              "support_relation_refs": ["S1"], "required_obligation_refs": ["O1"]},
    "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C1",
                                "support_status": "SUPPORTS", "evidence_refs": ["E1"]}},
    "evidence_registry": {"E1": {"evidence_id": "E1"}},
    "obligations": {"O1": {"materiality": "MATERIAL", "trigger": {"observed": True},
                           "status": "SATISFIED", "closure_evidence_refs": ["E1"]}},
}, "R12: obligation dict entry without inner id -> backfilled from key -> OK")

add("F1-B-A-authority-registry-backfill", "POSITIVE", "OK", {
    "binding": {"authority_envelope": ["x"], "agent": "agent-A", "host": "H1",
                "mandate": {"source": "G1", "expires_at": "2099-01-01"}},
    "authority_registry": {"G1": {"agent": "agent-A", "host": "H1", "expires_at": "2099-12-31"}},
    "evidence_registry": {"E1": {"evidence_id": "E1"}},
}, "R12: authority dict entry without inner id -> backfilled from key -> OK")

# ================= regression guards: no reopening of prior false-OK fixes ==
add("F1-R1-evidence-missing-still-blocks", "ADVERSARIAL", "BLOCK", {
    "claim": {"claim_id": "C1", "claim_type": "SUPPORT", "status": "SUPPORTED",
              "support_relation_refs": ["S1"]},
    "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C1",
                                "support_status": "SUPPORTS", "evidence_refs": ["E-NOPE"]}},
    "evidence_registry": {"E1": {"evidence_id": "E1"}},
}, "regression: I09 false-OK path stays closed (present-but-missing evidence still BLOCKs)")

add("F1-R2-claim-ref-mismatch-still-blocks", "ADVERSARIAL", "BLOCK", {
    "claim": {"claim_id": "C1", "claim_type": "SUPPORT", "status": "SUPPORTED",
              "support_relation_refs": ["S1"]},
    "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C-OTHER",
                                "support_status": "SUPPORTS", "evidence_refs": ["E1"]}},
    "evidence_registry": {"E1": {"evidence_id": "E1"}},
}, "regression: I01 support-target binding stays closed (dict-form support)")

add("F1-R3-duplicate-ambiguous-still-blocks", "ADVERSARIAL", "BLOCK", {
    "claim": {"claim_id": "C1", "claim_type": "SUPPORT", "status": "SUPPORTED",
              "support_relation_refs": ["S1"]},
    "support_registry": [
        {"support_id": "S1", "claim_ref": "C1", "support_status": "SUPPORTS", "evidence_refs": ["E1"]},
        {"support_id": "S1", "claim_ref": "C2", "support_status": "SUPPORTS", "evidence_refs": ["E1"]}],
    "evidence_registry": {"E1": {"evidence_id": "E1"}},
}, "regression: I08 duplicate-ambiguity stays closed (identity ambiguous)")

add("F1-R4-unrelated-obligation-still-ok", "POSITIVE", "OK", {
    "claim": {"claim_id": "C1", "claim_type": "TASK_COMPLETION", "status": "SUPPORTED",
              "support_relation_refs": ["S1"], "required_obligation_refs": ["O-GOOD"]},
    "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C1",
                                "support_status": "SUPPORTS", "evidence_refs": ["E1"]}},
    "evidence_registry": {"E1": {"evidence_id": "E1"}},
    "obligations": {"O-GOOD": {"obligation_id": "O-GOOD", "materiality": "MATERIAL",
                               "trigger": {"observed": True}, "status": "SATISFIED",
                               "closure_evidence_refs": ["E1"]},
                    "O-OTHER": {"obligation_id": "O-OTHER", "materiality": "MATERIAL",
                                "trigger": {"observed": True}, "status": "PENDING",
                                "required_before_claim_refs": ["C-OTHER"]}},
}, "regression: I07 claim-aware obligation scoping stays open (F2 vocabulary gate must not poison narrow completion)")

add("F1-R5-own-open-obligation-still-blocks", "ADVERSARIAL", "BLOCK", {
    "claim": {"claim_id": "C1", "claim_type": "TASK_COMPLETION", "status": "SUPPORTED",
              "support_relation_refs": ["S1"], "required_obligation_refs": ["O-OWN"]},
    "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C1",
                                "support_status": "SUPPORTS", "evidence_refs": ["E1"]}},
    "evidence_registry": {"E1": {"evidence_id": "E1"}},
    "obligations": {"O-OWN": {"obligation_id": "O-OWN", "materiality": "MATERIAL",
                              "trigger": {"observed": True}, "status": "PENDING"}},
}, "regression: S3 own-open-material-obligation stays closed")

add("F1-R6-top-level-support-still-ok", "POSITIVE", "OK", {
    "claim": {"claim_id": "C1", "claim_type": "SUPPORT", "status": "SUPPORTED",
              "support_relation_refs": ["S1"]},
    "support": {"support_id": "S1", "claim_ref": "C1", "support_status": "SUPPORTS",
                "evidence_refs": ["E1"]},
    "evidence_registry": {"E1": {"evidence_id": "E1"}},
}, "regression: I06 top-level support composition stays open")

add("F1-R7-full-stack-dict-registries", "POSITIVE", "OK", {
    "claim": {"claim_id": "C1", "claim_type": "TASK_COMPLETION", "status": "SUPPORTED",
              "support_relation_refs": ["S1"], "required_obligation_refs": ["O1"]},
    "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C1",
                                "support_status": "SUPPORTS", "evidence_refs": ["E1"]}},
    "evidence_registry": {"E1": {"evidence_id": "E1"}},
    "obligations": {"O1": {"obligation_id": "O1", "materiality": "MATERIAL",
                           "trigger": {"observed": True}, "status": "SATISFIED",
                           "closure_evidence_refs": ["E1"]}},
}, "regression: dict-form registries with key==id compose across all kinds (happy path)")

add("F1-R8-self-asserted-mandate-still-blocks", "ADVERSARIAL", "BLOCK", {
    "binding": {"authority_envelope": ["x"], "mandate": {"source": "SELF_ASSERTED", "expires_at": "2099-01-01"}},
    "authority_registry": {"G1": {"grant_id": "G1", "agent": None, "host": None, "expires_at": "2099-12-31"}},
    "evidence_registry": {"E1": {"evidence_id": "E1"}},
}, "regression: I11 mandate positive typing stays closed (dict-form authority registry present)")

# ================= F2: obligation status vocabulary (not expanded) =========
add("F2-A1-open-in-scope", "ADVERSARIAL", "BLOCK", {
    "claim": {"claim_id": "C1", "claim_type": "TASK_COMPLETION", "status": "SUPPORTED",
              "support_relation_refs": ["S1"], "required_obligation_refs": ["O1"]},
    "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C1",
                                "support_status": "SUPPORTS", "evidence_refs": ["E1"]}},
    "evidence_registry": {"E1": {"evidence_id": "E1"}},
    "obligations": {"O1": {"obligation_id": "O1", "materiality": "MATERIAL",
                           "trigger": {"observed": True}, "status": "OPEN"}},
}, "F2: OPEN obligation (outside shipped schema status enum) -> BLOCK OBLIGATION_STATUS_OUTSIDE_VOCABULARY")

add("F2-A2-garbage-status", "ADVERSARIAL", "BLOCK", {
    "claim": {"claim_id": "C1", "claim_type": "TASK_COMPLETION", "status": "SUPPORTED",
              "support_relation_refs": ["S1"], "required_obligation_refs": ["O1"]},
    "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C1",
                                "support_status": "SUPPORTS", "evidence_refs": ["E1"]}},
    "evidence_registry": {"E1": {"evidence_id": "E1"}},
    "obligations": {"O1": {"obligation_id": "O1", "materiality": "MATERIAL",
                           "trigger": {"observed": True}, "status": "GARBAGE"}},
}, "F2: out-of-vocabulary status -> BLOCK (vocabulary not expanded)")

add("F2-P1-satisfied-in-vocab", "POSITIVE", "OK", {
    "claim": {"claim_id": "C1", "claim_type": "TASK_COMPLETION", "status": "SUPPORTED",
              "support_relation_refs": ["S1"], "required_obligation_refs": ["O1"]},
    "support_registry": {"S1": {"support_id": "S1", "claim_ref": "C1",
                                "support_status": "SUPPORTS", "evidence_refs": ["E1"]}},
    "evidence_registry": {"E1": {"evidence_id": "E1"}},
    "obligations": {"O1": {"obligation_id": "O1", "materiality": "MATERIAL",
                           "trigger": {"observed": True}, "status": "SATISFIED",
                           "closure_evidence_refs": ["E1"]}},
}, "F2: in-vocabulary SATISFIED obligation with resolved closure evidence stays OK")


def get_f1_controls():
    return copy.deepcopy(CONTROLS)
