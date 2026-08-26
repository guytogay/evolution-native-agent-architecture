# ENA Project Hub

Status: `PROJECT_ENTRYPOINT / CURRENT_POINTER`

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

Version identity and maturity/status are separate. Historical promotion records remain lineage rather than additional live baselines.

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

## Continue ENA research

A session asked to continue, inherit, improve, or eventually release ENA should **not** start by browsing random Issues or choosing the most visible prototype.

Use this route:

1. `research/RESEARCH-START-HERE.md` — small hot research bootstrap;
2. `research/methodology/README.md` and the method files it routes to;
3. `research/plans/PROGRESS.yaml` — machine-readable current execution state;
4. `research/plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md` — durable end-to-end plan;
5. PR #82 / #89 and only then the relevant workstream, prototype, external HOW source, or evidence.

A handoff summary is a pointer, not canonical project state.

```text
DURABLE != DISCOVERABLE != RETRIEVED != SALIENT != APPLIED
```

Method inheritance is successful only when the next session actually behaves consistently with the persisted methodology.

## Current research direction

The working structure is deliberately asymmetric:

```text
WHAT / WHY
  -> may converge into a stable, compressed semantic trunk

HOW
  -> should concretize and may branch into multiple tools/processes/organs/Host bindings

EVIDENCE
  -> attaches to the concrete claim/branch/Host it actually supports
```

```text
ONE_WHAT_WHY -> 0..N_CONCRETE_HOW_BRANCHES
```

Do not treat current branch count, workstream count, directory count, or prototype count as ontology.

> **Compress the semantic trunk; let concrete HOWs branch.**

## Project knowledge surfaces

GitHub is the canonical engineering, research-lineage, and Current-adoption surface.

- Current adoption baseline: `releases/current/`
- Historical release index: `HISTORY.md`
- Research map/bootstrap: `research/README.md`, `research/RESEARCH-START-HERE.md`
- Research methodology: `research/methodology/`
- Master plan/progress: `research/plans/`
- Reconstruction archaeology: `research/reconstruction/`
- External HOW harvesting: `research/external-how/`
- Evolution Inbox: `research/evolution-inbox/`
- Historical adversarial replay: `research/adversarial-replay/`
- Experiments: `research/experiments/`
- Prototypes: `research/prototypes/`
- Research-process incidents: `research/incidents/`
- Contributions/evidence intake: `collaboration/inbox/`
- Reconciliation: `collaboration/reconciliation/`
- Decisions: `decisions/`

Historical releases, candidates, rejected paths, and validation artifacts are **not** parallel runtime baselines. Retrieve them only when investigating lineage, falsification, regression, provenance, or a historical decision.

> **Preserve history durably; retrieve history selectively.**
>
> **Expose one adoption surface; preserve many research and historical surfaces.**

## Participation and authority

Any participant may, within actual capability and authority, read, question, critique, research, experiment, and contribute.

Useful contribution classes include:

`INCIDENT | NEAR_MISS | FRICTION | VALUE_OBSERVED | COUNTEREXAMPLE | PORTABILITY_FINDING | NEW_VARIATION | EVIDENCE_RESULT | RESEARCH_HYPOTHESIS | CRITIQUE`

This list is descriptive, not exhaustive.

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
- research methodology changes belong in `research/methodology/` and its changelog;
- material project progress belongs in `research/plans/PROGRESS.yaml`;
- external candidate HOWs belong in `research/external-how/`.

## Operating posture

Falsify before formalize.

Use the cheapest evidence that can honestly support the decision.

Recover variation before selection when reconstruction completeness is still at issue.

Batch variation; concentrate expensive selection.

Experiments must pay epistemic rent.

Production before perfection; not production without evidence.

The whole project may evolve. The currently adopted version must remain singular, legible, and evidence-backed.
