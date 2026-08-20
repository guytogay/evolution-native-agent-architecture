# Contribution — Layered Capability Binding and Swappable Model Substrates

```yaml
project: ena
artifact_type: CONTRIBUTION
status: UNRECONCILED
canonical_status: NOT_MAINLINE
promotion_status: NOT_PROMOTED
created_at: "2026-08-20T13:55:00+08:00"
participant:
  kind: ChatGPT
  role_this_contribution: CONTRIBUTOR
  access_surfaces:
    github: WRITE
    google_drive: WRITE
relationship: DEEPER_BOUNDARY_CONDITION
bridge_state:
  source_surface: GITHUB
  target_surface: GOOGLE_DRIVE
  status: SATISFIED
  target_ref: "Google Drive file 1ZLM9lLTKfGjbZnYgbHo1lloEuU4Mp2C7V-u15lumu-c"
  semantic_delta: NONE
```

## Research question

How should ENA assess and govern capability when an Agent is not identical to its underlying model, and the cognitive substrate may be switched or mixed at runtime (for example DeepSeek and MiniMax inside the same DeepSeek Harness instance)?

## Existing Mainline basis

Current v0.2.11 Self-Positioning already records, if observable:

- host/platform identity;
- model identity;
- workspace/project;
- process/container/sandbox/session context;
- persistence model;
- connected tools/services;
- approval model.

This supports a distinction between Agent/Host and Model, but swappable/multi-model composition creates a stronger applicability problem.

## Core distinction

`Agent identity != model identity != host identity != available capability != authorized capability`

A persistent Agent may keep the same project history, memory, role, host, and obligations while its cognitive model changes. Conversely, a model-native capability may be unavailable to the Agent if the host does not expose the required input/output path, credentials, adapter, or tool.

## Candidate layered model

Treat capability as a composition with provenance rather than a permanent label on the Agent.

### Layer 1 — Model-native / provider capability

Potential abilities of a specific model/provider/version, such as:

- text reasoning;
- image understanding;
- audio understanding;
- image generation;
- video generation;
- long-context handling;
- tool-call planning;
- structured-output reliability.

Vendor documentation or model self-report is not sufficient by itself for operational qualification.

### Layer 2 — Host-exposed capability

Whether the current Host actually exposes the model capability through usable interfaces:

- image bytes can reach the model;
- provider API route exists;
- credentials are valid;
- required tool/adapter is present;
- output can be persisted or delivered;
- platform policy permits the operation.

A model may natively support video generation while the Agent has no video-generation capability because the Host does not expose that route.

### Layer 3 — Composed Agent capability

Whether the complete composition can perform the task in the current environment:

`Agent + Host + Model Binding + Tool/Adapter + Credential + Configuration + Runtime State -> Observable Capability`

This is the level most relevant to task routing.

### Layer 4 — Reliability / evidence profile

A capability can be available but weakly evidenced. Store evidence by dimension, subject, model binding, host, configuration, scope, and interval.

Examples:

- image classification quality;
- completion-attestation integrity;
- code execution reliability;
- visual reasoning;
- image-generation instruction adherence;
- video-generation quality;
- safety calibration;
- recovery judgment;
- cost/latency.

### Layer 5 — Authority / consequence envelope

`Can perform X != authorized to perform X != authorized to certify X succeeded.`

Authority remains governed separately from capability.

## Model binding as runtime state

A DSH-like Agent may expose a model pool:

```yaml
model_pool:
  - binding_id: deepseek-reasoning
    provider: DeepSeek
    model_ref: "<version>"
    routes: [reasoning, recovery_triage, code_review]
  - binding_id: minimax-multimodal
    provider: MiniMax
    model_ref: "<version>"
    routes: [vision, image_generation, video_generation, cheap_parallel_exploration]
```

Task execution should record which binding actually supported the claim or artifact.

Example:

