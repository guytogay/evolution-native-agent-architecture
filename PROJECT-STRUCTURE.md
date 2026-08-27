# ENA Persistent Project Structure

Status: `PROJECT_INFORMATION_ARCHITECTURE / CURRENT`

ENA uses one persistent project with multiple semantic areas. Participants do not receive separate ENA projects by Agent identity.

## GitHub semantic areas

| Area | Path | Role |
|---|---|---|
| Project Hub / machine metadata | `PROJECT-HUB.md`, `PROJECT-METADATA.yaml` | stable discovery and project state |
| Current adoption baseline | `releases/current/` | **single complete adopter-facing Current target** |
| Research control entry | `research/README.md`, `research/ACTIVE-RESEARCH.yaml` | discover active research without branch/PR guessing |
| Handoff framework | `research/handoffs/` root files | canonical outgoing/incoming session succession rules, takeover contract, management discipline |
| Handoff records | `research/handoffs/records/<handoff-id>/` | time-bounded project/session handoff occurrences and lineage |
| Research methodology | `research/methodology/` | canonical method for researching ENA itself |
| Convergence/divergence method | `research/methodology/CONVERGENCE-DIVERGENCE-DISCIPLINE.md` | distinguish valid representation compression from variation ablation |
| Project-state alignment | `research/methodology/PROJECT-STATE-ALIGNMENT-GATE.md` | realign live state, routing, method, plan, progress, candidate/release state after material transitions |
| Branch governance | `research/BRANCH-GOVERNANCE.md`, `research/BRANCH-INVENTORY.yaml` | branch roles, lifecycle, active-pointer discipline, cleanup |
| Long-horizon research plan | `research/plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md` | stable reconstruction-to-release plan |
| Fast-moving progress | `research/plans/PROGRESS.yaml` | aligned current execution projection |
| Active research execution | branch named by `research/ACTIVE-RESEARCH.yaml` | fast-moving reconstruction/prototypes/evidence/progress |
| Operational Architecture | `research/operational-architecture/` | problem/cue -> plural HOW -> implementation/evidence navigation |
| Release-scope research | `research/release-scope/` | candidate cargo selection, optionality, tooling/language/scope evidence |
| Evolution Inbox | `research/evolution-inbox/` | open unpromoted research/candidate state |
| Experiments | `research/experiments/` | experiment plans/results |
| Prototypes | `research/prototypes/` | non-current machine/design prototypes |
| Evidence | `evidence/` | observations/reference evidence |
| Contributions | `collaboration/inbox/` | unreconciled participant contributions |
| Reconciliation / freeze / validation | `collaboration/reconciliation/` | candidate freeze, author/independent validation, contribution reconciliation |
| Decisions | `decisions/` | durable architecture/process decisions |

## Succession hierarchy

The handoff system has three distinct layers:

```text
HANDOFF FRAMEWORK
research/handoffs/
  README.md
  CURRENT-HANDOFF.yaml
  HANDOFF-PROTOCOL.md
  REQUIRED-TAKEOVER-CONTEXT.yaml
  PROJECT-MANAGEMENT-DISCIPLINE.md

HANDOFF RECORDS
research/handoffs/records/<handoff-id>/
  instance-specific state / recent decisions / file map / readback

PROJECT METHODOLOGY
research/methodology/
  ENA research methods
```

```text
HANDOFF_FRAMEWORK != HANDOFF_RECORD
HANDOFF_RECORD != PROJECT_METHODOLOGY
```

The framework and project methodology are both mandatory takeover context.

Reusable method discovered during one record is promoted out of the record. Historical occurrence evidence remains in records/Git history.

## Current live topology

At the current transition:

```text
main
research/ena-reconstruction
candidate/v0.3.7-candidate.0
```

`main` is the permanent project control plane.

`research/ena-reconstruction` is the active research integration branch named by the main-visible pointer.

`candidate/v0.3.7-candidate.0` is a release-lifecycle surface; its branch head is **not** frozen candidate identity.

