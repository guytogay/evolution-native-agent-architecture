# Retrieval Obligation 0.4 — Subject-Bound Sufficiency Resolution

Status: `RESEARCH_PROTOTYPE / NOT_CURRENT_BASELINE / NOT_AUTHORITY / NOT_RELEASE_CANDIDATE`

## Why 0.4 exists

0.3 fixed two structural false-confidence paths:

- closure could prefer an older discovery over newer represented discovery;
- a retrieval HIT could be treated as sufficient merely because something was found.

0.3 therefore introduced:

`RETRIEVAL_SUFFICIENCY_RESOLVED`

with an external:

`sufficiency_resolution_ref`.

A cross-prototype review then exposed a repeated failure pattern already seen during the Memory Security Waist work:

> **An external resolution reference that is not bound to the subject it resolved can be replayed after the subject changes.**

## Falsification

0.3 could represent:

`decision context v1`
→ `scope plan S1`
→ `attempt A1 returns memory M1`
→ `sufficiency_resolution_ref = R7`
→ `READY`.

Then mutate:

- decision context;
- selected scopes;
- returned memories;
- later retrieval attempts;
- decision consequence;

while retaining the same string:

`R7`.

The validator had no machine relation between R7 and the state R7 allegedly resolved.

Therefore:

`external resolution exists != external resolution applies to this current retrieval subject`.

## 0.4 refinement

0.4 introduces subject-bound sufficiency-resolution packets.

A Host/evaluator resolution packet contains:

- `resolution_ref`;
- `subject_fingerprint`;
- `receipt_ref`.

The subject fingerprint is computed over the represented retrieval subject:

- decision identity and consequence;
- retrieval intent identity;
- immutable/versioned `decision_context_snapshot_ref`;
- obligation identity and resolver;
- latest represented scope discovery;
- **all represented attempts from that latest discovery**.

Therefore changing any of those dimensions invalidates the old resolution packet.

Short form:

> **Resolution applies to a subject, not to a label.**

## Why all latest-discovery attempts are in the subject

A sufficiency resolution must not remain valid merely because its originally cited HIT still exists after new retrieval evidence arrives.

Example:

`A1 -> HIT M1`
→ sufficiency resolved
→ later `A2 -> HIT M2` or other new retrieval evidence.

If A2 is represented, the retrieval subject has changed.

0.4 therefore fingerprints all attempts under the latest discovery, not only closure-cited attempts.

This does **not** require every attempt to be semantically decisive. It only prevents later represented retrieval evidence from being invisible to an old sufficiency resolution.

## Decision-context snapshot

0.4 renames the reference-organ field to:

`decision_context_snapshot_ref`.

The Host should treat it as immutable/versioned for the retrieval lifecycle.

The validator cannot prove external immutability. The naming and subject-binding exist to prevent a mutable pointer from being silently treated as a stable retrieval subject.

## Trust boundary

0.4 still does not authenticate the external resolver/evaluator.

A malicious or broken Host could still issue a false resolution packet with the correct fingerprint.

The contract only checks:

> the represented external resolution is bound to the represented subject it claims to resolve.

It does not prove:

> the resolver was correct.

This is the same narrow distinction used elsewhere in ENA:

`represented binding != external-world truth`.

## Cross-prototype reuse, not a new ENA rule

The subject-binding lesson was already established during security-boundary review.

Retrieval 0.4 reuses that lesson rather than minting a retrieval-specific Constitution principle.

Current already distinguishes identities, effects, scopes, evidence, and applicability.

No new ENA rule/capability is proposed.

## Retained residuals

Still intentionally external/behavioral:

- R0 trigger false negatives;
- stale registry applicability;
- false-complete scope discovery;
- resolver recall;
- semantic correctness of sufficiency resolution;
- Search-All / scope-expansion cost.

## Focused deterministic result

Local focused regression before commit:

`RETRIEVAL_OBLIGATION_04_SUBJECT_BINDING_SELFTEST_PASS 15`

The focused cases include stale-resolution invalidation after:

- context change;
- new attempt;
- scope-plan change;
- consequence change;

plus resolution-packet existence/identity checks and retained external trust-boundary cases.

## Next review boundary

After this reconciliation, another independent reviewer can add epistemic value by attacking the **retrieval lifecycle as a whole**, especially:

- subject-binding gaps not covered by the current fingerprint;
- false-BLOCK created by requiring latest discovery;
- replay across decisions/obligations/Hosts;
- whether `RETRIEVAL_SUFFICIENCY_RESOLVED` is an honest narrow waist or merely Host magic;
- whether bounded scope expansion can terminate without Search-All.

Do not ask for another opinion on R0 CALL/SKIP behavior; that layer is already closed pending a new trigger mechanism.
