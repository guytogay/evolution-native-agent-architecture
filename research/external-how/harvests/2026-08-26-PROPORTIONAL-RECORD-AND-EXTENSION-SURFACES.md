# External HOW Harvest — Proportional Record and Extension Surfaces

Date: 2026-08-26

Status: `EXTERNAL_HOW_HARVEST / CANDIDATE_MECHANISMS / NOT_SELECTION / CURRENT_UNCHANGED`

Related: #104, `research/reconstruction/RECOVERED-VARIATION-MAP.md` RV-002 and RV-004.

## Research questions

### RV-002 — proportional evolution-record representation

Can an Agent/Host preserve truthful evolution lineage without requiring one large future-complete record shape for every low-consequence occurrence?

### RV-004 — portable core + Host extension surface

Can ENA preserve a strict interoperable portable core while allowing useful Host-local metadata without forcing schema forks or opening the whole schema indiscriminately?

This harvest searches for **mechanism patterns**, not framework winners.

---

## HOW family A — CloudEvents core + optional + extension attributes

Source class: `OPEN_STANDARD / OFFICIAL_SPECIFICATION`

Sources:

- https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md
- https://github.com/cloudevents/spec/blob/main/cloudevents/extensions/README.md
- https://github.com/cloudevents/spec/blob/main/cloudevents/formats/cloudevents.proto

Observed mechanism:

CloudEvents separates:

```text
REQUIRED CORE CONTEXT
+ OPTIONAL STANDARD CONTEXT
+ EXTENSION CONTEXT ATTRIBUTES
+ EVENT DATA
```

The core specification defines a small required event identity/context surface. Extension attributes can be added without becoming core semantics. Documented extensions can be tried and standardized separately; implementations are not limited to only the documented extension set.

The protobuf format makes the separation concrete: required attributes are explicit fields while optional/extension attributes are carried in a map.

### ENA mapping

This is a strong candidate HOW for RV-004:

```text
ENA_PORTABLE_CORE_RECORD
+ namespaced/typed extension context
+ Host-local or experimental metadata
```

It suggests a middle path between:

```text
additionalProperties: false everywhere
```

and:

```text
arbitrary open object everywhere
```

### Important boundary

CloudEvents extension attributes have no universal meaning merely because they are carried. ENA would still need provenance/namespace/version semantics if an extension affects a material decision.

```text
EXTENSION_CARRIED != EXTENSION_TRUSTED
EXTENSION_PRESENT != CORE_SEMANTIC
```

### Candidate disposition

`HIGH_VALUE_REFERENCE_PATTERN / DO_NOT_COPY_SCHEMA_BLINDLY`

---

## HOW family B — CloudEvents experimental extension promotion path

Source class: `OPEN_STANDARD_GOVERNANCE_PATTERN`

Source:

- https://github.com/cloudevents/spec/blob/main/cloudevents/extensions/README.md

Observed mechanism:

Extensions can exist and be tested before inclusion in the core specification. Support is optional; extension-level requirements apply only when that extension is used.

### ENA mapping

This directly fits the tree/HOW-growth discipline:

```text
portable trunk
-> experimental extension/HOW branch
-> field use
-> retain/specialize/retire
-> only sometimes promote shared semantics
```

It is therefore useful not only as schema extensibility but as an external example of **variation without premature core promotion**.

### Candidate disposition

`REFERENCE_GOVERNANCE_PATTERN`.

---

## HOW family C — OpenTelemetry event records for point-in-time occurrence

Source class: `OPEN_OBSERVABILITY_STANDARD / OFFICIAL_DOCUMENTATION`

Sources:

- https://opentelemetry.io/docs/specs/semconv/
- https://opentelemetry.io/docs/specs/semconv/general/events/

Observed mechanism:

OpenTelemetry distinguishes named point-in-time Events from longer operations/traces. Events are appropriate for checkpoints, state changes, lifecycle moments, outcomes, and other meaningful occurrences in a longer/asynchronous flow.

