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

Participants are independent research nodes. They do not share reliable live context and must not assume another node already knows recent conclusions, topology, progress, or methodology.

## Required bootstrap

Before substantive continuation:

1. start from the repository default branch `main` and read `PROJECT-HUB.md`;
2. verify actual Current from `releases/current/CURRENT-BASELINE.yaml`;
3. read `research/ACTIVE-RESEARCH.yaml` on `main` to discover the one active research integration **branch**;
4. read `research/methodology/README.md`, `research/methodology/ENA-RESEARCH-DISCIPLINE.md`, and relevant focused method files on `main`;
5. determine whether a material project transition occurred since the last aligned checkpoint; if so, run `research/methodology/PROJECT-STATE-ALIGNMENT-GATE.md` before substantive work;
6. follow the active branch pointer and read that branch's `research/RESEARCH-START-HERE.md` and `research/plans/PROGRESS.yaml`;
7. read `research/plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md` for the stable long-horizon route;
8. read #89 and only the relevant #90–#94 workstreams/prototypes/evidence for the task at hand;
9. retrieve PR #82, PR #101, deleted predecessor branch names, or other historical artifacts only when lineage/provenance makes them decision-relevant;
10. if a previous conversation export contains recent material work not yet mapped into GitHub, inspect only the decision/method-bearing parts needed to repair the durable state.

An open PR is **not required** for the active research branch to remain authoritative. Discover a current PR by active head branch only when review/integration context is needed.

Only after this routing should a new research node select substantive work.

## Alignment before resume

At every session inheritance or major resume, verify whether the control plane reports a material transition that could have made current-state files disagree.

Run the full Project State Alignment Gate after changes such as:

- branch handoff/cleanup;
- directory or canonical-path changes;
- material methodology changes;
- master-plan phase or closure-rule changes;
- Current/candidate/release state changes;
- major research checkpoint merges.

Do not turn this into ceremony after every ordinary content commit.

```text
INDIVIDUAL_FILE_CORRECT != PROJECT_STATE_COHERENT
MATERIAL_TRANSITION -> ALIGN -> RESUME
```

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

If it reads the latest control plane but continues from a deleted branch, stale PR identity, superseded plan, or contradictory progress state, inheritance failed at the project-state alignment layer.

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

Before ending a session after material project, control-plane, methodology, plan, or architecture change:

- persist the change in GitHub;
- update `research/plans/PROGRESS.yaml` when execution state changed materially;
- update `METHOD-CHANGELOG.md` when research methodology changed materially;
- update stable routing only when routing actually changed;
- run or explicitly defer the Project State Alignment Gate when the change is capable of making routing/method/plan/progress disagree;
- do not rely on chat summary as the only carrier;
- distinguish current action state from historical discussion;
- leave exact routing to the cold sources needed by the next node.

The purpose is not to reproduce the whole session. It is to preserve the **decision-changing state and the method required to interpret it correctly**.

## Design principle

> **Share lineage, evidence, candidate state, and research method; preserve cognitive diversity.**

> **Do not merely inherit conclusions. Inherit the method that governs how new conclusions may be produced.**
