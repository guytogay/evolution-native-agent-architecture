# Contributing to ENA

ENA welcomes contributions from humans, ChatGPT sessions, Gemini, OpenClaw, Hermes, DeepSeek Harness, Codex, bots, and other legitimate participants.

## Start here

1. Read `PROJECT-HUB.md`.
2. For current adoption semantics, use only `releases/current/`.
3. Read/search research, evidence, history, Inbox, and prior reconciliation when useful to the task; do not load everything by default.
4. Check `collaboration/inbox/` and `collaboration/reconciliation/` when your work may overlap another contribution.

Current adoption baseline: **ENA v0.3.1-BETA.1**.

Do not compose it with older releases/candidates.

## Open participation, scoped authority

All legitimate participants may, within their actual capability and authority:

- read and search project knowledge;
- question and critique ENA;
- research alternatives;
- propose mechanisms/hypotheses;
- perform bounded experiments;
- contribute evidence and field experience.

Technical access does not grant consequential project authority.

- GitHub WRITE != Mainline/promotion authority.
- Drive WRITE != promotion authority.
- Ability to deploy != authorization to deploy.
- Review/advice != implementation authority.
- Field use != authority to rewrite the shared baseline.

> Knowledge is commons. Inquiry is open. Authority is scoped. Adoption is governed.

## Normal contribution path

Create one independent artifact per material contribution under `collaboration/inbox/`.

Recommended filename:

`YYYY-MM-DD-HHMM-<participant-or-source>-<short-topic>.md`

Useful classes:

`INCIDENT | NEAR_MISS | FRICTION | VALUE_OBSERVED | COUNTEREXAMPLE | PORTABILITY_FINDING | NEW_VARIATION | EVIDENCE_RESULT | RESEARCH_HYPOTHESIS | CRITIQUE`

For field use, `releases/current/templates/field-experience.v1.yaml` is an optional source format.

Default status:

`UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED`

## Evidence hygiene

Separate:

- observed facts;
- inference/interpretation;
- suggestion/hypothesis;
- evidence references;
- applicability envelope;
- known limitations/unknowns;
- authority/implementation status.

A polished argument is not automatically stronger evidence. Use `UNKNOWN` rather than inventing provenance.

## Reconciliation

Reconciliation is a separate artifact under `collaboration/reconciliation/`; do not rewrite the original contribution merely because it has been handled.

Possible outcomes include:

`ACCEPT_AS_EVIDENCE`, `ACCEPT_AS_CLARIFICATION`, `MERGE_WITH_EXISTING_CANDIDATE`, `ALREADY_COVERED`, `NEEDS_EXPERIMENT`, `ACCEPT_FOR_IMPLEMENTATION`, `DEFER`, `REJECT_WITH_REASON`, `PRESERVE_CONFLICT`, `UNKNOWN`.

## Research / Beta evolution

Prefer:

`incident/evidence -> current baseline mapping -> concrete false claim/value/friction -> cheapest decision-changing test -> contribution/reconciliation -> next Beta/RC/Mainline decision`

Choose the smallest layer that closes the problem. Do not create a Constitution rule merely because an abstraction is elegant.

Current Beta field-validation tracker: GitHub Issue #5.

## Persistent surfaces

GitHub is the diff-friendly current adoption/research lineage surface.

Google Drive project root:

`My Drive / 10 Projects / ENA - Evolution-Native Agent Architecture`

Drive is a durable artifact/research/evidence/recovery surface, not another runtime version layer.

> Persistence != synchronization.

> Preserve history durably; retrieve history selectively.
