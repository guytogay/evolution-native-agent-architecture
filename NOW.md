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
- practical HOW/action is too far downstream from the default product surface;
- ENA has accumulated too much project-specific vocabulary that an adopter must learn before acting.

Working findings:

- `F-208-13_AGENCY_FIRST_SEMANTICS_CAN_PROJECT_AS_DEFENSIVE_FIRST_HOT_POSTURE`
- `F-208-14_DURABLE_DISTINCTIONS_DO_NOT_BY_THEMSELVES_PROVIDE_AN_ACTION_BRIDGE_TO_HOW`
- `F-208-15_THEORY_FIRST_ADOPTER_SURFACE_WEAKENS_PRACTICAL_UTILITY`
- `F-208-16_DERIVATION_TAX_SPENDS_RUNTIME_ATTENTION_PROVING_BOUNDARIES_INSTEAD_OF_ENABLING_ACTION`

## v0.4 product standard

The rebuilt ENA should be:

```text
SIMPLE
CLEAR
PRACTICAL
GROUNDED_IN_REAL_WORK
```

In ordinary language: **简洁、清楚、实用、接地气**.

This does not permit capability loss:

```text
ALL_DECISION_MATERIAL_CAPABILITIES_MUST_BE_COVERED
!= EVERY_CAPABILITY_NEEDS_ITS_OWN_TERM_FILE_CARD_OR_FRAMEWORK
```

Prefer ordinary language. Retain or coin ENA-specific terminology only when plain language would lose decision-material precision and the term clearly earns its learning cost through repeated useful reuse.

```text
PLAIN_LANGUAGE_FIRST
TERM_ONLY_WHEN_IT_PAYS_RENT
```

An Agent should not need to learn an ENA dialect before solving the real problem.

## v0.4 clean-root rebuild

Branch: `rebuild/v0.4.0-practical-core`
Status: `ACTIVE_REBUILD / NOT_CURRENT / NOT_PROMOTED`

Primary artifacts:

- `rebuild/v0.4.0/START-HERE.md`
- `rebuild/v0.4.0/PRACTICAL-CORE.md`
- `rebuild/v0.4.0/LEGACY-SEMANTIC-COVERAGE.md`

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

## Rebuild progress

The first legacy semantic coverage pass is complete on the rebuild branch.

- 29 major legacy property/failure families now have practical placements.
- The 19-item durable-distinction catalogue is marked `RETIRE` as a product unit; decision-material slices move to action/guard/cold locations.
- Mandatory `semantic -> Cue Index -> HOW Map` traversal is marked for retirement as the default product path; problem/action surfaces should link deeper HOW directly when needed.
- Practical Core dogfood covered ENA rebuild work and a real non-ENA Human-AI Workbench decision.
- Dogfood exposed one bounded gap: material opportunities that cannot move immediately needed explicit wake/unblock semantics. `PRACTICAL-CORE.md` now carries the compact `ACT_NOW | WAIT_FOR_SIGNAL | BLOCKED | DROP` liveness rule.
- `START-HERE.md` now makes capability coverage mandatory while allowing the cheapest useful representation, and adds the plain-language/jargon-rent rule.

## Issue #234

Issue `#234` reports the same "cabbage != radish" hot prose-rent failure from a DSH field-adopter Host.

Maintainer disposition: `ACCEPT_CORE_DEFECT / NARROW_MACHINE_ONLY_CLAIM / ADVANCE_NOW_IN_V040_REBUILD`.

Keep the useful rule:

```text
MACHINE_FIRST_WHEN_MACHINE_FIT != MACHINE_ONLY
```

Machine guards should carry machine-fit properties, but local validators cannot by themselves prove external mandate, real-world effects, causal support, or future field behavior.

The initial placement pass now exists, but Issue #234 remains open until the rebuilt practical surface demonstrates material protection with lower prose/derivation rent.

## Immediate next action

`COVER_ALL_FIVE_V040_PRACTICAL_FAMILIES_AND_REALITY_TEST_THEIR_REPRESENTATION`

Process all five remaining practical families:

`EVIDENCE/SUPPORT | EFFECT LIFECYCLE | RECOVERY/RESUME | ADAPTATION IMPORT | COMPOSITION`

For each family:

1. identify the real capability/protection that v0.4 must preserve;
2. use a real problem/task rather than mirroring an old concept;
3. determine whether the Core already covers it;
4. fill any remaining gap with the cheapest fitting representation: `ACTION_CARD | MACHINE_GUARD | EXTERNAL_CONTROL | COLD_HOW | combination`;
5. use ordinary language unless a specialist term demonstrably earns its cost;
6. verify that no decision-material capability was lost.

Do not require five separate cards merely for symmetry. Do not leave any of the five capability families uncovered merely to keep the product short.

Do not run broad fresh-model experiments yet. Use bounded fresh acceptance only when a concrete uncertainty can change the product decision.

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
