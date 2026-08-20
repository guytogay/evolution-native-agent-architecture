# ENA Cross-Session Reconciliation

Status: `RECONCILIATION_LAYER / NON_NORMATIVE_UNTIL_PROMOTED`

This directory records how persisted cross-session contributions were compared against current ENA state, evidence, and existing candidates.

A reconciliation record should identify the contribution(s) being reviewed and produce an explicit outcome.

## Suggested outcomes

- `ACCEPT_AS_EVIDENCE`
- `ACCEPT_AS_CLARIFICATION`
- `MERGE_WITH_EXISTING_CANDIDATE`
- `ALREADY_COVERED`
- `NEEDS_EXPERIMENT`
- `DEFER`
- `REJECT_WITH_REASON`
- `PRESERVE_CONFLICT`

## Suggested structure

Contribution refs:
Reviewer / project node:
Date:
Current MAINLINE:
Relevant existing candidate/rule:
Evidence reviewed:
Conflict or overlap:
Outcome:
Reasoning summary:
Follow-up issue / experiment / PR:
Normative status after reconciliation:

## Discipline

Reconciliation may change the project’s understanding of a contribution, but should not rewrite the original contribution history.

If competing interpretations remain plausible, preserve the conflict rather than forcing consensus.

Reconciliation ≠ promotion.

Promotion or implementation still requires the project’s normal evidence, authority, and release process.
