# Minimum Sufficient Intervention

Status: `RESEARCH_HYPOTHESIS / ISSUE-11 / NOT_CURRENT_BASELINE / NOT_PROMOTED`

This note develops a research hypothesis for ENA. It does not modify `releases/current/` and must not be treated as an additional runtime layer.

## Core question

When a viable Agent ecology can absorb a problem through local adaptation, feedback, evidence, negotiation, or bounded selection, should ENA deliberately avoid adding a stronger centralized control?

Candidate formulation:

> **Use the minimum intervention sufficient to preserve viable agency, contain material externality, and keep future correction available.**

A stronger formulation remains deliberately unpromoted:

> **Govern the conditions of evolution, not the shape of evolution.**

The claim is not that less governance is always better. The claim to test is that **unnecessary intervention consumes useful behavioral variety and creates viability cost**, while insufficient intervention can externalize harm, hide coordination failure, or allow locally stable but globally damaging equilibria.

## Existing Current anchors

This research appears to extend, not replace, existing `v0.3.1-BETA.1` semantics:

- `ENA-CON-016` — Protocol-Level Unity, Cognitive Diversity;
- `ENA-CON-033` — Residual Decision Authority Should Track Residual Consequence Exposure;
- `ENA-CON-034` — Governance Burden Must Be Proportional to Consequential Risk;
- `ENA-CON-038` — Governance Must Preserve Viable Agency and Remain Value-Accountable.

Therefore the default research presumption is **no new Constitution rule unless a real semantic gap is demonstrated**.

## Working definitions

### Intervention

Any deliberate mechanism that narrows, redirects, delays, blocks, escalates, standardizes, or overrides an Agent's otherwise available decision/action space.

Intervention can be useful. It also has cost.

### Enabling constraint

A boundary, interface, invariant, signal, or consequence condition that shapes the space of possible behavior without prescribing one detailed solution path.

Examples in ENA may include:

- consequence envelopes;
- evidence requirements for consequential claims;
- capability/authority boundaries;
- append-only historical truth;
- interface contracts that permit heterogeneous internal implementations.

### Prescriptive constraint

A rule that specifies a narrower behavior, sequence, mechanism, or solution path than the underlying safety/viability property strictly requires.

Prescriptive constraints can be appropriate where cause/effect is stable, externality is material, or hard prevention is required. They should not be assumed to be superior merely because they are more explicit.

### Governance tax

Material cost introduced by governance, including where observable:

- token/context cost;
- model/tool calls;
- latency;
- human review;
- implementation/maintenance burden;
- lost solution variety;
- blocked local adaptation;
- false-positive intervention;
- additional coordination state.

### Productive friction

Friction that changes a consequential decision, exposes a material unknown, prevents or contains a real failure, preserves evidence/recovery, or improves future correction enough to justify its cost.

`Friction != automatically waste.`

`Friction != automatically value.`

## Candidate intervention ladder

This ladder is a research instrument, not a Current obligation.

0. `OBSERVE`
   - preserve reality/evidence;
   - do not interfere merely because a difference exists.

1. `EXPOSE_SIGNAL`
   - surface contradiction, uncertainty, cost, drift, externality, or relevant evidence;
   - allow the local actor to adapt before imposing a stronger path.

2. `SHAPE_CONDITIONS`
   - add an enabling constraint, boundary, resource condition, interface, or feedback loop;
   - avoid dictating an implementation when the property can be protected without doing so.

3. `LOCAL_COORDINATION`
   - provide low-cost reconciliation, negotiation, arbitration, shared-resource protocol, or conflict-resolution path when independent local adaptations collide.

4. `SCOPED_HARD_BOUNDARY`
   - deterministically prevent or require approval for a defined consequential effect surface;
   - keep the boundary as narrow as the supported risk claim permits.

5. `EMERGENCY_CONTAINMENT`
   - halt, isolate, revoke, or otherwise contain when delay itself creates unacceptable consequence, blast radius, irreversibility, or recovery loss.

### Escalation heuristic

Escalation becomes more justified as one or more of the following rise materially:

