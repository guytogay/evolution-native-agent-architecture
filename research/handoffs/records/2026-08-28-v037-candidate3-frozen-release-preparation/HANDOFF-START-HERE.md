# Handoff — candidate.3 frozen; v0.3.7 release preparation next

Status: `HANDOFF_READY / CANDIDATE3_FROZEN / TARGETED_POSTFREEZE_PASS / RELEASE_PREPARATION_SUPPORTED`

## Canonical state

Current remains:

`v0.3.6 / CURRENT / FIELD_VALIDATION`

Frozen final candidate target:

`v0.3.7-candidate.3`

- frozen source: `b7e88d7adb70396bd671ca97066daf2c120e0adc`
- frozen subtree: `e3a9a20d16cecd78df7f32f19fca56e21159e810`
- exact pre-freeze run: `33150269264` — SUCCESS
- targeted post-freeze run: `33150553992` — SUCCESS
- candidate succession: `STOP`
- release preparation: `SUPPORTED`

Key records:

- `collaboration/reconciliation/2026-08-28-v037-candidate3-successor-repair-reconciliation.md`
- `collaboration/reconciliation/2026-08-28-v037-candidate3-freeze.md`
- `collaboration/reconciliation/2026-08-28-v037-candidate3-targeted-postfreeze-revalidation.md`
- `collaboration/reconciliation/2026-08-28-v037-candidate3-final-release-reconciliation.md`

## Immediate next action

`PREPARE_V0_3_7_RELEASE_BRANCH_FROM_EXACT_FROZEN_CANDIDATE3`

Follow the established v0.3.6 release pattern:

1. make this reconciliation/control state main-visible;
2. create governed `release/v0.3.7` from that exact main checkpoint;
3. transplant frozen candidate.3 subtree byte-for-byte into `releases/current/` as a separately auditable packaging start;
4. then perform release identity/status packaging without silently changing material semantics;
5. run exact-head release validation / Main Gate / CodeQL / package parity/readback;
6. explicitly authorize merge only on the exact reviewed release head;
7. post-merge reverify Current and update project alignment/handoff.

Do not modify frozen candidate.3 bytes. A material candidate-byte correction would require candidate.4, but candidate.4 is not a planned or automatic step.

Attack cardinality remains OPEN. External truth / natural Host behavior remain field evidence boundaries, not automatically candidate blockers.
