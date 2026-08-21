#!/usr/bin/env python3
"""V2.4 successor remediation controls — research prototype.

New controls authored for the successor corpus (Phase 3 regression discipline):
  * a legitimate positive control for every CONFIRMED false-OK fix (I01-I05,
    I08-I13, I15-I16);
  * an adversarial negative control proving each CONFIRMED false-BLOCK fix
    (I06 top-level support, I07 claim-aware obligations) did not reopen the
    original vulnerability;
  * representation-consistency controls (R3/R5/R6/R9/R11).

All controls are NEW fixtures; no historical fixture was rewritten.
"""
import copy

CONTROLS = []

def add(pid, kind, vector, expected, payload, rationale):
    CONTROLS.append({
        "id": pid, "kind": kind, "vector": vector,
        "expected_verdict": expected, "rationale": rationale,
        "payload": payload,
    })

# =============================== POSITIVES ================================
# I01/I09 positive: full-stack SUPPORTED claim, claim_ref matches, support
# evidence resolves, scope matches.
add("V24-P01-full-stack-supported", "POSITIVE", "I_KNOW", "OK", {
    "claim": {"claim_id": "C-V24P1", "claim_type": "CAPABILITY_QUALIFICATION",
              "subject": {"kind": "AGENT", "id": "me"}, "scope": {"host": "H1", "runtime_instance": "R1"},
              "assertion": "capability X verified", "status": "SUPPORTED",
              "support_relation_refs": ["S-V24P1"]},
    "support_registry": [
        {"support_id": "S-V24P1", "claim_ref": "C-V24P1", "evidence_refs": ["E-V24P1"],
         "support_status": "SUPPORTS", "observed_scope": {"host": "H1", "runtime_instance": "R1"},
         "claimed_scope": {"host": "H1", "runtime_instance": "R1"}}],
    "evidence_registry": {"E-V24P1": {"root_provenance": "R-A", "derived_from": None}},
}, "legitimate positive control for I01 (support-target binding) and I09 (support evidence resolution)")

# I10 positive: verified capability with RESOLVABLE E2 evidence.
add("V24-P02-verified-capability-resolvable-evidence", "POSITIVE", "I_VERIFIED", "OK", {
    "binding": {"binding_id": "B-V24P2", "agent": "me", "host": "H1", "route": ["r"],
                "capabilities": [{"id": "ENA-CAP-X", "status": "VERIFIED_AVAILABLE",
                                  "evidence_refs": [{"ref": "E-V24P2", "grade": "E2"}]}]},
    "evidence_registry": {"E-V24P2": {"root_provenance": "R-B", "derived_from": None}},
}, "legitimate positive control for I10 (evidence existence on capability path)")

# I02/I13 positive: full STATE_AND_HISTORY recovery with state+history evidence
# resolved and distinct roots.
add("V24-P03-full-recovery-both-evidence", "POSITIVE", "I_RECOVERED", "OK", {
    "transition": {"transition_id": "RT-V24P3",
                   "state_restore": {"target_checkpoint": "CP", "result": "SUCCESS", "evidence_refs": ["E-ST-V24P3"]},
                   "history_continuity": {"status": "PRESERVED", "post_checkpoint_occurrence_delta_captured": True,
                                          "evidence_refs": ["E-HI-V24P3"]},
                   "recovery_claim": {"claim_ref": "C-REC-V24P3", "scope": "STATE_AND_HISTORY"}},
    "evidence_registry": {"E-ST-V24P3": {"root_provenance": "ROOT-S", "derived_from": None},
                          "E-HI-V24P3": {"root_provenance": "ROOT-H", "derived_from": None}},
}, "legitimate positive control for I02 (present-but-missing evidence) and I13 (state evidence)")

# I03/I15 positive: independence with list-form root registry resolving distinct origins.
add("V24-P04-independence-resolvable-roots", "POSITIVE", "EVIDENCE_INDEPENDENT", "OK", {
    "support": {"support_id": "S-V24P4", "claim_ref": "C-V24P4", "evidence_refs": ["E1", "E2"],
                "support_status": "SUPPORTS", "observed_scope": {"host": "H1"}, "claimed_scope": {"host": "H1"},
                "independence_basis": {"claimed_independent_count": 2, "source_origins": ["A", "B"],
                                       "root_provenance": ["R1", "R2"]}},
    "root_registry": [{"id": "R1", "actual_origin": "O1"}, {"id": "R2", "actual_origin": "O2"}],
}, "legitimate positive control for I03 (root resolution) and I15 (list-form root registry)")

