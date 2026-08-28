# ENA Research

Status: `MAIN_VISIBLE_RESEARCH_ENTRYPOINT / PROJECT_CONTROL_PLANE / V0_3_7_RELEASE_PACKAGING`

This directory is the stable research/project-management entrypoint. Do not infer active work from branch recency, old PRs, candidate numbering, or chat history.

## Start here

1. verify Current at `../releases/current/CURRENT-BASELINE.yaml` on `main`;
2. read `handoffs/CURRENT-HANDOFF.yaml` plus the canonical handoff framework;
3. read the current handoff record named by that pointer;
4. read required methodology under `methodology/`;
5. read `ACTIVE-RESEARCH.yaml`;
6. run the Project State Alignment Gate if live/current surfaces disagree;
7. read `plans/PROGRESS.yaml` and the master plan;
8. retrieve deeper candidate/reconciliation/release evidence only when the current action requires it.

## Current phase — 2026-08-28

Current adoption remains:

`v0.3.6 / CURRENT / FIELD_VALIDATION`

Frozen final candidate:

```text
v0.3.7-candidate.3
source  = b7e88d7adb70396bd671ca97066daf2c120e0adc
subtree = e3a9a20d16cecd78df7f32f19fca56e21159e810
exact pre-freeze run      = 33150269264 PASS
targeted post-freeze run  = 33150553992 PASS
release hardening run     = 33152201566 PASS
candidate succession      = STOP
release preparation       = SUPPORTED
```

Release packaging has begun:

```text
main checkpoint            = 280a8b0f7629d5deb013a5257cb74759213e8080
release branch             = release/v0.3.7
byte-exact transplant head = 8e4e25a8ba1940560fc55d7528ad31ef89a7f135
transplanted tree          = e3a9a20d16cecd78df7f32f19fca56e21159e810
identity/status transform  = pending
```

The transplant deliberately retains candidate identity bytes. It is not Current and is not yet a release verdict.

## Immediate next action

After the current alignment checkpoint reaches `main`:

`RELEASE_IDENTITY_STATUS_PACKAGING_ON_RELEASE_V0_3_7`

Then run exact-head release gates, Main Gate, CodeQL/regressions, package parity/readback, and explicit release authorization before merge.

## Method boundaries

```text
WHAT / WHY -> may compress
HOW -> concretize / branch / recombine
FAILURE SPACE -> remain open while materially distinct shapes remain plausible
PROVEN REPRESENTATION DUPLICATION -> may compress
```

```text
COMPRESS REPRESENTATION != COMPRESS POSSIBILITY SPACE
PROPERTY != ORGAN != HOST_BINDING != EVIDENCE != ADOPTION
```

Fresh independent validation remains a different epistemic role from project-manager succession. A fresh A-S reviewer receives a physically isolated, priming-reduced review surface rather than this project-manager context.

## Reusable clean-room infrastructure

`guytogay/independent-validation-cleanroom` is reusable validation infrastructure across ENA stages and across different projects. Its contents are stage-scoped ephemeral review state; durable occurrence truth returns to each source project.

## Research architecture

- canonical methodology: `methodology/`;
- active integration branch: discovered from `ACTIVE-RESEARCH.yaml`;
- Operational Architecture: `operational-architecture/`;
- release scope: `release-scope/`;
- external HOW registry: `external-how/`;
- experiments/prototypes: `experiments/`, `prototypes/`;
- plans/progress: `plans/`;
- handoff framework: `handoffs/`;
- reconciliation/freeze/validation: `../collaboration/reconciliation/`.

> One active research integration surface, one singular Current, and open-cardinality concrete HOW/failure space.
