# ENA External HOW Source Registry

Status: `ACTIVE_REGISTRY / OPEN_CARDINALITY / RESEARCH_ONLY`

Observed: 2026-08-26

This registry records concrete external mechanisms that may enlarge ENA's HOW possibility space. Entries are not endorsements and are not exhaustive.

## LangGraph — persistence, checkpoints, interrupts, time travel

Source class: `OFFICIAL_FRAMEWORK_DOCUMENTATION`

Sources:

- https://docs.langchain.com/oss/python/langgraph/persistence
- https://docs.langchain.com/oss/python/langgraph/interrupts
- https://docs.langchain.com/oss/python/langgraph/add-memory

Observed mechanisms:

- per-thread durable checkpoints;
- restart from last successful graph state;
- pending writes from successful nodes preserved across partial failure;
- human/external interrupts that persist state and resume later;
- replay/time-travel from prior checkpoints;
- explicit short-term and long-term memory separation.

Important failure detail:

A node containing an interrupt restarts from the beginning when resumed, so side effects performed before an interrupt must be idempotent or otherwise safely handled.

ENA mapping:

- Recovery / checkpoint organ;
- WAIT / pause / human-input state;
- Effect Lifecycle / idempotency;
- History fork/time-travel semantics;
- Memory / thread persistence.

Candidate HOW role:

`LANGGRAPH_CHECKPOINT_INTERRUPT_ADAPTER` or native-Host mapping for Hosts already built on LangGraph.

Selection state: `RETAIN_AS_CANDIDATE_HOW_FAMILY`.

---

## Temporal — durable execution, Workflow/Activity separation, signals/updates, compensation

Source class: `OFFICIAL_DURABLE_EXECUTION_DOCUMENTATION`

Sources:

- https://go.temporal.io/platform-hub/ai-engineering/ai-reference-architecture
- https://go.temporal.io/platform-hub/ai-engineering
- https://docs.temporal.io/

Observed mechanisms:

- Workflow state persists independently of worker process lifetime;
- non-deterministic external/LLM/tool effects are isolated in Activities;
- Activity results are recorded so recovery does not blindly replay completed side effects;
- durable waits/signals/updates for long-running interactions;
- workflow history as operational/audit record;
- `continue_as_new` pattern to bound long workflow histories;
- retry/timeout/heartbeat and Saga/compensation patterns.

ENA mapping:

- Recovery Kernel vs effect execution;
- External Effect Lifecycle;
- WAIT / Autonomous Patience;
- settlement/reconciliation;
- bounded history / memory metabolism;
- durable commitment execution.

Candidate HOW role:

`DURABLE_WORKFLOW_NATIVE_ORGAN` for Hosts capable of using Temporal-like runtimes, plus reference patterns for other Hosts.

Selection state: `HIGH_VALUE_CANDIDATE / REQUIRES_ENA_COMPOSITION_ANALYSIS`.

---

## OpenAI Agents SDK — sessions, resumable run state, compaction, sandbox memory

Source class: `OFFICIAL_AGENT_SDK_DOCUMENTATION`

Sources:

- https://openai.github.io/openai-agents-python/sessions/
- https://openai.github.io/openai-agents-js/guides/sessions/
- https://openai.github.io/openai-agents-python/sandbox/memory/

Observed mechanisms:

- pluggable persistent `Session` interface;
- multiple storage implementations (SQLite, Redis, SQLAlchemy, MongoDB, Dapr, Conversations API, encrypted/session wrappers);
- resumable/interrupted `RunState` paths;
- automatic Responses compaction wrapping a backing session;
- compaction replacement/rollback handling and concurrency caveats;
- sandbox-agent memory separates conversational session history from distilled lessons written to workspace memory files.

ENA mapping:

- Host persistence adapter;
- Memory Metabolism / conversation vs compiled memory;
- compaction and bounded active context;
- recovery/continuation;
- provenance risk around compaction/rewrite.

