# ENA Research

Status: `MAIN_VISIBLE_RESEARCH_ENTRYPOINT / PROJECT_CONTROL_PLANE`

This directory is the stable starting point for anyone asked to **continue, inherit, review, or improve ENA research**.

Do not discover the active research workspace by browsing branch names or old pull requests.

## Start here

1. `ACTIVE-RESEARCH.yaml` — canonical pointer to the one active research integration **branch**.
2. `methodology/README.md` — how ENA research must be conducted before selecting work.
3. `methodology/PROJECT-STATE-ALIGNMENT-GATE.md` — how to realign project state after material transitions before substantive work resumes.
4. `BRANCH-GOVERNANCE.md` — branch naming/lifecycle/closure rules.
5. `BRANCH-INVENTORY.yaml` — current live branch classification plus durable cleanup lineage.
6. `plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md` — durable long-horizon project plan.
7. Follow `ACTIVE-RESEARCH.yaml` to the active branch, then read its `research/RESEARCH-START-HERE.md` and `research/plans/PROGRESS.yaml` for fast-moving execution state.
8. Discover an open PR by active head branch only when review/integration context is needed.

```text
MAIN PROJECT CONTROL PLANE
        |
        +--> Current adoption -> releases/current/
        |
        +--> Research control -> research/ACTIVE-RESEARCH.yaml
                                  |
                                  v
                        research/ena-reconstruction
                                  |
                     +------------+------------+
                     |            |            |
                 prototypes    evidence    experiments / HOWs
```

Observed live long-lived topology after the 2026-08-26 cleanup:

```text
main
research/ena-reconstruction
```

Historical branch names remain lineage only when their refs have been deleted.

## Separation of concerns

`main` carries the stable project control plane and Current adoption baseline.

The active research integration branch carries fast-moving reconstruction, prototypes, external-HOW harvesting, experiments, evidence, and execution progress.

Temporary work branches may exist when isolation is genuinely useful, but they do not become continuation authority.

```text
BRANCH_EXISTS != BRANCH_ACTIVE
OPEN_PR != ACTIVE_BRANCH_AUTHORITY
RESEARCH_ARTIFACT_EXISTS != CURRENT
MAIN_FILE_EXISTS != ENA_CONSTITUTION
```

## Research methodology

ENA research has its own evolving methodology and must not rely on one Agent/session remembering it correctly.

The methodology is maintained under:

`research/methodology/`

Important current disciplines include:

- explanatory coverage is not operational solution;
- concrete organs must not be dissolved by parent abstractions;
- WHAT/WHY may form a compressed semantic trunk;
- HOW should concretize, branch, and remain plural where reality supports it;
- HOW cardinality and taxonomy are discovered rather than preallocated;
- experiments must pay epistemic rent;
- arbitrary numbers do not become evidence by being numeric;
- evidence is applicability/branch/Host scoped;
- research can legitimately yield NO_CHANGE, dormancy, simplification, plurality, or retirement with lineage;
- methodology inheritance is successful only when it changes actual research behavior;
- after material project transitions, method/routing/plan/progress must be aligned before substantive research resumes.

## Project State Alignment Gate

A branch handoff, cleanup, checkpoint merge, directory move, material method change, plan change, or release-state change can leave individually reasonable files describing different generations of the project.

Use:

`research/methodology/PROJECT-STATE-ALIGNMENT-GATE.md`

```text
INDIVIDUAL_FILE_CORRECT != PROJECT_STATE_COHERENT
MATERIAL_TRANSITION -> ALIGN -> RESUME
```

The gate is transition-triggered, not a ritual after every minor commit.

## Active-work discoverability

The active branch can change over time. The path to discover it does not:

`research/ACTIVE-RESEARCH.yaml`

A successor session should therefore **not need a branch census** for ordinary continuation.

An open PR may or may not exist. PR identity is not continuation authority.

## Historical branches and PRs

Historical, frozen, superseded, merged, or deleted branches and prior PR generations are lineage, not navigation.

Use `BRANCH-INVENTORY.yaml` only when cleaning topology or investigating provenance. Retrieve PR #82/#101 when their checkpoint/handoff history is relevant, not as mandatory startup context.

> **One active research integration surface; many concrete HOW branches may grow inside the research tree.**
