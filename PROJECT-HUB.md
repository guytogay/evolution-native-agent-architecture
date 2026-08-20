# ENA Project Hub

Status: `PROJECT_ENTRYPOINT / CURRENT`

Project: **Evolution-Native Agent Architecture (ENA)**

This file is the standard cross-session entrypoint for any ChatGPT session that is asked to continue, review, research, advise on, or contribute to ENA.

## Current canonical state

Formal baseline: **ENA v0.2.11 MAINLINE**

Release posture:

- adopted from v0.2.11 Candidate Revision 2;
- promotion transition complete;
- normative semantic delta from Candidate Revision 2: `NONE`;
- known DSH host defects remain visible;
- no v0.2.12 is currently open.

Do not infer that a research artifact, Issue, prototype, or contribution is part of MAINLINE unless it is explicitly promoted.

## First-read order for cross-session work

When the user says another session has been working on ENA, or asks you to continue/review ENA:

1. Read this file.
2. Read `README.md` for repository role and baseline identity.
3. Read `research/EVOLUTION-INBOX.md` for current unpromoted candidates.
4. Read `research/adversarial-replay/README.md` when the task concerns current research pressure or historical incidents.
5. Check `collaboration/inbox/` for contributions from parallel sessions.
6. Check `collaboration/reconciliation/` for resolved/merged/rejected contribution state.
7. Read only the specific MAINLINE/release/evidence artifacts needed for the task.

Do not rely only on remembered chat context when persisted state may have changed.

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

Global project discovery index:
`ChatGPT Project Registry`

Global cross-session protocol:
`ChatGPT Cross-Session Project Collaboration Protocol`

Important ENA Drive artifacts include:

- validated ENA v0.2.11 MAINLINE release artifacts;
- ENA Historical Adversarial Replay Register;
- the living ENA research document;
- ENA GitHub fossil/adversarial review input;
- ENA Parallel Research Node Collaboration Protocol.

Drive is the durable artifact/research recovery layer. GitHub is the structured engineering/research lineage from repository adoption onward.

## Where parallel sessions should contribute

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
- a negative result.

Default contribution status:

`UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED`

## Reconciliation

Project-maintaining sessions should review new contribution files without surprise.

Reconciliation records belong under:

`collaboration/reconciliation/`

Possible outcomes:

- `ACCEPT_AS_EVIDENCE`
- `ACCEPT_AS_CLARIFICATION`
- `MERGE_WITH_EXISTING_CANDIDATE`
- `ALREADY_COVERED`
- `NEEDS_EXPERIMENT`
- `DEFER`
- `REJECT_WITH_REASON`
- `PRESERVE_CONFLICT`

Do not delete the original contribution merely because it was reconciled.

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

Parallel review/research does not automatically authorize MAINLINE changes.

Do not silently:

- create v0.2.12;
- edit Constitution/Capability/Validation semantics because a candidate sounds elegant;
- promote a contribution because another ChatGPT session proposed it;
- remediate unrelated DSH defects;
- erase conflicting interpretations to make sessions agree;
- confuse review/advice authority with implementation authority.

## Cross-session model

```text
Session A ─┐
Session B ─┼→ contribution / evidence → reconciliation → candidate → MAINLINE only when justified
Session C ─┘
```

The sessions do not need shared live context.

They need shared discoverability, lineage, evidence, and contribution state.

> Protocol-level unity + cognitive diversity.
