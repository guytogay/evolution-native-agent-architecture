# ENA Research

Status: `MAIN_VISIBLE_RESEARCH_ENTRYPOINT / PROJECT_CONTROL_PLANE / V0_3_7_CANDIDATE0_FROZEN`

This directory is the stable starting point for anyone asked to continue, inherit, review, or improve ENA research.

Do not discover active work by browsing branch names, old pull requests, candidate recency, or chat history.

## Start here

1. `../releases/current/CURRENT-BASELINE.yaml` — verify singular Current.
2. `handoffs/CURRENT-HANDOFF.yaml` — current handoff record pointer + takeover contract.
3. `handoffs/HANDOFF-PROTOCOL.md` — canonical outgoing/incoming succession rules.
4. `handoffs/REQUIRED-TAKEOVER-CONTEXT.yaml` — mandatory takeover context.
5. `handoffs/PROJECT-MANAGEMENT-DISCIPLINE.md` — cross-session project-management rules.
6. Read the current record under `handoffs/records/` named by the pointer.
7. `methodology/README.md` — canonical ENA research-method index.
8. `ACTIVE-RESEARCH.yaml` — active research integration pointer.
9. `methodology/CONVERGENCE-DIVERGENCE-DISCIPLINE.md` — compression/growth/anti-ablation discipline.
10. `methodology/PROJECT-STATE-ALIGNMENT-GATE.md` — material-transition alignment.
11. `plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md` and `plans/PROGRESS.yaml`.
12. Retrieve Operational Architecture, release-scope, prototypes, evidence, reconstruction, or external HOWs only when the current action requires them.

```text
main
|
+--> Current adoption
|     -> releases/current/
|
+--> handoff framework
|     -> research/handoffs/
|          +--> CURRENT-HANDOFF.yaml
|          +--> HANDOFF-PROTOCOL.md
|          +--> REQUIRED-TAKEOVER-CONTEXT.yaml
|          +--> PROJECT-MANAGEMENT-DISCIPLINE.md
|          +--> records/<handoff-id>/
|
+--> ENA research methodology
|     -> research/methodology/
|
+--> active research control
      -> research/ACTIVE-RESEARCH.yaml
           -> research/ena-reconstruction

candidate/v0.3.7-candidate.0
-> release-lifecycle/review surface
-> branch head != frozen identity
```

## Succession distinction

```text
HANDOFF_FRAMEWORK != HANDOFF_RECORD
HANDOFF_RECORD != PROJECT_METHODOLOGY
PROJECT_STATE_INHERITANCE_WITHOUT_METHOD_INHERITANCE = INCOMPLETE_TAKEOVER
```

The handoff framework governs how responsibility is transferred and received.

A handoff record is one time-bounded succession occurrence.

`research/methodology/` governs how ENA research itself is performed.

All are relevant to takeover, but they are not the same authority layer.

## Current phase

Current adoption remains:

`v0.3.6 / CURRENT / FIELD_VALIDATION`

Next release line: `v0.3.7`.

Frozen candidate.0:

```text
candidate = v0.3.7-candidate.0
source = d0e793593184740d9732902e948afd48ed96ae2f
candidate subtree = cffbf76fe1448b020b637c78d1f7ae46e4c0115b
```

The `1080 -> 188` anti-ablation audit is complete with `PASS_WITH_TREE_EXTERNAL_COVERAGE_REPAIR`; candidate bytes did not change.

Fresh independent semantic falsification is pending.

Current phase:

`FRESH_INDEPENDENT_FALSIFICATION_PHASE_A`

Review surface:

`PR #115 / DO NOT MERGE`

A fresh validator must inspect exact frozen bytes and derive attacks before consulting author-side expected outcomes/oracles.

## Research methodology

Canonical ENA research methodology lives under `research/methodology/`.

Important disciplines include:

- explanatory coverage is not operational solution;
- WHAT/WHY may be compressed into a semantic trunk;
- concrete HOW branches remain plural when behavior differs or equivalence is unproven;
- failure/adversarial space grows while distinct failure shapes remain plausible;
- `COMPRESS REPRESENTATION != COMPRESS POSSIBILITY SPACE`;
- recover variation before selecting among it;
- working taxonomies/counts are not ontology;
- experiments must pay epistemic rent;
- evidence is branch/Host/applicability scoped;
- NO_CHANGE, dormancy, simplification and evidence-backed retirement are valid outcomes;
- a concrete HOW says both how to use it and when it does not apply;
- after material transitions, align routing/plan/progress/handoff/live Git state before continuing.

## Operational Architecture

`research/operational-architecture/` provides:

```text
problem/cue
-> CUE-INDEX
-> WHAT/WHY node
-> plural HOW branches
-> reference / procedure / Host pattern
-> action or honest residual
```

A release-local form is bundled in frozen v0.3.7 candidate.0.

## Release scope

`research/release-scope/` records candidate cargo selection and deferred branches.

```text
NO_NEW_CORE_RULES != NO_RELEASE_VALUE
LARGE_RESEARCH_TREE != SHIP_EVERYTHING
BUNDLED_REFERENCE != REQUIRED_RUNTIME_ORGAN
DEFERRED != RETIRED
```

## Handoff semantics

Reusable succession rules live at `research/handoffs/` root.

Time-bounded occurrences live under `research/handoffs/records/`.

Only `CURRENT-HANDOFF.yaml` identifies the intended current record.

```text
HANDOFF_RECORD != PROJECT_AUTHORITY
HISTORICAL_HANDOFF_PRESERVED != HISTORICAL_HANDOFF_ACTIVE
```

## Branch/PR semantics

```text
BRANCH_EXISTS != BRANCH_ACTIVE
OPEN_PR != ACTIVE_RESEARCH_AUTHORITY
CANDIDATE_BRANCH_HEAD != FROZEN_CANDIDATE_IDENTITY
RESEARCH_ARTIFACT_EXISTS != CURRENT
MAIN_FILE_EXISTS != ENA_CONSTITUTION
```

> **One active research integration surface; one current handoff pointer; many concrete HOW/failure branches may remain open inside the research tree.**
