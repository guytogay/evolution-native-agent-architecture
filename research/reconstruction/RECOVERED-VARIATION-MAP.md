# ENA Recovered Variation Map

Status: `ACTIVE_ARCHAEOLOGY / OPEN_CARDINALITY / RECOVER_BEFORE_SELECT / CURRENT_UNCHANGED / NOT_RELEASE_AUTHORITY`

Parent: #89  
Focused archaeology tracker: #104

## Purpose

Preserve concrete engineering variations that appeared historically but can disappear when later semantic compression, release closure, prototype selection, or tracker succession makes them less salient.

This file is **not** a backlog of changes ENA must implement. It is a recovered variation surface.

```text
RECOVERED != SELECTED
HISTORICAL_CANDIDATE != CURRENT_RECOMMENDATION
UNSELECTED != ABSENT
SUPERSEDED != ERASED
SIMPLIFICATION_CANDIDATE != DELETION_AUTHORITY
```

The map is open-cardinality. Add branches when another archaeology pass reveals decision-distinct historical variation.

## Sources reviewed in this pass

1. #89 master reconstruction source map and comments.
2. #88 anti-dissolution audit.
3. #90–#94 reconstruction workstreams and their comments.
4. `MECHANISM-RETENTION-LEDGER.md`.
5. `DEGRADATION-AUDIT-2026-08-26.md`.
6. Historical GitHub Issue census, including old field-validation and repository/publication trackers.
7. Predecessor-session export and an independent v0.3.6 architecture critique preserved in the user's durable conversation-file library.

### Issue-census result

The Issue-level pass did **not** reveal a large missing Core/topic family.

- #5 heterogeneous field-validation findings were later split into more specific release/adoption/evidence/authority/effect work and tracker succession.
- #61 explicitly closed as `SUPERSEDED_AND_ABSORBED`, preserving WorkBuddy claim-tightening and handing active questions to #70 + #89/#90–#94.
- #9 public-release work is primarily project-control/publication lineage rather than a missing ENA operational organ.
- historical placeholder Issues with no ENA meaning remain non-evidence.

The more material gap was lower-level: **concrete HOW and simplification variations existed in prior review/session material but were not retained in the current mechanism ledger as visible branches.**

---

## RV-001 — Verification Boundary Projection

### Earliest recovered appearance

Independent v0.3.6 architecture critique: schema/validator PASS can create an impression of trustworthy evolution even when the validator checks represented consistency only.

### WHAT

Make the boundary of a machine verification step explicit enough that downstream users/Agents do not upgrade:

```text
REPRESENTED_CONSISTENCY_PASS
```

into:

```text
EXTERNAL_TRUTH / REAL_AUTHORITY / ACTUAL_APPLICATION / FITNESS_PROOF
```

### WHY

A warning hidden in prose can lose to the psychological/operational authority of a green machine PASS.

Failure:

```text
VALIDATOR_PASS
-> confidence laundering
-> represented state narrated as reality proof
```

### Historical HOW branches

#### HOW-A — Machine-readable `verification_boundary`

Historical candidate enum family such as represented-only / Host-asserted / externally observed / independently supported.

Disposition: `RECOVERED_CANDIDATE / SHAPE_NOT_ACCEPTED`.

The exact enum is not authoritative and may recreate evidence-maturity pseudo-ladders if treated too strongly.

#### HOW-B — Separate represented-state and evidence carriers

Historical stronger candidate: keep structural record validation separate from evidence/observation validation.

Disposition: `PARTLY_REEXPRESSED` through later Generic Evidence Envelope / Evidence Dependency Map work.

#### HOW-C — Validator output carries explicit negative scope

A verifier emits what it did **not** check as part of the result, rather than relying on surrounding documentation.

Disposition: `OPEN_CANDIDATE`.

### Current surviving mechanisms

- prose boundary: schema PASS != semantic/external truth;
- Generic Evidence Envelope;
- Evidence Dependency Map;
- evidence/applicability workstream #94.

### Evidence needed

Determine whether a separate verification-boundary projection changes downstream interpretation/automation beyond what the current envelope/dependency mechanisms already provide.