- externality to non-consenting consequence-bearers;
- blast radius;
- irreversibility;
- authority escalation;
- secrets/security impact;
- recovery weakness;
- evidence of repeated local failure;
- speed of propagation relative to detection/recovery;
- uncertainty where the downside is materially asymmetric;
- governance/meta proximity where a mistake can alter the control system itself.

These intentionally resemble `ENA-CON-034`; this research is trying to operationalize proportionality, not create a competing risk model.

### De-escalation heuristic

Intervention should not become permanent merely because it was once justified.

When evidence shows that a stronger intervention is no longer decision-changing, or a lower-cost layer now protects the same property, test removal or downgrade.

> **A control that once paid rent can later become governance debt.**

## Research hypotheses

### H1 — Variety preservation

Within a bounded consequence envelope, Minimum Sufficient Intervention preserves more useful solution variety than prescriptive governance without materially degrading outcome quality or safety.

### H2 — Viability economics

A graduated intervention policy reduces governance tax compared with default high-control governance on low/medium consequence work.

### H3 — Hard-boundary necessity

For high-externality, high-irreversibility, rapidly propagating, or weakly recoverable effects, hard boundaries outperform ecological selection/feedback alone.

### H4 — De-escalation value

Explicit downgrade/removal of no-longer-useful controls prevents governance accumulation without increasing material failure.

### H5 — Context dependence

The correct intervention layer is host/task/consequence dependent; no universal preference for `enabling` or `hard` constraints should be assumed.

## Failure modes that must remain visible

A self-organizing system may stabilize into a bad equilibrium. Watch for:

- local optimum / global loss;
- collusion or coordinated deception;
- monopoly or authority capture;
- race to the bottom;
- hidden externality;
- slow cumulative harm below alarm thresholds;
- monoculture created by shared incentives;
- coordination deadlock;
- evidence suppression by successful local actors;
- under-intervention caused by romanticizing autonomy;
- over-intervention caused by equating visible order with viability.

`Equilibrium != desirable equilibrium.`

## External convergence (research inputs, not ENA authority)

Relevant independent traditions include:

- Elinor Ostrom's commons research: local-condition congruence, participant rule-making, monitoring, graduated sanctions, cheap conflict resolution, self-organization rights, nested governance;
- W. Ross Ashby's Law of Requisite Variety: regulation must retain sufficient response variety for the disturbances it faces;
- Stafford Beer's Viable System Model: local autonomy plus coordination/viability functions rather than exhaustive central instruction;
- complexity-governance work on **enabling constraints**: broad boundaries that permit bottom-up experimentation/learning without prescribing behavior;
- contemporary Agent governance/runtime projects that independently converge on hard effect boundaries while leaving model cognition heterogeneous.

Pointers:

- Ostrom Nobel lecture: https://www.nobelprize.org/uploads/2018/06/ostrom_lecture.pdf
- Ashby, *An Introduction to Cybernetics*: https://www.ashby.info/Ashby-Introduction-to-Cybernetics.pdf
- Beer, Viable System Model overview/article DOI: https://doi.org/10.1057/jors.1984.2
- Pegram & Kreienkamp, *Governing Complexity*: https://pmc.ncbi.nlm.nih.gov/articles/PMC7665564/
- Microsoft Agent Governance Toolkit: https://github.com/microsoft/agent-governance-toolkit
- Evolving Agents / ai-os: https://github.com/EvolvingAgentsLabs/ai-os
- Axiarch: https://github.com/hiroyuki-miyauchi/axiarch

## Promotion discipline

This research should not be promoted because the philosophy is attractive.

Before any Current change, obtain evidence that answers at least:

1. Does the intervention ladder change real decisions compared with existing `CON-034/038` proportionality semantics?
2. Does it reduce measurable governance tax?
3. Does it preserve useful variety rather than merely increase inconsistency?
4. Does it still escalate fast enough for material externality/irreversibility?
5. Is a new normative rule actually needed, or would a decision heuristic/example/tool be sufficient?

Possible outcomes include:

`NO_NEW_RULE | CLARIFICATION | EXAMPLE | DECISION_HEURISTIC | TOOLING | EXPERIMENT_ONLY | REJECT`

Issue: #11
