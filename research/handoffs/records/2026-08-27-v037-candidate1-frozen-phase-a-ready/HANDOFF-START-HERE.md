# ENA handoff — v0.3.7 candidate.1 frozen / fresh Phase A ready

Status: `PROJECT_MANAGER_HANDOFF_READY / CANDIDATE1_FROZEN / FRESH_BLIND_PHASE_A_NEXT / NOT_CURRENT`

This record is for **project-manager/session succession**. A fresh Phase-A validator must **not** use this record before sealing Phase A; the validator uses only the minimal blind entry described below.

## Current

`v0.3.6 / CURRENT / FIELD_VALIDATION`

Current remains unchanged.

## Frozen candidate.1

- identity: `v0.3.7-candidate.1`
- source commit: `ae6903464133cb5bcf3cd8909ecae1215fe0b9ba`
- candidate subtree: `c0458e0d7ea417b841cbf4c8bf6e64e4aff37319`
- Current subtree at frozen source: `7dcbb3934883ffa6cc5292a662588cafc1533cff`
- exact pre-freeze gate: run `33055811978` — SUCCESS
- freeze record: `collaboration/reconciliation/2026-08-27-v037-candidate1-freeze.md`

Any material change to candidate.1 now requires candidate.2. Do not mutate the frozen tree in place.

## Immediate project action

`CANDIDATE1_FRESH_BLIND_PHASE_A`

Prepared intake:

- issue: `#128`
- branch: `validation/v037-c1-blind-phase-a-primary`
- branch intake head before validator report: `bac074097579ad930b2e90c46c00773f6f20c86d`
- blind entry: `collaboration/reconciliation/2026-08-27-v037-candidate1-blind-phase-a-entry.md`
- required report: `collaboration/reconciliation/2026-08-27-v037-candidate1-independent-phase-a-primary.md`

The validation branch was created from the frozen source and only the blind entry was added outside the candidate subtree; its `releases/` tree remains the frozen one.

## Information boundary

The fresh validator must not receive this project-manager handoff, candidate.0 findings, candidate.1 repair narrative, author attack maps, targeted/open-branch expected observations, or release recommendation before Phase A is sealed.

`REPORT_COMMITTED -> PHASE_A_SEALED -> STOP`

After seal, the project manager verifies exact identity, then opens Phase B reconciliation.

## Project-manager read order

1. `research/handoffs/CURRENT-HANDOFF.yaml`
2. canonical handoff framework and required takeover context
3. project methodology, especially convergence/divergence and independent-validation information boundary
4. this record's `PROJECT-STATE.md`
5. `RECENT-THREE-ROUNDS.md`
6. `FILE-CATALOG.md`
7. `research/ACTIVE-RESEARCH.yaml`
8. `research/plans/PROGRESS.yaml`
9. live GitHub refs / Issue #128 / validation branch

## Do not

- modify or promote `releases/current/`;
- mutate frozen candidate.0 or candidate.1 in place;
- call same-falsifier regressions fresh independent review;
- expose author-shaped context to the candidate.1 fresh validator before its seal;
- treat successful exact machine validation as possibility-space completeness;
- invent a universal candidate-ID namespace rule merely to eliminate a visible residual.

Attack cardinality remains `OPEN`.
