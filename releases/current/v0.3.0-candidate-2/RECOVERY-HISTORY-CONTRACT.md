# Recovery-History Contract

Status: `STRONG_CANDIDATE / HOST_EVIDENCED / NOT_MAINLINE`

## Core distinction

`Recovery State != Historical Time.`

A recovery operation may legitimately restore mutable state to an earlier known-good point.

It must not silently imply that post-checkpoint material occurrences never happened.

## Candidate property

> Rollback state; preserve history.

### Monotonic History Across Restore

For material occurrences:

- a restore may revert current mutable state;
- canonical occurrence truth should remain monotonic across restore;
- if complete occurrence preservation is not possible, the history gap itself must become visible evidence;
- recovery success claims must distinguish state restoration from historical continuity.

## Why this exists

DSH k-0083 demonstrated a failure shape where mutable knowledge state was restored while a post-checkpoint occurrence body disappeared and an event reference survived.

This is not ordinary backup correctness. Recovery material and canonical history have different temporal semantics.

## Candidate recovery transition model

Before restore, capture or classify the target mutable generation, recovery checkpoint, post-checkpoint material occurrence delta if available, canonical history stores, derived projections, and known gaps/unknowns.

After restore:

1. restore mutable state;
2. preserve or reconcile post-checkpoint canonical occurrences;
3. rebuild projections if needed;
4. validate cross-artifact references where material;
5. record any unrecoverable history gap as evidence;
6. make a scoped recovery claim.

## Recovery claim examples

Bad:

`recovery_success = true`

Better:

```text
state_restored = true
canonical_history_preserved = true|false|unknown
projection_rebuilt = true|false|not_required
known_history_gap = ...
```

A successful state restore with unknown history continuity is not a complete historical-recovery claim.

## Non-goal

This contract does not require one storage engine, event-sourcing implementation, database, Git history, or immutable ledger.

Standardize the temporal property; discover the host-specific organ.
