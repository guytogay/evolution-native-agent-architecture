# HOW-B — Tool-native semantic retrieval

Status: `REFERENCE_HOW / RESEARCH_ONLY`

## Host fit

Best when the Host already provides a reliable semantic search, memory index, document retrieval tool, or connected knowledge source that can resolve ENA material on demand.

Typical Hosts:

- assistants with built-in semantic memory/search;
- Hosts with vector/full-text indexes;
- tool-using Agents where retrieval calls are cheap and observable;
- remote knowledge-base deployments.

## Concrete mechanism

Keep only a compact recognition surface hot. When a material decision shape is recognized, query the Host's native retrieval primitive for the relevant ENA concept/decision shape.

Example sequence:

```text
resident cue
-> semantic query: "external effect may already have committed after timeout"
-> native retrieval tool
-> candidate ENA sections
-> bind result to canonical Current/source identity
-> if candidate confidence/scope is insufficient, use exact-path/canonical fallback
-> project only decision-relevant material into active context
```

This HOW can reuse the research Semantic Router as a fallback or grounding map, but the Host's native retrieval organ remains first-class. ENA does not require a separate vector database.

## Required operational evidence

The Host should be able to distinguish at least:

```text
NOT_ATTEMPTED
SUCCESS
PARTIAL
FAILED
```

and preserve enough evidence to answer:

- what query/decision shape triggered retrieval;
- what canonical source/version was searched;
- what results/sections were returned;
- whether exact fallback was attempted;
- whether the final projection omitted known material hits.

The exact trace format is Host-specific.

## Refresh/invalidation

When canonical Current/source identity changes:

- index contents must be refreshed or marked stale;
- cached retrieval results cannot silently remain current;
- old embeddings/index entries may remain historical but must not be narrated as the new Current.

A Host can implement this using index generation IDs, source digests, collection versions, or native document revision metadata.

## Failure behavior

If the semantic tool is unavailable:

- use an exact canonical fallback if available;
- otherwise material work narrows/waits/declares the missing semantic dependency;
- do not reconstruct the entire cold corpus from model memory and label that retrieval success.

If search returns multiple ambiguous sections, `PARTIAL` is valid; broader retrieval is preferable to a false exact hit.

## What this HOW is good at

- low resident cost;
- flexible natural-language decision-shape lookup;
- large cold corpora;
- Hosts that already have mature retrieval infrastructure.

## What it is bad at

- silent/no-op retrieval tools;
- indexes without source/version binding;
- environments where retrieval latency dominates the task;
- weak exact fallback after index drift.

## Variants

- vector semantic retrieval + exact document fetch;
- full-text/BM25 search + concept-map reranking;
- memory tool + explicit canonical-file fallback;
- remote document search with immutable source revision IDs.

`LOCAL_WINNER = TOOL_RICH_RETRIEVAL_HOST_CANDIDATE`
