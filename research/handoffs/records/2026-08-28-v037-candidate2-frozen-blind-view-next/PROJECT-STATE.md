# Project state — 2026-08-28

## Current

- version: `v0.3.6`
- status: `CURRENT / FIELD_VALIDATION`
- Current subtree observed through candidate.2 exact gate: `7dcbb3934883ffa6cc5292a662588cafc1533cff`
- candidate work does not authorize Current mutation.

## Frozen candidate lineage

### candidate.0

- identity: `v0.3.7-candidate.0`
- source: `d0e793593184740d9732902e948afd48ed96ae2f`
- subtree: `cffbf76fe1448b020b637c78d1f7ae46e4c0115b`
- fresh Phase-A seal: `5ba3d241efa460fe170253860ad67045aa1d96a5`
- verdict: `NEEDS_REVISION`

### candidate.1

- identity: `v0.3.7-candidate.1`
- source: `ae6903464133cb5bcf3cd8909ecae1215fe0b9ba`
- subtree: `c0458e0d7ea417b841cbf4c8bf6e64e4aff37319`
- fresh semantic A-S seal: `2e6b46aeedc1945a03aac93620ad36aa1ccbd70f`
- A-P completion: `b970148fe9596ea9cad0a2817a3b399a1d2b75f5`
- verdict: `NEEDS_REVISION / SUPERSEDED_BY_CANDIDATE2`

### candidate.2

- identity: `v0.3.7-candidate.2`
- frozen source: `bda470e0a6b170cec61225a905957a501454a2fe`
- frozen subtree: `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`
- exact pre-freeze run: `33095987843 / SUCCESS`
- repair reconciliation: `collaboration/reconciliation/2026-08-28-v037-candidate2-successor-repair-reconciliation.md`
- freeze record: `collaboration/reconciliation/2026-08-28-v037-candidate2-freeze.md`
- post-freeze independence decision: `collaboration/reconciliation/2026-08-28-v037-candidate2-post-freeze-independence-decision.md`
- status: `FROZEN / NOT_CURRENT / NOT_RELEASED`
- material correction rule: `CANDIDATE3_REQUIRED`
- attack cardinality: `OPEN`

## Candidate.2 repair evidence

- focused repair run `33090294820`, cargo `613c1e8be898865ce674199118618c0f9389da97`
- open-branch observation run `33090585653`
- round-2 repair run `33091573678`, cargo `34458c2ba0b94b82d182afe2606efe48e741bcda`
- committed re-probe run `33091652046`
- pre-freeze status transition run `33095122958`, final candidate cargo `aba6f12cabc84146c92809bd7d8293a3c907dc55`
- exact pre-freeze successful run `33095987843`, tested source `bda470e0a6b170cec61225a905957a501454a2fe`

Two earlier exact-gate attempts were validation-tooling defects only and did not alter candidate subtree:

- `33095464230` — incorrect schema-title normalization oracle
- `33095677352` — incorrect Authority harness API call

## Immediate project phase

`CANDIDATE2_FROZEN / FRESH_BLIND_SEMANTIC_VIEW_PREPARATION_NEXT`

One fresh A-S -> A-P cycle is warranted. It is a search-space independence check, not a completeness ritual.

The current project-manager session has material prior exposure and is ineligible to claim fresh A-S.
