# Project state — candidate.2 A-S sealed

## Current

`v0.3.6 / CURRENT / FIELD_VALIDATION`

No Current bytes changed.

## Candidate.2

`v0.3.7-candidate.2 / FROZEN / NOT_CURRENT / NOT_RELEASED`

Frozen identity:

- source `bda470e0a6b170cec61225a905957a501454a2fe`
- subtree `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`

## Independent validation

Dedicated clean-room A-S completed by a fresh reviewer.

Exact report SHA-256:
`0e6bb214cc3398b34c13fc6a3bebd1f548ae00ea067b4c338e8ce88f42ad955f`

Exact report size: `14839` bytes.

Persisted Git blob SHA-1: `a8ec063fc1dcda9be70a53bf150e45ea11ac125e`.

Verdict: `NOT_CLEARED`.

Findings:

1. A-S-01 — composed authority represented revocation/scope gap.
2. A-S-02 — terminal effect receipt can regress into retry.
3. A-S-03 — migrated source INTEGRATED chronology/snapshot gap.
4. A-S-04 — self-referential A-S report hash instruction.

These are independent occurrence truth, not yet project-manager Phase-B classification.

## Sequence boundary

A-P: `NOT_STARTED`.

Phase B: `NOT_STARTED`.

Candidate repair: `NOT_ALLOWED_BEFORE_A_P_COMPLETES`.

Next: prepare A-P surface in the dedicated clean room and return the same fresh reviewer to it. The reviewer must stop after A-P; project-manager reconciliation follows afterward.