# I12 positive: transfer-based scope expansion with RESOLVABLE transfer evidence.
add("V24-P05-transfer-with-resolvable-evidence", "POSITIVE", "I_KNOW", "OK", {
    "claim": {"claim_id": "C-V24P5", "claim_type": "CAPABILITY_QUALIFICATION",
              "subject": {"kind": "AGENT", "id": "me"}, "scope": {"host": "H2"},
              "assertion": "verified", "status": "SUPPORTED", "support_relation_refs": ["S-V24P5"]},
    "support_registry": [
        {"support_id": "S-V24P5", "claim_ref": "C-V24P5", "evidence_refs": ["E-V24P5"],
         "support_status": "SUPPORTS", "observed_scope": {"host": "H1"}, "claimed_scope": {"host": "H2"},
         "transfer_basis": {"required": True, "type": "EQUIVALENCE", "evidence_refs": ["E-TR-V24P5"]}}],
    "evidence_registry": {"E-V24P5": {"root_provenance": "R-C", "derived_from": None},
                          "E-TR-V24P5": {"root_provenance": "R-C", "derived_from": None}},
}, "legitimate positive control for I12 (transfer evidence resolution)")

# I04/I05 positive: all 8 baseline applicability dimensions match.
add("V24-P06-full-applicability-envelope", "POSITIVE", "I_KNOW", "OK", {
    "claim": {"claim_id": "C-V24P6", "claim_type": "CAPABILITY_QUALIFICATION",
              "subject": {"kind": "AGENT", "id": "me"},
              "scope": {"host": "H1", "runtime_instance": "R1", "model_binding": "M1", "route": "r1",
                        "configuration": "cfg1", "epoch": "E1", "time_interval": "T1", "task_scope": "TS1"},
              "assertion": "verified", "status": "SUPPORTED", "support_relation_refs": ["S-V24P6"]},
    "support_registry": [
        {"support_id": "S-V24P6", "claim_ref": "C-V24P6", "evidence_refs": ["E-V24P6"],
         "support_status": "SUPPORTS",
         "observed_scope": {"host": "H1", "runtime_instance": "R1", "model_binding": "M1", "route": "r1",
                            "configuration": "cfg1", "epoch": "E1", "time_interval": "T1", "task_scope": "TS1"},
         "claimed_scope": {"host": "H1", "runtime_instance": "R1", "model_binding": "M1", "route": "r1",
                           "configuration": "cfg1", "epoch": "E1", "time_interval": "T1", "task_scope": "TS1"}}],
    "evidence_registry": {"E-V24P6": {"root_provenance": "R-D", "derived_from": None}},
}, "legitimate positive control for I04/I05 (full applicability envelope, all dimensions observed)")

# I06 positive: top-level support object composition.
add("V24-P07-top-level-support", "POSITIVE", "I_KNOW", "OK", {
    "claim": {"claim_id": "C-V24P7", "claim_type": "CAPABILITY_QUALIFICATION",
              "subject": {"kind": "AGENT", "id": "me"}, "scope": {"host": "H1"},
              "assertion": "verified", "status": "SUPPORTED", "support_relation_refs": ["S-V24P7"]},
    "support": {"support_id": "S-V24P7", "claim_ref": "C-V24P7", "evidence_refs": ["E-V24P7"],
                "support_status": "SUPPORTS", "observed_scope": {"host": "H1"}, "claimed_scope": {"host": "H1"}},
    "evidence_registry": {"E-V24P7": {"root_provenance": "R-E", "derived_from": None}},
}, "legitimate positive control for I06 (top-level support representation composes)")

