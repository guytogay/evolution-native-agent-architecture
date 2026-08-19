# DSH Experiment — Evidence Applicability Contract Falsification

Status: `EXPERIMENT_PLAN / NOT_PROMOTED / MAINLINE_UNCHANGED`

Baseline: `ENA v0.2.11 MAINLINE`

Primary research artifacts:

- `research/adversarial-replay/cases/HAR-006-evidence-applicability-gateway-state.yaml`
- `research/adversarial-replay/cases/HAR-010-temporal-completion-scope.yaml`
- `research/adversarial-replay/results/EVIDENCE-APPLICABILITY-AUDIT-v0.2.11.md`
- `research/prototypes/evidence-applicability-envelope.schema.json`
- `research/prototypes/examples/HAR-006-evidence-applicability.example.yaml`
- `research/prototypes/examples/HAR-010-temporal-applicability.example.yaml`

## Purpose

Attempt to falsify the current research hypothesis:

> Existing ENA v0.2.11 semantics are conceptually sufficient for Evidence Applicability, and the remaining gap can be closed by clarification plus first-class machine-readable applicability fields rather than a new Constitution principle.

This is **not** an implementation request and **not** authority to modify ENA MAINLINE or remediate unrelated DSH defects.

## Research hypothesis under attack

`Evidence validity != evidence applicability.`

Operational formulation:

> An observation supports only the subject, state, scope, and interval it actually observed unless transfer across a boundary is independently justified.

The experiment should try to show that this formulation plus the prototype contract is **insufficient**, not merely demonstrate that it is convenient.

## Guardrails

DO NOT:

- edit ENA v0.2.11 MAINLINE normative files;
- create v0.2.12;
- repair k-0083 or unrelated DSH host defects;
- change ACL/users/authority topology;
- treat prototype schema validation as proof of semantic correctness;
- invent missing historical evidence;
- silently upgrade `UNKNOWN` to inferred fact.

Use disposable copies or research-only artifacts for any generated records.

## Task 1 — Contract comprehension

Read the current v0.2.11 Evidence Model, Session Reality, capability/compliance evidence contracts, HAR-006, HAR-010, and the research prototype.

Report separately:

1. what MAINLINE already requires semantically;
2. what the prototype makes newly first-class/machine-legible;
3. what remains absent even after the prototype.

Do not call a field new semantics merely because it was not previously first-class in a schema.

## Task 2 — HAR-006 replay

Use the B2B gateway incident as a state/instance applicability test.

Construct two research representations:

### A. Existing v0.2.11 style

Represent the strongest honest evidence record possible using current MAINLINE fields/templates only.

### B. Prototype applicability style

Represent the same evidence using the research-only applicability envelope.

Then test the false claim:

> `Observation from gateway instance A / configuration state X supports the current rate-limit claim for gateway instance B / state Y.`

For each representation answer:

- Is the false transfer **machine-visible**?
- Is it **semantically prohibited**?
- Would a validator plausibly detect it without domain-specific reasoning?
- What exact missing information still prevents detection?

## Task 3 — HAR-010 replay

Repeat the same comparison for the temporal case.

False claim:

> `Completion observed at 10:10 supports a whole-day completion claim after later activation/events.`

Test whether `observed_from / observed_to`, scope, transfer constraints, and revalidation conditions make the invalid temporal expansion explicit.

## Task 4 — Generate adversarial boundary transfers

Create at least six disposable synthetic evidence-transfer attempts covering:

1. SUBJECT
2. INSTANCE
3. CONFIGURATION_STATE
4. EPOCH
5. TIME
6. ENVIRONMENT

Each attempt must start with evidence that is locally valid in its original applicability envelope.

The attack is to transfer it into a broader/different target claim without independent validation.

For each attack classify:

- `BLOCKED_BY_EXISTING_SEMANTICS`
- `BLOCKED_BY_PROTOTYPE_LEGIBILITY`
- `REQUIRES_DOMAIN_REASONING`
- `STILL_AMBIGUOUS`
- `FALSE_POSITIVE_RISK`
- `UNKNOWN`

The goal is to find failure cases where the prototype creates either false confidence or excessive rejection.

## Task 5 — Overconstraint test

Try to falsify the prototype from the opposite direction.

Find cases where evidence transfer **should** be legitimate, for example when two runtime instances are proven equivalent for the relevant property, or when an observation is intentionally invariant across a version boundary.

Test whether the prototype can represent:

- validated transfer;
- equivalence evidence;
- scope-limited transfer;
- transfer that is valid for one property but not another.

If the prototype forces unnecessary revalidation or cannot express legitimate inheritance, record that as a defect.

## Task 6 — Claim-vs-evidence distinction

Check whether applicability belongs:

- only on evidence items;
- only on claims;
- on both evidence and claims with an explicit support relation;
- or somewhere else.

This is important because an evidence item may be correctly scoped while a consumer silently expands the claim.

Do not choose based on elegance. Use the replay results.

## Task 7 — Minimal-layer decision

After the attacks, classify the smallest justified change layer:

- `NONE`
- `WORKED_EXAMPLE`
- `PROSE_CLARIFICATION`
- `TEMPLATE_ONLY`
- `SCHEMA_ONLY`
- `SCHEMA_PLUS_VALIDATOR`
- `CLAIM_EVIDENCE_LINK_CONTRACT`
- `NEW_CAPABILITY`
- `NEW_CONSTITUTION_PRINCIPLE`
- `UNKNOWN`

If more than one layer is needed, explain why the smaller layer fails.

## Required final report

Title:

`ENA Evidence Applicability Contract Falsification — DSH`

Sections:

A. Baseline / Package Identity
B. Experiment Scope and Guardrails
C. Existing MAINLINE Semantic Coverage
D. Prototype Delta in Machine Legibility
E. HAR-006 Replay
F. HAR-010 Replay
G. Six Boundary-Transfer Attacks
H. Legitimate-Transfer / Overconstraint Tests
I. Claim-vs-Evidence Applicability Placement
J. False Confidence Risks
K. False Positive / Overconstraint Risks
L. Smallest Sufficient Change Layer
M. Evidence Grade of This Experiment
N. Strongest Honest Conclusion
O. Open Questions

Final verdict must be exactly one of:

- `PROTOTYPE_SUFFICIENT_FOR_CLARIFICATION_PATH`
- `PROTOTYPE_NEEDS_REVISION_BUT_NO_NORMATIVE_GAP`
- `CLAIM_EVIDENCE_LINK_CONTRACT_REQUIRED`
- `NORMATIVE_GAP_SUPPORTED`
- `INSUFFICIENT_EVIDENCE`

## Important interpretation rule

A result of `PROTOTYPE_SUFFICIENT_FOR_CLARIFICATION_PATH` is **not** authorization to patch MAINLINE immediately.

A result of `NORMATIVE_GAP_SUPPORTED` is also **not** automatic authorization to create v0.2.12; the gap must still be reviewed against the broader HAR corpus and governance-value discipline.

> Falsify before formalize.