### Status

`PROPERTY = COVERED`
`HOW_VARIATION = PARTLY_RECOVERED`
`DECISION_DISTINCT_HOW_GAP = POSSIBLE`
`CURRENT_CHANGE = NO`

---

## RV-002 — Proportional Evolution-Record Representation

### Earliest recovered appearance

Independent v0.3.6 critique of evolution-record burden.

### WHAT

Allow the **representation cost of an evolution occurrence** to scale with consequence/decision need instead of forcing every variation through the same rich record shape.

### WHY

This is not the same problem as finite-context/LITE adoption.

```text
FINITE_CONTEXT_ADOPTION
= cost of carrying/activating ENA in a Host

EVOLUTION_RECORD_WEIGHT
= cost of representing one variation/evolution occurrence after adoption
```

Failure:

```text
RECORDING_COST > VARIATION_VALUE
-> fewer variations represented
-> evolution starves under its own governance machinery
```

### Historical HOW branches

#### HOW-A — `LIGHT / STANDARD / FULL` record-weight modes

A historical concrete phenotype proposed different required-field sets.

Disposition: `RECOVERED_CANDIDATE / COUNT_AND_NAMES_NON_NORMATIVE`.

The three labels are presentation history, not proof that reality has three tiers.

#### HOW-B — Consequence-triggered progressive enrichment

Start with a minimal occurrence identity/hypothesis and require richer evidence/authority/settlement fields only when consequence or lifecycle transition makes them decision-relevant.

Disposition: `OPEN_CANDIDATE`.

#### HOW-C — Split occurrence log from later compilation/evaluation records

Use append-only minimal occurrence capture, then attach richer experiment/evaluation/integration records as those events actually happen.

Disposition: `OPEN_CANDIDATE`, structurally related to event sourcing and Memory Metabolism.

### Current surviving mechanisms

- LITE adoption prose;
- latent variation semantics;
- governance-must-pay-rent principle;
- #93 resource/evolution economics questions.

None by itself proves proportional **record** representation exists.

### Evidence needed

- inspect current v2 record/tool field burden against realistic low-consequence variations;
- determine whether progressive enrichment preserves required truth/lineage while materially reducing friction;
- field evidence that representation burden actually suppresses useful variation before standardizing a tier system.

### Status

`PROPERTY = PARTLY_COVERED`
`ORGAN = NOT_ESTABLISHED`
`HOW_VARIATION = RECOVERED`
`HOST_BINDING = OPEN`

---

## RV-003 — Constitution-to-Observable-Behavior Bridge

### Earliest recovered appearance

Independent critique: binding Constitution prose can coexist with valid machine records even if the Host does not actually live the property.

### WHAT

Provide concrete ways to map a semantic property to observable Host behavior/evidence without pretending the full Constitution is mechanically decidable.

### WHY

Failure:

```text
CONSTITUTION_PRESENT
+ EVOLUTION_RECORD_VALID
!= HOST_BEHAVIOR_CONFORMS_TO_PROPERTY
```

### Historical HOW branches

#### HOW-A — CON-ID -> observable-behavior/evidence checklist

Example historical proposal: each semantic ID points to at least one observable Host behavior or evidence question.

Disposition: `RECOVERED_CANDIDATE`.

This is a mapping aid, not a truth validator.

#### HOW-B — Host adapter/property mapping

For each Host, record which native mechanism realizes a property and how it can be observed/falsified.

Disposition: `OPEN / ALIGNED_WITH_CURRENT_HOST_BINDING_DIRECTION`.

#### HOW-C — Scenario/fixture-based semantic conformance

Test property semantics through decision-changing scenarios rather than formalizing prose into one policy language.

Disposition: `PARTLY_REEXPRESSED` in field-validation / language / deterministic fixture work.

#### HOW-D — Full policy-as-code Constitution

Disposition: `HISTORICAL_STRONG_ALTERNATIVE / LOW_CURRENT_FITNESS` because formalization may create false precision/false-BLOCK and large governance burden.

Keep as lineage; do not silently promote or erase.

