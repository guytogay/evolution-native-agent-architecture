# ENA Release Scope Workspace

Status: `ACTIVE_RELEASE_SCOPE_RECONCILIATION / CARGO_DECISIONS_MADE / SCOPE_STABILITY_GATE_NEXT / CURRENT_UNCHANGED / VERSION_UNASSIGNED`

This directory is the transition surface between Operational Architecture assembly and a future release candidate.

It does **not** authorize changes to `releases/current/`.

## Start here

1. `RELEASE-SCOPE-ENTRY-GATE-001.md` — Operational Architecture is traversable enough to begin release selection.
2. `RELEASE-SCOPE-RECONCILIATION-001.md` — first practical cargo pass.
3. `RELEASE-TOOLING-RECONCILIATION-001.md` — minimal v2 helper selected for candidate default tooling; legacy v1.2 is explicit compatibility/lineage only.
4. `REFERENCE-LIBRARY-SELECTION-001.md` — selected general and advanced/specialized optional reference set; Commitment/Settlement recovered reconstruction deferred.
5. `CANDIDATE-SURFACE-DESIGN-001.md` — working minimal inhabitable candidate package and top-level delta matrix.
6. `CANDIDATE-REFERENCE-MANIFEST-DRAFT.yaml` — machine-readable draft for reference optionality/applicability packaging roles.
7. `LANGUAGE-SCOPE-001.md` — selected zh-CN projection scope for new operational HOW surfaces and reference semantic guide.
8. `ANTI-ABLATION-SELECTION-AUDIT-001.md` — verifies current first-candidate selection does not silently dissolve unselected HOW branches.
9. `../plans/PROGRESS.yaml` — current fast-moving state.
10. `../operational-architecture/` — source assembly and concrete HOW branches.

## Current release thesis

The next release is being shaped as an **operational architecture release**, not a constitutional expansion.

At the current scope checkpoint:

```text
NEW_CONSTITUTION_RULE_REQUIRED = 0_DEMONSTRATED
NEW_CORE_SEMANTIC_DELTA_REQUIRED = 0_DEMONSTRATED
PRACTICAL_ADOPTER_DELTA = MATERIAL_SELECTED
REFERENCE_LIBRARY_DELTA = MATERIAL_SELECTED
TOOLING_DELTA = MATERIAL_SELECTED
LANGUAGE/ADOPTION_DELTA = MATERIAL_SELECTED
NEXT_VERSION = UNASSIGNED_PENDING_SCOPE_STABILITY_GATE
CURRENT_CHANGE = NO
```

## Selection is not compression back to one HOW

Release reconciliation asks what should be distributed to adopters, not which single HOW is metaphysically correct.

Working packaging roles include:

```text
CURRENT_SEMANTIC_ANCHOR
ADOPTER_GUIDANCE
GENERAL_OPTIONAL_REFERENCE
ADVANCED_OPTIONAL_REFERENCE
SPECIALIZED_OPTIONAL_REFERENCE
HOST_ADAPTER_PATTERN
FIELD_OR_MESOCOSM_ONLY
RESEARCH_EXPERIMENTAL
DORMANT_LINEAGE
```

These are routing/packaging classes, not ontology.

## Selected reference set

General optional:

```text
Retrieval Obligation 0.5
WAIT
Authority Lease
Effect Lifecycle
Recovery Adapter
```

Advanced/specialized optional:

```text
Evidence Envelope
Evidence Dependency Map
Contested Authorship
```

Deferred from first candidate machine-reference library:

```text
Commitment/Settlement recovered reconstruction
```

Deferred does not mean retired or disproven.

## Selected tooling direction

```text
minimal v2-compatible evolution helper = candidate default practical path
legacy ena_evolve.py v1.2 = explicit legacy/compatibility only
narrow legacy repair = not selected as primary answer
```

The research helper has passed deterministic and actual CLI round-trip GitHub Actions gates while reusing Current record/packet semantic surfaces rather than duplicating the record semantic engine.

## Candidate surface direction

A new adopter should be able to navigate:

```text
00-READ-ME-FIRST
-> RUNTIME-ADOPTION-KERNEL
-> operational/README
-> operational/CUE-INDEX
-> operational/HOW-MAP
-> procedure / optional reference / Host pattern
-> act / WAIT / UNKNOWN / not-applicable
```

The operational HOW library remains cold by default.

## Language direction

New decision-bearing operational entry/HOW surfaces receive zh-CN semantic projection. Machine schemas/code may keep stable identifiers while a zh-CN reference guide exposes applicability, state meanings, composition and evidence boundaries.

Structural parity remains distinct from behavioral decision equivalence.

## Next gate

Before assigning a version, run a scope-stability gate:

> Is there any remaining open question that can still materially change candidate cargo, rather than only candidate implementation/layout details or validation evidence?

If yes, keep reconciling.

If no, record scope stable, inspect versioning/history, assign the next version, align the main-visible project phase, and begin candidate build under release discipline.

`CURRENT_CHANGE = NO`
