# ENA Research Methodology — Project State Alignment Gate

Status: `CANONICAL_FOCUSED_METHOD / CONTINUITY_ALIGNMENT / NON_NORMATIVE_TO_CURRENT`

Purpose: prevent individually correct project documents from drifting into a collectively inconsistent project state after a material transition.

```text
INDIVIDUAL_FILE_CORRECT != PROJECT_STATE_COHERENT
MATERIAL_TRANSITION -> ALIGN -> RESUME
HISTORY_PRESERVED != HISTORY_USED_AS_CURRENT_POINTER
```

This method is about maintaining ENA, not an adopter-facing Constitution rule.

## Default topology after the 2026-09 simplification

ENA no longer requires a permanent fast-moving research integration branch.

Normal live topology is:

```text
main / NOW.md
-> relevant Issue or artifact
-> short-lived main-based branch only when review/isolation is useful
-> merge durable result to main
```

The older `main + research/ena-reconstruction` topology remains valid historical lineage but is no longer the default live project model.

## Why alignment still matters

Material transitions can still leave different live surfaces describing different generations of the project:

```text
phase/method/release/topology transition
-> one live pointer changes
-> another live guide still describes the previous state
-> successor receives a mixed map
-> work drifts before the real research starts
```

Alignment fixes **live routing**, not historical prose.

## Trigger conditions

Run a focused alignment pass after changes that can alter current routing, authority, method, or phase, such as:

- `NOW.md` phase/next-action transition;
- Current/candidate/release identity change;
- branch-governance model change;
- retirement/creation of a long-lived compatibility pointer;
- directory/information-architecture change moving live entrypoints;
- material research-method correction;
- deep session succession following any of the above;
- discovery that two live control surfaces disagree.

Do **not** run full alignment after every ordinary research edit.

## Alignment surfaces

Check only surfaces that can still affect the current decision.

### 1. Live project state

- `NOW.md`
- relevant Issue/artifact
- actual `main` head before writes
- `releases/current/CURRENT-BASELINE.yaml` when Current identity matters

### 2. Compatibility/control routing when changed

- `PROJECT-HUB.md`
- `research/ACTIVE-RESEARCH.yaml`
- `research/BRANCH-GOVERNANCE.md`
- `research/BRANCH-INVENTORY.yaml`
- `research/handoffs/CURRENT-HANDOFF.yaml` for deep succession

These files may exist partly for historical compatibility. They must route correctly but need not duplicate NOW.

### 3. Research method when method changed

- `research/methodology/README.md`
- `research/methodology/ENA-RESEARCH-DISCIPLINE.md`
- the focused method actually implicated by the transition

Do not reread every methodology file when one local rule changed.

### 4. Historical plans/progress

Retrieve old plan/progress files only when they can change the current decision or explain lineage.

They are no longer mandatory hot project-control surfaces merely because they exist.

### 5. Branch cleanup

When retiring branches:

```text
inspect unique content
-> preserve decision-relevant material
-> verify durable carrier
-> delete ref
```

Do not merge an old diverged branch wholesale simply to avoid losing one useful file.

## Closure condition

Alignment is complete when a fresh successor can determine, without contradictory live guidance:

- what Current is, if relevant;
- what project phase is active;
- where the live status lives;
- what the next consequential action is;
- which historical refs are only lineage;
- what is explicitly not authorized yet.

For the current project generation, the expected answer is normally:

```text
continuation = main + NOW.md
work branch = short-lived if needed
Current = releases/current/ declared baseline
history = retrieve only when decision-changing
```

## Non-goals

Alignment is not:

- a full repository audit;
- automatic handoff-package regeneration;
- rewriting truthful historical records;
- forcing all research files into a new schema;
- proving architecture completeness;
- authorizing a release.

```text
ALIGNMENT_GATE != FULL_PROJECT_REVIEW_FROM_ZERO
ALIGNMENT_COMPLETE != RESEARCH_COMPLETE
ALIGNMENT_COMPLETE != RELEASE_AUTHORIZED
```

> **Keep the live map coherent; leave the forest's history intact.**
