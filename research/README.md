# ENA Research

Status: `MAIN_VISIBLE_RESEARCH_ENTRYPOINT / PROJECT_CONTROL_PLANE`

This directory is the stable starting point for anyone asked to **continue, inherit, review, or improve ENA research**.

Do not discover the active research workspace by browsing branch names.

## Start here

1. `ACTIVE-RESEARCH.yaml` — canonical pointer to the one active research integration branch and PR.
2. `methodology/README.md` — how ENA research must be conducted before selecting work.
3. `BRANCH-GOVERNANCE.md` — branch naming/lifecycle/closure rules.
4. `BRANCH-INVENTORY.yaml` — current branch classification and cleanup state.
5. `plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md` — durable long-horizon project plan.
6. Follow `ACTIVE-RESEARCH.yaml` to the active branch, then read its `research/RESEARCH-START-HERE.md` and `research/plans/PROGRESS.yaml` for fast-moving execution state.

```text
MAIN PROJECT CONTROL PLANE
        |
        +--> Current adoption -> releases/current/
        |
        +--> Research control -> research/ACTIVE-RESEARCH.yaml
                                  |
                                  v
                           one active research
                           integration branch
                                  |
                     +------------+------------+
                     |            |            |
                 prototypes    evidence    experiments / HOWs
```

## Separation of concerns

`main` carries the stable project control plane and Current adoption baseline.

The active research integration branch carries fast-moving reconstruction, prototypes, external-HOW harvesting, experiments, evidence, and execution progress.

Temporary work branches may exist when isolation is genuinely useful, but they do not become continuation authority.

```text
BRANCH_EXISTS != BRANCH_ACTIVE
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
- methodology inheritance is successful only when it changes actual research behavior.

## Active-work discoverability

The active branch can change over time. The path to discover it does not:

`research/ACTIVE-RESEARCH.yaml`

A successor session should therefore **not need a branch census** for ordinary continuation.

## Historical branches

Historical, frozen, superseded, or merged branches are lineage, not navigation.

Use `BRANCH-INVENTORY.yaml` only when cleaning topology or investigating provenance.

> **One active research integration surface; many concrete HOW branches may grow inside the research tree.**
