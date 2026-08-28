# Handoff readback — candidate.2 frozen / blind semantic view next

Date: 2026-08-28

Status: `READBACK_PASS / PROJECT_MANAGER_SUCCESSION_READY / FRESH_VALIDATOR_CONTEXT_SEPARATE`

## Live readback

Research branch observed after the frozen-state control-plane transition:

`research/ena-reconstruction @ db74134c1c8d7b1d8a03fb2ea272033db9d47136`

Current remains:

`v0.3.6 / CURRENT / FIELD_VALIDATION`

Frozen candidate.2 identity remains:

- identity: `v0.3.7-candidate.2`
- exact tested/frozen source: `bda470e0a6b170cec61225a905957a501454a2fe`
- exact frozen candidate subtree: `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`
- Current subtree at the same source: `7dcbb3934883ffa6cc5292a662588cafc1533cff`
- exact pre-freeze run: `33095987843` — PASS
- freeze record: `collaboration/reconciliation/2026-08-28-v037-candidate2-freeze.md`
- post-freeze independence decision: `FRESH_BLIND_SUCCESSOR_REVIEW_WARRANTED_ONE_CYCLE`

The candidate subtree was not rewritten to record freeze status. Any material candidate-byte correction now requires a new successor identity (candidate.3 or later).

## Control-plane readback

`research/ACTIVE-RESEARCH.yaml` and `research/handoffs/CURRENT-HANDOFF.yaml` now agree that the next governed action is:

`PREPARE_CANDIDATE2_BLIND_SEMANTIC_VIEW_AND_FRESH_INTAKE`

The current handoff pointer identifies this record and does not treat branch recency, an old PR, or this record itself as project authority.

## Epistemic role boundary

The project-manager session that performed candidate.2 repair, exact pre-freeze validation, freeze reconciliation, and post-freeze independence decision is materially exposed to author-side search maps and therefore cannot claim fresh A-S for candidate.2.

A fresh validator must receive only the task-specific blind semantic entry and blind view before A-S seal. It must not receive the full project-manager handoff, candidate.1 findings, candidate.2 repair narrative, author-side open-branch probes, expected outcomes, or reconciliation verdicts before A-S is persisted.

After A-S seal, A-P may inspect the withheld candidate-local history/oracle surfaces from the exact frozen source, then must persist A-P and stop before project-manager Phase B.

## Invariants rechecked

- `FROZEN != CURRENT`
- `EXACT_PREFREEZE_PASS != FRESH_INDEPENDENT_ACCEPTANCE`
- `BLIND_VIEW != NEW_CANDIDATE`
- `EXCLUSION_FOR_BLINDNESS != RELEASE_ABLATION`
- `PROJECT_MANAGER_TAKEOVER_CONTEXT != FRESH_VALIDATOR_A_S_CONTEXT`
- `ATTACK_CARDINALITY = OPEN`
- `releases/current/**` remains outside the candidate.2 validation/freeze transition.

## Readback verdict

`PASS`

The project-manager handoff is now complete for the candidate.2 frozen state. The next permitted project-manager work is construction/audit of the blind semantic view and neutral fresh intake; substantive candidate.2 bytes must remain untouched.
