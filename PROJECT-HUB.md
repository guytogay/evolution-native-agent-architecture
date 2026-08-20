# ENA Project Hub

Status: `PROJECT_ENTRYPOINT / CURRENT`

Project: **Evolution-Native Agent Architecture (ENA)**

This is the stable entrypoint for any participant asked to continue, review, research, advise on, experiment on, or contribute to ENA. Participants may include ChatGPT sessions, Gemini, OpenClaw, Hermes Agent, DeepSeek Harness, Codex, humans, bots, or other systems with access to at least one declared persistent project surface.

The participant does not need shared hidden context with previous participants. It needs legible persisted project state.

## Current canonical state

Formal baseline: **ENA v0.2.11 MAINLINE**

- adopted from v0.2.11 Candidate Revision 2;
- promotion transition complete;
- normative semantic delta from Candidate Revision 2: `NONE`;
- known DSH host defects remain visible;
- no v0.2.12 is currently open.

Do not infer that a research artifact, Issue, prototype, contribution, committed file, or Drive document is part of MAINLINE unless it is explicitly promoted.

Machine-readable navigation/state: `PROJECT-METADATA.yaml`.

## First-read order

1. Read this file.
2. Read `PROJECT-METADATA.yaml` for exact surface paths and IDs.
3. Read `README.md` for repository role and baseline identity.
4. Read `research/evolution-inbox/README.md` for current unpromoted candidate state.
5. Read `research/adversarial-replay/README.md` when the task concerns current research pressure or historical incidents.
6. Check `collaboration/inbox/` for unreconciled GitHub-side contributions.
7. Check `collaboration/reconciliation/` for prior handling of contributions.
8. If Drive is available, check the Drive Project Hub and Drive Collaboration Inbox for Drive-only contributions.
9. Read only the specific MAINLINE/release/evidence artifacts needed for the task.

Compatibility: `research/EVOLUTION-INBOX.md` remains as a pointer for older participants.

## Global collaboration infrastructure

ENA adopts the **Persistent Project Collaboration Protocol** and **Persistent Project Structure and Naming Standard**.

Google Drive global discovery:

`My Drive / 00 Persistent Collaboration`

Key global artifacts:

- `00 START HERE - Persistent Project Collaboration`
- `Persistent Project Registry`
- `Persistent Project Collaboration Protocol`
- `Persistent Project Structure and Naming Standard`
- `Persistent Project Collaboration Bootstrap Template`

Core rules:

- project-first, not Agent-first;
- persistent project state is the collaboration bus;
- tool access is connectivity, not project authority;
- one contribution should normally be one independent artifact;
- contribution and reconciliation are separate;
- conflicts remain visible until evidence/authorized decision resolves them;
- copy is not synchronization;
- project continuity does not depend on one permanent owning session/agent.

## Persistent surfaces

### GitHub

Repository: `guytogay/evolution-native-agent-architecture`

Role: diff-friendly engineering/research lineage, structured research, Issues, experiments, prototypes, contributions, future candidate/release work.

Primary paths:

- Evolution Inbox: `research/evolution-inbox/`
- Historical Adversarial Replay: `research/adversarial-replay/`
- Experiments: `research/experiments/`
- Prototypes: `research/prototypes/`
- Contributions: `collaboration/inbox/`
- Reconciliation: `collaboration/reconciliation/`
- Decisions: `decisions/`

### Google Drive

Project root:

`My Drive / 10 Projects / ENA - Evolution-Native Agent Architecture`

Folder ID: `1uRMP44TsHEhiJZG8Jcc4ja3UHpyZqRmi`

Stable Drive entrypoint:

`00 Project Hub / ENA - PROJECT HUB`

Drive layout:

- `10 Mainline`
- `20 Research / 00 Evolution Inbox`
- `20 Research / 10 Historical Adversarial Replay`
- `20 Research / 20 Experiments`
- `20 Research / 30 Prototypes`
- `30 Evidence / 10 DSH`
- `30 Evidence / 20 Historical and External`
- `40 Releases / 10 Current`
- `40 Releases / 90 Archive`
- `50 Collaboration / 10 Inbox`
- `50 Collaboration / 20 Reconciliation`
- `50 Collaboration / 30 Templates`
- `60 Decisions`
- `90 Archive`

Drive role: durable release artifacts, human-readable research/evidence reports, Drive-only discovery/contributions, and independent recovery anchors.

`ChatGPT Knowledge` is now a legacy/general knowledge location, **not** the ENA project root.

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

Implementation, promotion, deployment, remediation, and scope-expansion authority must be separately justified.

## Contribution workflow

Do **not** normally edit one shared Inbox file concurrently.

GitHub contribution: create one independent artifact under `collaboration/inbox/`.

Drive-only contribution: create one independent artifact under `50 Collaboration / 10 Inbox`.

Preferred GitHub filename:

`YYYY-MM-DD-HHMM-<participant-or-source>-<short-topic>.md`

Use `collaboration/CONTRIBUTION-TEMPLATE.md` when useful.

Default status:

`UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED`

## Reconciliation

Reconciliation is a separate artifact; never rewrite the original contribution merely because it was handled.

GitHub: `collaboration/reconciliation/`

Drive: `50 Collaboration / 20 Reconciliation`

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

## Current research posture

Historical Adversarial Replay checkpoint:

`10 HAR cases -> 0 NORMATIVE_GAP`

Current high-priority research:

1. Evidence Applicability contract falsification on DSH — Issue #4.
2. Session Context Lineage clean-session counterfactual — Issue #3.
3. Influence Integrity / Persuasion Boundary — open cross-cutting research vector.

Current discipline:

> Falsify before formalize.

> Historical Failure Coverage ↑ while Universal Semantic Complexity stays stable or decreases.

## Modification guardrails

Do not silently:

- create v0.2.12;
- edit Constitution/Capability/Validation semantics because a candidate sounds elegant;
- promote a contribution because another participant proposed it;
- remediate unrelated DSH defects;
- erase conflicting interpretations to make participants agree;
- confuse review/advice authority with implementation authority;
- use a technically available write path as proof of mandate.

Participants need shared discoverability, lineage, evidence, contribution state, and explicit authority boundaries—not shared hidden internal state.
