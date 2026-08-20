# ENA Parallel Research Node Collaboration Protocol

Status: `RESEARCH-PROCESS / NON_NORMATIVE`

This protocol defines how multiple ChatGPT sessions may contribute to one ENA research lineage without silently creating multiple ENAs.

## Core topology

```text
Session A ─┐
           ├→ Shared Evolution Inbox → Reconciliation → ENA Mainline
Session B ─┘
```

The goal is **protocol-level unity with cognitive diversity**.

Parallel sessions are independent research nodes. They are not replicas, do not share reliable live context, and should not assume that another session already knows their most recent conclusions.

## Canonical roles of persistence layers

### ENA Mainline

The current MAINLINE is the converged normative architecture.

- Current baseline: `ENA v0.2.11 MAINLINE`.
- Mainline is not modified merely because a research node proposes an elegant concept.
- GitHub is the diff-friendly engineering lineage from repository adoption onward.
- Validated release artifacts remain independently recoverable in Google Drive.

### Shared Evolution Inbox

Google Drive Evolution Inbox artifacts are the cross-session shared research desk.

They carry:

- review input;
- open questions;
- candidate abstractions;
- negative findings;
- host/reference evidence links;
- unresolved disagreements.

Default state:

`EVOLUTION_INBOX / REVIEW_INPUT or OPEN_QUESTION / NOT_PROMOTED`

Research may be mirrored into GitHub for structured diff, HAR linkage, issues, prototypes, and experiments. Mirroring does not promote the content.

### GitHub research lineage

GitHub records structured research state:

- Historical Adversarial Replay cases;
- candidate/evidence reconciliation;
- experiment plans;
- prototypes;
- issues and future PRs;
- engineering decisions.

GitHub research artifacts do not acquire normative authority merely because they are committed.

## Session-start discipline for context-dependent ENA work

When a task depends on current ENA status or recent work by another research node:

1. re-read the latest relevant persisted artifacts;
2. verify current MAINLINE identity;
3. read relevant shared Evolution Inbox material;
4. read current GitHub research/HAR state when applicable;
5. only then continue local reasoning.

Do not rely only on session memory when persisted state may have changed.

## Contribution discipline

A new finding should normally travel through:

`Capture → Compare → Classify → Persist → Reconcile → Promote only after evidence`

Before naming a new mechanism or rule, ask:

1. Is the problem already covered by current ENA semantics?
2. Is it only a clarification or machine-legibility issue?
3. Is it host-specific?
4. Is this genuinely new evidence for an existing candidate?
5. Does it conflict with an existing candidate?
6. Is there repeated independent-domain evidence for a Universal gap?

Only the last category creates serious pressure for a normative revision.

## Duplicate and conflict handling

If another session has already studied the same topic, do not independently rename/reinvent it by default.

Classify the relationship:

- `SAME_PROBLEM`
- `NEW_EVIDENCE`
- `COUNTEREXAMPLE`
- `DEEPER_BOUNDARY_CONDITION`
- `CONFLICTING_INTERPRETATION`
- `ALREADY_COVERED`

Conflicts must remain visible until reconciliation. Do not erase disagreement merely to make research nodes appear consistent.

## Authority of another research node

Another ChatGPT session is not a higher-authority source merely because it produced a polished analysis.

Treat its output as a provenance-bearing research contribution subject to the same ENA standards:

- evidence grade;
- source/provenance;
- scoped applicability;
- current Mainline mapping;
- known limitations;
- reconciliation status.

## Reconciliation

Reconciliation is where parallel search paths are compared against the same persisted evidence and Mainline semantics.

A reconciliation result may:

- merge compatible formulations;
- downgrade a candidate to a worked example;
- mark a clarification gap;
- preserve competing hypotheses;
- reject a candidate;
- create a targeted experiment;
- only with sufficient support, create a normative candidate change.

Reconciliation must preserve why a conclusion changed.

## Design principle

> Share lineage, evidence, and candidate state; do not attempt to synchronize personalities or force identical reasoning paths.

> Protocol-level unity + cognitive diversity.

This collaboration protocol is itself a research-process artifact, not an ENA Constitution rule.
