# ENA Evolution Inbox

Status: `RESEARCH / OPEN / NOT_CURRENT_BASELINE`

This directory holds durable ENA research directions, unresolved questions, counterexamples, historical candidate material, and evidence vectors that may inform future ENA versions.

The current adoption baseline is **ENA v0.3.2** at `releases/current/`.

Nothing in this Inbox is an additional runtime layer. Do not compose Inbox material with the Current baseline unless a later ENA release explicitly incorporates it.

The default rule remains:

> Do not convert a clever abstraction into a Constitution rule merely because it sounds universal.

Prefer historical adversarial replay, host evidence, cross-host recurrence, clarification, or the smallest mechanism that closes the observed problem.

## Research vectors still worth watching

### General Projection Semantics
Projection may legitimately truncate, summarize, deduplicate, rank, merge, omit, or decay information. The danger is semantic inflation.

> A projection may simplify representation, but must not silently acquire stronger truth semantics than its transformation supports.

### Witness Survivability / Failure-Domain Independence
A witness/control that claims to detect or recover from a failure should survive, or remain independently observable across, the relevant failure domain. v0.3.2 also clarifies that authority independence and failure-path congruence are separate concerns.

### Distributed History Merge Semantics
Append-only preservation does not make concurrent writers conflict-free.

> Append-only is a property of history preservation, not a concurrency protocol.

### Autobiographical Provenance Integrity
Knowing that an event happened does not mean the current Agent performed it.

`Observed Knowledge != Lived Experience != Authored Action != Owned Decision`

### Authority Separation Must Not Become Awareness Separation
Role/scope separation can degenerate into responsibility deflection.

> Separate decision authority, not the duty to notice.

### Session Context Lineage / Cognitive Context Provenance
Host continuity does not guarantee cognitive-context continuity.

> Context provenance, not context purity.

### Governance Salience
Relevant rules may be known and retrievable yet fail to dominate the final decision surface.

`Known != Retrieved != Salient != Applied`

### Minimum Sufficient Intervention / Ecological Governance

The named experimental ladder remains research:

`OBSERVE -> EXPOSE_SIGNAL -> SHAPE_CONDITIONS -> LOCAL_COORDINATION -> SCOPED_HARD_BOUNDARY -> EMERGENCY_CONTAINMENT`

v0.3.2 incorporates only the narrower reconciled property: prefer the lowest-cost intervention that honestly protects the required property, while allowing immediate escalation to a hard boundary when lower layers are insufficient. The fixed ladder is not Current normative machinery.

- Tracker: Issue #11
- Research note: `MINIMUM-SUFFICIENT-INTERVENTION.md`
- Experiment: `../experiments/MINIMUM-SUFFICIENT-INTERVENTION-EXPERIMENT.md`

### Network-Protocol Design Extraction

The 62-pass network-protocol exploration is now reconciled into v0.3.2 where it earned operational value:

- provenance independence/derivative-support handling -> existing Claim ↔ Evidence contract;
- authority lease/expiry/subject binding -> existing Capability/Route/Authority Binding contract;
- mixed-baseline transition safety -> Release Discipline;
- effect retry/concurrency/replay/cancel semantics -> Composition/Effect contract;
- narrow-waist principle -> shared architecture/release guidance.

Protocol-specific machinery and unresolved patterns remain research; Issue #14 is closed as the completed divergent research pass.

### Task-Scoped Cognitive Modes / Explicit Mode Transitions

v0.3.2 incorporates only the boundary:

`Agent identity != cognitive mode != role != authority`

A fixed universal cognitive-mode state machine remains research. Evidence is still insufficient to standardize exact mode names/transitions.

- Tracker: Issue #15

### Release Identity ≠ Artifact Schema Identity
An ENA release version and an artifact schema-contract version may legitimately differ. Keep the relationship explicit when it matters.

### Migration Is Not Remediation Mandate
A migration/adoption task does not silently authorize adjacent remediation merely because remediation appears useful.

## Incorporated into Current v0.3.2

The following families are Current semantics and should be field-tested rather than loaded as research overlays:

- Claim ↔ Evidence Support, including provenance-independence/closure refinements;
- Triggered Material Obligation Closure;
- Recovery State ≠ Historical Time / Monotonic History Across Restore;
- Capability / Model / Route / Authority Binding;
- effect identity, replay/retry/concurrency/cancel semantics;
- Agency-Preserving Uncertainty;
- Viability Economics, including control-composition/compensation cost;
- Influence Integrity;
- concrete LITE adoption projection;
- narrow-waist implementation-diversity discipline;
- immutable self-contained adoption-version/distribution parity discipline;
- open participation and field contribution.

Current status is `FIELD_VALIDATION / NOT_MAINLINE`; inclusion does not mean universal proof.

## Historical adversarial replay

Preferred loop:

`Historical incident -> concrete failure claim -> current ENA mapping -> false claim/value/friction -> cheapest decision-changing test -> contribution/reconciliation -> accumulate coherent change batch -> next flattened release`

Historical HAR checkpoint before v0.3.1 flattening: **13 replay cases, 0 new Constitution-level normative gaps**.

## Contribution rule

Do not append parallel-Agent advice directly into this file by default. Put one material contribution per artifact under `collaboration/inbox/` and reconcile separately.

Useful contribution types include:

`INCIDENT | NEAR_MISS | FRICTION | VALUE_OBSERVED | COUNTEREXAMPLE | PORTABILITY_FINDING | NEW_VARIATION | EVIDENCE_RESULT | RESEARCH_HYPOTHESIS | CRITIQUE`

> Knowledge is commons. Inquiry is open. Authority is scoped. Adoption is governed.