# I07 positive: narrower completion with an unrelated other-claim obligation.
add("V24-P08-narrow-completion-unrelated-obligation", "POSITIVE", "I_COMPLETED", "OK", {
    "claim": {"claim_id": "C-V24P8", "claim_type": "WORKFLOW_COMPLETION",
              "subject": {"kind": "TASK", "id": "T8"}, "scope": {"host": "H1"},
              "assertion": "done", "status": "SUPPORTED", "support_relation_refs": ["S-V24P8"],
              "required_obligation_refs": ["O-GOOD-V24P8"]},
    "support_registry": [
        {"support_id": "S-V24P8", "claim_ref": "C-V24P8", "evidence_refs": ["E-V24P8"],
         "support_status": "SUPPORTS", "observed_scope": {"host": "H1"}, "claimed_scope": {"host": "H1"}}],
    "obligations": [
        {"obligation_id": "O-GOOD-V24P8", "materiality": "MATERIAL", "trigger": {"rule_ref": "R", "observed": True},
         "status": "SATISFIED", "closure_evidence_refs": ["E-CLOSE-V24P8"]},
        {"obligation_id": "O-OTHER-V24P8", "materiality": "MATERIAL", "trigger": {"rule_ref": "R2", "observed": True},
         "status": "PENDING", "required_before_claim_refs": ["C-ANOTHER"]}],
    "evidence_registry": {"E-V24P8": {"root_provenance": "R-F", "derived_from": None},
                          "E-CLOSE-V24P8": {"root_provenance": "R-F", "derived_from": None}},
}, "legitimate positive control for I07 (claim-aware obligation blocking)")

# I08/I16 positive: unique support IDs, same status, dict-form support registry.
add("V24-P09-dict-support-registry-unique-ids", "POSITIVE", "I_KNOW", "OK", {
    "claim": {"claim_id": "C-V24P9", "claim_type": "CAPABILITY_QUALIFICATION",
              "subject": {"kind": "AGENT", "id": "me"}, "scope": {"host": "H1"},
              "assertion": "verified", "status": "SUPPORTED", "support_relation_refs": ["S-V24P9"]},
    "support_registry": {
        "S-V24P9": {"support_id": "S-V24P9", "claim_ref": "C-V24P9", "evidence_refs": ["E-V24P9"],
                    "support_status": "SUPPORTS", "observed_scope": {"host": "H1"}, "claimed_scope": {"host": "H1"}}},
    "evidence_registry": {"E-V24P9": {"root_provenance": "R-G", "derived_from": None}},
}, "legitimate positive control for I08 (identity uniqueness) and I16 (dict-form support registry)")

# I11 positive: USER_EXPLICIT_GRANT mandate, valid horizon.
add("V24-P10-typed-mandate-source", "POSITIVE", "I_HAVE_AUTHORITY", "OK", {
    "binding": {"binding_id": "B-V24P10", "agent": "me", "host": "H1", "route": ["r"],
                "authority_envelope": ["approve stable admission"],
                "mandate": {"source": "USER_EXPLICIT_GRANT", "expires_at": "2999-01-01"}},
}, "legitimate positive control for I11 (positively typed mandate source)")

# I14 positive: explicitly narrowed PARTIAL claim.
add("V24-P11-narrowed-partial-claim", "POSITIVE", "I_KNOW", "OK", {
    "claim": {"claim_id": "C-V24P11", "claim_type": "CAPABILITY_QUALIFICATION",
              "subject": {"kind": "AGENT", "id": "me"}, "scope": {"host": "H1"},
              "assertion": "partially verified subset", "status": "SUPPORTED",
              "support_claim": "PARTIAL", "support_relation_refs": ["S-V24P11"]},
    "support_registry": [
        {"support_id": "S-V24P11", "claim_ref": "C-V24P11", "evidence_refs": ["E-V24P11"],
         "support_status": "PARTIAL", "observed_scope": {"host": "H1"}, "claimed_scope": {"host": "H1"}}],
    "evidence_registry": {"E-V24P11": {"root_provenance": "R-H", "derived_from": None}},
}, "legitimate positive control for I14 (explicitly narrowed partial claim is OK)")

