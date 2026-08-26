# ENA Project Hub

Status: `PROJECT_ENTRYPOINT / CURRENT_POINTER / RESEARCH_CONTROL_POINTER`

Project: **Evolution-Native Agent Architecture (ENA)**

This is the stable entrypoint for participants asked to adopt, use, continue, review, research, experiment on, or contribute to ENA.

## Canonical adoption pointer

For any new or refreshed adoption:

1. use the repository's canonical default branch;
2. read `releases/current/CURRENT-BASELINE.yaml` for the effective version and maturity/status;
3. use only `releases/current/` as the adoption baseline.

Never infer Current from:

- the highest-looking version number;
- the newest commit;
- a candidate directory or historical candidate name;
- a development/release branch;
- research or validation artifacts.

`releases/current/CURRENT-BASELINE.yaml` is the machine-readable adoption pointer.

Version identity and maturity/status are separate. Beginning with v0.3.5, the active adopter-facing model is **Current + declared maturity/status**. Historical promotion records remain lineage rather than additional live baselines.

## First adoption

1. `releases/current/CURRENT-BASELINE.yaml`
2. `releases/current/00-READ-ME-FIRST.md`
3. `releases/current/CONSTITUTION-CONCEPT-MAP.yaml`
4. `releases/current/01-CONSTITUTION.md`
5. `releases/current/02-SELF-POSITIONING-AND-LOCAL-PROJECTION.md`
6. `releases/current/RUNTIME-ADOPTION-KERNEL.md`
7. `releases/current/09-EVOLUTION-METABOLISM.md`
8. use `releases/current/LITE-ADOPTION-INSTRUCTION.md` when the real task is bounded and low-consequence;
9. retrieve longer contracts, schemas, tools, or research only when consequence, ambiguity, novelty, evidence conflict, or exact semantics make them decision-relevant.

After successful persistent adoption, familiar tasks should normally use the internalized Runtime Kernel and still-valid Local Projection rather than re-reading ENA from zero.

> **Canonical source is the cold path; internalized semantics are the hot path.**

## Continue or inherit ENA research

Do **not** choose a research branch by name, recency, or number of commits.

Start from `main` and use this route:

1. `research/ACTIVE-RESEARCH.yaml` — canonical pointer to the one active research integration branch and PR;
2. `research/methodology/README.md` — research method and anti-drift discipline;
3. `research/plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md` — stable long-horizon plan;
4. follow the active branch pointer;
5. on that branch, read `research/RESEARCH-START-HERE.md` and `research/plans/PROGRESS.yaml` for fast-moving state;
6. only then continue the relevant workstream/prototype/evidence.

A successor session should **not need a branch census** for normal continuation.

```text
BRANCH_EXISTS != BRANCH_ACTIVE
BRANCH_RECENT != BRANCH_AUTHORITATIVE
HANDOFF_SUMMARY != PROJECT_STATE
```

Branch naming/lifecycle policy:

`research/BRANCH-GOVERNANCE.md`

Current branch inventory/cleanup state:

`research/BRANCH-INVENTORY.yaml`

## Research architecture direction

ENA research currently distinguishes the semantic trunk from operational growth:

```text
WHAT / WHY
  -> may converge into stable, compressed semantics

HOW
  -> should concretize and may branch into multiple tools/processes/organs/Host bindings

EVIDENCE
  -> attaches to the concrete claim/branch/Host it actually supports
```

```text
ONE_WHAT_WHY -> 0..N_CONCRETE_HOW_BRANCHES
```

> **Compress the semantic trunk; let concrete HOWs branch.**

## Project knowledge surfaces

GitHub is the canonical engineering, research-lineage, and Current-adoption surface.

- Current adoption baseline: `releases/current/`
- Historical release index: `HISTORY.md`
- Research control/entrypoint: `research/README.md`, `research/ACTIVE-RESEARCH.yaml`
- Research methodology: `research/methodology/`
- Long-horizon research/release plan: `research/plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md`
- Active fast-moving research: branch named by `research/ACTIVE-RESEARCH.yaml`
- Evolution Inbox: `research/evolution-inbox/`
- Historical adversarial replay: `research/adversarial-replay/`
- Experiments: `research/experiments/`
- Prototypes: `research/prototypes/`
- Contributions/evidence intake: `collaboration/inbox/`
- Reconciliation: `collaboration/reconciliation/`
- Decisions: `decisions/`

Historical releases, candidates, rejected paths, temporary branches, and validation artifacts are **not** parallel runtime or research baselines. Retrieve them only when investigating lineage, falsification, regression, provenance, or a historical decision.

> **Preserve history durably; retrieve history selectively.**
>
> **Expose one adoption surface and one active research pointer; preserve many historical surfaces.**

## Participation and authority

Any participant may, within actual capability and authority, read, question, critique, research, experiment, and contribute.

Useful contribution classes include:

`INCIDENT | NEAR_MISS | FRICTION | VALUE_OBSERVED | COUNTEREXAMPLE | PORTABILITY_FINDING | NEW_VARIATION | EVIDENCE_RESULT | RESEARCH_HYPOTHESIS | CRITIQUE`

For trackable bugs, enhancements, research questions, or release concerns, prefer a GitHub Issue when it is the smallest useful durable tracker.

`Contribution != Reconciliation != Release/Promotion Authority.`

GitHub write capability does not grant release, deployment, remediation, or scope-expansion authority.

## Persistent collaboration rules

- project-first, not Agent-first;
- persistent project state is the collaboration bus;
- tool access is connectivity, not project authority;
- conflicts remain visible until evidence/authorized decision resolves them;
- persistence is not synchronization;
- project continuity does not depend on one permanent owning session/Agent;
- one active research integration branch is the coordination pointer, not a claim that research has one topic;
- temporary branches must pay isolation/validation rent and should retire after use.

## Operating posture

Falsify before formalize.

Use the cheapest evidence that can honestly support the decision.

Batch variation; concentrate expensive selection.

Production before perfection; not production without evidence.

The whole project may evolve. The currently adopted version must remain singular, legible, and evidence-backed.
