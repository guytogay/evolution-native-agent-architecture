# Retrieval Obligation 0.2 — Scope Discovery Boundary

Status: `RESEARCH_PROTOTYPE / NOT_CURRENT_BASELINE / NOT_AUTHORITY / NOT_RELEASE_CANDIDATE`

## Why 0.2 exists

Behavioral runs 001 and 002 support a narrow claim: a small generic R0 reflex can decide **when** durable memory retrieval is warranted without degenerating into Always-Retrieve or a topic-keyword catalog.

That exposes the next unknown-known failure:

> R0 fires correctly, but the system searches the wrong memory domain.

The 0.1 runtime schema attached `query_scope_ref` directly to the retrieval obligation. That quietly assumed the triggering Agent already knew which memory scope to search.

If the hot reflex must also retain a map from decision shapes to project memory domains, the architecture risks rebuilding the original hot-catalog scaling problem one level higher.

## 0.2 candidate

> **A retrieval obligation carries an intent; a resolver discovers scope.**

Reference flow:

`decision -> R0 trigger -> retrieval intent -> retrieval obligation -> cold scope discovery -> targeted retrieval -> bounded closure -> decision`

The hot/runtime intent contains no memory-domain list.

It carries only an opaque reference to the bounded current decision context and a generic reason why durable past state may matter.

The resolver then uses its own cold registry/catalog/index state to discover one or more candidate scopes.

## Two distinct completeness claims

A bounded NO_HIT now needs two different represented claims:

1. **Scope-discovery coverage** — did the resolver claim that its search for relevant scopes was complete for the represented discovery process?
2. **In-scope retrieval coverage** — for every selected scope, did retrieval complete without a hit?

Therefore:

`NO_HIT in selected scope != no relevant memory`

and

`complete retrieval inside wrong scope != complete memory check`.

The runtime validator can check that these claims are represented consistently. It cannot prove either claim is externally true.

## Why `registry_snapshot_ref` exists

Scope discovery depends on some resolver-side map/catalog/registry or equivalent mechanism.

That mechanism may change independently of the Agent.

A discovery receipt therefore records an opaque `registry_snapshot_ref` so a later audit can distinguish:

- the same query against changed registry state;
- a stale registry from a current one;
- a changed scope plan from a changed memory result.

ENA does not require a literal registry database. A Host may implement this through files, a graph, search service, SQL metadata, vector collections, tool routing, or another organ.

## Deliberate trust boundary

0.2 still cannot prove:

- that the decision context supplied to the resolver was semantically sufficient;
- that the resolver discovered every relevant store/domain;
- that `DECLARED_DISCOVERY_COMPLETE` is truthful;
- that a registry/catalog is fresh;
- that a selected scope is semantically relevant;
- that retrieval within a scope has real recall;
- that a returned memory is actually decision-material.

These remain evaluation/Host evidence questions.

The contract exists only to prevent a narrower false confidence:

> **Do not let in-scope search completeness silently stand in for scope-selection completeness.**

## Scaling hypothesis

The hot path need not grow as:

`N memories -> N cues`

or:

`N memory domains -> N hot routes`.

Instead it may remain approximately:

`generic trigger + generic resolver entry point + bounded current decision context`.

Cold resolver-side routing may scale with memory/store count without forcing the entire routing catalog into active Agent context.

This is an architectural possibility, not a proven complexity bound for every Host.

## Next falsification targets

1. Can scope discovery itself become a single point of blindness?
2. Can a stale registry make `DECLARED_DISCOVERY_COMPLETE` dangerously confident?
3. Does sending the whole current task context to a generic resolver create a new context-cost problem?
4. Can a resolver discover adjacent/non-obvious domains without a hot topic map?
5. What is the minimum escalation rule when the first scope plan returns no hit?
6. Can repeated scope expansion collapse into Always-Search-All?
7. Can one resolver entry point preserve organ neutrality across file/search/vector/graph/SQL Hosts?

## Behavioral next step

Do not run another R0 CALL/SKIP fixture unless a new trigger mechanism is hypothesized.

The next decision-changing experiment should hold R0=`CALL` fixed and compare competing scope-selection mechanisms, for example:

- `HOT_DOMAIN_SELECTION` — Agent chooses a domain before calling the resolver;
- `COLD_SCOPE_DISCOVERY` — Agent supplies generic retrieval intent and resolver chooses domains from cold registry/index state;
- `SEARCH_ALL` — high-cost upper-bound control.

The useful question is no longer "did the Agent remember to search?"

It is:

> **Can a generic resolver find the right place to search without moving the memory catalog back into hot state?**
