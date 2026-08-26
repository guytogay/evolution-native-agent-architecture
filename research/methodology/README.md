# ENA Research Methodology

Status: `CANONICAL_PROJECT_RESEARCH_METHOD_SURFACE / MAIN_VISIBLE / OPEN_CARDINALITY / NON_NORMATIVE_TO_CURRENT`

This directory is the stable home for **how ENA itself is researched**.

It is project process, not adopter-facing ENA Constitution semantics.

A future session should not reconstruct the research method from old chat, Issue comments, branch names, or whichever prototype is most visible.

## Canonical rule

The main-visible methodology is the research-control reference for session inheritance.

Fast-moving active research may contain newer method observations, but a material method change that should govern future sessions must be reconciled back into this directory on `main` and recorded in the method changelog.

```text
CHAT_INSIGHT != DURABLE_METHOD
ACTIVE_BRANCH_NOTE != CANONICAL_METHOD
METHOD_WRITTEN != METHOD_APPLIED
```

## Read order

1. `ENA-RESEARCH-DISCIPLINE.md` — open-cardinality master method ledger.
2. `METHOD-CHANGELOG.md` — why significant method corrections were introduced.
3. `../BRANCH-GOVERNANCE.md` — how research topology is controlled across sessions.
4. `../ACTIVE-RESEARCH.yaml` — where the active work actually lives now.

Focused methodology files may be added when a distinction is important enough to change behavior; the file count is not a completeness claim.

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

## Update discipline

When research reveals a new method defect or stronger discipline:

1. capture the triggering evidence/incident durably;
2. determine whether the new lesson changes research behavior rather than merely wording;
3. update the master ledger or add a focused method file;
4. record why in `METHOD-CHANGELOG.md`;
5. update `research/ACTIVE-RESEARCH.yaml` or other project-control pointers only when routing changes;
6. do not force the method into an existing category merely to keep the list short;
7. do not split methods merely to make the directory look comprehensive.

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

> **Do not merely inherit conclusions. Inherit the method that governs how new conclusions may be produced.**
