# ENA Reconstruction-to-Release Master Plan

Status: `ACTIVE_MASTER_PLAN / MAIN_VISIBLE_PROJECT_CONTROL / CURRENT_UNCHANGED_UNTIL_RELEASE`

This is the stable long-horizon plan for continuing ENA from the v0.3.6 semantic trunk into a usable operational architecture and, when evidence/release gates justify it, a new Current release.

Fast-moving execution state lives on the branch named by `research/ACTIVE-RESEARCH.yaml`.

## Goal

ENA should become usable not only as a philosophy/semantic Constitution but as an operational architecture that lets an Agent discover concrete ways to implement the philosophy.

Working shape:

```text
TELOS / PURPOSE
      |
      v
WHAT / WHY
stable semantic trunk; abstraction may be useful
      |
      +--> HOW-A
      |     +--> concrete organ/process/tool/protocol
      |     +--> Host binding / adapter
      |     +--> failure/fallback behavior
      |     +--> evidence
      |
      +--> HOW-B
      +--> HOW-C
      +--> ...
```

```text
ONE_WHAT_WHY -> 0..N_CONCRETE_HOW_BRANCHES
```

The final test is whether an Agent can actually live by the architecture.

## Project control and active workspace

Start from `main`:

1. `PROJECT-HUB.md`;
2. verify `releases/current/CURRENT-BASELINE.yaml`;
3. `research/ACTIVE-RESEARCH.yaml` for the one active research integration **branch**;
4. `research/methodology/README.md` and canonical methodology;
5. if a material project transition occurred, complete `research/methodology/PROJECT-STATE-ALIGNMENT-GATE.md` before substantive work resumes;
6. read this plan;
7. follow the active branch pointer;
8. read the active branch's `research/RESEARCH-START-HERE.md` and `research/plans/PROGRESS.yaml`;
9. discover an open PR by active head branch only when review/integration context is needed.

Do not infer active work from branch names, recency, or historical PR numbers.

## Current aligned execution posture — 2026-08-26

The repository/control-plane cleanup is now an established baseline rather than an unresolved prerequisite.

Observed long-lived topology:

```text
main
research/ena-reconstruction
```

Current adoption remains:

```text
v0.3.6 / CURRENT / FIELD_VALIDATION
```

Research-state summary:

- repository information architecture / branch control: aligned baseline established;
- anti-ablation archaeology: active;
- HOW branch expansion: active;
- external HOW harvesting: active;
- Host binding: partial;
- cross-organ composition: active, with stale-executor/fencing gap established;
- Operational Architecture assembly: not ready;
- release-scope reconciliation: not started;
- candidate build/validation: not started;
- promotion: not started.

Historical PR #82 and PR #101 are checkpoint/handoff lineage, not current continuation authority.

## Phase — Research continuity and repository control plane

Purpose:

Make ENA research inheritable without reconstructing state from chat history or branch archaeology.

Required capabilities:

- main-visible active research branch pointer;
- branch governance/lifecycle rules;
- canonical research methodology;
- project-state alignment method;
- durable long-horizon plan;
- active-branch progress carrier;
- clear separation between Current adoption and research work.

Current state:

`BASELINE_ESTABLISHED / MAINTAIN_AS_INVARIANT`

Closure condition for the current topology:

A fresh session can start from `main` and identify Current, active research branch, methodology, plan, progress, and next permitted work without a branch census or old chat reconstruction.

This phase is not “finished forever.” A material control-plane transition reopens an alignment obligation even when the baseline architecture remains valid.

## Project State Alignment Gate

Purpose:

Prevent routing, methodology, plan, progress, and live Git state from describing different generations of the project after a material transition.

Canonical method:

`research/methodology/PROJECT-STATE-ALIGNMENT-GATE.md`

Trigger examples:

- branch handoff/cleanup;
- main control-plane checkpoint merge;
- directory/canonical-path change;
- material methodology change;
- master-plan phase/closure-rule change;
- Current/candidate/release-state change;
- major session handoff after such changes.

```text
INDIVIDUAL_FILE_CORRECT != PROJECT_STATE_COHERENT
MATERIAL_TRANSITION -> ALIGN -> RESUME
```

The gate is transition-triggered, not required after every ordinary commit.

## Phase — Anti-ablation archaeology / variation recovery

Purpose:

Recover concrete problems/HOWs that were previously compressed by higher-level semantic coverage.

Sources include:

- historical Issues, PRs, comments, decisions, experiments, prototypes, and field reports;
- prior session exports when they contain material research not durably mapped elsewhere;
- existing Host-specific mechanisms and failed/abandoned branches;
- previously dissolved concrete organs.

For each surviving topic reconstruct:

```text
WHAT
WHY
HOW — existing/plural candidates
EVIDENCE — existing/needed
PROPERTY
ORGAN
HOST_BINDING
EVIDENCE
ADOPTION
```

Closure rule:

Continue while additional archaeology can still reveal material missing lineage likely to change the engineering map. Do not use a fixed topic count as closure.

