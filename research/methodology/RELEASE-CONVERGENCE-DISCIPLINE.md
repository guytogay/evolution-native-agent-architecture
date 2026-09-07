# ENA Release Convergence Discipline

Status: `PROJECT_METHOD / MAIN_CONTROL_PLANE / IMMEDIATE_EFFECT_AFTER_MERGE`

Updated: 2026-09-07

## Purpose

A release is not a point where known work is renamed, deferred, or rolled into an indefinite future queue. It is a convergence boundary at which the project must make the best currently available decisions about every known material work item.

```text
RELEASE != BACKLOG_RENAMING_EVENT
NEXT_CYCLE != GENERIC_DEFERRAL_BUCKET
OPEN_WORK_ITEM != DURABLE_MEMORY
```

The ideal release-ready state is:

```text
OPEN_MATERIAL_PR = 0
OPEN_MATERIAL_ISSUE = 0
UNSPECIFIED_PENDING = 0
```

This is a target for decision closure, not a command to hide uncertainty or close tickets cosmetically.

## What counts as resolved

A known material item is resolved only when one of these is true:

1. **Integrated** — the supported bounded value has been implemented/admitted and relevant gates/readback pass.
2. **Rejected** — evidence or reasoning is sufficient to decide not to adopt it; preserve provenance needed to avoid rediscovery.
3. **Superseded/absorbed** — its useful content is demonstrably covered by another integrated change; record the mapping and close the redundant item.
4. **Narrowed and integrated** — an overbroad proposal is reduced to the part current evidence actually supports, then integrated.
5. **Externally unresolvable now** — the decision truly depends on a future external fact that cannot be manufactured, substituted, or obtained with current authority/tooling. In this case preserve a dormant evidence record with the observable trigger, then close the active PR/Issue. If the trigger later occurs, create a new work item from that new occurrence.

The fifth state is not "move to next cycle." It ends the present work item because there is no present action left to perform.

```text
DORMANT_EVIDENCE != OPEN_WORK
FUTURE_TRIGGER_OCCURS -> NEW_ACTIVE_OCCURRENCE
```

## Invalid release dispositions

The following do not resolve a material item:

- `revisit later`;
- `next version` / `next cycle` without a current decision;
- `more evidence needed` when the evidence can be gathered now;
- `accepted direction` with no integration/rejection decision;
- `keep open for visibility`;
- `field validation` used as a parking state;
- `research idea` used as a permanent GitHub queue entry.

```text
NAMED_FUTURE_CYCLE != RESOLUTION
OPEN_FOR_VISIBILITY != ACTIVE_WORK
```

## Release-close review

Before promoting a new Current, review the whole live project surface, not only the release PR:

- all open PRs;
- all open Issues;
- candidate/admission queues in live state files;
- `WAIT`, `UNKNOWN`, `BLOCKED`, `DRAFT`, `EVIDENCE_NEEDED`, and similar states;
- cross-repository pending items in the canonical project ecosystem;
- temporary experiment surfaces that still contain unique evidence.

For each material item ask in this order:

1. Can the Agent/project execute a decision-changing action now? If yes, do it.
2. Is enough evidence already present to integrate a narrower claim? If yes, narrow and integrate.
3. Is enough evidence present to reject/supersede it? If yes, close with that decision.
4. Does the unresolved part depend on a genuinely future external occurrence? If yes, preserve dormant evidence + trigger and close the active item.
5. Otherwise the project has not converged; do not call the release backlog-clean.

## Relationship to Opportunity Liveness

Opportunity Liveness prevents accepted opportunities from becoming unspecified limbo during active development.

Release Convergence is stronger at a release boundary:

```text
ACTIVE_DEVELOPMENT: opportunity must have liveness
RELEASE_BOUNDARY: known material work must reach a current decision
```

`WAIT_FOR_SIGNAL` may be valid during active work. It is not a reason to carry an open GitHub work item forever. At release close, convert it to a durable dormant record and close the active item unless the signal is already obtainable and therefore should be pursued now.

## Relationship to field validation

Field validation continues through real use, but a permanently open umbrella Issue is not required to preserve that fact.

A field occurrence should create a concrete active work item when it exists. Once reconciled, close it. New reality contact creates a new occurrence rather than keeping an eternal catch-all backlog ticket open.

```text
FIELD_VALIDATION != PERMANENT_OPEN_ISSUE
REALITY_CONTACT_CONTINUES != BACKLOG_MUST_STAY_OPEN
```

## Anti-cosmetic-closure rule

Do not optimize the metric by closing unresolved work without deciding it.

A zero-open release is meaningful only if:

- integrated work is actually integrated;
- rejected work has a reason;
- superseded work names what replaced it;
- dormant evidence names the external trigger and contains no executable present action;
- no known actionable defect/opportunity has been hidden in prose, handoff notes, or a future-cycle label.

```text
ZERO_OPEN_ITEMS_WITH_HIDDEN_DEBT != CONVERGENCE
```

## Product implication

ENA should not stop at `understand the distinction`. For decision-relevant signals, the architecture should make the transition from understanding to action/selection/closure explicit.

A useful ENA should reduce the frequency of:

> "Yes, that distinction makes sense. So what?"

The operational answer must be one of:

```text
ACT
TEST
INTEGRATE
NARROW
REJECT
CLOSE_AS_DORMANT_EXTERNAL_TRIGGER
```

not indefinite acknowledgement.

## Durable relations

```text
RELEASE != BACKLOG_RENAMING_EVENT
NEXT_CYCLE != GENERIC_DEFERRAL_BUCKET
OPEN_WORK_ITEM != DURABLE_MEMORY
DORMANT_EVIDENCE != OPEN_WORK
FIELD_VALIDATION != PERMANENT_OPEN_ISSUE
ZERO_OPEN_ITEMS_WITH_HIDDEN_DEBT != CONVERGENCE
UNDERSTANDING_WITHOUT_DECISION_PATH != OPERATIONAL_COMPLETION
```
