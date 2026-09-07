# ENA — NOW

This is the default live project-status surface. Read this first; use handoff/issues/history only when needed.

## Current

- `v0.3.14 / CURRENT / FIELD_VALIDATION`
- identity authority: `releases/current/CURRENT-BASELINE.yaml`
- effective package: `releases/current/`
- predecessor / rollback occurrence: `v0.3.13`
- field stream: Issue `#208`

Do not mutate `releases/current/**` without successor identity.

## Strategic product pivot

The active design direction is no longer incremental repair of the v0.3.x adopter-facing structure.

Field and owner review found a structural practicality problem:

- adopter/runtime attention is over-spent on theory, semantic distinctions and derivations;
- many `X != Y` statements are true but do not tell an Agent what to do;
- the hot projection is more defensive than ENA's agency-first purpose;
- practical HOW/action is too far downstream from the default product surface.

Working findings:

- `F-208-13_AGENCY_FIRST_SEMANTICS_CAN_PROJECT_AS_DEFENSIVE_FIRST_HOT_POSTURE`
- `F-208-14_DURABLE_DISTINCTIONS_DO_NOT_BY_THEMSELVES_PROVIDE_AN_ACTION_BRIDGE_TO_HOW`
- `F-208-15_THEORY_FIRST_ADOPTER_SURFACE_WEAKENS_PRACTICAL_UTILITY`
- `F-208-16_DERIVATION_TAX_SPENDS_RUNTIME_ATTENTION_PROVING_BOUNDARIES_INSTEAD_OF_ENABLING_ACTION`

## v0.4 clean-root rebuild

Branch: `rebuild/v0.4.0-practical-core`
Status: `ACTIVE_REBUILD / NOT_CURRENT / NOT_PROMOTED`

Primary artifacts:

- `rebuild/v0.4.0/START-HERE.md`
- `rebuild/v0.4.0/PRACTICAL-CORE.md`

Core decision:

```text
V0.3.X = PRESERVED RESEARCH + SEMANTIC + PROVENANCE ASSET
V0.4.0 = PRACTICE-FIRST PRODUCT REBUILD
PRESERVE_HISTORY != PRESERVE_PRODUCT_SHAPE
```

Do not copy the v0.3.x tree and edit it down. Extract decision-material value and redesign from practical problems/actions outward.

Target product order:

```text
PROBLEM / OPPORTUNITY
-> DO NOW
-> OBSERVE
-> SELECT / STOP / REVALIDATE
-> OPTIONAL BOUNDARY / THEORY
```

## Issue #234

Issue `#234` reports the same "cabbage != radish" hot prose-rent failure from a DSH field-adopter Host.

Maintainer disposition: `ACCEPT_CORE_DEFECT / NARROW_MACHINE_ONLY_CLAIM / ADVANCE_NOW_IN_V040_REBUILD`.

Keep the useful rule:

```text
MACHINE_FIRST_WHEN_MACHINE_FIT != MACHINE_ONLY
```

Machine guards should carry machine-fit properties, but local validators cannot by themselves prove external mandate, real-world effects, causal support, or future field behavior.

## Immediate next action

`BUILD_V040_LEGACY_SEMANTIC_COVERAGE_LEDGER_AND_TEST_PRACTICAL_CORE_ON_REAL_WORK`

For major v0.3.x properties, decide based on practical consequence rather than inheritance:

`PRACTICAL_CORE | ACTION_CARD | MACHINE_GUARD | EXTERNAL_CONTROL | COLD_HOW | THEORY_ONLY | RETIRE`

Ask:

1. What wrong action does this prevent?
2. What positive action/capability does this enable?
3. What is the cheapest representation that preserves that value?

Then dogfood the Practical Core on real ENA work and at least one real non-ENA Agent task. Use bounded fresh tests only when their result can change the product decision.

## Active occurrences

- Issue `#208` — Current field validation umbrella; do not close cosmetically.
- Issue `#222` — broad design occurrence; re-adjudicate useful directions through agency-first/practicality-first lens.
- PR `#224` — contribution occurrence showing the actionability problem; do not merge its paragraph-scale rewrite into v0.3.14.
- Issue `#234` — active prose-rent/practicality input to v0.4.
- `ena-field-guide` PR `#6` — admission candidate; helper existence is not recovery proof.

## Research status

Evolutionary-memory mechanism-discrimination campaign remains `CLOSED`. Reopen only for a concrete decision-changing failure or genuinely new non-derivable discriminator.

## Project ecosystem

- ENA repo — theory, Current/release semantics, evidence, field findings, v0.4 product rebuild.
- `human-ai-workbench` — reusable project-general working/succession/coordination method.
- `ena-field-guide` — evidence-backed practical ENA-derived HOW.
- `independent-validation-cleanroom*` — disposable execution surfaces, not canonical knowledge stores.

## Operating restraint

Do not solve ENA's complexity by writing a larger framework about simplicity.

> What is the simplest useful thing to do next?