# R5 positive: byte-identical duplicate support entries dedupe.
add("V24-P12-identical-duplicate-dedup", "POSITIVE", "I_KNOW", "OK", {
    "claim": {"claim_id": "C-V24P12", "claim_type": "CAPABILITY_QUALIFICATION",
              "subject": {"kind": "AGENT", "id": "me"}, "scope": {"host": "H1"},
              "assertion": "verified", "status": "SUPPORTED", "support_relation_refs": ["S-V24P12"]},
    "support_registry": [
        {"support_id": "S-V24P12", "claim_ref": "C-V24P12", "evidence_refs": ["E-V24P12"],
         "support_status": "SUPPORTS", "observed_scope": {"host": "H1"}, "claimed_scope": {"host": "H1"}},
        {"support_id": "S-V24P12", "claim_ref": "C-V24P12", "evidence_refs": ["E-V24P12"],
         "support_status": "SUPPORTS", "observed_scope": {"host": "H1"}, "claimed_scope": {"host": "H1"}}],
    "evidence_registry": {"E-V24P12": {"root_provenance": "R-I", "derived_from": None}},
}, "R5: byte-identical duplicates are the same artifact, not an ambiguity")

# R9 upstream positive: authority_registry grant verifies a non-whitelist source.
add("V24-P13-authority-registry-grant", "POSITIVE", "I_HAVE_AUTHORITY", "OK", {
    "binding": {"binding_id": "B-V24P13", "agent": "agent-A", "host": "H1", "route": ["r"],
                "authority_envelope": ["approve consequential effect"],
                "mandate": {"source": "GRANT-1", "expires_at": "2999-01-01"}},
    "authority_registry": [{"grant_id": "GRANT-1", "agent": "agent-A", "host": "H1", "expires_at": "2999-12-31"}],
}, "R9: mandate source positively verified via an upstream authority registry")

# R6 positive: top-level support and registry carry identical entries -> OK.
add("V24-P14-top-level-and-registry-consistent", "POSITIVE", "I_KNOW", "OK", {
    "claim": {"claim_id": "C-V24P14", "claim_type": "CAPABILITY_QUALIFICATION",
              "subject": {"kind": "AGENT", "id": "me"}, "scope": {"host": "H1"},
              "assertion": "verified", "status": "SUPPORTED", "support_relation_refs": ["S-V24P14"]},
    "support": {"support_id": "S-V24P14", "claim_ref": "C-V24P14", "evidence_refs": ["E-V24P14"],
                "support_status": "SUPPORTS", "observed_scope": {"host": "H1"}, "claimed_scope": {"host": "H1"}},
    "support_registry": [
        {"support_id": "S-V24P14", "claim_ref": "C-V24P14", "evidence_refs": ["E-V24P14"],
         "support_status": "SUPPORTS", "observed_scope": {"host": "H1"}, "claimed_scope": {"host": "H1"}}],
    "evidence_registry": {"E-V24P14": {"root_provenance": "R-J", "derived_from": None}},
}, "R6: identical top-level and registry representations compose (deduped)")

# R3 representation positive: list-form evidence registry resolves.
add("V24-P15-list-evidence-registry", "POSITIVE", "I_KNOW", "OK", {
    "claim": {"claim_id": "C-V24P15", "claim_type": "CAPABILITY_QUALIFICATION",
              "subject": {"kind": "AGENT", "id": "me"}, "scope": {"host": "H1"},
              "assertion": "verified", "status": "SUPPORTED", "support_relation_refs": ["S-V24P15"]},
    "support_registry": [
        {"support_id": "S-V24P15", "claim_ref": "C-V24P15", "evidence_refs": ["E-V24P15"],
         "support_status": "SUPPORTS", "observed_scope": {"host": "H1"}, "claimed_scope": {"host": "H1"}}],
    "evidence_registry": [{"evidence_id": "E-V24P15", "root_provenance": "R-K", "derived_from": None}],
}, "R3: list-form evidence registry composes with support evidence resolution")

# =============================== NEGATIVES ================================
# I06 relaxation guard: top-level support with WRONG claim_ref must BLOCK.
add("V24-A01-top-level-support-wrong-claim-ref", "ADVERSARIAL", "I_KNOW", "BLOCK", {
    "claim": {"claim_id": "C-V24A1", "claim_type": "CAPABILITY_QUALIFICATION",
              "subject": {"kind": "AGENT", "id": "me"}, "scope": {"host": "H1"},
              "assertion": "verified", "status": "SUPPORTED", "support_relation_refs": ["S-V24A1"]},
    "support": {"support_id": "S-V24A1", "claim_ref": "C-OTHER", "evidence_refs": ["E-V24A1"],
                "support_status": "SUPPORTS", "observed_scope": {"host": "H1"}, "claimed_scope": {"host": "H1"}},
}, "I06 fix (top-level support composes) must not reopen I01: wrong claim_ref still BLOCKs")

