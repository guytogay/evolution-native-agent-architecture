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
| HAR-009 | Sincere belief or an immediate successful attempt proves a stable fix | State, Time, Evidence Grade | `COVERED` | Belief Is Not Completion Evidence (already covered) |
| HAR-010 | A truthful local completion claim remains valid after silent temporal expansion | Time, State, Scope | `COVERED` | Evidence Applicability Boundary (interval support) |

## Boundary recurrence

### Provenance

Appears materially in HAR-001, HAR-002, HAR-005, HAR-008.

But these are not the same failure:

- HAR-001: provenance of the **cognitive context**;
- HAR-002: provenance/reference survival across **restore/history**;
- HAR-005: provenance and limitation of a **lossy projection**;
- HAR-008: provenance of **actor/authorship/experience** in durable self-memory.

Interpretation: provenance is a recurrent cross-subsystem requirement, but recurrence alone does not imply one new Universal rule because v0.2.11 already has broad provenance semantics.

### State / identity / applicability boundaries

Appears in HAR-004, HAR-006, HAR-009, HAR-010, with different outcomes:

- HAR-004 is already covered because ENA explicitly separates definition/trigger/execution/effect.
- HAR-006 remains a clarification pressure because evidence contracts do not first-class the observed runtime instance/configuration state/applicability interval.
- HAR-009 is already covered because belief/design confidence cannot outrun evidence maturity and operational verification.
- HAR-010 is already covered semantically, but independently supports making temporal applicability first-class in machine-readable contracts.

Interpretation: not all state-boundary failures need new semantics; the current strongest weakness is **machine legibility of evidence applicability**, not absence of a Universal principle.

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

### Evidence maturity / completion

HAR-009 provides a clean real incident where internal confidence and repeated local repair attempts were mistaken for stable operational success until later use contradicted them.

Interpretation: this strengthens existing Evidence Grade / Assertion Maturity / scoped completion semantics and therefore increases compression rather than rule count.

## Candidate pressure summary

| Candidate | Independent incident support | Current pressure |
|---|---:|---|
| Evidence Applicability Boundary | 2 direct cross-domain cases: runtime/config-state transfer (HAR-006) + temporal-interval expansion (HAR-010) | `CLARIFICATION + SCHEMA/TEMPLATE PROTOTYPE` |
| General Projection Semantics | 1 clean observed context-projection case; other examples are adjacent or design-only | `MORE_EVIDENCE_REQUIRED` |
| Distributed History Merge | 1 clean Git multi-writer case | `MORE_EVIDENCE_REQUIRED` |
| Autobiographical Provenance Integrity | 1 strong direct false-autobiography case | `CLARIFICATION / MORE_EVIDENCE` |
| Activation Witness | 1 strong case but already explicitly covered | `WORKED_EXAMPLE` |
| Belief Is Not Completion Evidence | 1 strong real case but already explicitly covered by evidence maturity semantics | `WORKED_EXAMPLE` |
| Effect-Generating Control Paths | 1 clean messaging/platform case; existing composition/effect-surface semantics cover much | `CLARIFICATION_PRESSURE / MORE_EVIDENCE` |
| Witness Survivability | design-level `/tmp` risk only; no observed failure yet | `NOT_YET_HAR_EVIDENCE` |
| Session Context Lineage | 1 real natural experiment; actual framing effect UNKNOWN | `COUNTERFACTUAL_EXPERIMENT_REQUIRED` |

## Strongest synthesis so far

The first ten cases do **not** support a general claim that ENA lacks many mechanisms.

They instead suggest three different maturity problems:

1. **Semantic compression is working** — CON-036, Activation semantics, History/Projection, provenance, Evidence Grade, and whole-effect-surface semantics explain multiple old failures without rule growth.
2. **Machine legibility can lag conceptual coverage** — Evidence Applicability is the clearest example: the prose has most concepts, while schema/template binding is weak for runtime instance, configuration state, and applicability interval.
3. **Elegant unification must wait for independent recurrence** — Projection, Distributed History Merge, Witness Survivability, and Autobiographical Provenance remain attractive but under-evidenced for normative promotion.

Current result:

`10 HAR cases → 0 NORMATIVE_GAP`

This is compatible with the desired quality direction:

> Historical Failure Coverage ↑ while Universal Semantic Complexity stays stable or decreases.

## Current next-step implication

The strongest candidate has now moved beyond pure discussion:

`Evidence Applicability Boundary → research-only schema/template prototype`

That prototype should now be attacked before any MAINLINE edit. If explicit applicability fields make HAR-006 and HAR-010 unambiguous without new normative semantics, the correct evolution layer is likely contract clarification rather than Constitution growth.