Semantic conventions provide common fields where interoperability matters while attributes carry event-specific details.

### ENA mapping

Candidate HOW for RV-002:

```text
minimal occurrence event
-> later related experiment/evaluation/integration events
-> composition/query produces current lifecycle understanding
```

Rather than writing one object with empty placeholders for events that have not happened yet.

This is structurally close to event sourcing but can be used as a lightweight operational/evidence pattern without requiring a full event-sourced Host.

### Candidate disposition

`HIGH_VALUE_PROGRESSIVE_ENRICHMENT_PATTERN`.

---

## HOW family D — OpenAI Agents SDK trace/span/custom metadata

Source class: `OFFICIAL_AGENT_SDK_DOCUMENTATION`

Sources:

- https://openai.github.io/openai-agents-python/tracing/
- https://openai.github.io/openai-agents-python/ref/tracing/create/

Observed mechanisms:

- a Trace represents one logical end-to-end workflow;
- Spans represent actual operations as they occur;
- custom spans can carry arbitrary structured operation-specific data;
- trace metadata is optional/customizable;
- automatic task/turn spans can be disabled for a more compact hierarchy while keeping materially useful agent/tool/generation/handoff/custom spans;
- sensitive input/output capture can be disabled independently of trace existence.

### ENA mapping

For RV-002, this is a concrete Agent-runtime example of **pay-for-observation detail when useful** instead of one universal maximal record shape.

Possible ENA pattern:

```text
EVOLUTION_TRACE / CANDIDATE_ID
  + occurrence spans/events only when they occur
  + richer evidence/settlement spans only when material
  + optional/custom Host metadata
```

For RV-009 Selective Legibility, sensitive-data capture controls also demonstrate that occurrence/provenance visibility can be separated from payload disclosure.

### Important boundary

Tracing is observability, not by itself an evolution-governance record. ENA must not infer that a trace/span system proves authority, fitness, commitment settlement, or semantic compliance.

### Candidate disposition

`AGENT_NATIVE_REFERENCE_PATTERN / NEEDS_ENA_SEMANTIC_MAPPING`.

---

## Preliminary comparison

| Mechanism | RV-002 proportional record | RV-004 extension surface | Key risk |
|---|---|---|---|
| CloudEvents required/optional/extensions | medium | high | extensions can become ungoverned semantic soup |
| CloudEvents experimental extensions | low/medium | high | optionality can fragment interoperability |
| OpenTelemetry event records | high | medium | observability events may lack governance/authority semantics |
| OpenAI trace/span/custom metadata | high for Agent Hosts | medium | tracing can be mistaken for truth/evidence |

The table is not a ranking or selection result.

## Candidate combined branch

A possible ENA reference HOW family suggested by the external mechanisms is:

```text
minimal portable occurrence envelope
+ append/attach later lifecycle events as reality unfolds
+ strict shared core
+ explicit namespaced Host extensions
+ material-decision resolver/projector
```

This is **not yet selected**. It must be compared against the current v2 record semantics, validators, migration packet requirements, and Host evidence.

## Falsification questions

Before adopting this direction, test:

1. Does split event/envelope representation lose invariants that the current single record can enforce cheaply?
2. Can a material decision resolve all required experiment/evaluation/authority/settlement facts without expensive joins or missing-event ambiguity?
3. Can extensions remain clearly non-Core while still traveling across Hosts when needed?
4. What prevents Host extensions from laundering unvalidated fields into selection decisions?
5. Does progressive enrichment actually reduce Agent/Host burden in real use, or merely move complexity into the resolver?
6. Which events must be immutable occurrence facts versus derived/current projections?

## Current disposition

`EXTERNAL_HOW_SPACE_EXPANDED = YES`

`UNIVERSAL_WINNER_SELECTED = NO`

`CURRENT_CHANGE = NO`

Next: map these mechanisms against the current evolution-record/tool shape and only then decide whether a reference prototype or deterministic fixture would pay engineering rent.
