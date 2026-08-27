# ENA Research

Status: `MAIN_VISIBLE_RESEARCH_ENTRYPOINT / PROJECT_CONTROL_PLANE / V0_3_7_CANDIDATE0_FROZEN`

This directory is the stable starting point for anyone asked to continue, inherit, review, or improve ENA research.

Do not discover active work by browsing branch names, old pull requests, candidate recency, or chat history.

## Start here

1. `../releases/current/CURRENT-BASELINE.yaml` — verify singular Current.
2. `handoffs/CURRENT-HANDOFF.yaml` — locate the latest intended project-manager/session handoff package.
3. `ACTIVE-RESEARCH.yaml` — canonical pointer to the one active research integration branch.
4. `methodology/README.md` — canonical research/handoff method index.
5. `methodology/SESSION-HANDOFF-DISCIPLINE.md` — how outgoing/incoming sessions preserve project continuity.
6. `methodology/CONVERGENCE-DIVERGENCE-DISCIPLINE.md` — when to compress vs preserve/grow variation.
7. `methodology/PROJECT-STATE-ALIGNMENT-GATE.md` — required after material transitions or state disagreement.
8. `plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md` — durable long-horizon plan.
9. Follow the active branch and read `RESEARCH-START-HERE.md` + `plans/PROGRESS.yaml`.
10. Retrieve `operational-architecture/`, `release-scope/`, prototypes, evidence, reconstruction, or external HOWs only when the current action requires them.

```text
main
|
+--> Current adoption
|     -> releases/current/
|
+--> current handoff
|     -> research/handoffs/CURRENT-HANDOFF.yaml
|
+--> research control
      -> research/ACTIVE-RESEARCH.yaml
           |
           v
      research/ena-reconstruction
           |
           +--> fast-moving progress / validation-method work
           +--> methodology lineage
           +--> operational-architecture / release-scope
           +--> prototypes / evidence / experiments / external HOWs

candidate/v0.3.7-candidate.0
-> release-lifecycle/review surface
-> branch head != frozen identity
```

## Current phase

Current adoption remains:

`v0.3.6 / CURRENT / FIELD_VALIDATION`

Next release line:

`v0.3.7`

Candidate.0 is frozen by exact external source/tree identity:

```text
candidate = v0.3.7-candidate.0
source = d0e793593184740d9732902e948afd48ed96ae2f
candidate subtree = cffbf76fe1448b020b637c78d1f7ae46e4c0115b
```

Author exact pre-freeze validation passed, but fresh independent semantic falsification is pending.

Current research phase:

`VALIDATION_ANTI_ABLATION_AUDIT_BEFORE_INDEPENDENT_FALSIFICATION`

Immediate next action:

**1080 -> 188 author-harness anti-ablation audit**, outside frozen candidate.0.

Why: a smaller/cleaner validation harness cannot be called epistemically better until materially distinct predecessor attack/failure shapes have explicit disposition.

## Research methodology

Canonical methodology lives under `research/methodology/`.

Important current disciplines include:

- explanatory coverage is not operational solution;
- WHAT/WHY may be compressed into a semantic trunk;
- concrete HOW branches remain plural when behavior differs or equivalence is unproven;
- failure/adversarial space should expand while distinct failure shapes remain plausible;
- `COMPRESS REPRESENTATION != COMPRESS POSSIBILITY SPACE`;
- recover variation before selecting among it;
- working taxonomies/counts are not ontology;
- experiments must pay epistemic rent;
- evidence is branch/Host/applicability scoped;
- NO_CHANGE, dormancy, simplification and evidence-backed retirement are valid outcomes;
- a concrete HOW says both how to use it and when it does not apply;
- missing pointer != missing organ;
- session handoff is a normal lifecycle and must be durable/standardized;
- after material transitions, align routing/plan/progress/handoff/live Git state before continuing.

## Operational Architecture

`research/operational-architecture/` provides the research navigation chain:

```text
problem/cue
-> CUE-INDEX
-> WHAT/WHY node
-> plural HOW branches
-> REFERENCE-POINTER-MATRIX
-> prototype / bounded procedure / Host pattern
-> action or honest residual
```

A release-local form of this architecture is bundled in frozen v0.3.7 candidate.0.

The library may be much larger than an Agent's active context. Hot routing should retrieve relevant branches rather than load everything.

## Release scope

`research/release-scope/` records why candidate.0 contains its current adopter guidance, optional references, tooling, language surface, and deferred branches.

Key distinctions:

```text
NO_NEW_CORE_RULES != NO_RELEASE_VALUE
LARGE_RESEARCH_TREE != SHIP_EVERYTHING
BUNDLED_REFERENCE != REQUIRED_RUNTIME_ORGAN
DEFERRED != RETIRED
```

## Handoff semantics

`research/handoffs/` stores historical/current session handoff packages.

Only `CURRENT-HANDOFF.yaml` identifies the latest intended handoff.

```text
HANDOFF_PACKAGE != PROJECT_AUTHORITY
HISTORICAL_HANDOFF_PRESERVED != HISTORICAL_HANDOFF_ACTIVE
```

The incoming session reads the handoff for speed, then verifies Current, live refs, frozen identity, methodology, Progress, and plan from canonical sources.

## Branch/PR semantics

```text
BRANCH_EXISTS != BRANCH_ACTIVE
OPEN_PR != ACTIVE_RESEARCH_AUTHORITY
CANDIDATE_BRANCH_HEAD != FROZEN_CANDIDATE_IDENTITY
RESEARCH_ARTIFACT_EXISTS != CURRENT
MAIN_FILE_EXISTS != ENA_CONSTITUTION
```

Historical PRs/branches are durable lineage/checkpoints. The main-visible active branch pointer remains continuation authority.

> **One active research integration surface; one current handoff pointer; many concrete HOW/failure branches may remain open inside the research tree.**
