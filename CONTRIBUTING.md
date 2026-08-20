# Contributing to ENA

ENA uses the **Persistent Project Collaboration Protocol**. This guide applies to humans, ChatGPT sessions, Gemini, OpenClaw, Hermes Agent, DeepSeek Harness, Codex, bots, and other participants.

## Start here

Before contributing:

1. Read `PROJECT-HUB.md`.
2. Read `PROJECT-METADATA.yaml` for current paths, status, and surface roles.
3. Read only the relevant current Mainline/research/evidence material.
4. Check `collaboration/inbox/` and `collaboration/reconciliation/` when your work may overlap another participant.

Do not rely only on remembered conversation/session context when persisted state may have changed.

## Contribution is not authority

Technical write access does not establish project authority.

- GitHub WRITE != authority to change ENA MAINLINE.
- Drive WRITE != authority to promote research or rewrite evidence.
- Ability to deploy != authorization to deploy.
- Ability to remediate != remediation mandate.
- Review/advice authority != implementation or release authority.

Unless the user/project explicitly authorizes a canonical change, default to a contribution/research artifact rather than a Mainline edit.

## Normal contribution path

For advice, research, evidence, counterexamples, design concerns, negative findings, experiment proposals, or conflicting interpretations:

1. Create **one independent artifact per contribution** under `collaboration/inbox/`.
2. Prefer filename:
   `YYYY-MM-DD-HHMM-<participant-or-source>-<short-topic>.md`
3. Use `collaboration/CONTRIBUTION-TEMPLATE.md` when useful.
4. Default status:
   `UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED`
5. Do not append unrelated contributions into one giant shared Inbox file.

## Recommended contribution header

```yaml
project: ena
artifact_type: CONTRIBUTION
status: UNRECONCILED
created_at: "<ISO-8601 with timezone>"
participant:
  kind: "Human | ChatGPT | Gemini | OpenClaw | Hermes | DeepSeek Harness | Codex | Bot | Other"
  runtime_or_model: "<if useful/known>"
  session_or_run_ref: "<if available>"
  access_surfaces:
    github: "NONE | READ | WRITE"
    google_drive: "NONE | READ | WRITE"
source_refs: []
related_artifacts: []
authority_note: "advice only | experiment authorized | implementation authorized | unknown"
```

Use `UNKNOWN` rather than inventing provenance.

## Separate fact from interpretation

A useful contribution distinguishes:

- observed facts;
- inference;
- suggestion/question;
- evidence references;
- known limitations/unknowns;
- requested reconciliation;
- authority/implementation note.

A polished argument is not automatically stronger evidence.

## Reconciliation

A participant acting as Project Steward should reconcile contributions in a separate artifact under `collaboration/reconciliation/`.

Use `collaboration/RECONCILIATION-TEMPLATE.md`.

Possible outcomes include:

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

Never delete or rewrite the original contribution merely because it has been reconciled.

## Research changes

Current formal baseline: **ENA v0.2.11 MAINLINE**.

No v0.2.12 is currently open.

Research should normally follow:

`incident/evidence → current ENA mapping → false claim/boundary → replay/experiment → clarification or candidate → promotion only after evidence`

Prefer the smallest layer that closes the problem:

`example → clarification → schema/template → validator → host implementation → normative change`

Do not create a new Constitution/Capability simply because an abstraction is elegant.

## Direct canonical edits

Direct edits to accepted specification/Mainline content are appropriate only when the task carries sufficient implementation/promotion authority and the required evidence/review conditions are satisfied.

When in doubt, create a contribution, experiment, prototype, or decision proposal instead.

## Decisions

Material changes to project structure, collaboration semantics, release process, canonical-state interpretation, or other durable architecture should receive a decision record under `decisions/`.

Use `decisions/ADR-TEMPLATE.md`.

## Persistent surfaces

GitHub is ENA's diff-friendly engineering/research lineage from repository adoption onward.

Google Drive project root:

`My Drive / 10 Projects / ENA - Evolution-Native Agent Architecture`

Drive supports durable release artifacts, human-readable reports, Drive-only discovery/contributions, and independent recovery anchors.

Copy != synchronization. If you mirror semantic state across surfaces, label it as `CANONICAL`, `MIRROR`, `SNAPSHOT`, `INDEX`, `BRIDGE`, `BACKUP`, or `ARCHIVE`.

## Core discipline

> Falsify before formalize.

> Historical Failure Coverage ↑ while Universal Semantic Complexity stays stable or decreases.
