# Handoff start here — candidate.2 clean-room A-S ready

Current remains `v0.3.6 / CURRENT / FIELD_VALIDATION`.

Candidate.2 is frozen and immutable:

- source `bda470e0a6b170cec61225a905957a501454a2fe`
- candidate subtree `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`
- NOT_CURRENT / NOT_RELEASED

Issue #137 is historical validation-interface abort evidence only. Do not reuse its same-repository validation branch as fresh A-S.

Active fresh-review surface:

`https://github.com/guytogay/independent-validation-cleanroom`

Pinned A-S state:

`28dde50c9caaeee3b5cfabf51410083dbbb05a93`

Tree:

`42debebed620bd05e6e2635409057f20b57bfa9e`

That commit is parentless and contains only the stage-scoped A-S surface. The clean room is reusable infrastructure; its contents may be reset after this review occurrence.

A genuinely fresh reviewer receives only the clean-room URL/pinned commit and starts at the root README / `INTAKE-A-S.md`. Do not provide ENA project-manager history or A-P material before A-S report content is sealed.

Required sequence:

```text
fresh reviewer
-> clean-room A-S
-> completed A-S report
-> SHA-256 exact report bytes
-> STOP

project manager
-> verify/persist A-S report + digest
-> only then open A-P to same reviewer
-> reviewer completes A-P
-> STOP before Phase B
```

The deterministic r3 ZIP build remains construction/integrity evidence, not the required reviewer-facing transport.

Next action:

`GET_GENUINELY_FRESH_REVIEWER_TO_RUN_CANDIDATE2_A_S_IN_DEDICATED_CLEAN_ROOM`