### Current surviving mechanisms

- stable semantic IDs and concept map;
- Runtime Kernel cues;
- Host-binding research;
- language semantic conformance work;
- deterministic semantic fixtures in narrower domains.

### Evidence needed

Determine where an observable mapping changes real adoption/falsification decisions rather than becoming another checklist bureaucracy.

### Status

`PROPERTY = COVERED`
`REFERENCE_HOW = PARTIAL`
`HOST_BINDING = PARTIAL`
`EVIDENCE = OPEN`

---

## RV-004 — Host Extension Surface for Portable Schemas

### Earliest recovered appearance

Independent critique of strict closed schemas forcing local Hosts either to fork the schema or omit useful local state.

### WHAT

Preserve a portable ENA core record while allowing Host-local fields/metadata without misrepresenting those extensions as universal ENA semantics.

### WHY

Two symmetric failures exist:

```text
TOO_CLOSED
-> Host forks schema / drops useful data / lies to fit portable model

TOO_OPEN
-> interoperability and validation boundary dissolve
```

### Historical HOW branches

#### HOW-A — Globally open `additionalProperties`

Disposition: `RECOVERED_BUT_OVERBROAD`.

It solves extension friction by weakening the portable boundary everywhere.

#### HOW-B — Explicit namespaced extension object

Example shape:

```text
host_extensions:
  <host-or-schema-namespace>: {...}
```

Disposition: `OPEN_CANDIDATE`.

#### HOW-C — Sidecar Host metadata

Portable ENA record remains strict; local extension state lives in a separately versioned/linked Host record.

Disposition: `OPEN_CANDIDATE`.

#### HOW-D — Schema composition / governed extension profiles

Core schema + explicit Host/profile schema composed at validation time.

Disposition: `OPEN_CANDIDATE`.

### Evidence needed

Inspect real Host extensions and determine whether they need to travel with portable records, remain local, or influence ENA decisions. Selection should follow concrete interoperability failures, not generic extensibility preference.

### Status

`PROPERTY = UNDERREPRESENTED`
`HOW_VARIATION = RECOVERED`
`SELECTION = OPEN`

---

## RV-005 — State / Taxonomy Simplification Variations

### Earliest recovered appearance

Independent v0.3.6 critique proposed several deletions/merges/demotions.

### WHAT

Preserve candidate simplifications whenever a distinction may not earn behavioral independence.

### WHY

The anti-dissolution method protects useful concrete differences, but the opposite failure also exists:

```text
DISTINCTION_EXISTS
-> treated as permanent because it has a name/ID/schema slot
-> taxonomy burden survives after decision value disappears
```

Correct guard:

```text
IF_DISTINCTION_DOES_NOT_CHANGE_DECISION
-> CONSIDER MERGE / DEMOTION / OPTIONALIZATION
```

not automatic deletion.

### Historical candidate branches

- merge/demote `ARCHIVED` vs `RETIRED` if no lifecycle decision differs;
- test whether `PARTIAL` remains decision-distinct from `SUPPORTED + explicit tradeoffs`;
- test whether expression needs a universal explicit axis on every Host or can be represented by routing/event/loading mechanisms;
- demote optional Roles from a large normative-looking list to reference patterns if they do not change capability/authority behavior;
- demote long-tail Capability IDs that function only as vocabulary/aspiration;
- make conceptual references optional where machine presence creates fake precision without a resolver.

Disposition for all: `RECOVERED_SIMPLIFICATION_VARIATIONS / NOT_ACCEPTED_CHANGES`.

### Current evaluators

- Cardinality Discovery Guard;
- complexity-rent discipline;
- three-axis operational-rent research in #93;
- role/niche lifecycle research;
- anti-fake-precision evidence discipline.

### Evidence needed

For each distinction independently ask what decision, routing, evidence, lifecycle, or safety behavior changes. Do not use absence of current field use alone as deletion proof.

### Status

`VARIATION = RECOVERED`
`SELECTION = DEFERRED_TO_DECISION-SPECIFIC_EVIDENCE`

---

