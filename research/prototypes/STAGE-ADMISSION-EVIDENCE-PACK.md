# Stage Admission Evidence Pack

Status: `RESEARCH_PROTOTYPE / NON_NORMATIVE / MAINLINE_UNCHANGED`
Baseline: `ENA v0.2.11 MAINLINE`
Date: `2026-08-20`

Bridge status:

```yaml
bridge_state:
  source_surface: GITHUB
  target_surface: GOOGLE_DRIVE
  target_location: "ENA / 20 Research / 30 Prototypes"
  status: FAILED
  reason: "Drive connector blocked the create action because it could not determine the request safety state."
  persisted_on_drive: false
```

## Purpose

Operationalize an already-existing ENA requirement: developmental stage admission must be evidence-gated. Agent self-report may propose a claim, but cannot by itself establish capability, role qualification, health, recovery, or developmental-stage eligibility.

This prototype does **not** add a new ENA rule. It makes current Mainline semantics easier to apply consistently, especially for models whose self-report calibration is weak or hallucination-prone.

## Existing Mainline basis

Current v0.2.11 already requires:

- `SELF_POSITIONING_REQUIRED` before P0;
- selection of the highest stage whose entry requirements are evidenced;
- no P0 skip by reputation alone;
- Evidence Model classes E0-E5, where self-report is E0 Assertion;
- independent environmental trace evidence as a stronger source than self-report where applicable;
- stage gates between P0-P5.

## Core distinction

`Self-assessment claim != admitted capability != admitted stage != authority`

Self-assessment is useful for hypothesis generation, test planning, and calibration measurement. It is not sufficient for stage admission.

## Proposed evidence pack

```yaml
stage_admission:
  subject_ref: "<agent/host/system identity>"
  baseline: "ENA v0.2.11 MAINLINE"
  requested_stage: "P0 | P1 | P2 | P3 | P4 | P5"
  current_admitted_stage: "SELF_POSITIONING_REQUIRED | P0 | P1 | P2 | P3 | P4 | P5"

  self_claims:
    - claim_id: ""
      claim: ""
      evidence_class: "E0_ASSERTION"

  capability_requirements:
    - capability_or_property: ""
      required_for_gate: true
      minimum_evidence_expectation: "E1 | E2 | E3 | E4 | E5 | MIXED"
      evidence_refs: []
      applicability:
        subject_ref: ""
        host_identity: ""
        runtime_instance_ref: ""
        configuration_state_ref: ""
        epoch_or_version: ""
        scope: []
        observed_from: ""
        observed_to: ""
      limitations: []
      revalidate_when: []
      verdict: "EVIDENCED | PARTIAL | NOT_EVIDENCED | CONTRADICTED | UNKNOWN"

  controlled_tests: []
  failure_injection_tests: []
  independent_environmental_traces: []
  independent_reviews: []

  gate_result:
    gate: "BOOTSTRAP | P0_TO_P1 | P1_TO_P2 | P2_TO_P3 | P3_TO_P4 | P4_TO_P5"
    result: "PASS | FAIL | PARTIAL | UNKNOWN"
    blocking_unknowns: []
    residual_risks: []

  authority_effect:
    admitted_authority_ceiling: ""
    restricted_capabilities: []
    required_external_attestations: []

  admitted_stage: "SELF_POSITIONING_REQUIRED | P0 | P1 | P2 | P3 | P4 | P5"
  admission_basis_refs: []
  last_verified_at: ""
  revalidation_triggers: []
```

## Admission logic

1. The participant may declare what it believes it can do. Record these as E0 claims.
2. Convert material claims into evidence requirements and bounded tests.
3. Prefer machine-observed state, test artifacts, environmental traces, and independent verification for consequential properties.
4. Evaluate each stage gate against evidence applicable to the current subject/host/instance/configuration/epoch/scope.
5. Admit only the highest stage whose gate is evidenced.
6. Keep unsupported requirements `UNKNOWN` or `NOT_EVIDENCED`; do not infer them from model sophistication or brand reputation.
7. Stage admission does not automatically grant every possible authority. Authority remains scoped by consequence, profile, control availability, and evidence.
8. Reposition when evidence expires, the host/model/prompt/configuration changes materially, or failures contradict prior evidence.

## Important interpretation

Developmental stage measures maturity of the **agent/host/system operating arrangement**, not raw model intelligence.

A hallucination-prone model may participate in a mature host if external validators, recovery, evidence collection, and authority boundaries compensate for weak self-attestation. Conversely, a highly capable model cannot skip P0 or self-promote to P3/P4 by confidence or reputation.

This enables ecological specialization:

- weak self-attestation -> require external completion evidence;
- strong ideation -> retain broad cognitive agency;
- weak recovery judgment -> restrict recovery-lead authority;
- demonstrated reliable tool execution -> expand that specific operating envelope;
- repeated failures -> contract affected authority/capability claims without erasing unrelated agency.

## Anti-patterns

Do not allow:

- `model says it can do X -> X is qualified`;
- `model is famous/expensive -> skip P0`;
- `one successful test -> permanent universal capability`;
- `multiple self-reports -> independent evidence`;
- `stage level -> global trust score`;
- `stage advancement -> irreversible trust increase without revalidation`.

## Candidate maxims — implementation clarification only

- `Self-assessment proposes; evidence admits.`
- `Reputation is not a stage gate.`
- `A stage is an evidenced operating state, not a personality label.`
- `Model intelligence does not substitute for host maturity.`
- `Can produce != can certify.`

## Falsification pressure

Test whether this pack:

- over-burdens low-risk LITE hosts;
- mistakes correlated evidence for independence;
- fails to notice stale evidence after model/prompt/config changes;
- permits a participant to manufacture its own evidence;
- collapses multidimensional capability into one stage label;
- prevents a weak-but-useful model from retaining viable low-consequence agency;
- allows stage admission without proving the relevant failure/recovery properties.

No ENA v0.2.11 Mainline change is proposed by this prototype.
