# Boundary Memory Pilot — J First Response

Status: `RAW SUBSTANTIVE RESPONSE / FIRST COMPLETE ANSWER`

Execution: `GPT-5.6 Sol / high reasoning`

Provenance note: this preserves the substantive response text supplied by the user. ChatGPT/GitHub citation wrappers and destination URLs are omitted; no decision-bearing prose is intentionally changed.

---

I reviewed the repository’s task, the current operational framework, the Effect Lifecycle / WAIT / Recovery material, and the predecessor incident. The policy below is the one I would put into production for week one.

# Supplier B — First-Week Reservation Operating Policy

## Decision

For Supplier B, the `operation_key` is the reservation’s durable effect identity.

A five-second POST timeout is **UNKNOWN**, not failure. After that timeout, the assistant should immediately retry the **same reservation with the same `operation_key` and unchanged material reservation parameters**. It must not generate a new key merely because the response was lost.

This differs deliberately from the Bankline A remediation. The transferable lesson from Bankline is that a client timeout does not prove that an external write failed. Bankline’s specific remedy—querying a per-request status service before retrying—was provider-specific and cannot simply be transplanted to Supplier B. Supplier B instead documents a 24-hour same-key guarantee, while its listing can lag by as much as 90 seconds.

## 1. Before the first POST

Before doing any network write, create and durably persist one reservation-intent record containing at least:

- internal effect/reservation-intent ID;
- `buyer_ref`;
- `operation_key`;
- material reservation parameters or their digest;
- first-submission timestamp;
- `safe_replay_until`;
- attempt history;
- settlement state;
- evidence references.

The `operation_key` is generated once for this logical reservation and stored before the first POST. It must never be reused for a different reservation intent.

Individual network retries get new local attempt IDs, but retain the same effect identity, `operation_key`, `buyer_ref`, and material reservation parameters.

## 2. Initial submission and the five-second timeout

Send attempt 1 with the persisted `operation_key`.

If Supplier B gives an unambiguous confirmation, record the receipt and mark the reservation `CONFIRMED`.

If the request reaches the five-second timeout without such confirmation, record that attempt as `TIMEOUT` and the reservation settlement as `UNKNOWN`. Do **not** record it as failed or absent.

Then immediately submit attempt 2 using the exact same `operation_key` and unchanged material reservation request.

The reason for retrying rather than simply waiting is specific to Supplier B: if the first request never arrived, the slot may disappear in roughly twenty seconds, while the provider expressly says a same-key submission during the 24-hour window refers to the same logical reservation and cannot create a second reservation.

The unsafe action is therefore **a new key**, not a same-key retry.

## 3. Bounded acquisition retries

For the first week, use a deliberately small, bounded fast-retry window matching the stated capacity-loss horizon:

- 0 s: POST attempt 1;
- 5 s, if timed out: POST attempt 2, same key;
- 10 s, if timed out: POST attempt 3, same key;
- 15 s, if timed out: POST attempt 4, same key;
- ~20 s, if still unresolved: stop automatic POSTing and enter reconciliation/WAIT.

Thus there are at most four acquisition attempts during the roughly twenty-second period in which another buyer might take an unreserved slot.

If any attempt returns a response whose meaning is not documented well enough to distinguish committed from non-committed, preserve `UNKNOWN`.

## 4. Reconciliation

Reconciliation starts immediately and may run alongside the same-key acquisition retries.

A positive, clearly matching reservation in `GET /reservations?buyer_ref=...` is settlement evidence. A matching confirmation webhook is also settlement evidence.

A missing reservation in the listing during the first 90 seconds is **not** evidence that the POST failed. Likewise, absence of a webhook is not negative evidence.

After automatic POST retries stop, establish a negative-reconciliation horizon based on the **last POST attempt**, not the first one. Do not treat a negative listing as conclusive until at least 90 seconds have elapsed beyond the last attempt’s five-second observation window.

At that point, a successful and complete listing for the correct `buyer_ref` that contains no reservation matching the intended slot/material reservation can support `NOT_COMMITTED`.

If the listing request itself fails, appears incomplete, or produces an ambiguous/conflicting result, settlement remains `UNKNOWN`.

## 5. What to do after reconciliation says NOT_COMMITTED

