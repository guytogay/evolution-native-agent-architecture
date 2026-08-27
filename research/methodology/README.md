# ENA Research Methodology

Status: `CANONICAL_PROJECT_RESEARCH_METHOD_SURFACE / MAIN_VISIBLE / OPEN_CARDINALITY / NON_NORMATIVE_TO_CURRENT`

This directory is the stable home for **how ENA itself is researched**.

It is project process, not adopter-facing ENA Constitution semantics and not the canonical session-handoff framework.

Session succession now lives under:

`research/handoffs/`

Canonical succession method:

`research/handoffs/HANDOFF-PROTOCOL.md`

Mandatory takeover context:

`research/handoffs/REQUIRED-TAKEOVER-CONTEXT.yaml`

This separation is intentional:

```text
HANDOFF FRAMEWORK = how operators exchange project responsibility
PROJECT METHODOLOGY = how ENA research itself is performed
HANDOFF RECORD = one time-bounded succession occurrence
```

A successor must inherit both framework and methodology.

## Canonical rule

The main-visible methodology is the research-control reference for session inheritance.

Fast-moving active research may contain newer observations, but a material method change that should govern future work must be reconciled to canonical methodology on `main` and recorded in the method changelog.

```text
CHAT_INSIGHT != DURABLE_METHOD
ACTIVE_BRANCH_NOTE != CANONICAL_METHOD
METHOD_WRITTEN != METHOD_APPLIED
```

## Read order

1. `ENA-RESEARCH-DISCIPLINE.md` — open-cardinality master method ledger.
2. `CONVERGENCE-DIVERGENCE-DISCIPLINE.md` — when abstraction/compression is valid and when HOW/failure/Host variation must remain open or grow.
3. `PROJECT-STATE-ALIGNMENT-GATE.md` — realign routing, method, plan, progress, candidate/release state, and next actions after material transitions.
4. `METHOD-CHANGELOG.md` — why significant method corrections were introduced.
5. `incidents/` — concrete method failures that changed future behavior.
6. `../BRANCH-GOVERNANCE.md` — research/candidate topology across sessions.
7. `../ACTIVE-RESEARCH.yaml` — active research routing.
8. `../handoffs/CURRENT-HANDOFF.yaml` — current succession pointer.
9. `../handoffs/HANDOFF-PROTOCOL.md` — outgoing/incoming succession rules.
10. `../handoffs/REQUIRED-TAKEOVER-CONTEXT.yaml` — explicit mandatory inheritance context.

Focused methodology files may be added when a distinction changes behavior; file count is not a completeness claim.

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

## Project-state alignment rule

Durable files can all be locally reasonable yet collectively stale after a material transition.

```text
INDIVIDUAL_FILE_CORRECT != PROJECT_STATE_COHERENT
MATERIAL_TRANSITION -> ALIGN -> RESUME
```

Use `PROJECT-STATE-ALIGNMENT-GATE.md` when a handoff, branch transition, directory/method change, candidate/release-state change, or plan change can make current-state surfaces disagree.

The gate is not ceremony after every ordinary content commit.

## Update discipline

When research reveals a new method defect or stronger discipline:

1. capture triggering evidence/incident durably;
2. determine whether the lesson changes research behavior rather than wording;
3. update the master ledger or add a focused method;
4. record why in `METHOD-CHANGELOG.md`;
5. update project-control pointers only when routing/phase changes;
6. run alignment when the change materially affects current-state coherence;
7. do not force the method into an existing category merely to keep the list short;
8. do not split methods merely to make the directory look comprehensive.

```text
CURRENT_METHOD_SET != COMPLETE_METHOD_SPACE
METHOD_FILE_COUNT != METHODOLOGY_COMPLETENESS
```

## Inheritance test

A successor has not inherited the method merely because it can quote it.

```text
WRITTEN -> RETRIEVED -> INTERPRETED -> SALIENT -> APPLIED
```

If it reads anti-dissolution/plural-HOW discipline and then immediately compresses the work into one abstract mechanism or selects before recovery, inheritance failed.

If it treats a smaller assertion/file/category count as success without proving behavioral equivalence, inheritance failed.

If it reads project state but skips the handoff framework or project methodology, takeover failed.

If it reads a new branch/control-plane state but continues from stale routing or superseded plan, project-state inheritance failed.

> **Do not merely inherit conclusions. Inherit the method that governs how new conclusions may be produced.**