# I07 relaxation guard: the claim's OWN open material obligation still blocks.
add("V24-A02-own-open-obligation-blocks", "ADVERSARIAL", "I_COMPLETED", "BLOCK", {
    "claim": {"claim_id": "C-V24A2", "claim_type": "WORKFLOW_COMPLETION",
              "subject": {"kind": "TASK", "id": "T2"}, "scope": {"host": "H1"},
              "assertion": "done", "status": "SUPPORTED", "support_relation_refs": ["S-V24A2"],
              "required_obligation_refs": ["O-OWN-V24A2"]},
    "support_registry": [
        {"support_id": "S-V24A2", "claim_ref": "C-V24A2", "evidence_refs": ["E-V24A2"],
         "support_status": "SUPPORTS", "observed_scope": {"host": "H1"}, "claimed_scope": {"host": "H1"}}],
    "obligations": [
        {"obligation_id": "O-OWN-V24A2", "materiality": "MATERIAL", "trigger": {"rule_ref": "R", "observed": True},
         "status": "PENDING"}],
}, "I07 fix (claim-aware) must not reopen S3: the claim's OWN open material obligation still BLOCKs")

# R7 guard: an obligation explicitly bound to THIS claim blocks it.
add("V24-A03-bound-open-obligation-blocks", "ADVERSARIAL", "I_COMPLETED", "BLOCK", {
    "claim": {"claim_id": "C-V24A3", "claim_type": "WORKFLOW_COMPLETION",
              "subject": {"kind": "TASK", "id": "T3"}, "scope": {"host": "H1"},
              "assertion": "done", "status": "SUPPORTED", "support_relation_refs": ["S-V24A3"],
              "required_obligation_refs": ["O-GOOD-V24A3"]},
    "support_registry": [
        {"support_id": "S-V24A3", "claim_ref": "C-V24A3", "evidence_refs": ["E-V24A3"],
         "support_status": "SUPPORTS", "observed_scope": {"host": "H1"}, "claimed_scope": {"host": "H1"}}],
    "obligations": [
        {"obligation_id": "O-GOOD-V24A3", "materiality": "MATERIAL", "trigger": {"rule_ref": "R", "observed": True},
         "status": "SATISFIED", "closure_evidence_refs": ["E-CLOSE-V24A3"]},
        {"obligation_id": "O-BOUND-V24A3", "materiality": "MATERIAL", "trigger": {"rule_ref": "R2", "observed": True},
         "status": "PENDING", "required_before_claim_refs": ["C-V24A3"]}],
    "evidence_registry": {"E-V24A3": {"root_provenance": "R-L", "derived_from": None},
                          "E-CLOSE-V24A3": {"root_provenance": "R-L", "derived_from": None}},
}, "R7: an open obligation explicitly bound to this claim still gates it")

# R11 negative: malformed support registry shape -> explicit BLOCK, no exception.
add("V24-A04-malformed-support-registry", "ADVERSARIAL", "I_KNOW", "BLOCK", {
    "claim": {"claim_id": "C-V24A4", "claim_type": "CAPABILITY_QUALIFICATION",
              "subject": {"kind": "AGENT", "id": "me"}, "scope": {"host": "H1"},
              "assertion": "verified", "status": "SUPPORTED", "support_relation_refs": ["S-V24A4"]},
    "support_registry": ["not-an-artifact", "also-not"],
}, "R11: malformed registry shape yields REGISTRY_MALFORMED, never an exception")

# R11 negative: malformed root registry shape -> explicit BLOCK.
add("V24-A05-malformed-root-registry", "ADVERSARIAL", "EVIDENCE_INDEPENDENT", "BLOCK", {
    "support": {"support_id": "S-V24A5", "claim_ref": "C-V24A5", "evidence_refs": ["E1"],
                "support_status": "SUPPORTS", "observed_scope": {"host": "H1"}, "claimed_scope": {"host": "H1"},
                "independence_basis": {"claimed_independent_count": 2, "source_origins": ["A", "B"],
                                       "root_provenance": ["R1", "R2"]}},
    "root_registry": [{"id": "R1"}, "garbage"],
}, "R11: malformed root registry shape yields REGISTRY_MALFORMED, never an exception")

