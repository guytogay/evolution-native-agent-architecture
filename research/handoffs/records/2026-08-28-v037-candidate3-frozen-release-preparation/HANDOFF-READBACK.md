# Handoff Readback

Pre-main-checkpoint readback on 2026-08-28:

- Current remains `v0.3.6 / CURRENT / FIELD_VALIDATION` with subtree `7dcbb3934883ffa6cc5292a662588cafc1533cff`.
- frozen candidate.3 source/subtree are `b7e88d7adb70396bd671ca97066daf2c120e0adc` / `e3a9a20d16cecd78df7f32f19fca56e21159e810`.
- exact pre-freeze run `33150269264` SUCCESS.
- targeted post-freeze run `33150553992` SUCCESS.
- all six candidate.2 material repair classes are recorded CLOSED under targeted replay.
- final release reconciliation says `CANDIDATE_SUCCESSION_STOP=YES` and `RELEASE_PREPARATION_SUPPORTED`.
- candidate.3 material mutation remains forbidden after freeze.
- immediate next action is `PREPARE_V0_3_7_RELEASE_BRANCH_FROM_EXACT_FROZEN_CANDIDATE3` after the reconciliation/control checkpoint becomes main-visible.

After main integration, re-read exact main SHA and control pointers before creating the release branch.