Frozen candidate.0 identity:

```text
source commit = d0e793593184740d9732902e948afd48ed96ae2f
candidate subtree = cffbf76fe1448b020b637c78d1f7ae46e4c0115b
```

The anti-ablation audit is complete with tree-external coverage repair. PR #115 is the draft `DO NOT MERGE` fresh independent falsification surface. Fresh Phase A is next.

## Control plane vs active work vs handoff

`main` carries the stable control plane:

```text
Current adoption pointer
+ project hub/metadata
+ current handoff pointer
+ handoff/takeover framework
+ active research pointer
+ research methodology
+ project-state alignment method
+ branch governance
+ long-horizon plan
```

The active research branch carries fast-moving work.

The current handoff **record** is a bootstrap projection, not authority.

```text
HANDOFF_RECORD != PROJECT_AUTHORITY
```

The handoff **framework** is canonical project process for succession.

An open PR is a transient review/integration artifact and is not continuation authority.

```text
BRANCH_EXISTS != BRANCH_ACTIVE
OPEN_PR != ACTIVE_BRANCH_AUTHORITY
TEMPORARY_BRANCH != RESEARCH_AUTHORITY
CANDIDATE_BRANCH_HEAD != FROZEN_CANDIDATE_IDENTITY
```

## Normal continuation route

```text
PROJECT-HUB.md
-> releases/current/CURRENT-BASELINE.yaml
-> research/handoffs/CURRENT-HANDOFF.yaml
-> research/handoffs/HANDOFF-PROTOCOL.md
-> research/handoffs/REQUIRED-TAKEOVER-CONTEXT.yaml
-> research/handoffs/PROJECT-MANAGEMENT-DISCIPLINE.md
-> current handoff record
-> required project methodology under research/methodology/
-> research/ACTIVE-RESEARCH.yaml
-> research/plans/PROGRESS.yaml
-> exact next action
```

There is one current handoff pointer at a time and many historical records.

```text
LATEST_HANDOFF_POINTER = ONE
HISTORICAL_HANDOFF_RECORDS = MANY
```

## Alignment after material transition

A material branch/control-plane handoff, session replacement, canonical-path move, methodology change, plan change, candidate/freeze/release-state change, or major checkpoint can leave project surfaces describing different generations.

Before substantive work resumes, use:

`research/methodology/PROJECT-STATE-ALIGNMENT-GATE.md`

```text
INDIVIDUAL_FILE_CORRECT != PROJECT_STATE_COHERENT
MATERIAL_TRANSITION -> ALIGN -> RESUME
```

The gate is transition-triggered rather than mandatory after every ordinary content commit.

## History preservation

GitHub does not need to preserve every historical branch name or handoff directory at its original live path forever in order to preserve history.

Superseded releases/candidates/research branches/handoffs remain recoverable through commits/trees, PRs, freeze/reconciliation records, evidence artifacts, and historical handoff records.

```text
MOVE_RECORD != ERASE_HISTORY
DELETE_BRANCH != DELETE_HISTORY
HISTORICAL_HANDOFF_PRESERVED != HISTORICAL_HANDOFF_ACTIVE
```

## Core information rules

- project-first, not Agent-first;
- project continuity must survive session replacement;
- one Current adoption baseline;
- one canonical current handoff pointer;
- one canonical active research integration pointer;
- handoff framework, handoff records, and project methodology are distinct layers;
- project-state inheritance without method inheritance is incomplete takeover;
- research topics/HOWs remain open-cardinality inside the active research tree;
- handoff records are maps, not project authority;
- candidate branch head is not frozen candidate identity;
- persistence != synchronization;
- Contribution != Reconciliation != Promotion;
- compression may reduce representation only after materially distinct behavior/variation is accounted for;
- material project transitions require state alignment before substantive work resumes.

> Preserve history durably; retrieve history selectively.

> Open knowledge does not mean always-loaded knowledge.
