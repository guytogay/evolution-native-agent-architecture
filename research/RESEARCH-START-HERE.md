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

Frozen predecessor candidate.0:

```text
identity = v0.3.7-candidate.0
source   = d0e793593184740d9732902e948afd48ed96ae2f
subtree  = cffbf76fe1448b020b637c78d1f7ae46e4c0115b
verdict  = NEEDS_REVISION / SUPERSEDED_BY_CANDIDATE1
```

Frozen active successor candidate.1:

```text
identity = v0.3.7-candidate.1
source   = ae6903464133cb5bcf3cd8909ecae1215fe0b9ba
subtree  = c0458e0d7ea417b841cbf4c8bf6e64e4aff37319
exact pre-freeze run = 33055811978 / PASS
state    = FROZEN / NOT_CURRENT / NOT_RELEASED
```

```text
FROZEN != INDEPENDENTLY_RECONCILED != RELEASED != CURRENT
```

Candidate.1 frozen bytes must not be edited in place. A material candidate/package correction after freeze requires a successor candidate.

## Independent-validation method transition

The first candidate.1 post-freeze blind intake was Issue #128.

A genuinely fresh reviewer correctly stopped after discovering that a permitted candidate-local self-description file disclosed predecessor findings and candidate.1 repair history. No Phase-A report was sealed.

Therefore:

```text
CANDIDATE_LOCAL != AUTOMATICALLY_BLIND_SAFE
VALIDATION_INTERFACE_DEFECT != CANDIDATE_BYTE_DEFECT
```

Issue #128 is historical invalid-intake occurrence truth, not active review authority and not candidate acceptance/rejection evidence.

Canonical method:

`research/methodology/INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md`

Incident:

`research/methodology/incidents/2026-08-27-CANDIDATE-SELF-PRIMING-INCIDENT.md`

Reconciliation:

`collaboration/reconciliation/2026-08-27-v037-candidate1-blind-view-repair.md`

## Immediate next action

`CANDIDATE1_FRESH_A_S_A_P`

Active independent intake:

- Issue `#131 — Fresh independent A-S/A-P — v0.3.7 candidate.1`
- branch `validation/v037-c1-blind-semantic-primary`
- entry `collaboration/reconciliation/2026-08-27-v037-candidate1-blind-semantic-entry.md`
- view manifest `collaboration/reconciliation/2026-08-27-v037-candidate1-blind-semantic-view.yaml`

The validation branch is a mechanically bound **projection**, not a successor candidate and not release authority.

Sequence:

```text
A-S BLIND SEMANTIC FALSIFICATION
-> PERSIST A-S SEAL
-> A-P INDEPENDENT PACKAGE / SELF-DESCRIPTION / ORACLE AUDIT
-> PERSIST A-P REPORT
-> STOP
-> PROJECT-MANAGER PHASE B RECONCILIATION
```

Required independent outputs:

- A-S: `collaboration/reconciliation/2026-08-27-v037-candidate1-independent-a-s-primary.md`
- A-P: `collaboration/reconciliation/2026-08-27-v037-candidate1-independent-a-p-primary.md`

Before A-S seal, the reviewer must not receive project-manager handoff context, predecessor findings, repair narratives, author attack maps, expected fixtures, or candidate-local history/oracle surfaces withheld by the view manifest.

After A-S seal, A-P may inspect those withheld candidate-local surfaces from the exact frozen source. A-P remains independent but is not claimed to retain search-space blindness after history/oracles open.

After A-P, the fresh reviewer stops before Phase B.

```text
FULL_PACKAGE_INDEPENDENCE != FULL_PACKAGE_SEARCH_SPACE_BLINDNESS
ATTACK_CARDINALITY = OPEN
```

## Decision after A-S/A-P

The project manager first verifies:

- A-S seal commit;
- A-P report commit;
- candidate.1 frozen source/subtree unchanged;
- Current remains v0.3.6;
- the independent reviewer respected the declared information boundary.

Only then open author/project-manager evidence for Phase B reconciliation.

```text
material candidate-byte/package defect -> candidate.2 may be required
validation-interface defect alone      -> repair interface/method, not candidate identity
no material defect                     -> do not manufacture successor for closure
```

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
- Issue #131 = active fresh A-S/A-P intake;
- fresh validator entry = blind semantic entry, not the full project-manager takeover context;
- A-S must seal before A-P opens withheld candidate-local history/oracles;
- A-P stops before Phase B;
- `releases/current/` remains untouched until governed release/promotion.

> **Do not merely inherit conclusions. Inherit project state, method, management discipline, open variation, and the exact next permitted action — while preserving the information boundary required by each role.**
