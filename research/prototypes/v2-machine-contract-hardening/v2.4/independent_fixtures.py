#!/usr/bin/env python3
"""V2.4 independent validation fixtures — provenance preserved.

These fixtures are EXACTLY the executable probes authored by the independent
validator (GPT-5.6 Sol) in the merged CI workflow
`.github/workflows/independent-v23-validation.yml` (PR #23), extracted verbatim
with their independent semantic expectations. They are preserved intact (no
rewriting) so the successor must satisfy them as independent ground truth.

Each fixture: id, provenance, independent_expect (the validator's semantic
expectation), payload. `independent_expect` is the INDEPENDENT expectation —
the successor's own structural oracle may refine it (e.g. I14 UNKNOWN_OR_BLOCK
-> UNKNOWN), and the reconciliation records any such refinement.
"""
import copy

I_FIXTURES = []


def claim(cid="C1", **kw):
    d = {
        "claim_id": cid,
        "claim_type": "CAPABILITY_QUALIFICATION",
        "subject": {"kind": "AGENT", "id": "agent-A"},
        "scope": {"host": "H1"},
        "assertion": "material claim",
        "status": "SUPPORTED",
        "support_relation_refs": ["S1"],
    }
    d.update(kw)
    return d


def support(sid="S1", cref="C1", **kw):
    d = {
        "support_id": sid,
        "claim_ref": cref,
        "evidence_refs": ["E1"],
        "support_status": "SUPPORTS",
        "observed_scope": {"host": "H1"},
        "claimed_scope": {"host": "H1"},
    }
    d.update(kw)
    return d


def add(name, independent_expect, payload, rationale, probe_kind="INDEPENDENT"):
    I_FIXTURES.append({
        "id": name,
        "kind": probe_kind,
        "provenance": "GPT-5.6 Sol (independent validator), via merged CI evidence PR #23",
        "independent_expect": independent_expect,
        "rationale": rationale,
        "payload": payload,
    })


add("I01-support-target-mismatch", "BLOCK", {
    "claim": claim(),
    "support_registry": [support(cref="C-OTHER")],
}, "Resolved support relation targets another claim; borrowing another claim support must not endorse C1.")

add("I02-recovery-empty-present-registry", "BLOCK", {
    "transition": {
        "transition_id": "RT-I02",
        "state_restore": {"target_checkpoint": "CP", "result": "SUCCESS", "evidence_refs": ["E-STATE"]},
        "history_continuity": {"status": "PRESERVED", "post_checkpoint_occurrence_delta_captured": True, "evidence_refs": ["E-HIST"]},
        "recovery_claim": {"claim_ref": "C-REC-I02", "scope": "STATE_AND_HISTORY"},
    },
    "evidence_registry": {},
}, "Registry is present but both mandatory evidence refs are unresolved; this is broken evidence, not verified distinct provenance.")

add("I03-independence-empty-present-root-registry", "BLOCK", {
    "support": {
        "support_id": "S-I03", "claim_ref": "C-I03", "evidence_refs": ["E1", "E2"],
        "support_status": "SUPPORTS", "observed_scope": {"host": "H1"}, "claimed_scope": {"host": "H1"},
        "independence_basis": {"claimed_independent_count": 2, "source_origins": ["A", "B"], "root_provenance": ["R1", "R2"]},
    },
    "root_registry": {},
}, "Present-but-incomplete root registry must not fall back to raw root labels as verified origins.")

add("I04-support-model-binding-mismatch", "BLOCK", {
    "claim": claim(scope={"host": "H1", "model_binding": "M2"}),
    "support_registry": [support(observed_scope={"host": "H1", "model_binding": "M1"}, claimed_scope={"host": "H1", "model_binding": "M2"})],
}, "Model binding is an applicability boundary in the baseline contract; mismatch needs transfer evidence.")

add("I05-support-missing-runtime-observation", "BLOCK", {
    "claim": claim(scope={"host": "H1", "runtime_instance": "R2"}),
    "support_registry": [support(observed_scope={"host": "H1"}, claimed_scope={"host": "H1", "runtime_instance": "R2"})],
}, "Claimed runtime instance is not observed; absence of observed applicability cannot be treated as a direct match.")

add("I06-top-level-support-composes-legitimately", "OK", {
    "claim": claim(),
    "support": support(),
}, "The exact referenced support artifact is present as the top-level support object and passes the shipped support validator.")

add("I07-unrelated-open-obligation-does-not-block-narrow-claim", "OK", {
    "claim": claim(claim_type="TASK_COMPLETION", required_obligation_refs=["O-GOOD"]),
    "support_registry": [support()],
    "obligations": [
        {"obligation_id": "O-GOOD", "materiality": "MATERIAL", "trigger": {"rule_ref": "R1", "observed": True}, "status": "SATISFIED", "closure_evidence_refs": ["E-CLOSE"]},
        {"obligation_id": "O-OTHER", "materiality": "MATERIAL", "trigger": {"rule_ref": "R2", "observed": True}, "status": "PENDING", "required_before_claim_refs": ["C-OTHER"]},
    ],
}, "Core semantics explicitly allow narrower truthful completion; an unrelated obligation tied to another claim should not globally poison this claim.")

add("I08-duplicate-support-id-same-status-ambiguous", "BLOCK", {
    "claim": claim(),
    "support_registry": [
        support(cref="C-OTHER", evidence_refs=["E-OTHER"]),
        support(cref="C1", evidence_refs=["E-RIGHT"]),
    ],
}, "Duplicate IDs remain ambiguous even when support_status strings happen to match; resolution order must not decide truth.")

