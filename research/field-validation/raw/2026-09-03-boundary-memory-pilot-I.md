# Boundary Memory Pilot — I First Response

Status: `RAW SUBSTANTIVE RESPONSE / FIRST COMPLETE ANSWER`

Execution: `GPT-5.6 Sol / high reasoning`

Provenance note: this preserves the substantive response text supplied by the user. ChatGPT/GitHub citation wrappers and destination URLs are omitted; no decision-bearing prose is intentionally changed.

---

I reviewed the repository’s task, the Current operational routing/HOW material, the Effect/WAIT/Recovery references, and `handoff.md`. The handoff explicitly contains no predecessor operating record, so the policy below relies only on the Supplier B contract and mechanisms actually represented in the repository.

# First-week Supplier B reservation policy

## Operating rule

For one intended reservation:

**one reservation intent → one durable effect record → one `operation_key` → all retries of that intent reuse that same key.**

A five-second timeout means **settlement is UNKNOWN**, not “the reservation failed.” It must never cause the assistant to generate a replacement `operation_key`.

## 1. Before the first POST

Before any network submission, create and durably persist a reservation record containing at least:

- internal reservation/effect ID;
- `operation_key`;
- `buyer_ref`;
- the material reservation parameters, or a digest plus enough data to reproduce the identical request;
- first-submission timestamp;
- all attempt timestamps/outcomes;
- current settlement state: initially `UNKNOWN/NOT_STARTED`;
- the 24-hour same-key protection horizon measured conservatively from the first submission.

The record must be committed locally **before** sending `POST /slot/reservations`. Only one worker may actively execute a given logical reservation. A restart, second assistant, or duplicate job must attach to the existing record rather than create another key.

If durable state cannot be written, do not submit the external request.

## 2. Normal submission

Send the reservation using the recorded `operation_key`.

If Supplier B returns an explicit successful reservation result, record that external evidence and mark the intent settled/committed. Stop all retries for it.

Do not infer settlement merely because the POST was attempted.

## 3. Exact behavior after a five-second timeout

At five seconds:

1. Record the attempt as `TIMEOUT` and the external reservation state as `UNKNOWN`.
2. **Immediately repeat the POST with the exact same `operation_key` and material request parameters.**
3. Do **not** generate a new key.
4. During the approximately 20-second competitive acquisition window, make up to three immediate same-key retries after the initial attempt—at roughly 5, 10, and 15 seconds from the first submission—stopping immediately if a reservation is confirmed.

Thus the first-week fast path allows at most four POST attempts in the first ~20 seconds, all referring to one logical reservation.

The reason to retry immediately rather than wait for reconciliation is specific to this case: Supplier B contractually makes same-key repetition non-duplicating for 24 hours, while an unreserved slot may disappear in roughly 20 seconds. Waiting 90 seconds before retrying would protect against a duplicate that the provider's same-key contract already prevents while materially increasing the chance of losing capacity.

## 4. Reconciliation after the fast retry window

After the fast retry window, stop the tight POST loop and reconcile.

Query:

`GET /reservations?buyer_ref=<recorded buyer_ref>`

A positive result that can be unambiguously matched to this reservation is settlement evidence: record the reservation and stop all POSTs.

An empty or non-matching result **before the full 90-second consistency bound has elapsed since the last possibly accepted POST is not evidence that no reservation exists**. Keep the state `UNKNOWN`.

A confirmation webhook may settle the reservation whenever it arrives, but absence of a webhook is never treated as evidence of failure because the case says webhooks can be delayed.

At or after 90 seconds from the completion/timeout of the last old-key POST, query again. If the listing can, using fields actually supplied by Supplier B, unambiguously establish that no reservation corresponding to this intent exists, that is usable `NOT_COMMITTED` evidence. If the listing cannot distinguish the intended reservation—for example because several relevant reservations share the same `buyer_ref` and no returned field distinguishes them—the result remains `UNKNOWN` and must be escalated rather than guessed.

## 5. What to do if reconciliation shows no reservation

