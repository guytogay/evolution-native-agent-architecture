# ENA — NOW

This is the default live project-status surface.

## Current

- `v0.3.12 / CURRENT / FIELD_VALIDATION`
- authority: `releases/current/CURRENT-BASELINE.yaml`
- effective adopter package: `releases/current/`
- predecessor / rollback / occurrence truth: `v0.3.11`
- field stream: GitHub Issue `#208` — version-neutral Current field validation

v0.3.12 is an R0 adoption/identity/routing-coherence successor. It preserves the 38-ID Constitution and core behavior while incorporating external DSH contribution PR `#216` and verified Issues `#217` / `#218`.

Closed findings:

- `F-208-05_CURRENT_OPERATIONAL_IDENTITY_AND_GATE_COVERAGE_GAP` — Current operational surfaces no longer carry v0.3.8/v0.3.7 candidate-era active identity; `ENFORCEMENT-MAP.yaml` now self-identifies as `CURRENT`; the active field template no longer defaults new records to v0.3.7 semantic identity; recurrence checks cover this class without forbidding genuine historical provenance.
- `F-208-06_REFERENCE_INDEX_DEAD_HOW_MAP_ANCHORS` — dead `HOW-MAP.md#...` fragments are no longer published; routing falls back to the valid file-level HOW Map reference until stable deep-linkable nodes are deliberately introduced.

```text
CONTRIBUTOR != PROMOTION_AUTHORITY
EXTERNAL_CONTRIBUTION != UNTRUSTED_BY_DEFAULT
HISTORICAL_PROVENANCE != ACTIVE_RELEASE_IDENTITY
FIELD_VALIDATION != KNOWN_DEFECT_TOLERANCE
```

The original DSH contribution commit remains in release lineage; maintainer release projection is a separate successor step.

## Adoption contract

```text
DEFAULT_AGENT_HOT_PAYLOAD = releases/current/RUNTIME-ADOPTION-KERNEL.md
AVAILABLE_RESOURCE != DEFAULT_HOT_PAYLOAD
HOT_KERNEL != FULL_HOW_LIBRARY
```

For ordinary Agent runtime, only the Runtime Adoption Kernel is resident by default. Cue Index, HOW Map, Enforcement Map, fixtures, references, Constitution detail, and research lineage are cold/on-demand.

Human adopters start at `releases/current/ADOPTER-QUICKSTART.md`.

## Share-ready contract

Before recommending Current to another adopter/Agent:

- known decision-bearing defects with a clear bounded fix must be resolved through the smallest successor;
- current machine/regression gates must pass;
- bounded identity/adopter readback must agree with `CURRENT-BASELINE.yaml`;
- unknown future defects remain legitimate field-validation risk, but known unfixed defects are not an acceptable recommendation state.

## Release posture

```text
IMMUTABLE_VERSION != IMMOBILE_CURRENT
PRESERVE_OLD_RELEASES + MOVE_CURRENT_QUICKLY
```

Method: `research/methodology/RAPID-CURRENT-RELEASE-DISCIPLINE.md`

- R0 — adoption / projection / bounded tooling or publication-coherence field patch: machine/regression/readback + rollback; fresh independent evidence may be post-release.
- R1 — operational behavior change: targeted adversarial/independent evidence when decision-material.
- R2 — core semantic/high-consequence change: heavy freeze/fresh falsification by default.

## Active field stream

Issue `#208` follows Current, not one release number. F-208-01 through F-208-06 have produced rapid R0 successors. New bounded defects should create the smallest justified successor instead of remaining knowingly unfixed.

## Research status

The evolutionary-memory mechanism-discrimination campaign is **CLOSED**. No active mechanism primary remains. Reopen research only for a concrete decision-changing failure or a genuinely new non-derivable discriminator.

## Open work

- GitHub Issue `#208` — version-neutral Current field validation.
- Continue reality contact with actual adopters/contributors; do not manufacture a new mechanism experiment merely because the previous campaign is closed.
