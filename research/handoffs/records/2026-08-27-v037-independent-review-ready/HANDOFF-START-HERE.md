# ENA Project Handoff — Start Here

Status: `CURRENT_SESSION_HANDOFF_RECORD / INDEPENDENT_REVIEW_READY / NOT_PROJECT_AUTHORITY`

Handoff ID: `2026-08-27-v037-independent-review-ready`

Before using this record, read the canonical handoff framework:

1. `research/handoffs/HANDOFF-PROTOCOL.md`
2. `research/handoffs/REQUIRED-TAKEOVER-CONTEXT.yaml`
3. `research/handoffs/PROJECT-MANAGEMENT-DISCIPLINE.md`

Then inherit the project methodology listed by `REQUIRED-TAKEOVER-CONTEXT.yaml`.

## Current project state

ENA Current remains:

```text
v0.3.6 / CURRENT / FIELD_VALIDATION
```

Current authority:

`releases/current/CURRENT-BASELINE.yaml`

Next release line:

`v0.3.7`

Frozen candidate:

```text
identity       = v0.3.7-candidate.0
frozen source  = d0e793593184740d9732902e948afd48ed96ae2f
frozen subtree = cffbf76fe1448b020b637c78d1f7ae46e4c0115b
subtree path   = releases/v0.3.7-candidate/
```

Candidate.0 is frozen, not Current, not released, and not yet independently semantically validated.

## What changed since the previous handoff record

The required author-harness `1080 -> 188` anti-ablation audit has completed.

Result:

`PASS_WITH_TREE_EXTERNAL_COVERAGE_REPAIR`

The audit found that the reduction mixed legitimate phase-aware oracle repair with accidental loss of several materially distinct attack shapes. Lost shapes were restored **outside** frozen candidate bytes.

Frozen candidate bytes did not change.

A draft review surface now exists:

`PR #115 — DO NOT MERGE: v0.3.7 candidate.0 fresh independent falsification`

PR #115 is a review surface only. It is not release or promotion authority.

## Exact next action

`FRESH_INDEPENDENT_FALSIFICATION_PHASE_A`

A fresh independent validator must inspect the exact frozen candidate bytes and derive attacks **before** consulting author-side expected outcomes/oracles.

Primary review target:

```text
source commit = d0e793593184740d9732902e948afd48ed96ae2f
subtree sha   = cffbf76fe1448b020b637c78d1f7ae46e4c0115b
review PR     = #115
```

Only after Phase A findings exist should Phase B compare them with author harnesses, pre-freeze evidence, reference selftests, language fixtures, and the anti-ablation audit.

## Do not do these things

- do not modify `releases/current/`;
- do not call v0.3.7 Current;
- do not edit frozen candidate.0 bytes in place;
- do not let author oracles precede fresh Phase A;
- do not treat the anti-ablation audit as independent validation;
- do not merge PR #115 as a release/promotion action;
- do not create candidate.1 unless a material candidate-byte correction is required;
- do not collapse unproven HOW/failure/Host/evidence variation for narrative neatness.

## Takeover read order

1. `PROJECT-HUB.md`
2. `releases/current/CURRENT-BASELINE.yaml`
3. `research/handoffs/CURRENT-HANDOFF.yaml`
4. `research/handoffs/HANDOFF-PROTOCOL.md`
5. `research/handoffs/REQUIRED-TAKEOVER-CONTEXT.yaml`
6. `research/handoffs/PROJECT-MANAGEMENT-DISCIPLINE.md`
7. required project methodology under `research/methodology/`
8. this record's `HANDOFF-MANIFEST.yaml` and `PROJECT-STATE.md`
9. `research/ACTIVE-RESEARCH.yaml`
10. `research/plans/PROGRESS.yaml`
11. `research/plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md`
12. `RECENT-THREE-ROUNDS.md`
13. `FILE-CATALOG.md`
14. exact freeze/audit/review records named by `PROJECT-STATE.md`

Before any write, reverify live branch heads and exact frozen identity.

## Expected first takeover statement

A correct successor should be able to state, from persisted sources:

```text
Current = v0.3.6
candidate.0 = frozen, not Current
anti-ablation audit = complete with tree-external coverage repair
fresh independent validation = pending Phase A
review surface = PR #115 / DO NOT MERGE
next action = fresh independent Phase A before author oracle comparison
project state + project method + handoff protocol are all mandatory inherited context
```
