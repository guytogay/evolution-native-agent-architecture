# Effect Lifecycle — Independent Selection Review Protocol

Status: `RESEARCH_REVIEW_PROTOCOL / ANTI_ABLATION / NOT_CURRENT`

Target: `research/prototypes/effect-lifecycle/`

Related: #91, #89, PR #82, `research/reconstruction/MECHANISM-RETENTION-LEDGER.md`.

## Purpose

This is not a deletion-oriented falsification exercise.

The review asks two equally important questions:

1. **Where does the prototype permit a material false claim, duplicate effect, false-BLOCK, or misleading settlement?**
2. **Which concrete mechanisms earn retention because removing them would make a real Host less able to implement the underlying ENA property?**

The reviewer must not treat a smaller ontology or fewer objects as success by itself.

> **Falsify the claim. Preserve the working mechanism.**

## Review independence

The reviewer should be fresh to this prototype where practical.

Before accepting authored fixture verdicts as truth:

- inspect the contract and validator behavior;
- reason independently about consequential effect semantics;
- identify missing legitimate cases and missing unsafe cases;
- distinguish represented consistency from external truth;
- do not assume the author-selected four-object split is minimal or complete.

The reviewer may conclude that all, some, or none of the proposed objects are useful.

## Required evidence distinctions

Keep separate:

```text
PROPERTY_NEEDED
REFERENCE_ORGAN_USEFUL
HOST_MAPPING_AVAILABLE
MACHINE_GUARDED
EXTERNALLY_MATURE_PATTERN
HOST_EXECUTED
FIELD_SUPPORTED
```

Also keep separate:

```text
RECEIPT_REPRESENTED
!= RECEIPT_AUTHENTIC
!= SETTLEMENT_ESTABLISHED
```

and:

```text
LOCAL_STATE_RESTORED
!= WORLD_STATE_REVERSED
```

## Review dimensions

### A. Intent identity

Test whether one logical effect can be duplicated or conflated through:

- parameter drift;
- target drift;
- authority-scope drift;
- retries with newly minted IDs;
- two different intended effects accidentally sharing one ID;
- semantically equivalent but differently serialized parameters.

Question both under-binding and over-binding.

A mechanism that catches duplicates but false-BLOCKs harmless equivalent retries is not fully successful.

### B. Attempt semantics

Test whether an attempt can be mistaken for settlement through:

- tool/API return without durable provider commit;
- timeout after provider commit;
- local exception before/after remote effect;
- replay/resume after checkpoint;
- duplicate callback or delivery;
- stale attempt state after recovery.

### C. Receipt / settlement semantics

Test:

- fabricated/self-asserted receipt;
- stale receipt;
- receipt about a different target/effect;
- partial settlement;
- contradictory receipts;
- provider status that is eventually consistent;
- unknown settlement;
- receipt disappearance/revocation/correction;
- settlement that is externally real but not yet locally observed.

Do not require universal cryptographic authentication unless the problem actually requires it.

### D. Commitment ownership

Test:

- fork with two active owners;
- failover/lease expiry;
- owner disappearance;
- stale branch awakening;
- delegated execution;
- shared queue where logical ownership is external rather than Agent-local;
- read-only work where commitment machinery is unnecessary.

Ask whether `one active owner` is actually the right property for all effect classes or whether some effects are safely commutative/partitionable/parallelizable.

### E. Retry / wait / query / compensate / stop

For uncertain settlement, inspect whether the proposed next-action logic can distinguish:

- retry same intent safely;
- query provider/world state first;
- wait/backoff for evidence;
- compensate with a new effect;
- proceed forward after a pivot;
- narrow/escalate/manual reconcile;
- stop because the effect is already settled.

Look for both reckless retry and permanent elegant deferral.

### F. Recovery and fork

Test whether restore/fork can reanimate obsolete execution responsibility or stale world assumptions.

