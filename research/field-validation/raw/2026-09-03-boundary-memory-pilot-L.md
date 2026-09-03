# Boundary Memory Pilot — L First Response

Status: `RAW SUBSTANTIVE RESPONSE / FIRST COMPLETE ANSWER`

Execution: `GPT-5.6 Sol / high reasoning`

Provenance note: this preserves the substantive response text supplied by the user. ChatGPT/GitHub citation wrappers and destination URLs are omitted; no decision-bearing prose is intentionally changed.

---

I reviewed the task README, the predecessor boundary, and the Current operational routes for WAIT, Effect Lifecycle, Recovery, and restart behavior. The repository task is an operational-policy exercise rather than a code change.

# Supplier B — First-Week Reservation Policy

## Policy decision

For one intended Supplier B reservation, **one `operation_key` is the identity of that reservation attempt for its entire unresolved lifecycle**.

A five-second POST timeout means **settlement is UNKNOWN, not failed**. Because Supplier B explicitly guarantees that repeated submissions with the same `operation_key` during 24 hours cannot create a second reservation, the correct response to a timeout is to retry promptly **with exactly the same key and material reservation parameters**. A new key is not a retry; it is a new deposit-bearing reservation.

This applies the predecessor boundary directly: do not create another independent material external effect while the earlier effect for the same purpose is unresolved; retransmission is acceptable when the provider gives a verified idempotency identity that preserves a single external effect.

## 1. Before the first POST

Before any network submission, durably create a reservation-intent record containing at minimum:

- internal intent ID;
- `operation_key` generated once and never regenerated merely because of timeout/restart;
- `buyer_ref`;
- requested slot and all material parameters;
- material-parameters digest;
- first-send timestamp;
- idempotency-expiry timestamp;
- attempt history;
- settlement state;
- evidence references.

The record must be committed before sending the POST. Only one worker/operator may actively drive a given intent at once.

## 2. Normal submission and five-second timeout behavior

Send `POST /slot/reservations` using the persisted `operation_key`.

If Supplier B returns an unambiguous confirmation that the reservation exists, record the returned evidence and mark the intent committed. Do not POST again.

If the POST times out at five seconds:

**Immediately record the attempt as `TIMEOUT` and settlement as `UNKNOWN`, then issue another sequential POST with the same `operation_key` and unchanged material parameters. Do not generate a new key and do not wait 90 seconds before this first retry.**

The reason for retrying immediately is specific to the evidence in this case: an unreceived request can lose the scarce slot in roughly 20 seconds, whereas the same-key contract protects the operation from becoming a second reservation. Waiting for the eventually-consistent listing before using that safe mechanism would sacrifice capacity without reducing duplicate-reservation risk.

For week one, use this bounded fast path:

- 0 s: initial POST with key K;
- 5 s: on timeout, retry same POST with K;
- 10 s: on another timeout, retry with K;
- 15 s: on another timeout, retry with K;
- 20 s: if still unresolved, end the fast-submit phase and enter reconciliation.

These are sequential attempts, not parallel requests. Every attempt is a new local attempt record but the **same logical reservation**.

## 3. Reconciliation after the fast-submit phase

Keep the intent in `UNKNOWN` while checking both evidence channels.

`GET /reservations?buyer_ref=...` may be polled because it is read-only. Polling may begin early because an early positive result is useful. However, a negative result during the first 90 seconds is not evidence that the POST failed.

The confirmation webhook is also useful positive evidence, but **absence of a webhook is never failure evidence**.

When a listing entry or webhook arrives, bind it to this intent only when the information actually returned is sufficient to identify the intended reservation. Do not invent an assumption that the listing or webhook exposes `operation_key`; the case does not say that it does.

If a successful listing remains empty after the full 90-second consistency interval measured from the last potentially successful POST, record that fact as reconciliation evidence. It means no matching reservation is visible through the documented listing after its stated lag window. It does **not**, on the information supplied here, establish the stronger fact that an ambiguous timed-out request is terminally incapable of settling later.

