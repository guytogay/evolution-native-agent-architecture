# HOW-B — Causal context / sibling preservation

Status: `REFERENCE_HOW / RESEARCH_ONLY`

## Host fit

Use this HOW when state is replicated across nodes/Agents, may be edited offline, and wall-clock ordering is too weak to distinguish stale state from genuinely concurrent work.

Typical surfaces:

- replicated memory/object stores;
- multi-Agent shared state;
- offline mobile/edge Agents;
- distributed preference/configuration objects;
- replicated working sets where per-object causal metadata is affordable.

## Concrete mechanism

Attach causal context to each version. A Host may use vector clocks, dotted version vectors, Lamport-style metadata plus explicit branch IDs, or another causality-preserving representation.

Illustrative vector:

```text
V1 = {A: 4, B: 2}
V2 = {A: 5, B: 2}
V3 = {A: 4, B: 3}
```

Comparison rule:

```text
X dominates Y
  iff every component of X >= Y
  and at least one component is >

X == Y
  iff all represented components are equal

X concurrent Y
  iff neither dominates the other
```

For the example:

```text
V2 descends from V1
V3 descends from V1
V2 and V3 are concurrent siblings
```

## Concrete decision procedure

```text
1. read local version + causal context
2. read incoming version + causal context
3. compare causality
4. if equivalent -> dedupe/reference same logical frontier
5. if local dominates incoming -> incoming is stale/ancestor; retain if useful, do not overwrite
6. if incoming dominates local -> advance frontier
7. if concurrent -> preserve both siblings
8. invoke domain reconciliation only when the state class permits/needs it
9. if reconciliation creates a new version, its causal context must dominate/include both input frontiers
```

## Why sibling preservation matters

Concurrent values are not evidence that one is wrong. They mean the available causal metadata cannot order them as ancestor/descendant.

For material state:

```text
sibling A = learned durable heuristic from Host A
sibling B = learned durable heuristic from Host B
```

Possible dispositions include:

- keep both dormant;
- select one locally;
- merge them with a domain-specific operation;
- create a third reconciled version;
- keep disagreement explicit.

The causal organ must not silently choose a winner based only on arrival order.

## Restore behavior

A restored snapshot with an older causal context is detectable as an ancestor if current context is known.

```text
current = {A:8, B:5}
restored = {A:6, B:5}
-> restored is stale ancestor
```

This prevents `restore happened now` from becoming `restore is latest`.

## Unknown/partial causal context

If causal metadata is missing or from an incompatible epoch/namespace, the correct relation may be `UNKNOWN`.

Do not map `UNKNOWN` to `CONCURRENT` or `LATEST` automatically. A Host may:

- fetch more context;
- isolate the incoming branch;
- require manual reconciliation;
- retain both values with an uncertainty marker.

## False-BLOCK controls

Do not require full vector clocks for every Host.

Alternatives include:

- per-object dotted vectors;
- branch/epoch + monotonic local counters;
- database revision tokens that already expose causal/optimistic-concurrency semantics;
- native store siblings/version stamps.

The property is causal distinguishability, not one metadata format.

## Known limits

Causal context does not decide:

- which sibling is semantically preferable;
- whether a self-change is legitimately authored;
- whether an external side effect committed;
- whether sibling values are safe to combine;
- whether one Agent currently has execution authority.

## Evidence targets

Useful fixtures:

- descendant advance;
- stale ancestor rejection;
- true concurrent siblings;
- concurrent siblings reconciled into a descendant of both;
- missing causal context -> UNKNOWN;
- later wall-clock timestamp but stale causal state;
- sibling preservation across restart/replication.

`LOCAL_WINNER = REPLICATED_CAUSAL_STATE_CANDIDATE`
