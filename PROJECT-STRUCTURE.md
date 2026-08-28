# ENA Persistent Project Structure

Status: `PROJECT_INFORMATION_ARCHITECTURE / CURRENT`

ENA is one persistent project with distinct authority and evidence surfaces. Agent/session identity does not define project identity.

## Semantic areas

| Area | Path / surface | Role |
|---|---|---|
| Project control | `main`, `PROJECT-HUB.md`, `PROJECT-METADATA.yaml` | stable routing and Current authority pointers |
| Current adoption | `releases/current/` on `main` | singular complete adopter-facing Current baseline |
| Active research | branch named by `research/ACTIVE-RESEARCH.yaml` | integrated fast-moving research/project-management work |
| Handoff framework | `research/handoffs/` root | reusable outgoing/incoming succession rules |
| Handoff records | `research/handoffs/records/<handoff-id>/` | time-bounded succession occurrence truth |
| Research methodology | `research/methodology/` | how ENA research is performed |
| Plans/progress | `research/plans/` | long-horizon route + fast execution projection |
| Release branches | `release/<version>` | bounded temporary packaging/promotion surfaces |
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

## Current live topology — 2026-08-28 post-promotion

Authoritative live roles are narrow:

```text
main                         # project control + v0.3.7 Current
research/ena-reconstruction  # sole active research integration surface
```

A temporary `integration/v037-postpromotion-alignment` branch exists only while this Alignment Gate is being merged/read back.

Other release/candidate/validation/tmp/prepromotion/control-fix refs may remain physically visible because the current connector lacks delete-ref capability. Their branch names no longer carry active authority; durable occurrence truth is preserved in exact commits/trees, PRs, reconciliation, handoff, issues, sealed evidence, and Git history.

Current is:

```text
v0.3.7 / CURRENT / FIELD_VALIDATION
Current tree = f33e73ed997c1b66a4572685ab5474182e136e97
release merge = 50a4bb06b98dc0dd719230f71ed1d47e42e1fad9
field tracker = #150
```

Frozen release source remains exact candidate.3 source/tree:

```text
b7e88d7adb70396bd671ca97066daf2c120e0adc
e3a9a20d16cecd78df7f32f19fca56e21159e810
```

## Control plane vs work surfaces

`main` carries stable authority/routing. `research/ena-reconstruction` is the sole research continuation surface named by the canonical pointer. A completed release branch is historical workspace, not Current authority.

```text
BRANCH_EXISTS != BRANCH_ACTIVE
OPEN_PR != ACTIVE_RESEARCH_AUTHORITY
RELEASE_BRANCH != CURRENT
CANDIDATE_BRANCH_HEAD != FROZEN_IDENTITY
VALIDATION_BRANCH != RELEASE_AUTHORITY
```

## Issue and branch lifecycle distinction

```text
OPEN_RESEARCH_ISSUE = durable unresolved research/work obligation
SHORT_LIVED_BRANCH = temporary isolation mechanism
```

Current field evidence is tracked in #150. Reconstruction issues #89–#94 and #104 remain open while useful. Old field tracker #70 is closed and preserved as predecessor evidence.

Short-lived branch names should be removed after their lifecycle closes and durable lineage exists. The available connector lacks a delete-ref operation, so branch deletion remains explicit repository maintenance rather than being simulated by moving refs.

## Immutable Current and errata

v0.3.7's 118-file Current package is an immutable version identity. A stale pre-promotion sentence inside `CURRENT-BASELINE.yaml` is recorded externally as a release-metadata erratum rather than silently edited under the same version. Future correction requires a governed future release identity.

## Independent validation carrier

`guytogay/independent-validation-cleanroom` is reusable infrastructure rather than ENA project history. Its repository identity can be reused across stages and projects; contents are disposable stage-scoped review state. Durable findings and seals return to the relevant source project.

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

```text
INDIVIDUAL_FILE_CORRECT != PROJECT_STATE_COHERENT
MATERIAL_TRANSITION -> ALIGN -> RESUME
```

History may remain available through Git/PR/reconciliation records without masquerading as current routing.

> Preserve history durably; expose current authority narrowly; let concrete HOW and failure variation remain recoverable without turning repository topology into ontology.
