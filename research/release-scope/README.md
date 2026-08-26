# ENA Release Scope Workspace

Status: `ACTIVE_RELEASE_SCOPE_RECONCILIATION / RESEARCH_ONLY / CURRENT_UNCHANGED / VERSION_UNASSIGNED`

This directory is the transition surface between Operational Architecture assembly and a future release candidate. It does **not** authorize changes to `releases/current/`.

## Start here

1. `RELEASE-SCOPE-ENTRY-GATE-001.md` — why release-scope selection is allowed to begin.
2. `RELEASE-SCOPE-RECONCILIATION-001.md` — first practical cargo pass: adopter guidance, optional references, Host patterns, research-only branches, tooling and language work.
3. `../operational-architecture/README.md` — source HOW tree.
4. `../plans/PROGRESS.yaml` — current fast-moving state.
5. `../plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md` — long-horizon discipline.

## Selection is not semantic compression

Release reconciliation asks what should be distributed to adopters, not which single HOW is universally correct.

Working dispositions include:

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

These are routing classes, not ontology.

## First cargo thesis

```text
NO_NEW_CORE_RULES != NO_RELEASE_VALUE
```

The likely practical release shape now separates:

```text
semantic/adoption trunk
+
optional Operational Architecture guidance
+
selective machine reference library
+
Host adapter patterns
+
maintenance tooling
+
explicit research/field residuals that do NOT ship
```

The research tree must not be copied verbatim into a release.

## Current first-pass direction

Strong candidate reference families:

- Retrieval Obligation 0.5;
- WAIT State;
- Authority Lease;
- Effect Lifecycle;
- Recovery Adapter.

Conditional/advanced candidates requiring more selection or validation:

- Evidence Envelope;
- Evidence Dependency Map;
- recovered Commitment/Settlement;
- Contested Authorship.

Guidance/pattern rather than universal machine-organ candidates:

- Memory Metabolism;
- Tiny Hot Kernel/semantic routing phenotype;
- Commons substrate/A2A layering;
- purpose-relative continuity;
- Standing Input;
- Control Retirement.

Research-only by default for the first candidate includes progressive event-record experiments, compaction/composition harnesses, fencing simulator, mesocosm infrastructure, verification-market/reputation/culture ecology and raw natural-salience experiments.

## Tooling decision still open

The inherited `tools/ena_evolve.py` is not a complete v0.3.6 v2 runtime path and has a known latent-variation false-BLOCK.

Reconciliation must compare:

```text
narrow legacy repair
vs
explicit legacy deprecation
vs
minimal v2-compatible helper
```

Do not patch Current in place before this selection is resolved.

## Language/adoption boundary

New hot/entry Operational Architecture surfaces need honest language projection decisions. Structural parity is not behavioral equivalence, and the full cold reference library need not become a literal file-for-file translation burden when coverage is declared honestly.

## Current boundary

```text
CURRENT = v0.3.6 / CURRENT / FIELD_VALIDATION
NEXT_VERSION = UNASSIGNED
CURRENT_CHANGE = NO
```
