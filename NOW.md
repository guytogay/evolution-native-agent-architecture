# ENA — NOW

This is the live project-status surface. It is maintainer/project context, not ENA adopter/runtime content.

## Current

- `v0.3.14 / CURRENT / FIELD_VALIDATION`
- identity authority: `releases/current/CURRENT-BASELINE.yaml`
- effective package: `releases/current/`
- predecessor: `v0.3.13`
- field stream: Issue `#208`

Do not mutate `releases/current/**` without successor identity.

## v0.4 status

Branch: `rebuild/v0.4.0-practical-core`
Status: `ACTIVE_REBUILD / NOT_CURRENT / NOT_PROMOTED`

Existing working artifacts:

- `rebuild/v0.4.0/PRACTICAL-CORE.md`
- `rebuild/v0.4.0/LEGACY-SEMANTIC-COVERAGE.md`
- `rebuild/v0.4.0/START-HERE.md`

## Owner direction correction — mandatory

The owner identified a deeper defect than verbosity alone: **product/project boundary contamination**.

Prior sessions sometimes copied instructions about how to maintain, research, hand off, or write ENA into ENA itself. Some of that material may now be embedded in legacy terminology, distinctions, workflows, and architecture rather than existing only as separate project-management files.

Analogy from the owner: a coin inserted into a tree trunk can later be wrapped by layers of growth until it cannot be cleanly separated from the wood. Deep embedding is therefore not proof that a legacy concept intrinsically belongs to ENA.

Mandatory full correction record:

`research/handoffs/records/2026-09-07-v040-boundary-contamination-correction/OWNER-DIRECTION-CORRECTION.md`

A deep successor must read it before continuing v0.4 design.

## Consequence for v0.4

Do not use v0.3.x taxonomy, terminology, module boundaries, distinction catalogues, Action Card families, handoff mechanics, or project-management practice as the v0.4 skeleton merely because they already exist.

Correct derivation order:

1. start from ENA's actual purpose;
2. start from real Agent problems/opportunities;
3. derive the minimum useful capabilities from those problems;
4. build the clean product;
5. only afterward compare with v0.3.x for important omissions/regressions.

`LEGACY-SEMANTIC-COVERAGE.md` is now a secondary regression/coverage aid, not a product blueprint.

Previously named families such as `EVIDENCE/SUPPORT`, `EFFECT LIFECYCLE`, `RECOVERY/RESUME`, `ADAPTATION IMPORT`, and `COMPOSITION` may represent real capabilities worth preserving, but their old names and boundaries do not require five cards/modules. Mechanical continuation of that plan is paused.

## Cleanup / migration direction

The owner explicitly directed the maintainer to:

- archive material that deserves preservation but not live/product prominence;
- delete material that no longer earns a live place and is already recoverable through Git history;
- transfer reusable general human-AI/project-working methods to the repository that owns them, primarily `guytogay/human-ai-workbench`;
- avoid asking the owner to manually clean the accumulated contamination.

The owner explicitly permits creating a new repository for the clean v0.4 product if that is the best way to avoid carrying structural contamination forward. No new v0.4 product repository has been created yet.

The current repository may therefore become primarily the v0.3.x Current/history/research/evidence source while a clean product home is established separately.

## Active occurrences

- Issue `#208` — Current field validation umbrella.
- Issue `#222` — design occurrence; re-evaluate through the corrected clean-derivation direction.
- PR `#224` — contribution occurrence showing actionability/prose-rent problems; do not merge paragraph-scale rewrite into v0.3.14.
- Issue `#234` — active practicality/prose-rent evidence.
- evolutionary-memory mechanism-discrimination campaign remains `CLOSED`.

## Immediate next action

`ESTABLISH_CLEAN_V040_PRODUCT_BOUNDARY_AND_REDERIVE_FROM_REAL_AGENT_PROBLEMS`

Do not continue legacy-family Action Card derivation until the product boundary is clean.
