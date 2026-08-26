# ENA Research — Start Here

Status: `RESEARCH_BOOTSTRAP / HOT_ENTRYPOINT / NON_NORMATIVE / NOT_RELEASE_AUTHORITY`

Purpose: give a fresh research session the **smallest sufficient entrypoint** for continuing ENA without reconstructing the research method and project state from hundreds of commits, Issues, comments, or prior chat exports.

This file is a retrieval/bootstrap surface, not a compressed replacement for research history, methodology, or the master plan.

```text
BOOTSTRAP != COMPLETE_RESEARCH_STATE
HOT_ENTRYPOINT != ONTOLOGY
POINTER != SUBSTITUTE_FOR_COLD_SOURCE
```

## Required read order before substantive ENA continuation

1. Verify actual Current from `releases/current/CURRENT-BASELINE.yaml` on the default branch. Never trust a version hard-coded in old research material.
2. Read `research/methodology/README.md`.
3. Read `research/methodology/ENA-RESEARCH-DISCIPLINE.md`.
4. Read `research/methodology/HOW-GROWTH-DISCIPLINE.md` and any other method file relevant to the planned action.
5. Read `research/plans/PROGRESS.yaml` for current project execution state.
6. Read `research/plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md` for the durable end-to-end plan.
7. Read PR #82 and #89; then only the relevant #90–#94 workstream/prototype/evidence.
8. When looking for a practical HOW, inspect `research/external-how/SOURCE-REGISTRY.md` and perform fresh external research if the current source map is insufficient or stale.
9. If inheriting from a prior ChatGPT/session export and recent methodology changed near its end, read the methodology/decision-bearing tail rather than relying only on a compressed handoff summary.

Only after these reads should a new research node select substantive work.

## Current research posture

The reconstruction is not primarily a search for more abstract Constitution prose.

The working structural direction is:

```text
TELOS / PURPOSE
      |
      v
WHAT / WHY        <- semantic trunk; abstraction/compression may be useful
      |
      +--> HOW-A  <- concrete organ/process/tool/procedure
      |     +--> Host binding / adapter
      |     +--> failure/fallback behavior
      |     +--> branch-scoped evidence
      |
      +--> HOW-B  <- materially different concrete path
      |
      +--> HOW-C  <- Host-conditional / experimental path
      |
      +--> ...
```

Key constraints:

```text
PROPERTY != ORGAN != HOST_BINDING != EVIDENCE != ADOPTION
ONE_WHAT_WHY -> 0..N_CONCRETE_HOW_BRANCHES
REQUESTED_N != DISCOVERED_N
CURRENT_CATEGORY_SET != ONTOLOGY
PROTOTYPED != MORE_FUNDAMENTAL
UNPROTOTYPED != UNIMPORTANT
UNSELECTED != ABSENT
```

> **Compress the semantic trunk; let concrete HOWs branch.**

The number, depth, and boundary of HOW branches are research results, not directory slots.

## Reconstruction-phase discipline

During anti-ablation reconstruction:

```text
RECOVER VARIATION
-> preserve durable lineage
-> reconstruct WHAT / WHY / HOW / EVIDENCE
-> search external HOWs where internal mechanisms are insufficient
-> only then select, merge, retire, specialize, or promote where justified
```

Do not choose the "most important next organ" merely because it is already visible, prototyped, or easy to engineer. That creates selection-induced ablation of less visible historical HOWs.

A better new organ does not erase old HOW lineage. Evidence-backed retirement is allowed; silent dissolution is not.

## External HOW rule

ENA does not need to invent every practical organ.

Search current AI frameworks, AI memory systems, durable workflow systems, agent protocols, research organizations, developer communities, and adjacent engineering domains for concrete mechanisms.

Map them before selecting them:

```text
EXTERNAL_MECHANISM
+ ENA_FAILURE_MAPPING
+ HOST_CONDITIONS
-> CANDIDATE_HOW
```

```text
POPULAR != CORRECT
VENDOR_CLAIM != INDEPENDENT_EVIDENCE
ANALOGY != ARCHITECTURAL_NECESSITY
```

External harvesting is persisted under `research/external-how/`.

## Research action gate

Before a substantial action, verify at least:

```text
Am I explaining a problem or solving it?
Am I treating a parent property as proof that a concrete problem is solved?
Am I preserving plural/Host-specific/failed/dormant HOW lineage?
Am I selecting before enough variation has been recovered for this decision?
Am I freezing a convenient count, taxonomy, or organ boundary into ontology?
If I call something a HOW, can a fresh Agent actually perform or instantiate it?
Have I checked whether a mature external mechanism already solves part of this problem?
Can the proposed experiment reveal structure that cannot already be derived statically?
What exact decision could the next evidence change?
Could NO_CHANGE, dormancy, simplification, or multiple coexisting HOWs be correct?
```

The checklist is open-cardinality. The canonical working methodology is the methodology directory, not this abbreviated bootstrap.

## Evidence activation check

A research method being written somewhere is not enough:

```text
WRITTEN -> RETRIEVED -> INTERPRETED -> SALIENT -> APPLIED
```

For session inheritance, explicitly distinguish:

```text
DURABLE != DISCOVERABLE
DISCOVERABLE != RETRIEVED
RETRIEVED != SALIENT
SALIENT != APPLIED
```

A new session that can quote methodology but immediately performs a forbidden compression/selection has **not inherited the methodology operationally**.

## Record-first continuity

After material progress:

- update `research/plans/PROGRESS.yaml`;
- update `research/methodology/METHOD-CHANGELOG.md` only if research method changed materially;
- update relevant reconstruction/prototype/Issue evidence;
- add external mechanisms to `research/external-how/` when they change the candidate HOW space;
- update this bootstrap only when routing changes.

A handoff summary is a pointer, not the project state.

## Final inheritance test

Before claiming a new session has successfully inherited ENA research, it should be able to state from persisted sources rather than memory alone:

- what Current actually is;
- what phase the reconstruction-to-release plan is in;
- why WHAT/WHY coverage does not imply practical closure;
- why HOW is open-cardinality and may branch into multiple concrete mechanisms;
- why #90–#94 and directory categories are organizational shelves rather than ontology;
- where the full research methodology lives;
- where current progress and the master plan live;
- where external candidate HOWs are recorded;
- what next action is permitted without silently dissolving historical variation.

> **Do not merely inherit conclusions. Inherit the method that governs how new conclusions may be produced.**
