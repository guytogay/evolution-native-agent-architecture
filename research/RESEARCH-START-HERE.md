# ENA Research — Start Here

Status: `ACTIVE_RESEARCH_BOOTSTRAP / HOT_ENTRYPOINT / NON_NORMATIVE / NOT_RELEASE_AUTHORITY`

This file is the fast-moving bootstrap **inside the active research integration branch**.

The canonical project/research control plane now lives on `main`. A successor session should discover this branch from `main`; it should not discover `main` from this branch.

```text
MAIN CONTROL PLANE
-> research/ACTIVE-RESEARCH.yaml
-> ACTIVE RESEARCH BRANCH
-> this file / PROGRESS.yaml
```

```text
BOOTSTRAP != COMPLETE_RESEARCH_STATE
HOT_ENTRYPOINT != ONTOLOGY
BRANCH_NAME != BRANCH_AUTHORITY
```

## Required continuation order

Before substantive ENA continuation:

1. Start from the repository default branch `main`.
2. Read `research/ACTIVE-RESEARCH.yaml` on `main`; verify that it still designates this branch / PR #82 as the active research integration surface.
3. Read `research/methodology/README.md` and `research/methodology/ENA-RESEARCH-DISCIPLINE.md` on `main`. Main is the canonical cross-session methodology/control surface.
4. Read `research/BRANCH-GOVERNANCE.md` on `main` when branch creation, handoff, candidate work, validation isolation, or cleanup is relevant.
5. Verify actual Current from `releases/current/CURRENT-BASELINE.yaml` on `main`.
6. On the active research branch, read `research/plans/PROGRESS.yaml` for fast-moving execution state.
7. Read the durable master plan from `research/plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md` on `main`; active-branch copies/history do not override it.
8. Read PR #82 and #89, then only the relevant #90–#94 workstream/prototype/evidence.
9. When looking for a practical HOW, inspect `research/external-how/SOURCE-REGISTRY.md` on this active branch and perform fresh external research when the map is insufficient or stale.
10. If a prior session export contains material work not yet mapped into GitHub, retrieve only the decision/method-bearing parts needed to repair the durable project state.

Only after this routing should a new research node select substantive work.

## Authority of local methodology copies

This branch contains methodology files produced during reconstruction. They remain useful lineage and may contain candidate refinements, but they are not allowed to become a silent parallel cross-session constitution for research method.

```text
MAIN_METHODOLOGY = CANONICAL_CROSS_SESSION_METHOD
ACTIVE_BRANCH_METHOD_CHANGE = CANDIDATE_UNTIL_RECONCILED_TO_MAIN
```

When this branch discovers a material new research-method lesson:

1. capture the triggering incident/evidence here;
2. use it immediately where needed to avoid repeating a known error;
3. reconcile the durable method change back to `main/research/methodology/`;
4. record the reason in the main methodology changelog.

This avoids methodology drift between long-running research branches and the default project entrypoint.

## Current research posture

The reconstruction is not primarily a search for more abstract Constitution prose.

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
      +--> HOW-B
      +--> HOW-C
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

## Reconstruction-phase discipline

During anti-ablation reconstruction:

```text
RECOVER VARIATION
-> preserve durable lineage
-> reconstruct WHAT / WHY / HOW / EVIDENCE
-> search external HOWs where internal mechanisms are insufficient
-> only then select, merge, retire, specialize, or promote where justified
```

Do not choose the "most important next organ" merely because it is visible, prototyped, or easy to engineer.

A better new organ does not erase old HOW lineage. Evidence-backed retirement is allowed; silent dissolution is not.

## External HOW rule

ENA does not need to invent every practical organ.

Search current AI frameworks, AI memory systems, durable workflow systems, agent protocols, research organizations, developer communities, and adjacent engineering domains for concrete mechanisms.

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

External harvesting is persisted under `research/external-how/` on the active research branch until reconciled/assembled elsewhere.

## Research action gate

Before a substantial action, ask at least:

```text
Am I continuing from the active branch named by main, or from a guessed branch?
Am I explaining a problem or solving it?
Am I treating a parent property as proof that a concrete problem is solved?
Am I preserving plural/Host-specific/failed/dormant HOW lineage?
Am I selecting before enough variation has been recovered for this decision?
Am I freezing a convenient count, taxonomy, organ boundary, or branch layout into ontology?
If I call something a HOW, can a fresh Agent actually perform or instantiate it?
Have I checked whether a mature external mechanism already solves part of this problem?
Can the proposed experiment reveal structure that cannot already be derived statically?
What exact decision could the next evidence change?
Could NO_CHANGE, dormancy, simplification, retirement, or multiple coexisting HOWs be correct?
```

The checklist is open-cardinality. Canonical cross-session methodology is on `main`.

## Evidence activation check

```text
WRITTEN -> RETRIEVED -> INTERPRETED -> SALIENT -> APPLIED
```

```text
DURABLE != DISCOVERABLE
DISCOVERABLE != RETRIEVED
RETRIEVED != SALIENT
SALIENT != APPLIED
```

A new session that can quote methodology but immediately performs forbidden compression/selection has not inherited it operationally.

## Record-first continuity

After material progress:

- update `research/plans/PROGRESS.yaml` on this active branch;
- update relevant reconstruction/prototype/Issue evidence;
- add external mechanisms under `research/external-how/` when they change the HOW possibility space;
- if the research method itself changes, capture the evidence here and reconcile the durable methodology update to `main`;
- if active branch identity/routing changes, update `main/research/ACTIVE-RESEARCH.yaml` before retiring the old active surface.

A handoff summary is a pointer, not project state.

## Final inheritance test

Before claiming successful inheritance, a successor should be able to state from persisted sources:

- what Current actually is;
- which branch/PR main currently designates as active research;
- what phase the reconstruction-to-release plan is in;
- why WHAT/WHY coverage does not imply practical closure;
- why HOW is open-cardinality and may branch into multiple concrete mechanisms;
- where canonical methodology lives;
- where active fast-moving progress and external HOW research live;
- and what next action is permitted without silently dissolving historical variation.

> **Do not merely inherit conclusions. Inherit the method that governs how new conclusions may be produced.**
