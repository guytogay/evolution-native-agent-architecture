# ENA Research Methodology

Status: `CANONICAL_PROJECT_RESEARCH_METHOD_SURFACE / MAIN_VISIBLE / OPEN_CARDINALITY / NON_NORMATIVE_TO_CURRENT`

This directory is the stable home for **how ENA itself is researched and handed between project-manager sessions**.

It is project process, not adopter-facing ENA Constitution semantics.

A future session should not reconstruct the research method from old chat, Issue comments, branch names, old PR numbers, or whichever prototype is most visible.

## Canonical rule

The main-visible methodology is the research-control reference for session inheritance.

Fast-moving active research may contain newer method observations, but a material method change that should govern future sessions must be reconciled back into this directory on `main` and recorded in the method changelog.

```text
CHAT_INSIGHT != DURABLE_METHOD
ACTIVE_BRANCH_NOTE != CANONICAL_METHOD
METHOD_WRITTEN != METHOD_APPLIED
HANDOFF_PACKAGE != PROJECT_AUTHORITY
```

## Read order

1. `ENA-RESEARCH-DISCIPLINE.md` — open-cardinality master method ledger.
2. `SESSION-HANDOFF-DISCIPLINE.md` — how an outgoing session durably hands over and how a new session takes over without reconstructing the project from chat.
3. `CONVERGENCE-DIVERGENCE-DISCIPLINE.md` — when abstraction/compression is valid and when HOW/failure/Host variation must remain open or grow.
4. `PROJECT-STATE-ALIGNMENT-GATE.md` — how to realign routing, method, plan, progress, candidate/release state, and next actions after material transitions.
5. `METHOD-CHANGELOG.md` — why significant method corrections were introduced.
6. `incidents/` — concrete method failures that changed future behavior.
7. `../BRANCH-GOVERNANCE.md` — how research/candidate topology is controlled across sessions.
8. `../ACTIVE-RESEARCH.yaml` — where active research work actually lives now.
9. `../handoffs/CURRENT-HANDOFF.yaml` — latest standardized project-manager/session handoff projection.

Focused methodology files may be added when a distinction is important enough to change behavior; file count is not a completeness claim.

## Core shape

```text
TELOS / PURPOSE
      |
      v
WHAT / WHY
semantic trunk; abstraction/compression may help
      |
      +--> HOW-A
      +--> HOW-B
      +--> HOW-C
      +--> ...
             |
             +--> Host binding / tool / process / protocol
             +--> failure / fallback behavior
             +--> evidence
```

> **Compress the semantic trunk; let concrete HOWs branch.**

And:

```text
COMPRESS REPRESENTATION != COMPRESS POSSIBILITY SPACE
PROVEN_BEHAVIORAL_EQUIVALENCE -> MAY_COMPRESS
UNPROVEN_EQUIVALENCE -> DO_NOT_COLLAPSE
UNKNOWN_SPACE -> EXPAND
```

## Session handoff rule

Project continuity must survive replacement of the current conversational session.

```text
PROJECT_CONTINUITY > SESSION_CONTINUITY
```

An outgoing session persists project state and produces a standardized handoff package under `research/handoffs/`, then updates `research/handoffs/CURRENT-HANDOFF.yaml`.

An incoming session reads the handoff for speed, then independently re-verifies Current, live refs, frozen candidate identities, methodology, Progress, and plan from canonical sources before substantive work.

```text
HANDOFF = BOOTSTRAP MAP
CANONICAL SOURCES + LIVE REFS = TERRAIN
```

## Project-state alignment rule

Durable files can all be locally reasonable yet collectively stale after a material handoff, branch transition, directory change, method change, candidate/release-state change, or plan change.

```text
INDIVIDUAL_FILE_CORRECT != PROJECT_STATE_COHERENT
MATERIAL_TRANSITION -> ALIGN -> RESUME
```

A successor/resuming session should check whether such a transition occurred. When it did, run `PROJECT-STATE-ALIGNMENT-GATE.md` before selecting substantive research work.

The gate is not ceremony after every ordinary content commit. It is a continuity repair mechanism for transitions capable of making current-state surfaces disagree.

## Update discipline

When research reveals a new method defect or stronger discipline:

1. capture the triggering evidence/incident durably;
2. determine whether the new lesson changes research behavior rather than merely wording;
3. update the master ledger or add a focused method file;
4. record why in `METHOD-CHANGELOG.md`;
5. update project-control pointers only when routing/phase changes;
6. run the Project State Alignment Gate when the change is material enough to affect routing, plan, progress, candidate/release state, or future-session continuation;
7. do not force the method into an existing category merely to keep the list short;
8. do not split methods or create duplicate helper files merely to make the directory look comprehensive.

```text
CURRENT_METHOD_SET != COMPLETE_METHOD_SPACE
METHOD_FILE_COUNT != METHODOLOGY_COMPLETENESS
```

## Session inheritance test

A successor has not inherited the method merely because it can quote it.

```text
WRITTEN -> RETRIEVED -> INTERPRETED -> SALIENT -> APPLIED
```

If it reads anti-dissolution/plural-HOW discipline and then immediately compresses the work into one abstract mechanism or selects before recovery, inheritance failed at the salience/application layer.

If it reads the convergence/divergence rule and treats a smaller assertion/file/category count as success without proving behavioral equivalence, inheritance failed.

If it reads a handoff package but does not verify live canonical state, inheritance failed.

If it reads a new branch/control-plane state but continues from stale routing or a superseded plan, inheritance failed at the project-state alignment layer.

> **Do not merely inherit conclusions. Inherit the method that governs how new conclusions may be produced.**
