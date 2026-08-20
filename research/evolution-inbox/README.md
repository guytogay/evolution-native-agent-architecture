# ENA Evolution Inbox

Status: `RESEARCH / OPEN / NOT_CURRENT_BASELINE`

This directory holds durable ENA research directions, unresolved questions, counterexamples, historical candidate material, and evidence vectors that may inform future ENA versions.

The current adoption baseline is **ENA v0.3.1-BETA.1** at `releases/current/`.

Nothing in this Inbox is an additional runtime layer. Do not compose Inbox material with the Current baseline unless a later ENA release explicitly incorporates it.

The default rule remains:

> Do not convert a clever abstraction into a Constitution rule merely because it sounds universal.

Prefer historical adversarial replay, host evidence, cross-host recurrence, clarification, or the smallest mechanism that closes the observed problem.

## Research vectors still worth watching

### General Projection Semantics
Projection may legitimately truncate, summarize, deduplicate, rank, merge, omit, or decay information. The danger is semantic inflation.

> A projection may simplify representation, but must not silently acquire stronger truth semantics than its transformation supports.

Reference domains include history→knowledge, conversation→context, runtime→health, source artifacts→derived themes, and project metadata/indexes→current project state.

### Witness Survivability / Failure-Domain Independence
A witness/control that claims to detect or recover from a failure should survive, or remain independently observable across, the relevant failure domain.

> Witness survival domain must cover the failure domain of the claim it supports.

Current evidence is still insufficient for a separate Universal subsystem.

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

The current baseline already includes Triggered Material Obligation Closure and Influence Integrity as operational protections; this research area remains open for additional failure modes.

### Minimum Sufficient Intervention / Ecological Governance

Research whether ENA should explicitly prefer the **lowest intervention layer sufficient to protect viability and contain material externality**, rather than accumulating stronger controls by default.

Candidate ladder under test:

`OBSERVE -> EXPOSE_SIGNAL -> SHAPE_CONDITIONS -> LOCAL_COORDINATION -> SCOPED_HARD_BOUNDARY -> EMERGENCY_CONTAINMENT`

This is **not Current semantics**. The research must test both under-intervention and over-intervention failure modes, including bad equilibria, externality, monoculture, governance debt, and lost behavioral variety.

- Tracker: Issue #11
- Research note: `MINIMUM-SUFFICIENT-INTERVENTION.md`
- Experiment: `../experiments/MINIMUM-SUFFICIENT-INTERVENTION-EXPERIMENT.md`

### Network-Protocol Design Extraction

The first divergent network-protocol exploration has now been deliberately converged. Current actionable candidates are:

- circular provenance / self-confirming support paths;
- mixed-baseline transition safety;
- authority lease / expiry semantics.

OSPF/DNS/TCP/LLDP/CSMA-style analogies mostly reinforce existing ENA semantics and should not become new mechanisms merely because the analogy is attractive.

- Tracker: Issue #14
- Convergence note: `NETWORK-PROTOCOL-DESIGN-EXTRACTION.md`
- Experiments: `ENA-EXP-NET-001..003` under `../experiments/`

### Task-Scoped Cognitive Modes / Explicit Mode Transitions

Research whether temporary cognitive/operating modes should be task-scoped and bounded by explicit exit/transition conditions rather than treated as persistent Agent identity or authority.

Observed motivating case: a temporary Divergent Explorer mode was useful for network-protocol ideation but became inappropriate once the maintainer requested convergence and implementation.

`Agent identity != cognitive mode != role != authority`

- Tracker: Issue #15

### Release Identity ≠ Artifact Schema Identity
An ENA release version and an artifact schema-contract version may legitimately differ. Keep the relationship explicit when it matters.

### Migration Is Not Remediation Mandate
A migration/adoption task does not silently authorize adjacent remediation merely because remediation appears useful.

## Already incorporated into the Current Beta baseline

The following research families are now part of `v0.3.1-BETA.1` and should be field-tested as Current semantics rather than treated as separate overlays:

- Claim ↔ Evidence Support;
- Triggered Material Obligation Closure;
- Recovery State ≠ Historical Time / Monotonic History Across Restore;
- Capability / Model / Route Binding;
- Agency-Preserving Uncertainty;
- Viability Economics;
- Influence Integrity;
- open participation and field contribution;
- singular self-contained adoption-version discipline.

Their presence in the Beta means **field validation is requested**, not that they are universally proven or Mainline-promoted.

## Historical adversarial replay

Preferred loop:

`Historical incident -> concrete failure claim -> current ENA mapping -> false claim/value/friction -> cheapest decision-changing test -> contribution/reconciliation -> next release decision`

Current HAR checkpoint before Beta flattening: **13 replay cases, 0 new Constitution-level normative gaps**.

## Contribution rule

Do not append parallel-Agent advice directly into this file by default. Put one material contribution per artifact under `collaboration/inbox/` and reconcile separately.

Useful contribution types include:

`INCIDENT | NEAR_MISS | FRICTION | VALUE_OBSERVED | COUNTEREXAMPLE | PORTABILITY_FINDING | NEW_VARIATION | EVIDENCE_RESULT | RESEARCH_HYPOTHESIS | CRITIQUE`

> Knowledge is commons. Inquiry is open. Authority is scoped. Adoption is governed.
