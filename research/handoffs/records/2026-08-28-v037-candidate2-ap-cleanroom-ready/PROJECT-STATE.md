# Project state — candidate.2 A-P clean-room ready

## Current

`v0.3.6 / CURRENT / FIELD_VALIDATION`

No Current bytes changed.

## Candidate.2

`v0.3.7-candidate.2 / FROZEN / NOT_CURRENT / NOT_RELEASED`

Frozen identity:

- source `bda470e0a6b170cec61225a905957a501454a2fe`
- subtree `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`

## A-S

Fresh clean-room A-S is complete and content-sealed.

- report SHA-256 `0e6bb214cc3398b34c13fc6a3bebd1f548ae00ea067b4c338e8ce88f42ad955f`
- verdict `NOT_CLEARED`
- findings `A-S-01..A-S-04`

The originally supplied A-S wrapper SHA was wrong/unresolvable. The actual parentless A-S commit is `28dde50c9caaeee3b5c269e28a7be5f07ac29ae5` with tree `42debebed620bd05e6e2635409057f20b57bfa9e`. The tree was already recorded correctly, so the correction does not alter the reviewed A-S file surface.

## A-P

A separate A-P clean-room stage is ready but not yet reviewed:

- commit `aea2ed25107145a557b3fe46ca0e4b90e2b90fa9`
- tree `08ac16303d69a6a268197ac26b23c5b20972b727`
- parent count `0`
- exact package subtree `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`

The root contains only the A-P intake/manifest/readme plus the exact frozen candidate package.

## Sequence boundary

A-P: `READY_NOT_STARTED`.

Phase B: `NOT_STARTED`.

Candidate repair: `FORBIDDEN_UNTIL_A_P_AND_PHASE_B`.

Next: return the same fresh reviewer to the A-P clean room, collect its final A-P report plus external SHA-256, then begin project-manager Phase B.
