# Effect Lifecycle reference prototype

Status: `RESEARCH_PROTOTYPE / NOT_CURRENT / NOT_RELEASE_CANDIDATE`

Related: #91 Reconstruction B, #89, PR #82.

## WHAT

Represent consequential external work without collapsing four different subjects:

```text
INTENT       = the one world change meant
ATTEMPT      = one execution incarnation
RECEIPT      = evidence about what the external world accepted/committed
COMMITMENT   = why work is still owed and who currently owns execution responsibility
```

## WHY

Without this separation, restart/retry/fork/failover can create familiar false claims and duplicate effects:

```text
timeout -> new action -> duplicate effect
restore local pending state -> replay -> world had already committed
fork memory -> both branches think they own execution
local rollback -> narrate external consequence as reversed
```

## HOW — this prototype

- `effect-lifecycle.v0.1.json` — small research contract/vocabulary and decision rules;
- `fixtures/effect-lifecycle-cases.jsonl` — deterministic positive/negative cases;
- `tools/validate_effect_lifecycle.py` — stdlib validator/evaluator;
- `tools/selftest_effect_lifecycle.py` — portable regression selftest.

The prototype intentionally does **not** promise universal exactly-once execution.

A Host may map the same property to:

- native idempotency key;
- transactional queue/workflow identity;
- provider status/receipt query;
- compensating action;
- manual/external settlement;
- `UNKNOWN + WAIT/NARROW/ESCALATE` when the external world cannot be resolved safely.

## Core reference properties

1. Retrying the same intended effect keeps one `effect_id`; it does not silently mint a new intent.
2. One `effect_id` remains bound to materially equivalent operation parameters/scope.
3. `attempt outcome` is not `external settlement` unless the Host evidence actually establishes it.
4. Known external `COMMITTED` state must not be overwritten by restored/local `PENDING` memory.
5. A compensation is a **new effect** linked to the original occurrence; it is not time reversal.
6. Fork/restart may copy knowledge of a commitment but does not automatically copy executor ownership.
7. A commitment cannot be called `SETTLED` without settlement evidence appropriate to the Host.
8. Read-only or intrinsically repeatable operations do not need idempotency ceremony merely to satisfy the vocabulary.
9. `UNKNOWN` is an allowed settlement state; false completion is worse than honest unresolved state.

## Evidence boundary

The external patterns motivating this prototype are mature (idempotency, durable workflow replay, Saga/compensation, callback wait), but the ENA composition is still a research organ.

`STRUCTURAL_FIXTURE_PASS != EXTERNAL_EXACTLY_ONCE`

`RECEIPT_REPRESENTED != RECEIPT_EXTERNALLY_TRUE`

`LOCAL_RECOVERY != WORLD_ROLLBACK`

`CURRENT_CHANGE = NO`
