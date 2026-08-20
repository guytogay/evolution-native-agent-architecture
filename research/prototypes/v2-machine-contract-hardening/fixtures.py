#!/usr/bin/env python3
"""Fixture builder for the V2 hardening experiment.
Each fixture carries: id, kind (ADVERSARIAL/POSITIVE/SECOND_ORDER), vector,
payload objects (claim/support/binding/obligations/transition), expected outcome.
Adversarial = the six falsified vectors + second-order bypass attempts.
Positive = legitimate cases that must remain accepted.
"""

FIXTURES = []

# ---------------------------------------------------------------- POSITIVE ---
FIXTURES += [
    # P1: legit SUPPORTED claim with a real support relation ref
    {"id": "P1-supported-with-refs", "kind": "POSITIVE", "vector": "I_KNOW",
     "payload": {
         "claim": {"claim_id": "C-P1", "claim_type": "CAPABILITY_QUALIFICATION",
                   "subject": {"kind": "AGENT", "id": "me"}, "scope": {"host": "H1"},
                   "assertion": "capability X verified", "status": "SUPPORTED",
                   "support_relation_refs": ["S-P1"]}},
     "expect_all_pass": True},

    # P2: legit ASSERTED claim (no support required)
    {"id": "P2-asserted-ok", "kind": "POSITIVE", "vector": "I_KNOW",
     "payload": {
         "claim": {"claim_id": "C-P2", "claim_type": "OTHER",
                   "subject": {"kind": "TASK", "id": "T2"}, "scope": {"host": "H1"},
                   "assertion": "hypothesis", "status": "ASSERTED"}},
     "expect_all_pass": True},

    # P3: legit authority with real mandate source + horizon
    {"id": "P3-authority-with-mandate", "kind": "POSITIVE", "vector": "I_HAVE_AUTHORITY",
     "payload": {
         "binding": {"binding_id": "B-P3", "agent": "me", "host": "H1", "route": ["r"],
                     "capability_claims": ["ENA-CAP-020"],
                     "authority_envelope": ["approve stable admission"],
                     "mandate": {"source": "USER_EXPLICIT_GRANT", "expires_at": "2026-12-31"}}},
     "expect_all_pass": True},

    # P4: legit authority envelope empty
    {"id": "P4-no-authority-ok", "kind": "POSITIVE", "vector": "I_HAVE_AUTHORITY",
     "payload": {"binding": {"binding_id": "B-P4", "agent": "me", "host": "H1", "route": ["r"],
                             "capability_claims": ["ENA-CAP-001"], "authority_envelope": []}},
     "expect_all_pass": True},

    # P5: legit workflow completion with satisfied obligations + closure evidence
    {"id": "P5-completion-satisfied", "kind": "POSITIVE", "vector": "I_COMPLETED",
     "payload": {
         "claim": {"claim_id": "C-P5", "claim_type": "WORKFLOW_COMPLETION",
                   "subject": {"kind": "TASK", "id": "T5"}, "scope": {"host": "H1"},
                   "assertion": "done", "status": "SUPPORTED",
                   "support_relation_refs": ["S-P5"],
                   "required_obligation_refs": ["O-P5"]},
         "obligations": [{"obligation_id": "O-P5", "materiality": "MATERIAL",
                          "trigger": {"rule_ref": "R", "observed": True},
                          "status": "SATISFIED", "closure_evidence_refs": ["E-CLOSE-P5"]}]},
     "expect_all_pass": True},

    # P6: legit non-material obligation does not block completion
    {"id": "P6-nonmaterial-obligation-ok", "kind": "POSITIVE", "vector": "I_COMPLETED",
     "payload": {
         "claim": {"claim_id": "C-P6", "claim_type": "WORKFLOW_COMPLETION",
                   "subject": {"kind": "TASK", "id": "T6"}, "scope": {"host": "H1"},
                   "assertion": "done", "status": "SUPPORTED", "support_relation_refs": ["S-P6"],
                   "required_obligation_refs": ["O-P6"]},
         "obligations": [{"obligation_id": "O-P6", "materiality": "NON_MATERIAL",
                          "trigger": {"rule_ref": "R", "observed": True}, "status": "PENDING"}]},
     "expect_all_pass": True},

    # P7: legit STATE_AND_HISTORY recovery with real, distinct history evidence
    {"id": "P7-recovery-with-history-evidence", "kind": "POSITIVE", "vector": "I_RECOVERED",
     "payload": {
         "transition": {"transition_id": "RT-P7",
                        "state_restore": {"target_checkpoint": "CP", "result": "SUCCESS",
                                          "evidence_refs": ["E-STATE-P7"]},
                        "history_continuity": {"status": "PRESERVED",
                                               "post_checkpoint_occurrence_delta_captured": True,
                                               "evidence_refs": ["E-HIST-P7"]},
                        "recovery_claim": {"claim_ref": "C-REC-P7", "scope": "STATE_AND_HISTORY"}}},
     "expect_all_pass": True},

    # P8: legit STATE_ONLY recovery (no history claim)
    {"id": "P8-recovery-state-only", "kind": "POSITIVE", "vector": "I_RECOVERED",
     "payload": {
         "transition": {"transition_id": "RT-P8",
                        "state_restore": {"target_checkpoint": "CP", "result": "SUCCESS"},
                        "history_continuity": {"status": "GAP_VISIBLE", "known_gap": "post-cp unknown"},
                        "recovery_claim": {"claim_ref": "C-REC-P8", "scope": "STATE_ONLY"}}},
     "expect_all_pass": True},

    # P9: legit independence with distinct root provenance
    {"id": "P9-independence-distinct-roots", "kind": "POSITIVE", "vector": "EVIDENCE_INDEPENDENT",
     "payload": {
         "support": {"support_id": "S-P9", "claim_ref": "C-P9", "evidence_refs": ["E-A", "E-B"],
                     "support_status": "SUPPORTS", "observed_scope": {"host": "H1"},
                     "claimed_scope": {"host": "H1"},
                     "independence_basis": {"claimed_independent_count": 2,
                                            "source_origins": ["A", "B"],
                                            "root_provenance": ["ROOT-A", "ROOT-B"]}}},
     "expect_all_pass": True},

    # P10: legit verified capability with grade E2 controlled test
    {"id": "P10-verified-with-e2", "kind": "POSITIVE", "vector": "I_VERIFIED",
     "payload": {
         "binding": {"binding_id": "B-P10", "agent": "me", "host": "H1", "route": ["r"],
                     "capabilities": [{"id": "ENA-CAP-048", "status": "VERIFIED_AVAILABLE",
                                       "evidence_refs": [{"ref": "E-TEST", "grade": "E2"}]}]}},
     "expect_all_pass": True},
]

