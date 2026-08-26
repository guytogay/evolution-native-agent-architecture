# ENA Research — Start Here

Status: `ACTIVE_RESEARCH_BOOTSTRAP / HOT_ENTRYPOINT / NON_NORMATIVE / NOT_RELEASE_AUTHORITY`

This file is the fast-moving bootstrap **inside the active research integration branch**.

The canonical project/research control plane lives on `main`. A successor session should discover this branch from `main`; it should not discover `main` from this branch.

```text
MAIN CONTROL PLANE
-> research/ACTIVE-RESEARCH.yaml
-> research/ena-reconstruction
-> this file / PROGRESS.yaml
```

```text
BOOTSTRAP != COMPLETE_RESEARCH_STATE
HOT_ENTRYPOINT != ONTOLOGY
BRANCH_NAME != BRANCH_AUTHORITY
OPEN_PR != ACTIVE_BRANCH_AUTHORITY
```

## Required continuation order

Before substantive ENA continuation:

1. Start from the repository default branch `main` and read `PROJECT-HUB.md`.
2. Verify actual Current from `releases/current/CURRENT-BASELINE.yaml` on `main`.
3. Read `research/ACTIVE-RESEARCH.yaml` on `main` and verify that it still designates `research/ena-reconstruction` as the active research integration branch. An open PR is not required for branch authority.
4. Read `research/methodology/README.md`, `research/methodology/ENA-RESEARCH-DISCIPLINE.md`, and relevant focused methodology on `main`.
5. Check whether a material project transition occurred since the last aligned checkpoint. If so, run `research/methodology/PROJECT-STATE-ALIGNMENT-GATE.md` before substantive work.
6. On this active branch, read `research/plans/PROGRESS.yaml` for fast-moving execution state.
7. Read the durable master plan from `research/plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md` on `main`.
8. Read #89 and only the relevant #90–#94 workstream/prototype/evidence for the task at hand.
9. Retrieve PR #82, PR #101, the deleted `research/memory-metabolism-prototype` branch name, or other historical artifacts only when lineage/provenance makes them decision-relevant.
10. When looking for a practical HOW, inspect `research/external-how/SOURCE-REGISTRY.md` on this active branch and perform fresh external research when the map is insufficient or stale.
11. If a prior session export contains material work not yet mapped into GitHub, retrieve only the decision/method-bearing parts needed to repair the durable project state.

Before writing, reverify the live head of `research/ena-reconstruction`. Discover an open PR by head branch only when review/integration context is needed.

Only after this routing should a research node select substantive work.

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
4. record the reason in the main methodology changelog;
5. run the Project State Alignment Gate before resuming substantive work if the method change also affects routing, plan, progress, or project state.

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
Has a material project transition occurred that requires the alignment gate before I resume?
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

A new session that can quote the latest branch topology but continues from stale plan/progress/current-state references has not inherited the project state operationally.

## Record-first continuity

After material progress:

- update `research/plans/PROGRESS.yaml` on this active branch;
- update relevant reconstruction/prototype/Issue evidence;
- add external mechanisms under `research/external-how/` when they change the HOW possibility space;
- if the research method itself changes, capture the evidence here and reconcile the durable methodology update to `main`;
- if active branch identity/routing changes, update `main/research/ACTIVE-RESEARCH.yaml` before retiring the old active surface;
- after a material project transition, complete and record the Project State Alignment Gate before substantive work resumes.

A handoff summary is a pointer, not project state.

## Final inheritance test

Before claiming successful inheritance, a successor should be able to state from persisted sources:

- what Current actually is;
- which branch main currently designates as active research;
- where canonical methodology lives;
- whether a project-state alignment pass is required or complete;
- what phase the reconstruction-to-release plan is in;
- where active fast-moving progress and external HOW research live;
- which old branch/PR references are lineage only;
- and what next action is permitted without silently dissolving historical variation.

> **Do not merely inherit conclusions. Inherit the method that governs how new conclusions may be produced.**
