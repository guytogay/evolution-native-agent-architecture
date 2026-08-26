# ENA Composition Analysis — Commitment × Effect × Authority × Durable Execution

Date: 2026-08-26

Status: `STATIC_COMPOSITION_ANALYSIS / CONCRETE_HOW_EXPANSION / NOT_CURRENT / NOT_RELEASE_CANDIDATE`

Related: #91, #89, PR #82, Effect Lifecycle, Authority Grant / Lease, Recovery Adapter, external HOW registry.

## Question

Can these currently represented facts, when composed, prevent a stale fork/retry/restored executor from producing an erroneous second consequential external effect?

```text
current commitment assignment
+
valid represented authority
+
coherent effect identity/lifecycle
+
safe-resume decision
```

## Short answer

Not by themselves.

The current organs can describe which executor **should** act, whether authority **appears valid**, whether the effect record is coherent, and whether a recovered process **should** resume.

They do not necessarily make an external target reject a stale executor that still possesses a technically usable effect path.

```text
UNIQUE_CURRENT_ASSIGNMENT
!=
STALE_EXECUTOR_CANNOT_CAUSE_EFFECT
```

```text
AUTHORIZED
!=
CURRENTLY_ASSIGNED_EXECUTOR
```

```text
SAFE_RESUME_DECISION_FOR_NEW_EXECUTOR
!=
OLD_EXECUTOR_PHYSICALLY_FENCED
```

This is an execution-surface problem, not another wording problem.

## Existing component coverage

### Effect Lifecycle

Already represents:

- stable `effect_id` across retry;
- distinct attempts;
- receipt/settlement state;
- commitment ownership;
- no duplicate ACTIVE assignment for an indivisible commitment unless explicit partition semantics are represented;
- `UNKNOWN` settlement;
- idempotency strategies.

Important boundary:

The prototype explicitly validates represented lifecycle consistency only. It does not make an external target exactly-once.

### Authority Grant / Lease

Already resolves whether a named represented grant authorizes a grantee/action/subject/task/Host/optional epoch/credential at evaluation time.

Important boundary:

A valid grant is about mandate, not commitment assignment generation. A deliberately broad grant may remain valid across executor succession.

Therefore:

```text
GRANT_CURRENT
!=
EXECUTOR_ASSIGNMENT_CURRENT
```

### Recovery Adapter

Already blocks resume when represented world reconciliation or authority resolution remains unresolved.

Important boundary:

It governs the process following the recovery adapter. A stale process, old fork, old worker, alternate tool path, or delayed network request may still reach the target outside that decision path.

Therefore:

```text
RECOVERY_GATE_CORRECT
!=
WHOLE_EFFECT_SURFACE_FENCED
```

## Static failure trace

Consider one indivisible commitment `C` and one consequential effect `E`.

### Initial state

```text
commitment C
assignment generation 1 -> executor A
external grant G -> valid for grantee identity A-or-shared-agent identity
effect E -> PENDING / no confirmed receipt
```

A starts an external call and then becomes paused, partitioned, loses its local session, or becomes unreachable before learning the final external result.

### Reassignment / recovery

The system decides A is no longer the current executor and reassigns C:

```text
assignment generation 2 -> executor B
```

B may also possess valid authority for E, either through a new grant or a broad continuing mandate.

The commitment ledger is internally correct: only B is current.

### Stale execution

A later wakes, receives a delayed callback, restores an old checkpoint, or continues an already queued request.

If A can reach the external target using a still-technically-valid path, and the target does not participate in assignment/effect duplicate suppression, A can still cause E.

B can also cause E.

The system therefore has:

```text
ONE_REPRESENTED_CURRENT_EXECUTOR
+
TWO_PHYSICALLY_EFFECTIVE_EXECUTION_PATHS
```

No contradiction in the local assignment ledger prevents the second fact.

## External reality patterns

### Fenced lock / target-side fencing token

