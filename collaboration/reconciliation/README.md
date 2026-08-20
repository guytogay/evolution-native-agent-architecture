# ENA Collaboration Reconciliation

Status: `RECONCILIATION_LAYER / NON_NORMATIVE_UNTIL_PROMOTED_OR_ACCEPTED`

This directory records how persisted participant contributions are compared against current ENA state, evidence, existing candidates, authority, and implementation reality.

A reconciliation record is separate from the original contribution. It should identify the contribution(s) being reviewed and produce an explicit outcome without rewriting source history.

## Suggested outcomes

- `ACCEPT_AS_EVIDENCE`
- `ACCEPT_AS_CLARIFICATION`
- `MERGE_WITH_EXISTING_CANDIDATE`
- `ALREADY_COVERED`
- `NEEDS_EXPERIMENT`
- `ACCEPT_FOR_IMPLEMENTATION`
- `DEFER`
- `REJECT_WITH_REASON`
- `PRESERVE_CONFLICT`
- `UNKNOWN`

## Required distinctions

A reconciliation should distinguish:

- contribution content;
- evidence actually verified;
- inference/current ENA mapping;
- conflict/overlap with existing state;
- outcome;
- next action;
- authority used for any implementation or promotion.

Use `../RECONCILIATION-TEMPLATE.md` when useful.

## Drive-side reconciliation

Google Drive path:

`My Drive / 10 Projects / ENA - Evolution-Native Agent Architecture / 50 Collaboration / 20 Reconciliation`

If one surface is used as a bridge for another, preserve the original contribution reference and semantic status.

## Discipline

Reconciliation may change the project’s understanding of a contribution, but should not rewrite the original contribution history.

If competing interpretations remain plausible, preserve the conflict rather than forcing consensus.

Reconciliation != promotion.

Acceptance as evidence != implementation authority.

Implementation/promotion still requires the project’s normal evidence, authority, and release process.
