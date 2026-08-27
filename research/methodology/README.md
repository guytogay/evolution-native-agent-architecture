# ENA Research Methodology

Status: `CANONICAL_PROJECT_RESEARCH_METHOD_SURFACE / MAIN_VISIBLE / OPEN_CARDINALITY / NON_NORMATIVE_TO_CURRENT`

This directory is the stable home for **how ENA itself is researched**.

It is project process, not adopter-facing ENA Constitution semantics.

A future session should not reconstruct the research method from old chat, Issue comments, branch names, old PR numbers, or whichever prototype is most visible.

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
2. `CONVERGENCE-DIVERGENCE-DISCIPLINE.md` — guard against LLM-style premature summary/convergence that silently compresses HOW, failure, Host, or evidence variation.
3. `PROJECT-STATE-ALIGNMENT-GATE.md` — how to realign routing, method, plan, and progress after material project transitions before substantive work resumes.
4. `METHOD-CHANGELOG.md` — why significant method corrections were introduced.
5. `../BRANCH-GOVERNANCE.md` — how research topology is controlled across sessions.
6. `../ACTIVE-RESEARCH.yaml` — where the active work actually lives now.

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

## Convergence/divergence guard

LLMs often express progress by summarizing, consolidating, and reducing visible complexity. In ENA this is safe only when the change compresses representation rather than silently shrinking the decision-relevant possibility space.

```text
COMPRESS REPRESENTATION != COMPRESS POSSIBILITY SPACE
PROVEN_BEHAVIORAL_EQUIVALENCE -> MAY_COMPRESS
UNPROVEN_EQUIVALENCE -> DO_NOT_COLLAPSE
UNKNOWN_SPACE -> EXPAND
```

HOW branches, adversarial/failure shapes, Host-specific mechanisms, evidence-applicability conditions, and unresolved/dormant alternatives should remain distinct until equivalence, replacement, or retirement is actually evidenced.

Before replacing a larger surface with a smaller abstraction, use `CONVERGENCE-DIVERGENCE-DISCIPLINE.md` to account for what was preserved, merged, replaced, retired, lost, or remains unknown.

## Project-state alignment rule

Durable files can all be locally reasonable yet collectively stale after a material handoff, branch transition, directory change, method change, release-state change, or plan change.

```text
INDIVIDUAL_FILE_CORRECT != PROJECT_STATE_COHERENT
MATERIAL_TRANSITION -> ALIGN -> RESUME
```

A successor/resuming session should check whether such a transition occurred. When it did, run `PROJECT-STATE-ALIGNMENT-GATE.md` before selecting substantive research work.

The gate is not ceremony after every ordinary commit. It is a continuity repair mechanism for transitions capable of making current-state surfaces disagree.

## Update discipline

When research reveals a new method defect or stronger discipline:

1. capture the triggering evidence/incident durably;
2. determine whether the new lesson changes research behavior rather than merely wording;
3. update the master ledger or add a focused method file;
4. record why in `METHOD-CHANGELOG.md`;
5. update `research/ACTIVE-RESEARCH.yaml` or other project-control pointers only when routing changes;
6. run the project-state alignment gate when the change is material enough to affect routing, plan, progress, release state, or future-session continuation;
7. do not force the method into an existing category merely to keep the list short;
8. do not split methods merely to make the directory look comprehensive.

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

If it reads convergence/divergence discipline and then treats a smaller summary, harness, category set, or branch inventory as intrinsically superior without a variation-disposition map, inheritance failed at the anti-convergence layer.

If it reads a new branch/control-plane state but continues from stale routing or a superseded plan, inheritance failed at the project-state alignment layer.

> **Do not merely inherit conclusions. Inherit the method that governs how new conclusions may be produced.**
