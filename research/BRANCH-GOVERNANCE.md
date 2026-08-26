# ENA Branch Governance

Status: `PROJECT_CONTROL_PLANE / MAIN_VISIBLE / NON_NORMATIVE_TO_ENA_CURRENT`

Purpose: make branch topology legible to humans and future Agent sessions without turning Git branch names, PR numbers, or cached head SHAs into ENA semantics.

## Core rule

> **Discover active work from a canonical branch pointer, never from branch recency, naming intuition, an old PR number, or an embedded head SHA.**

The canonical pointer is:

`research/ACTIVE-RESEARCH.yaml`

```text
BRANCH_EXISTS != BRANCH_ACTIVE
BRANCH_RECENT != BRANCH_AUTHORITATIVE
OPEN_PR != ACTIVE_BRANCH_AUTHORITY
OPEN_PR != CURRENT
EMBEDDED_HEAD_SHA != LIVE_HEAD_PROOF
FROZEN_COMMIT != ACTIVE_WORKSPACE
```

## Why branch identity is stable but PR/head observations are not

The active research integration **branch** is the stable continuation coordinate selected by the main-visible control plane.

An integration PR is a transient transport/review artifact. The same active branch may have no open PR immediately after a checkpoint merge and later open a new PR without changing continuation authority.

Likewise, an exact head SHA is a live Git fact that must be re-read before writes. Embedding the active branch's own head SHA inside a file committed on that same branch is inherently self-staling: the commit that records the SHA creates a new SHA.

Therefore:

- active branch identity comes from `main/research/ACTIVE-RESEARCH.yaml`;
- open PRs are discovered from the active head branch when needed;
- current head is reverified from GitHub before writes;
- cached PR numbers or SHAs may be retained only as historical observations, not identity locks.

## Branch roles

### `main`

Permanent project control plane and canonical repository branch.

Carries:

- Current adoption pointer and `releases/current/`;
- project entrypoints and metadata;
- research branch pointer/governance;
- canonical research methodology and long-horizon project plan;
- merged durable research/evidence/history when reconciliation justifies it.

`main` does not mean every file on main is ENA Current. Current remains only the explicitly declared adopter-facing surface.

### Active research integration branch

Exactly one branch is designated by `research/ACTIVE-RESEARCH.yaml` as the current research integration workspace.

The count of one has a project-coordination reason: a successor session needs one unambiguous place to continue integrated research. It is not a claim that research has one topic or one HOW.

Current active branch:

`research/ena-reconstruction`

It succeeded the checkpointed and retired `research/memory-metabolism-prototype` generation after PR #82. The predecessor ref has been deleted; its lineage remains durable through Git history, PR #82, checkpoint commits, issues, and merged research artifacts.

### Temporary research/work branch

Use only when isolation is materially useful, for example:

- parallel implementation that cannot safely share a moving integration head;
- an independent validation environment;
- a destructive/rebase experiment;
- a machine harness that needs a separate PR/check surface.

Temporary branches:

- must target the active research integration branch or `main`, according to purpose;
- do not become inheritance authority;
- should have an Issue/PR/provenance link explaining why isolation was needed;
- should be deleted after merge/abandonment once unique lineage is durably reachable by commit/PR/evidence.

Do not create a branch merely because a new idea exists. Prefer an Issue, research artifact, or commit on the active integration branch.

### Candidate branch

Candidate branches exist only during an actual release-candidate lifecycle.

Preferred naming:

`candidate/<version>-candidate.<generation>`

where the generation is a real succession identity, not a decorative number.

Once frozen, the authoritative candidate identity is its exact commit/tree/freeze record, not continued branch mutability.

After the candidate lineage is closed or superseded and immutable refs are durably recorded, the branch may be deleted; deletion does not erase Git/PR/reconciliation lineage.

### Release branch

Use only for actual release packaging/promotion work:

`release/<version>`

Only one release branch should be active for one release decision at a time. The constraint is a release-coordination rule, not a statement about how many research lines may exist.

Delete/retire the branch after release closure once exact release identity is durably recorded.

### Evidence / validation / housekeeping branch

Short-lived branches that target `main` for bounded project/evidence work.

Examples:

`evidence/<slug>`
`validation/<slug>`
`housekeeping/<slug>`

They never become the active ENA research continuation surface unless `ACTIVE-RESEARCH.yaml` is explicitly changed through project-control-plane reconciliation.

## Naming policy going forward

Prefer role-first names whose first path component answers what the branch is for:

```text
research/ena-reconstruction      # current integration branch
research/work/<slug>             # temporary isolated research, if needed
candidate/<version>-candidate.<generation>
release/<version>
evidence/<slug>
validation/<slug>
housekeeping/<slug>
```

Do not create near-synonyms such as `build`, `rebased`, `plural`, `cross-how`, `final2`, etc. as long-lived topology. Put that information in the PR/commit/artifact, not in an ever-growing permanent branch namespace.

## Lifecycle state

Every non-main branch should be interpretable as one of:

```text
ACTIVE_INTEGRATION
TEMPORARY_ACTIVE
FROZEN_LINEAGE
MERGED_COMPLETE
CLOSED_SUPERSEDED
ABANDONED
DELETE_SAFE_AFTER_LINEAGE_CHECK
UNKNOWN_REQUIRES_REVIEW
```

The working inventory is `research/BRANCH-INVENTORY.yaml`.

## Branch closure rule

A branch is not kept merely because deleting it feels risky.

Before deletion/retirement, verify that decision-relevant lineage remains reachable through one or more of:

- merged commit;
- immutable commit SHA/tree;
- closed PR retaining the head identity;
- freeze/reconciliation record;
- evidence artifact.

Then the branch name may disappear without losing history.

```text
DELETE_BRANCH != DELETE_HISTORY
```

Conversely, a branch should not be deleted while it is the only discoverable carrier of material unmerged work.

## Successor-session protocol

A fresh session asked to continue ENA should:

1. start on `main`;
2. read `PROJECT-HUB.md`;
3. read `research/ACTIVE-RESEARCH.yaml`;
4. read `research/methodology/README.md` and the canonical methodology;
5. follow the active branch pointer and read its progress/plan;
6. reverify the active Git head and discover any open PR for that branch before writing;
7. ignore all other branches unless lineage/provenance makes them relevant.

It should **not** run a full branch census as a prerequisite to normal continuation.

## Pointer transition

Changing the active research integration **branch** is a project-state change and must update, in the same reconciled change where practical:

- `research/ACTIVE-RESEARCH.yaml`;
- `research/BRANCH-INVENTORY.yaml`;
- project metadata/pointers if their paths change;
- the old branch/PR with a visible handoff/closure note.

Opening, merging, closing, or replacing an integration PR on the **same active branch** does not by itself change active-branch authority and therefore must not require another control-plane branch transition.

The new branch must be discoverable from `main` before the old active branch is retired.

## Anti-bloat rule

Branch topology itself must pay complexity rent.

A new branch is justified only if isolation provides a material coordination, reproducibility, validation, or safety benefit that cannot be achieved economically with an Issue/artifact/commit on an existing appropriate branch.

> **One active research integration branch; many PR generations, research ideas, and HOW branches may live through it.**
