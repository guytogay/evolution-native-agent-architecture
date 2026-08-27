# ENA v0.3.7 candidate.1 post-freeze independence decision

Date: 2026-08-27

## Decision

`FRESH_BLIND_SUCCESSOR_REVIEW_WARRANTED / ONE_REVIEW_CYCLE / NOT_RELEASE_AUTHORITY`

Frozen target:

- identity: `v0.3.7-candidate.1`
- exact source commit: `ae6903464133cb5bcf3cd8909ecae1215fe0b9ba`
- exact candidate subtree: `c0458e0d7ea417b841cbf4c8bf6e64e4aff37319`
- exact pre-freeze gate: workflow run `33055811978` — SUCCESS
- freeze record: `collaboration/reconciliation/2026-08-27-v037-candidate1-freeze.md`

Current remains `v0.3.6 / CURRENT / FIELD_VALIDATION` and is not changed by this decision.

## Why another fresh blind review pays epistemic rent

This is not a ritual requirement that every successor must always be independently re-reviewed.

A fresh blind inspection is warranted here because all of the following are simultaneously true:

1. candidate.1 contains **material executable/validator corrections**, not only prose or packaging changes;
2. those corrections govern chronology, represented history, migration provenance, and validation behavior — surfaces that can create both false confidence and false blocking if subtly wrong;
3. the predecessor's fresh blind Phase A found material defects that the author-side attack corpus had missed, demonstrating that the author/project-manager search map was not sufficient by itself;
4. candidate.1 targeted and focused regressions show that the known defects were repaired, but those checks were built after the findings were known and therefore do not restore search-space independence;
5. the exact candidate.1 tree is now frozen, so an independent reviewer can inspect a stable target without moving-target ambiguity.

Therefore one fresh blind review of the exact frozen candidate.1 bytes has a clear information gain: it asks whether a reviewer who has not inherited the author attack map discovers materially different failure or false-block shapes in the successor itself.

## Why this is not endless validation

The authorized next independent step is **one fresh blind review cycle** against this exact frozen tree.

It is not a claim that validation must continue until no reviewer can imagine another test.

After the fresh report is sealed:

- if it identifies a material candidate-byte defect, candidate.1 remains frozen occurrence truth and any correction requires candidate.2;
- if it identifies oracle/test defects, evidence-boundary issues, intentional residuals, or non-contract possibilities, reconcile those without mutating candidate.1 merely to manufacture closure;
- if it finds no material blocker after independent inspection, proceed to Phase B evidence reconciliation and release decision work;
- attack cardinality remains `OPEN` in every outcome.

A later candidate.2, if required, would receive its own post-freeze independence decision based on semantic radius and evidence need; fresh review is not inherited as an automatic infinite loop.

## Information-boundary requirement

The fresh reviewer must not be primed with:

- candidate.0 Phase-A findings;
- candidate.1 repair descriptions;
- author attack harness conclusions;
- targeted/open-branch expected observations;
- reconciliation verdicts;
- this decision's detailed rationale beyond the fact that a fresh blind review is requested.

Before sealing Phase A, provide only the minimal blind entry, exact frozen identity, the candidate bytes themselves, and neutral task instructions.

The reviewer must grow its own attack tree from the frozen implementation and its represented contracts.

## Next governed action

`CANDIDATE1_FRESH_BLIND_PHASE_A`

Use:

`collaboration/reconciliation/2026-08-27-v037-candidate1-blind-phase-a-entry.md`

The report must be committed and sealed before author-side context is opened.