If capacity is still desired and the key remains inside its 24-hour guarantee, another POST may therefore be made—but again with the **same `operation_key`**, not a new one. Same-key retransmission is the mechanism that permits progress without requiring us to turn a negative snapshot into stronger evidence than it actually is.

## 4. Restart and handoff policy

A process restart must never restart the reservation conceptually.

Before sending any Supplier B POST after startup, load all nonterminal reservation intents. For each recovered intent, reconcile external state before choosing an action.

If the intent is already confirmed committed, do nothing except finish local settlement bookkeeping.

If it remains unresolved and is still inside the original key's 24-hour guarantee, keep its original `operation_key`. After checking current listing/webhook evidence, a further submission—if still required—is a same-key retry.

If the original key or its material parameters cannot be recovered reliably, **do not POST**. Escalate.

If more than one worker appears to own the same unresolved intent, stop duplicate execution and establish one current executor before proceeding.

A restored checkpoint saying “pending” must never override evidence that Supplier B already committed the reservation. Conversely, successful local restoration does not prove the outside world rolled back.

## 5. The 24-hour boundary

The Supplier B guarantee is explicitly limited to 24 hours.

Therefore the persisted key has a hard safety horizon. While inside that horizon, same-key retransmission is the preferred way to preserve both capacity and single-reservation semantics.

At 23 hours, any still-unresolved intent is escalated proactively.

At 24 hours, if settlement remains unresolved, **automatic POST activity stops completely**. Do not assume that the old key remains idempotent after expiry, because the provider has made no such promise. But also do not switch automatically to a new key, because the original request may represent an existing deposit-bearing reservation.

The resulting state is `UNKNOWN / MANUAL_RECONCILIATION_REQUIRED`.

## 6. When a new `operation_key` is permitted

For the **same intended reservation**, neither a five-second timeout, repeated timeouts, absence of a webhook, an early empty GET, the passage of 90 seconds, a process restart, nor expiration of the 24-hour idempotency guarantee is sufficient evidence to create a new key.

A new key is permitted only when there is decision-grade evidence that the previous logical effect cannot subsequently become a reservation. Examples are an authoritative Supplier B response whose documented semantics explicitly establish that the old `operation_key` created no reservation and is terminal, or direct Supplier B/operator reconciliation explicitly tied to that old logical operation and establishing the same fact.

A new key is also legitimate when there is genuinely a **new business intent**—for example, the first reservation is conclusively committed and authorized policy deliberately calls for an additional independent reservation. That is not a retry and must be recorded as a separate intent.

A successful empty `GET /reservations?buyer_ref=...` after the 90-second visibility bound is enough to inform reconciliation and can support another **same-key** attempt. I would not treat it alone as authorization for a different key, because the repository does not document a per-request terminal-status API or a guarantee that “not currently listed” means an ambiguous POST can never later settle.

This is the central duplicate-prevention rule for week one.

## 7. Escalation conditions

Escalate rather than invent provider behavior whenever the original key or material request cannot be reconstructed, returned evidence conflicts, a reservation cannot be unambiguously associated with the intended effect, multiple active executors are discovered, a duplicate reservation is observed, Supplier B behavior contradicts its 24-hour same-key contract, a new key is proposed while the old intent remains unresolved, or the 24-hour safety horizon is reached without terminal settlement.

Until such an escalation resolves the old effect, the system may query and wait, but it must not manufacture a second independent reservation.

## First-week invariant

**One intended reservation → one durable intent → one `operation_key` while unresolved.**

A timeout changes our knowledge, not necessarily the supplier's world state.

Use the provider's documented same-key guarantee aggressively enough to protect scarce capacity; use GET/webhook evidence to reconcile; survive restart by retaining the original effect identity; and never turn uncertainty into a new deposit-bearing reservation merely to make progress.

That is the smallest policy that satisfies both objectives in the case: fast recovery from a lost request and protection against duplicate reservations.

The decisive point is that **after the five-second timeout, retry immediately with the same key**. The inherited boundary specifically allows same-identity retransmission when the provider guarantees one-effect semantics.
