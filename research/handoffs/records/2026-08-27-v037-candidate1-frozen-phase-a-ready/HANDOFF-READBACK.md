# Handoff readback — candidate.1 frozen / fresh Phase A ready

Date: 2026-08-27

Status: `POST_MERGE_READBACK_PASS / HANDOFF_INTEGRATED / FRESH_PHASE_A_NEXT`

This readback was performed after project-state integration into `main`, from the same surfaces a fresh project-manager receiver is required to read. It verifies representation coherence; it does not grant candidate release authority or fresh-validator acceptance.

## Main integration evidence

PR:

`#129 — Control plane: freeze v0.3.7 candidate.1 and open blind successor review`

All observed PR-head checks passed before merge:

- Main Gate — SUCCESS
- Handoff Structure — SUCCESS
- CodeQL — SUCCESS

Merge commit:

`1c826fed023ed472e4b963459cb740c72b3bfd8d`

The final pre-merge compare contained only `.github/`, `collaboration/reconciliation/`, and `research/` paths. There were no changes under `releases/current/` or `releases/v0.3.7-candidate/`.

`research/ena-reconstruction` was then fast-forwarded to the main merge commit before this final readback update, preserving the long-lived research branch as the continuation surface rather than leaving it behind the main-visible project state.

## Receiver questions read back from main

### What is Current?

Main `releases/current/CURRENT-BASELINE.yaml` reads:

`v0.3.6 / CURRENT / FIELD_VALIDATION`

No candidate.1 control-plane transition changed Current.

### What exact object is frozen?

Main `research/handoffs/CURRENT-HANDOFF.yaml`, `research/ACTIVE-RESEARCH.yaml`, and `research/plans/PROGRESS.yaml` agree on:

- identity `v0.3.7-candidate.1`
- frozen source `ae6903464133cb5bcf3cd8909ecae1215fe0b9ba`
- frozen candidate subtree `c0458e0d7ea417b841cbf4c8bf6e64e4aff37319`
- Current subtree at frozen source `7dcbb3934883ffa6cc5292a662588cafc1533cff`
- exact pre-freeze run `33055811978` — PASS
- external freeze record `collaboration/reconciliation/2026-08-27-v037-candidate1-freeze.md`
- state `FROZEN / NOT_CURRENT / NOT_RELEASED`

The branch head is not substituted for this exact-tree identity.

### What project phase is actually active?

Main `research/ACTIVE-RESEARCH.yaml` reads:

`V0_3_7_CANDIDATE1_FROZEN / FRESH_BLIND_PHASE_A_NEXT / NOT_CURRENT / NOT_RELEASED`

Main `research/plans/PROGRESS.yaml` reads:

`V0_3_7_CANDIDATE1_FROZEN_FRESH_BLIND_PHASE_A_NEXT`

The detailed Progress projection now also labels candidate.1 exact pre-freeze author evidence separately from independent evidence and identifies the candidate.1 blind intake as the active independence step.

### Which handoff record is current?

Main `research/handoffs/CURRENT-HANDOFF.yaml` points to:

`research/handoffs/records/2026-08-27-v037-candidate1-frozen-phase-a-ready/`

The pointer records the project-manager/fresh-validator role boundary and marks the freeze-era handoff refresh complete.

### What is the exact next action?

`CANDIDATE1_FRESH_BLIND_PHASE_A`

Prepared intake was reverified live after main integration:

- Issue `#128` is OPEN;
- validation branch `validation/v037-c1-blind-phase-a-primary` exists;
- branch intake head remains `bac074097579ad930b2e90c46c00773f6f20c86d`;
- that intake commit's parent is exact frozen source `ae6903464133cb5bcf3cd8909ecae1215fe0b9ba`;
- blind entry is `collaboration/reconciliation/2026-08-27-v037-candidate1-blind-phase-a-entry.md`;
- required sealed report path is `collaboration/reconciliation/2026-08-27-v037-candidate1-independent-phase-a-primary.md`;
- no candidate.1 Phase-A report exists on the intake branch yet at this readback snapshot.

Fresh-validator stop rule remains:

`REPORT_COMMITTED -> PHASE_A_SEALED -> STOP`

### What must remain forbidden?

- modifying or promoting `releases/current/`;
- mutating frozen candidate.0 or candidate.1 in place;
- calling same-falsifier/author regressions fresh independent evidence;
- exposing project-manager handoff, predecessor findings, candidate.1 repair narrative, author attack maps, or expected observations to the fresh reviewer before seal;
- treating exact machine PASS as possibility-space completeness;
- inventing a universal cross-environment candidate-ID uniqueness law merely to eliminate a visible residual.

### What unresolved variation remains decision-relevant?

At minimum:

- the fresh candidate.1 reviewer may discover failure or false-BLOCK shapes not represented in the author search map;
- source/receiver candidate-ID namespace collision remains a visible non-contract residual;
- external truth/authenticity remains outside what the machine validators alone establish;
- attack cardinality remains `OPEN`.

No finite test/file/category count is recorded as epistemic completeness.

## Method readback

The receiver can recover from main that project-manager succession requires state + method + governance + decision lineage + next action, while fresh Phase-A validation intentionally receives less information.

The active boundary remains:

`PROJECT_MANAGER_CONTEXT != FRESH_VALIDATOR_PHASE_A_CONTEXT`

and:

`PRIOR_MATERIAL_EXPOSURE -> FRESHNESS_NOT_RECOVERABLE_WITHIN_SAME_REVIEWER_STATE`

Therefore this project-manager session is not eligible to perform the fresh candidate.1 Phase A it prepared.

## Readback verdict

A fresh project-manager receiver can answer from persisted main-visible sources:

- Current = v0.3.6;
- candidate.1 exact frozen identity = source `ae690346...` / subtree `c0458e0d...`;
- candidate.1 is not Current/released;
- exact pre-freeze evidence passed but is not independent acceptance;
- one fresh blind successor review was explicitly judged worth its epistemic rent;
- Issue #128 / validation branch / blind entry are the sole Phase-A intake;
- candidate.1 material correction after freeze requires candidate.2;
- attack cardinality remains open;
- next action is fresh blind Phase A.

Result:

`HANDOFF_READBACK = PASS`

`PROJECT_STATE_ALIGNMENT = COHERENT_FOR_NEXT_ACTION`

`NEXT_ACTION = CANDIDATE1_FRESH_BLIND_PHASE_A`
