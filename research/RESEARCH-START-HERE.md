# ENA Research — Start Here

Status: `ACTIVE_RESEARCH_BOOTSTRAP / HOT_ENTRYPOINT / NON_NORMATIVE / NOT_RELEASE_AUTHORITY`

This file is the fast-moving bootstrap inside the active research integration branch.

The canonical project/control plane lives on `main`. A successor discovers the active branch from `main`, not the other way around.

## Required continuation order

Before substantive ENA work:

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
7. read `research/ACTIVE-RESEARCH.yaml` and verify the active research branch;
8. if canonical/live surfaces disagree, run the alignment gate before substantive work;
9. read `research/plans/PROGRESS.yaml` and the master plan;
10. reverify live branch/candidate heads before writing;
11. retrieve deeper Issues/prototypes/evidence only when the next action requires them.

```text
PROJECT_STATE_INHERITANCE WITHOUT METHOD_INHERITANCE = INCOMPLETE_TAKEOVER
HANDOFF_RECORD != PROJECT_AUTHORITY
BRANCH_HEAD != FROZEN_IDENTITY
```

A new session should not ask the user to reconstruct already-persisted background.

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

## Completed validation-method transition

The required `1080 -> 188` author-harness anti-ablation audit is complete.

Result:

`PASS_WITH_TREE_EXTERNAL_COVERAGE_REPAIR`

Audit record:

`collaboration/reconciliation/2026-08-27-v037-candidate0-author-harness-anti-ablation-audit.md`

Workflow run: `33035656311`.

The audit found both legitimate lifecycle-sensitive oracle repair and several materially distinct lost attack shapes. Lost shapes were restored outside frozen candidate.0; candidate bytes did not change.

The earlier narrative that 1080 -> 188 was simply “better” is therefore not accepted as a general conclusion.

## Immediate next action

`FRESH_INDEPENDENT_FALSIFICATION_PHASE_A`

Review surface:

`PR #115 — DO NOT MERGE`

A **fresh independent validator** must inspect the exact frozen candidate bytes and independently derive attacks before consulting author-side expected outcomes/oracles.

Phase A should directly test, among other implementation-suggested risks:

- false claims and false confidence;
- false-BLOCK pressure;
- operational routing/reachability;
- composition seams;
- migration/source-selection laundering;
- language decision-semantic drift;
- hot/cold operational inhabitation;
- optional-reference burden;
- deferred machinery consequences.

The list is open-cardinality.

Only after Phase A findings exist should Phase B compare against author harnesses, exact pre-freeze evidence, reference selftests, language fixtures, and anti-ablation evidence.

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

## Final inheritance test

Before claiming successful takeover, a successor should be able to state from persisted sources:

- Current = v0.3.6;
- active research branch = the branch named by `main`'s `ACTIVE-RESEARCH.yaml`;
- handoff protocol and project-management discipline = root files under `research/handoffs/`;
- current handoff record = the record named by `CURRENT-HANDOFF.yaml`;
- project methodology = mandatory context under `research/methodology/`;
- candidate.0 exact frozen source/tree;
- anti-ablation audit = complete, tree-external repair PASS;
- independent validation = pending fresh Phase A on PR #115;
- `releases/current/` remains untouched until governed release/promotion.

> **Do not merely inherit conclusions. Inherit project state, method, management discipline, open variation, and the exact next permitted action.**
