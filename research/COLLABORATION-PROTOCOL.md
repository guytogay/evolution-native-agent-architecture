# ENA Parallel Research Node Collaboration Protocol

Status: `RESEARCH-PROCESS / NON_NORMATIVE`

This protocol defines how multiple ChatGPT sessions or other participants may contribute to one ENA research lineage without silently creating multiple ENAs or silently regressing the research method.

## Core topology

```text
Participant A ─┐
               ├→ Shared research/intake → Reconciliation → selection/release only when justified
Participant B ─┘
```

The goal is **protocol-level unity with cognitive diversity**.

Parallel participants are independent research nodes. They are not replicas, do not share reliable live context, and must not assume that another participant already knows the latest conclusions or methodology.

## Research bootstrap

Before substantive continuation, read:

1. `research/RESEARCH-START-HERE.md`;
2. `research/methodology/ENA-RESEARCH-DISCIPLINE.md`;
3. PR #82 and master reconstruction ledger #89;
4. only then the relevant workstream/issues/prototypes.

Do not hard-code the Current adoption version in this process file. Verify the actual Current identity from:

`releases/current/CURRENT-BASELINE.yaml`

on the default branch.

## Shared research/intake

GitHub Issues, `research/`, collaboration/intake artifacts, prototypes, PRs, and evidence files form the shared research desk.

They may carry:

- review input;
- open questions;
- candidate abstractions;
- concrete HOWs/reference organs;
- negative findings;
- Host/reference evidence links;
- unresolved disagreements;
- research-method corrections.

Persistence does not create normative authority, but persistence is required for durable inheritance.

```text
PERSISTED != CURRENT
PERSISTED != VERIFIED
PERSISTED != SALIENT
PERSISTED != APPLIED
```

## Context-dependent work

When a task depends on current ENA status or recent work by another participant:

1. verify Current identity from its canonical machine carrier;
2. read the small research bootstrap;
3. retrieve the relevant canonical methodology/ledger/workstream state;
4. if a prior-session export exists and recent methodology changed near its end, inspect the methodology-bearing tail rather than relying only on a compressed summary;
5. only then choose a substantive next action.

Do not load the entire project history when targeted cold retrieval is sufficient. Do not rely only on session memory or summary when persisted state exists.

## Method inheritance is behavioral

A participant has not successfully inherited the methodology merely because it can quote it.

Use the same activation distinction ENA applies elsewhere:

```text
WRITTEN -> RETRIEVED -> INTERPRETED -> SALIENT -> APPLIED
```

A successor that reads anti-dissolution rules and then immediately compresses plural concrete HOWs into one abstract principle has failed methodology inheritance at the salience/application layer.

## Contribution discipline

A new finding should normally travel through:

`Capture → Compare → Classify → Persist → Reconcile → select/retain/specialize/retire when evidence justifies it`

Before naming or selecting a mechanism, ask:

- What WHAT/WHY failure or property is involved?
- What concrete HOW lineage already exists, including Host-specific, dormant, failed, historical, or competing variants?
- Does Current cover only the parent property, or does a usable organ actually exist?
- Can multiple HOWs legitimately coexist under the same WHAT/WHY?
- Am I selecting before relevant historical variation has been recovered?
- What Host conditions change applicability/fitness?
- What evidence could change the decision?
- Could `NO_CHANGE`, dormancy, simplification, or multiple surviving branches be the correct result?

Never use `already covered`, `Host-specific`, `no Core delta`, or `reference organ` as automatic closure operators.

```text
CURRENT_ALREADY_COVERS_PARENT_PROPERTY
!= PRACTICAL_PROBLEM_SOLVED
```

## Compression boundary

Core semantic compression remains useful for WHAT/WHY. It must not silently erase concrete operational branches.

```text
WHAT / WHY
    |
    +--> HOW-A
    +--> HOW-B
    +--> HOW-C
    +--> ...
```

The number and boundaries of HOWs are discovered, not preallocated.

> **Compress the semantic trunk; let concrete HOWs branch.**

## Duplicate and conflict handling

If another participant has already studied the same topic, do not independently rename/reinvent it by default.

Classify the relationship where useful:

- `SAME_PROBLEM`
- `NEW_EVIDENCE`
- `COUNTEREXAMPLE`
- `DEEPER_BOUNDARY_CONDITION`
- `CONFLICTING_INTERPRETATION`
- `PARENT_PROPERTY_ALREADY_COVERED`
- `COMPETING_HOW`
- `HOST_SPECIALIZATION`

`PARENT_PROPERTY_ALREADY_COVERED` does not imply organ closure.

Conflicts and competing HOWs may remain visible until selection evidence exists. Do not erase disagreement or variation merely to make research nodes appear consistent.

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

Reconciliation may:

- merge compatible formulations;
- retain multiple concrete HOWs under one property;
- specialize a HOW by Host/condition;
- downgrade a candidate to a worked example;
- mark a clarification or implementation gap;
- preserve competing hypotheses;
- reject or retire a candidate with lineage preserved;
- create a targeted experiment only when it can pay epistemic rent;
- accept an implementation candidate;
- eventually contribute to a release when a real release delta exists.

Reconciliation must preserve why a conclusion changed.

## Handoff discipline

Before ending a session after a material research-method or architecture change:

- persist the change in GitHub;
- update the obvious research entrypoint/pointer if future action depends on it;
- do not rely on a chat summary as the only carrier;
- distinguish current action state from historical discussion;
- leave enough routing information for a fresh participant to retrieve the exact cold sources.

The purpose is not to reproduce the whole session. It is to preserve the **decision-changing state and the method required to interpret it correctly**.

## Design principle

> Share lineage, evidence, candidate state, and research method; do not attempt to synchronize personalities or force identical reasoning paths.

> **Protocol-level unity + cognitive diversity.**

> **Do not merely inherit conclusions. Inherit the method that governs how new conclusions may be produced.**

This collaboration protocol is itself a research-process artifact, not an ENA Constitution rule.
