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

## HOW — deliberately plural and open-cardinality

This family currently contains **five identified implementation lineages**. The count is descriptive, not normative or closed. None is the universal default, and a new materially distinct Host phenotype may justify another HOW without being forced into the nearest existing slot.

`CURRENTLY_IDENTIFIED_HOW_COUNT != ARCHITECTURAL_SLOT_COUNT`

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

### HOW-E — Native Host organ rebind / mapping-only adoption

A mature Host keeps existing native organs that already realize relevant ENA properties and updates semantic bindings, source identity, gap mappings, and revalidation only where the new Current changes a material decision.

Fit: mature long-lived Agents whose transaction/recovery/state/audit/wake/governance organs already carry much of the required behavior, so importing duplicate ENA-shaped machinery would add burden without decision value.

See `HOW-E-NATIVE-HOST-REBIND.md`.

This HOW was added after DSH field evidence did not fit HOW-D without distorting the reported Host phenotype. The model expanded rather than compressing the Host into the existing count.

## Common expectations — interface only

The HOWs differ internally, but each should answer these practical questions:

1. **Identity** — which canonical ENA Current/source does this runtime claim to derive from?
2. **Availability** — how can decision-relevant semantics actually reach the Agent?
3. **Freshness** — what happens when canonical Current/source identity changes?
4. **Failure** — what happens when the selected semantic access path is unavailable or partial?
5. **Projection honesty** — does a local/hot/native projection distinguish itself from the complete canonical source and preserve its limitations?
6. **Economics** — what resident/context/tool/migration/maintenance cost does the Host pay?

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

or:

```text
native Host transaction/recovery organs
+ mapping-only ENA rebind
+ one small adapter only for an actual semantic gap
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
- migration and duplicate-organ burden;
- maintenance burden;
- semantic projection drift;
- naturalistic fresh-session behavior.

Do not select one HOW from aggregate token count or architectural elegance alone.

## Machine evidence status

HOW-A through HOW-E now have separate reference behavior and targeted machine coverage on the research branch. The currently implemented count remains an implementation inventory, not an architectural invariant.

Exact research head `2d0f589ea17b6b3b47d026006318a7363e6f25be` passed `Finite Context Adoption Research`, run `32927153520`, job `98052250754`:

- all currently implemented plural HOW tools compiled;
- plural adoption HOW selftest passed with open fixture cardinality;
- deployment recipe selftest passed, including HOW-E stale/evidence/gap boundaries;
- verification boundary completed with `HOW_CARDINALITY=OPEN` and `CURRENT_IMPLEMENTED_COUNT_IS_NOT_ONTOLOGY=TRUE`.

This upgrades HOW-E from design-only reference to **machine-guarded reference behavior**. It does not prove naturalistic Host application, cross-Host fitness, or that five is the final number of adoption HOWs.

Future family-level selftests must preserve both:

- scenarios where multiple HOWs remain acceptable;
- scenarios where one local winner is reasonable;
- the ability to add another materially distinct HOW without failing an accidental exact-count assertion;
- the ability to retire/merge a HOW only when function parity or usefulness failure supports that change.

A later field experiment should compare materially different HOWs on real Hosts before any adopter-facing recommendation is generalized.

## Cardinality discovery guard

This family follows `research/reconstruction/CARDINALITY-DISCOVERY-GUARD.md`.

Do not transform:

```text
five HOWs currently identified
```

into:

```text
finite-context adoption has five HOW slots
```

The same rule prevents the opposite distortion: if only two materially distinct HOWs survive reality contact for some scoped problem family, do not preserve five merely for symmetry.

## Degradation alarms

Raise an explicit warning if future work does any of the following:

- treats Tiny Hot Kernel as the universal adoption implementation;
- treats monolithic-hot as a failed architecture solely because it is large;
- replaces tool-native retrieval with a mandated ENA-specific index without Host evidence;
- turns compiled projection into a shadow canonical ENA;
- forces a mature native-organ Host into HOW-D or another pre-existing bucket merely to preserve taxonomy symmetry;
- drops source identity/freshness because the projection "usually works";
- collapses currently identified HOWs into one schema whose fields assume one runtime architecture;
- hard-codes the accidental current HOW count into validators or fixtures;
- pads the family with weak distinctions to satisfy a requested count;
- merges or omits material HOWs to satisfy a smaller requested count;
- declares one local winner to be the universal adopter profile;
- reduces a working HOW to `Host-specific detail` without preserving the actual recipe/tooling.

## Evidence boundary

A valid adoption mechanism does not prove:

- the model will naturally apply every retrieved semantic;
- all decision-relevant ENA material was retrieved;
- the canonical source is externally trustworthy merely because identity matches;
- one HOW is globally superior;
- the currently observed number of HOWs is complete or final.

`CURRENT_CHANGE = NO`

`HOW_PLURALITY = ACTIVE`

`HOW_CARDINALITY = DISCOVERED_NOT_PREALLOCATED`

`ADOPTION != APPLICATION`
