# ENA Project Hub

Status: `PROJECT_ENTRYPOINT / CURRENT_POINTER / RESEARCH_CONTROL_POINTER / HANDOFF_POINTER`

Project: **Evolution-Native Agent Architecture (ENA)**

This is the stable entrypoint for participants asked to adopt, use, continue, review, research, experiment on, or contribute to ENA.

## Canonical adoption pointer

For any new or refreshed adoption:

1. use the repository default branch `main`;
2. read `releases/current/CURRENT-BASELINE.yaml` for effective version and maturity/status;
3. use only `releases/current/` as the adoption baseline.

Never infer Current from:

- the highest-looking version number;
- the newest commit;
- a candidate directory or candidate branch;
- a development/release branch;
- research, handoff, validation, or historical artifacts.

`releases/current/CURRENT-BASELINE.yaml` is the machine-readable Current identity authority.

The active adopter-facing model is **Current + declared maturity/status**. Candidate, research, handoff, and historical surfaces do not replace that model unless governed release/promotion changes Current.

Current at this handoff transition remains:

```text
v0.3.6 / CURRENT / FIELD_VALIDATION
```

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

> **Canonical source is the cold path; internalized semantics are the hot path.**

## Continue or inherit ENA research/project management

Session replacement is a normal project lifecycle. Do not reconstruct the project from chat if a standardized handoff exists.

Start from `main` and use this route:

1. `releases/current/CURRENT-BASELINE.yaml` — verify Current;
2. `research/handoffs/CURRENT-HANDOFF.yaml` — find the latest intended project-manager/session handoff package;
3. read the pointed `HANDOFF-START-HERE.md` and `HANDOFF-MANIFEST.yaml`;
4. `research/ACTIVE-RESEARCH.yaml` — discover the one active research integration branch and current project phase;
5. `research/methodology/README.md` — canonical method index;
6. `research/methodology/SESSION-HANDOFF-DISCIPLINE.md` — outgoing/incoming session protocol;
7. `research/methodology/CONVERGENCE-DIVERGENCE-DISCIPLINE.md` — guard against summarization/ablation bias;
8. `research/methodology/PROJECT-STATE-ALIGNMENT-GATE.md` — use if handoff/live/control-plane surfaces disagree or another material transition occurred;
9. follow the active branch pointer;
10. on that branch, read `research/RESEARCH-START-HERE.md` and `research/plans/PROGRESS.yaml`;
11. read `research/plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md` for long-horizon phase constraints;
12. discover an open PR only when integration/review context is needed.

Before writing, independently reverify live branch heads and exact frozen identities named by the handoff.

```text
BRANCH_EXISTS != BRANCH_ACTIVE
BRANCH_RECENT != BRANCH_AUTHORITATIVE
OPEN_PR != ACTIVE_BRANCH_AUTHORITY
HANDOFF_PACKAGE != PROJECT_AUTHORITY
CHAT_CONTEXT != PROJECT_STATE
```

A successor session should not need a branch census, historical PR census, or user reconstruction of recent decisions for normal continuation.

## Current project/release posture

At the standardized handoff transition:

```text
Current = v0.3.6
next release line = v0.3.7
candidate.0 = frozen
independent semantic falsification = pending
release preparation = not started
promotion = not started
```

Frozen v0.3.7 candidate.0 identity is governed by its external freeze record, not by candidate branch recency.

Current handoff package provides the exact source/tree and next action.

## Alignment before substantive resume

After a material branch/control-plane transition, session handoff, directory move, methodology change, master-plan phase change, candidate/freeze/release-state change, or major checkpoint merge, verify that live repository state, routing guides, methodology, plan, Progress, handoff, and next actions tell one coherent current story.

Canonical method:

`research/methodology/PROJECT-STATE-ALIGNMENT-GATE.md`

```text
INDIVIDUAL_FILE_CORRECT != PROJECT_STATE_COHERENT
MATERIAL_TRANSITION -> ALIGN -> RESUME
```