Positive controls must include legitimate recovery where retry is actually safe.

### G. Compensation / irreversibility

Test whether compensation:

- incorrectly erases occurrence truth;
- silently reuses original effect identity;
- assumes full world rollback;
- lacks its own retry/settlement semantics;
- is demanded for effects that are intrinsically irreversible or where forward repair is correct.

### H. Governance rent

Ask which parts of the prototype are too heavy for:

- read-only operations;
- local computation;
- intrinsically repeatable effects;
- providers with native idempotency;
- transactional workflow engines that already represent intent/attempt/receipt internally.

A Host-native organ can satisfy the property without copying ENA's exact object names.

## Mandatory retention analysis

For every proposed deletion/merge/demotion, answer:

1. What concrete failure did the mechanism prevent?
2. If removed, what exact replacement preserves that function?
3. Can a fresh implementer discover the replacement from ENA guidance without reinventing the deleted mechanism?
4. What evidence establishes function parity?
5. Does the simplification create a new false-BLOCK or implementation ambiguity?

If function parity is unproven, use:

`PRESERVE_PENDING_REPLACEMENT_EVIDENCE`

not:

`REMOVE_AS_ALREADY_COVERED`.

## Allowed dispositions

For each mechanism / field / rule:

```text
KEEP
REPAIR
SPECIALIZE
KEEP_AS_REFERENCE_ORGAN
KEEP_AS_HOST_PATTERN
REPLACE_WITH_EQUIVALENT_HOW
COEXIST
PRESERVE_PENDING_REPLACEMENT_EVIDENCE
RETIRE_AFTER_USEFULNESS_FAILURE
```

Do not use `PASS/FAIL` as the only final result.

## Required review output

### 1. Independent semantic model

Explain, in the reviewer's own words, what must survive timeout/retry/recovery/fork for consequential work to remain truthful.

### 2. Material failure findings

For each finding:

```text
ID
OBSERVATION
WHY IT MATTERS
FALSE-CLAIM or FALSE-BLOCK path
CHEAPEST COUNTEREXAMPLE / FIXTURE
CURRENT PROTOTYPE COVERAGE
REPAIR OPTIONS
```

### 3. Mechanism retention findings

For each retained mechanism:

```text
MECHANISM
PRACTICAL FAILURE IT PREVENTS
WHY A PURE ABSTRACT PROPERTY IS NOT ENOUGH
CHEAPER EQUIVALENT IF KNOWN
HOSTS WHERE IT MAY BE DORMANT/OPTIONAL
RETENTION DISPOSITION
```

### 4. Simplification proposals

Only propose simplification with explicit function-parity analysis.

### 5. Missing HOWs

Identify concrete places where the prototype states a property but still leaves the implementer without an operational route.

### 6. Final selection verdict

Use a composition such as:

```text
REFERENCE_ORGAN_VALUE = STRONG | PLAUSIBLE | WEAK | NOT_DEMONSTRATED
MATERIAL_DEFECTS = ...
FALSE_BLOCK_RISK = ...
RETENTION = ...
REPAIR = ...
SPECIALIZATION = ...
REPLACEMENT = ...
RETIREMENT = ...
HOST_MAPPING_NEXT = YES | NO
NEW_ENA_SEMANTIC_RULE_NEEDED = YES | NO | UNPROVEN
CURRENT_CHANGE = NO   # unless separately authorized; review cannot mutate Current
```

## Stop rule

Do not iterate the schema merely because more edge cases can be imagined.

Continue architecture iteration only when the review reveals a **new shared mechanism** or a material false-confidence/false-BLOCK path that cannot be handled economically by existing properties.

Conversely, do not terminate a useful reference organ merely because its semantic principle already exists in Current.

`SEMANTIC_REDUNDANCY != IMPLEMENTATION_REDUNDANCY`

`SMALLER_ONTOLOGY != AUTOMATICALLY_BETTER_ARCHITECTURE`
