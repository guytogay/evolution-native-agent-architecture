# ENA Release Scope Workspace

Status: `RELEASE_SCOPE_RECONCILIATION_WORKSPACE / RESEARCH_ONLY / CURRENT_UNCHANGED / VERSION_UNASSIGNED`

This directory is the transition surface between Operational Architecture assembly and a future release candidate.

It does **not** authorize changes to `releases/current/`.

## Start here

1. `RELEASE-SCOPE-ENTRY-GATE-001.md` — determines whether Operational Architecture is traversable enough to begin release-scope selection.
2. Future reconciliation records in this directory — classify what should ship, what remains optional/reference/Host-specific/research, and what is an actual semantic delta.
3. `../operational-architecture/` — source assembly and concrete HOW branches.
4. `../plans/PROGRESS.yaml` — current fast-moving phase state.
5. `../plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md` — long-horizon phase discipline.

## Selection is not compression back to one HOW

Release reconciliation asks what should be distributed to adopters, not which single HOW is metaphysically correct.

One operational node may produce multiple release dispositions:

```text
CURRENT_SEMANTIC_ANCHOR
ADOPTER_GUIDANCE_CANDIDATE
REFERENCE_ORGAN_CANDIDATE
HOST_ADAPTER_PATTERN
FIELD_OR_MESOCOSM_ONLY
MAINTENANCE_TOOLING_CANDIDATE
RESEARCH_EXPERIMENTAL
DORMANT_LINEAGE
SEMANTIC_DELTA_CANDIDATE
```

These labels are working routing classes, not ontology.

## Critical release question

```text
NO_NEW_CORE_RULES
!=
NO_RELEASE_VALUE
```

A release may improve practical inhabitability through concrete HOW navigation, optional reference organs, Host patterns, tooling repair, and adopter guidance without expanding the Constitution.

Conversely, a large research tree does not itself justify shipping everything.

## Current boundary

Current remains:

```text
v0.3.6 / CURRENT / FIELD_VALIDATION
```

The next version remains unassigned until release scope stabilizes.

`CURRENT_CHANGE = NO`
