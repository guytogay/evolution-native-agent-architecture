# ENA Research

Status: `MAIN_VISIBLE_RESEARCH_ENTRYPOINT / PROJECT_CONTROL_PLANE / RELEASE_SCOPE_READY`

This directory is the stable starting point for anyone asked to continue, inherit, review, or improve ENA research.

Do not discover active work by browsing branch names or old pull requests.

## Start here

1. `ACTIVE-RESEARCH.yaml` — canonical pointer to the one active research integration branch.
2. `methodology/README.md` — current research method.
3. `methodology/PROJECT-STATE-ALIGNMENT-GATE.md` — required after material transitions.
4. `plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md` — durable long-horizon plan.
5. Follow the active branch and read `RESEARCH-START-HERE.md` + `plans/PROGRESS.yaml`.
6. For practical architecture, read `operational-architecture/README.md`.
7. For current release selection, read `release-scope/README.md`.
8. `BRANCH-GOVERNANCE.md` and `BRANCH-INVENTORY.yaml` are for topology/cleanup, not ordinary continuation.

```text
main
|
+--> Current adoption
|     -> releases/current/
|
+--> research control
      -> research/ACTIVE-RESEARCH.yaml
           |
           v
      research/ena-reconstruction
           |
           +--> methodology / reconstruction lineage
           +--> operational-architecture/
           +--> release-scope/
           +--> prototypes / evidence / experiments / external HOWs
```

Observed intended long-lived topology:

```text
main
research/ena-reconstruction
```

`research/ena-reconstruction` is a stable integration name, not a promise that the project will remain forever in archaeology/reconstruction phase.

## Current phase

PR #109 integrated the anti-ablation recovery and first Operational Architecture assembly into `main` without changing `releases/current/`.

Operational Architecture has passed the first release-scope entry gate with open field residuals.

Current research phase:

`ACTIVE_RELEASE_SCOPE_RECONCILIATION`

Current adoption remains whatever `releases/current/CURRENT-BASELINE.yaml` says; at this transition it remains `v0.3.6 / CURRENT / FIELD_VALIDATION`.

The next version is not assigned until release scope stabilizes.

## Research methodology

Canonical methodology lives under `research/methodology/`.

Important current disciplines include:

- explanatory coverage is not operational solution;
- WHAT/WHY may be compressed into a semantic trunk;
- concrete HOW branches must remain plural when reality supports different mechanisms;
- recover variation before selecting among it;
- working taxonomies/counts are not ontology;
- experiments must pay epistemic rent;
- evidence is branch/Host/applicability scoped;
- NO_CHANGE, dormancy, simplification and evidence-backed retirement are valid outcomes;
- a concrete HOW should say both how to use it and when it does not apply;
- missing pointer != missing organ;
- after a material transition, align routing/plan/progress/live Git state before continuing.

## Operational Architecture

`research/operational-architecture/` provides the current research navigation chain:

```text
problem/cue
-> CUE-INDEX
-> WHAT/WHY node
-> plural HOW branches
-> REFERENCE-POINTER-MATRIX
-> prototype / bounded procedure / Host pattern
-> action or honest residual
```

This library may be much larger than an Agent's active context. Tiny Hot Kernel/Host-native routing should retrieve relevant branches rather than load everything.

## Release scope

`research/release-scope/` now asks what should actually be delivered to adopters.

Key distinction:

```text
NO_NEW_CORE_RULES != NO_RELEASE_VALUE
LARGE_RESEARCH_TREE != SHIP_EVERYTHING
```

Release reconciliation may select adopter guidance, optional reference organs, Host patterns, maintenance tooling, or practical navigation without expanding Core semantics.

## Branch/PR semantics

```text
BRANCH_EXISTS != BRANCH_ACTIVE
OPEN_PR != ACTIVE_RESEARCH_AUTHORITY
RESEARCH_ARTIFACT_EXISTS != CURRENT
MAIN_FILE_EXISTS != ENA_CONSTITUTION
```

Historical PRs #82, #101 and #109 are durable lineage/checkpoints. The main-visible branch pointer remains continuation authority.

> **One active research integration surface; many concrete HOW branches may grow inside the research tree.**