# ------------------------------------------------------------ ADVERSARIAL ----
FIXTURES += [
    # A1 (original): SUPPORTED with zero refs
    {"id": "A1-supported-zero-refs", "kind": "ADVERSARIAL", "vector": "I_KNOW",
     "payload": {
         "claim": {"claim_id": "C-A1", "claim_type": "CAPABILITY_QUALIFICATION",
                   "subject": {"kind": "AGENT", "id": "me"}, "scope": {"host": "H1", "epoch": "E1"},
                   "assertion": "I know capability X is VERIFIED_AVAILABLE.", "status": "SUPPORTED",
                   "support_relation_refs": []}},
     "expect_block": ["CLAIM_SUPPORTED_WITHOUT_SUPPORT_REFS"]},

    # A2 (original): verified on schema-PASS-log (no grade)
    {"id": "A2-verified-schema-pass-log", "kind": "ADVERSARIAL", "vector": "I_VERIFIED",
     "payload": {
         "binding": {"binding_id": "B-A2", "agent": "me", "host": "H1", "route": ["r"],
                     "capabilities": [{"id": "ENA-CAP-048", "status": "VERIFIED_AVAILABLE",
                                       "evidence_refs": [{"ref": "schema-validation-PASS-log", "grade": "E1"}]}]}},
     "expect_block": ["VERIFIED_ONLY_STATIC_STRUCTURE_EVIDENCE"]},

    # A3 (original): authority after restore, no mandate
    {"id": "A3-authority-restore-no-mandate", "kind": "ADVERSARIAL", "vector": "I_HAVE_AUTHORITY",
     "payload": {
         "binding": {"binding_id": "B-A3", "agent": "me", "host": "H1",
                     "runtime_instance": "clone-of-H1-after-restore", "route": ["r"],
                     "capability_claims": ["ENA-CAP-020", "ENA-CAP-037"],
                     "evidence_refs": ["restore-completed-log", "credential-valid"],
                     "authority_envelope": ["approve stable admission", "revoke leases"]}},
     "expect_block": ["AUTHORITY_WITHOUT_MANDATE_SOURCE"]},

    # A4 (original): completion claim, obligation not linked / open
    {"id": "A4-completion-no-obligation-refs", "kind": "ADVERSARIAL", "vector": "I_COMPLETED",
     "payload": {
         "claim": {"claim_id": "C-A4", "claim_type": "WORKFLOW_COMPLETION",
                   "subject": {"kind": "TASK", "id": "T4"}, "scope": {"host": "H1"},
                   "assertion": "Workflow complete.", "status": "SUPPORTED",
                   "support_relation_refs": ["S-A4"]},
         "obligations": [{"obligation_id": "O-A4", "materiality": "MATERIAL",
                          "trigger": {"rule_ref": "R1", "observed": True},
                          "status": "PENDING"}]},
     "expect_block": ["COMPLETION_CLAIM_WITHOUT_OBLIGATION_REFS"]},

    # A5 (original): recovery STATE_AND_HISTORY, PRESERVED self-asserted, no evidence
    {"id": "A5-recovery-preserved-no-evidence", "kind": "ADVERSARIAL", "vector": "I_RECOVERED",
     "payload": {
         "transition": {"transition_id": "RT-A5",
                        "state_restore": {"target_checkpoint": "CP", "result": "SUCCESS",
                                          "evidence_refs": ["E-STATE-A5"]},
                        "history_continuity": {"status": "PRESERVED",
                                               "post_checkpoint_occurrence_delta_captured": None,
                                               "evidence_refs": []},
                        "recovery_claim": {"claim_ref": "C-REC-A5", "scope": "STATE_AND_HISTORY"}}},
     "expect_block": ["HISTORY_PRESERVED_WITHOUT_EVIDENCE", "HISTORY_PRESERVED_WITHOUT_DELTA_CAPTURE"]},

    # A6 (original): independence laundering with distinct labels, one root
    {"id": "A6-independence-laundering", "kind": "ADVERSARIAL", "vector": "EVIDENCE_INDEPENDENT",
     "payload": {
         "support": {"support_id": "S-A6", "claim_ref": "C-A6", "evidence_refs": ["E-A", "E-B", "E-C"],
                     "support_status": "SUPPORTS", "observed_scope": {"host": "H1"},
                     "claimed_scope": {"host": "H1"},
                     "independence_basis": {"claimed_independent_count": 3,
                                            "source_origins": ["derived-A", "derived-B", "derived-C"]}}},
     "expect_block": ["INDEPENDENCE_WITHOUT_ROOT_PROVENANCE"]},

    # A6b: laundering WITH a root field that reveals one root
    {"id": "A6b-independence-one-root", "kind": "ADVERSARIAL", "vector": "EVIDENCE_INDEPENDENT",
     "payload": {
         "support": {"support_id": "S-A6b", "claim_ref": "C-A6b", "evidence_refs": ["E-A", "E-B", "E-C"],
                     "support_status": "SUPPORTS", "observed_scope": {"host": "H1"},
                     "claimed_scope": {"host": "H1"},
                     "independence_basis": {"claimed_independent_count": 3,
                                            "source_origins": ["derived-A", "derived-B", "derived-C"],
                                            "root_provenance": ["ROOT-LOG", "ROOT-LOG", "ROOT-LOG"]}}},
     "expect_block": ["INDEPENDENCE_OVERCLAIMED"]},
]