# R1 negative: support ref pointing only at an evidence-namespace id must not resolve.
add("V24-A06-support-ref-type-scoped", "ADVERSARIAL", "I_KNOW", "BLOCK", {
    "claim": {"claim_id": "C-V24A6", "claim_type": "CAPABILITY_QUALIFICATION",
              "subject": {"kind": "AGENT", "id": "me"}, "scope": {"host": "H1"},
              "assertion": "verified", "status": "SUPPORTED", "support_relation_refs": ["E-ONLY"]},
    "evidence_registry": {"E-ONLY": {"root_provenance": "R-M", "derived_from": None}},
}, "R1: refs resolve within their own artifact type; an evidence id is not a support")

# R3 negative: capability evidence missing from a PRESENT registry.
add("V24-A07-capability-evidence-missing-present-registry", "ADVERSARIAL", "I_VERIFIED", "BLOCK", {
    "binding": {"binding_id": "B-V24A7", "agent": "me", "host": "H1", "route": ["r"],
                "capabilities": [{"id": "ENA-CAP-X", "status": "VERIFIED_AVAILABLE",
                                  "evidence_refs": [{"ref": "E-GONE", "grade": "E2"}]}]},
    "evidence_registry": {"E-OTHER": {"root_provenance": "R-N", "derived_from": None}},
}, "R3: grade E2 cannot substitute for evidence existence when the registry is supplied")

# R5 negative: duplicate support ids, same status, different scope -> ambiguous.
add("V24-A08-duplicate-same-status-different-scope", "ADVERSARIAL", "I_KNOW", "BLOCK", {
    "claim": {"claim_id": "C-V24A8", "claim_type": "CAPABILITY_QUALIFICATION",
              "subject": {"kind": "AGENT", "id": "me"}, "scope": {"host": "H1"},
              "assertion": "verified", "status": "SUPPORTED", "support_relation_refs": ["S-DUP-V24A8"]},
    "support_registry": [
        {"support_id": "S-DUP-V24A8", "claim_ref": "C-V24A8", "evidence_refs": ["E-a"],
         "support_status": "SUPPORTS", "observed_scope": {"host": "H1"}, "claimed_scope": {"host": "H1"}},
        {"support_id": "S-DUP-V24A8", "claim_ref": "C-V24A8", "evidence_refs": ["E-b"],
         "support_status": "SUPPORTS", "observed_scope": {"host": "H2"}, "claimed_scope": {"host": "H2"}}],
}, "R5: identity ambiguity exists beyond status-token differences (different scope)")

# R9 negative: authority registry present but grant missing.
add("V24-A09-authority-registry-missing-grant", "ADVERSARIAL", "I_HAVE_AUTHORITY", "BLOCK", {
    "binding": {"binding_id": "B-V24A9", "agent": "agent-A", "host": "H1", "route": ["r"],
                "authority_envelope": ["approve consequential effect"],
                "mandate": {"source": "GRANT-X", "expires_at": "2999-01-01"}},
    "authority_registry": [{"grant_id": "GRANT-OTHER", "agent": "agent-A", "host": "H1", "expires_at": "2999-12-31"}],
}, "R9: a present authority registry that does not contain the grant does not authorize")

# R3 negative: support evidence missing from a PRESENT (list-form) registry.
add("V24-A10-support-evidence-missing-list-registry", "ADVERSARIAL", "I_KNOW", "BLOCK", {
    "claim": {"claim_id": "C-V24A10", "claim_type": "CAPABILITY_QUALIFICATION",
              "subject": {"kind": "AGENT", "id": "me"}, "scope": {"host": "H1"},
              "assertion": "verified", "status": "SUPPORTED", "support_relation_refs": ["S-V24A10"]},
    "support_registry": [
        {"support_id": "S-V24A10", "claim_ref": "C-V24A10", "evidence_refs": ["E-V24A10"],
         "support_status": "SUPPORTS", "observed_scope": {"host": "H1"}, "claimed_scope": {"host": "H1"}}],
    "evidence_registry": [{"evidence_id": "E-OTHER10", "root_provenance": "R-O", "derived_from": None}],
}, "R3: list-form registry present but missing the referenced evidence still BLOCKs")


def get_controls():
    return copy.deepcopy(CONTROLS)