## Phase — HOW branch expansion

Purpose:

Turn semantic properties into concrete ways an Agent can act.

Candidate HOW forms include:

- state machines;
- workflows;
- protocols;
- resolvers;
- adapters;
- schemas;
- tools/scripts/validators;
- file/layout conventions;
- manual procedures where automation is unjustified;
- Host-native mechanism mappings.

One property may retain multiple HOWs indefinitely when applicability differs.

## Phase — External HOW harvest

Purpose:

Avoid inventing every mechanism from scratch.

Search actively across:

- AI Agent frameworks and SDKs;
- memory systems;
- durable workflow engines;
- orchestration/protocol ecosystems;
- AI developer communities and field reports;
- distributed systems and adjacent engineering domains;
- relevant academic/industry research.

Correct sequence:

```text
ENA failure
-> search external mechanisms
-> extract concrete mechanism
-> map to ENA/Host conditions
-> falsify/compare
-> retain/specialize/reject
```

External popularity, framework maturity, or vendor authority does not prove universal ENA fitness.

## Phase — Host binding

For each promising HOW, determine whether/how it binds to real Hosts.

Possible outcomes include:

```text
NATIVE_HOST_ORGAN
ADAPTER_REQUIRED
REFERENCE_IMPLEMENTATION
MANUAL_PROCEDURE
INAPPLICABLE
UNKNOWN
```

Do not force every Host to instantiate every organ.

## Phase — Cross-organ composition

Test whether individually reasonable organs create false confidence or false blocking when composed.

Current high-value seams include:

- Commitment/Settlement × Effect Lifecycle × Authority Lease × durable execution/fencing;
- Memory Metabolism × Retrieval × Decision Projection × compaction/salience;
- Tiny Hot Kernel × exact cold retrieval × language projection;
- Identity/lineage × commitment × reputation;
- Commons/coordination × A2A/task lifecycle × specialization/resource economics.

Prefer deterministic/state-space falsification when the bug is statically reachable.

## Phase — Operational Architecture assembly

Only after archaeology/HOW recovery is sufficiently mature for the decision, assemble an adopter-facing operational architecture around the semantic trunk.

The assembly should make concrete HOWs discoverable without forcing all HOWs into every runtime context.

Likely structure:

```text
small semantic/runtime hot surface
-> retrieve relevant WHAT/WHY
-> route to applicable HOW family
-> select/map according to Host conditions
-> execute with concrete tool/process
-> capture evidence/failure
-> evolve/revise
```

Do not assemble prematurely merely to produce a neat document.

## Phase — Release scope reconciliation

Ask separately:

- Which changes belong in adopter-facing Current?
- Which belong as reference organs/guidance/tools?
- Which remain research/experimental/Host-specific?
- Which old surfaces should be simplified/retired?
- What real release delta exists?

Research effort alone does not force a release delta.

The next version number is assigned only after release scope stabilizes.

## Phase — Candidate build and validation

When release scope is stable:

1. construct a self-contained candidate;
2. preserve exact source/tree identity;
3. run deterministic machine validation;
4. freeze the candidate;
5. obtain independent semantic/implementation falsification appropriate to the changes;
6. reconcile findings without mutating frozen identity;
7. create successor candidate only when material correction is required;
8. stop candidate succession when another round has no plausible decision-changing value.

## Phase — Release and promotion

Only after candidate/reconciliation evidence supports release:

- create release branch;
- package exact Current candidate bytes;
- verify file-set/hash parity and release identity;
- run required CI/security/regression checks;
- publish/read back release artifact where applicable;
- merge through release discipline;
- verify post-merge `releases/current/` identity and package/readback;
- update project/history/control pointers;
- complete a project-state alignment pass before declaring the post-release project state stable.

Do not claim release complete on narrative confidence alone.

## Research-method invariants

```text
PROPERTY != ORGAN != HOST_BINDING != EVIDENCE != ADOPTION
WHAT_WHY_COVERAGE != HOW_COMPLETION
REQUESTED_N != DISCOVERED_N
WORKING_TAXONOMY != ONTOLOGY
EXPERIMENTS_MUST_PAY_EPISTEMIC_RENT
EXTERNAL_POPULARITY != SELECTION_PROOF
NO_CHANGE = VALID_OUTCOME
REMOVE_FROM_ACTIVE_ARCHITECTURE != ERASE_FROM_LINEAGE
HANDOFF_SUMMARY != PROJECT_STATE
BRANCH_EXISTS != ACTIVE_RESEARCH_AUTHORITY
OPEN_PR != ACTIVE_RESEARCH_AUTHORITY
MATERIAL_TRANSITION -> ALIGN -> RESUME
```

## Progress carrier

Do not add fast-changing task-by-task progress to this main plan.

Follow `research/ACTIVE-RESEARCH.yaml` to the active branch and read:

`research/plans/PROGRESS.yaml`

That file may change frequently. This plan should change only when the long-horizon execution model itself changes.
