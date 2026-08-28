# Project State — candidate.2 isolated A-S ready

## Canonical adoption

Current remains `v0.3.6 / CURRENT / FIELD_VALIDATION`.

## v0.3.7 candidate chain

- candidate.0: frozen predecessor, independently falsified, superseded.
- candidate.1: frozen predecessor, fresh A-S/A-P + Phase B => `NEEDS_REVISION`, superseded.
- candidate.2: frozen successor, exact pre-freeze PASS, not Current, not released.

Candidate.2 exact identity:
- source `bda470e0a6b170cec61225a905957a501454a2fe`
- subtree `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`

## Fresh-validation state

Issue #137 is historical interface-abort occurrence truth, not an active fresh-review intake.

The active fresh-review interface is r3 physical isolation:

`A-S isolated capsule -> A-S report SHA-256 seal -> A-P exact-package supplement -> STOP -> project-manager Phase B`

Carrier audit run `33131773164` passed physical isolation, exact A-P frozen-package equality, payload inventories and deterministic rebuilds.

Hashes:
- A-S `dfe15a686668440138bfd624453059d61a0b28625bb9a5e0c185b33eccf9c2da`
- A-P `427a1776aea199f5f27c4bea2827d3c827cf82fab2c8cd403da0e8cc1dd97649`

No A-S seal exists yet. A-P has not started. Phase B has not started.

## Authority boundaries

- Do not modify candidate.2 in place.
- Do not modify/promote Current from this transition.
- Do not reuse repository/branch navigation as the fresh A-S carrier.
- Do not supply A-P before A-S content seal.
- Current project-manager state cannot claim fresh A-S.
- `ATTACK_CARDINALITY = OPEN`.