## RV-006 — Evolution Commons Inter-Agent Contract

### Earliest recovered appearance

Independent critique: migration packet schema + Commons prose do not implement inter-Agent discovery, task exchange, provenance transfer, conflict handling, or composition observation.

### WHAT

Concrete coordination/protocol HOWs by which heterogeneous agents can exchange evolution artifacts without one universal centralized society protocol.

### WHY

```text
PACKET_SCHEMA != DISCOVERY
PACKET_SCHEMA != TASK_LIFECYCLE
PACKET_SCHEMA != CONFLICT_RESOLUTION
PACKET_SCHEMA != COMPOSITION_OBSERVATION
```

### Historical HOW branches

- full universal inter-Agent protocol: historical strong alternative, not justified by evidence at the time;
- minimal migration packet only: existing but incomplete for active coordination.

### Later recovered/new HOW branches

#93 external harvesting has reintroduced decision-distinct mechanisms including:

- A2A Task / Message / Artifact lifecycle;
- Microsoft Agent Framework workflow/orchestration patterns;
- Anthropic multi-agent specialization/coordination evidence;
- opaque-agent interoperability and provenance questions.

### Disposition

`RECOVERED_AND_PARTLY_REEXPRESSED`.

This is not a missing Core property. It remains an operational HOW ecology with Host-dependent selection.

---

## RV-007 — Resource / Evolution-Cost Representation

### Earliest recovered appearance

Historical “energy/metabolism” critique and later Resource Metabolism discussions.

### WHAT

Make evolution consume observable scarce resources rather than exist as a cost-free conceptual loop.

### WHY

```text
EVOLUTION_WORK consumes tokens/time/compute/attention/coordination budget

if cost is invisible:
- governance can starve task work;
- task pressure can starve evolution;
- selection can favor cheap but harmful behavior;
- discretionary exploration can disappear silently.
```

### Historical HOW branches

- optional per-variation cost/budget fields;
- cumulative evolution-cost tracking;
- stronger cost-based metabolism/starvation controller.

### Later HOW branches

#93 now contains:

- Resource Budget model;
- Selection Pressure Map;
- obligation / maintenance / exploration budgets;
- resource-pressure experiments where outcomes are not statically derivable.

### Disposition

`RECOVERED_AND_REEXPRESSED`.

Important retention note: the old field-level cost representation remains one concrete HOW phenotype beneath the abstract `Resource Metabolism` label.

---

## RV-008 — Honest Unresolved Reference vs Fake Precise Lifecycle

### Earliest recovered appearance

`triggered_obligation_refs` critique: structurally present strings can satisfy a validator without proving target existence, authenticity, authority, or closure.

### WHAT

Represent unresolved obligations/effects/evidence honestly when the Host cannot resolve a precise reference.

### WHY

```text
REFERENCE_STRING_PRESENT
!= TARGET_EXISTS
!= TARGET_AUTHENTIC
!= TARGET_CURRENT
!= TARGET_SETTLED
```

### Historical HOW branches

#### HOW-A — Boolean `unresolved_obligation`

Disposition: `RECOVERED_MINIMAL_HONESTY_PATTERN / INSUFFICIENT_FOR_REAL_SETTLEMENT`.

It may be more honest than a fake precise reference when no resolver exists, but it cannot support rich commitment/settlement semantics.

#### HOW-B — Resolvable obligation lifecycle object

Later research produced the stronger Commitment/Settlement direction.

Disposition: `CURRENTLY_STRONGER_RESEARCH_BRANCH`.

#### HOW-C — WAIT / NARROW / ESCALATE on unresolved consequential reference

Disposition: `OPEN_COMPOSITION_PATTERN`.

### Status

`PROPERTY = COVERED`
`STRONGER_HOW_LINEAGE = ACTIVE`
`MINIMAL_FALLBACK_HOW = RETAINED_AS_VARIATION`

---

## RV-009 — Publication / Selective Legibility Boundary

### Earliest recovered appearance

