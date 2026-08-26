# ENA Research Methodology — Session Continuity and Collaboration

Status: `ACTIVE_WORKING_METHOD / SESSION_CONTINUITY / NON_NORMATIVE_TO_CURRENT`

This protocol defines how multiple ChatGPT sessions or other research participants continue one ENA lineage without silently creating multiple ENAs or silently regressing the research method.

## Core topology

```text
Participant A ─┐
               ├→ Shared durable research state → Reconciliation → selection/release only when justified
Participant B ─┘
```

The goal is **protocol-level unity with cognitive diversity**.

Participants are independent research nodes. They do not share reliable live context and must not assume another node already knows recent conclusions or methodology.

## Required bootstrap

Before substantive continuation:

1. read `research/RESEARCH-START-HERE.md`;
2. verify actual Current from `releases/current/CURRENT-BASELINE.yaml` on the default branch;
3. read `research/methodology/ENA-RESEARCH-DISCIPLINE.md`;
4. read `research/methodology/HOW-GROWTH-DISCIPLINE.md` and other method files relevant to the task;
5. read `research/plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md` and `research/plans/PROGRESS.yaml`;
6. read PR #82 and #89, then only relevant workstreams/prototypes/evidence;
7. if a previous conversation export contains recent methodology-bearing decisions, inspect its tail instead of trusting only a compressed handoff.

Only then select substantive work.

## Method inheritance is behavioral

A participant has not successfully inherited methodology merely because it can quote it.

```text
WRITTEN -> RETRIEVED -> INTERPRETED -> SALIENT -> APPLIED
```

Likewise:

```text
DURABLE != DISCOVERABLE
DISCOVERABLE != RETRIEVED
RETRIEVED != SALIENT
SALIENT != APPLIED
```

If a successor reads anti-dissolution rules and then immediately compresses plural HOWs into one abstract principle, methodology inheritance failed at the salience/application layer.

## Contribution discipline

A finding should normally travel through:

`Capture → Compare → Classify → Persist → Reconcile → retain/specialize/retire/select when evidence justifies it`

Before selecting or naming a mechanism, ask:

- What WHAT/WHY failure or property is involved?
- What concrete HOW lineage already exists, including historical, Host-specific, dormant, failed, and competing variants?
- Does Current cover only the parent property, or does a usable organ exist?
- Can multiple HOWs legitimately coexist?
- Am I selecting before relevant variation has been recovered?
- What Host conditions change fitness/applicability?
- What evidence could change the decision?
- Could NO_CHANGE, dormancy, simplification, or multiple surviving branches be correct?

Never use `already covered`, `Host-specific`, `no Core delta`, or `reference organ` as automatic closure operators.

```text
CURRENT_ALREADY_COVERS_PARENT_PROPERTY != PRACTICAL_PROBLEM_SOLVED
```

## Compression boundary

Core semantic compression can be useful for WHAT/WHY. It must not erase operational branches.

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

Useful relationship classes may include:

- `SAME_PROBLEM`
- `NEW_EVIDENCE`
- `COUNTEREXAMPLE`
- `DEEPER_BOUNDARY_CONDITION`
- `CONFLICTING_INTERPRETATION`
- `PARENT_PROPERTY_ALREADY_COVERED`
- `COMPETING_HOW`
- `HOST_SPECIALIZATION`

The list is descriptive, not exhaustive.

`PARENT_PROPERTY_ALREADY_COVERED` does not imply organ closure.

Competing HOWs may remain visible until evidence supports selection. Do not erase variation merely to make participants appear consistent.

## External sources and other research nodes

Another participant, framework, paper, company blog, AI community discussion, or external tool is not higher-authority merely because it is polished or popular.

Treat it as provenance-bearing evidence/candidate input with:

- source and date;
- observed mechanism;
- evidence class;
- applicability assumptions;
- ENA failure mapping;
- known limitations;
- unresolved questions;
- reconciliation state.

External HOW harvesting belongs under `research/external-how/`.

## Reconciliation

Reconciliation may:

- merge compatible formulations;
- retain multiple concrete HOWs under one property;
- specialize a HOW by Host/condition;
- downgrade a candidate to a worked example;
- preserve competing hypotheses;
- reject or retire a candidate with lineage preserved;
- create a targeted experiment only when it can pay epistemic rent;
- accept an implementation candidate;
- contribute to a future release when a real release delta exists.

Reconciliation must preserve why a conclusion changed.

## Handoff discipline

Before ending a session after material project or methodology change:

- persist the change in GitHub;
- update `research/plans/PROGRESS.yaml` when project execution state changed materially;
- update `METHOD-CHANGELOG.md` when research methodology changed materially;
- update the hot entrypoint only when routing changed;
- do not rely on chat summary as the only carrier;
- distinguish current action state from historical discussion;
- leave exact routing to the cold sources needed by the next node.

The purpose is not to reproduce the whole session. It is to preserve the **decision-changing state and the method required to interpret it correctly**.

## Design principle

> **Share lineage, evidence, candidate state, and research method; preserve cognitive diversity.**

> **Do not merely inherit conclusions. Inherit the method that governs how new conclusions may be produced.**
