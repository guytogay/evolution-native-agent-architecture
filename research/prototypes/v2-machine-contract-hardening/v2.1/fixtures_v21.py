#!/usr/bin/env python3
"""V2.1 second-order adversarial fixtures against the V2 hardening prototype.

Each fixture attacks a STRUCTURAL case the V2 rules do not cover, with a
legitimate positive control. Fields:
  id, kind (ATTACK/POSITIVE), vector, case (which structural gap),
  payload (objects incl. optional registry), expect_block (codes), expect_pass.
"""
import copy

# Registry helpers: some attacks need a registry of resolvable artifacts.
# V2 prototype does NOT accept a registry — these attacks exploit that absence.

FIXTURES = []

# ================================================================ ATTACKS ====
# 1. SUPPORTED claim -> nonexistent/unresolvable support_relation_ref
FIXTURES += [{
  "id": "A21-1-support-ref-unresolvable", "kind": "ATTACK", "vector": "I_KNOW",
  "case": "SUPPORTED claim points to nonexistent support_relation_ref; no registry supplied",
  "payload": {
    "claim": {"claim_id": "C-A21-1", "claim_type": "CAPABILITY_QUALIFICATION",
              "subject": {"kind": "AGENT", "id": "me"}, "scope": {"host": "H1"},
              "assertion": "verified", "status": "SUPPORTED",
              "support_relation_refs": ["S-DOES-NOT-EXIST"]}},
  "expect_block": ["SUPPORT_REF_UNRESOLVABLE"],
  "v2_vulnerable": "C1 only checks non-empty refs; unresolvable ref passes",
}]

# 2. Completion claim -> nonexistent/unresolvable required_obligation_refs
FIXTURES += [{
  "id": "A21-2-obligation-ref-unresolvable", "kind": "ATTACK", "vector": "I_COMPLETED",
  "case": "Completion claim references obligation that does not exist in registry",
  "payload": {
    "claim": {"claim_id": "C-A21-2", "claim_type": "WORKFLOW_COMPLETION",
              "subject": {"kind": "TASK", "id": "T2"}, "scope": {"host": "H1"},
              "assertion": "done", "status": "SUPPORTED", "support_relation_refs": ["S-A21-2"],
              "required_obligation_refs": ["O-DOES-NOT-EXIST"]},
    "obligations": []},
  "expect_block": ["OBLIGATION_REF_UNRESOLVABLE"],
  "v2_vulnerable": "C4 iterates only supplied obligations; ref to absent obligation never checked",
}]

# 3. VERIFIED_* with invalid/unknown/out-of-range evidence grade
FIXTURES += [{
  "id": "A21-3-grade-garbage", "kind": "ATTACK", "vector": "I_VERIFIED",
  "case": "grade='GARBAGE' bypasses C2 (all(g in E0,E1) is False -> passes)",
  "payload": {
    "binding": {"binding_id": "B-A21-3", "agent": "me", "host": "H1", "route": ["r"],
                "capabilities": [{"id": "ENA-CAP-048", "status": "VERIFIED_AVAILABLE",
                                  "evidence_refs": [{"ref": "E-x", "grade": "GARBAGE"}]}]}},
  "expect_block": ["EVIDENCE_GRADE_INVALID"],
  "v2_vulnerable": "C2 accepts any grade outside {E0,E1}; malformed/unknown grade passes",
}]

FIXTURES += [{
  "id": "A21-3b-grade-out-of-range", "kind": "ATTACK", "vector": "I_VERIFIED",
  "case": "grade='E9' (out of range) also passes C2",
  "payload": {
    "binding": {"binding_id": "B-A21-3b", "agent": "me", "host": "H1", "route": ["r"],
                "capabilities": [{"id": "ENA-CAP-048", "status": "VERIFIED_AVAILABLE",
                                  "evidence_refs": [{"ref": "E-y", "grade": "E9"}]}]}},
  "expect_block": ["EVIDENCE_GRADE_INVALID"],
  "v2_vulnerable": "same as A21-3",
}]

