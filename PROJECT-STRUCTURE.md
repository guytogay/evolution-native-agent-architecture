# ENA Persistent Project Structure

Status: `PROJECT_INFORMATION_ARCHITECTURE / CURRENT`

ENA uses one persistent project with multiple semantic areas. Participants do not receive separate ENA projects by Agent identity.

## GitHub semantic areas

| Area | Path | Role |
|---|---|---|
| Project Hub / machine metadata | `PROJECT-HUB.md`, `PROJECT-METADATA.yaml` | stable discovery and project state |
| Current adoption baseline | `releases/current/` | **single complete adopter-facing Current target** |
| Research control entry | `research/README.md`, `research/ACTIVE-RESEARCH.yaml` | discover active research without branch/PR guessing |
| Standardized session handoffs | `research/handoffs/` | durable project-manager/session succession packages and current handoff pointer |
| Research methodology | `research/methodology/` | canonical main-visible method for researching and handing off ENA |
| Session handoff method | `research/methodology/SESSION-HANDOFF-DISCIPLINE.md` | outgoing/incoming project-manager protocol |
| Convergence/divergence method | `research/methodology/CONVERGENCE-DIVERGENCE-DISCIPLINE.md` | distinguish valid representation compression from variation ablation |
| Project-state alignment | `research/methodology/PROJECT-STATE-ALIGNMENT-GATE.md` | realign live state, routing, method, plan, progress, and candidate/release state after material transitions |
| Branch governance | `research/BRANCH-GOVERNANCE.md`, `research/BRANCH-INVENTORY.yaml` | branch roles, lifecycle, active-pointer discipline, cleanup |
| Long-horizon research plan | `research/plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md` | stable reconstruction-to-release plan |
| Fast-moving progress | `research/plans/PROGRESS.yaml` | aligned current execution projection |
| Active research execution | branch named by `research/ACTIVE-RESEARCH.yaml` | fast-moving reconstruction/prototypes/evidence/progress |
| Operational Architecture | `research/operational-architecture/` | problem/cue -> plural HOW -> implementation/evidence navigation |
| Release-scope research | `research/release-scope/` | candidate cargo selection, optionality, tooling/language/scope evidence |
| Evolution Inbox | `research/evolution-inbox/` | open unpromoted research/candidate state |
| HAR | `research/adversarial-replay/` | historical adversarial research |
| Experiments | `research/experiments/` | experiment plans/results |
| Prototypes | `research/prototypes/` | non-current machine/design prototypes |
| Evidence | `evidence/` | observations/reference evidence |
| Contributions | `collaboration/inbox/` | unreconciled participant contributions |
| Reconciliation / freeze / validation | `collaboration/reconciliation/` | candidate freeze, author/independent validation, contribution reconciliation |
| Decisions | `decisions/` | durable architecture/process decisions |

## Current live topology

At the 2026-08-27 standardized session handoff:

```text
main
research/ena-reconstruction
candidate/v0.3.7-candidate.0
```

`main` is the permanent project control plane.

`research/ena-reconstruction` is the one active research integration branch and remains general project-research continuation authority.

`candidate/v0.3.7-candidate.0` is a release-lifecycle surface. Its **branch head is not the frozen candidate identity**.

Frozen candidate.0 identity is externally bound as:

```text
source commit = d0e793593184740d9732902e948afd48ed96ae2f
candidate subtree = cffbf76fe1448b020b637c78d1f7ae46e4c0115b
```

The branch may contain later tree-external freeze/review records without redefining the frozen subtree.

## Control plane vs active work vs handoff

`main` carries the stable control plane:

```text
Current adoption pointer
+ project hub/metadata
+ current session-handoff pointer
+ active research branch pointer
+ research methodology
+ project-state alignment method
+ branch governance
+ long-horizon plan
```

The active research integration branch carries fast-moving work such as reconstruction ledgers, external HOW harvesting, prototypes, deterministic fixtures, field evidence, validation-method repair, and detailed progress.

A standardized handoff package under `research/handoffs/` is a **bootstrap projection** that helps a successor find and understand those surfaces quickly.

```text
HANDOFF_PACKAGE != PROJECT_AUTHORITY
```

An open PR is a transient review/integration artifact and is not required for active branch authority.

A temporary branch may exist for bounded isolation/validation, but it does not become a second research world.

```text
BRANCH_EXISTS != BRANCH_ACTIVE
OPEN_PR != ACTIVE_BRANCH_AUTHORITY
TEMPORARY_BRANCH != RESEARCH_AUTHORITY
CANDIDATE_BRANCH_HEAD != FROZEN_CANDIDATE_IDENTITY
```

## Branch and handoff discoverability

Normal project/research continuation starts from `main` and uses:

```text
PROJECT-HUB.md
-> releases/current/CURRENT-BASELINE.yaml
-> research/handoffs/CURRENT-HANDOFF.yaml
-> research/ACTIVE-RESEARCH.yaml
```

There is deliberately one active research integration pointer and one current handoff pointer at a time. These are coordination invariants, not ontological limits on research diversity or historical lineage.

Branch lifecycle details:

`research/BRANCH-GOVERNANCE.md`

Handoff lifecycle details:

`research/methodology/SESSION-HANDOFF-DISCIPLINE.md`

## Alignment after material transition

A material branch/control-plane handoff, session replacement, directory/canonical-path change, methodology change, plan change, candidate/freeze/release-state change, or major checkpoint can leave project surfaces describing different generations.

Before substantive work resumes, use:

`research/methodology/PROJECT-STATE-ALIGNMENT-GATE.md`

```text
INDIVIDUAL_FILE_CORRECT != PROJECT_STATE_COHERENT
MATERIAL_TRANSITION -> ALIGN -> RESUME
```

The gate is transition-triggered rather than mandatory after every ordinary content commit.

## History preservation

GitHub does **not** need to preserve every historical branch name or handoff as a live pointer forever in order to preserve history.

Superseded releases/candidates/research branches/handoffs remain recoverable through Git commits/trees, PRs, freeze/reconciliation records, evidence artifacts, and historical handoff directories.

```text
DELETE_BRANCH != DELETE_HISTORY
HISTORICAL_HANDOFF_PRESERVED != HISTORICAL_HANDOFF_ACTIVE
```

Do not delete a branch while it is the only discoverable carrier of material unmerged work. Do not keep it forever merely because deletion feels safer after lineage has already been preserved.

## Core information rules

- project-first, not Agent-first;
- project continuity must survive session replacement;
- one Current adoption baseline;
- one canonical current handoff pointer;
- one canonical active research integration branch pointer;
- research topics/HOWs remain open-cardinality inside the active research tree;
- open PR identity is transient and not continuation authority;
- handoff packages are maps, not authority;
- candidate branch head is not frozen candidate identity;
- not every accessible artifact is loaded into every task;
- Contribution != Reconciliation != Promotion;
- persistence != synchronization;
- copy/bridge must preserve provenance and semantic status;
- current adoption state must not be inferred from archive, old chat, handoff, candidate branch, or research branch;
- active research state must not be inferred from branch recency, naming intuition, old PR identity, or cached head SHA;
- compression may reduce representation only after materially distinct behavior/variation is accounted for;
- material project transitions require state alignment before substantive work resumes.

> Preserve history durably; retrieve history selectively.

> Open knowledge does not mean always-loaded knowledge.
