# ENA Release Convergence Discipline

Status: `PROJECT_METHOD / MAIN_CONTROL_PLANE / IMMEDIATE_EFFECT_AFTER_MERGE`

Updated: 2026-09-07

## Purpose

A release is not a point where known work is renamed, deferred, or rolled into an indefinite future queue. It is a convergence boundary at which the project must make the best currently available decisions about every known material work item **and every known material forward risk/opportunity**.

```text
RELEASE != BACKLOG_RENAMING_EVENT
NEXT_CYCLE != GENERIC_DEFERRAL_BUCKET
OPEN_WORK_ITEM != DURABLE_MEMORY
NO_CURRENT_INCIDENT != NO_FUTURE_RISK
```

The ideal release-ready state is:

```text
OPEN_MATERIAL_PR = 0
OPEN_MATERIAL_ISSUE = 0
UNSPECIFIED_PENDING = 0
UNADJUDICATED_KNOWN_FORWARD_RISK = 0
```

This is a target for real decision closure, not a command to hide uncertainty, optimize ticket counts, or solve only what already broke.

## Proactive resolution obligation

ENA must not wait for every foreseeable problem to become an incident before acting.

For every credible material defect, opportunity, failure path, scaling risk, portability risk, governance risk, or contributor hypothesis, ask:

1. **Can we reason it through now?** Use the current semantic model, prior evidence, counterexamples and dependency analysis.
2. **Can we obtain external evidence now?** Search relevant literature, implementations, incidents, communities, standards or comparable systems when that evidence can change the decision.
3. **Can we create a discriminating condition now?** Use a bounded prototype, adversarial case, counterfactual, simulation, canary, cleanroom or controlled reality contact when the outcome is not already baked into the setup.
4. **Can we prevent the failure cheaply now?** Prefer a bounded preventive mechanism when the risk is credible and the protection cost is justified.
5. **Can we narrow the claim so the supported part is useful now without pretending the unsupported part is solved?**

Only after these routes are exhausted may the project conclude that the unresolved remainder truly depends on a future external fact.

```text
KNOWN_PLAUSIBLE_RISK -> SEEK_DISCRIMINATING_EVIDENCE_OR_PREVENTION
NO_INCIDENT_YET != CLOSE_WITHOUT_ANALYSIS
FUTURE_RISK != FUTURE_CYCLE_BY_DEFAULT
```

The project should actively create conditions for learning when safe, cheap and decision-relevant. It should not manufacture low-information experiments merely to demonstrate activity.

```text
PROACTIVE != CEREMONIAL
ANTICIPATION != SPECULATION_ACCUMULATION
```

## What counts as resolved

A known material item is resolved only when one of these is true:

1. **Integrated** — the supported bounded value has been implemented/admitted and relevant gates/readback pass.
2. **Prevented/mitigated** — a credible forward failure path has a proportionate preventive mechanism or bounded safeguard whose residual risk is explicit.
3. **Rejected** — evidence/reasoning/counterexample analysis is sufficient to decide not to adopt the proposal or not to treat the forecast risk as material.
4. **Superseded/absorbed** — its useful content is demonstrably covered by another integrated change; record the mapping and close the redundant item.
5. **Narrowed and integrated** — an overbroad proposal is reduced to the part current evidence actually supports, then integrated.
6. **Externally unresolvable now after active search** — the decision truly depends on a future external fact that cannot be reasoned through, researched, simulated, safely prototyped, substituted, or obtained with current authority/tooling. Preserve a dormant evidence record containing the exact residual uncertainty, what proactive routes were attempted, and the observable trigger. Close the active PR/Issue only because there is literally no current decision-changing action left.

The sixth state is not "move to next cycle." It is a bounded epistemic conclusion after active effort.

```text
DORMANT_EVIDENCE != OPEN_WORK
FUTURE_TRIGGER_OCCURS -> NEW_ACTIVE_OCCURRENCE
```

## Invalid release dispositions

The following do not resolve a material item:

- `revisit later`;
- `next version` / `next cycle` without a current decision;
- `more evidence needed` when evidence can be gathered or a discriminating condition can be created now;
- `accepted direction` with no integration/rejection/prevention decision;
- `keep open for visibility`;
- `field validation` used as a parking state;
- `research idea` used as a permanent GitHub queue entry;
- `it has not happened yet` used as a reason to stop analysis of a credible forward risk.

```text
NAMED_FUTURE_CYCLE != RESOLUTION
OPEN_FOR_VISIBILITY != ACTIVE_WORK
ABSENCE_OF_INCIDENT != ABSENCE_OF_DECISION_MATERIAL_RISK
```

