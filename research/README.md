# ENA Research

Status: `MAIN_VISIBLE_RESEARCH_ENTRYPOINT / PROJECT_CONTROL_PLANE / V0_3_7_CURRENT_FIELD_VALIDATION`

This directory is the stable research/project-management entrypoint. Do not infer active work from branch recency, old PRs, candidate numbering, or chat history.

## Start here

1. verify Current at `../releases/current/CURRENT-BASELINE.yaml` on `main`;
2. read `handoffs/CURRENT-HANDOFF.yaml` plus the canonical handoff framework;
3. read the current handoff record named by that pointer as occurrence history;
4. read required methodology under `methodology/`;
5. read `ACTIVE-RESEARCH.yaml`;
6. run the Project State Alignment Gate if live/current surfaces disagree;
7. read `plans/PROGRESS.yaml` and the master plan;
8. retrieve deeper candidate/reconciliation/release evidence only when the current action requires it.

## Current phase — 2026-08-28

```text
Current                         = v0.3.7 / CURRENT / FIELD_VALIDATION
Current tree                    = f33e73ed997c1b66a4572685ab5474182e136e97
package files                   = 118
package SHA-256                 = 40d4dde277d54ce8252e0402e32f900fa7ab4fb0aeaa638b898073d0f02f848c
release PR                      = #144 / MERGED
release merge commit            = 50a4bb06b98dc0dd719230f71ed1d47e42e1fad9
active field-validation issue   = #150
```

Frozen release-source lineage remains `v0.3.7-candidate.3` at source/tree `b7e88d7adb70396bd671ca97066daf2c120e0adc` / `e3a9a20d16cecd78df7f32f19fca56e21159e810`. Candidate succession is stopped; candidate.4 is not justified by current evidence. Attack cardinality remains open.

## Current research route

The release/promotion project has transitioned into field validation plus reopenable reconstruction:

- `#150`: v0.3.7 Operational Architecture field evidence on heterogeneous Hosts/models/languages;
- `#89`–`#94`: long-lived reconstruction workstreams;
- `#104`: archaeology / variation-recovery obligation.

These issues are not release defects merely because they remain open. Select the next bounded step only when it can change a decision, expose a mechanism/failure/Host dependency, or materially improve the architecture.

## Release-metadata erratum

The immutable v0.3.7 Current baseline contains one stale pre-promotion residual sentence that says v0.3.6 remains Current until explicit promotion. Promotion has occurred. Do not rewrite released v0.3.7 bytes in place; preserve package identity, document the erratum externally, and correct it under a future governed release identity.

## Branch hygiene

`research/ena-reconstruction` remains the sole research continuation branch named by `ACTIVE-RESEARCH.yaml`. Completed release/candidate/validation/tmp/integration/control-fix refs are lifecycle-complete cleanup candidates after durable lineage. The current connector lacks a true delete-ref action; branch cleanup is classified durably rather than simulated by ref movement.

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
EXPERIMENTS_MUST_PAY_EPISTEMIC_RENT
```

Fresh independent validation remains a different epistemic role from project-manager succession. A fresh A-S reviewer receives a physically isolated, priming-reduced review surface rather than this project-manager context.

## Reusable clean-room infrastructure

`guytogay/independent-validation-cleanroom` is reusable validation infrastructure across ENA stages and different projects. Its contents are stage-scoped ephemeral review state; durable occurrence truth returns to each source project.

## Research architecture

- canonical methodology: `methodology/`;
- active integration branch: discovered from `ACTIVE-RESEARCH.yaml`;
- Operational Architecture research: `operational-architecture/`;
- release scope: `release-scope/`;
- external HOW registry: `external-how/`;
- experiments/prototypes: `experiments/`, `prototypes/`;
- plans/progress: `plans/`;
- handoff framework: `handoffs/`;
- reconciliation/freeze/validation: `../collaboration/reconciliation/`.

> One active research integration surface, one singular Current, and open-cardinality concrete HOW/failure space.
