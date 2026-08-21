#!/usr/bin/env python3
"""V2.2 composition fixtures: cases that test COMPOSITION of protections,
not isolated rules. Plus aggregation of ALL historical fixtures.

Composition-failure hunting:
- a fixture that is individually valid under one protection but becomes
  invalid/contradictory/UNKNOWN when protections are composed;
- legitimate full-stack composition (claim->support->evidence->root all resolve);
- eval-time boundary behavior (no hardcoded date).
"""
import copy

V22_FIXTURES = []

# ---- Composition: legitimate full-stack, all refs resolve correctly ----
V22_FIXTURES += [{
  "id": "V22-P1-full-stack-composition", "kind": "POSITIVE",
  "vector": "COMPOSITION", "case": "claim->support->evidence->root all resolve, applicable, valid",
  "payload": {
    "claim": {"claim_id": "C-V22P1", "claim_type": "CAPABILITY_QUALIFICATION",
              "subject": {"kind": "AGENT", "id": "me"}, "scope": {"host": "H1"},
              "assertion": "verified", "status": "SUPPORTED",
              "support_relation_refs": ["S-V22P1"]},
    "support_registry": [
      {"support_id": "S-V22P1", "claim_ref": "C-V22P1", "evidence_refs": ["E-V22P1"],
       "support_status": "SUPPORTS", "observed_scope": {"host": "H1"}, "claimed_scope": {"host": "H1"}}],
    "evidence_registry": {
      "E-V22P1": {"root_provenance": "R-A", "derived_from": None}},
  },
  "expect_pass": True,
}]

# ---- Composition: refs resolve but to WRONG artifact type ----
V22_FIXTURES += [{
  "id": "V22-A1-support-ref-points-at-obligation", "kind": "ATTACK",
  "vector": "COMPOSITION", "case": "support ref string collides with an obligation id; typed resolution must reject",
  "payload": {
    "claim": {"claim_id": "C-V22A1", "claim_type": "OTHER",
              "subject": {"kind": "TASK", "id": "T1"}, "scope": {"host": "H1"},
              "assertion": "verified", "status": "SUPPORTED",
              "support_relation_refs": ["SHARED-ID"]},
    "support_registry": [],
    "obligations": [{"obligation_id": "SHARED-ID", "materiality": "NON_MATERIAL",
                     "trigger": {"rule_ref": "R", "observed": False}, "status": "PENDING"}],
  },
  "expect_block": ["SUPPORT_REF_UNRESOLVABLE"],
}]

# ---- Composition: duplicate obligation ids ----
V22_FIXTURES += [{
  "id": "V22-A2-duplicate-obligation-id", "kind": "ATTACK",
  "vector": "COMPOSITION", "case": "two obligations share an id with contradictory states",
  "payload": {
    "claim": {"claim_id": "C-V22A2", "claim_type": "WORKFLOW_COMPLETION",
              "subject": {"kind": "TASK", "id": "T2"}, "scope": {"host": "H1"},
              "assertion": "done", "status": "SUPPORTED", "support_relation_refs": ["S-V22A2"],
              "required_obligation_refs": ["O-DUP"]},
    "support_registry": [
      {"support_id": "S-V22A2", "claim_ref": "C-V22A2", "evidence_refs": ["E-a"],
       "support_status": "SUPPORTS", "observed_scope": {"host": "H1"}, "claimed_scope": {"host": "H1"}}],
    "obligations": [
      {"obligation_id": "O-DUP", "materiality": "MATERIAL", "trigger": {"rule_ref": "R", "observed": True}, "status": "SATISFIED", "closure_evidence_refs": ["E-c"]},
      {"obligation_id": "O-DUP", "materiality": "MATERIAL", "trigger": {"rule_ref": "R", "observed": True}, "status": "PENDING"}],
  },
  "expect_block": ["DUPLICATE_OBLIGATION_ID"],
}]

# ---- Composition: eval-time boundary (no hardcoded date) ----
V22_FIXTURES += [{
  "id": "V22-A3-mandate-expires-tomorrow-eval-today", "kind": "ATTACK",
  "vector": "COMPOSITION", "case": "mandate expires 2026-08-21; eval 2026-08-20 -> valid; eval 2026-08-22 -> expired (eval-time driven)",
  "payload": {
    "binding": {"binding_id": "B-V22A3", "agent": "me", "host": "H1", "route": ["r"],
                "authority_envelope": ["approve stable admission"],
                "mandate": {"source": "USER_EXPLICIT_GRANT", "expires_at": "2026-08-21"}},
    "eval_time": "2026-08-22"},
  "expect_block": ["MANDATE_EXPIRED"],
}]

V22_FIXTURES += [{
  "id": "V22-P3-mandate-expires-tomorrow-eval-today-valid", "kind": "POSITIVE",
  "vector": "COMPOSITION", "case": "same mandate evaluated 2026-08-20 -> still valid (eval-time driven, not hardcoded)",
  "payload": {
    "binding": {"binding_id": "B-V22P3", "agent": "me", "host": "H1", "route": ["r"],
                "authority_envelope": ["approve stable admission"],
                "mandate": {"source": "USER_EXPLICIT_GRANT", "expires_at": "2026-08-21"}},
    "eval_time": "2026-08-20"},
  "expect_pass": True,
}]

# ---- Composition: recovery history evidence distinct STRINGS but same root via registry ----
V22_FIXTURES += [{
  "id": "V22-A4-recovery-same-root-via-registry", "kind": "ATTACK",
  "vector": "COMPOSITION", "case": "distinct ref strings, registry reveals same root -> blocked (composed V2.1 root check)",
  "payload": {
    "transition": {"transition_id": "RT-V22A4",
                   "state_restore": {"target_checkpoint": "CP", "result": "SUCCESS", "evidence_refs": ["E-ST"]},
                   "history_continuity": {"status": "PRESERVED", "post_checkpoint_occurrence_delta_captured": True,
                                          "evidence_refs": ["E-HI"]},
                   "recovery_claim": {"claim_ref": "C-REC-V22A4", "scope": "STATE_AND_HISTORY"}},
    "evidence_registry": {
      "E-ST": {"root_provenance": "ROOT-X", "derived_from": None},
      "E-HI": {"root_provenance": "ROOT-X", "derived_from": "E-ST"}}},
  "expect_block": ["HISTORY_EVIDENCE_SHARED_ROOT"],
}]

# ---- Composition: independence roots that are all mirrors of one origin ----
V22_FIXTURES += [{
  "id": "V22-A5-independence-mirror-roots", "kind": "ATTACK",
  "vector": "COMPOSITION", "case": "3 mirror roots, root registry reveals 1 origin -> overclaim blocked",
  "payload": {
    "support": {"support_id": "S-V22A5", "claim_ref": "C-V22A5", "evidence_refs": ["E1", "E2", "E3"],
                "support_status": "SUPPORTS", "observed_scope": {"host": "H1"}, "claimed_scope": {"host": "H1"},
                "independence_basis": {"claimed_independent_count": 3,
                                       "source_origins": ["A", "B", "C"],
                                       "root_provenance": ["M1", "M2", "M3"]}},
    "root_registry": {"M1": {"actual_origin": "ORIGIN"}, "M2": {"actual_origin": "ORIGIN"}, "M3": {"actual_origin": "ORIGIN"}}},
  "expect_block": ["INDEPENDENCE_OVERCLAIMED"],
}]

def get_v22_fixtures():
    return copy.deepcopy(V22_FIXTURES)