## Release-close review

Before promoting a new Current, review the whole live project surface, not only the release PR:

- all open PRs;
- all open Issues;
- candidate/admission queues in live state files;
- `WAIT`, `UNKNOWN`, `BLOCKED`, `DRAFT`, `EVIDENCE_NEEDED`, and similar states;
- known forward risks/opportunities recorded outside GitHub work items;
- cross-repository pending items in the canonical project ecosystem;
- temporary experiment surfaces that still contain unique evidence.

For each material item ask in this order:

1. Can the Agent/project execute a decision-changing action now? If yes, do it.
2. Can external research, adversarial reasoning, a prototype, simulation, canary or bounded reality contact produce discriminating evidence now? If yes, do the cheapest valid one.
3. Is enough evidence present to prevent/mitigate a credible forward failure now? If yes, implement proportionately.
4. Is enough evidence already present to integrate a narrower claim? If yes, narrow and integrate.
5. Is enough evidence present to reject/supersede it? If yes, close with that decision.
6. Does the unresolved remainder truly depend on a future external occurrence after the proactive routes above are exhausted? If yes, preserve a dormant evidence record + trigger and close the active item.
7. Otherwise the project has not converged; do not call the release backlog-clean.

## Relationship to Opportunity Liveness

Opportunity Liveness prevents accepted opportunities from becoming unspecified limbo during active development.

Release Convergence is stronger at a release boundary:

```text
ACTIVE_DEVELOPMENT: opportunity must have liveness
RELEASE_BOUNDARY: known material work and forward risk must reach a current decision
```

`WAIT_FOR_SIGNAL` may be valid during active work only when the signal cannot reasonably be created or substituted now. It is not a reason to carry an open GitHub work item forever. At release close, convert a truly irreducible future dependency to a durable dormant record and close the active item; if the signal is obtainable now, pursue it instead.

## Relationship to field validation

Field validation continues through real use, but a permanently open umbrella Issue is not required to preserve that fact.

A field occurrence should create concrete active work when it exists. Once reconciled, close it. New reality contact creates a new occurrence rather than keeping an eternal catch-all backlog ticket open.

At the same time, field validation is not an excuse to postpone predictable failure analysis until production reality supplies an incident.

```text
FIELD_VALIDATION != PERMANENT_OPEN_ISSUE
REALITY_CONTACT_CONTINUES != BACKLOG_MUST_STAY_OPEN
FIELD_VALIDATION != WAIT_FOR_FAILURE
```

## Anti-cosmetic-closure rule

Do not optimize the metric by closing unresolved work without deciding it.

A zero-open release is meaningful only if:

- integrated work is actually integrated;
- preventive work actually addresses a named credible failure path;
- rejected work has a reason;
- superseded work names what replaced it;
- dormant evidence records what proactive routes were exhausted and names the irreducible external trigger;
- no known actionable defect/opportunity/forward risk has been hidden in prose, handoff notes, or a future-cycle label.

```text
ZERO_OPEN_ITEMS_WITH_HIDDEN_DEBT != CONVERGENCE
```

## Product implication

ENA should not stop at `understand the distinction`. For decision-relevant signals and credible forward risks, the architecture should make the transition from understanding to action, evidence creation, prevention, selection or closure explicit.

A useful ENA should reduce the frequency of:

> "Yes, that distinction makes sense. So what?"

The operational answer must be one of:

```text
ACT
RESEARCH
TEST
SIMULATE
PREVENT
INTEGRATE
NARROW
REJECT
CLOSE_AS_TRULY_IRREDUCIBLE_DORMANT_EVIDENCE
```

not indefinite acknowledgement and not "nothing has broken yet."

## Durable relations

```text
RELEASE != BACKLOG_RENAMING_EVENT
NEXT_CYCLE != GENERIC_DEFERRAL_BUCKET
OPEN_WORK_ITEM != DURABLE_MEMORY
NO_CURRENT_INCIDENT != NO_FUTURE_RISK
KNOWN_PLAUSIBLE_RISK -> SEEK_DISCRIMINATING_EVIDENCE_OR_PREVENTION
DORMANT_EVIDENCE != OPEN_WORK
FIELD_VALIDATION != PERMANENT_OPEN_ISSUE
FIELD_VALIDATION != WAIT_FOR_FAILURE
ZERO_OPEN_ITEMS_WITH_HIDDEN_DEBT != CONVERGENCE
UNDERSTANDING_WITHOUT_DECISION_PATH != OPERATIONAL_COMPLETION
PROACTIVE != CEREMONIAL
```
