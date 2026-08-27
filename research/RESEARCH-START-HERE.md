# ENA Research — Start Here

Status: `ACTIVE_RESEARCH_BOOTSTRAP / HOT_ENTRYPOINT / NON_NORMATIVE / NOT_RELEASE_AUTHORITY`

This file is the fast-moving bootstrap **inside the active research integration branch**.

The canonical project/research control plane lives on `main`. A successor session should discover this branch from `main`; it should not discover `main` from this branch.

```text
MAIN
-> PROJECT-HUB.md
-> CURRENT baseline
-> CURRENT-HANDOFF.yaml
-> ACTIVE-RESEARCH.yaml
-> canonical methodology
-> active branch
-> this file / PROGRESS.yaml
```

```text
BOOTSTRAP != COMPLETE_RESEARCH_STATE
HANDOFF != PROJECT_AUTHORITY
BRANCH_NAME != BRANCH_AUTHORITY
OPEN_PR != ACTIVE_BRANCH_AUTHORITY
```

## Required continuation order

Before substantive ENA continuation:

1. Start from repository `main` and read `PROJECT-HUB.md`.
2. Verify actual Current from `releases/current/CURRENT-BASELINE.yaml`.
3. Read `research/handoffs/CURRENT-HANDOFF.yaml` and the pointed handoff package.
4. Read `research/ACTIVE-RESEARCH.yaml` and verify that it still designates `research/ena-reconstruction` as the active research integration branch.
5. Read `research/methodology/README.md`, especially:
   - `SESSION-HANDOFF-DISCIPLINE.md`;
   - `CONVERGENCE-DIVERGENCE-DISCIPLINE.md`;
   - `PROJECT-STATE-ALIGNMENT-GATE.md`.
6. If live/canonical state disagrees with the handoff or a material transition occurred, run the alignment gate before substantive work.
7. On the active branch, read `research/plans/PROGRESS.yaml`.
8. Read `research/plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md` for long-horizon phase constraints.
9. Reverify live branch/candidate heads before writing.
10. Retrieve deeper Issues/prototypes/reconstruction/external HOW evidence only when the next action requires them.

A new session should not ask the user to reconstruct already-persisted project state.

## Current project posture

Current remains:

```text
v0.3.6 / CURRENT / FIELD_VALIDATION
```

Next release line:

`v0.3.7`

Candidate.0 is frozen:

```text
candidate = v0.3.7-candidate.0
frozen source = d0e793593184740d9732902e948afd48ed96ae2f
frozen candidate subtree = cffbf76fe1448b020b637c78d1f7ae46e4c0115b
```

Do not infer frozen identity from the current candidate branch head.

Author-side exact pre-freeze validation passed, but fresh independent semantic falsification has not occurred.

```text
FROZEN != INDEPENDENTLY_VALIDATED != RELEASED != CURRENT
```

## Immediate next action

Before creating the independent-falsification review PR, perform a **tree-external 1080 -> 188 author-harness anti-ablation audit**.

Why:

The user challenged an author claim that reducing an observed 1080 pass conditions to 188 structured pass conditions was an improvement. The project now requires proof that materially distinct predecessor attack/failure shapes were not silently lost.

Canonical guard:

`research/methodology/CONVERGENCE-DIVERGENCE-DISCIPLINE.md`

Audit target:

```text
old attack space
-> recover materially distinct failure shapes
-> map each shape to newer harness
-> explicit disposition
```

Do not optimize for reproducing the number 1080.

Optimize for recovering/preserving behaviorally distinct adversarial variation.

If only the validator/oracle is incomplete, repair validation **outside the frozen candidate subtree**.

If a recovered attack exposes a material frozen-candidate byte defect, candidate.0 remains frozen lineage and candidate.1 is created only as required by the repair.

After the audit, create a clearly labeled `DO NOT MERGE / INDEPENDENT FALSIFICATION` review PR bound to the exact frozen source/tree and use a fresh validator with Phase A independent inspection before Phase B comparison against author evidence.

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
- if methodology changes, reconcile it to `main/research/methodology/`;
- if handoff becomes necessary, follow `SESSION-HANDOFF-DISCIPLINE.md` and update `CURRENT-HANDOFF.yaml`;
- if project routing/phase/release state changes, align main-visible control surfaces before continuation.

```text
LOCAL_ARTIFACT_IS_NOT_DURABLE_UNTIL_PERSISTED
```

## Final inheritance test

Before claiming successful takeover, a successor should be able to state from persisted sources:

- Current = v0.3.6;
- active research branch = the branch named by main's `ACTIVE-RESEARCH.yaml`;
- current handoff package = the package named by `CURRENT-HANDOFF.yaml`;
- candidate.0 exact frozen source/tree;
- candidate.0 is frozen but not independently validated/released/Current;
- convergence/divergence discipline now governs test/harness compression;
- immediate next action is the 1080 -> 188 anti-ablation audit;
- `releases/current/` must remain untouched until governed release/promotion.

> **Do not merely inherit conclusions. Inherit project state, method, open variation, and the exact next permitted action.**
