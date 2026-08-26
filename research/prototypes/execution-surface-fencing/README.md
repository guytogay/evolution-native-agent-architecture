# Execution-Surface Fencing HOW Comparison

Status: `RESEARCH_COMPOSITION_SIMULATOR / NOT_CURRENT / NOT_RELEASE_CANDIDATE`

Related: #91, `research/reconstruction/COMPOSITION-COMMITMENT-EFFECT-AUTHORITY-DURABLE-WORKFLOW.md`.

## Purpose

Turn the established static seam

```text
UNIQUE_CURRENT_ASSIGNMENT != STALE_EXECUTOR_PHYSICALLY_FENCED
```

into deterministic comparisons of materially different HOWs.

The simulator is deliberately small. It does not model Hazelcast, Stripe, Kubernetes, Temporal, or any provider exactly. It models **where enforcement occurs and what failure it can or cannot prevent**.

## HOWs compared

### Local assignment truth only

A ledger can truthfully say generation 2 is current while generation 1 still reaches the target. Both effects may commit.

### Provider idempotency

A stable operation/effect identity can suppress duplicate realization of the same material effect. Reusing the key for different material parameters must reject rather than silently deduplicate.

Primary protection: duplicate effect identity.

It does not intrinsically prove current executor ownership.

### Target-side fencing token

The target remembers the current/highest generation and rejects requests carrying an older generation.

Primary protection: stale executor after assignment succession.

### Optimistic concurrency / expected external version

Two requests using one expected target version cannot both mutate that version.

Important counterexample: the **stale executor can win first**, causing the current executor to receive the version conflict.

Therefore:

```text
SINGLE_VERSIONED_WRITE != CURRENT_EXECUTOR_WON
```

Optimistic concurrency is not automatically assignment fencing.

### Controlled effect gateway

A gateway can reject stale assignment generation only when all effect-equivalent paths traverse the gateway.

If a direct/bypass path remains usable:

```text
GATEWAY_CORRECT != WHOLE_EFFECT_SURFACE_FENCED
```

### Status query before retry

If the stale/unknown attempt already committed, an authoritative status query can stop the current executor from duplicating it.

But a `NOT_COMMITTED` answer does not fence a delayed stale request that arrives **after** the query.

Therefore:

```text
STATUS_QUERY
= settlement ambiguity control
!= future stale-executor fence
```

### WAIT on unknown

The current executor can decline to retry while settlement is unknown. This can avoid a duplicate attempt even if the stale executor later commits.

WAIT is safe non-action, not physical fencing.

## Deterministic evidence

The current selftest corpus exercises:

- local-ledger false confidence;
- provider idempotency duplicate suppression;
- idempotency/material-parameter mismatch rejection;
- target-side stale generation rejection;
- optimistic-concurrency stale-winner counterexample;
- fully controlled gateway;
- gateway bypass failure;
- status-query success when effect already committed;
- status-query failure to fence a future delayed stale request;
- WAIT avoiding a second attempt without claiming stale fencing.

Corpus cardinality is descriptive and open.

## Resulting engineering distinction

```text
EFFECT_IDENTITY_DEDUPE
!= ASSIGNMENT_FENCING
!= VERSION_CONFLICT_CONTROL
!= SETTLEMENT_QUERY
!= EFFECT_SURFACE_SERIALIZATION
!= SAFE_NON_RETRY
```

A Host may compose several HOWs. Selection depends on target semantics and available enforcement paths.

Do not extract a universal `ExecutionFence` schema from this simulator yet.

`ORGAN_BOUNDARY = OPEN`
`EXTERNAL_EXACTLY_ONCE = NOT_CLAIMED`
`CURRENT_CHANGE = NO`
