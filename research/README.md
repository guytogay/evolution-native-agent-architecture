# ENA Research

Status: `MAIN_VISIBLE_RESEARCH_ENTRYPOINT / PROJECT_CONTROL_PLANE / V0_3_7_PREPROMOTION_RELEASE_READINESS`

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

```text
v0.3.6 / CURRENT / FIELD_VALIDATION
Current tree = 7dcbb3934883ffa6cc5292a662588cafc1533cff
```

Frozen final candidate:

```text
v0.3.7-candidate.3
source  = b7e88d7adb70396bd671ca97066daf2c120e0adc
subtree = e3a9a20d16cecd78df7f32f19fca56e21159e810
exact pre-freeze run      = 33150269264 PASS
targeted post-freeze run  = 33150553992 PASS
release hardening run     = 33152201566 PASS
candidate succession      = STOP
candidate.4               = not justified by current evidence
```

Release packaging and exact-head validation are complete on the prospective release surface:

```text
release branch                  = release/v0.3.7
release PR                      = #144 / OPEN DRAFT / NOT PROMOTED
byte-exact transplant head      = 8e4e25a8ba1940560fc55d7528ad31ef89a7f135
prospective Current tree        = f33e73ed997c1b66a4572685ab5474182e136e97
exact validated release head    = bcda18a28141f572688f9a1b15cfd820dea02f97
prospective Current file count  = 118
package SHA-256                 = 40d4dde277d54ce8252e0402e32f900fa7ab4fb0aeaa638b898073d0f02f848c
Exact Release Gate              = 33161514271 PASS
Current validate/package        = 33161516641 PASS
Main Gate                       = 33161516581 PASS
Selection Qualification         = 33161516591 PASS
research helper                 = 33161516586 PASS
CodeQL                          = 33161516568 PASS
```

The prospective release payload is not Current yet. Passing gates establish bounded release readiness; they do not mint promotion authority.

## Control-plane corrections made during release preparation

Selection Qualification exposed a stale research oracle that treated an uninstantiated evolution-record template as a valid instantiated record. The control was repaired in PR #145 and merged to `main` without changing candidate or release payload bytes. The repair was then synchronized into the release branch through PR #146.

The v0.3.7 Exact Release Gate was also hardened so **every push** to `release/v0.3.7` reruns the exact gate; a later release-head change can no longer silently rely on an older green run.

## Immediate next action

After this pre-promotion alignment checkpoint reaches `main`:

```text
sync aligned main into release/v0.3.7
-> rerun exact release and ordinary PR checks on the resulting exact head
-> verify prospective Current tree and deterministic package digest remain stable
-> present the exact reviewed head and open evidence boundaries
-> obtain explicit promotion authorization
```

Only after explicit authorization may PR #144 merge. Post-merge work then reverifies Current from `main`, updates status/history/field-validation routing, and runs the Project State Alignment Gate again.

## Open issues and branch hygiene

Open reconstruction/workstream issues `#89`–`#94` and `#104` remain research obligations while their scopes remain unfinished. They are not release blockers merely because they are open. Issue `#70` is tied to the v0.3.6 field-validation stream and should be superseded or reframed after v0.3.7 promotion.

Branch lifecycle is separate. Short-lived merged/noise/predecessor/validation refs should be removed after durable lineage is confirmed, while `research/ena-reconstruction`, `release/v0.3.7`, and frozen candidate.3 still have live pre-promotion roles. See `BRANCH-INVENTORY.yaml`. The current connector lacks a true delete-ref operation, so branch cleanup is classified durably rather than simulated by ref movement.

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
