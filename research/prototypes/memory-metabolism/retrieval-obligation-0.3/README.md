# Retrieval Obligation 0.3 — Latest Discovery and Retrieval Sufficiency

Status: `RESEARCH_PROTOTYPE / NOT_CURRENT_BASELINE / NOT_AUTHORITY / NOT_RELEASE_CANDIDATE`

## Why 0.3 exists

0.2 separated:

`R0 trigger -> retrieval intent -> cold scope discovery -> targeted retrieval`

and correctly distinguished:

`scope-discovery completeness != in-scope retrieval completeness`.

Static falsification then exposed two additional false-confidence paths.

### F1 — an older discovery could close over newer represented reality

The validator did not require a closure to bind the latest represented discovery.

Reachable trace:

`discovery 1: NO_RELEVANT_SCOPE / complete`
-> `discovery 2: scope found / HIT`
-> closure cites discovery 1
-> `NO_HIT_BOUNDED`
-> decision `READY`.

The later discovery is represented but can be ignored.

Refinement:

> **A closure must bind the latest represented scope-discovery sequence for that obligation.**

Discovery sequence numbers are therefore unique within an obligation.

This does not claim wall-clock truth. It prevents the contract from preferring an older represented discovery while a newer one is already present in the same lifecycle.

### F2 — one HIT could masquerade as sufficient retrieval

0.2 allowed:

`scope discovery = PARTIAL`
-> `retrieval attempt = HIT / PARTIAL`
-> closure = RETRIEVAL_USED
-> decision = READY.

That conflates:

`retrieved something != retrieved enough`.

A relevant memory may have been found while another decision-material memory remains omitted.

Refinement:

> **A HIT is retrieval evidence, not retrieval-sufficiency evidence.**

0.3 removes `RETRIEVAL_USED` as a READY-satisfying closure.

To close a represented obligation for `READY` using a HIT, 0.3 requires:

`RETRIEVAL_SUFFICIENCY_RESOLVED`

plus:

- a HIT basis attempt;
- an external `sufficiency_resolution_ref`.

The validator does not prove that external resolution is truthful. The point is narrower: semantic sufficiency must no longer be minted automatically from retrieval activity.

## NO_HIT_BOUNDED remains stricter than a local no-hit

A bounded no-hit still requires:

1. latest represented discovery;
2. `DECLARED_DISCOVERY_COMPLETE`;
3. either `NO_RELEVANT_SCOPE`, or every selected scope covered by `NO_HIT + DECLARED_SCOPE_COMPLETE`;
4. all represented attempts from the basis discovery accounted for;
5. no represented HIT hidden from the closure.

Therefore:

`searched one selected scope completely != bounded memory no-hit`

and:

`ignored a HIT != no-hit`.

## Deliberate trust boundary

0.3 still intentionally cannot prove:

- whether R0 should have fired;
- whether the decision context sent to the resolver was semantically sufficient;
- whether a registry snapshot is current;
- whether `DECLARED_DISCOVERY_COMPLETE` is true;
- whether all relevant scopes were discovered;
- whether resolver recall is real;
- whether an external sufficiency resolution is correct.

Those remain behavioral/Host/evaluation evidence questions.

A `sufficiency_resolution_ref` is not a magical truth token. It is only a representation boundary separating:

`HIT observed`

from:

`sufficiency externally resolved`.

## Residuals retained rather than over-engineered

### Stale registry

A stale `registry_snapshot_ref` can still structurally pass.

This is deliberate for now. The schema can record which resolver state was used, but it cannot infer whether that state was fresh enough for the current decision.

Evaluation class:

`STALE_REGISTRY_BASIS`.

### Scope-discovery false negative

A resolver can still claim:

`NO_RELEVANT_SCOPE + DECLARED_DISCOVERY_COMPLETE`

while a relevant cold domain actually exists.

The runtime contract cannot disprove this without an oracle.

Evaluation class:

`SCOPE_DISCOVERY_FALSE_NEGATIVE`.

### Search-All degeneration

The schema does not prohibit selecting many scopes.

That is not a structural truth violation by itself. It becomes a viability problem when retrieval cost/context/latency approaches Always-Search-All.

Evaluation class:

`SCOPE_EXPANSION_COST`.

## Current reference sequence

`decision`
-> `R0 trigger`
-> `retrieval intent`
-> `obligation`
-> `scope discovery 1..N`
-> `latest represented discovery`
-> `retrieval attempts`
-> either:
   - `NO_HIT_BOUNDED`, or
   - `RETRIEVAL_SUFFICIENCY_RESOLVED`, or
   - uncertainty/narrow/abstain
-> decision.

## Main research result so far

The unknown-known problem has now separated into at least three independent questions:

1. **Invocation** — did the Agent realize it should ask its past?
2. **Scope discovery** — did the resolver look in the right places?
3. **Retrieval sufficiency** — did finding something actually provide enough durable context for the decision?

These must not be collapsed.

## Next evidence target

Do not return to more R0 CALL/SKIP classification.

The next useful evidence should attack resolver-side scope discovery and expansion:

- stale registry versus current registry;
- non-obvious adjacent domain discovery;
- first-scope no-hit followed by bounded expansion;
- stopping before Search-All;
- whether a single generic resolver becomes a single point of blindness.

No Current/release change is proposed.
