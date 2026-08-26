# Triggered Retrieval Obligation — research prototype 0.1

Status: `RESEARCH_PROTOTYPE / NOT_CURRENT_BASELINE / NOT_AUTHORITY / NOT_RELEASE_CANDIDATE`

Related: Issue #73, PR #82.

## Research question

How can a bounded Agent reduce unknown-known failures without keeping one always-hot cue per durable memory?

Candidate answer:

> **Keep the invocation condition hot, not the memory catalog.**

A small R0 reflex may trigger one generic Memory Resolver. The resolver may internally use registries, graphs, vector search, SQL, files, tools, or other Host-fit organs while the active decision surface remains bounded.

Reference flow:

`decision -> R0 trigger -> retrieval obligation -> resolver attempt -> bounded closure -> decision`

## Pre-commit falsification log

The first local sketch was deliberately attacked before publication.

### F1 — runtime `retrieval_risk` was false confidence

The sketch let the runtime label a decision `NONE | POSSIBLE | MATERIAL | UNKNOWN` and used that label to require retrieval.

But an unknown-known failure can simply manifest as the runtime incorrectly claiming `NONE`.

That means the schema would appear to check the central problem while actually trusting the actor that may have forgotten.

Refinement:

> **Runtime validation begins after a trigger exists. Whether a trigger should have fired is evaluation evidence, not runtime self-attestation.**

### F2 — `NO_HIT_BOUNDED` had no represented scope

A no-hit claim without a query/coverage scope is not meaningfully bounded.

Refinement:

Each obligation and attempt carries an opaque `query_scope_ref`; `DECLARED_SCOPE_COMPLETE` means only complete for that represented resolver scope. The validator does not prove the scope itself is adequate or truthful.

### F3 — unresolved low-risk retrieval could still be called `READY`

Continuing low-consequence work can be legitimate, but it must not narrate failed retrieval as completed retrieval.

Refinement:

`READY` requires every represented retrieval obligation for the decision to be closed by `RETRIEVAL_USED` or `NO_HIT_BOUNDED`.

Low-consequence continuation after incomplete retrieval uses explicit `PROCEED_UNCERTAIN` + `UNCERTAIN_CONTINUATION` instead.

### F4 — closure needed a specific attempt basis

With retries, one failed attempt and one successful attempt can coexist. A closure must identify which attempt supports the closure claim.

Refinement:

Every closure binds to `basis_attempt_id` within the same obligation.

## Runtime contract

The runtime contract intentionally starts **after** R0 has fired.

It can check:

- every represented trigger externalizes exactly one retrieval obligation;
- resolver and query-scope references stay bound through attempts;
- `HIT` cannot be empty and `NO_HIT` cannot return records;
- a closed obligation identifies a supporting attempt;
- `NO_HIT_BOUNDED` requires `NO_HIT + DECLARED_SCOPE_COMPLETE` on the basis attempt;
- `READY` cannot coexist with unresolved/failed retrieval semantics;
- non-material work may proceed with explicit uncertainty;
- material work may narrow or abstain rather than silently treating retrieval failure as success.

It cannot check:

- whether R0 should have fired;
- whether `query_scope_ref` was the right scope;
- whether the resolver really covered its declared scope;
- whether a returned memory is semantically relevant;
- whether all decision-material memory was found.

Those are external/behavioral questions.

## Evaluation plane

Unknown-known detection requires an evaluator/oracle outside the runtime Agent.

The evaluation trace distinguishes:

`TRIGGER_FALSE_NEGATIVE`
→ `RESOLVER_NOT_INVOKED`
→ `QUERY_SCOPE_MISS / QUERY_SCOPE_UNKNOWN`
→ `RESOLVER_FAILURE / RESOLVER_FALSE_NEGATIVE`
→ `PROJECTION_DROP`
→ `APPLICATION_FAILURE`
→ `SUCCESS`

This prevents one final task outcome from hiding where memory failed.

`oracle_relevant_record_ids` is test/field evidence only. It is not ordinary runtime state.

## Why this avoids a flat hot cue catalog

Nothing in the runtime schema enumerates durable memories or per-memory cues.

The always-hot part may be as small as a generic invocation reflex plus the ability to call one resolver.

Therefore the architecture does not require:

`N memories -> N hot cue entries`.

It does not prove every Host implementation is O(1), but it removes linear hot-catalog growth as a semantic requirement.

## Main unresolved questions

1. Can a generic R0 reflex achieve useful recall without firing on nearly every action?
2. Can query-scope selection become the new hidden unknown-known bottleneck? (The evaluation plane now treats this as a distinct failure stage.)
3. Can resolver registry/index staleness make `DECLARED_SCOPE_COMPLETE` dangerously confident?
4. How should false-positive trigger cost be measured against false-negative material omissions?
5. Can a resolver become a single point of retrieval blindness?
6. Which decision shapes create a material retrieval obligation without growing a topic-specific cue catalog?

These questions now justify behavioral/adversarial evaluation more than further schema elaboration.