Hazelcast's FencedLock documents the exact stale-holder failure class: a client can lose lock ownership during a long pause, another client can acquire ownership, and the first client may later wake and still attempt a side effect.

The mechanism issues monotonically ordered fencing tokens on ownership changes and requires external resources to reject requests carrying an older token.

ENA implication:

```text
assignment succession
-> fencing generation/token
-> token travels with consequential request
-> target remembers/validates current-or-newer generation
-> stale executor request rejected
```

This is a strong HOW where the target can participate.

### Provider idempotency key

Stripe exposes server-side idempotency keys so retries of the same operation can reuse one key and avoid creating the same side effect twice. It also compares parameters to prevent one key from being silently reused for a materially different request.

ENA implication:

```text
stable effect_id / material intent
-> provider idempotency key
-> stale/new attempts reuse same external operation identity
-> provider suppresses duplicate realization
```

This fences duplicate **effect identity**, not necessarily stale executor identity. That may be sufficient when all legitimate executors are trying to realize the same exact effect.

The protection is provider- and retention-window-specific; local possession of an idempotency key is not universal exactly-once proof.

### Optimistic concurrency / expected resource version

Kubernetes exposes `resourceVersion` as a server-side object-version identity used for change detection and optimistic concurrency.

ENA implication:

For state transitions that can be expressed as conditional updates:

```text
read expected resource version
-> propose update bound to that version
-> stale write conflicts after another accepted transition
```

This protects a versioned resource mutation rather than arbitrary irreversible external effects.

### Durable workflow execution identity

Temporal-style durable execution and AWS Step Functions Standard workflows demonstrate another HOW family: persist workflow execution state/history so process restart does not automatically mean a fresh logical execution.

This can suppress duplicate orchestration/replay when all consequential paths are actually routed through the durable workflow boundary.

ENA implication:

```text
stable workflow/execution identity
+ durable history
+ durable Activity/task identity
+ controlled effect path
-> process restart/failover need not mint a new logical effect
```

But a durable workflow cannot make a fundamentally non-idempotent external API exactly-once merely by wrapping it. If the external call commits and the acknowledgement is lost, safe retry still needs provider idempotency, status query/settlement evidence, fencing, compensation, or human reconciliation.

## Candidate HOW branches

These are **coexisting mechanisms**, not a fixed universal ladder.

### HOW — Effect-identity idempotency

Use when the target/provider accepts a stable idempotency key.

```text
effect_id + material_parameters_digest
-> stable provider operation key
-> every retry/failover/reassigned executor uses the same key
```

Primary protection:

- duplicate realization of the same intended effect.

Failure boundary:

- provider does not support idempotency;
- key retention/namespace differs from commitment lifetime;
- alternate path bypasses the key;
- the second request is materially a different effect.

### HOW — Assignment-generation fencing

Use when the external target can validate an ordered ownership/fencing generation.

```text
assignment ownership changes
-> issue monotonic fencing generation
-> every consequential request carries generation
-> target persists highest/current generation
-> target rejects stale generation
```

Primary protection:

- stale executor after reassignment/lease loss.

Failure boundary:

- target cannot participate;
- some effect-equivalent path omits the token;
- generation is only checked locally rather than at the side-effect boundary.

### HOW — Conditional state transition / optimistic concurrency

Use when the consequential action is a versioned resource mutation.

```text
expected external version
-> conditional update
-> stale update rejected after competing accepted change
```

Primary protection:

- stale writes to mutable versioned state.

Failure boundary:

- irreversible actions without a versioned target;
- create/send/pay operations whose semantics are not reducible to one resource CAS.

### HOW — Durable single logical execution

Use when a workflow/runtime can persist execution identity, task/activity history, retries, waits, and failover.

Primary protection:

- process restart/failover does not create a new logical workflow merely because the worker changed.

Failure boundary:

- uncontrolled direct APIs/tools bypass the workflow;
- external effect acknowledgement ambiguity remains unresolved;
- the runtime history is itself not authoritative for the external target.

### HOW — Status-query / settlement-before-retry

