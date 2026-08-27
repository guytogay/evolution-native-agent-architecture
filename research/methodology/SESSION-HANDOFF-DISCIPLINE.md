# ENA Session Handoff Discipline

Status: `CANONICAL_PROJECT_HANDOFF_METHOD / MAIN_VISIBLE / NON_NORMATIVE_TO_ENA_CURRENT / OPEN_CARDINALITY`

This method standardizes **project-manager/session succession** for ENA. Session handoff is a normal lifecycle event, not an exception or failure.

The goal is that a fresh Agent/session can take over without asking the user to reconstruct project history, without inferring authority from stale chat, and without silently losing unresolved variation.

```text
SESSION_CONTINUITY != CHAT_CONTINUITY
HANDOFF_PACKAGE != PROJECT_AUTHORITY
DURABLE != DISCOVERABLE != RETRIEVED != SALIENT != APPLIED
```

## 1. Core rule

A handoff is a **durable bootstrap projection over canonical project state**.

It must make the project easy to inherit, but it must never become a competing source of truth.

```text
HANDOFF_SUMMARY = FAST_BOOTSTRAP_PROJECTION
CANONICAL_FILES + LIVE_REFS = AUTHORITY
```

When handoff text conflicts with Current, a frozen candidate record, a live branch ref, a canonical methodology file, or another explicit authority surface, the authority surface wins and the handoff must be repaired.

## 2. When handoff is required

Create or refresh a handoff package when any of the following is true:

- the current session is becoming unstable, saturated, or likely to be restarted;
- the user intentionally rotates to a new project-manager session/Agent;
- a long pause makes conversational memory unreliable;
- a material branch/release/candidate/research phase transition occurred and a new operator will continue;
- the current operator is about to stop while material work remains open;
- the user explicitly asks for project handoff.

Do not wait for catastrophic context loss.

## 3. Required handoff package

Every material handoff must provide a coherent package under `research/handoffs/<handoff-id>/`.

The standard package contains at least:

1. **`HANDOFF-START-HERE.md`**
   - executive project state;
   - exact current phase;
   - what must not be changed casually;
   - exact next action;
   - takeover read order.

2. **`PROJECT-STATE.md`**
   - Current identity;
   - active research branch and live observed head;
   - candidate/release/freeze state;
   - exact frozen source/tree bindings where applicable;
   - PR/CI/reconciliation state;
   - open residuals and blockers;
   - allowed/forbidden next transitions.

3. **`RECENT-THREE-ROUNDS.md`**
   - at least the latest three decision-bearing project conversation rounds;
   - for each round: user concern/decision, project-manager response, durable change, unresolved consequence;
   - include older rounds when they are still necessary to explain the current decision.

`THREE_ROUNDS = MINIMUM_CONTINUITY_WINDOW`, not a completeness limit.

4. **`FILE-CATALOG.md`**
   - classified directory tree;
   - exact repository paths;
   - what each file/directory is for;
   - which files are authority, bootstrap projection, evidence, lineage, or optional detail;
   - recommended read order for different takeover tasks.

5. **`PROJECT-MANAGEMENT-LESSONS.md`**
   - newly learned project/research-management lessons;
   - incidents that changed method;
   - operational traps the next session should not repeat;
   - links to canonical methodology where lessons were promoted.

6. **`HANDOFF-MANIFEST.yaml`**
   - machine-readable package identity;
   - exact canonical pointers;
   - live-observed refs at handoff time;
   - frozen candidate identity where relevant;
   - next action and forbidden actions;
   - handoff completeness/readback state.

The package may grow when a distinct handoff problem requires another artifact. Do not add files merely for presentation symmetry.

## 4. Stable handoff pointer

`research/handoffs/CURRENT-HANDOFF.yaml` is the stable pointer to the latest intended session handoff package.

Historical handoffs remain durable lineage and must not compete as current pointers.

```text
LATEST_HANDOFF_POINTER = ONE
HISTORICAL_HANDOFFS = MANY
```

A successor should not infer the latest handoff from directory timestamps or lexicographic names.

## 5. Outgoing session protocol

Before declaring handoff ready, the outgoing project-manager session must:

### A. Flush material work

- persist all decision-material work to GitHub;
- do not leave material code, plans, fixtures, conclusions, or candidate state only in local/container/chat state;
- explicitly record anything that could not be persisted.

```text
LOCAL_ARTIFACT_IS_NOT_DURABLE_UNTIL_PERSISTED
```

### B. Reverify reality

Read live state rather than relying on cached conversation values:

- default/main head;
- active research branch head;
- Current baseline;
- candidate branch head if applicable;
- exact frozen candidate record/source/tree if applicable;
- open PRs and relevant CI/run state;
- release/promotion status.

### C. Align project-state projections

If material transitions occurred, run the Project State Alignment Gate before handoff.

At minimum reconcile stale:

- `PROJECT-HUB.md` routing;
- `research/ACTIVE-RESEARCH.yaml`;
- `research/plans/PROGRESS.yaml`;
- master plan phase state when materially changed;
- `research/RESEARCH-START-HERE.md` when takeover routing changed;
- `research/handoffs/CURRENT-HANDOFF.yaml`.

A handoff package must not paper over stale canonical state.

### D. Preserve exact identity and lineage

Record exact immutable identities for frozen/released objects.

Do not replace content-addressed identity with branch recency, filenames, file counts, or narrative descriptions.

```text
BRANCH_HEAD != FROZEN_CANDIDATE_IDENTITY
HISTORY_PRESERVED != HISTORY_USED_AS_CURRENT_POINTER
```

### E. Preserve unresolved variation

A handoff is allowed to compress prose, but it must not silently compress decision-relevant possibility space.

Use explicit disposition for unresolved branches:

```text
ACTIVE
NEXT
DEFERRED
DORMANT
FIELD_EVIDENCE_REQUIRED
BLOCKED
RETIRED_WITH_EVIDENCE
UNKNOWN
```

Do not turn `UNKNOWN`, `DEFERRED`, or `NOT_BUNDLED` into disappearance for narrative neatness.

### F. Capture recent conversation continuity

Preserve at least the last three decision-bearing rounds and any older reasoning needed to understand the next action.

Do not dump raw chat when a structured decision record is sufficient; do not summarize away disagreement, reversals, or method corrections.

### G. Publish and read back

- update `CURRENT-HANDOFF.yaml`;
- route the handoff from stable project entrypoints;
- use a PR to integrate main-visible handoff/control-plane changes;
- run applicable CI;
- after merge, read back the actual main state and compare it with the handoff manifest.

`WRITTEN != HANDOFF_COMPLETE`.

## 6. Incoming session protocol

A new project-manager session should use this sequence by default:

1. start at repository `main`;
2. read `PROJECT-HUB.md`;
3. verify `releases/current/CURRENT-BASELINE.yaml`;
4. read `research/handoffs/CURRENT-HANDOFF.yaml`;
5. read the pointed `HANDOFF-START-HERE.md` and `HANDOFF-MANIFEST.yaml`;
6. independently reverify live branch heads, frozen identities, and release state named by the handoff;
7. read `research/ACTIVE-RESEARCH.yaml`;
8. read canonical methodology, including this handoff discipline and the convergence/divergence discipline;
9. read `research/plans/PROGRESS.yaml` and the long-horizon master plan;
10. read the recent-three-rounds record and only the deeper evidence/prototypes needed for the next action;
11. if any current-state surfaces disagree, run the Project State Alignment Gate before substantive work;
12. state the inherited project state and first permitted next action from persisted evidence;
13. continue work without asking the user to repeat information already durably available.

The incoming session must treat the handoff as a **map**, then verify the terrain.

## 7. Authority hierarchy during takeover

For conflicts, prefer the most specific governed source:

```text
Current identity
  -> releases/current/CURRENT-BASELINE.yaml

Frozen candidate identity
  -> external freeze record + exact source/tree binding

Active research routing
  -> research/ACTIVE-RESEARCH.yaml on main

Canonical research method
  -> research/methodology/ on main

Fast-moving execution state
  -> research/plans/PROGRESS.yaml on the active research surface after alignment

Handoff package
  -> bootstrap projection / continuity aid

Chat summary
  -> non-authoritative context
```

## 8. Handoff completeness test

Do not call a handoff complete unless the next session can answer from persisted sources:

- What is Current?
- What phase is the project actually in?
- Which branch is active research authority?
- Is there a candidate? Is it mutable, frozen, validated, released, or Current?
- What exact immutable identity must not be rewritten?
- What changed in the latest session?
- What were the latest three decision-bearing conversation rounds?
- Which methodology governs the next step?
- What is the next permitted action?
- What actions are explicitly forbidden right now?
- Which open residuals may change the next release/candidate decision?
- Where are the supporting files and evidence?

If the next session must reconstruct these answers from chat archaeology, handoff failed.

## 9. Anti-convergence rule for handoff writing

LLMs tend to present successful handoffs as elegant summaries. ENA requires a different discipline when summary would erase decision-relevant branching.

```text
COMPRESS_HANDOFF_PROSE = ALLOWED
COMPRESS_DECISION_RELEVANT_VARIATION = NOT_ALLOWED_WITHOUT_EQUIVALENCE_EVIDENCE
```

The canonical focused guard is:

`research/methodology/CONVERGENCE-DIVERGENCE-DISCIPLINE.md`

## 10. Handoff is not promotion authority

Creating, merging, or reading a handoff does not authorize:

- Current mutation;
- candidate succession;
- release promotion;
- retiring unresolved HOWs;
- accepting an author's validation oracle;
- skipping independent review.

```text
HANDOFF_COMPLETE != PROJECT_DECISION_COMPLETE
```

## 11. Normal lifecycle rule

A project designed for many Agents/sessions must assume operators will be replaced.

> **A healthy ENA project should survive the loss of its current conversational context without losing project state, method, or decision lineage.**