Repository-publication lineage (#9/#10) removed maintainer-private storage coordinates while preserving non-secret research provenance and Current release identity.

### WHAT

Separate what must remain publicly/verifiably legible from what must remain private/restricted without treating redaction as provenance erasure.

### WHY

The repository event is project-process history, but it exposes an ENA-relevant structural tension already echoed by Selective Legibility and provenance-confidentiality research:

```text
TRUTHFUL_PROVENANCE != PUBLIC_DISCLOSURE_OF_EVERY_COORDINATE/PAYLOAD
REDACTION != EVENT_NEVER_EXISTED
```

### Historical HOW phenotype

- publish canonical engineering/release surface;
- remove private recovery coordinates from public metadata;
- retain private mirror only as abstract non-canonical dependency;
- preserve decision/history identity while changing visibility.

### Current relation

#89 includes provenance confidentiality / restricted evidence dereference and selective-legibility research, but this concrete publication phenotype was not explicitly retained as an organ example.

### Disposition

`PROJECT-PROCESS_EXAMPLE / CANDIDATE_REFERENCE_HOW_FOR_SELECTIVE_LEGIBILITY`.

Do not generalize from repository publication to all Agent privacy/deletion problems.

---

## RV-010 — Fresh-Session Evolution Evidence Boundary

### Earliest recovered appearance

v0.3.5 WorkBuddy field tracker #61.

### WHAT

Keep separate:

```text
PERSISTED
SAME_SESSION_READBACK
FRESH_SESSION_AUTOLOAD
NATURAL_SALIENCE
NATURAL_APPLICATION
FULL_OUTCOME-BEARING_EVOLUTION_CYCLE
```

### WHY

A guided first adoption can prove persistence/configuration while leaving the actual operational value proposition untested.

### Historical evidence phenotype

#61 explicitly tightened claims:

- guided adoption, not blind validation;
- same-session readback != fresh-session autoload;
- future salience/application unproven;
- recovery artifact != restore proof;
- one language user != semantic-equivalence proof;
- discovery/persistence/wake/observe/closure != full vary/experiment/select/integrate/prune/recombine cycle.

### Current relation

These distinctions were largely absorbed by #70/#90/#94 and the `WRITTEN -> ... -> APPLIED` methodology, so this is not a new organ gap.

### Disposition

`HISTORICAL_EVIDENCE_BOUNDARY / ABSORBED_BUT_EXPLICITLY_RETAINED`.

---

## Current disposition matrix

| Variation | Current disposition | Do next? |
|---|---|---|
| RV-001 Verification Boundary | partly reexpressed; possible distinct HOW gap | compare with Evidence Envelope / validator UX |
| RV-002 Proportional Evolution Record | recovered, organ not established | inspect current record/tool burden; external HOW search if distinct gap remains |
| RV-003 Constitution -> Observable Behavior | partial Host-binding direction | map existing Host/fixture mechanisms before inventing policy engine |
| RV-004 Host Extension Surface | underrepresented | inspect real schema/Host extension needs, then external pattern search |
| RV-005 Simplification Variations | retained dormant candidates | only test when a distinction affects current engineering/release decision |
| RV-006 Commons Inter-Agent Contract | reexpressed in #93 | continue A2A/coordination HOW mapping |
| RV-007 Resource Cost | reexpressed in #93 | retain field-level cost HOW; evidence before standardizing |
| RV-008 Honest Unresolved Reference | stronger Commitment/Settlement branch active | compose fallback with resolver/fencing work |
| RV-009 Selective Legibility Publication Pattern | concrete historical example | map only if privacy/provenance branch becomes active |
| RV-010 Fresh-Session Evidence Boundary | absorbed by current evidence methodology | preserve as field lineage |

The table is a routing snapshot, not a priority ranking and not a closed inventory.

## Archaeology closure posture

This pass has not proven historical completeness.

It has established:

1. major historical Issue families are broadly represented in #89/#90–#94;
2. a lower-level class of dormant concrete variations was missing from the active retention map;
3. these variations are now durable again without being promoted into Current or selected as winners.

Continue archaeology while another bounded pass can still expose a decision-distinct lost lineage.

> **Recover variation before selecting variation.**
