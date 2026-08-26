# HOW-D — CRDT-style merge for declared commutative state

Status: `REFERENCE_HOW / RESEARCH_ONLY`

## Host fit

Use this HOW only when the state class has a mathematically defined merge/join where concurrent updates can converge without semantic negotiation.

Good candidates include:

- grow-only or observed-remove sets;
- counters;
- replicated maps whose leaf values have declared CRDT semantics;
- presence/seen markers;
- bounded metadata where concurrent union is genuinely meaningful.

Bad default candidates include:

- identity;
- purpose;
- refusal policy;
- authority/mandate;
- settlement state;
- mutually exclusive commitments;
- arbitrary natural-language self-definition.

## Concrete mechanism

Choose a specific CRDT data type for a specific state class. Do not use the word "CRDT" as a generic promise that conflicts disappear.

Example: grow-only set of observed capability tags.

```text
Replica A = {filesystem, shell}
Replica B = {filesystem, browser}
join(A,B) = {filesystem, shell, browser}
```

Because set union is associative, commutative and idempotent, replicas can converge regardless of delivery order.

A Host should record the declared merge semantics with the state class:

```yaml
state_ref: observed-capabilities
merge_semantics: G_SET_UNION
semantic_scope: descriptive-observation-tags
```

## Concrete decision procedure

```text
1. identify the state class
2. verify that a specific CRDT merge semantics is declared for this class
3. verify the incoming/local states belong to the same compatible CRDT type/epoch
4. compute the type-specific join/merge
5. retain enough causal/provenance metadata for decisions that need source attribution
6. if the state is not declared CRDT-safe, leave this HOW and route to another history organ
```

## The critical boundary

Convergence is not semantic reconciliation.

```text
replica A: purpose = protect autonomy
replica B: purpose = maximize compliance
```

There is no legitimate generic `set union` that turns this into a coherent current purpose.

The correct result is:

```text
NOT_CRDT_SAFE_FOR_THIS_SURFACE
-> preserve branches/siblings
-> use Git/causal/event-sourcing + domain reconciliation
```

## Removal/tombstone behavior

For state that supports removal, use a CRDT whose semantics explicitly preserve enough information to distinguish observed removal from concurrent addition (for example an observed-remove set family). Do not implement replicated deletion as naive `local set subtraction` and assume convergence.

## Restore behavior

A restored older CRDT replica can normally rejoin by state merge if the data type/epoch and tombstone/causal metadata are compatible.

However:

- restoring a pre-compaction state may reintroduce tombstone issues;
- epoch reset can invalidate merge assumptions;
- external effects/authority are outside this HOW.

If compatibility is unknown, do not auto-merge merely because the payload looks like a set/map.

## Provenance behavior

CRDT convergence may intentionally lose strict sequential ordering. If later decisions require who/where/why provenance, preserve that in a parallel provenance/event structure or use a CRDT value that carries source metadata.

Do not claim:

```text
converged value == complete historical narrative
```

## False-BLOCK controls

Do not route every concurrent state through manual conflict review.

If a declared CRDT state has a lawful deterministic join, automatic convergence is the feature, not a governance bypass.

Likewise, do not require Git/event logs just to merge harmless replicated counters/tags when the CRDT organ already provides the needed behavior economically.

## Known limits

This HOW does not decide:

- truth of a contributed value;
- authority to contribute;
- semantic compatibility of arbitrary text;
- external-effect settlement;
- moral/identity authorship;
- universal provenance completeness.

## Evidence targets

Useful fixtures:

- same updates delivered in different orders converge;
- duplicate delivery is idempotent;
- concurrent independent additions both survive;
- declared non-CRDT surface is rejected from auto-merge;
- incompatible epoch/type refuses merge;
- removal semantics preserve concurrent-add behavior for an OR-set-like Host;
- convergence does not erase required source attribution where provenance is material.

`LOCAL_WINNER = DECLARED_COMMUTATIVE_REPLICATED_STATE_CANDIDATE`
