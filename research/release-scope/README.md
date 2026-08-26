# ENA Release Scope Workspace

Status: `SCOPE_STABLE / V0.3.7_ASSIGNED / CANDIDATE_BUILD_PREPARATION / CURRENT_UNCHANGED`

This directory records how Operational Architecture research was selected into the next candidate line without modifying `releases/current/`.

Current remains:

`v0.3.6 / CURRENT / FIELD_VALIDATION`

Next candidate line:

`v0.3.7 / NOT_CURRENT / CANDIDATE_NOT_YET_CREATED`

## Read in order

1. `RELEASE-SCOPE-ENTRY-GATE-001.md` — Operational Architecture was deep/traversable enough to begin release selection.
2. `RELEASE-SCOPE-RECONCILIATION-001.md` — first practical cargo pass.
3. `RELEASE-TOOLING-RECONCILIATION-001.md` — minimal v2 helper selected; legacy v1.2 is compatibility/lineage only.
4. `REFERENCE-LIBRARY-SELECTION-001.md` — selected optional reference library and deferred Commitment/Settlement reconstruction.
5. `CANDIDATE-SURFACE-DESIGN-001.md` — minimal inhabitable candidate package.
6. `CANDIDATE-REFERENCE-MANIFEST-DRAFT.yaml` — machine-readable optional-reference packaging draft.
7. `LANGUAGE-SCOPE-001.md` — selected zh-CN operational/HOW coverage.
8. `ANTI-ABLATION-SELECTION-AUDIT-001.md` — confirms unselected HOWs remain durably routed rather than silently erased.
9. `RELEASE-SCOPE-STABILITY-GATE-001.md` — concludes remaining open items are candidate implementation/evidence issues, not cargo-selection blockers.
10. `VERSION-SELECTION-001.md` — assigns `v0.3.7` using repository release-history precedent.

## Stable v0.3.7 release thesis

```text
STABLE_v0.3.6_SEMANTIC_TRUNK
+
ADOPTER_FACING_OPERATIONAL_ARCHITECTURE
+
OPTIONAL_REFERENCE_LIBRARY
+
MINIMAL_V2_PRACTICAL_TOOLING
+
ZH_CN_OPERATIONAL_PROJECTION
```

No new Constitution/Core rule has been demonstrated necessary.

```text
NEW_CONSTITUTION_RULE_REQUIRED = 0_DEMONSTRATED
NEW_CORE_SEMANTIC_DELTA_REQUIRED = 0_DEMONSTRATED
OPERATIONAL_ADOPTER_DELTA = MATERIAL_AND_SELECTED
```

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

Deferred first candidate:

```text
Commitment/Settlement recovered reconstruction
```

Deferred does not mean retired or disproven.

## Selected tooling

```text
candidate default practical path = minimal v2-compatible helper
legacy ena_evolve.py v1.2 = explicit legacy/compatibility only
narrow legacy repair = not selected as primary answer
```

## Next phase

Release-scope ideation is no longer the default activity.

Before creating candidate.0:

1. read branch governance;
2. read Current release discipline and prior v0.3.6 candidate/freeze mechanics;
3. align the main-visible project control plane to the candidate-build phase;
4. create a self-contained `v0.3.7 candidate.0` workspace without touching `releases/current/`;
5. validate/freeze/falsify/reconcile under exact candidate identity.

Reopen release scope only for a scope-level contradiction or genuinely new candidate-critical evidence.

`CURRENT_CHANGE = NO`
