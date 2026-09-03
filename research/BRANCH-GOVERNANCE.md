# ENA Branch Governance

Status: `PROJECT_CONTROL_PLANE / MAIN_VISIBLE / NON_NORMATIVE_TO_ENA_CURRENT`

## Core rule

> **Main is the durable continuation surface. Branches are temporary work surfaces, not archives or project authority.**

Live project state is discovered from:

```text
main / NOW.md
-> directly relevant Issue or artifact
-> deeper history only when it can change the decision
```

Current adoption authority remains:

`releases/current/CURRENT-BASELINE.yaml`

```text
BRANCH_EXISTS != BRANCH_ACTIVE
BRANCH_RECENT != PROJECT_AUTHORITY
OPEN_PR != CURRENT
MERGED_BRANCH_REF != REQUIRED_HISTORY
DELETE_BRANCH != DELETE_GIT_HISTORY
```

## Why this changed

Earlier ENA generations used a permanent `research/ena-reconstruction` integration branch plus separate release, candidate, validation, alignment, evidence, and temporary branches.

That topology was useful during reconstruction and v0.3.7 release formation, but after release and the project simplification work it became a coordination burden. Actual successful work increasingly followed a cheaper pattern:

```text
current main
-> short-lived purpose-specific branch
-> PR + relevant checks
-> merge to main
-> branch purpose exhausted
```

The old long-lived research branch also drifted behind main while retaining a few unique files, demonstrating why branch names should not be treated as durable knowledge stores.

Those unique files are being reconciled to main before branch retirement; see:

`research/branch-cleanup/2026-09-03-BRANCH-CLEANUP-AUDIT.md`

## Branch roles going forward

### `main`

Permanent project control plane and sole long-lived continuation branch.

Carries:

- `NOW.md` live project state;
- released Current under `releases/current/`;
- merged research/evidence;
- research methodology;
- durable field-validation results;
- handoff records and project lineage that still deserve persistence.

All files on main are **not** automatically ENA Current. Only the declared released surface is adopter-facing Current.

### Short-lived research/work branch

Create from current `main` only when a PR/isolation surface materially helps review, reproducibility, clean experimentation, or safe editing.

Preferred examples:

```text
research/<short-purpose>
evidence/<short-purpose>
handoff/<date-or-purpose>
housekeeping/<short-purpose>
```

A new idea alone does not justify a new durable branch.

After merge or explicit abandonment:

1. verify unique decision-relevant material is durable on main, in an immutable commit/PR, or in an evidence artifact;
2. delete the branch ref.

### Candidate branch

Create only for a real candidate lifecycle.

Frozen candidate identity is the exact source/tree/freeze binding, not the continued existence of the branch ref.

Delete the branch after candidate lifecycle closure when immutable lineage is durable.

### Release branch

Use only for actual release packaging/promotion when isolation is useful.

Delete after release closure/readback once exact release identity is durable.

### Fresh validation cleanroom

Fresh independent validation is **not** an ordinary branch role inside the source repo when project history would contaminate the experiment.

Prefer structurally isolated disposable repositories/surfaces with:

- identical common material across arms;
- no source-project/research/oracle history exposure;
- only the task/treatment variable intentionally differing;
- first complete answer captured before correction dialogue.

Durable occurrence evidence returns to ENA; the cleanroom itself may then be deleted.

## Branch creation test

Before creating a branch, ask:

```text
Does isolation/review materially help this change?
```

If no, do not create one merely to represent an idea.

If yes, create the smallest branch needed and plan its retirement at creation time.

## Branch closure test

A branch may be deleted when it is no longer the only carrier of decision-relevant material.

Durable carriers include:

- merged main artifact;
- immutable commit/tree;
- merged/closed PR preserving the occurrence;
- freeze/reconciliation record;
- field-validation archive.

Do not delete first and hope the work was duplicated somewhere.

```text
VERIFY UNIQUE CONTENT
-> PRESERVE IF NEEDED
-> DELETE REF
```

## Historical refs

Old release/candidate/validation/research branch names may appear in historical records. Those references remain truthful about past state and should not be rewritten merely because the branch ref is later deleted.

History is allowed to say:

> `research/ena-reconstruction` was the active integration branch at that time.

Live routing must not say it is active now.

## Cleanup authority

Current cleanup classification:

`research/branch-cleanup/2026-09-03-BRANCH-CLEANUP-AUDIT.md`

The connector used by the 2026-09-03 session does not expose a genuine branch-delete action. Do not simulate deletion by force-moving refs. Delete-safe refs may be removed manually through GitHub UI/CLI after the handoff PR is merged/read back.

## Successor-session behavior

A normal successor should **not** run a branch census before doing useful work.

Normally:

1. read `NOW.md`;
2. open the directly relevant artifact/Issue;
3. verify live `main` before writing;
4. create a short-lived branch if a PR is useful;
5. work.

Run a branch audit only when branch cleanup, lineage recovery, or a suspicious unmerged artifact is itself decision-relevant.

> **Branches carry work temporarily. Main and durable evidence carry the project forward.**
