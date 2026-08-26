# ENA Persistent Project Structure

Status: `PROJECT_INFORMATION_ARCHITECTURE / CURRENT`

ENA uses one persistent project with multiple semantic areas. Participants do not receive separate ENA projects by Agent identity.

## GitHub semantic areas

| Area | Path | Role |
|---|---|---|
| Project Hub / machine metadata | `PROJECT-HUB.md`, `PROJECT-METADATA.yaml` | stable discovery and project state |
| Current adoption baseline | `releases/current/` | **single complete adopter-facing Current target** |
| Research control entry | `research/README.md`, `research/ACTIVE-RESEARCH.yaml` | discover active research without branch guessing |
| Research methodology | `research/methodology/` | canonical main-visible method for researching ENA |
| Branch governance | `research/BRANCH-GOVERNANCE.md`, `research/BRANCH-INVENTORY.yaml` | branch roles, lifecycle, active-pointer discipline, cleanup |
| Long-horizon research plan | `research/plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md` | stable reconstruction-to-release plan |
| Active research execution | branch named by `research/ACTIVE-RESEARCH.yaml` | fast-moving reconstruction/prototypes/evidence/progress |
| Evolution Inbox | `research/evolution-inbox/` | open unpromoted research/candidate state |
| HAR | `research/adversarial-replay/` | historical adversarial research |
| Experiments | `research/experiments/` | experiment plans/results |
| Prototypes | `research/prototypes/` | non-current machine/design prototypes |
| Evidence | `evidence/` | observations/reference evidence |
| Contributions | `collaboration/inbox/` | unreconciled participant contributions |
| Reconciliation | `collaboration/reconciliation/` | handling/selection of contributions |
| Decisions | `decisions/` | durable architecture/process decisions |

## Control plane vs active work

`main` carries the stable control plane:

```text
Current adoption pointer
+ project hub/metadata
+ active research pointer
+ research methodology
+ branch governance
+ long-horizon plan
```

The active research integration branch carries fast-moving work such as reconstruction ledgers, external HOW harvesting, prototypes, deterministic fixtures, field evidence, and detailed progress.

A temporary branch may exist for bounded isolation/validation, but it does not become a second research world.

```text
BRANCH_EXISTS != BRANCH_ACTIVE
TEMPORARY_BRANCH != RESEARCH_AUTHORITY
```

## Branch discoverability

Normal research continuation starts from:

`research/ACTIVE-RESEARCH.yaml`

There is deliberately one active research integration pointer at a time so a successor session has an unambiguous continuation target. This is a coordination invariant, not an ontology or limit on research diversity.

Branch lifecycle details:

`research/BRANCH-GOVERNANCE.md`

## History preservation

GitHub does **not** need to preserve every historical branch name forever in order to preserve history.

Superseded releases/candidates/research branches remain recoverable through Git commits/trees, merged or closed PRs, freeze/reconciliation records, and evidence artifacts.

```text
DELETE_BRANCH != DELETE_HISTORY
```

Do not delete a branch while it is the only discoverable carrier of material unmerged work. Do not keep it forever merely because deletion feels safer after lineage has already been preserved.

## Maintainer recovery mirror

The maintainer may keep a private complementary durable artifact/research/evidence/recovery surface. Its storage coordinates are intentionally outside public project metadata.

That surface is not required for adoption and does not create another ENA runtime/adoption layer.

## Core information rules

- project-first, not Agent-first;
- one Current adoption baseline;
- one canonical active research integration pointer;
- research topics/HOWs remain open-cardinality inside the active research tree;
- knowledge/research may remain broad and open;
- not every accessible artifact is loaded into every task;
- Contribution != Reconciliation != Promotion;
- persistence != synchronization;
- copy/bridge must preserve provenance and semantic status;
- current adoption state must not be inferred from an archive, old chat, candidate branch, or research branch;
- active research state must not be inferred from branch recency or naming intuition.

> Preserve history durably; retrieve history selectively.

> Open knowledge does not mean always-loaded knowledge.
