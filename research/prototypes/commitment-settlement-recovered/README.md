# Commitment / Settlement — recovered reconstruction

Status: `RESEARCH_PROTOTYPE / RECOVERED_RECONSTRUCTION / NOT_CURRENT / NOT_RELEASE_CANDIDATE`

Related: #91, #89, Effect Lifecycle, Authority Lease, Recovery Adapter, migration-lineage survival research.

## Recovery note

An earlier local Commitment/Settlement prototype was discussed and summarized durably, but its full validator/fixtures were found not to be present in GitHub during the 2026-08-26 archaeology pass. Only the durable README/Issue semantics remained reliably available.

This directory is therefore a **new reconstruction from durable semantics**, not a byte-for-byte restoration of the missing prototype.

```text
RECOVERED_SEMANTICS != ORIGINAL_BYTES
SAME_CASE_COUNT != SAME_CORPUS
```

The reconstructed selftest currently contains 18 cases. That number happens to match a prior historical corpus count but carries **no identity or ontological meaning**; the cases are newly reconstructed and fixture cardinality remains open.

## WHAT

Keep separate:

```text
OBLIGATION SUBJECT
EXECUTOR ASSIGNMENT
EFFECT IDENTITY
SETTLEMENT
```

The organ does not need to answer metaphysical sameness of an Agent across restart/fork/migration.

## WHY

Failure classes:

- two descendants both act on one indivisible obligation;
- a stale assignment remains active after a newer generation;
- executor reassignment is narrated as transfer of what is owed;
- lease expiry is narrated as cancellation;
- local completion is narrated as settlement without evidence;
- partitioning is asserted without any represented disjointness basis;
- counterparty-sensitive reassignment activates without represented acceptance;
- an accepted obligation transfer lacks basis/evidence;
- UNKNOWN/PARTIAL settlement is forced into false completion.

## Current reconstructed HOW

Files:

- `commitment-settlement.recovered-0.2.json` — research vocabulary/boundaries;
- `tools/validate_commitment_settlement.py` — represented-consistency validator + conservative next-action evaluator;
- `tools/selftest_commitment_settlement.py` — deterministic reconstructed corpus.

Core rules include:

1. one `commitment_id` survives restart/fork/reassignment;
2. `obligation_subject_ref != executor_ref`;
3. indivisible commitment has at most one ACTIVE represented assignment;
4. newer assignment generation invalidates stale ACTIVE ownership;
5. partitioned parallelism requires explicit partition IDs and a represented disjointness basis;
6. assignment/lease terminal state does not settle the obligation;
7. SETTLED/CANCELLED require represented settlement evidence;
8. obligation transfer is separate from assignment handoff and requires its own accepted basis/evidence;
9. UNKNOWN/PARTIAL remains unresolved and routes to reconciliation;
10. `represented current assignment != stale executor physically fenced`.

## Composition boundary

This organ does **not** replace:

- Effect Lifecycle: effect identity/attempt/receipt/idempotency;
- Authority Lease: current authority;
- Recovery Adapter: checkpoint/rescue/restore;
- target/provider enforcement: fencing, idempotency key, CAS, revocation.

A record may be structurally valid while external enforcement is still unsafe.

## Evidence

The reconstructed deterministic corpus is evidence only for the represented rules in this directory.

It does not prove:

- source/counterparty authenticity;
- real partition disjointness;
- current external authority;
- exactly-once effects;
- stale executor fencing;
- universal Host fit.

`CURRENT_CHANGE = NO`
