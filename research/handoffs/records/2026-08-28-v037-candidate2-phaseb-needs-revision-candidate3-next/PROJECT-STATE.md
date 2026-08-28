# Project State — after candidate.2 Phase B

## Current

`v0.3.6 / CURRENT / FIELD_VALIDATION`

Current subtree remains `7dcbb3934883ffa6cc5292a662588cafc1533cff`.

## Candidate.2

Identity: `v0.3.7-candidate.2`

Frozen source: `bda470e0a6b170cec61225a905957a501454a2fe`

Frozen subtree: `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`

State: `FROZEN / A-S SEALED / A-P SEALED / PHASE-B NEEDS_REVISION / NOT_CURRENT / NOT_RELEASED`

A-S report SHA-256: `0e6bb214cc3398b34c13fc6a3bebd1f548ae00ea067b4c338e8ce88f42ad955f`

A-P report SHA-256: `80987d24a80c2aff90fddd96bc1891ee03c6ac02b25381d8af2a22418ebbe1db`

Phase-B verdict: `NEEDS_REVISION / CANDIDATE_3_REQUIRED`.

## Confirmed successor repair classes

Semantic/executable:

- composed authority can accept represented revoked/out-of-scope grants;
- terminal COMMITTED effect can be downgraded by a later NOT_COMMITTED receipt into retry posture;
- transferred source INTEGRATED history lacks local-equivalent commit chronology/snapshot parity.

Package/provenance:

- inherited regression harness/result falsely attributes candidate-local execution to Current;
- candidate birth-base/lineage/changelog reader-facing surfaces are stale;
- zh-CN reconciliation status is internally contradictory.

Validation-interface defects, not candidate bytes:

- A-S exact-report self-hash instruction was recursive; use external digest;
- initial A-S clean-room wrapper SHA was recorded incorrectly while the A-S tree/content surface remained correct; canonical correction is already recorded.

## Successor discipline

Any material candidate correction requires `v0.3.7-candidate.3`.

Candidate.3 must start from frozen candidate.2 source/tree and remain bounded to the Phase-B repair scope. Existing visible residuals are not broadened without a governing contract.

Attack cardinality remains `OPEN` but does not imply infinite review.
