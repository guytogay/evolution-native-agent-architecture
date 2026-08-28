# ENA Research — Start Here

Status: `ACTIVE_RESEARCH_BOOTSTRAP / HOT_ENTRYPOINT / NON_NORMATIVE / NOT_RELEASE_AUTHORITY`

This file is the fast-moving bootstrap inside the active research integration branch.

The canonical project/control plane lives on `main`. A successor discovers the active branch from `main`, not the other way around.

## Required project-manager continuation order

Before substantive ENA project-management/research work:

1. start from repository `main` and read `PROJECT-HUB.md`;
2. verify Current from `releases/current/CURRENT-BASELINE.yaml`;
3. read `research/handoffs/CURRENT-HANDOFF.yaml`;
4. read the handoff framework:
   - `research/handoffs/HANDOFF-PROTOCOL.md`;
   - `research/handoffs/REQUIRED-TAKEOVER-CONTEXT.yaml`;
   - `research/handoffs/PROJECT-MANAGEMENT-DISCIPLINE.md`;
5. read the current handoff record under `research/handoffs/records/` named by the pointer;
6. read required project methodology under `research/methodology/`, especially:
   - `ENA-RESEARCH-DISCIPLINE.md`;
   - `CONVERGENCE-DIVERGENCE-DISCIPLINE.md`;
   - `PROJECT-STATE-ALIGNMENT-GATE.md`;
   - `INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md` while independent validation is active;
   - `INDEPENDENT-VALIDATION-CAPSULE-CARRIER.md` when repository navigation is not blind-safe;
7. read `research/ACTIVE-RESEARCH.yaml` and verify the active research branch;
8. if canonical/live surfaces disagree, run the alignment gate before substantive work;
9. read `research/plans/PROGRESS.yaml` and the master plan;
10. reverify live branch/candidate heads before writing;
11. retrieve deeper Issues/prototypes/evidence only when the next project-management action requires them.

```text
PROJECT_STATE_INHERITANCE WITHOUT METHOD_INHERITANCE = INCOMPLETE_TAKEOVER
HANDOFF_RECORD != PROJECT_AUTHORITY
BRANCH_HEAD != FROZEN_IDENTITY
```

A new project-manager session should not ask the user to reconstruct already-persisted background.

A **fresh independent validator is not a project-manager successor**. Do not send that validator through the full continuation route above before A-S.

## Current project posture

Current remains:

```text
v0.3.6 / CURRENT / FIELD_VALIDATION
```

Next release line: `v0.3.7`.

Frozen candidate lineage now culminates in:

```text
candidate.3 = b7e88d7adb70396bd671ca97066daf2c120e0adc / e3a9a20d16cecd78df7f32f19fca56e21159e810
state = FROZEN / EXACT_PREFREEZE_PASS / TARGETED_POSTFREEZE_PASS / RELEASE_HARDENING_PASS
candidate succession = STOP
release preparation = SUPPORTED
Current changed = NO
```

Key evidence:

- exact pre-freeze run `33150269264` — SUCCESS;
- targeted post-freeze run `33150553992` — SUCCESS;
- release hardening run `33152201566` — SUCCESS;
- freeze record `collaboration/reconciliation/2026-08-28-v037-candidate3-freeze.md`;
- final release reconciliation `collaboration/reconciliation/2026-08-28-v037-candidate3-final-release-reconciliation.md`;
- release hardening reconciliation `collaboration/reconciliation/2026-08-28-v037-candidate3-release-hardening-reconciliation.md`.

The hardening audit found no material frozen candidate-byte defect requiring candidate.4. It confirmed adopter traversal, v0.3.6 compatibility/legacy relocation, release identity projection readiness, visible evidence boundaries, 38 stable Constitution IDs, 164/164 inherited zero-flip behavior, and 61/61 successor closure behavior.

`attack_cardinality = OPEN` and external/field truth remain evidence boundaries, not completeness claims.

## Immediate next action

`MAIN_VISIBLE_CHECKPOINT_THEN_CREATE_RELEASE_V0_3_7_AND_TRANSPLANT_FROZEN_CANDIDATE3`

Required sequence:

```text
MAIN-VISIBLE CANDIDATE.3 CHECKPOINT
-> CREATE release/v0.3.7 FROM EXACT MAIN
-> BYTE-FOR-BYTE TRANSPLANT frozen candidate.3 INTO releases/current
-> RECORD TRANSPLANT IDENTITY
-> RELEASE IDENTITY/PACKAGING TRANSFORM ONLY
-> EXACT RELEASE GATES + MAIN GATE + CODEQL + PACKAGE READBACK
-> EXPLICIT RELEASE AUTHORIZATION
-> MERGE / POST-MERGE CURRENT READBACK
```

Do not modify frozen candidate.3. Candidate.4 is permitted only if new evidence demonstrates a material defect in the frozen candidate bytes/semantics rather than in release packaging or field evidence.

## Core research direction

```text
WHAT / WHY
-> abstraction/compression may help

HOW
-> concretize / branch / recombine

FAILURE / ADVERSARIAL SPACE
-> expand while distinct failure shapes remain plausible

PROVEN REPRESENTATION DUPLICATION
-> may compress
```

```text
PROPERTY != ORGAN != HOST_BINDING != EVIDENCE != ADOPTION
ONE_WHAT_WHY -> 0..N_CONCRETE_HOW_BRANCHES
COMPRESS_REPRESENTATION != COMPRESS_POSSIBILITY_SPACE
```

## Record-first continuity

After material progress:

- update `research/plans/PROGRESS.yaml`;
- persist decision-material evidence/prototypes/reconciliation records;
- promote reusable handoff/project-management lessons to `research/handoffs/` root rather than trapping them in one record;
- reconcile ENA research-method changes to `research/methodology/`;
- update the current handoff record/pointer when succession context materially changes;
- align main-visible control surfaces after material routing/phase/candidate/release changes.

```text
LOCAL_ARTIFACT_IS_NOT_DURABLE_UNTIL_PERSISTED
```

## Final project-manager inheritance test

Before claiming successful takeover, a successor project manager should be able to state from persisted sources:

- Current = v0.3.6;
- active research branch = the branch named by `main`'s `ACTIVE-RESEARCH.yaml`;
- handoff protocol and project-management discipline = root files under `research/handoffs/`;
- current handoff record = the record named by `CURRENT-HANDOFF.yaml`;
- project methodology = mandatory context under `research/methodology/`;
- candidate.0 = frozen predecessor, NEEDS_REVISION, superseded;
- candidate.1 = exact frozen successor at `ae690346...` / `c0458e0...`;
- Issue #128 = invalidated self-primed intake with no Phase-A seal;
- Issue #131 = sealed A-S/A-P occurrence truth for candidate.1;
- A-S seal = `2e6b46ae...`; A-P final = `b970148f...`;
- candidate.1 = `NEEDS_REVISION`, immutable predecessor to candidate.2;
- candidate.2 = frozen at `bda470e0...` / `d5fefc8c...`; Issue #137 is interface-aborted history; active A-S carrier is clean-room commit `28dde50c...`;
- fresh validator entry remains blind semantic entry, not full project-manager context for any future independent intake;
- `releases/current/` remains untouched until governed release/promotion.

> **Do not merely inherit conclusions. Inherit project state, method, management discipline, open variation, and the exact next permitted action — while preserving the information boundary required by each role.**
