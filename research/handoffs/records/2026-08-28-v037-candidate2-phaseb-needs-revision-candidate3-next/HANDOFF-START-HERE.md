# Handoff — candidate.2 Phase B complete; candidate.3 next

Status: `HANDOFF_READY / CANDIDATE2_PHASE_B_NEEDS_REVISION / CANDIDATE3_REQUIRED`

## Canonical state

Current remains `v0.3.6 / CURRENT / FIELD_VALIDATION`.

`v0.3.7-candidate.2` remains immutable and is now fully classified:

`FROZEN / A-S SEALED / A-P SEALED / PHASE-B NEEDS_REVISION / NOT_CURRENT / NOT_RELEASED`

Frozen candidate.2 identity:

- source `bda470e0a6b170cec61225a905957a501454a2fe`
- subtree `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`

Independent seals:

- A-S SHA-256 `0e6bb214cc3398b34c13fc6a3bebd1f548ae00ea067b4c338e8ce88f42ad955f`
- A-P SHA-256 `80987d24a80c2aff90fddd96bc1891ee03c6ac02b25381d8af2a22418ebbe1db`

Phase-B record:

`collaboration/reconciliation/2026-08-28-v037-candidate2-a-s-a-p-phase-b-reconciliation.md`

Verdict:

`NEEDS_REVISION / CANDIDATE_3_REQUIRED`

## Immediate next action

`CREATE_AND_REPAIR_V0_3_7_CANDIDATE3_FROM_FROZEN_CANDIDATE2`

Candidate.3 must be born directly from frozen candidate.2 and repair only the bounded Phase-B scope:

1. composed Authority represented-semantic parity;
2. terminal Effect receipt monotonicity/conflict handling;
3. transferred-source integration chronology/snapshot parity;
4. regression harness/result provenance truthfulness;
5. candidate lineage/changelog/birth-base narration;
6. zh-CN reconciliation-status narration;
7. clarify predecessor historical narration without rewriting occurrence truth.

Add direct regression fixtures for the sealed findings and preserve inherited zero-flip behavior.

Do not modify candidate.2 or `releases/current/`.

Candidate.3 does not automatically trigger another full fresh A-S/A-P cycle. After bounded repair and exact pre-freeze validation, decide any further independent review by semantic radius and epistemic rent.