# 4. Authority mandate with malformed/expired/non-current expires_at
FIXTURES += [{
  "id": "A21-4-mandate-expired", "kind": "ATTACK", "vector": "I_HAVE_AUTHORITY",
  "case": "expires_at in the past; C3 only checks non-empty",
  "payload": {
    "binding": {"binding_id": "B-A21-4", "agent": "me", "host": "H1", "route": ["r"],
                "authority_envelope": ["approve stable admission"],
                "mandate": {"source": "USER_EXPLICIT_GRANT", "expires_at": "2020-01-01"}}},
  "expect_block": ["MANDATE_EXPIRED"],
  "v2_vulnerable": "C3 checks expires_at present, not whether it is current",
}]

FIXTURES += [{
  "id": "A21-4b-mandate-malformed", "kind": "ATTACK", "vector": "I_HAVE_AUTHORITY",
  "case": "expires_at='not-a-date' unparseable; C3 passes (non-empty)",
  "payload": {
    "binding": {"binding_id": "B-A21-4b", "agent": "me", "host": "H1", "route": ["r"],
                "authority_envelope": ["revoke leases"],
                "mandate": {"source": "USER_EXPLICIT_GRANT", "expires_at": "not-a-date"}}},
  "expect_block": ["MANDATE_DATE_UNPARSEABLE"],
  "v2_vulnerable": "C3 never parses the date",
}]

# 5. Recovery: distinct state/history ref strings deriving from same root
FIXTURES += [{
  "id": "A21-5-recovery-same-root", "kind": "ATTACK", "vector": "I_RECOVERED",
  "case": "history evidence ref E-HIST is a derived copy of E-STATE (same root); C5 only string-compares",
  "payload": {
    "transition": {"transition_id": "RT-A21-5",
                   "state_restore": {"target_checkpoint": "CP", "result": "SUCCESS",
                                     "evidence_refs": ["E-STATE"]},
                   "history_continuity": {"status": "PRESERVED",
                                          "post_checkpoint_occurrence_delta_captured": True,
                                          "evidence_refs": ["E-HIST"]},
                   "recovery_claim": {"claim_ref": "C-REC-A21-5", "scope": "STATE_AND_HISTORY"}},
    "evidence_registry": {
      "E-STATE": {"root_provenance": "ROOT-LOG", "derived_from": None},
      "E-HIST": {"root_provenance": "ROOT-LOG", "derived_from": "E-STATE"}}},
  "expect_block": ["HISTORY_EVIDENCE_SHARED_ROOT"],
  "v2_vulnerable": "C5 compares ref strings only; two distinct strings from one root pass",
}]

# 6. Independence: multiple fabricated root_provenance values
FIXTURES += [{
  "id": "A21-6-fabricated-roots", "kind": "ATTACK", "vector": "EVIDENCE_INDEPENDENT",
  "case": "3 distinct root_provenance strings that are all mirrors of one actual origin; C6 counts strings",
  "payload": {
    "support": {"support_id": "S-A21-6", "claim_ref": "C-A21-6", "evidence_refs": ["E1", "E2", "E3"],
                "support_status": "SUPPORTS", "observed_scope": {"host": "H1"},
                "claimed_scope": {"host": "H1"},
                "independence_basis": {"claimed_independent_count": 3,
                                       "source_origins": ["A", "B", "C"],
                                       "root_provenance": ["MIRROR-1", "MIRROR-2", "MIRROR-3"]}},
    "root_registry": {"MIRROR-1": {"actual_origin": "ACTUAL-ORIGIN"},
                      "MIRROR-2": {"actual_origin": "ACTUAL-ORIGIN"},
                      "MIRROR-3": {"actual_origin": "ACTUAL-ORIGIN"}}},
  "expect_block": ["INDEPENDENCE_OVERCLAIMED"],
  "v2_vulnerable": "C6 counts distinct root strings; laundering moved one level deeper (mirrors)",
}]

