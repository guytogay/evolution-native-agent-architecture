# ENA v0.3.5 candidate.2 freeze record

Date: 2026-08-23

## Status

`FROZEN_CANDIDATE.2 / AUTHOR_RECONCILED / AWAITING_NARROW_SAME_FALSIFIER_REVALIDATION / NOT_CURRENT / NOT_RELEASED`

This record freezes the second successor candidate after candidate.1 received same-falsifier targeted support with residuals.

Passing author/CI checks is not independent acceptance.

## Frozen candidate.2 identity

Source commit:

`8393b8b05d34797965c612e8b9ca938d306f6322`

Effective candidate subtree:

`releases/v0.3.5-candidate/`

Git tree:

`b10854f191d9641138e2f44278f043f124a2e120`

Current at the same source commit remains:

`releases/current/`

Git tree:

`b237802c08d608bb9be650fe213b7846d3be4bf6`

No `releases/current/**` change is part of candidate.2.

## Predecessor evidence

### Frozen first candidate

- source: `eb6d7ba00894ed446903aebe61cd59f0bdb59af7`
- tree: `f373e7695348c157dcd48d3ed243ea3079215b8f`
- independent DSH verdict: `NEEDS_REVISION`

### Frozen candidate.1

- source: `e6ff1e76afb8ad8919186786100ec153a5f0d07a`
- tree: `ff2cb44c7a5d1b472800180578b5df7baa123aec`
- freeze-record commit: `63ca8bdb14bfa4aca213d1dc88287f15572dd5c2`
- DSH role: `SAME_FALSIFIER / TARGETED_REVALIDATION / NOT_FRESH`
- targeted verdict: `TARGETED_REVALIDATION_SUPPORTED_WITH_RESIDUALS`

The same falsifier mechanically confirmed the material predecessor defects were closed and reported no evolution-starvation/over-governance regression.

## candidate.2 authorized repair scope

candidate.2 deliberately closes the concrete release-decision residuals from the candidate.1 targeted revalidation:

1. N1 — migration packet CLI now rejects invalid `source_lifecycle_state` values directly rather than relying on JSON Schema alone.
2. N2 — migration packet CLI fixes `source_authentication` to `NOT_AUTHENTICATED_BY_THIS_PACKET` and rejects forged stronger self-authentication strings.
3. N7 — committed `regression-results-v033.json` is synchronized with the current inherited regression suite; CI regenerates it and requires zero diff.
4. Adjacent same-class hardening — CLI also fixes/validates `transfer_status=TRANSFERRED_SOURCE_EVIDENCE_NOT_LOCAL_PROOF`.
5. `tools/candidate2_adversarial.py` mechanizes the N1/N2/transfer-status closures.
6. Active English and zh-CN candidate/projection identities advance to candidate.2.

No Constitution rule changed for these implementation residuals.

## Intentionally retained residuals

These observations remain visible rather than being converted into unresearched release gates:

- N3 — multiple evaluations may reinterpret the same represented experiment; history remains append-visible, but no new-experiment-per-verdict-change rule is imposed.
- N4 — after receiver-side positive reselection, source negative lineage remains nested rather than promoted to top-level packet summary.
- N5 — the reference tool has no in-place restore/reopen transition for `ARCHIVED/RETIRED`; new variation/export paths remain available.
- N6 — nested migration lineage may grow in depth across generations.

These were not judged material blockers by the candidate.1 targeted revalidation. They remain future research/field-evidence opportunities.

## Automated evidence at frozen source

At source commit `8393b8b05d34797965c612e8b9ca938d306f6322`:

- Validate ENA v0.3.5 candidate — run `32616616552` — SUCCESS
  - inherited composed-validator regression PASS;
  - committed regression-result regeneration parity PASS;
  - `ena_evolve.py selftest` PASS;
  - candidate.1 adversarial regression PASS;
  - candidate.2 residual-closure adversarial regression PASS;
  - actual tool record/packet JSON-schema wiring PASS;
  - Constitution EN/zh-CN ID parity PASS;
  - bilingual fixture structural checks PASS;
  - candidate pointer / Current isolation checks PASS.
- Main Gate — run `32616616488` — SUCCESS.
- CodeQL — run `32616616572` — SUCCESS.

Automated success does not prove external evidence truth, source authentication, authority, recovery, universal cross-language behavior, net field benefit, or independent acceptance.

## Required next step

Use the same DSH falsifier for a **narrow candidate.2 targeted revalidation**, labeled:

`SAME_FALSIFIER / NARROW_RESIDUAL_REVALIDATION / NOT_FRESH`

The minimum required checks are:

- N1 malformed lifecycle packet with recomputed digest is rejected by CLI;
- N2 forged `source_authentication` with recomputed digest is rejected by CLI;
- forged `transfer_status` with recomputed digest is rejected by CLI;
- regenerated `regression-results-v033.json` remains byte-clean;
- candidate.1 material regression probes still pass;
- Constitution and Current remain unchanged;
- no new evolution-starvation behavior was introduced by the narrow fixes.

Do not modify this frozen candidate.2 tree during revalidation.

## Freeze rule

Any material correction after this record requires a new successor candidate identity. Do not silently mutate tree `b10854f191d9641138e2f44278f043f124a2e120` and continue calling it this frozen candidate.2.
