# 8. Release and Canonical-Lineage Discipline — v0.3.8-candidate.0

Status: `CANDIDATE / R0_FIELD_PATCH_ADOPTION_SURFACE / NOT_CURRENT / NOT_RELEASED`.

Released Current is still `v0.3.7 / CURRENT / FIELD_VALIDATION` until this successor is promoted.

## Core distinction

A released version must be immutable as occurrence truth. The Current pointer must not therefore become immobile.

```text
IMMUTABLE_VERSION != IMMOBILE_CURRENT
```

One released version identifies one immutable effective-content state:

`same ena_version -> same effective content`

A material correction creates a new version identity. It does **not** require keeping an older Current in place after a bounded better successor is ready.

## Rapid Current succession

ENA prefers:

```text
observe defect/opportunity
-> create smallest useful successor
-> classify release risk
-> run proportional gates
-> move Current
-> preserve predecessor as rollback/history
-> continue field selection
```

not:

```text
observe fix
-> accumulate unrelated research/gates
-> protect old Current from succession
```

Release delay is itself governance friction and must pay rent.

## Release lanes

### R0 — Field patch / adoption surface

Use when Constitution semantics and core-contract semantics are unchanged and rollback to the predecessor release is practical.

Typical changes:

- adopter entrypoints / quickstarts;
- status-narration repair;
- language-projection fidelity;
- routing / retrieval / HOW discoverability that preserves inherited semantics;
- validator/CI hardening;
- packaging or enforcement-visibility improvements.

Required before Current admission:

1. unique successor identity;
2. exact candidate bytes committed;
3. bounded delta classification;
4. relevant machine/regression PASS;
5. recoverable predecessor release;
6. explicit evidence/residual boundary;
7. exact release projection/readback.

Fresh independent validation is **not a mandatory pre-release gate** for R0. It can occur after admission as field validation and may trigger a rapid successor.

### R1 — Operational behavior change

Use when a HOW/tool/policy materially changes decision behavior without changing the binding semantic floor.

Add targeted adversarial tests and independent/cross-context evidence when that evidence can plausibly change admission.

A full cleanroom/freeze/falsification cycle is not automatic.

### R2 — Core semantic / high-consequence change

Use for Constitution/core-contract semantic change, broad compatibility break, or high-consequence meta-governance change.

R2 normally uses:

```text
candidate
-> author/adversarial validation
-> exact freeze
-> fresh independent falsification/validation
-> reconciliation
-> explicit release decision
```

Even here, every gate must name the decision it can change.

## v0.3.8 classification

This successor is classified:

```text
LANE = R0_FIELD_PATCH_ADOPTION_SURFACE
CORE_CONSTITUTION_DELTA = NONE
CORE_CONTRACT_SEMANTIC_DELTA = NONE_DEMONSTRATED
ROLLBACK_ANCHOR = v0.3.7
```

Primary driver: Issue #201 plus adopter/product usability evidence.

Primary value:

- separate research lineage from adopter payload;
- provide product-first human and Agent adoption entrypoints;
- distinguish model guidance, machine guards, external controls and field-only claims;
- restore zh-CN hot-surface fidelity;
- repair concept-map retrieval/applicability;
- broaden semantic fixtures;
- make recurrence machine-detectable where possible.

The candidate Main Gate and CodeQL have passed. The candidate validator also binds inherited Constitution 01–04 and key machine paths to v0.3.7 bytes.

Therefore **generic fresh cleanroom falsification is not a prerequisite for v0.3.8 admission**. The release path should now be exact R0 packaging/readback/promotion, followed by field validation.

## Candidate / release identity

```text
candidate: v0.3.8-candidate.0
branch: candidate/v0.3.8-candidate.0
candidate root: releases/v0.3.8-candidate/
predecessor Current: v0.3.7
```

Candidate branch names do not create Current status. Current changes only through explicit release/promotion.

```text
Git main != ENA Current
candidate branch != released
CI PASS != external truth
```

## Canonical ENA evolution

Canonical change requires durable lineage sufficient for the actual lane:

- proposal/change identity;
- reviewable effective content;
- lane-appropriate evidence;
- explicit admission/release record;
- immutable version identity;
- recoverable/publicly inspectable history appropriate to the project.

Do not demand R2 evidence for an R0 change merely because the project historically used a heavy candidate lifecycle.

## Current mobility and rollback

Current must be singular at any instant, but it may move frequently.

```text
Current(v0.3.7) -> Current(v0.3.8) -> Current(v0.3.9)
```

The predecessor remains history/rollback; it is not silently rewritten.

If v0.3.8 field evidence finds a decision-bearing defect, prefer a small v0.3.9 successor over leaving a known defect in place while waiting for a distant major release.

## Source/distribution identity

A release must be built from identified committed source/effective-content bytes.

Release evidence may include:

- source commit/tree;
- exact file set;
- byte/hash parity;
- package digest;
- published/promoted readback.

Ordinary adopters need the minimum sufficient immutable effective-content identity; they do not need release-author ceremony.

## Language projections

Supported projections bind to the same release identity.

```text
literal wording parity != decision parity
structural parity != behavioral equivalence
```

Structural/fixture checks are release evidence; natural cross-language model behavior remains field evidence unless directly observed.

## Runtime/reference compatibility

Candidate.0 inherits the primary practical v2 path:

`tools/ena_evolve_v2.py`

and retains legacy v1.2 only under:

`tools/legacy/ena_evolve_v1_2.py`

Bundled optional references do not become normative Host implementations merely by packaging.

`canonical semantic property != bundled reference implementation != Host mechanism`

## Product-surface release condition

For this R0 successor, release review asks whether:

- human/Agent entrypoints describe one coherent state;
- adopters can identify what to load without reading research history;
- soft/model guidance is not narrated as hard enforcement;
- supported language projections preserve decision-bearing hot semantics;
- conformance fixtures cover the high-value claims made by the adoption surface;
- simplification did not erase applicability or predecessor-valid machine behavior.

These are already represented in the candidate-specific Main Gate validator and bounded release readback.

## Open research does not block this release

Metamemory Update Policy v1 and other field/longitudinal questions are separate research streams.

```text
UNRELATED_RESEARCH != RELEASE_DEPENDENCY
OPEN_FIELD_QUESTION != RELEASE_BLOCKER
```

## History and carriers

Preserve historical releases/candidates/evidence as occurrence truth without forcing ordinary adopters to reconstruct history to determine Current.

GitHub is the present carrier of the lineage, not the metaphysical source of validity.

> **Preserve old releases; move Current quickly.**
>
> **Release immutability protects truth; Current mobility protects evolution.**