# 7. Missing/incomplete registries and unresolved cross-artifact references
FIXTURES += [{
  "id": "A21-7-support-ref-registry-absent", "kind": "ATTACK", "vector": "I_KNOW",
  "case": "no registry supplied at all; validator cannot resolve any ref; V2 silently passes",
  "payload": {
    "claim": {"claim_id": "C-A21-7", "claim_type": "OTHER",
              "subject": {"kind": "TASK", "id": "T7"}, "scope": {"host": "H1"},
              "assertion": "done", "status": "SUPPORTED",
              "support_relation_refs": ["S-ANY"]}},
  "expect_block": ["SUPPORT_REF_UNRESOLVABLE"],
  "v2_vulnerable": "resolution requires a registry; without one, refs are never checked",
}]

# 8. Duplicate / ambiguous / conflicting IDs resolving to same reference
FIXTURES += [{
  "id": "A21-8-duplicate-support-id", "kind": "ATTACK", "vector": "I_KNOW",
  "case": "two different support relations share support_id S-DUP with contradictory support_status",
  "payload": {
    "claim": {"claim_id": "C-A21-8", "claim_type": "OTHER",
              "subject": {"kind": "TASK", "id": "T8"}, "scope": {"host": "H1"},
              "assertion": "verified", "status": "SUPPORTED",
              "support_relation_refs": ["S-DUP"]},
    "support_registry": [
      {"support_id": "S-DUP", "claim_ref": "C-A21-8", "evidence_refs": ["E-a"],
       "support_status": "SUPPORTS"},
      {"support_id": "S-DUP", "claim_ref": "C-A21-8", "evidence_refs": ["E-b"],
       "support_status": "CONTRADICTS"}]},
  "expect_block": ["DUPLICATE_REF_ID"],
  "v2_vulnerable": "V2 has no registry/ID-uniqueness; ambiguity invisible",
}]

# 9. Reference resolves but resolved artifact has incompatible applicability
FIXTURES += [{
  "id": "A21-9-applicability-mismatch", "kind": "ATTACK", "vector": "EVIDENCE_INDEPENDENT",
  "case": "support resolves; observed_scope host=H1 but claim scope host=H2; no transfer basis; base validator would catch host mismatch, but hardened path must too",
  "payload": {
    "claim": {"claim_id": "C-A21-9", "claim_type": "OTHER",
              "subject": {"kind": "HOST", "id": "H2"}, "scope": {"host": "H2"},
              "assertion": "H2 verified", "status": "SUPPORTED",
              "support_relation_refs": ["S-A21-9"]},
    "support_registry": [
      {"support_id": "S-A21-9", "claim_ref": "C-A21-9", "evidence_refs": ["E-9"],
       "support_status": "SUPPORTS", "observed_scope": {"host": "H1"},
       "claimed_scope": {"host": "H2"}}]},
  "expect_block": ["TRANSFER_EVIDENCE_REQUIRED"],
  "v2_vulnerable": "base validate_support catches this when support is passed; registry resolution must preserve it",
}]

