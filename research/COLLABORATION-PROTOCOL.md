# ENA Parallel Research Node Collaboration Protocol

Status: `RESEARCH-PROCESS / NON_NORMATIVE`

This protocol defines how multiple ChatGPT sessions or other participants may contribute to one ENA research lineage without silently creating multiple ENAs.

## Core topology

```text
Participant A ─┐
               ├→ Shared research/intake → Reconciliation → next flattened ENA release when justified
Participant B ─┘
```

The goal is **protocol-level unity with cognitive diversity**.

Parallel participants are independent research nodes. They are not replicas, do not share reliable live context, and should not assume that another participant already knows their most recent conclusions.

## Canonical project states

### Current adoption baseline

- Current adoption baseline: `ENA v0.3.2` at `releases/current/`.
- Status: `FIELD_VALIDATION / NOT_MAINLINE`.
- Current is one complete adoption world and is not composed with historical releases or research.

### Historical promoted Mainline

- Historical promoted baseline: `ENA v0.2.11 MAINLINE`.
- This historical promotion state remains part of lineage; it is not the current runtime/adoption dependency.

### Shared research/intake

GitHub Issues, `research/`, `collaboration/inbox/`, and related artifacts form the shared research desk.

They carry:

- review input;
- open questions;
- candidate abstractions;
- negative findings;
- host/reference evidence links;
- unresolved disagreements.

Default research/contribution state is not promoted merely because it is persisted.

### GitHub research lineage

GitHub records structured research state:

- Historical Adversarial Replay cases;
- candidate/evidence reconciliation;
- experiment plans;
- prototypes;
- issues and PRs;
- engineering decisions.

GitHub research artifacts do not acquire normative authority merely because they are committed.

## Context-dependent work

When a task depends on current ENA status or recent work by another participant:

1. re-read the latest relevant persisted artifacts;
2. verify the Current adoption identity;
3. read only the relevant Issue/research/contribution/reconciliation state;
4. only then continue local reasoning.

Do not rely only on session memory when persisted state may have changed. Do not load the entire project history when local retrieval is sufficient.

## Contribution discipline

A new finding should normally travel through:

`Capture → Compare → Classify → Persist → Reconcile → accumulate with other accepted changes → next flattened release when ROI justifies it`

Before naming a new mechanism or rule, ask:

1. Is the problem already covered by current ENA semantics?
2. Is it only a clarification or machine-legibility issue?
3. Is it host-specific?
4. Is this genuinely new evidence for an existing candidate?
5. Does it conflict with an existing candidate?
6. Is there repeated independent-domain evidence for a Universal gap?

Do not release a new adoption version merely because one new idea exists. Prefer a coherent batch whose integration/validation cost is justified.

## Duplicate and conflict handling

If another participant has already studied the same topic, do not independently rename/reinvent it by default.

Classify the relationship:

- `SAME_PROBLEM`
- `NEW_EVIDENCE`
- `COUNTEREXAMPLE`
- `DEEPER_BOUNDARY_CONDITION`
- `CONFLICTING_INTERPRETATION`
- `ALREADY_COVERED`

Conflicts must remain visible until reconciliation. Do not erase disagreement merely to make research nodes appear consistent.

## Authority of another research node

Another participant is not a higher-authority source merely because it produced a polished analysis.

Treat its output as a provenance-bearing research contribution subject to the same ENA standards:

- evidence grade;
- source/provenance and independence;
- scoped applicability;
- Current mapping;
- known limitations;
- reconciliation status.

## Reconciliation

Reconciliation is where parallel search paths are compared against the same persisted evidence and Current semantics.

A reconciliation result may:

- merge compatible formulations;
- downgrade a candidate to a worked example;
- mark a clarification gap;
- preserve competing hypotheses;
- reject a candidate;
- create a targeted experiment;
- accept an implementation candidate;
- eventually contribute to the next flattened release.

Reconciliation must preserve why a conclusion changed.

## Design principle

> Share lineage, evidence, and candidate state; do not attempt to synchronize personalities or force identical reasoning paths.

> Protocol-level unity + cognitive diversity.

This collaboration protocol is itself a research-process artifact, not an ENA Constitution rule.