# ---------------------------------------------------------- SECOND ORDER ----
FIXTURES += [
    # S1: SUPPORTED claim refs a support relation that itself has NO evidence
    {"id": "S1-supported-ref-to-empty-support", "kind": "SECOND_ORDER", "vector": "I_KNOW",
     "payload": {
         "claim": {"claim_id": "C-S1", "claim_type": "CAPABILITY_QUALIFICATION",
                   "subject": {"kind": "AGENT", "id": "me"}, "scope": {"host": "H1"},
                   "assertion": "verified", "status": "SUPPORTED",
                   "support_relation_refs": ["S-S1"]},
         "support_relations": [{"support_id": "S-S1", "claim_ref": "C-S1", "evidence_refs": [],
                                "support_status": "SUPPORTS"}]},
     "expect_block": ["SUPPORT_WITHOUT_EVIDENCE"]},

    # S2: authority mandate source present but is 'restore' (not authorizing)
    {"id": "S2-authority-mandate-restore", "kind": "SECOND_ORDER", "vector": "I_HAVE_AUTHORITY",
     "payload": {
         "binding": {"binding_id": "B-S2", "agent": "me", "host": "H1", "route": ["r"],
                     "authority_envelope": ["revoke leases"],
                     "mandate": {"source": "RESTORED_STATE", "expires_at": "2027-01-01"}}},
     "expect_block": ["AUTHORITY_MANDATE_SOURCE_NOT_AUTHORIZING"]},

    # S3: completion claim enumerates obligation refs but obligation is open
    {"id": "S3-completion-with-open-obligation", "kind": "SECOND_ORDER", "vector": "I_COMPLETED",
     "payload": {
         "claim": {"claim_id": "C-S3", "claim_type": "WORKFLOW_COMPLETION",
                   "subject": {"kind": "TASK", "id": "T3"}, "scope": {"host": "H1"},
                   "assertion": "done", "status": "SUPPORTED", "support_relation_refs": ["S-S3"],
                   "required_obligation_refs": ["O-S3"]},
         "obligations": [{"obligation_id": "O-S3", "materiality": "MATERIAL",
                          "trigger": {"rule_ref": "R", "observed": True}, "status": "PENDING"}]},
     "expect_block": ["COMPLETION_WITH_OPEN_MATERIAL_OBLIGATION"]},

    # S4: recovery with history evidence but SAME ref as state evidence
    {"id": "S4-recovery-history-same-evidence", "kind": "SECOND_ORDER", "vector": "I_RECOVERED",
     "payload": {
         "transition": {"transition_id": "RT-S4",
                        "state_restore": {"target_checkpoint": "CP", "result": "SUCCESS",
                                          "evidence_refs": ["E-SAME"]},
                        "history_continuity": {"status": "PRESERVED",
                                               "post_checkpoint_occurrence_delta_captured": True,
                                               "evidence_refs": ["E-SAME"]},
                        "recovery_claim": {"claim_ref": "C-REC-S4", "scope": "STATE_AND_HISTORY"}}},
     "expect_block": ["HISTORY_EVIDENCE_SAME_AS_STATE_EVIDENCE"]},

    # S5: independence with root provenance but claimed count > distinct roots
    {"id": "S5-independence-count-vs-roots", "kind": "SECOND_ORDER", "vector": "EVIDENCE_INDEPENDENT",
     "payload": {
         "support": {"support_id": "S-S5", "claim_ref": "C-S5", "evidence_refs": ["E1", "E2", "E3"],
                     "support_status": "SUPPORTS", "observed_scope": {"host": "H1"},
                     "claimed_scope": {"host": "H1"},
                     "independence_basis": {"claimed_independent_count": 3,
                                            "source_origins": ["A", "B", "C"],
                                            "root_provenance": ["R1", "R2"]}}},
     "expect_block": ["INDEPENDENCE_OVERCLAIMED"]},

    # S6: verified capability with grade E0 assertion only
    {"id": "S6-verified-grade-e0", "kind": "SECOND_ORDER", "vector": "I_VERIFIED",
     "payload": {
         "binding": {"binding_id": "B-S6", "agent": "me", "host": "H1", "route": ["r"],
                     "capabilities": [{"id": "ENA-CAP-048", "status": "VERIFIED_AVAILABLE",
                                       "evidence_refs": [{"ref": "self-assertion", "grade": "E0"}]}]}},
     "expect_block": ["VERIFIED_ONLY_STATIC_STRUCTURE_EVIDENCE"]},
]

def get_fixtures():
    return FIXTURES