Use when the external system exposes a reliable way to query whether the intended effect already occurred.

```text
timeout / unknown
-> do not mint new intent
-> query external status using stable effect/business identity
-> retry only after NOT_COMMITTED evidence
```

Primary protection:

- acknowledgement loss / uncertain settlement.

Failure boundary:

- no authoritative status query;
- query is stale/ambiguous;
- externally visible effect has no stable lookup identity.

### HOW — Serialization through one effect gateway

Use when the Host can constrain all effect-equivalent paths behind one durable gateway/queue/outbox/worker boundary.

Primary protection:

- multiple local executors cannot independently bypass the ownership/duplicate-suppression mechanism.

Failure boundary:

- alternate tools/native APIs remain available;
- gateway shares a failure domain that creates false liveness/ownership assumptions;
- serialization alone does not resolve uncertain external commit.

### HOW — Compensation / manual reconciliation

Use when prevention is impossible but consequences are detectable/compensable.

Primary protection:

- truthful recovery from duplicate/partial external reality.

This is not duplicate prevention and must not be narrated as exactly-once execution.

### HOW — WAIT / refuse unsafe retry

Use when:

```text
settlement = UNKNOWN
AND no provider idempotency
AND no authoritative status query
AND no enforceable fencing/conditional-write path
AND duplicate consequence is material
```

Then the correct operational behavior can be:

```text
WAIT / NARROW / ESCALATE / MANUAL_RECONCILIATION
```

rather than creating a new attempt with false confidence.

## Composition rule that emerges

The practical property is not merely:

> only one current executor should exist.

It is closer to:

> A superseded executor must not be able to produce an unaccounted consequential effect through the controlled effect surface once execution ownership has moved, unless the effect is safely duplicate-tolerant and this is explicit.

This is still a **property statement**, not a mandated organ.

Different Hosts may satisfy it through different combinations of:

- provider idempotency;
- fencing tokens;
- conditional versions;
- durable workflow identity/history;
- single effect gateway;
- status/settlement queries;
- compensation/reconciliation;
- safe refusal to retry.

## No new universal organ yet

Do **not** immediately create a universal `ExecutionFence` object/schema.

The evidence currently supports a missing **execution-fencing capability/property** and several concrete HOWs.

Whether this deserves:

- a new standalone reference organ;
- an Effect Lifecycle extension;
- a Commitment Assignment extension;
- an Authority Lease binding;
- a Host adapter interface;
- or only an effect-surface composition contract

remains a boundary hypothesis.

`ORGAN_BOUNDARY = OPEN`.

## Concrete next engineering work

1. Repair/finish the separate Commitment/Settlement reference prototype so assignment generations and partition semantics are represented without claiming physical fencing.
2. Extend cross-organ deterministic fixtures with a stale-executor case where local ledgers are all internally valid but the target accepts both old and new executors.
3. Add positive controls for materially different HOWs:
   - provider idempotency;
   - target-side fencing token;
   - conditional external version;
   - durable workflow + controlled effect gateway;
   - status-query-before-retry;
   - unresolved/no-safe-path -> WAIT/manual reconciliation.
4. Explicitly test effect-equivalent bypass paths.
5. Only after these concrete mechanisms exist, consider extracting a common Host adapter/interface.

## Evidence boundary

This analysis statically proves a representational/composition gap: current assignment/authority/recovery records do not by themselves physically stop stale external execution.

It does **not** prove:

- one fencing mechanism is universally best;
- external targets actually implement the represented mechanism;
- provider idempotency lasts for the entire ENA commitment lifetime;
- durable workflow history is external settlement truth;
- optimistic concurrency applies to arbitrary effects;
- the current candidate HOW inventory is complete.

```text
STATIC_COMPOSITION_GAP = ESTABLISHED
UNIVERSAL_ORGAN_SHAPE = NOT_ESTABLISHED
EXTERNAL_EXACTLY_ONCE = NOT_CLAIMED
CURRENT_CHANGE = NO
```
