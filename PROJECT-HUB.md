# ENA Project Hub

Status: `PROJECT_ENTRYPOINT / CURRENT`

Project: **Evolution-Native Agent Architecture (ENA)**

This file is the standard entrypoint for any participant asked to continue, review, research, advise on, experiment on, or contribute to ENA.

Participants may include ChatGPT sessions, Gemini, OpenClaw, Hermes Agent, DeepSeek Harness, Codex, humans, bots, or other systems with access to at least one declared persistent project surface.

The participant does not need shared hidden context with previous participants. It needs legible persisted project state.

## Current canonical state

Formal baseline: **ENA v0.2.11 MAINLINE**

Release posture:

- adopted from v0.2.11 Candidate Revision 2;
- promotion transition complete;
- normative semantic delta from Candidate Revision 2: `NONE`;
- known DSH host defects remain visible;
- no v0.2.12 is currently open.

Do not infer that a research artifact, Issue, prototype, contribution, or committed file is part of MAINLINE unless it is explicitly promoted.

## First-read order

When the user says another session/agent has been working on ENA, or asks you to continue/review/contribute:

1. Read this file.
2. Read `README.md` for repository role and baseline identity.
3. Read `research/EVOLUTION-INBOX.md` for current unpromoted candidates.
4. Read `research/adversarial-replay/README.md` when the task concerns current research pressure or historical incidents.
5. Check `collaboration/inbox/` for unreconciled contributions from parallel participants.
6. Check `collaboration/reconciliation/` for prior handling of contributions.
7. Read only the specific MAINLINE/release/evidence artifacts needed for the task.

Do not rely only on remembered conversational context when persisted state may have changed.

## Global collaboration protocol

ENA adopts the **Persistent Project Collaboration Protocol**.

Global discovery index in Google Drive:
`Persistent Project Registry`

General protocol in Google Drive:
`Persistent Project Collaboration Protocol`

Core rules:

- persistent project state is the collaboration bus;
- tool access is connectivity, not project authority;
- one contribution should normally be one independent artifact;
- contribution and reconciliation are separate;
- conflicts remain visible until evidence/authorized decision resolves them;
- project continuity does not depend on one permanent owning session/agent.

## Shared persistence layers

### GitHub

Repository:
`guytogay/evolution-native-agent-architecture`

Role:

- diff-friendly engineering/research lineage;
- structured research;
- Issues / experiments / prototypes;
- collaboration contributions;
- future candidate/release work.

### Google Drive

Primary project folder:
`ChatGPT Knowledge`

Folder ID:
`1NjWvXzlvkt7xgOs4yDPfit5DlszUDsPr`

General discovery index:
`Persistent Project Registry`

General collaboration protocol:
`Persistent Project Collaboration Protocol`

Important ENA Drive artifacts include:

- validated ENA v0.2.11 MAINLINE release artifacts;
- ENA Historical Adversarial Replay Register;
- the living ENA research document;
- ENA GitHub fossil/adversarial review input;
- ENA Parallel Research Node Collaboration Protocol.

Drive is the durable artifact/research recovery layer. GitHub is the structured engineering/research lineage from repository adoption onward.

A participant may join with GitHub-only or Drive-only access, provided it follows the available entrypoint and does not claim access/persistence it does not have.

## Participant capability and authority

When materially relevant, contributors should make their access/capability legible:

```yaml
participant:
  kind: "ChatGPT | Gemini | OpenClaw | Hermes | DeepSeek Harness | Codex | Human | Bot | Other"
  runtime_or_model: "if known/useful"
  session_or_run_ref: "if available"
  access_surfaces:
    github: "NONE | READ | WRITE"
    google_drive: "NONE | READ | WRITE"
  role_this_contribution: "REVIEW_ONLY | CONTRIBUTOR | EXPERIMENTER | IMPLEMENTER | STEWARD | OTHER"
```

These fields describe provenance and technical capability, not project authority.

**GitHub WRITE != authority to change ENA MAINLINE.**

**Drive WRITE != authority to promote research or rewrite evidence.**

Implementation/promotion/remediation authority must be separately justified.

## Where parallel participants should contribute

Do **not** normally edit one shared Inbox file concurrently.

Create a new contribution under:

`collaboration/inbox/`

Preferred filename:

`YYYY-MM-DD-HHMM-<short-topic>.md`

Use `collaboration/CONTRIBUTION-TEMPLATE.md` when useful.

A contribution can contain:

- advice;
- new evidence;
- a counterexample;
- a conflicting interpretation;
- a design concern;
- a historical incident;
- a clarification suggestion;
- a proposed experiment;
- a negative result;
- implementation review.

Default contribution status:

`UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED`

## Reconciliation

The participant currently acting as Project Steward should review new contribution files during substantive ENA maintenance.

Reconciliation records belong under:

`collaboration/reconciliation/`

Possible outcomes:

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

Do not delete or rewrite the original contribution merely because it was reconciled.

## Current research posture

Historical Adversarial Replay checkpoint:

`10 HAR cases -> 0 NORMATIVE_GAP`

Current high-priority research:

1. Evidence Applicability contract falsification on DSH — GitHub Issue #4.
2. Session Context Lineage clean-session counterfactual — GitHub Issue #3.
3. Influence Integrity / Persuasion Boundary as an open cross-cutting vector touching Evidence/Claim support, Authorization, and Governance Salience.

Current discipline:

> Falsify before formalize.

> Historical Failure Coverage ↑ while Universal Semantic Complexity stays stable or decreases.

## Modification guardrails

Review/research access does not automatically authorize MAINLINE changes.

Do not silently:

- create v0.2.12;
- edit Constitution/Capability/Validation semantics because a candidate sounds elegant;
- promote a contribution because another model/agent proposed it;
- remediate unrelated DSH defects;
- erase conflicting interpretations to make participants agree;
- confuse review/advice authority with implementation authority;
- use a technically available write path as proof of mandate.

## Collaboration topology

```text
ChatGPT ─┐
Gemini  ─┤
Hermes  ─┤
DSH     ─┼→ independent contribution/evidence → reconciliation → candidate → MAINLINE only when justified
OpenClaw─┤
Human   ─┤
Other   ─┘
```

Participants do not need shared live context.

They need shared discoverability, lineage, evidence, contribution state, and explicit authority boundaries.

> Persistent project state is the collaboration bus.

> Protocol-level unity + cognitive diversity + implementation diversity.
