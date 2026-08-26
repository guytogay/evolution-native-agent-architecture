# Finite-Context / LITE Adoption — plural reference HOW family

Status: `RESEARCH_PROTOTYPE_FAMILY / NOT_CURRENT / NOT_RELEASE_CANDIDATE`

Related: #90, #89, #46, #51, #72, Tiny Hot Kernel / Semantic Router, PR #82.

## WHAT

Make ENA usable by a finite-context Host without requiring every Host to load the whole Current package into every decision.

The practical adoption problem is:

> How does a fresh Agent have enough ENA semantics available at the right time, know which Current it is using, notice staleness, and fail honestly when the semantic source cannot be recovered?

This is not one storage/retrieval problem. Different Hosts expose materially different runtime substrates.

## WHY

Observed/credible failure shapes include:

```text
complete ENA package exists on disk
-> ordinary session never loads relevant semantics
-> ADOPTION != RETRIEVAL/APPLICATION
```

```text
all ENA text injected every session
-> high context cost / task starvation
-> semantics remain available but adoption becomes economically brittle
```

```text
small local projection is loaded
-> canonical Current changes
-> projection still narrates old semantics as current
```

```text
semantic search/index exists
-> index or resolver is unavailable
-> Agent silently answers from vague memory
-> retrieval failure becomes false confidence
```

```text
Host has strong native memory/tooling
-> universal ENA packet forces redundant machinery
-> adoption cost rises without decision value
```

## HOW — deliberately plural

This family preserves four implementation lineages. None is the universal default.

### HOW-A — File/Git tiny-resident + exact cold source

A small always-loaded kernel/pointer lives in a file; canonical Current remains in a local Git checkout or immutable package; a deterministic router/exact-path read recovers cold semantics.

Fit: file-oriented Agents, Codex/CLI-style Hosts, repositories with durable local instructions.

See `HOW-A-FILE-GIT-TINY-COLD.md`.

### HOW-B — Tool-native semantic retrieval

Resident cues stay small; a Host-native retrieval/search tool resolves decision-shaped queries into canonical Current material, with exact-path fallback and explicit retrieval status.

Fit: Hosts with reliable search/index/memory tools and cheap tool invocation.

See `HOW-B-TOOL-NATIVE-RETRIEVAL.md`.

### HOW-C — Monolithic hot projection

A Host intentionally keeps a large or complete ENA operational projection always resident. This is valid when context cost is acceptable and retrieval reliability would otherwise be worse.

Fit: Hosts with large context budgets, stable instruction injection, or weak/unavailable cold retrieval.

See `HOW-C-MONOLITHIC-HOT.md`.

### HOW-D — Hybrid compiled local projection

A Host compiles a task/runtime-oriented local projection from canonical Current, keeps that projection hot, and maintains source identity + refresh/invalidation rules while retaining cold canonical access for misses.

Fit: mature Agents with durable local projection/compiler machinery.

See `HOW-D-HYBRID-COMPILED-PROJECTION.md`.

## Common expectations — interface only

The HOWs differ internally, but each should answer these practical questions:

1. **Identity** — which canonical ENA Current/source does this runtime claim to derive from?
2. **Availability** — how can decision-relevant semantics actually reach the Agent?
3. **Freshness** — what happens when canonical Current/source identity changes?
4. **Failure** — what happens when the selected semantic access path is unavailable or partial?
5. **Projection honesty** — does a local/hot projection distinguish itself from the complete canonical source?
6. **Economics** — what resident/context/tool/maintenance cost does the Host pay?

These are not a mandate for one common packet schema.

## Multiple HOWs can coexist in one Host

A Host may combine mechanisms, for example:

```text
small resident consequence kernel
+ native semantic search
+ exact Git fallback
+ compiled local projection for frequently used domains
```

or:

```text
monolithic hot load for a small dedicated governance Agent
+ no runtime cold resolver at all
```

Coexistence is allowed. A local winner is also allowed.

## Selection questions

Evaluate per Host/environment:

- material false-negative rate: relevant ENA semantics never become available;
- false-positive/context tax: irrelevant semantics interrupt ordinary work;
- source freshness and invalidation reliability;
- retrieval/fallback failure honesty;
- resident token/byte cost;
- tool latency/availability;
- maintenance burden;
- semantic projection drift;
- naturalistic fresh-session behavior.

Do not select one HOW from aggregate token count or architectural elegance alone.

## Planned machine evidence

This prototype family includes separate executable reference mechanisms and one Host-fit selftest. The selftest must preserve both:

- scenarios where multiple HOWs remain acceptable;
- scenarios where one local winner is reasonable.

A later field experiment should compare at least two materially different HOWs on real Hosts before any adopter-facing recommendation is generalized.

## Degradation alarms

Raise an explicit warning if future work does any of the following:

- treats Tiny Hot Kernel as the universal adoption implementation;
- treats monolithic-hot as a failed architecture solely because it is large;
- replaces tool-native retrieval with a mandated ENA-specific index without Host evidence;
- turns compiled projection into a shadow canonical ENA;
- drops source identity/freshness because the projection "usually works";
- collapses all four HOWs into one schema whose fields assume one runtime architecture;
- declares one local winner to be the universal adopter profile;
- reduces a working HOW to `Host-specific detail` without preserving the actual recipe/tooling.

## Evidence boundary

A valid adoption mechanism does not prove:

- the model will naturally apply every retrieved semantic;
- all decision-relevant ENA material was retrieved;
- the canonical source is externally trustworthy merely because identity matches;
- one HOW is globally superior.

`CURRENT_CHANGE = NO`

`HOW_PLURALITY = ACTIVE`

`ADOPTION != APPLICATION`
