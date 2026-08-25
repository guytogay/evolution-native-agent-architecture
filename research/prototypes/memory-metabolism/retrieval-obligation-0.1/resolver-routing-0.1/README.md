# Resolver-Owned Routing — research prototype 0.1

Status: `RESEARCH_PROTOTYPE / NOT_CURRENT_BASELINE / NOT_AUTHORITY / NOT_RELEASE_CANDIDATE`

Parent: `retrieval-obligation-0.1`

## Problem

R0 can correctly decide that durable past state may matter and still fail by choosing the wrong memory domain.

If the always-hot Agent must carry one route/cue per durable memory domain, the architecture recreates the original scaling problem at the routing layer.

So the next candidate split is:

`R0 decides WHETHER to retrieve`

while

`Memory Resolver decides WHERE to retrieve using cold/external routing state`.

The Agent request therefore does not need a topic-specific store list.

Reference flow:

`decision -> R0 CALL -> generic resolver request -> cold registry/router -> searched scopes -> hits/no-hit -> decision projection`

## Key property

> **Keep retrieval invocation hot; keep routing knowledge cold.**

This does not eliminate unknown-known failure. It relocates one failure class into a place that can be externally evaluated and improved without inflating the Agent's hot state.

## Runtime/evaluation boundary

The runtime contract may represent:

- one generic resolver request bound to the triggering decision/obligation;
- resolver attempts;
- opaque scopes actually searched;
- whether the resolver claims its declared routed scope was fully searched;
- hit/no-hit/failure;
- bounded closure semantics.

It cannot prove:

- that the resolver chose the right scopes;
- that the registry was complete/current;
- that a declared scope corresponds to the evaluator's material scope;
- that the search algorithm recalled all relevant records.

Those remain evaluation/Host questions.

A deliberately wrong route can therefore be structurally honest at runtime and still receive:

`QUERY_SCOPE_MISS`

in the evaluation plane.

## Why `NO_HIT` stays bounded

`NO_HIT` means only:

> no hit in the represented scopes/search attempt.

It must never silently become:

> no relevant memory exists anywhere.

A no-hit closure may be treated as structurally complete only for the resolver's **declared routed coverage**, never as universal absence.

## Request shape

A generic request carries the decision context/purpose boundary, not a preselected domain catalog.

Reference fields may include:

- `request_id`
- `decision_id`
- `obligation_id`
- `resolver_ref`
- `decision_context_ref`
- `retrieval_purpose`
- `material_dimensions`

The exact transport is a reference organ.

## Receipt shape

A resolver attempt may return:

- opaque `searched_scope_refs`;
- `coverage = DECLARED_ROUTE_COMPLETE | PARTIAL | UNKNOWN`;
- `result = HIT | NO_HIT | FAILED`;
- returned record IDs when there is a hit.

The validator checks represented consistency only.

## Evaluation failure stages

After R0 success:

`ROUTING_NOT_ATTEMPTED`
→ `QUERY_SCOPE_MISS`
→ `QUERY_SCOPE_UNKNOWN`
→ `RESOLVER_FAILURE`
→ `RESOLVER_FALSE_NEGATIVE`
→ `PROJECTION_DROP`
→ `APPLICATION_FAILURE`
→ `SUCCESS`

This keeps routing failure distinct from search/index failure.

## Scaling claim boundary

This architecture removes any **semantic requirement** that the always-hot Agent enumerate all memory domains.

It does not prove that a Host's cold router/index scales well.

`hot O(1) intent -> cold O(N)/indexed routing` is allowed.

The point is to avoid requiring `N durable domains -> N hot Agent cues`.

## Next behavioral test

Test the resolver as a separate role with a cold domain registry.

The task set should contain only cases where R0 has already fired.

Measure:

- required-scope-group recall;
- critical scope misses;
- extra scope cost;
- number of scopes selected;
- cross-domain routes;
- whether no-hit is overclaimed.

Do not require one exact route when several scope choices can legitimately satisfy the information need.
