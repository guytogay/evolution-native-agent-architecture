# ENA Opportunity Liveness Discipline

Status: `PROJECT_METHOD / MAIN_CONTROL_PLANE / IMMEDIATE_EFFECT_AFTER_MERGE`

Updated: 2026-09-07

## Why this exists

ENA already permits external contributions, latent variations, `WAIT_FOR_CONTEXT`, dormancy, wake channels, and rapid successors. Those mechanisms protect against premature mutation, but they can also create a different failure mode:

```text
VALUABLE_OPPORTUNITY
-> ACCEPT_DIRECTION
-> WAIT_FOR_MORE_EVIDENCE
-> no explicit next action or wake condition
-> indefinite opportunity debt
```

A legitimate latent state must not become an unbounded parking lot.

This discipline closes the gap between:

- contribution admission;
- triggered material obligations;
- activation/wake semantics;
- the Minimum Evolution Loop;
- rapid Current succession.

```text
LATENT != FORGOTTEN
WAIT != UNSPECIFIED_DELAY
ACCEPT_DIRECTION != COMPLETE_RECONCILIATION
```

## Scope

Apply this discipline to decision-relevant:

- external contributions;
- design opportunities;
- maintainer-discovered improvements;
- latent evolution candidates;
- partially supported variations;
- field findings whose value is plausible but not yet sufficient for integration.

It does not require every passing idea to become tracked work.

## Required liveness disposition

Once a maintainer/project manager has concluded that an opportunity is worth preserving as a real candidate, reconciliation is incomplete until the candidate has exactly one current liveness disposition:

### `ADVANCE_NOW`

Use when a bounded decision-changing next action exists now and the project/Agent has the authority and tools to execute it.

Required fields:

- exact next action;
- decision it can change;
- evidence/result that would advance, narrow, reject, or integrate the candidate;
- consequence/recovery boundary where material.

Rule:

```text
DECISION_CHANGING_ACTION_AVAILABLE
+ AUTHORITY_AVAILABLE
+ TOOLING_AVAILABLE
-> EXECUTE_OR_EXPLICITLY_DEPRIORITIZE
```

Do not write `more evidence needed` when the cheapest relevant evidence can already be gathered.

### `WAIT_FOR_SIGNAL`

Use only when the required evidence depends on a future context that is not presently available or when forcing the trial would distort the phenomenon.

Required fields:

- exact wake signal / context;
- why manufacturing the signal now would be inferior or invalid;
- first action to execute when the signal occurs;
- fallback review condition if the wake signal becomes obsolete or implausible.

Invalid wake conditions include:

- `wait for more evidence`;
- `revisit later`;
- `wait for a future release`;
- `wait until we have time`.

A valid wake condition names an observable event or decision context.

### `BLOCKED`

Use when a real external boundary prevents the next decision-changing action.

Required fields:

- blocker;
- whether it is authority, tool, Host, account/UI, physical, dependency, safety, or other boundary;
- exact unblock condition;
- what can be prepared without crossing the boundary.

Do not use `BLOCKED` when the Agent can self-execute the work with available tools and authority.

### `REJECT`

Use when the candidate is not worth further cost, is contradicted, duplicates a better path, or cannot plausibly change a material decision.

Preserve the occurrence/provenance needed to avoid rediscovering the same dead end.

### `ARCHIVE`

Use when the candidate was once relevant but has been superseded or its activation context no longer exists.

Archive is not a negative selection verdict unless evidence supports that verdict.

## Candidate progression contract

For every preserved material opportunity:

```text
OBSERVE
-> RECONCILE
-> ADVANCE_NOW | WAIT_FOR_SIGNAL | BLOCKED | REJECT | ARCHIVE
-> reality contact when activated
-> SELECT
-> INTEGRATE / NARROW / DORMANT / REJECT / ARCHIVE
```

The following states are not sufficient on their own:

```text
OPEN
DRAFT
ACCEPT_DIRECTION
EVIDENCE_NEEDED
NO_SUCCESSOR_TRIGGER_YET
```

Each must be paired with a liveness disposition that says what happens next or why nothing should happen yet.

## Opportunity debt

Opportunity debt exists when a preserved candidate has value acknowledged but lacks a valid liveness disposition.

Examples:

- a PR remains open because the direction is attractive, with no named experiment or wake condition;
- an Issue lists a plausible design improvement but only says it should be revalidated someday;
- a candidate is `UNKNOWN` and repeatedly carried across handoffs without a decision-changing next observation;
- a project says `NO_SUCCESSOR_TRIGGER_YET` without naming what observation would create or permanently remove that trigger.

Opportunity debt should be treated like governance debt: make it explicit, then either pay it with the smallest decision-changing action or close/dormant it truthfully.

```text
PRESERVE_POSSIBILITY != PRESERVE_UNBOUNDED_BACKLOG
UNKNOWN != PERMANENT_LIMBO
```

## Priority rule

Liveness does not mean every candidate runs immediately.

When several `ADVANCE_NOW` candidates compete, prioritize by:

1. decision consequence;
2. information gain per cost;
3. reversibility / recovery quality;
4. dependency unlocking;
5. whether delay knowingly exports a defect or blocks useful evolution.

A lower-priority candidate may remain pending, but its next action and reason for deprioritization must stay explicit.

## Relation to rapid Current succession

A confirmed bounded Current defect with an available fix already follows the Rapid Current Release Discipline and should not be held in opportunity state.

For non-defect opportunities:

```text
OPPORTUNITY_IDENTIFIED
-> LIVENESS_DISPOSITION
-> smallest decision-changing reality contact
-> if value demonstrated: smallest justified successor
-> otherwise narrow/reject/archive
```

Do not require an opportunity to masquerade as a bug before it may progress.

```text
BUG != ONLY_VALID_SUCCESSOR_TRIGGER
DEMONSTRATED_BOUNDED_VALUE -> SUCCESSOR_CANDIDATE
```

The evidence burden remains proportional to R0/R1/R2 change class.

## Handoff/readback rule

Deep succession must not merely list open candidates. For every live material candidate, preserve:

- current liveness disposition;
- exact next action or wake/unblock condition;
- current evidence boundary;
- canonical location/provenance.

A successor session should be able to tell whether it should act now, wait for a named event, or close the candidate without reconstructing the original conversation.

## Anti-ceremony boundary

Do not add arbitrary deadlines or periodic reviews merely to create motion.

Time itself is a valid wake trigger only when time changes applicability, cost, authority, evidence, or consequence. Otherwise prefer event/context triggers.

A queue that repeatedly wakes candidates when nothing can change is not liveness; it is ceremony.

## Durable relations

```text
LATENT != FORGOTTEN
WAIT != UNSPECIFIED_DELAY
ACCEPT_DIRECTION != COMPLETE_RECONCILIATION
NO_SUCCESSOR_TRIGGER_YET -> NAME_THE_TRIGGER_OR_CLOSE_THE_PATH
DECISION_CHANGING_ACTION_AVAILABLE + AUTHORITY_AVAILABLE -> ADVANCE_NOW
PRESERVE_POSSIBILITY != PRESERVE_UNBOUNDED_BACKLOG
BUG != ONLY_VALID_SUCCESSOR_TRIGGER
DEMONSTRATED_BOUNDED_VALUE -> SMALLEST_JUSTIFIED_SUCCESSOR
```