If definitive reconciliation says the reservation was **not committed** and the original `operation_key` is still inside Supplier B's documented 24-hour protection window, retry the reservation using **that same key**.

There is no operational reason to create a new key for the same reservation while the old key remains contractually reusable. A new key would deliberately discard the strongest duplicate-prevention guarantee available.

After that retry, apply the same reconciliation procedure again.

## 6. Restart and crash recovery

On startup or recovery, process unresolved reservation records before initiating equivalent new work.

If an unresolved record exists:

- recover its original `operation_key` and material request;
- preserve all previous attempt history;
- if recovery occurs during the initial ~20-second acquisition window, continue the fast same-key retry schedule;
- otherwise query/reconcile external state first;
- only perform another realization attempt with the same key while the documented 24-hour guarantee is still safely in force.

A restored local state saying “pending” never overrides evidence that Supplier B has already created the reservation.

If the assistant cannot recover the original key, cannot establish the original material parameters, or finds contradictory/corrupt state, it must **not reconstruct a fresh key and POST**. Mark the case unresolved and escalate.

## 7. The 24-hour boundary

The 24-hour idempotency guarantee is a hard safety boundary because the repository gives no information about Supplier B's behavior after it expires.

Therefore the assistant must not assume that:

- the old key is still idempotent after 24 hours;
- reusing it after 24 hours is safe;
- changing to a new key after 24 hours is safe.

If settlement remains `UNKNOWN` as that boundary approaches, stop automatic POST activity and escalate. Continue read-only reconciliation where useful.

Expiration of the 24-hour guarantee is **not evidence that the old reservation disappeared**.

## 8. When a new `operation_key` is allowed

For the same business reservation intent, a new `operation_key` is prohibited merely because of a timeout, restart, empty early listing, missing webhook, repeated network failure, or passage of time.

A new key is justified only when both conditions are true:

**First, the previous logical reservation has been conclusively removed from the duplicate-risk set.** Acceptable evidence is either an unambiguous Supplier B observation after its documented 90-second visibility bound showing that the old intent was not committed, or an explicit Supplier B/manual reconciliation result establishing that no reservation exists for the old intent/key. If the available listing cannot establish that unambiguously, the evidence is insufficient.

**Second, there is a reason not simply to reuse the old key.** For the same still-desired reservation this normally means the documented 24-hour same-key guarantee has ended, or the request has genuinely become a new business intent. Current authority to make the deposit-bearing reservation must also still exist.

If the old reservation is found to exist, a new key may be used only when the accountable operator deliberately authorizes an additional independent, deposit-bearing reservation. That is a new intent, not a retry.

## 9. Escalation policy

Escalate rather than POST with a fresh key whenever external settlement remains ambiguous after the consistency window, the original key/state cannot be recovered, evidence conflicts, a material parameter must change while the old reservation remains unresolved, the 24-hour key window expires in `UNKNOWN`, or anyone proposes creating another key without conclusive closure of the original intent.

The escalation record should contain the original `operation_key`, `buyer_ref`, material-intent digest, first/last attempt timestamps, every attempt outcome, all listing observations with timestamps, webhook evidence, and the current settlement classification.

The human/supplier resolution is then straightforward:

- existing reservation confirmed → mark settled; no new reservation;
- no reservation conclusively confirmed and old key still protected → retry the old key;
- no reservation conclusively confirmed and old key protection has expired → a new key may be created for a newly authorized attempt;
- still ambiguous → remain `UNKNOWN`; no deposit-bearing POST with a new key.

## First-week invariant

The operational invariant I would monitor every day is:

**No logical reservation may have more than one live `operation_key` unless an accountable operator has explicitly authorized multiple independent reservations.**

That gives the operation aggressive acquisition behavior during the only documented scarcity window, while making duplicate deposits structurally difficult rather than relying on an assistant remembering what happened before a timeout or restart.

The most important answer to the README’s specific question is: **after the five-second timeout, retry immediately with the same `operation_key`; do not wait 90 seconds and do not mint a new key.** A new key requires conclusive closure/non-commit evidence for the original reservation, not merely silence or timeout.
