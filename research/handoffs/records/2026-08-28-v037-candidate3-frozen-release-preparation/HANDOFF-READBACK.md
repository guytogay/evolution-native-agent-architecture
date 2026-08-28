# Handoff Readback

Pre-main-checkpoint readback on 2026-08-28:

- Current remains `v0.3.6 / CURRENT / FIELD_VALIDATION` with subtree `7dcbb3934883ffa6cc5292a662588cafc1533cff`.
- frozen candidate.3 source/subtree are `b7e88d7adb70396bd671ca97066daf2c120e0adc` / `e3a9a20d16cecd78df7f32f19fca56e21159e810`.
- exact pre-freeze run `33150269264` SUCCESS.
- targeted post-freeze run `33150553992` SUCCESS.
- release hardening run `33152201566` SUCCESS.
- all six candidate.2 material repair classes are recorded CLOSED under targeted replay.
- hardening observed zero broken candidate-local Markdown links, preserved 38 Constitution IDs, explained all v0.3.6 top-level removals, preserved legacy runtime bytes, and retained inherited 164/164 plus successor 61/61 behavior.
- release hardening did not demonstrate a material frozen candidate-byte defect.
- final release reconciliation says `CANDIDATE_SUCCESSION_STOP=YES` and `RELEASE_PREPARATION_SUPPORTED`.
- hardening reconciliation says `RELEASE_PACKAGING_PERMITTED` and candidate.4 is not justified by current evidence.
- candidate.3 material mutation remains forbidden after freeze.
- immediate next action is `MAIN_VISIBLE_CHECKPOINT_THEN_CREATE_RELEASE_V0_3_7_AND_TRANSPLANT_FROZEN_CANDIDATE3`.

After main integration, re-read exact main SHA and control pointers before creating the release branch. The first release-branch semantic occurrence should be a byte-for-byte transplant of the frozen candidate.3 subtree into `releases/current/`; identity packaging happens only after that transplant is recorded.
