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
   - `INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md` when independent validation is active;
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

A **fresh independent validator is not a project-manager successor**. Do not send that validator through the full continuation route above before Phase A.

## Current project posture

Current remains:

```text
v0.3.6 / CURRENT / FIELD_VALIDATION
```

Next release line: `v0.3.7`.

Frozen candidate:

```text
candidate identity = v0.3.7-candidate.0
frozen source      = d0e793593184740d9732902e948afd48ed96ae2f
frozen subtree     = cffbf76fe1448b020b637c78d1f7ae46e4c0115b
```

```text
FROZEN != INDEPENDENTLY_VALIDATED != RELEASED != CURRENT
```

## Completed validation-method transitions

The required `1080 -> 188` author-harness anti-ablation audit is complete.

Result:

`PASS_WITH_TREE_EXTERNAL_COVERAGE_REPAIR`

Audit record:

`collaboration/reconciliation/2026-08-27-v037-candidate0-author-harness-anti-ablation-audit.md`

Workflow run: `33035656311`.

The audit found both legitimate lifecycle-sensitive oracle repair and several materially distinct lost attack shapes. Lost shapes were restored outside frozen candidate.0; candidate bytes did not change.

The earlier narrative that 1080 -> 188 was simply “better” is therefore not accepted as a general conclusion.

A subsequent re-takeover review found a second method issue: the original detailed validator handoff/PR exposed an author-generated attack map before Phase A. That can prime a nominally fresh validator and preserve shared blind spots even without reusing expected verdicts.

Correction:

```text
PROJECT_MANAGER_TAKEOVER_CONTEXT
!=
FRESH_VALIDATOR_PRE_PHASE_A_CONTEXT
```

Canonical focused method:

`research/methodology/INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md`

## Immediate next action

`FRESH_INDEPENDENT_FALSIFICATION_PHASE_A_VIA_BLIND_ENTRY`

Review surface:

`PR #115 — DO NOT MERGE`

Fresh validator entrypoint:

`collaboration/reconciliation/2026-08-27-v037-candidate0-blind-phase-a-entry.md`

A **genuinely fresh independent validator** should receive that minimal-prime entry, inspect the exact frozen candidate subtree, independently derive material claims, attacks, legitimate controls, and unknowns, then persist/seal a Phase-A artifact.

Before that seal, do not preload the validator with the author's attack taxonomy, expected verdicts, detailed reconciliation narrative, or the original detailed validator handoff.

Only after Phase A is sealed should Phase B open:

`collaboration/reconciliation/2026-08-27-v037-candidate0-independent-falsification-handoff.md`

and compare the independent findings with author harnesses, exact pre-freeze evidence, reference selftests, language fixtures, anti-ablation evidence, and other decision-relevant lineage.

```text
INDEPENDENT_INSPECTION
-> PERSIST_PHASE_A
-> OPEN_PHASE_B_CONTEXT
-> RECONCILE
```

The Phase-A attack space remains open-cardinality. The absence of a predeclared attack list is intentional; it lets another observer grow a different tree before the trees are compared.

## Candidate succession rule

```text
research residual alone -> candidate.1 NOT required
material candidate-byte correction -> candidate.1 required
```

Candidate.0 remains frozen lineage either way.

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
- candidate.0 exact frozen source/tree;
- anti-ablation audit = complete, tree-external repair PASS;
- independent validation = pending fresh blind Phase A on PR #115;
- fresh validator entry = blind Phase-A entry, not the full project-manager takeover context;
- detailed author validator handoff = Phase B only after the Phase-A seal;
- `releases/current/` remains untouched until governed release/promotion.

> **Do not merely inherit conclusions. Inherit project state, method, management discipline, open variation, and the exact next permitted action — while preserving the information boundary required by each role.**
