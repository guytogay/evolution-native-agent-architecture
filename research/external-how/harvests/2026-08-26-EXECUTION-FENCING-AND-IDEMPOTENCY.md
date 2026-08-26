# External HOW Harvest — Execution Fencing and Idempotency — 2026-08-26

Status: `DATED_EXTERNAL_HOW_HARVEST / EFFECT_EXECUTION / NOT_SELECTION / NOT_CURRENT`

Related: `research/reconstruction/COMPOSITION-COMMITMENT-EFFECT-AUTHORITY-DURABLE-WORKFLOW.md`, #91.

## Research question

Once commitment execution ownership moves from one executor to another, what concrete mechanisms can prevent an old/stale executor, retry, delayed request, or restored process from causing a second consequential external effect?

The search deliberately distinguishes several failure classes rather than treating "idempotency" as one universal answer.

## Hazelcast FencedLock — target-side stale-owner rejection

Source class: `OFFICIAL_DISTRIBUTED_SYSTEM_DOCUMENTATION`

Sources:

- https://docs.hazelcast.com/hazelcast/5.6/data-structures/fencedlock
- https://docs.hazelcast.com/hazelcast/5.2/data-structures/fencedlock

Observed mechanism:

A client can lose lock ownership during a long pause while another client acquires the lock. The old client may later wake and still attempt to act. Hazelcast therefore issues monotonically increasing fencing tokens on ownership changes; external services/resources must receive the token and reject requests carrying an older token.

ENA mapping:

```text
commitment assignment generation
-> fencing token
-> consequential request carries token
-> target persists/validates current-or-newer token
-> stale assignment request rejected
```

This mechanism addresses **stale executor ownership**, not merely duplicate logical effect identity.

Selection state: `HIGH_VALUE_CANDIDATE_HOW / TARGET_MUST_PARTICIPATE`.

## Stripe idempotency — provider-side effect identity deduplication

Source class: `OFFICIAL_PROVIDER_API_DOCUMENTATION`

Source:

- https://docs.stripe.com/api/idempotent_requests

Observed mechanism:

Clients send a stable idempotency key for a create/update operation. Stripe persists the first execution result for the key and returns the same result for later retries; it also compares parameters so the key is not silently reused for materially different requests.

ENA mapping:

```text
stable ENA effect_id / material intent
-> provider idempotency key
-> all retry/failover/reassigned attempts reuse key
-> provider suppresses duplicate realization
```

This addresses duplicate realization of one logical effect. It does not establish executor-currentness and is bounded by provider semantics/retention scope.

Selection state: `HIGH_VALUE_PROVIDER_NATIVE_HOW`.

## Kubernetes resourceVersion — optimistic concurrency / stale state mutation rejection

Source class: `OFFICIAL_PLATFORM_API_DOCUMENTATION`

Sources:

- https://kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-meta/
- https://kubernetes.io/docs/reference/using-api/api-concepts/

Observed mechanism:

Kubernetes objects carry a server-generated `resourceVersion` that can be used for optimistic concurrency/change detection. Clients can bind a state-changing operation to the external object's expected version rather than assuming their local copy is current.

ENA mapping:

```text
read external state/version
-> propose transition against expected version
-> another accepted transition changes version
-> stale writer no longer has a matching precondition
```

This is a concrete HOW for versioned mutable resources. It is not a solution for every external effect such as sending an email or making a payment.

Selection state: `CONDITIONAL_HOW / VERSIONED_RESOURCE_EFFECTS`.

## AWS Step Functions — durable logical workflow execution identity

Source class: `OFFICIAL_DURABLE_WORKFLOW_DOCUMENTATION`

Source:

- https://docs.aws.amazon.com/step-functions/latest/dg/step-functions-dg.pdf

Observed mechanism:

AWS documents different execution guarantees by workflow class. Standard Workflows persist state between transitions and provide exactly-once workflow execution semantics; starting a currently-running Standard workflow with the same name receives idempotent handling. Express workflows have different guarantees and require idempotent state-machine logic where applicable.

ENA mapping:

```text
stable workflow/execution identity
+ durable state/history
-> worker/process restart does not automatically mint a second logical execution
```

Important boundary:

Workflow-level exactly-once claims do not automatically prove arbitrary downstream external APIs have exactly-once side effects. Effect-level idempotency/settlement must still be considered.

Selection state: `DURABLE_EXECUTION_HOW / GUARANTEE_SCOPE_MUST_REMAIN_EXPLICIT`.

## Temporal engineering boundary — wrapping a non-idempotent external API is not magic

Source class: `FRAMEWORK_COMMUNITY_SUPPORT / ENGINEERING_EXPLANATION`

Source:

- https://community.temporal.io/t/activity-external-call-idempotency/7543

Observed claim:

A Temporal maintainer explains that if an external API is non-idempotent and a timeout leaves commit status unknown, a wrapper cannot guarantee exactly-once invocation; practical options require an idempotent external API or a way to query whether the request was applied.

ENA mapping:

This reinforces:

```text
durable local workflow
!= external exactly-once
```

and supports `QUERY_SETTLEMENT / WAIT / MANUAL_RECONCILIATION` when the external system cannot safely deduplicate or reveal commit state.

Evidence caution:

This is community/support evidence rather than a formal proof artifact, although it expresses a standard distributed-systems impossibility boundary.

Selection state: `BOUNDARY_EVIDENCE`.

## Synthesis — distinct concrete HOW families

The external search supports multiple non-equivalent mechanisms:

```text
provider idempotency key
assignment-generation fencing token
conditional external version / optimistic concurrency
durable workflow/execution identity
status-query-before-retry
single controlled effect gateway
compensation/manual reconciliation
WAIT/refuse unsafe retry
```

This list is open-cardinality and descriptive.

### Key distinction

```text
EFFECT_IDEMPOTENCY
!= EXECUTOR_FENCING
!= STALE_STATE_CONCURRENCY_CONTROL
!= DURABLE_LOGICAL_EXECUTION
!= EXTERNAL_SETTLEMENT_PROOF
```

They can compose but must not be silently merged into one generic "exactly once" claim.

## ENA implication

The immediate ENA property exposed by composition is:

> After execution ownership moves, a superseded executor must not be able to produce an unaccounted consequential effect through the controlled effect surface unless duplicate execution is explicitly safe for that effect.

This property does not yet establish a universal organ shape.

Potential implementation locations remain open:

- Effect Lifecycle extension;
- Commitment Assignment/Settlement organ;
- Host effect adapter;
- authority/assignment binding;
- target/provider-native mechanism;
- whole-effect-surface gateway.

`ORGAN_BOUNDARY = OPEN`.

## Next evidence

Use deterministic composition fixtures before stochastic experiments:

- stale executor accepted when only the local assignment ledger changes;
- same scenario blocked by target-side fencing;
- same-effect retries suppressed by provider idempotency;
- stale resource update rejected by external version precondition;
- durable workflow prevents fresh logical execution after worker restart;
- external commit UNKNOWN with no safe mechanism -> WAIT/manual reconciliation;
- effect-equivalent alternate path bypasses the selected fence and must remain visible as a defect.
