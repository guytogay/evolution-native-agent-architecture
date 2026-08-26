# External HOW Harvest — Initial Landscape — 2026-08-26

Status: `DATED_RESEARCH_HARVEST / NOT_SELECTION / NOT_CURRENT`

Purpose: preserve the first external mechanism scan performed after the HOW-growth methodology was made explicit.

This harvest is a dated observation. `SOURCE-REGISTRY.md` is the continuing registry.

## Main finding

The external ecosystem already contains many concrete mechanisms that map directly to ENA's unresolved operational surfaces.

Therefore ENA should not treat HOW engineering as synonymous with inventing custom ENA machinery.

A more productive path is:

```text
ENA failure/property
-> external mechanism search
-> concrete mechanism mapping
-> static/adversarial comparison
-> Host applicability
-> evidence-selected adoption/coexistence
```

## Mechanism clusters observed

### Durable state / recovery / WAIT / consequential effects

LangGraph and Temporal provide materially different but overlapping HOW families:

- checkpointed state;
- durable waits and resumable execution;
- replay/history;
- separation of deterministic orchestration from non-deterministic effects;
- retry/partial-failure handling;
- human/external interrupts.

The important ENA opportunity is not to standardize on either framework, but to extract reusable operational patterns and Host adapter contracts.

### Memory / bounded context / compilation

OpenAI Agents SDK, Letta, and Mem0 expose distinct memory shapes:

- conversation/session persistence;
- history compaction;
- distilled run lessons separate from session history;
- self-editable persistent in-context blocks;
- dynamic attach/detach of memory;
- extracted/updated/retrieved structured memories.

This supports ENA's direction that `memory != one store` and that several concrete HOWs can realize bounded active context and durable learning.

### Multi-agent coordination / interoperability

Microsoft Agent Framework, A2A, and Anthropic's multi-agent research system provide different coordination mechanisms:

- explicit workflow graphs;
- predefined orchestration patterns;
- cross-service agent task protocols;
- opaque-agent interoperability;
- parallel specialist research nodes.

These should not be collapsed into one "multi-agent HOW". They address different failure/topology conditions.

### Community failure evidence

Recent developer discussions still report that sophisticated memory storage can fail at the activation layer: the agent simply does not decide to retrieve memory when relevant.

This reinforces the ENA distinction:

```text
KNOWN != RETRIEVED != SALIENT != APPLIED
```

but remains weak community evidence rather than controlled proof.

## Immediate reconstruction implications

High-value mappings for further ENA work include:

- `Commitment / Settlement × Effect Lifecycle × durable workflow / task lifecycle`;
- `Recovery Adapter × Temporal/LangGraph checkpoint semantics`;
- `Tiny Hot Kernel × Letta blocks / SDK session-compaction / exact retrieval`;
- `Evolution Commons × A2A task/message/artifact model`;
- `Ecological specialization × Microsoft orchestration / Anthropic parallel research`;
- `Memory Compiler × Letta/OpenAI sandbox memory/Mem0 extraction-consolidation patterns`.

These are candidate branch directions, not a fixed priority order or exhaustive taxonomy.

## Selection warning

External ecosystem maturity creates a new risk: **framework-shaped ENA**.

Do not redesign the ENA ontology to mirror whichever framework has the best documentation.

Instead:

```text
ENA failure model remains the parent question
external framework supplies candidate organ patterns
Host reality selects fit
```

## Sources

See `../SOURCE-REGISTRY.md` for the source URLs and mechanism-level notes used in this harvest.
