# ENA Project Handoff Protocol

Status: `CANONICAL_HANDOFF_FRAMEWORK / MAIN_VISIBLE / OUTGOING_AND_INCOMING_EQUAL_PRIORITY / NOT_ENA_CURRENT`

This file governs normal project-manager/session succession for ENA.

The project must survive replacement of the current conversational Agent without requiring the user to reconstruct project history, method, or decision lineage.

```text
PROJECT_CONTINUITY > SESSION_CONTINUITY
HANDOFF_FRAMEWORK != HANDOFF_RECORD
HANDOFF_RECORD != PROJECT_AUTHORITY
PROJECT_STATE_INHERITANCE WITHOUT METHOD_INHERITANCE = INCOMPLETE_TAKEOVER
```

## 1. Three-layer model

### A. Handoff framework — `research/handoffs/`

Persistent rules for **how to hand over and how to take over**.

Canonical framework files:

- `HANDOFF-PROTOCOL.md` — this file; outgoing and incoming rules;
- `REQUIRED-TAKEOVER-CONTEXT.yaml` — machine-readable mandatory context;
- `PROJECT-MANAGEMENT-DISCIPLINE.md` — cross-session project-management rules and promoted lessons;
- `CURRENT-HANDOFF.yaml` — stable pointer to the latest intended record.

### B. Handoff records — `research/handoffs/records/<handoff-id>/`

Time-bounded project-state snapshots and continuity evidence for one succession event.

A record may describe what method mattered at that time, but reusable method must live in the framework or project methodology, not permanently inside one record.

### C. Project methodology — `research/methodology/`

How ENA research itself is performed: falsification, convergence/divergence, project-state alignment, evidence discipline, etc.

Project methodology is mandatory takeover context even though it is not project state.

```text
TAKEOVER = STATE + METHOD + GOVERNANCE + DECISION_LINEAGE + NEXT_ACTION
```

## 2. Equality rule: transfer and takeover both matter

The outgoing protocol and incoming protocol have equal project-continuity importance.

A perfect outgoing package can still fail if the receiver does not retrieve, verify, interpret, and apply it.

A disciplined receiver cannot recover information that the outgoing session never persisted.

```text
HANDOFF_QUALITY = OUTGOING_COMPLETENESS x INCOMING_APPLICATION
```

This is conceptual composition, not a numeric scoring formula.

## 3. Outgoing session protocol

Before declaring succession ready, the outgoing project manager must:

1. **Flush material work**
   - persist decision-material code, plans, evidence, conclusions, fixtures, and open questions;
   - explicitly record anything that could not be persisted.

2. **Reverify live reality**
   - main/default head;
   - active research pointer and live branch head;
   - Current baseline;
   - candidate/release/freeze identity;
   - open PR/review state and material CI state.

3. **Run project-state alignment when needed**
   - repair stale routing, Progress, plan, Active Research, handoff pointer, and other current-state projections after material transitions.

4. **Preserve exact immutable identity**
   - frozen/released objects use exact source/tree/content identity;
   - branch recency is not frozen identity.

5. **Preserve unresolved variation**
   - summary may compress prose;
   - it may not silently erase materially distinct HOW, failure, Host, evidence, or decision branches whose equivalence is unproven.

6. **Create/update the current handoff record**
   - project state;
   - recent decision-bearing conversation context;
   - file catalog;
   - exact next action;
   - forbidden actions;
   - readback/completeness evidence.

7. **Promote reusable lessons out of the record**
   - project-management rule -> `research/handoffs/PROJECT-MANAGEMENT-DISCIPLINE.md`;
   - handoff/takeover rule -> this protocol or `REQUIRED-TAKEOVER-CONTEXT.yaml`;
   - ENA research-method rule -> `research/methodology/`.

8. **Update `CURRENT-HANDOFF.yaml`**
   - point to the latest intended record;
   - explicitly declare mandatory framework and project-methodology context.

9. **Integrate and read back**
   - PR + applicable CI;
   - after merge, read from `main` as a fresh receiver would;
   - verify that pointer, Current, active research, methodology, record, and next action agree.