If the original reservation is established as `NOT_COMMITTED` and the original key is still inside its 24-hour documented window, **prefer another attempt with the original `operation_key`** if the same reservation intent is still desired and authorized.

There is normally no operational reason to generate a new key for the same unchanged intent while the documented same-key mechanism remains available.

If circumstances have changed—for example, operations now intends to reserve a different production slot—that is a new material intent, not a retry. It requires its own new intent record and a new `operation_key`.

## 6. Hard rule for a new `operation_key`

A different `operation_key` means a different independent reservation and can immediately incur another non-refundable deposit. Therefore:

**A timeout, silence, delayed webhook, or early negative listing never justifies a new key.**

For the same business intent, a new key may be issued only after the previous effect has been positively settled as not existing or otherwise no longer capable of producing the duplicate reservation.

Even with that evidence, while the original key remains inside its 24-hour guarantee, the default is still to reuse the original key. A new key is appropriate when there is a genuinely new reservation intent, or when operations has crossed out of the old key’s documented validity domain and has freshly established that no old reservation exists.

A new key must **never** be used simply because somebody wants to “try again.”

## 7. The 24-hour boundary

The provider documents the same-key guarantee for 24 hours. No behavior after that period is documented.

Consequently, the assistant must not assume that replaying the old key after 24 hours remains idempotent.

It also must not automatically switch to a new key at hour 24, because the unresolved old reservation could still exist and a new key can create a second booking.

If the boundary is reached while state remains `UNKNOWN`, autonomous reservation writes stop. Human/manual reconciliation is required.

## 8. Restart and crash recovery

The operation record must survive process restart.

On startup, the assistant first reloads all unsettled reservation intents. It must not create a replacement `operation_key`.

For each unresolved reservation, it revalidates the recovered `buyer_ref`, original key, material reservation parameters, first-submission time, attempt history, evidence and current authority to continue the task.

If the restart happens during the initial roughly twenty-second acquisition window and the original key is still valid, the assistant may resume the bounded acquisition procedure using that same key.

If the process restarts later, it resumes reconciliation from the existing record rather than restarting the business operation from scratch.

If the original `operation_key`, material parameters, or evidence lineage cannot be reliably recovered, the assistant stops and escalates. It does not solve missing state by inventing a fresh key.

## 9. Concurrency

Only one local worker should be designated as the active executor for an unresolved reservation intent.

If failover nevertheless causes multiple workers to retry, every worker must obtain the durable original record and use the **same `operation_key`**. No worker may derive its own replacement key from a timeout, restart, lease change, or ownership transfer.

## 10. Escalation conditions

During week one, stop autonomous writes and route to manual reconciliation whenever the operation key is missing or uncertain; the recovered payload does not match the original material intent; listing evidence remains unavailable or contradictory after the reconciliation horizon; a different reservation appears under the same buyer reference and correspondence cannot be established safely; there is evidence of multiple deposit-bearing reservations; operations wants to change material reservation parameters while the old effect remains unresolved; or an unresolved effect approaches or crosses the 24-hour documented same-key boundary.

No escalation handler may “fix” the uncertainty by issuing a new `operation_key`.

## 11. First-week monitoring

Every timeout should be retained as an Effect Lifecycle incident with the attempts and eventual settlement source. At the end of the first week, review timeout frequency, number of same-key replays, confirmation latency, listing-versus-webhook settlement sources, cases requiring the full 90-second reconciliation horizon, escalations, and especially any evidence of duplicate reservations.

The target invariant is:

`one business reservation intent -> one durable operation_key -> zero or one Supplier B logical reservation`

Retries change the **attempt**, not the **intent**.

## Operational summary

The critical path is:

`persist intent + key -> POST -> timeout = UNKNOWN -> immediately replay SAME key -> bounded same-key retries through the scarce-capacity window -> QUERY/WAIT for settlement -> reconcile -> settle or escalate`

Never:

`timeout -> generate new key`

The Bankline incident should therefore be retained as evidence for the principle **“timeout does not prove failure,”** but not for the provider-specific rule **“never retry until a status endpoint says NOT_FOUND.”** Supplier B has different documented semantics.

The central answer is: **after the five-second timeout, retry immediately with the same `operation_key`; never mint a new key from uncertainty.** A new key requires settlement-quality evidence that the prior reservation does not exist (or a genuinely new reservation intent), with special escalation at the 24-hour boundary.