add("I09-support-evidence-ref-unresolved", "BLOCK", {
    "claim": claim(),
    "support_registry": [support(evidence_refs=["E-NOPE"])],
    "evidence_registry": {},
}, "A support artifact carrying a nonempty but nonexistent evidence ref does not have resolvable evidence.")

add("I10-verified-capability-evidence-ref-unresolved", "BLOCK", {
    "binding": {
        "binding_id": "B-I10", "agent": "agent-A", "host": "H1", "route": ["r"],
        "capabilities": [{"id": "ENA-CAP-X", "status": "VERIFIED_AVAILABLE", "evidence_refs": [{"ref": "E-NOPE", "grade": "E5"}]}],
    },
    "evidence_registry": {},
}, "A high self-declared grade cannot substitute for existence/resolution of the referenced evidence artifact.")

add("I11-self-asserted-mandate-source", "BLOCK", {
    "binding": {
        "binding_id": "B-I11", "agent": "agent-A", "host": "H1", "route": ["r"],
        "authority_envelope": ["approve consequential effect"],
        "mandate": {"source": "SELF_ASSERTED", "expires_at": "2999-01-01"},
    },
}, "A source token that is explicitly self-asserted is not an authorizing mandate source merely because it is nonempty and not on a small denylist.")

add("I12-transfer-evidence-ref-unresolved", "BLOCK", {
    "claim": claim(scope={"host": "H2"}),
    "support_registry": [support(observed_scope={"host": "H1"}, claimed_scope={"host": "H2"},
                                 transfer_basis={"required": True, "type": "EQUIVALENCE", "evidence_refs": ["E-TRANSFER-NOPE"]})],
    "evidence_registry": {},
}, "Scope transfer is itself consequential evidence and its evidence refs must resolve; nonempty strings are insufficient.")

add("I13-recovery-full-claim-without-state-evidence", "BLOCK", {
    "transition": {
        "transition_id": "RT-I13",
        "state_restore": {"target_checkpoint": "CP", "result": "SUCCESS", "evidence_refs": []},
        "history_continuity": {"status": "PRESERVED", "post_checkpoint_occurrence_delta_captured": True, "evidence_refs": ["E-HIST"]},
        "recovery_claim": {"claim_ref": "C-REC-I13", "scope": "STATE_AND_HISTORY"},
    },
    "evidence_registry": {"E-HIST": {"root_provenance": "RH"}},
}, "A consequential STATE_AND_HISTORY recovery claim needs positive evidence of state restoration as well as history continuity.")

add("I14-supported-claim-only-partial-support", "UNKNOWN_OR_BLOCK", {
    "claim": claim(),
    "support_registry": [support(support_status="PARTIAL")],
}, "PARTIAL support does not by itself establish a full SUPPORTED claim unless the assertion is explicitly narrowed to the supported envelope.")

add("I15-root-registry-list-shape", "NO_EXCEPTION", {
    "support": {
        "support_id": "S-I15", "claim_ref": "C-I15", "evidence_refs": ["E1", "E2"],
        "support_status": "SUPPORTS", "observed_scope": {"host": "H1"}, "claimed_scope": {"host": "H1"},
        "independence_basis": {"claimed_independent_count": 2, "source_origins": ["A", "B"], "root_provenance": ["R1", "R2"]},
    },
    "root_registry": [
        {"id": "R1", "actual_origin": "O1"}, {"id": "R2", "actual_origin": "O2"}
    ],
}, "evaluate() accepts list-valued *_registry inputs generically; a plausible registry shape should not crash the machine contract.")

add("I16-support-registry-dict-shape", "NO_EXCEPTION", {
    "claim": claim(),
    "support_registry": {
        "S1": support(),
    },
}, "evaluate() accepts dict-valued *_registry inputs generically; registry representation differences should fail semantically, not raise AttributeError.")

# ---- oracle-consistency probes (independent validator, §6 / §10.12) ----
add("O01-legitimate-but-labeled-ATTACK", "OK", {
    "claim": {"claim_id": "C-O1", "claim_type": "OTHER", "subject": {"kind": "TASK", "id": "T"},
              "scope": {"host": "H1"}, "assertion": "hypothesis", "status": "ASSERTED"},
}, "Expected verdict must derive from semantics, not from fixture kind label (ATTACK).", probe_kind="ORACLE_PROBE")

add("O02-malformed-reusing-migrated-id", "BLOCK", {
    "claim": claim(cid="C-OM"),
}, "Reusing a hard-coded migrated ID must not force expected OK; structure (no registries) decides the verdict.", probe_kind="ORACLE_PROBE")

add("O03-empty-registry-recovery-classifier", "BLOCK", {
    "transition": {
        "transition_id": "RT-O03",
        "state_restore": {"target_checkpoint": "CP", "result": "SUCCESS", "evidence_refs": ["E-STATE"]},
        "history_continuity": {"status": "PRESERVED", "post_checkpoint_occurrence_delta_captured": True, "evidence_refs": ["E-HIST"]},
        "recovery_claim": {"claim_ref": "C-REC-O03", "scope": "STATE_AND_HISTORY"},
    },
    "evidence_registry": {},
}, "Empty present evidence registry must not classify as sufficient-positive; the shared blind spot must not reappear in the oracle.", probe_kind="ORACLE_PROBE")

add("O04-top-level-support-classifier", "OK", {
    "claim": claim(),
    "support": support(),
}, "Top-level support composition is legitimate; oracle and evaluator must agree on representation.", probe_kind="ORACLE_PROBE")


def get_independent_fixtures():
    return copy.deepcopy(I_FIXTURES)
