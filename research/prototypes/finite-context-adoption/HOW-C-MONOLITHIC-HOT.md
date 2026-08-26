# HOW-C — Monolithic hot projection

Status: `REFERENCE_HOW / RESEARCH_ONLY`

## Host fit

Use this HOW when keeping a large or complete ENA operational projection always resident is cheaper/more reliable than depending on cold retrieval.

This is intentionally preserved as a valid phenotype. Large resident context is not automatically a design failure.

Typical Hosts:

- dedicated governance/research Agents with large context budgets;
- Hosts with weak/unavailable retrieval tooling;
- environments where instruction injection is highly reliable but tool availability is not;
- small enough ENA projections whose resident cost is acceptable relative to task complexity.

## Concrete layout

Example:

```text
always-loaded instruction surface
  = ENA operational projection
  + exact canonical source identity
  + projection limitations
  + refresh marker
```

The projection may be the full operational subset or nearly the entire Current package, depending on Host economics.

## Runtime sequence

```text
fresh session
-> inject hot ENA projection automatically
-> ordinary reasoning sees ENA semantics without retrieval step
-> decision proceeds using resident material
-> exact cold source is optional for ambiguity/history/revalidation, not mandatory for every decision
```

## Freshness requirement

Monolithic-hot does not remove source identity requirements.

The injection surface should expose:

- canonical ENA version/source identity;
- projection generation/revision identity;
- refresh procedure or invalidation condition.

If canonical Current changes, the hot projection must be refreshed or explicitly marked stale.

## Economic measurement

This HOW should be judged on real cost rather than aesthetic size.

Measure at least:

- resident bytes/tokens;
- percentage of ordinary task context consumed;
- task-instruction starvation or collision;
- fresh-session injection reliability;
- material cue false-negative rate compared with cold-resolver alternatives;
- maintenance/refresh cost.

A large resident surface can be a local winner if it materially reduces retrieval failures and fits the Host budget.

## Failure behavior

If injection is missing in a fresh session, that is an adoption failure; the Agent must not claim resident ENA availability merely because a file exists somewhere.

If injection is stale, the Host may:

- refresh before material ENA-dependent work;
- use canonical cold read for changed dimensions;
- proceed on unaffected low-consequence work with explicit projection staleness.

## What this HOW is good at

- no retrieval-invocation false-negative after successful injection;
- simple runtime mechanics;
- robust behavior when tool access is unreliable;
- easy naturalistic observation of what is actually resident.

## What it is bad at

- context-constrained Hosts;
- large projections that compete with task instructions/data;
- high update frequency where reinjection/refresh is expensive;
- subtle projection drift hidden inside one large instruction block.

## Anti-degradation note

Do **not** classify this HOW as inferior merely because Tiny Hot Kernel is smaller.

OpenClaw-like field evidence already shows that some Hosts may choose monolithic hot loading. The correct question is local fitness:

```text
reliability gained
vs
context/maintenance cost
```

not:

```text
smaller == more evolved
```

`LOCAL_WINNER = LARGE_CONTEXT_OR_WEAK_RETRIEVAL_HOST_CANDIDATE`