Do not turn this into ceremony after every ordinary content commit.

## Research architecture direction

ENA research distinguishes semantic compression from operational/adversarial growth:

```text
WHAT / WHY
  -> may converge into stable, compressed semantics

HOW
  -> should concretize and may branch into multiple tools/processes/organs/Host bindings

FAILURE / ADVERSARIAL SPACE
  -> should remain open/grow while materially distinct failure shapes remain plausible

EVIDENCE
  -> attaches to the concrete claim/branch/Host it actually supports
```

```text
ONE_WHAT_WHY -> 0..N_CONCRETE_HOW_BRANCHES
COMPRESS REPRESENTATION != COMPRESS POSSIBILITY SPACE
```

> **Compress the semantic trunk; let concrete HOWs branch.**

## Project knowledge surfaces

GitHub is the canonical engineering, research-lineage, and Current-adoption surface.

- Current adoption baseline: `releases/current/`
- Historical release index: `HISTORY.md`
- Research control/entrypoint: `research/README.md`, `research/ACTIVE-RESEARCH.yaml`
- Standardized session handoffs: `research/handoffs/`
- Current handoff pointer: `research/handoffs/CURRENT-HANDOFF.yaml`
- Research methodology: `research/methodology/`
- Session handoff discipline: `research/methodology/SESSION-HANDOFF-DISCIPLINE.md`
- Convergence/divergence discipline: `research/methodology/CONVERGENCE-DIVERGENCE-DISCIPLINE.md`
- Project-state alignment method: `research/methodology/PROJECT-STATE-ALIGNMENT-GATE.md`
- Long-horizon research/release plan: `research/plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md`
- Fast-moving progress: `research/plans/PROGRESS.yaml` on the active aligned research surface
- Operational Architecture research: `research/operational-architecture/`
- Release-scope research: `research/release-scope/`
- Experiments/prototypes: `research/experiments/`, `research/prototypes/`
- External HOW registry: `research/external-how/`
- Reconciliation/freeze/validation records: `collaboration/reconciliation/`
- Decisions: `decisions/`

Historical releases, candidates, old handoffs, rejected paths, deleted research branches, old PR generations, and validation artifacts are **not** parallel runtime or research baselines. Retrieve them only when lineage, falsification, regression, provenance, or a historical decision makes them relevant.

> **Preserve history durably; retrieve history selectively.**
>
> **Expose one adoption surface, one active research pointer, and one current handoff pointer; preserve many historical surfaces.**

## Participation and authority

Any participant may, within actual capability and authority, read, question, critique, research, experiment, and contribute.

Useful contribution classes include:

`INCIDENT | NEAR_MISS | FRICTION | VALUE_OBSERVED | COUNTEREXAMPLE | PORTABILITY_FINDING | NEW_VARIATION | EVIDENCE_RESULT | RESEARCH_HYPOTHESIS | CRITIQUE`

`Contribution != Reconciliation != Release/Promotion Authority.`

GitHub write capability, candidate branch access, or handoff authorship does not grant release/deployment/promotion authority.

## Persistent collaboration rules

- project-first, not Agent-first;
- persistent project state is the collaboration bus;
- project continuity must survive session replacement;
- handoff is a bootstrap map, not a competing source of truth;
- conflicts remain visible until evidence/authorized decision resolves them;
- persistence is not synchronization;
- one active research integration branch is the coordination pointer, not a claim that research has one topic;
- candidate branch head is not frozen identity;
- temporary branches/process artifacts must pay complexity rent;
- material project transitions require alignment before substantive work resumes;
- summarization must not silently dissolve materially distinct HOW/failure/Host/evidence variation.

## Operating posture

Falsify before formalize.

Use the cheapest evidence that can honestly support the decision.

Recover variation before selection when omission could change the decision.

Batch variation; concentrate expensive selection.

Production before perfection; not production without evidence.

The whole project may evolve. The currently adopted version must remain singular, legible, and evidence-backed.