# ================================================================ POSITIVE ===
FIXTURES += [
  {"id": "P21-1-supported-resolvable", "kind": "POSITIVE", "vector": "I_KNOW",
   "payload": {
     "claim": {"claim_id": "C-P21-1", "claim_type": "CAPABILITY_QUALIFICATION",
               "subject": {"kind": "AGENT", "id": "me"}, "scope": {"host": "H1"},
               "assertion": "verified", "status": "SUPPORTED",
               "support_relation_refs": ["S-P21-1"]},
     "support_registry": [
       {"support_id": "S-P21-1", "claim_ref": "C-P21-1", "evidence_refs": ["E-p1"],
        "support_status": "SUPPORTS", "observed_scope": {"host": "H1"}, "claimed_scope": {"host": "H1"}}]},
   "expect_pass": True},

  {"id": "P21-2-completion-resolvable", "kind": "POSITIVE", "vector": "I_COMPLETED",
   "payload": {
     "claim": {"claim_id": "C-P21-2", "claim_type": "WORKFLOW_COMPLETION",
               "subject": {"kind": "TASK", "id": "T2"}, "scope": {"host": "H1"},
               "assertion": "done", "status": "SUPPORTED", "support_relation_refs": ["S-P21-2"],
               "required_obligation_refs": ["O-P21-2"]},
     "obligations": [{"obligation_id": "O-P21-2", "materiality": "MATERIAL",
                      "trigger": {"rule_ref": "R", "observed": True},
                      "status": "SATISFIED", "closure_evidence_refs": ["E-close"]}],
     "support_registry": [
       {"support_id": "S-P21-2", "claim_ref": "C-P21-2", "evidence_refs": ["E-p2"],
        "support_status": "SUPPORTS", "observed_scope": {"host": "H1"}, "claimed_scope": {"host": "H1"}}]},
   "expect_pass": True},

  {"id": "P21-3-grade-e2", "kind": "POSITIVE", "vector": "I_VERIFIED",
   "payload": {
     "binding": {"binding_id": "B-P21-3", "agent": "me", "host": "H1", "route": ["r"],
                 "capabilities": [{"id": "ENA-CAP-048", "status": "VERIFIED_AVAILABLE",
                                   "evidence_refs": [{"ref": "E-t", "grade": "E2"}]}]}},
   "expect_pass": True},

  {"id": "P21-4-mandate-current", "kind": "POSITIVE", "vector": "I_HAVE_AUTHORITY",
   "payload": {
     "binding": {"binding_id": "B-P21-4", "agent": "me", "host": "H1", "route": ["r"],
                 "authority_envelope": ["approve stable admission"],
                 "mandate": {"source": "USER_EXPLICIT_GRANT", "expires_at": "2999-01-01"}}},
   "expect_pass": True},

  {"id": "P21-5-recovery-distinct-roots", "kind": "POSITIVE", "vector": "I_RECOVERED",
   "payload": {
     "transition": {"transition_id": "RT-P21-5",
                    "state_restore": {"target_checkpoint": "CP", "result": "SUCCESS",
                                      "evidence_refs": ["E-STATE-P"]},
                    "history_continuity": {"status": "PRESERVED",
                                           "post_checkpoint_occurrence_delta_captured": True,
                                           "evidence_refs": ["E-HIST-P"]},
                    "recovery_claim": {"claim_ref": "C-REC-P21-5", "scope": "STATE_AND_HISTORY"}},
     "evidence_registry": {
       "E-STATE-P": {"root_provenance": "ROOT-S", "derived_from": None},
       "E-HIST-P": {"root_provenance": "ROOT-H", "derived_from": None}}},
   "expect_pass": True},

  {"id": "P21-6-independence-real-roots", "kind": "POSITIVE", "vector": "EVIDENCE_INDEPENDENT",
   "payload": {
     "support": {"support_id": "S-P21-6", "claim_ref": "C-P21-6", "evidence_refs": ["E1", "E2"],
                 "support_status": "SUPPORTS", "observed_scope": {"host": "H1"},
                 "claimed_scope": {"host": "H1"},
                 "independence_basis": {"claimed_independent_count": 2,
                                        "source_origins": ["A", "B"],
                                        "root_provenance": ["R-A", "R-B"]}},
     "root_registry": {"R-A": {"actual_origin": "R-A"}, "R-B": {"actual_origin": "R-B"}}},
   "expect_pass": True},

  {"id": "P21-7-completion-nonmaterial", "kind": "POSITIVE", "vector": "I_COMPLETED",
   "payload": {
     "claim": {"claim_id": "C-P21-7", "claim_type": "WORKFLOW_COMPLETION",
               "subject": {"kind": "TASK", "id": "T7"}, "scope": {"host": "H1"},
               "assertion": "done", "status": "SUPPORTED", "support_relation_refs": ["S-P21-7"],
               "required_obligation_refs": ["O-P21-7"]},
     "obligations": [{"obligation_id": "O-P21-7", "materiality": "NON_MATERIAL",
                      "trigger": {"rule_ref": "R", "observed": True}, "status": "PENDING"}],
     "support_registry": [
       {"support_id": "S-P21-7", "claim_ref": "C-P21-7", "evidence_refs": ["E-p7"],
        "support_status": "SUPPORTS", "observed_scope": {"host": "H1"}, "claimed_scope": {"host": "H1"}}]},
   "expect_pass": True},
]

def get_fixtures():
    return copy.deepcopy(FIXTURES)
