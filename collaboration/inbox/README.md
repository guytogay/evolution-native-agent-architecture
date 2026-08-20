# ENA Collaboration Inbox

Status: `CONTRIBUTION_INBOX / NON_NORMATIVE`

This directory receives independent contributions from humans, ChatGPT sessions, Gemini, OpenClaw, Hermes Agent, DeepSeek Harness, Codex, bots, or other project participants.

## Default behavior

Prefer **one artifact per contribution** instead of multiple participants editing one shared Inbox file.

Preferred filename:

`YYYY-MM-DD-HHMM-<participant-or-source>-<short-topic>.md`

Use `../CONTRIBUTION-TEMPLATE.md` when useful.

The artifact body should carry an offset-aware `created_at` timestamp when available; filename time is a sorting aid, not authoritative chronology.

## Allowed contribution types

- review input;
- evidence;
- counterexample;
- open question;
- historical incident;
- conflicting interpretation;
- clarification suggestion;
- experiment proposal;
- negative result;
- implementation concern/review.

## Default semantic status

A file appearing here means only:

`PERSISTED CONTRIBUTION / UNRECONCILED`

It does **not** mean:

`ACCEPTED`
`PROMOTED`
`AUTHORIZED FOR IMPLEMENTATION`
`MAINLINE`

Tool access is connectivity, not project authority.

## Drive-only participants

Google Drive contribution surface:

`My Drive / 10 Projects / ENA - Evolution-Native Agent Architecture / 50 Collaboration / 10 Inbox`

If a contribution is bridged between Drive and GitHub, preserve participant provenance and original semantic status. Do not transform “participant proposed X” into “project decided X”.

## After contribution

A Project Steward or authorized maintainer should inspect new contributions and create a separate reconciliation record under `../reconciliation/`.

Original contributions should normally remain preserved after reconciliation.
