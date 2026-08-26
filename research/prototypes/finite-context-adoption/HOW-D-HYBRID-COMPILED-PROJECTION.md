# HOW-D — Hybrid compiled local projection

Status: `REFERENCE_HOW / RESEARCH_ONLY`

## Host fit

Best when the Host already maintains durable local projections, generated instruction surfaces, compiled memory, or task/domain-specific policy summaries and can refresh them from canonical sources.

Typical Hosts:

- mature long-lived Agents;
- Hosts with durable local state and compilation pipelines;
- Agents that need a stable resident subset but cannot afford monolithic hot loading;
- environments with repeated domain/task families where a compiled projection has reuse value.

## Concrete mechanism

Compile a bounded local ENA projection from canonical Current and Host-specific applicability.

Example layout:

```text
canonical Current
      |
      v
projection compiler
  inputs:
    exact Current identity
    Host capability profile
    frequently used decision families
    local applicability constraints
      |
      v
compiled local projection
  + source identity
  + generation identity
  + included semantic families/targets
  + declared omissions/limitations
  + refresh/invalidation trigger
      |
      +--> hot resident surface
      +--> canonical cold fallback for misses/ambiguity
```

## Runtime sequence

```text
fresh session
-> load compiled projection
-> decision shape matched inside projection -> use resident semantics
-> projection miss/uncertainty -> consult canonical cold source/router
-> if cold source contradicts projection -> canonical source wins for that dimension
-> schedule/perform projection regeneration
```

## Projection compiler behavior

The compiler may choose different ENA material for different Hosts. It must not silently turn selection into normativity.

For example:

```text
single local companion Agent
-> Commons/migration semantics may remain cold/dormant

multi-Agent workflow Host
-> composition/effect/authority semantics may be resident
```

`not resident != not part of Current`

and

`compiled into projection != universally applicable`

## Freshness/invalidation

At minimum the projection should bind:

- source Current identity;
- projection generation identity;
- material Host/runtime assumptions;
- explicit stale state when those assumptions change.

Invalidation can be triggered by:

- Current tree/version change;
- Host capability topology change;
- model/runtime change where material;
- projection compiler version change;
- observed retrieval miss showing the projection omitted a recurring material family.

## Failure behavior

If projection source identity is unknown or mismatched:

- mark projection `STALE/UNKNOWN_SOURCE`;
- use canonical cold source for material affected decisions when available;
- do not narrate the projection as complete Current.

If compiler fails, last known projection may remain historical/limited input; it must not gain stronger freshness merely because regeneration failed.

## What this HOW is good at

- bounded resident cost;
- stable Host-tailored semantics;
- lower retrieval frequency for recurring decision families;
- explicit path for learning which semantics deserve residency.

## What it is bad at

- compiler bugs/omissions can become systematic silent false-negatives;
- projection can drift into a shadow canonical ENA;
- more moving parts than monolithic-hot or simple file/Git cold read;
- refresh/invalidation logic itself needs evidence.

## Variants

- generated `AGENTS.md` / `SOUL.md` projection;
- compiled JSON/YAML local semantic map;
- local domain profile generated from Current concept map;
- task-family-specific resident bundles;
- adaptive projection whose residency changes from naturalistic retrieval evidence.

## Anti-degradation note

Do not let this HOW absorb the others by saying every mechanism is "just a projection compiler adapter". A monolithic-hot Host may have no meaningful compiler; a tool-native Host may retrieve directly; a file/Git Host may only need a tiny pointer/kernel.

`LOCAL_WINNER = DURABLE_PROJECTION_HOST_CANDIDATE`
