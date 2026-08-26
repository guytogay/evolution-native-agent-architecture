# ENA Research Methodology — Project State Alignment Gate

Status: `CANONICAL_FOCUSED_METHOD / CONTINUITY_ALIGNMENT / NON_NORMATIVE_TO_CURRENT`

Purpose: prevent individually correct project documents from drifting into a collectively inconsistent project state after a material transition.

```text
INDIVIDUAL_FILE_CORRECT != PROJECT_STATE_COHERENT
MATERIAL_TRANSITION -> ALIGN -> RESUME
HISTORY_PRESERVED != HISTORY_USED_AS_CURRENT_POINTER
```

This method is about researching and maintaining ENA. It is not an adopter-facing Constitution rule.

## Why this gate exists

ENA research is intentionally distributed across a stable `main` control plane and a fast-moving active research branch. Branch handoffs, checkpoint merges, directory changes, method corrections, release-state changes, and cleanup can make several documents stale in different directions even when each change was locally reasonable.

The failure pattern is:

```text
material project transition
-> one pointer is updated
-> another guide still describes the old topology
-> progress still names an old PR/branch/state
-> a successor retrieves a mixed picture
-> selection/routing drifts before substantive research even starts
```

The correction is to align the project state as a system before resuming substantive work.

## Trigger conditions

Run the full alignment gate after a material transition capable of changing project routing, method, planning, or authority, including:

- active research branch creation, handoff, retirement, rename, or deletion;
- branch-governance or active-pointer changes;
- a major research checkpoint merge to `main`;
- directory/information-architecture changes that move canonical files;
- a material research-methodology correction;
- a master-plan phase, closure rule, or release path change;
- Current/candidate/release identity or maturity-state change;
- a session handoff that follows any of the above;
- discovery of contradictory current-state statements in canonical files.

Do **not** turn this into ceremony after every ordinary content commit. A minor prototype edit, evidence append, or wording correction that does not change routing/method/plan/state does not automatically require a full alignment pass.

A successor/resuming session should still verify whether a material transition occurred since the last aligned checkpoint.

## Required alignment surfaces

### 1. Live repository state

Verify from GitHub rather than prose memory:

- default branch;
- actual live branch list when topology changed;
- active research branch from `main/research/ACTIVE-RESEARCH.yaml`;
- current live branch head before writes;
- open PR for the active branch only when PR context is needed;
- `releases/current/CURRENT-BASELINE.yaml` for Current adoption identity.

```text
ACTIVE_RESEARCH_AUTHORITY = MAIN_VISIBLE_BRANCH_POINTER
OPEN_PR = TRANSIENT_INTEGRATION_ARTIFACT
HEAD_SHA = LIVE_REVERIFY_BEFORE_WRITE
```

### 2. Stable routing / directory guides

Check that these tell the same current story:

- `PROJECT-HUB.md`;
- `PROJECT-STRUCTURE.md`;
- `PROJECT-METADATA.yaml` where machine-readable routing matters;
- `research/README.md`;
- `research/ACTIVE-RESEARCH.yaml`;
- `research/BRANCH-GOVERNANCE.md`;
- `research/BRANCH-INVENTORY.yaml`.

Historical branch/PR names may remain as lineage but must not be phrased as current continuation authority.

### 3. Research methodology

Check:

- `research/methodology/README.md`;
- `research/methodology/ENA-RESEARCH-DISCIPLINE.md`;
- relevant focused methodology files;
- `research/methodology/METHOD-CHANGELOG.md`.

A material method discovered on the active branch must be reconciled into the main-visible canonical methodology before relying on future sessions to inherit it.

### 4. Plan and progress

Check together:

- `research/plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md` on `main`;
- `research/plans/PROGRESS.yaml` on the active research branch;
- `research/RESEARCH-START-HERE.md` on the active branch.

The master plan describes the stable route; Progress describes where execution actually is. Neither may silently override Current.

### 5. Current vs lineage references

Classify stale-looking references before deleting them:

```text
CURRENT_POINTER
CURRENT_WORKSPACE
HISTORICAL_LINEAGE
EVIDENCE_SOURCE
SUPERSEDED_GUIDANCE
```

Old PRs, branches, and commits may remain valuable history. The goal is not to erase them; it is to stop history from masquerading as current state.

### 6. Next-action coherence

Before closing the gate, verify that the next actions permitted by Progress are consistent with:

- the active methodology;
- the current research phase;
- known evidence/failure boundaries;
- branch/release authority;
- the master plan's prerequisites.

If the documents disagree about what should happen next, alignment is not complete.

## Closure condition

The alignment gate closes when a fresh successor can answer from persisted sources, without guessing:

- What is Current?
- What is the one active research branch?
- Where is canonical research methodology?
- What is the current long-horizon phase structure?
- What is the fast-moving execution state?
- Which old branches/PRs are only lineage?
- What next substantive work is permitted?
- What is explicitly **not** authorized yet?

and those answers are mutually consistent across the control plane, method, plan, and progress surfaces.

## Non-goals

Alignment is not:

- rereading every historical artifact;
- reopening every resolved issue;
- forcing all research into `main`;
- synchronizing every file after every commit;
- proving the architecture is complete;
- authorizing a release.

```text
ALIGNMENT_GATE != FULL_PROJECT_REVIEW_FROM_ZERO
ALIGNMENT_COMPLETE != RESEARCH_COMPLETE
ALIGNMENT_COMPLETE != RELEASE_AUTHORIZED
```

## Handoff rule

After any material transition, do not resume substantive ENA research until the alignment gate has either:

- been completed and recorded in `research/plans/PROGRESS.yaml`; or
- been shown unnecessary because no routing/method/plan/state surface changed.

> **Before growing the next branch of the tree, make sure every map still points to the same tree.**
