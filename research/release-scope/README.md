# ENA Release Scope Workspace

Status: `ACTIVE_RELEASE_SCOPE_RECONCILIATION / RESEARCH_ONLY / CURRENT_UNCHANGED / VERSION_UNASSIGNED`

This directory is the transition surface between Operational Architecture assembly and a future release candidate.

It does **not** authorize changes to `releases/current/`.

## Start here

1. `RELEASE-SCOPE-ENTRY-GATE-001.md` — confirms the Operational Architecture is traversable enough to begin release selection.
2. `RELEASE-SCOPE-RECONCILIATION-001.md` — first practical cargo pass and working package hypothesis.
3. `RELEASE-TOOLING-RECONCILIATION-001.md` — selects the minimal v2-compatible helper for the next candidate default tooling path; legacy v1.2 remains explicit legacy/compatibility only.
4. `REFERENCE-LIBRARY-SELECTION-001.md` — selects the general and advanced/specialized optional reference set and records deferred branches.
5. `../plans/PROGRESS.yaml` — current fast-moving phase state.
6. `../operational-architecture/` — source assembly and concrete HOW branches.
7. `../plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md` — long-horizon phase discipline.

## Selection is not compression back to one HOW

Release reconciliation asks what should be distributed to adopters, not which single HOW is metaphysically correct.

One operational node may produce multiple release dispositions:

```text
CURRENT_SEMANTIC_ANCHOR
ADOPTER_GUIDANCE_CANDIDATE
GENERAL_OPTIONAL_REFERENCE
ADVANCED_OPTIONAL_REFERENCE
SPECIALIZED_OPTIONAL_REFERENCE
HOST_ADAPTER_PATTERN
FIELD_OR_MESOCOSM_ONLY
MAINTENANCE_TOOLING_CANDIDATE
RESEARCH_EXPERIMENTAL
DORMANT_LINEAGE
SEMANTIC_DELTA_CANDIDATE
```

These labels are working routing/packaging classes, not ontology.

## Critical release question

```text
NO_NEW_CORE_RULES
!=
NO_RELEASE_VALUE
```

A release may improve practical inhabitability through concrete HOW navigation, optional reference organs, Host patterns, tooling repair, and adopter guidance without expanding the Constitution.

Conversely, a large research tree does not itself justify shipping everything.

## Current selected shape

Adopter-facing candidate cargo currently includes:

- Operational Architecture entrypoint;
- cue index;
- cold HOW map;
- release-local reference pointer/index;
- bounded procedures and Commons patterns;
- curated Memory Metabolism guidance.

Selected general optional machine references:

```text
Retrieval Obligation 0.5
WAIT
Authority Lease
Effect Lifecycle
Recovery Adapter
```

Selected advanced/specialized optional references:

```text
Evidence Envelope
Evidence Dependency Map
Contested Authorship
```

Deferred from first candidate machine-reference library:

```text
Commitment/Settlement recovered reconstruction
```

The deferred branch remains live research lineage and may still inform HOW guidance.

Selected tooling direction:

```text
minimal v2-compatible evolution helper = candidate default practical path
legacy ena_evolve.py v1.2 = explicit legacy/compatibility only
narrow legacy repair = not selected as primary answer
```

## Remaining scope work before version assignment

- define the exact release-local operational/package surface;
- make reference optionality sufficiently explicit/machine-readable;
- decide zh-CN coverage and semantic fixtures for new hot/entry surfaces;
- decide which existing Current top-level files require material change vs a pointer to the new operational library;
- run anti-ablation selection audit across selected/deferred/research HOWs;
- confirm no remaining scope question can materially change candidate cargo.

Only after those decisions stabilize should a version number be assigned.

## Current boundary

Current remains:

```text
v0.3.6 / CURRENT / FIELD_VALIDATION
```

`CURRENT_CHANGE = NO`
