# ENA handoff — candidate.1 blind semantic validation ready

Status: `HANDOFF_READY / CANDIDATE1_FROZEN / INVALID_FULL-PACKAGE_BLIND_INTAKE_RETIRED / A-S_A-P_NEXT / NOT_CURRENT`

## Start here

1. Verify Current from `releases/current/CURRENT-BASELINE.yaml`.
2. Read canonical handoff framework and project methodology.
3. Read `research/ACTIVE-RESEARCH.yaml` and `research/plans/PROGRESS.yaml`.
4. Reverify frozen candidate.1 identity and live validation refs.
5. Continue from Issue `#131`; do not reuse Issue `#128` as an active intake.

## Current

`v0.3.6 / CURRENT / FIELD_VALIDATION`

## Frozen candidate.1

- identity: `v0.3.7-candidate.1`
- source: `ae6903464133cb5bcf3cd8909ecae1215fe0b9ba`
- subtree: `c0458e0d7ea417b841cbf4c8bf6e64e4aff37319`
- exact pre-freeze run: `33055811978` — SUCCESS
- frozen bytes must not be edited in place.

## What changed after freeze

The first candidate.1 fresh intake, Issue #128, was invalidated when a genuinely fresh reviewer found that a permitted candidate-local self-description file disclosed predecessor findings and repair history before Phase-A sealing.

That reviewer correctly stopped and did not claim freshness.

This established a validation-interface defect:

`CANDIDATE_LOCAL != AUTOMATICALLY_BLIND_SAFE`

It did **not** establish a candidate behavior defect and therefore does not by itself require candidate.2.

## Replacement method

Fresh independent validation is split into:

- **A-S** — blind semantic falsification against an exact-byte-preserving, priming-reduced validation projection;
- **A-P** — after A-S seal, independent audit of withheld candidate-local history/oracle/selftest surfaces;
- then stop before Phase B.

Active intake:

- Issue `#131`
- branch `validation/v037-c1-blind-semantic-primary`
- entry `collaboration/reconciliation/2026-08-27-v037-candidate1-blind-semantic-entry.md`
- view manifest `collaboration/reconciliation/2026-08-27-v037-candidate1-blind-semantic-view.yaml`

The validation branch is **not a candidate** and has no release authority.

## Forbidden now

- modify/promote Current;
- mutate frozen candidate.0 or candidate.1;
- reuse the contaminated reviewer as fresh A-S;
- reopen #128 as the active blind intake;
- expose author/project-manager repair context before A-S seal;
- treat validation-view exclusions as release ablation;
- create candidate.2 without a material candidate-byte correction basis;
- treat attack cardinality as closed.
