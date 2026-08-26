# WAIT / Autonomous Patience reference organ

Status: `RESEARCH_PROTOTYPE / NEXT_RELEASE_INPUT / NOT_CURRENT / NOT_RELEASE_CANDIDATE`

Related: #15, #90, #91, #89, PR #82, Effect Lifecycle, Authority Lease.

## WHAT

Represent a deliberate evidence-dependent wait without turning temporary operating policy into Agent identity, role, authority, or a universal cognitive-mode taxonomy.

```text
WAIT != PAUSE != REFUSE != STOP != COMPLETE
```

This organ answers one narrow question:

> Has the represented wake condition actually occurred, should the Agent keep waiting, or has a timeout/cancellation boundary been reached?

It does **not** decide whether the Agent is authorized to resume or whether an external effect is safe to retry. Those remain separate organs.

## WHY

Without an explicit wait boundary, asynchronous workflows can become compulsive action loops:

```text
write/external effect
-> world has not settled yet
-> silence/timeout interpreted as failure
-> new action/retry
-> duplicate or conflicting consequence
```

The opposite pathology also matters:

```text
WAIT
-> no wake condition / no bounded exit where one is required
-> permanent elegant deferral
```

The useful property is **Autonomous Patience**:

> deliberately preserve agency by waiting for decision-changing evidence instead of acting merely because time passed or uncertainty is uncomfortable.

## HOW — minimal wait contract

A wait record contains, where represented:

- `wait_id`;
- `reason`;
- `entered_at`;
- a single explicit `wake_condition`;
- optional `deadline_at`;
- optional observed wake evidence/event;
- optional cancellation occurrence;
- optional `related_effect_refs` and `related_authority_refs` as dependency pointers only.

Wake-condition reference types are reference vocabulary, not a universal Host taxonomy:

- `EVIDENCE`
- `EVENT`
- `TIME`
- `MANUAL`

A Host may map these to callbacks, task tokens, timers, filesystem events, queues, polling, human responses, durable workflow signals, or another locally fitter organ.

## Resolution

- `WAITING` — wake condition not observed and no timeout/cancellation boundary reached.
- `WAKE_READY` — the represented wake condition is satisfied.
- `TIMEOUT_REACHED` — deadline passed before the wake condition was satisfied.
- `CANCELLED` — the wait was explicitly cancelled.
- `INVALID_RECORD` — represented wait state is internally inconsistent.

Reference postures:

```text
WAITING -> DO_NOT_REEXECUTE_JUST_BECAUSE_NOTHING_HAPPENED
WAKE_READY -> REVALIDATE_DEPENDENCIES_BEFORE_RESUME
TIMEOUT_REACHED -> APPLY_TIMEOUT_POLICY_NO_IMPLICIT_RETRY
CANCELLED -> STOP_WAIT_WITHOUT_COMPLETION_CLAIM
```

## Critical separations

### Wake != resume authority

A callback/event/time condition can wake the workflow while the original authority has expired or been revoked.

```text
WAKE_READY != AUTHORIZED_TO_RESUME
```

Use Authority Lease or the Host's equivalent authority mechanism where consequential authority matters.

### Timeout != retry permission

A timeout says the wait horizon ended. It does not say the external world failed to commit.

```text
TIMEOUT_REACHED != RETRY_EFFECT
```

Effect Lifecycle remains responsible for settlement/idempotency/retry decisions.

### Waiting != completion

A durable wait must not be flattened into success/completion simply because no work is currently running.

```text
NO_ACTIVE_EXECUTION != COMPLETED
```

### Waiting != refusal

WAIT preserves a path to future action when a wake condition occurs. REFUSE is a different branch/decision whose justification may remain challengeable/revisable.

This prototype does not create a universal REFUSE state machine.

## Timeout discipline

`deadline_at` is optional because not every legitimate wait requires a timer. The caller/Host remains responsible for deciding whether an open-ended wait is acceptable for the represented consequence.

Where indefinite waiting could strand a material obligation, a bounded timeout/lease/escalation path should be represented by the Host.

The reference organ therefore does **not** manufacture a universal timeout requirement merely to satisfy a schema.

## Cognitive-mode conclusion

The research does not justify a fixed ENA taxonomy such as:

`EXPLORE | EVALUATE | IMPLEMENT | VALIDATE | OBSERVE`

Those may remain useful Host-local operating policies.

The portable property that survived is smaller:

> temporary operating policy should have a decision-relevant entry/exit condition when persistence can materially change behavior; WAIT is a concrete case where the exit condition is operationally necessary.

`Agent identity != cognitive mode != role != authority` remains preserved.

## Evidence boundary

Machine PASS establishes represented wait/wake/timing consistency only.

It does not prove:

- a callback/event/evidence reference is externally authentic;
- a timer actually fires in a real Host;
- the chosen deadline is appropriate;
- wake implies effect settlement;
- wake implies current authority;
- open-ended waiting is safe for the actual obligation.

`WAKE_REPRESENTED != EXTERNAL_EVENT_TRUE`

`WAIT_CONTRACT_VALID != HOST_TIMER_LIVENESS_PROVEN`

`CURRENT_CHANGE = NO`
