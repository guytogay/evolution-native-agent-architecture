# HOW-C — Append-only event sourcing

Status: `REFERENCE_HOW / RESEARCH_ONLY`

## Host fit

Use this HOW when the system already has durable workflows, database/event-store infrastructure, or needs occurrence truth and replayable projections more than file-level branch editing.

Typical surfaces:

- workflow/commitment state;
- external-effect orchestration;
- operational Agent state;
- durable decisions/audit streams;
- systems where current state should be rebuildable from retained occurrences.

## Concrete mechanism

Store immutable occurrence events in an append-only stream. Current state is a projection, not the historical source of truth.

Illustrative event shape:

```yaml
event_id: EVT-103
stream_id: agent-42/policy
expected_stream_version: 17
kind: POLICY_CHANGE_PROPOSED
payload_ref: blob:...
actor_ref: agent-42
causal_refs: [EVT-099]
```

Append sequence:

```text
1. read stream head/version
2. build a new event with unique event_id
3. append using expected stream version / optimistic concurrency
4. if expected version mismatches, do not overwrite
5. read newly appended competing events
6. decide whether they are independent, commutative, or conflicting
7. append a reconciliation/selection/merge event when needed
8. rebuild projection from the retained event stream
```

## Concurrency behavior

Suppose two Agents read stream version 17:

```text
A appends EVT-A at expected_version=17 -> succeeds, stream becomes 18
B tries EVT-B at expected_version=17 -> concurrency failure
```

The correct response is not to mutate EVT-B's timestamp until it "wins". B reloads the stream and then may:

- abandon EVT-B;
- re-express it against the new state;
- append a conflict record;
- append a reconciliation event referencing EVT-A and the original proposal.

## Projection behavior

A projection may show only the current effective value, but the event stream retains the path that produced it.

```text
occurrence stream
-> projector
-> current state
```

A projection bug can be rebuilt/repaired without rewriting occurrence history.

This is useful for ENA distinctions such as:

```text
historical occurrence truth != current projected state
state rollback != consequence rollback
```

## Compensation behavior

Undo/compensation is represented as a new event/effect, not deletion of the old occurrence.

```text
PAYMENT_COMMITTED EVT-10
REFUND_REQUESTED EVT-14 references EVT-10
REFUND_COMMITTED EVT-18 references EVT-14
```

The historical payment still happened.

This HOW composes naturally with the Effect Lifecycle reference organ.

## Branch/merge behavior

Classic event sourcing often has one authoritative stream per aggregate. For genuinely divergent histories, a Host can use:

- separate branch stream IDs;
- a reconciliation stream/event that references multiple branch heads;
- a workflow engine's native history/continuation mechanism.

Do not pretend a single append-only sequence by itself solves offline branch merge.

## Restore behavior

Restoring an old local projection does not reset the canonical stream version.

```text
local projection restored to stream_version=11
canonical event store at version=19
-> local projection is stale
-> replay 12..19 before claiming current state
```

If the event store itself was restored/forked, history identity/epoch must be re-established before cross-branch claims.

## False-BLOCK controls

Do not require event sourcing for:

- ephemeral caches;
- trivial local scratch state;
- data that already has a safer native transactional substrate;
- CRDT-safe replicated values where a full event stream adds no decision value.

Events need not carry every ENA concept. Store the material occurrence/provenance needed by the local Host.

## Known limits

Append-only history does not prove:

- actor authority;
- event authenticity;
- semantic correctness of a projection;
- independence of multiple witnesses;
- safety of replaying external effects;
- automatic merge of divergent event stores.

## Evidence targets

Useful fixtures:

- optimistic concurrency rejection;
- stale projection replay;
- duplicate event_id with changed payload rejection;
- compensation as new event;
- projection rebuild after projector bug;
- branch stream reconciliation retaining both input head refs;
- replay logic that does not re-execute already-settled external effects.

`LOCAL_WINNER = WORKFLOW_EVENT_STORE_CANDIDATE`
