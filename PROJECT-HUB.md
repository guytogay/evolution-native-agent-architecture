# ENA Project Hub

Status: `PROJECT_ENTRYPOINT / CURRENT_POINTER / RESEARCH_CONTROL_POINTER / HANDOFF_POINTER`

Project: **Evolution-Native Agent Architecture (ENA)**

This is the stable entrypoint for participants asked to adopt, use, continue, review, research, experiment on, or contribute to ENA.

## Canonical adoption pointer

For any new or refreshed adoption:

1. use repository `main`;
2. read `releases/current/CURRENT-BASELINE.yaml` for effective version and maturity/status;
3. use only `releases/current/` as the adoption baseline.

Never infer Current from the highest-looking version, newest commit, candidate directory/branch, research branch, handoff record, or historical artifact.

The active adopter-facing model is **Current + declared maturity/status**.

Current remains:

```text
v0.3.6 / CURRENT / FIELD_VALIDATION
```

## Continue or inherit ENA project/research management

Session replacement is a normal project lifecycle. Do not reconstruct the project from chat when a standardized handoff exists.

Start from `main` and use this route:

1. `releases/current/CURRENT-BASELINE.yaml` — verify Current;
2. `research/handoffs/CURRENT-HANDOFF.yaml` — discover the intended current handoff record and takeover contract;
3. `research/handoffs/HANDOFF-PROTOCOL.md` — canonical outgoing/incoming succession rules;
4. `research/handoffs/REQUIRED-TAKEOVER-CONTEXT.yaml` — mandatory takeover context, including project methodology;
5. `research/handoffs/PROJECT-MANAGEMENT-DISCIPLINE.md` — cross-session project-management rules;
6. read the current record under `research/handoffs/records/` named by `CURRENT-HANDOFF.yaml`;
7. read required project methodology under `research/methodology/`;
8. `research/ACTIVE-RESEARCH.yaml` — discover active research integration branch and phase;
9. `research/plans/PROGRESS.yaml` and the master plan;
10. reverify live branch heads and exact frozen identities before writing.

```text
HANDOFF_FRAMEWORK != HANDOFF_RECORD
HANDOFF_RECORD != PROJECT_METHODOLOGY
PROJECT_STATE_INHERITANCE_WITHOUT_METHOD_INHERITANCE = INCOMPLETE_TAKEOVER
```

A handoff **record** is a map, not project authority. The handoff **framework** is canonical succession process. ENA project methodology remains a separate canonical surface.

## Current project/release posture

```text
Current = v0.3.6
next release line = v0.3.7
candidate.0 = frozen
1080->188 anti-ablation audit = complete with tree-external coverage repair
fresh independent falsification = pending Phase A
review surface = PR #115 / DO NOT MERGE
release preparation = not started
promotion = not started
```

Frozen v0.3.7 candidate.0 identity:

```text
source commit = d0e793593184740d9732902e948afd48ed96ae2f
candidate subtree = cffbf76fe1448b020b637c78d1f7ae46e4c0115b
```

Frozen identity is governed by exact source/tree records, not branch recency.

The current project next action is **fresh independent falsification Phase A** on exact frozen bytes before author-oracle comparison.

## Alignment before substantive resume

After a material branch/control-plane transition, session handoff, canonical directory/path move, methodology change, plan phase change, candidate/freeze/release-state change, or major checkpoint merge, verify that live repository state, routing guides, method, plan, Progress, handoff, and next actions tell one coherent story.

Canonical method:

`research/methodology/PROJECT-STATE-ALIGNMENT-GATE.md`

```text
INDIVIDUAL_FILE_CORRECT != PROJECT_STATE_COHERENT
MATERIAL_TRANSITION -> ALIGN -> RESUME
```

Do not turn this into ceremony after every ordinary content commit.

## Research architecture direction

ENA distinguishes semantic compression from operational/adversarial growth:

```text
WHAT / WHY
  -> may converge into stable compressed semantics

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

## Project knowledge surfaces

- Current adoption baseline: `releases/current/`
- Historical release index: `HISTORY.md`
- Research control: `research/README.md`, `research/ACTIVE-RESEARCH.yaml`
- Handoff framework: `research/handoffs/`
- Current handoff pointer: `research/handoffs/CURRENT-HANDOFF.yaml`
- Handoff protocol: `research/handoffs/HANDOFF-PROTOCOL.md`
- Required takeover context: `research/handoffs/REQUIRED-TAKEOVER-CONTEXT.yaml`
- Project-management discipline: `research/handoffs/PROJECT-MANAGEMENT-DISCIPLINE.md`
- Historical/current handoff records: `research/handoffs/records/`
- ENA research methodology: `research/methodology/`
- Convergence/divergence discipline: `research/methodology/CONVERGENCE-DIVERGENCE-DISCIPLINE.md`
- Project-state alignment: `research/methodology/PROJECT-STATE-ALIGNMENT-GATE.md`
- Long-horizon plan: `research/plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md`
- Fast-moving progress: `research/plans/PROGRESS.yaml`
- Operational Architecture research: `research/operational-architecture/`
- Release-scope research: `research/release-scope/`
- Experiments/prototypes: `research/experiments/`, `research/prototypes/`
- External HOW registry: `research/external-how/`
- Reconciliation/freeze/validation records: `collaboration/reconciliation/`
- Decisions: `decisions/`

Historical releases, candidates, old handoff records, rejected paths, deleted research branches, old PR generations, and validation artifacts are not parallel runtime/research baselines. Retrieve them only when lineage, falsification, regression, provenance, or a historical decision makes them relevant.

## Participation and authority

Any participant may, within actual capability and authority, read, question, critique, research, experiment, and contribute.

`Contribution != Reconciliation != Release/Promotion Authority.`

GitHub write capability, candidate-branch access, handoff authorship, or review-PR access does not grant promotion authority.

## Persistent collaboration rules

- project-first, not Agent-first;
- project continuity must survive session replacement;
- outgoing and incoming succession method are equally important;
- project state and project methodology are equally required for takeover;
- handoff framework, handoff record, and ENA research methodology remain distinct;
- persistent project state is the collaboration bus;
- conflicts remain visible until evidence/authorized decision resolves them;
- one active research pointer is coordination, not an ontology claim;
- candidate branch head is not frozen identity;
- material transitions require alignment before substantive work resumes;
- summarization must not silently dissolve materially distinct HOW/failure/Host/evidence variation.

## Operating posture

Falsify before formalize.

Use the cheapest evidence that can honestly support the decision.

Recover variation before selection when omission could change the decision.

Batch variation; concentrate expensive selection.

Production before perfection; not production without evidence.

The whole project may evolve. Current must remain singular, legible, and evidence-backed.
