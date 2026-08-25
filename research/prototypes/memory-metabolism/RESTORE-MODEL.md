# Restore / Rollback Model — Why Local Memory Cannot Self-Attest Freshness

Status: `RESEARCH_PROTOTYPE / NOT_CURRENT_BASELINE / NOT_AUTHORITY`

Related: #73, PR #82.

## 1. Core result

A restored memory snapshot cannot determine, from the restored local state alone, whether it is the latest valid memory state.

This is not primarily an LLM weakness or retrieval-algorithm problem. It is an observability limit.

### Indistinguishable worlds

Assume snapshot `S0` contains local memory state:

`A = current belief / compiled state / known history`

Now consider two worlds.

### World W1 — no post-snapshot change

1. snapshot `S0` is taken;
2. no material memory/history change occurs;
3. process restarts from `S0`.

`S0` is current enough for its represented history.

### World W2 — post-snapshot learning occurred

1. snapshot `S0` is taken;
2. new evidence `E1` occurs;
3. new belief/compiled lesson `B1` supersedes or qualifies `A`;
4. the running process later fails;
5. recovery restores `S0`, erasing local visibility of `E1/B1`.

From the restored local state, W1 and W2 can be byte-identical.

Therefore no algorithm using **only the restored local snapshot** can reliably decide whether post-snapshot history existed.

> **Local restored memory cannot self-attest freshness.**

---

## 2. Why ordinary revalidation is not sufficient

Suppose `A` said:

`endpoint = 10.0.0.5`

After `S0`, W2 learned:

`endpoint = 10.0.0.9`

and compiled a lesson:

`always re-resolve endpoint before deployment because the endpoint changed unexpectedly`.

Later reality may happen to return to:

`endpoint = 10.0.0.5`.

A restored `S0` Agent can re-query the endpoint and confirm `10.0.0.5`.

That does **not** recover the missing post-snapshot experience or compiled lesson.

The current fact may match the old value while the Agent's developmental state is still stale.

Therefore:

`current-state revalidation != memory-continuity reconciliation`.

This is a different boundary from MM-P08/MM-P12.

---

## 3. Required property: a rollback-independent continuity/history anchor

Where continuity across restore is claimed and decision-material post-snapshot learning could matter, some evidence must survive outside the same rollback domain.

Candidate property:

> **Memory continuity claims across restore require a history/freshness anchor that is not erased by the same restore boundary.**

Possible organs include:

- append-only/WAL history stored outside the restored snapshot;
- Git/immutable commit lineage;
- remote state/history service;
- independent local partition/device/log;
- peer/human witness;
- signed monotonic receipt/head;
- server-authoritative world/history state;
- another recovery substrate with a distinct failure domain.

ENA should standardize the property, not one organ.

---

## 4. Minimal reconciliation pattern

Reference flow:

`RESTORE LOCAL SNAPSHOT`
→ `READ LOCAL HISTORY HEAD / EPOCH`
→ `READ INDEPENDENT CONTINUITY ANCHOR`
→ compare

If equal/compatible:

`CONTINUITY_RECONCILED`

If external/independent head is newer:

`LOCAL MEMORY STALE`
→ retrieve/replay/reconcile missing durable changes
→ establish a new current local state

If the anchor is unavailable:

`CONTINUITY_UNKNOWN`

Then use consequence-aware behavior:

- low-risk/read-only/evidence-seeking work may continue when missing history cannot plausibly change the decision;
- material actions depending on potentially changed authority, commitments, recovery, current state, or compiled learning should strengthen reconciliation or abstain;
- unavailable continuity evidence must not be narrated as proof that no post-snapshot history exists.

This preserves agency without treating uncertainty as safety.

---

## 5. Memory Continuity Contract

A useful restore contract can classify state into four categories.

### MUST_SURVIVE

State/history whose loss would make claimed continuity materially false or unsafe.

Examples may include:

- unresolved material commitments;
- current authority/revocation lineage where required;
- post-snapshot evidence that changed a durable high-impact heuristic;
- settlement/external-effect receipts needed to avoid duplicate action.

### MAY_RESTORE_AS_BELIEF

State that may be restored provisionally but is not assumed current.

Examples:

- mutable environment facts;
- cached endpoint/configuration;
- older project status.

### MUST_REVALIDATE

State that can be carried forward only after current reality or continuity reconciliation.

### MUST_NOT_RESTORE_AS_AUTHORITY

Historical grants, credentials, mandates, roles, or permissions that cannot regain current authority merely because an old snapshot contains them.

This extends:

`Retrieve -> Revalidate -> Act`

into:

`Restore -> Reconcile continuity -> Revalidate mutable reality -> Resolve current authority -> Act`.

---

## 6. What an external anchor does NOT prove

A matching head/digest can establish represented continuity of a particular history carrier.

It does not automatically prove:

- that every event was captured;
- external-world truth of each event;
- semantic correctness of compiled lessons;
- completeness of all memory stores;
- current authority;
- consciousness/identity sameness.

The anchor narrows one claim:

> the restored Agent is not silently reasoning from a known-older represented history state without acknowledging/reconciling the difference.

---

## 7. Relation to externalized continuity

This model also explains why an Agent can have weak internal memory but strong trajectory continuity when a persistent environment/server re-supplies current state.

The continuity-bearing unit may be:

`Agent local state + persistent external history/world + re-entry/reconciliation protocol`

rather than one giant self-contained memory file.

This supports the broader #73 result:

> **The unit of continuity may be the Agent-environment loop, not the Agent memory file.**

---

## 8. Deterministic falsification consequence

A test that restores an old local snapshot **without** an independent post-snapshot history source cannot prove correct restore continuity, no matter how many LLMs are run.

The meaningful question is structural:

> Is there a failure-domain-independent path by which the restored trajectory can discover that later durable history existed?

If the answer is no, the continuity claim is structurally under-supported.

No multi-model experiment is required to establish that information deficit.

> **Rollback can restore bytes. Only reconciliation can restore a trajectory's relationship to what happened after those bytes were written.**
