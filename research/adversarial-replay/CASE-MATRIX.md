# HAR Case × Boundary × Candidate Matrix

Status: `RESEARCH_SYNTHESIS / NOT_PROMOTED`

Baseline: `ENA v0.2.11 MAINLINE`

This matrix is a synthesis layer over the individual HAR records. It does not replace case evidence and does not itself create normative authority.

## Case matrix

| Case | Primary false claim | Main boundaries | Verdict | Candidate pressure |
|---|---|---|---|---|
| HAR-001 | Host/durable continuity sufficiently describes current cognitive context | Session Context, Provenance | `CLARIFICATION_GAP` | Session Context Lineage |
| HAR-002 | Successful restore implies complete canonical history | Recovery, Time, Provenance | `COVERED` | Recovery State ≠ Historical Time (already covered semantically) |
| HAR-003 | Append-only shared file implies one coherent canonical history | Concurrency, Composition, History | `CLARIFICATION_GAP` | Distributed History Merge |
| HAR-004 | Registered/ready hook implies operational activation | Activation, State | `COVERED` | Activation Witness (collapsed into existing semantics) |
| HAR-005 | Truncated context projection preserves complete source semantics | Projection, Provenance | `COVERED_BUT_AMBIGUOUS` | General Projection Semantics |
| HAR-006 | Valid observation from runtime A/state X supports runtime B/state Y | Subject, State, Instance, Epoch | `CLARIFICATION_GAP` | Evidence Applicability Boundary |
| HAR-007 | Suppression control reduces effect surface merely because primary output is handled | Composition, Secondary Effect | `COVERED_BUT_AMBIGUOUS` | Effect-Generating Control Paths |
| HAR-008 | Knowledge in my memory implies I authored/performed the underlying work | Provenance, Subject, Session Context | `CLARIFICATION_GAP` | Autobiographical Provenance Integrity |

## Boundary recurrence

### Provenance

Appears materially in HAR-001, HAR-002, HAR-005, HAR-008.

But these are not the same failure:

- HAR-001: provenance of the **cognitive context**;
- HAR-002: provenance/reference survival across **restore/history**;
- HAR-005: provenance and limitation of a **lossy projection**;
- HAR-008: provenance of **actor/authorship/experience** in durable self-memory.

Interpretation: provenance is a recurrent cross-subsystem requirement, but recurrence alone does not imply one new Universal rule because v0.2.11 already has broad provenance semantics.

### State / identity boundaries

Appears in HAR-004 and HAR-006, with different outcomes:

- HAR-004 is already covered because ENA explicitly separates definition/trigger/execution/effect.
- HAR-006 remains ambiguous because evidence contracts do not first-class the observed runtime instance/configuration state/applicability interval.

Interpretation: not all state-boundary failures need new semantics; machine-contract legibility matters.

### Composition

Appears in HAR-003 and HAR-007.

- HAR-003: locally truthful history branches do not automatically compose into one reconciled history.
- HAR-007: locally sensible suppression behavior does not automatically compose safely with downstream platform error behavior.

Both are strongly related to CON-036 (`Local Validity Does Not Imply Composed Validity`).

Interpretation: current evidence strengthens CON-036 as a high-compression abstraction rather than demanding a new composition Constitution.

### Projection

Only HAR-005 is currently a clean observed incident whose main failure is projection truth-semantic inflation.

HAR-002 includes derived knowledge projection but is primarily a restore/history incident. Historical memory-health scoring is only design-risk evidence, not an observed projection failure.

Interpretation: General Projection Semantics remains under-evidenced for normative promotion.

### Concurrency

HAR-003 is currently the only clean multi-writer canonical-history conflict case.

Interpretation: seek an independent non-Git multi-writer history/log/event case.

## Candidate pressure summary

| Candidate | Independent incident support | Current pressure |
|---|---:|---|
| Evidence Applicability Boundary | 1 strong direct case; related provenance cases exist but are structurally different | `CLARIFICATION + SCHEMA/TEMPLATE` |
| General Projection Semantics | 1 clean observed context-projection case; other examples are adjacent or design-only | `MORE_EVIDENCE_REQUIRED` |
| Distributed History Merge | 1 clean Git multi-writer case | `MORE_EVIDENCE_REQUIRED` |
| Autobiographical Provenance Integrity | 1 strong direct false-autobiography case | `CLARIFICATION / MORE_EVIDENCE` |
| Activation Witness | 1 strong case but already explicitly covered | `WORKED_EXAMPLE` |
| Effect-Generating Control Paths | 1 clean messaging/platform case; existing composition/effect-surface semantics cover much | `CLARIFICATION_PRESSURE / MORE_EVIDENCE` |
| Witness Survivability | design-level `/tmp` risk only; no observed failure yet | `NOT_YET_HAR_EVIDENCE` |
| Session Context Lineage | 1 real natural experiment; actual framing effect UNKNOWN | `COUNTERFACTUAL_EXPERIMENT_REQUIRED` |

## Strongest synthesis so far

The first eight cases do **not** support a general claim that ENA lacks many mechanisms.

They instead suggest three different maturity problems:

1. **Semantic compression is working** — CON-036, Activation semantics, History/Projection, provenance, and whole-effect-surface semantics explain multiple old failures without rule growth.
2. **Machine legibility can lag conceptual coverage** — Evidence Applicability is the clearest example: the prose has most concepts, while schema/template binding is weak.
3. **Elegant unification must wait for independent recurrence** — Projection, Distributed History Merge, and Witness Survivability remain attractive but under-evidenced.

Current result:

`8 HAR cases → 0 NORMATIVE_GAP`

This is compatible with the desired quality direction:

> Historical Failure Coverage ↑ while Universal Semantic Complexity stays stable or decreases.