Candidate HOW role:

`OPENAI_SESSION_MEMORY_ADAPTER_FAMILY`, not one universal memory organ.

Open questions:

- compaction semantic sufficiency and provenance retention;
- natural recall/salience of distilled memory;
- decision-material loss across compaction.

Selection state: `RETAIN / FALSIFY_PROJECTION_BOUNDARIES`.

---

## Letta — memory hierarchy, persistent editable blocks, attach/detach context

Source class: `OFFICIAL_STATEFUL_AGENT_RUNTIME_DOCUMENTATION`

Sources:

- https://docs.letta.com/
- https://docs.letta.com/tutorials/attaching-detaching-blocks/
- https://docs.letta.com/api/typescript

Observed mechanisms:

- self-editing memory hierarchy split between in-context and out-of-context state;
- persistent editable memory blocks;
- memory blocks can be attached/detached dynamically;
- blocks can be shared across agents;
- detached blocks remain durable and can later be reattached;
- Agent state is persisted in a DB backend and can recreate the agent.

ENA mapping:

- Tiny Hot Kernel / selective hot context;
- Host-native memory organ;
- selective legibility/access boundary;
- shared multi-agent memory;
- Hot/Cold projection and context switching.

Candidate HOW role:

`NATIVE_MEMORY_BLOCK_REBIND` and a concrete counterexample to the assumption that every Host needs an ENA-shaped memory store.

Open questions:

- provenance/authorship of self-edited blocks;
- stale/shared-write conflict behavior;
- retrieval trigger behavior for cold memory;
- authority around sensitive block attach/detach.

Selection state: `HIGH_VALUE_HOST_PATTERN`.

---

## Microsoft Agent Framework — explicit workflows, checkpoints, HITL, agent/workflow spectrum

Source class: `OFFICIAL_FRAMEWORK_DOCUMENTATION`

Sources:

- https://learn.microsoft.com/en-us/agent-framework/
- https://learn.microsoft.com/en-us/agent-framework/concepts/workflows/
- https://learn.microsoft.com/en-us/agent-framework/workflows/checkpoints
- https://learn.microsoft.com/en-us/agent-framework/journey/workflows

Observed mechanisms:

- explicit inspectable workflows mixing deterministic executors, agents, and humans;
- checkpoint/resume for long-running workflows;
- workflow state, events, observability, fan-out/fan-in;
- sequential, concurrent, handoff, group-chat, and Magentic orchestration patterns;
- explicit spectrum between model-decided autonomy and developer-defined deterministic flow.

ENA mapping:

- role/niche and multi-agent orchestration;
- explicit operational state machines;
- WAIT/HITL;
- recovery/checkpoint;
- Minimum Sufficient Intervention: use deterministic structure where it pays rent, LLM freedom where needed.

Candidate HOW role:

`WORKFLOW_AGENT_HYBRID_ORGAN_FAMILY`.

Selection state: `RETAIN / COMPARE_WITH_LANGGRAPH_AND_TEMPORAL`.

---

## A2A Protocol — cross-agent discovery and stateful task lifecycle

Source class: `OPEN_PROTOCOL_OFFICIAL_SPECIFICATION`

Sources:

- https://a2a-protocol.org/dev/specification/
- https://a2a-protocol.org/v0.3.0/specification/

Observed mechanism:

- common interoperability model for independent opaque agents;
- capability discovery;
- `Task`, `Message`, `Artifact`, `contextId` and task-state semantics;
- streaming and asynchronous updates;
- task lifecycle includes paused/input-required/auth-required and terminal outcomes;
- independent agents need not expose internal memory/tools to collaborate.

ENA mapping:

- Evolution Commons discovery/interoperability;
- commitment/task identity;
- WAIT/input-required states;
- artifact/effect output identity;
- cross-agent opacity / selective legibility;
- external task settlement semantics.

Candidate HOW role:

`A2A_INTEROP_ADAPTER` and an external task-lifecycle reference pattern.

Open questions:

- commitment ownership vs A2A task status;
- authority delegation and counterparty settlement beyond transport/task state;
- provenance/trust across agent boundaries.

Selection state: `HIGH_VALUE_FOR_MULTI_AGENT_HOW_BRANCHES`.

---

## Anthropic multi-agent research system — parallel research topology and cost boundary

Source class: `AI_LAB_ENGINEERING_REPORT`

Source:

- https://www.anthropic.com/engineering/multi-agent-research-system

Observed mechanism/evidence:

- lead agent delegates independent search directions to parallel subagents;
- separate context windows reduce path dependence and increase breadth;
- multi-agent design is most useful for highly parallelizable research tasks;
- Anthropic reports substantially higher token cost for multi-agent research and warns that tightly coupled tasks are weaker fits.

ENA mapping:

- ecological specialization;
- parallel research nodes;
- evidence independence vs merely duplicated agents;
- resource metabolism / multi-agent cost;
- role/niche selection based on task topology.

Candidate HOW role:

`PARALLEL_RESEARCH_NODE_PATTERN`, conditional on task decomposition and budget.

Selection state: `CONDITIONAL / NOT_UNIVERSAL_MULTI_AGENT_DEFAULT`.

---

## Mem0 — extract/consolidate/update/search memory layer

Source class: `VENDOR_DOCUMENTATION_AND_ENGINEERING_BLOG`

Sources:

- https://docs.mem0.ai/core-concepts/memory-operations/add
- https://docs.mem0.ai/core-concepts/memory-operations/update
- https://docs.mem0.ai/core-concepts/memory-operations/search
- https://mem0.ai/blog

Observed mechanisms:

- infer structured memories from interactions;
- scope by user/agent/run and metadata;
- search through semantic + filtered retrieval;
- update memories when facts/preferences change;
- managed and OSS implementations;
- recent engineering discussion around staleness, event-based memory, background consolidation, and cross-session identity.

ENA mapping:

- Memory Compiler candidate;
- freshness/supersession;
- durable knowledge vs raw transcript;
- retrieval filters/scope;
- possible background consolidation organ.

Evidence caution:

Much of the performance/usefulness narrative is vendor-authored; mechanism existence is useful evidence, but superiority claims require independent validation.

Selection state: `RETAIN_AS_EXTERNAL_MEMORY_HOW_CANDIDATE`.

---

## AI developer community — memory activation failures

Source class: `COMMUNITY_FIELD_REPORTS / WEAK_NONINDEPENDENT_EVIDENCE`

Sources include:

- https://www.reddit.com/r/LocalLLaMA/comments/1uqfh7r/what_is_the_current_memory_meta/
- https://www.reddit.com/r/LocalLLaMA/comments/1q3t7go/llm_memory_systems/

Observed recurring claims:

- elaborate memory stores can still fail because agents do not naturally remember to retrieve them;
- simple inspectable files remain popular in practice;
- some practitioners force retrieval/tool calls because autonomous recall is unreliable;
- users distinguish working/decision/knowledge memory rather than treating all persistence as RAG.

ENA mapping:

- `KNOWN != RETRIEVED != SALIENT != APPLIED`;
- Tiny Hot Kernel / retrieval invocation;
- natural vs primed salience evidence;
- Memory Organ should not be judged by storage sophistication alone.

Evidence caution:

Community anecdotes are correlated, self-selected, and not controlled proof. Use them to find failure modes and candidate tests, not to establish universal facts.

Selection state: `FAILURE_MODE_DISCOVERY_INPUT`.

---

## Registry continuation rule

New entries should be added when they expose a materially new mechanism, boundary condition, counterexample, or Host realization.

Do not add frameworks merely to grow a list.

Do not stop searching because this registry already contains several recognizable ecosystems.

```text
CURRENT_SOURCE_SET != COMPLETE_HOW_SPACE
```