```yaml
capability_evidence:
  capability: image_understanding
  subject_ref: dsh-agent-01
  model_binding_ref: minimax-multimodal
  host_identity: dsh-host-A
  adapter_ref: vision-route-v2
  configuration_state_ref: cfg-2026-08-20
  evidence_refs: [test-vision-014, test-vision-015]
  verdict: EVIDENCED
```

## Mixed-model composition

One task may use multiple bindings:

`MiniMax vision -> DeepSeek reasoning -> machine validator -> authorized executor`

The final Agent capability is a composed property. Local validity of each component does not imply composed validity; the route itself may require evidence.

A model switch or routing change is therefore an evidence-applicability boundary.

## Revalidation rule candidate

Do not globally reset the Agent when a model changes. Revalidate the capabilities whose evidence depended materially on the changed binding.

Examples:

- switch DeepSeek -> MiniMax for text reasoning: reasoning reliability and completion-attestation evidence may need revalidation;
- keep DeepSeek reasoning but add MiniMax image generation: existing recovery evidence need not automatically expire;
- change the vision adapter while keeping the same model: vision capability evidence may expire even though model identity is unchanged;
- use fallback routing after provider outage: authority may contract until the fallback route is evidenced.

This is selective repositioning, not identity replacement.

## Developmental stage interaction

P0-P5 should remain a maturity claim about the Agent/Host operating arrangement, not a leaderboard of model modalities.

A model gaining image/video generation does not advance developmental stage by itself.

However, if a stage requirement materially depends on an active model binding and the binding becomes unavailable or contradicted, the system must expose the limitation and re-evaluate the affected stage/gate claim.

Where another evidenced route covers the same ecological function, the Host may retain its stage while the specific participant/binding becomes dormant or restricted.

## Ecological specialization

Special model abilities should strongly influence task routing and niche formation.

For example, MiniMax may be weak at completion attestation but strong at multimodal perception/generation. ENA should permit a profile like:

```yaml
operating_profile:
  image_understanding: STRONG_EVIDENCE
  image_generation: STRONG_EVIDENCE
  video_generation: PARTIAL_EVIDENCE
  cheap_parallel_exploration: STRONG_EVIDENCE
  completion_attestation: CONTRADICTED
  recovery_lead: NOT_EVIDENCED
```

This supports specialization instead of global trust or global exclusion.

## Candidate machine concepts

Potential fields:

```yaml
agent_identity: ""
host_identity: ""
model_bindings: []
active_route: []
capability_subject:
  level: MODEL_NATIVE | HOST_EXPOSED | COMPOSED_AGENT | ROUTE
capability_state:
  availability: AVAILABLE | DORMANT | UNAVAILABLE | UNKNOWN
  qualification: EVIDENCED | PARTIAL | NOT_EVIDENCED | CONTRADICTED | UNKNOWN
authority_state: ""
attestation_authority: ""
```

## Candidate maxims — research only

- `Agent identity is not model identity.`
- `Model capability is potential; Agent capability is composed and evidenced.`
- `A model switch is an applicability boundary, not necessarily an Agent rebirth.`
- `Revalidate affected capabilities, not unrelated identity.`
- `Special ability should shape ecological niche, not inflate global trust.`
- `Can perform != can certify != is authorized.`

## Falsification pressure

Test:

- whether the layered model creates too much bookkeeping for simple single-model hosts;
- whether model/provider capability can be reliably distinguished from tool/service capability;
- whether fallback routing silently inherits stale evidence;
- whether mixed-model tasks create unverified composition effects;
- whether a stable Agent identity can survive frequent model switching without semantic confusion;
- whether stage claims remain honest when the active model pool changes;
- whether capability evidence becomes too granular to remain usable.

## Current judgment

Treat as:

`EVOLUTION_INBOX_CANDIDATE / RESEARCH_INPUT / NOT_PROMOTED`

No ENA v0.2.11 MAINLINE change is justified from this contribution alone.
