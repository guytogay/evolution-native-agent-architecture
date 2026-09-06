# ENA Rapid Current Release Discipline

Status: `PROJECT_METHOD / MAIN_CONTROL_PLANE / IMMEDIATE_EFFECT_AFTER_MERGE`

Updated: 2026-09-06

## Why this exists

ENA is an evolutionary architecture. Its release process must not accidentally turn the current release into a protected monument.

The project previously over-coupled two different properties:

```text
IMMUTABLE_VERSION != IMMOBILE_CURRENT
```

A released version must remain immutable as occurrence truth. The `Current` pointer, however, should move whenever a better bounded successor has paid the amount of evidence appropriate to its actual change.

The objective is:

```text
FAST_SUCCESSION
+ EXACT_VERSION_IDENTITY
+ PROPORTIONAL_VALIDATION
+ CHEAP_ROLLBACK
+ FIELD_SELECTION
```

not maximum pre-release ceremony.

## Core rule

> **Preserve old releases; move Current quickly.**

`same version -> same effective content` remains true.

But:

```text
Current(v0.3.7) -> Current(v0.3.8) -> Current(v0.3.9)
```

may happen frequently. A new Current does not erase the predecessor; it supersedes it as the default adoption surface while preserving the predecessor as a rollback/history anchor.

## Release lanes

Validation intensity follows the material change, not the existence of a candidate branch.

### Lane R0 — Field patch / adoption-surface successor

Use when the successor does **not** change Constitution semantics or core contract semantics and is materially reversible through release rollback.

Typical examples:

- adopter entrypoint/quickstart improvements;
- stale or contradictory status narration repair;
- language-projection fidelity repair;
- routing / retrieval / HOW discoverability improvements that preserve existing semantics;
- validator/CI hardening;
- packaging and enforcement-visibility improvements;
- optional-reference presentation or non-semantic organization.

Required before Current admission:

1. unique successor version identity;
2. exact candidate bytes committed;
3. bounded change classification recorded;
4. relevant machine/regression gates PASS;
5. predecessor Current remains recoverable;
6. known residuals/evidence boundary explicit;
7. release projection/readback proves the intended Current bytes.

Fresh independent validation is **not a mandatory pre-release gate** for R0. It may run in parallel or after admission as field validation. A decision-changing post-release defect creates the next rapid successor rather than retroactively making the prior release disappear.

### Lane R1 — Operational behavior change

Use when a HOW/tool/policy changes decision behavior materially but does not rewrite the Constitution or the shared core contract floor.

Examples:

- new or changed executable decision policy;
- changed evolution helper semantics;
- new default operational mechanism;
- changed retry/recovery/selection behavior within an existing semantic property.

Required before Current admission:

1. R0 requirements;
2. targeted adversarial tests for the changed behavior;
3. explicit consequence/recovery assessment;
4. targeted independent or cross-context evidence **when it can plausibly change the admission decision**.

A full cleanroom/freeze/falsification cycle is not automatic. Use it only if independence is decision-material.

### Lane R2 — Core semantic / high-consequence change

Use when the successor changes the binding semantic floor or creates a high-consequence compatibility break.

Examples:

- Constitution ID/meaning change;
- core contract semantic change;
- authority/effect/recovery invariant change;
- breaking machine-contract/schema semantics with broad adopter consequence;
- meta-governance change that can silently redefine admission truth.

R2 normally requires the heavy lifecycle:

```text
candidate
-> author/adversarial validation
-> exact freeze
-> fresh independent falsification/validation
-> reconciliation
-> explicit release decision
```

A heavy gate must still pay epistemic rent; it is not ceremonial even in R2.

## Escalation rule

When classification is ambiguous, ask:

```text
Could this change silently alter a consequential decision that existing regression evidence would not expose?
```

- If no, prefer R0.
- If yes but the binding semantic floor is unchanged, use R1.
- If the semantic floor itself changes or compatibility blast radius is high, use R2.

Do not escalate merely because the file count is large. A full successor package copied from Current can contain many unchanged files while carrying a small semantic delta.

## Field-validation meaning

`FIELD_VALIDATION` means reality contact is part of selection, not an admission purgatory.

A FIELD_VALIDATION Current is allowed to advance before every longitudinal or cross-Host question is closed, provided:

- its claims stay bounded;
- rollback/successor paths exist;
- unresolved evidence is visible;
- no open question is falsely narrated as proof.

```text
OPEN_FIELD_QUESTION != RELEASE_BLOCKER
```

## Release latency as a governance cost

Release delay is itself an ENA cost.

For each blocker, ask:

```text
What exact failure could this gate catch?
Would that failure change the release decision?
Can a cheaper machine/targeted/field check catch it instead?
```

If the answer is no, remove or defer the gate.

This operationalizes ENA-CON-034 and ENA-CON-038:

```text
GOVERNANCE_MUST_CONVERGE
CONTROL_MUST_PAY_RENT
```

## Rapid successor rule

When Current has a decision-bearing defect:

```text
observe defect
-> record evidence
-> create smallest successor identity
-> repair
-> run lane-appropriate gates
-> move Current
-> preserve predecessor
-> continue field selection
```

Do not leave a known fix sitting in candidate state merely to complete unrelated research.

```text
UNRELATED_RESEARCH != RELEASE_DEPENDENCY
```

## v0.3.8 classification

The v0.3.8 adoption-surface successor created from Issue #201 is classified:

```text
LANE = R0_FIELD_PATCH_ADOPTION_SURFACE
CORE_CONSTITUTION_DELTA = NONE
CORE_CONTRACT_SEMANTIC_DELTA = NONE_DEMONSTRATED
PRIMARY_VALUE = ADOPTION_CONSISTENCY + LANGUAGE_FIDELITY + ENFORCEMENT_VISIBILITY + REGRESSION_HARDENING
ROLLBACK_ANCHOR = v0.3.7
```

Its existing Main Gate and CodeQL PASS results satisfy the machine-validation class required for R0. Full fresh cleanroom falsification is therefore no longer a pre-release requirement. Post-admission field evidence remains welcome and can trigger v0.3.9 rapidly if needed.

## Anti-stagnation checks

A candidate is suspect when:

- all required lane gates have passed but it remains unreleased for unrelated research;
- the team repeatedly says `Current remains unchanged` as if immobility were itself evidence of quality;
- release preparation costs more than the bounded change it protects;
- post-release defects are accumulated for a distant major release instead of cut into small successors;
- validation cardinality grows without a named decision it can change.

## Durable distinction

```text
RELEASE_IMMUTABILITY protects historical truth.
CURRENT_MOBILITY protects evolution.
```

ENA needs both.
