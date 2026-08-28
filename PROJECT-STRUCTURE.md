# ENA Persistent Project Structure

Status: `PROJECT_INFORMATION_ARCHITECTURE / CURRENT`

ENA is one persistent project with distinct authority and evidence surfaces. Agent/session identity does not define project identity.

## Semantic areas

| Area | Path / surface | Role |
|---|---|---|
| Project control | `main`, `PROJECT-HUB.md`, `PROJECT-METADATA.yaml` | stable routing and Current authority pointers |
| Current adoption | `releases/current/` on `main` | single complete adopter-facing Current baseline |
| Active research | branch named by `research/ACTIVE-RESEARCH.yaml` | integrated fast-moving research/project-management work |
| Handoff framework | `research/handoffs/` root | reusable outgoing/incoming succession rules |
| Handoff records | `research/handoffs/records/<handoff-id>/` | time-bounded succession occurrence truth |
| Research methodology | `research/methodology/` | how ENA research is performed |
| Plans/progress | `research/plans/` | long-horizon route + fast-moving execution projection |
| Release branch | `release/<version>` | bounded packaging/promotion surface only |
| Candidate branches | `candidate/<version>-candidate.<generation>` | governed candidate lineage; frozen identity is exact source/tree, not branch recency |
| Validation surfaces | `validation/*` or isolated carrier | bounded review occurrence truth; never Current authority |
| Reconciliation/evidence | `collaboration/reconciliation/`, `evidence/` | durable decisions, freezes, validation and occurrence records |

## Succession layers

```text
HANDOFF FRAMEWORK = reusable succession method
HANDOFF RECORD = one succession occurrence
PROJECT METHODOLOGY = how ENA research is conducted
```

All are relevant to project-manager takeover, but a handoff record is not project authority.

## Current live topology — 2026-08-28 pre-promotion

Live coordination surfaces include:

```text
main
research/ena-reconstruction
release/v0.3.7
integration/v037-prepromotion-alignment   # temporary alignment surface
```

Candidate and historical validation refs also remain live. Their existence does not create parallel continuation authority. Their cleanup disposition is recorded in `research/BRANCH-INVENTORY.yaml`; branch names are not archives.

Current remains:

```text
v0.3.6 / CURRENT / FIELD_VALIDATION
Current tree = 7dcbb3934883ffa6cc5292a662588cafc1533cff
```

Frozen final release source:

```text
v0.3.7-candidate.3
source  = b7e88d7adb70396bd671ca97066daf2c120e0adc
subtree = e3a9a20d16cecd78df7f32f19fca56e21159e810
```

Prospective v0.3.7 release state:

```text
release branch                  = release/v0.3.7
release PR                      = #144 / OPEN DRAFT / NOT PROMOTED
byte-exact transplant commit    = 8e4e25a8ba1940560fc55d7528ad31ef89a7f135
prospective Current tree        = f33e73ed997c1b66a4572685ab5474182e136e97
exact validated release head    = bcda18a28141f572688f9a1b15cfd820dea02f97
118-file package SHA-256        = 40d4dde277d54ce8252e0402e32f900fa7ab4fb0aeaa638b898073d0f02f848c
identity/status projection      = complete on release branch
exact release gate              = PASS / run 33161514271
promotion                       = not authorized / not started
```

The release branch is not an adoption authority until exact-head checks, explicit authorization, merge, and post-merge readback complete.

## Control plane vs work surfaces

`main` carries stable authority/routing. `research/ena-reconstruction` is the sole research continuation surface named by the canonical pointer. `release/v0.3.7` is a bounded release packaging workspace. The pre-promotion alignment branch exists only to reconcile main-visible state before a promotion decision.

```text
BRANCH_EXISTS != BRANCH_ACTIVE
OPEN_PR != ACTIVE_RESEARCH_AUTHORITY
RELEASE_BRANCH != CURRENT
GREEN_RELEASE_GATE != PROMOTION_AUTHORITY
CANDIDATE_BRANCH_HEAD != FROZEN_IDENTITY
VALIDATION_BRANCH != RELEASE_AUTHORITY
```

## Issue and branch lifecycle distinction

Issue state and branch state serve different purposes:

```text
OPEN_RESEARCH_ISSUE = durable unresolved research/work obligation
SHORT_LIVED_BRANCH = temporary isolation mechanism
```

Research issues should remain open while they still carry decision-relevant obligations; they are not closed merely to make the repository look finished. Conversely, short-lived branch names should be removed once their lifecycle is closed and durable lineage is preserved. The currently available connector lacks a delete-ref operation, so branch deletion must remain an explicit maintenance action rather than being simulated by moving refs.

## Independent validation carrier

The reusable repository `guytogay/independent-validation-cleanroom` is infrastructure rather than ENA project history.

Its repository identity can be reused across stages and projects; its contents are disposable stage-scoped review state. Durable findings and seals return to the relevant source project.

## Normal continuation route

```text
PROJECT-HUB.md
-> Current baseline
-> current handoff pointer/framework/record
-> required methodology
-> ACTIVE-RESEARCH.yaml
-> PROGRESS.yaml + master plan
-> live ref/exact identity verification
-> first permitted unfinished action
```

## Alignment rule

After a material branch, candidate, release, methodology, plan, or handoff transition:

```text
INDIVIDUAL_FILE_CORRECT != PROJECT_STATE_COHERENT
MATERIAL_TRANSITION -> ALIGN -> RESUME
```

The present alignment exists because release packaging, oracle reconciliation, exact-head validation, and release-branch control hardening advanced beyond the prior main-visible projections while Current itself remained v0.3.6.

History may remain available through Git/PR/reconciliation records without continuing to masquerade as current routing.

> Preserve history durably; expose current authority narrowly; let concrete HOW and failure variation remain recoverable without turning repository topology into ontology.
