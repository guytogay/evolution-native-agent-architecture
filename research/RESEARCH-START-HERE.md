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

Frozen candidate lineage:

```text
candidate.0 = d0e793593184740d9732902e948afd48ed96ae2f / cffbf76fe1448b020b637c78d1f7ae46e4c0115b / NEEDS_REVISION
candidate.1 = ae6903464133cb5bcf3cd8909ecae1215fe0b9ba / c0458e0d7ea417b841cbf4c8bf6e64e4aff37319 / NEEDS_REVISION
candidate.2 = bda470e0a6b170cec61225a905957a501454a2fe / d5fefc8c786d7e40b3e9a59211ee7045bccee5bf / FROZEN_NOT_CURRENT_NOT_RELEASED
```

Candidate.2 exact pre-freeze run `33095987843` passed. External freeze authority is recorded at:

`collaboration/reconciliation/2026-08-28-v037-candidate2-freeze.md`

Repair/exact reconciliation:

`collaboration/reconciliation/2026-08-28-v037-candidate2-successor-repair-reconciliation.md`

Post-freeze independence decision:

`collaboration/reconciliation/2026-08-28-v037-candidate2-post-freeze-independence-decision.md`

Decision:

`FRESH_BLIND_SUCCESSOR_REVIEW_WARRANTED / ONE_FINAL_SEARCH_SPACE_INDEPENDENCE_CYCLE`

This is not a ritual completeness claim. It is justified because candidate.1 fresh review found author-missed defects and candidate.2's author-side nearby probe then found additional homologous decision-changing gaps after the known repairs.

The current project-manager session is **not eligible** to perform fresh candidate.2 A-S because it has material exposure to predecessor findings, candidate.2 repairs, probes, and exact regression expectations.

## Immediate next action

`GET_GENUINELY_FRESH_REVIEWER_TO_RUN_CANDIDATE2_A_S`

Fresh intake is ready:

- Issue `#137 — Fresh independent A-S/A-P — v0.3.7 candidate.2`
- validation branch `validation/v037-c2-blind-semantic-primary`
- neutral entry `collaboration/reconciliation/2026-08-28-v037-candidate2-blind-semantic-entry.md`
- blind view `collaboration/reconciliation/2026-08-28-v037-candidate2-blind-semantic-view.yaml`
- view audit `collaboration/reconciliation/2026-08-28-v037-candidate2-blind-view-preparation.md`

The source-to-view audit found 31 declared A-S removals plus the two intake files and **zero retained candidate-byte modifications**. The view is a projection, not a new candidate.

Required sequence:

```text
FRESH REVIEWER
-> A-S ON DECLARED BLIND VIEW
-> PERSIST / SEAL A-S
-> A-P OPENS WITHHELD CANDIDATE-LOCAL HISTORY / ORACLES FROM EXACT FROZEN SOURCE
-> PERSIST A-P
-> STOP FRESH REVIEWER
-> PROJECT-MANAGER PHASE B
```

Before A-S seal, do not send the fresh reviewer through the project-manager handoff, predecessor findings, candidate.2 repair narratives, author attack maps, expected fixtures, or candidate-local history/oracle surfaces declared withheld by the view manifest. The current project-manager session is not eligible to perform fresh candidate.2 A-S.

Candidate.2 is frozen. Any material candidate-byte correction after this point requires candidate.3; do not edit candidate.2 in place.

```text
FROZEN != INDEPENDENTLY_RECONCILED != RELEASED != CURRENT
ATTACK_CARDINALITY = OPEN
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
- Issue #131 = sealed A-S/A-P occurrence truth for candidate.1;
- A-S seal = `2e6b46ae...`; A-P final = `b970148f...`;
- candidate.1 = `NEEDS_REVISION`, immutable predecessor to candidate.2;
- candidate.2 = frozen at `bda470e0...` / `d5fefc8c...`, with fresh A-S intake Issue #137 ready on `validation/v037-c2-blind-semantic-primary`;
- fresh validator entry remains blind semantic entry, not full project-manager context for any future independent intake;
- `releases/current/` remains untouched until governed release/promotion.

> **Do not merely inherit conclusions. Inherit project state, method, management discipline, open variation, and the exact next permitted action — while preserving the information boundary required by each role.**
