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

Version identity and maturity/status are separate. Beginning with v0.3.5, the active adopter-facing model is **Current + declared maturity/status**. Historical `MAINLINE / NOT_MAINLINE` records remain history rather than an additional live status axis.

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

## Project knowledge surfaces

GitHub is the canonical engineering, research-lineage, and Current-adoption surface.

- Current adoption baseline: `releases/current/`
- Historical release index: `HISTORY.md`
- Evolution Inbox: `research/evolution-inbox/`
- Historical adversarial replay: `research/adversarial-replay/`
- Experiments: `research/experiments/`
- Prototypes: `research/prototypes/`
- Contributions/evidence intake: `collaboration/inbox/`
- Reconciliation: `collaboration/reconciliation/`
- Decisions: `decisions/`

Historical releases, candidates, rejected paths, and validation artifacts are **not** parallel runtime baselines. Retrieve them only when investigating lineage, falsification, regression, provenance, or a historical decision.

> **Preserve history durably; retrieve history selectively.**
>
> **Expose one adoption surface; preserve many historical surfaces.**

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
- one substantial contribution should normally be one independent artifact;
- conflicts remain visible until evidence/authorized decision resolves them;
- persistence is not synchronization;
- project continuity does not depend on one permanent owning session/Agent.

## Operating posture

Falsify before formalize.

Use the cheapest evidence that can honestly support the decision.

Batch variation; concentrate expensive selection.

Production before perfection; not production without evidence.

The whole project may evolve. The currently adopted version must remain singular, legible, and evidence-backed.
