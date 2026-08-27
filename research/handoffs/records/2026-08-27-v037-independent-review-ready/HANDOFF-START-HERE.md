# ENA Project Handoff — Start Here

Status: `CURRENT_SESSION_HANDOFF_RECORD / INDEPENDENT_REVIEW_READY / NOT_PROJECT_AUTHORITY`

Handoff ID: `2026-08-27-v037-independent-review-ready`

Before using this record as a **project-manager successor**, read the canonical handoff framework:

1. `research/handoffs/HANDOFF-PROTOCOL.md`
2. `research/handoffs/REQUIRED-TAKEOVER-CONTEXT.yaml`
3. `research/handoffs/PROJECT-MANAGEMENT-DISCIPLINE.md`

Then inherit the project methodology listed by `REQUIRED-TAKEOVER-CONTEXT.yaml`.

A fresh independent validator is a different role. Do **not** send that validator through this full project-manager takeover path before Phase A. Use the blind Phase-A entry named below.

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

The required author-harness `1080 -> 188` anti-ablation audit completed with:

`PASS_WITH_TREE_EXTERNAL_COVERAGE_REPAIR`

The audit found both legitimate phase-aware oracle repair and accidental loss of materially distinct attack shapes. Lost shapes were restored **outside** frozen candidate bytes. Candidate bytes did not change.

A draft review surface exists:

`PR #115 — DO NOT MERGE: v0.3.7 candidate.0 fresh independent falsification`

A subsequent project-method review found another validation-process issue: the original PR/validator handoff exposed a detailed author-generated attack map before Phase A, which could prime a nominally fresh validator's search space.

This is a validation-method defect, not a candidate-byte defect.

## Exact next action

`FRESH_INDEPENDENT_FALSIFICATION_PHASE_A_VIA_BLIND_ENTRY`

Fresh validator entrypoint:

`collaboration/reconciliation/2026-08-27-v037-candidate0-blind-phase-a-entry.md`

The fresh validator must inspect the exact frozen candidate bytes and independently grow a claim/attack/failure space **before** consulting author-side attack maps, expected outcomes, validation oracles, reconciliation narratives, or the detailed validator handoff.

Phase A must be durably persisted/sealed first.

Only after that seal should Phase B use:

`collaboration/reconciliation/2026-08-27-v037-candidate0-independent-falsification-handoff.md`

and compare the independent findings with author harnesses, pre-freeze evidence, reference selftests, language fixtures, and anti-ablation evidence.

## Role boundary

```text
PROJECT_MANAGER_TAKEOVER
-> full state + method + governance + decision lineage

FRESH_VALIDATOR_PHASE_A
-> exact target + freshness boundary + minimal-prime task
```

A reviewer already exposed to author oracle construction or the detailed author attack map may still contribute project management, Phase B analysis, oracle auditing, or reconciliation, but must not claim `FRESH_INDEPENDENT_PHASE_A`.

## Do not do these things

- do not modify `releases/current/`;
- do not call v0.3.7 Current;
- do not edit frozen candidate.0 bytes in place;
- do not let author oracles/attack taxonomy precede fresh Phase A;
- do not treat the anti-ablation audit as independent validation;
- do not merge PR #115 as a release/promotion action;
- do not create candidate.1 unless a material candidate-byte correction is required;
- do not collapse unproven HOW/failure/Host/evidence variation for narrative neatness.

## Project-manager takeover read order

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
14. exact freeze/audit/review records required by the next project-management action

Before any write, reverify live branch heads and exact frozen identity.

## Expected first project-manager takeover statement

A correct successor should be able to state, from persisted sources:

```text
Current = v0.3.6
candidate.0 = frozen, not Current
anti-ablation audit = complete with tree-external coverage repair
fresh independent validation = pending Phase A
review surface = PR #115 / DO NOT MERGE
fresh validator entry = blind Phase-A entry, not full project-manager handoff
Phase A must be sealed before detailed author Phase-B context opens
project state + project method + handoff protocol are mandatory for project-manager takeover
```