```text
WRITTEN != HANDOFF_COMPLETE
```

## 4. Incoming session protocol

A new project-manager session must, before substantive work:

1. start from repository `main`;
2. read `PROJECT-HUB.md` and verify `releases/current/CURRENT-BASELINE.yaml`;
3. read `research/handoffs/CURRENT-HANDOFF.yaml`;
4. read **this protocol** and `REQUIRED-TAKEOVER-CONTEXT.yaml`;
5. read `PROJECT-MANAGEMENT-DISCIPLINE.md`;
6. read the mandatory project methodology listed in `REQUIRED-TAKEOVER-CONTEXT.yaml`;
7. read the current handoff record pointed to by `CURRENT-HANDOFF.yaml`;
8. independently reverify live refs, exact frozen/released identities, review state, and Current;
9. read `research/ACTIVE-RESEARCH.yaml`, `research/plans/PROGRESS.yaml`, and the master plan;
10. read recent decision context and only then retrieve deeper evidence/prototypes required by the next action;
11. if current-state surfaces disagree, run the Project State Alignment Gate before substantive work;
12. state the inherited project state, governing methods, and first permitted next action from persisted evidence;
13. continue without asking the user to repeat information already durably available.

The receiver must inherit both **what the project currently says** and **how the project has learned to reason about what to do next**.

```text
READ_STATE_ONLY = INCOMPLETE_TAKEOVER
READ_METHOD_ONLY = INCOMPLETE_TAKEOVER
```

## 5. Required handoff-record contents

A material record normally contains:

- `HANDOFF-START-HERE.md` — shortest instance-specific bootstrap;
- `HANDOFF-MANIFEST.yaml` — machine-readable record identity/pointers;
- `PROJECT-STATE.md` — current-state projection and exact identities;
- `RECENT-THREE-ROUNDS.md` — at least the latest three decision-bearing rounds; older material when still necessary;
- `FILE-CATALOG.md` — instance-specific repository map/read order;
- `HANDOFF-READBACK.md` — integration/readback evidence.

`THREE_ROUNDS` is a minimum continuity window, not a completeness limit.

Do **not** permanently store canonical handoff rules or reusable project-management methodology inside the instance directory.

## 6. Authority hierarchy

When sources disagree, handoff records are maps, not authority.

```text
Current identity
  -> releases/current/CURRENT-BASELINE.yaml

Frozen candidate identity
  -> exact external freeze record + source/tree binding

Active research routing
  -> research/ACTIVE-RESEARCH.yaml on main

Handoff/takeover method
  -> research/handoffs/HANDOFF-PROTOCOL.md

Project-management discipline
  -> research/handoffs/PROJECT-MANAGEMENT-DISCIPLINE.md

Research methodology
  -> research/methodology/ on main

Fast execution state
  -> research/plans/PROGRESS.yaml after alignment

Handoff record
  -> bootstrap projection / lineage

Chat
  -> non-authoritative context
```

## 7. Anti-convergence rule

LLMs often narrate success by summarizing and collapsing detail. Handoff writing may compress representation but may not silently compress decision-relevant possibility space.

```text
COMPRESS_HANDOFF_PROSE = ALLOWED
COMPRESS_UNPROVEN_VARIATION = NOT_ALLOWED
```

Canonical project method:

`research/methodology/CONVERGENCE-DIVERGENCE-DISCIPLINE.md`

## 8. Completeness test

A handoff is not ready unless a fresh receiver can answer from persisted sources:

- What is Current?
- What project phase is actually active?
- Which exact object is frozen/released/current?
- Which branch is continuation authority?
- What changed recently and why?
- What is the exact next action?
- What is forbidden now?
- Which unresolved branches may still change the decision?
- Which project methodology governs the next work?
- Which handoff/takeover rules govern succession itself?
- Which project-management lessons must remain salient?
- Where are the supporting files/evidence?

If the receiver must ask the user to reconstruct these, succession failed.

## 9. Normal lifecycle rule

Session replacement is normal maintenance, not an exceptional recovery event.

> A healthy ENA project survives loss of the current conversational context without losing project state, project method, project-management discipline, authority boundaries, or decision lineage.
