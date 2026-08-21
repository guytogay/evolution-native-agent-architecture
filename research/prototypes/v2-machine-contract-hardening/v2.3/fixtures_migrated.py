#!/usr/bin/env python3
"""V2.3 migrated positive controls — research prototype (UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED).

The five historical positive fixtures that no longer reach OK under the
composed cumulative contract (P1/P5/P6 -> BLOCK, P7/P9 -> UNKNOWN) are preserved
UNCHANGED in their original modules (fixtures.py). These migrated equivalents
supply exactly the registry / provenance / support information the cumulative
contract now legitimately requires — completing the claim pack, NOT weakening
any resolvability / provenance protection.

Each migrated fixture:
  * keeps the original claim's semantic content;
  * adds the missing resolution source (support_registry / evidence_registry /
    root_registry) with internally consistent, applicable, evidence-carrying
    artifacts;
  * must reach OK through the SAME composed candidate implementation.
"""
import copy

MIGRATED_FIXTURES = [
    # ---- P1m: migrated P1 (SUPPORTED claim) — supplies support registry ----
    {"id": "P1m-supported-with-refs", "kind": "POSITIVE", "vector": "I_KNOW",
     "migrated_from": "P1-supported-with-refs",
     "case": "P1 + support_registry: S-P1 resolves, carries evidence, scope applies",
     "payload": {
         "claim": {"claim_id": "C-P1", "claim_type": "CAPABILITY_QUALIFICATION",
                   "subject": {"kind": "AGENT", "id": "me"}, "scope": {"host": "H1"},
                   "assertion": "capability X verified", "status": "SUPPORTED",
                   "support_relation_refs": ["S-P1"]},
         "support_registry": [
             {"support_id": "S-P1", "claim_ref": "C-P1", "evidence_refs": ["E-P1m"],
              "support_status": "SUPPORTS", "observed_scope": {"host": "H1"},
              "claimed_scope": {"host": "H1"}}]},
     "expect_pass": True},

    # ---- P5m: migrated P5 (completion, satisfied obligations) — supplies support registry ----
    {"id": "P5m-completion-satisfied", "kind": "POSITIVE", "vector": "I_COMPLETED",
     "migrated_from": "P5-completion-satisfied",
     "case": "P5 + support_registry: S-P5 resolves with evidence; O-P5 satisfied with closure evidence",
     "payload": {
         "claim": {"claim_id": "C-P5", "claim_type": "WORKFLOW_COMPLETION",
                   "subject": {"kind": "TASK", "id": "T5"}, "scope": {"host": "H1"},
                   "assertion": "done", "status": "SUPPORTED",
                   "support_relation_refs": ["S-P5"],
                   "required_obligation_refs": ["O-P5"]},
         "obligations": [{"obligation_id": "O-P5", "materiality": "MATERIAL",
                          "trigger": {"rule_ref": "R", "observed": True},
                          "status": "SATISFIED", "closure_evidence_refs": ["E-CLOSE-P5"]}],
         "support_registry": [
             {"support_id": "S-P5", "claim_ref": "C-P5", "evidence_refs": ["E-P5m"],
              "support_status": "SUPPORTS", "observed_scope": {"host": "H1"},
              "claimed_scope": {"host": "H1"}}]},
     "expect_pass": True},

    # ---- P6m: migrated P6 (completion, non-material obligation) — supplies support registry ----
    {"id": "P6m-nonmaterial-obligation-ok", "kind": "POSITIVE", "vector": "I_COMPLETED",
     "migrated_from": "P6-nonmaterial-obligation-ok",
     "case": "P6 + support_registry: S-P6 resolves with evidence; O-P6 NON_MATERIAL PENDING does not block",
     "payload": {
         "claim": {"claim_id": "C-P6", "claim_type": "WORKFLOW_COMPLETION",
                   "subject": {"kind": "TASK", "id": "T6"}, "scope": {"host": "H1"},
                   "assertion": "done", "status": "SUPPORTED", "support_relation_refs": ["S-P6"],
                   "required_obligation_refs": ["O-P6"]},
         "obligations": [{"obligation_id": "O-P6", "materiality": "NON_MATERIAL",
                          "trigger": {"rule_ref": "R", "observed": True}, "status": "PENDING"}],
         "support_registry": [
             {"support_id": "S-P6", "claim_ref": "C-P6", "evidence_refs": ["E-P6m"],
              "support_status": "SUPPORTS", "observed_scope": {"host": "H1"},
              "claimed_scope": {"host": "H1"}}]},
     "expect_pass": True},

    # ---- P7m: migrated P7 (STATE_AND_HISTORY recovery) — supplies evidence registry ----
    {"id": "P7m-recovery-with-history-evidence", "kind": "POSITIVE", "vector": "I_RECOVERED",
     "migrated_from": "P7-recovery-with-history-evidence",
     "case": "P7 + evidence_registry: E-STATE-P7 and E-HIST-P7 register DISTINCT roots",
     "payload": {
         "transition": {"transition_id": "RT-P7",
                        "state_restore": {"target_checkpoint": "CP", "result": "SUCCESS",
                                          "evidence_refs": ["E-STATE-P7"]},
                        "history_continuity": {"status": "PRESERVED",
                                               "post_checkpoint_occurrence_delta_captured": True,
                                               "evidence_refs": ["E-HIST-P7"]},
                        "recovery_claim": {"claim_ref": "C-REC-P7", "scope": "STATE_AND_HISTORY"}},
         "evidence_registry": {
             "E-STATE-P7": {"root_provenance": "ROOT-S7", "derived_from": None},
             "E-HIST-P7": {"root_provenance": "ROOT-H7", "derived_from": None}}},
     "expect_pass": True},

    # ---- P9m: migrated P9 (independence) — supplies root registry ----
    {"id": "P9m-independence-distinct-roots", "kind": "POSITIVE", "vector": "EVIDENCE_INDEPENDENT",
     "migrated_from": "P9-independence-distinct-roots",
     "case": "P9 + root_registry: ROOT-A/ROOT-B register DISTINCT actual origins; claimed 2 <= 2",
     "payload": {
         "support": {"support_id": "S-P9", "claim_ref": "C-P9", "evidence_refs": ["E-A", "E-B"],
                     "support_status": "SUPPORTS", "observed_scope": {"host": "H1"},
                     "claimed_scope": {"host": "H1"},
                     "independence_basis": {"claimed_independent_count": 2,
                                            "source_origins": ["A", "B"],
                                            "root_provenance": ["ROOT-A", "ROOT-B"]}},
         "root_registry": {"ROOT-A": {"actual_origin": "ROOT-A"},
                           "ROOT-B": {"actual_origin": "ROOT-B"}}},
     "expect_pass": True},
]


def get_migrated_fixtures():
    return copy.deepcopy(MIGRATED_FIXTURES)
