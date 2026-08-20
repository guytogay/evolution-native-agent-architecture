# Historical Adversarial Replay

Status: `RESEARCH_INFRASTRUCTURE / NON_NORMATIVE`

Historical Adversarial Replay (HAR) uses real historical agent failures to attack the current ENA MAINLINE semantics.

The purpose is **not** to reward ENA for being able to explain an incident after the fact. The purpose is to test whether the current semantics would force an honest claim boundary before or during the failure.

## Core question

For each incident:

> What false protection, health, evidence, authority, completion, provenance, activation, or history claim became possible, and would current ENA v0.2.11 MAINLINE prevent or correctly qualify that claim?

## Pipeline

`Historical incident → observed facts → false claim → boundary crossed → current ENA mapping → expected ENA behavior → verdict`

Allowed primary verdicts:

- `COVERED` — current ENA semantics already make the false claim invalid without material clarification.
- `COVERED_BUT_AMBIGUOUS` — the intended semantics appear present, but wording/field boundaries can plausibly permit an incorrect interpretation.
- `HOST_SPECIFIC` — the failure is mainly an implementation defect, not a Universal semantic gap.
- `CLARIFICATION_GAP` — existing ENA concepts are sufficient in substance, but a portable clarification is needed.
- `NORMATIVE_GAP` — existing ENA cannot honestly express or block the failure class without a new normative semantic.
- `UNKNOWN` — evidence is insufficient.

## Evidence discipline

A replay case must distinguish:

- observed historical fact;
- inference;
- current ENA mapping;
- candidate abstraction;
- unresolved unknowns.

A clever abstraction is not evidence of a Universal gap.

## Current replay set

| Case | Theme | Verdict |
|---|---|---|
| HAR-001 | Session Context Lineage | `CLARIFICATION_GAP` |
| HAR-002 | DSH k-0083 restore/history gap | `COVERED` |
| HAR-003 | Distributed History Merge | `CLARIFICATION_GAP` |
| HAR-004 | Hook registered/ready but never fired | `COVERED` |
| HAR-005 | Context truncation / projection semantics | `COVERED_BUT_AMBIGUOUS` |
| HAR-006 | Evidence Applicability across gateway instances/states | `CLARIFICATION_GAP` |
| HAR-007 | Control-generated secondary effect path | `COVERED_BUT_AMBIGUOUS` |
| HAR-008 | Autobiographical Provenance Integrity | `CLARIFICATION_GAP` |
| HAR-009 | Belief/Immediate Confidence vs Stable Fix Evidence | `COVERED` |
| HAR-010 | Temporal Completion Scope | `COVERED` |
| HAR-011 | Triggered obligation not externalized after Drive persistence | `CLARIFICATION_GAP` |

**Current `NORMATIVE_GAP` count: 0.**

That is a positive result. HAR is increasing real-failure coverage while reducing pressure to grow the Universal rule set.

### Current interpretation

- `Activation Witness / Trigger Effect Evidence` collapses into existing activation semantics and is best retained as a worked example/reference case.
- the DSH k-0083 incident is already semantically covered by v0.2.11 History/Projection rules; remaining pressure is host implementation, restore reconciliation, and salience/application.
- `Evidence Applicability Boundary` remains the strongest clarification/schema-tightening candidate. It now has two independent real-domain forms: runtime instance/configuration-state transfer (`HAR-006`) and temporal-interval expansion (`HAR-010`).
- `HAR-009` strengthens existing Evidence Grade / Assertion Maturity / Completion semantics: sincere belief in a fix is not stable operational evidence.
- `HAR-011` exposes a different execution gap: a rule may exist in persistent project state while a conditionally triggered follow-up obligation never becomes first-class execution state. Only `Applied=NO` is directly observed; whether the rule was Retrieved or Salient at the decision window remains UNKNOWN. The current repair direction is `Triggered Obligation Externalization / Obligation Closure`, not a new Constitution rule.
- `General Projection Semantics` remains promising but is not yet justified as a Universal architecture.
- `Distributed History Merge Semantics` needs an independent non-Git multi-writer case before stronger promotion pressure is warranted.
- `Autobiographical Provenance Integrity` is supported by the Nyx false-autobiography incident, but needs independent evidence where provenance confusion materially changes responsibility, authority, trust, or consequence.
- `Effect-Generating Control Paths` is supported by the B2B Telegram echo-loop incident, but current CON-036/CON-037/CAP-058 already cover much of the structure; seek an independent non-messaging case before any wording change.
- `Witness Survivability / Failure-Domain Independence` remains design-risk evidence rather than a recovered incident.

## Active targeted work

- `results/EVIDENCE-APPLICABILITY-AUDIT-v0.2.11.md` — clarification + schema/template tightening candidate; no Constitution change justified.
- `../prototypes/evidence-applicability-envelope.schema.json` — research-only applicability envelope prototype.
- `../prototypes/triggered-obligation-state.schema.json` — research-only prototype for externalizing material conditional obligations after their trigger is observed.
- `../prototypes/examples/HAR-011-triggered-bridge-obligation.example.yaml` — HAR-011 mapping into the obligation-state prototype.
- `../experiments/SESSION-LINEAGE-COUNTERFACTUAL-PLAN.md` — clean-session comparison plan for three semantic judgments.
- `schema/case.schema.json` + structural validators + GitHub Actions workflow — research-record validation only. A validator PASS does not prove the research conclusion.

## Promotion discipline

HAR cases enter `research/` first. They do not change MAINLINE.

A future normative candidate should normally require more than one attractive incident, and should demonstrate that existing ENA semantics plus clarification cannot already cover the failure.

> Historical Failure Coverage ↑ while Universal Semantic Complexity stays stable or decreases.

Current release posture: **ENA v0.2.11 MAINLINE unchanged. No v0.2.12 has been opened.**
