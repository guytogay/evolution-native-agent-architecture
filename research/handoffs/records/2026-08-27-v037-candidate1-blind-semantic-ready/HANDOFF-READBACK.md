# Handoff readback — blind semantic validation ready

Date: 2026-08-27

Status: `PRE_INTEGRATION_READBACK_PASS / MAIN_VISIBILITY_PENDING`

## Receiver reconstruction

Current:
`v0.3.6 / CURRENT / FIELD_VALIDATION`

Frozen candidate.1:
- source `ae6903464133cb5bcf3cd8909ecae1215fe0b9ba`
- subtree `c0458e0d7ea417b841cbf4c8bf6e64e4aff37319`
- immutable in place
- not Current / not released.

Old intake:
- Issue #128
- invalidated by candidate-local self-priming
- no Phase-A seal
- closed and historical only.

Active intake:
- Issue #131
- branch `validation/v037-c1-blind-semantic-primary`
- A-S then A-P then stop before Phase B.

Method:
`research/methodology/INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md`

Incident:
`research/methodology/incidents/2026-08-27-CANDIDATE-SELF-PRIMING-INCIDENT.md`

## Validation-view readback

A compare from exact frozen source `ae690346...` to the active validation branch showed:

- only declared candidate-file removals for history/oracle/regression/selftest/prior-probe information roles;
- no modified retained candidate file;
- validation entry/manifest added outside candidate cargo.

Therefore the validation branch is a projection, not a candidate successor.

The mixed-role `tools/validate_evolution_record_v2.py` remains exact. A-S explicitly withholds its embedded selftest source range while preserving implementation/CLI ranged reads.

## Next action

`CANDIDATE1_FRESH_A_S_A_P`

Do not ask the fresh reviewer to read full project-manager context.

## Pending integration action

Update canonical Active Research, Progress, and CURRENT-HANDOFF to this transition, integrate the method/control-plane-only change to main, and replace this status with `POST_MERGE_READBACK_PASS` after live main readback.
