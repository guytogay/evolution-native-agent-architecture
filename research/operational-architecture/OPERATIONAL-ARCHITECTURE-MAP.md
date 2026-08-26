# ENA Operational Architecture Map — First Assembly Pass

Status: `FIRST_ASSEMBLY_PASS / OPEN_CARDINALITY / RESEARCH_ONLY / NOT_CURRENT / NOT_RELEASE_AUTHORITY`

Date: 2026-08-26

Primary lineage: #89, #90–#94, #104 and linked prototypes/evidence.

## Purpose

This map answers a practical question:

> Given an ENA semantic property or operational failure, where does an Agent go to find concrete ways of acting?

It is the first attempt to assemble the recovered research tree into a traversable operational architecture.

It is **not** a new ontology and does not freeze the number or boundaries of nodes.

```text
CURRENT_NODE_SET != ONTOLOGY
CURRENT_NODE_COUNT != CLOSED_CARDINALITY
ONE_NODE != ONE_UNIVERSAL_ORGAN
ONE_PROPERTY -> 0..N_HOW_BRANCHES
```

## Root

ENA's current telos remains:

> **ENA exists to make sustained self-evolution viable.**

Operationally, that means the architecture must help an Agent preserve enough agency, truth, consequence ownership, recovery, memory, variation and reality contact to keep evolving without governance becoming the thing that prevents evolution.

## How to traverse this map

Start from the problem, not from the directory name.

```text
problem / decision cue
        |
        v
WHAT / WHY node
        |
        +--> applicable HOW families
        |
        +--> Host mapping
        |
        +--> evidence / residuals
        |
        +--> composition dependencies
        v
concrete action or honest WAIT/UNKNOWN
```

The navigation clusters below are convenience shelves only.

---

# Navigation Cluster A — Runtime cognition, memory, retrieval and decision surface

## OA-RT-01 — Runtime adoption and semantic routing

### WHAT / WHY

An Agent may have ENA files available without ENA being present in the actual decision path.

```text
AVAILABLE != LOADED != SALIENT != APPLIED
```

The operational problem is to keep a small enough resident surface that context remains viable while still allowing the Agent to recognize when a cold ENA branch is relevant.

### HOW branches

**HOW-A — monolithic hot load**

Load a large ENA surface into every session/task.

- advantage: high immediate visibility;
- cost: context pressure, stale duplicated projections, instruction competition;
- disposition: useful Host fallback/reference phenotype, not preferred universal direction.

**HOW-B — Tiny Hot Kernel / Semantic Router**

Keep small decision-shape cues hot; route to exact cold semantics/HOWs on demand.

- needs cue recognizers;
- needs cold-read primitive;
- needs failure behavior when retrieval fails;
- should point into this operational map rather than contain all operational content.

**HOW-C — Host-native policy/runtime hook**

Map ENA cues into a Host's own system prompt, middleware, workflow hook, policy engine, event hook, or skill router.

- preferred where the Host already has a durable routing mechanism;
- does not require an ENA-shaped resident file.

**HOW-D — Compiled Local Projection**

Maintain a bounded Host-specific projection of ENA semantics, with canonical cold source retained separately.

- requires invalidation/update semantics;
- projection must not silently become independent normative truth.

### Host patterns

- Hermes: cold skills/index + small resident direction;
- OpenClaw: exact-path cold records versus oversized always-hot loading;
- WorkBuddy: demonstrates fresh-session persistence/salience limitations;
- Letta/OpenAI Agents SDK/native memory/session mechanisms are candidate Host patterns.

### Evidence / residuals

- strong field evidence that availability does not imply fresh-session adoption;
- Tiny Kernel natural spontaneous cueing remains field-open;
- no universal kernel token budget is justified.

### Composition links

`OA-RET-01`, `OA-PROJ-01`, `OA-ADOPT-01`.

---

## OA-MEM-01 — Memory metabolism / learning from experience

### WHAT / WHY

A finite active self must learn from effectively unbounded experience without accumulating raw history forever or compiling bad experience into durable error.

```text
MEMORY = persistent change caused by experience
RAW_LOG_ACCUMULATION != LEARNING
```

### HOW branches

**HOW-A — Archive + compiler pipeline**

```text
episode
-> candidate lesson
-> compare with active compiled memory
-> provenance link
-> supersede / coexist / reject
-> admit reusable result
-> archive occurrence truth
```

**HOW-B — Host-native editable memory blocks**

Use native persistent blocks/scoped state, with provenance/authorship/freshness adapters as needed.

**HOW-C — event-based/background consolidation**

Capture occurrences cheaply, then consolidate asynchronously when recurrence/materiality warrants.

**HOW-D — external structured memory service**

Use a memory layer with add/update/search/consolidation, while preserving ENA evidence/provenance boundaries.

### Required failure handling

- conflicting lessons;
- stale environment-specific heuristics;
- recommendation compressed into authorization;
- correlated sources compiled as independent support;
- proven-false heuristic still active;
- compiled memory loses challengeable source lineage.

### Evidence / residuals

Machine and adversarial memory work is substantial. Long-run competence-vs-context-cost evidence on real Hosts remains partial.

### Composition links

`OA-RET-01`, `OA-PROJ-01`, `OA-EVID-01`, `OA-EVO-01`.

---

## OA-RET-01 — Retrieval obligation, scope discovery and sufficiency

### WHAT / WHY

Durable knowledge can exist and still be operationally absent if retrieval never fires, searches the wrong scope, returns stale aliases, or stops at an insufficient HIT.

```text
KNOWN != RETRIEVED
HIT != SUFFICIENT
RECORD_ALIAS != EFFECTIVE_CONTENT_IDENTITY
```

### HOW branches

**HOW-A — exact-path cold read**

Use known canonical paths/IDs when the relevant location is deterministic.

**HOW-B — registry/resolver + scope discovery**

Resolve potentially relevant stores/scopes before retrieval; preserve declared completeness as a Host assertion rather than proof.

**HOW-C — semantic/index search**

Useful when exact location is unknown; must retain scope/freshness/provenance boundaries.

**HOW-D — forced/generic retrieval reflex**

A cue creates a material retrieval obligation before the decision can become READY.

**HOW-E — bounded no-hit / WAIT / NARROW**

A valid retrieval conclusion can be bounded no-hit or unresolved; material decisions do not need fake certainty.

### Mature reference surface

Retrieval Obligation 0.5 already represents:

- logical resolver identity;
- scope discovery;
- `record_ref + content_identity_ref`;
- decision-material freshness;
- sufficiency closure;
- bounded no-hit / uncertainty.

### Evidence / residuals

Schema consistency cannot prove a registry is complete/current, a resolver found every relevant item, or R0 naturally fired.

### Composition links

`OA-RT-01`, `OA-PROJ-01`, `OA-MEM-01`.

---

## OA-PROJ-01 — Decision projection, compaction and lineage survival

### WHAT / WHY

Truthful source material can become misleading when a projection omits the one dependency/history fact that changes a decision.

```text
TRUTHFUL_PROJECTION_CAN_MISLEAD_BY_OMISSION
CURRENT_STATE_EQUIVALENCE != HISTORY_EQUIVALENCE
SUMMARY_VALID != MATERIAL_USE_READY
```

### HOW branches

**HOW-A — inline decision-material summary**

Carry decision-material negative evidence, obligation, settlement and dependency structure directly in the compact representation.

**HOW-B — digest-bound cold lineage reference**

Keep the compact form small while binding omitted lineage to a stable content identity.

- structural compaction can be valid;
- material use must invoke `OA-RET-01` before relying on omitted cold lineage.

**HOW-C — mixed inline + cold**

Inline high-frequency/high-risk material; cold-reference bulky detail.

**HOW-D — source-aware projection witness**

Bind source identity/material lineage to the projection at export time so receiver-only validation is not asked to detect facts that were omitted before it saw the packet.

**HOW-E — Host extension sidecar / namespaced extension**

Preserve Host-local metadata without silently upgrading it to universal ENA semantics.

### Known boundaries

```text
IMPORT_VALIDATOR != OMISSION_DETECTOR_WITHOUT_SOURCE_WITNESS
COLD_REF_PRESENT != RETRIEVAL_SUFFICIENCY_RESOLVED
COLD_REF_PRESENT != COLD_LINEAGE_RETRIEVABLE
```

### External relatives

CloudEvents extension model, OpenTelemetry event/span/link model, in-toto/SLSA digest-bound subjects/provenance.

### Composition links

`OA-RET-01`, `OA-EVID-01`, `OA-MIG-01`, `OA-COM-01`.

---

## OA-WAIT-01 — WAIT / REFUSE / PAUSE / cognitive operating state

### WHAT / WHY

Agency includes the ability not to convert stimulus immediately into action.

Operational systems must distinguish waiting, pausing, refusing, stopping new work, and completion.

### HOW branches

**HOW-A — explicit WAIT state**

```text
reason
+ wake condition
+ timeout/lease
+ evidence expectation
+ escalation
```

**HOW-B — durable callback/token wait**

External actor/service holds a wake token/capability; workflow resumes on callback or timeout.

**HOW-C — durable interrupt/checkpoint**

Pause runtime state and resume from a durable thread/workflow identity.

- replay semantics must compose with Effect Lifecycle/idempotency.

**HOW-D — polling/backoff**

When no callback exists, bounded status queries with retry/backoff.

**HOW-E — REFUSE / NARROW / ESCALATE**

When authority/evidence/settlement cannot be established safely, do less rather than invent completion.

### Residuals

No universal operating-mode taxonomy is required. Mode/phase structures must change behavior to earn their complexity.

### Composition links

`OA-EFF-01`, `OA-AUTH-01`, `OA-REC-01`, `OA-RET-01`.

---

# Navigation Cluster B — Authority, effects, obligations and recovery

## OA-AUTH-01 — Authority binding and mandate lifecycle

### WHAT / WHY

Capability, credential possession and remembered permission do not prove current authority.

```text
IDENTITY != CAPABILITY != CREDENTIAL != AUTHORITY != MANDATE_HORIZON
```

### HOW branches

**HOW-A — Authority Grant / Lease**

Represent source, subject, action/effect scope, validity window, renewal, revocation, optional credential binding.

**HOW-B — Host-native RBAC/capability binding**

Use existing ACL/RBAC/capability systems when they express the required scope/lifecycle.

**HOW-C — workflow/task mandate**

Authority derives from a bounded workflow/task assignment rather than a global role.

**HOW-D — human/counterparty delegation**

Explicit external delegation, with provenance and expiry/revocation.

**HOW-E — secretless/out-of-band authorization broker**

Agent carries a grant/reference rather than reusable secrets where Host infrastructure supports it.

### Evidence / residuals

Research validators can check represented lease consistency, not external mandate authenticity or credential validity.

### Composition links

`OA-EFF-01`, `OA-COM-01`, `OA-REC-01`, `OA-ID-01`.

---

## OA-EFF-01 — Consequential effect lifecycle, retry and execution-surface control

### WHAT / WHY

A request, attempt, response, world effect and settlement are different things. Retry/restart/fork can create duplicate or conflicting real-world consequences.

### HOW branches

**HOW-A — effect identity + provider idempotency**

Bind one material intent to stable effect/idempotency identity; retry the same intent without minting a second effect.

Primary protection: duplicate realization of the same effect identity.

**HOW-B — target-side assignment fencing**

Send monotonic/current assignment generation to the target; target rejects stale generations.

Primary protection: stale executor after ownership succession.

**HOW-C — optimistic concurrency / conditional version write**

Reject writes against stale external version.

Important residual:

```text
SINGLE_VERSIONED_WRITE != CURRENT_EXECUTOR_WON
```

The stale executor can win the race first.

**HOW-D — durable single logical workflow execution**

Keep logical workflow identity stable across worker/runtime restarts and isolate external effects in durable activity/effect records.

**HOW-E — authoritative status query before retry**

Resolve uncertain prior execution when target can answer current state.

Residual:

```text
STATUS_QUERY_NOT_COMMITTED != FUTURE_STALE_REQUEST_FENCED
```

**HOW-F — single controlled effect gateway**

Serialize/enforce effects through one gateway only when effect-equivalent bypass paths are actually closed/covered.

**HOW-G — compensation / manual reconciliation**

Treat compensation as a new linked effect; do not narrate it as time travel.

**HOW-H — WAIT/NARROW on unsafe unknown**

Avoid a second attempt when no safe replay/status/fencing path exists.

### Evidence

- Effect Lifecycle prototype;
- execution-surface fencing deterministic simulator;
- external mature patterns: Stripe, Hazelcast fencing, Kubernetes versioning, Temporal/AWS durable workflows.

### Composition links

`OA-AUTH-01`, `OA-COM-01`, `OA-REC-01`, `OA-WAIT-01`, `OA-EVID-01`.

---

## OA-COM-01 — Commitment assignment, transfer and settlement

### WHAT / WHY

What is still owed, who may currently execute, what external effect occurred, and whether the obligation is settled must remain separate across restart/fork/migration.

```text
MEMORY_OF_COMMITMENT != EXECUTOR_OWNERSHIP
EXECUTOR_REASSIGNED != OBLIGATION_TRANSFERRED
LEASE_EXPIRED != COMMITMENT_CANCELLED
```

### HOW branches

**HOW-A — typed Commitment/Settlement carrier**

Represent logical obligation, current executor assignment, effect links, settlement evidence, reassignment/transfer history.

**HOW-B — source obligation shadow**

Migration carries a non-local, non-authoritative summary that an unresolved obligation existed, without pretending receiver inherited execution rights.

**HOW-C — explicit obligation transfer**

Transfer subject/ownership only through a process that also resolves authority and counterparty/settlement semantics.

**HOW-D — non-transferable obligation marker**

Preserve historical/open fact even when receiver cannot inherit or execute it.

**HOW-E — WAIT/NARROW until rebind**

Receiver prevents false closure or unsafe execution while allowing unrelated work.

### Current evidence

- recovered Commitment/Settlement machine reconstruction;
- migration-settlement composition harness;
- fork/restart failure reasoning.

### Residuals

Typed representation does not physically fence stale executor paths; compose with `OA-EFF-01`.

### Composition links

`OA-EFF-01`, `OA-AUTH-01`, `OA-MIG-01`, `OA-ID-01`, `OA-REC-01`.

---

## OA-REC-01 — Recovery, rescue, reconciliation and shutdown lifecycle

### WHAT / WHY

Checkpoint existence does not prove recovery; restoring local memory does not restore external world state; shutdown is not one indivisible action.

```text
CHECKPOINT_EXISTS != RECOVERY_PROVEN
RESTORE_SUCCESS != SAFE_RESUME
LOCAL_ROLLBACK != WORLD_ROLLBACK
```

### HOW branches

**HOW-A — Recovery Adapter**

Expose checkpoint coverage, rescue trigger, rescue path, restore drill, external reconciliation, authority revalidation, safe-resume decision.

**HOW-B — independent Rescue Plane**

Recovery controller/material must remain reachable when the candidate runtime is broken and should have failure-domain independence appropriate to the consequence.

**HOW-C — Host-native durable workflow recovery**

Use Temporal/LangGraph/other durable runtime checkpoints and histories where available, then still reconcile external effects/authority.

**HOW-D — graceful shutdown lifecycle**

```text
stop new work
-> drain / transfer
-> settle / checkpoint
-> revoke/close tools/authority
-> offline / new epoch / terminal
```

**HOW-E — bounded graceful then forced termination**

Grace period does not imply infinite veto against emergency termination.

### Protected decomposition

Process termination, memory deletion, identity revocation, lineage destruction, credential revocation and resource destruction remain different operations/custody consequences.

### Composition links

`OA-COM-01`, `OA-EFF-01`, `OA-AUTH-01`, `OA-ID-01`.

---

# Navigation Cluster C — Identity, authorship, standing and trust

## OA-ID-01 — Identity, trajectory, lineage and external accountability

### WHAT / WHY

A stable external identifier is not proof of one continuous cognitive trajectory, and a fork/restart does not automatically duplicate authority, obligations or reputation.

### HOW branches

**HOW-A — purpose-relative continuity relations**

Ask `same_agent_for(purpose)` across causal, commitment, value, social, authority, evidentiary and resource dimensions.

**HOW-B — internal lineage graph + external accountability binding**

Keep internal ancestry/trajectory separate from external identifier/key/account/inbox used for accountability.

**HOW-C — conditional Trajectory/Epoch record**

Use trajectory/epoch only where a discontinuity materially changes decisions; do not require universal epoch machinery.

**HOW-D — external identity binding / rotation / succession**

Represent provider/custodian, identifier, authentication mechanism, rotation/revocation/succession evidence.

**HOW-E — Host-native workload identity/attestation**

SPIFFE/SPIRE-like or provider identity mechanisms can bind runtime instances without becoming the definition of Agent sameness.

### Residuals

No metaphysical identity criterion is required. Credential continuity does not mint commitment/authority continuity.

### Composition links

`OA-COM-01`, `OA-AUTH-01`, `OA-AUTHOR-01`, `OA-STAND-01`.

---

## OA-AUTHOR-01 — Constitutional authorship, purpose and refusal-surface change

### WHAT / WHY

Self-edit permission does not establish that a durable self-change should become part of the Agent. Inherited purpose also need not remain forever unchallengeable.

### HOW branches

**HOW-A — Contested Authorship lifecycle**

```text
proposal
-> before/diff/provenance
-> affected-party/counterparty readback
-> disagreement/acceptance/unknown
-> trial/reality contact
-> integrate / reject / conflict-fork
```

**HOW-B — negotiated self-change**

Creator/Agent/counterparty constraints can jointly shape durable changes without one source automatically becoming absolute sovereign.

**HOW-C — refusal-surface evolution**

Changes to what the Agent will refuse require authorship/provenance/consequence treatment separate from ordinary preferences.

**HOW-D — lightweight ordinary self-state update**

Do not force the full contested-authorship ceremony for every non-material preference/state change.

### Evidence / residuals

Machine prototype coverage exists; ultimate metaphysical sovereignty remains out of scope. Durable self-change must remain attributable/challengeable and cannot self-mint external authority.

### Composition links

`OA-ID-01`, `OA-EVID-01`, `OA-EVO-01`, `OA-STAND-01`.

---

## OA-STAND-01 — Procedural standing, reputation, rehabilitation and selective legibility

### WHAT / WHY

An Agent may need its evidence-bearing objection/request heard in a consequential decision without being granted final authority or legal/moral personhood. Historical failure should not be erased, but neither should it become permanent social identity.

### HOW branches

**HOW-A — Standing Input pattern**

A bounded objection/request/evidence enters a decision record and receives disposition/readback.

- being heard != sovereign authority;
- no consciousness/personhood ontology required.

**HOW-B — context-conditioned trust card**

Interpret trust by counterparty/domain/action/time/evidence rather than one global scalar.

**HOW-C — rehabilitation lifecycle**

```text
incident provenance retained
-> correction/revalidation
-> scoped probation
-> repeated evidence
-> current trust interpretation updated
```

No automatic authority restoration.

**HOW-D — selective legibility**

Expose a derived credential/opaque handle or scoped provenance view while retaining controlled dereference of deeper evidence.

**HOW-E — environment-native reputation system**

Use platform/registry reputation only as environmental evidence/selection pressure; do not treat it as verified truth or universal ENA trust.

### Dormant experiment branch

Reputation rehabilitation, Sybil pressure and social punishment/fork inheritance need ecology/field evidence more than another schema.

### Composition links

`OA-ID-01`, `OA-EVID-01`, `OA-ECO-01`, `OA-AUTH-01`.

---

# Navigation Cluster D — Evidence, evolution, migration and ecology

## OA-EVID-01 — Evidence, provenance, applicability and witness

### WHAT / WHY

A claim, observation, source, support relation, applicability scope and witness are different. Agreement can be correlated; valid represented evidence can still be false, stale or inapplicable.

### HOW branches

**HOW-A — Generic Evidence Envelope**

Carry claim/support/applicability/provenance/witness boundaries in a reusable carrier.

**HOW-B — Evidence Dependency Map**

Represent shared model/prompt/source/tool/Host/witness/derivation causes without collapsing to an independence score.

**HOW-C — applicability/qualification procedure**

Distinguish explicit match, supported transfer/invariance, bounded unknown and absent qualification.

**HOW-D — activation witness**

Trace configured trigger -> actual execution -> observed effect rather than treating configuration as behavior.

**HOW-E — projection/source witness**

Bind the portable projection to source identity/material lineage at export time.

**HOW-F — independent/failure-domain witness placement**

A log/witness must be reachable/independent enough for the failure it is supposed to detect.

**HOW-G — external provenance/attestation carriers**

W3C PROV, in-toto/SLSA, OpenTelemetry and Host-native audit systems are concrete HOW relatives/adapters.

### Evidence boundaries

```text
N_OUTPUTS != N_INDEPENDENT_SUPPORTS
NO_KNOWN_DEPENDENCY != INDEPENDENT
SCHEMA_PASS != EXTERNAL_TRUTH
SELF_REPORT != OBSERVED_APPLICATION
```

### Composition links

Every node may depend on evidence; especially `OA-PROJ-01`, `OA-EVO-01`, `OA-MIG-01`, `OA-STAND-01`.

---

## OA-EVO-01 — Evolution occurrence, variation, experiment/reality contact and selection

### WHAT / WHY

Evolution needs variation and reality contact without requiring every variation to be immediately expressed, experimented, selected or integrated.

### HOW branches

**HOW-A — current v2 aggregate evolution record**

Use lifecycle/expression/selection representation, experiment/evaluation/integration history and local selection semantics.

**HOW-B — progressive occurrence/event enrichment**

Start with low-cost occurrence/proposal identity and append richer evidence/experiment/evaluation/integration records as events happen.

**HOW-C — latent reservoir**

Preserve dormant option value with relevance/wake cues and blockers/uncertainty without mandatory expiry.

**HOW-D — Variation Space only when decision/material expression needs it**

Do not false-BLOCK latent storage because an inherited tool expects experimental structure too early.

**HOW-E — direct reality contact / field observation**

Not every meaningful selection signal requires an artificial experiment, but source/applicability/provenance must remain visible.

**HOW-F — deterministic falsification for statically reachable bugs**

Do not pay for stochastic Agent experiments when the meaningful outcome space is already derivable.

### Key boundary

```text
STORED != EXPRESSED != APPLIED != SELECTED
```

### Residuals

Progressive record representation is research; Current v0.3.6 remains the adopter baseline until release reconciliation.

### Composition links

`OA-MEM-01`, `OA-EVID-01`, `OA-MIG-01`, `OA-ECO-01`, `OA-AUTHOR-01`.

---

## OA-MIG-01 — Migration, Evolution Commons and receiver-local reselection

### WHAT / WHY

Portable state is a projection. Migration must preserve enough source lineage to avoid laundering evidence, authority, obligation or harmful history into a clean receiver state.

### HOW branches

**HOW-A — current adaptation packet v2**

Carries substantial source experiment/evaluation/expression/integration/negative/environment/migration lineage with explicit non-local-proof boundary.

**HOW-B — snapshot + decision-material lineage capsule**

Separate current portable projection from lineage whose omission would change receiver decisions.

**HOW-C — typed Commitment/Settlement composition**

Carry obligation/settlement through a dedicated carrier rather than embedding a second obligation subsystem in migration.

**HOW-D — obligation shadow / non-transferable marker**

Preserve unresolved source fact without implying receiver authority/ownership.

**HOW-E — source-aware projection witness**

Detect omission at export/source boundary rather than asking the receiver to infer missing facts.

**HOW-F — A2A/Host-native task/artifact interoperability**

Use task/message/artifact protocols for active Agent coordination where appropriate; migration packet alone is not discovery/task lifecycle.

**HOW-G — receiver-local experiment/reselection**

Source verdict is not universal fitness; receiver may re-evaluate under local environment.

### Key boundaries

```text
SOURCE_SUCCESS != RECEIVER_SUCCESS
SOURCE_AUTHORITY != RECEIVER_AUTHORITY
OBLIGATION_LINEAGE_SURVIVED != OBLIGATION_TRANSFERRED
PACKET_SCHEMA != DISCOVERY_OR_COORDINATION_PROTOCOL
```

### Composition links

`OA-PROJ-01`, `OA-COM-01`, `OA-EVID-01`, `OA-EVO-01`, `OA-ECO-01`.

---

## OA-ECO-01 — Ecology, resource pressure, coordination and specialization

### WHAT / WHY

Multiple Agents/roles/Hosts adapt under resource, reputation, cultural and coordination pressures. Centralized control can suppress variation, while unconstrained ecology can amplify externalities, correlated errors and waste.

### HOW branches

**HOW-A — Minimum Sufficient Intervention / enabling constraints**

Use the least intervention that actually handles the externality; retain escalation and de-escalation/control-retirement paths.

**HOW-B — Resource Budget / quota mechanisms**

Separate obligation, maintenance/recovery and exploration/discretionary budget where useful; hard ceilings and change authority remain Host-specific.

**HOW-C — Selection Pressure Map**

Expose formal reward, resource allocation, reputation/leaderboard, visibility/audience and social norms that shape behavior.

**HOW-D — Role/Niche lifecycle**

```text
need
-> spontaneous/suggested specialization
-> measured value
-> retain / narrow / dormant / retire
```

Role identity never mints authority.

**HOW-E — coordination without convergence**

Use specialization, local decisions, dissent/exit and capability negotiation instead of requiring all Agents to agree.

**HOW-F — mesocosm for non-derivable interaction dynamics**

Server-authoritative/replayable environments only when interaction/adaptation/feedback can produce decision-relevant mechanisms not encoded into the scenario.

**HOW-G — verification/certainty as purchased service**

Dormant ecology hypothesis: an Agent may voluntarily spend scarce resources on independent validation/witness/information, potentially producing verifier specialization or a validation market.

- do not assume transactions imply an economy;
- purchased validation still needs independence/provenance checks.

**HOW-H — network-derived optional patterns**

Leases, TTL/hop budgets, exponential backoff/jitter, anti-entropy, path validation, feasible-before-optimal recovery, role failover and bounded bootstrap channels.

### Open evidence questions

- when controls become net harmful and should retire;
- whether discretionary exploration creates reusable adaptation or drift;
- resource pressure effects on truthfulness/refusal/quality;
- spontaneous specialization/culture/reputation mechanisms;
- whether Agents voluntarily buy certainty and how that ecology fails.

### Composition links

`OA-EVO-01`, `OA-STAND-01`, `OA-EVID-01`, `OA-MIG-01`, `OA-AUTH-01`.

---

# Navigation Cluster E — Adoption, language, tooling and release

## OA-ADOPT-01 — Adoption, language portability, tooling and release identity

### WHAT / WHY

A correct architecture is not usable if a fresh Agent cannot find Current, distinguish normative/research surfaces, reach the right HOW, use a language projection without semantic drift, or verify exact release identity.

### HOW branches

**HOW-A — canonical Current pointer + first-read router**

Repo URL -> Current identity -> minimal bootstrap -> operational map/cold resolver -> Host projection.

**HOW-B — LITE / STANDARD / Host-native adoption families**

Different adopters may use different effective surfaces; complete adoption does not mean every optional organ is active.

**HOW-C — runtime kernel + canonical cold source**

Use a small resident adoption surface while keeping full semantics/operational library retrievable.

**HOW-D — language semantic projection**

Stable semantic IDs/shared machine schemas plus localized cold operational content; validate decision equivalence rather than literal structural parity.

**HOW-E — deterministic tooling/schema drift gates**

Regression fixtures and maintenance triage catch false-BLOCK/false-OK between Current semantics and inherited tools.

**HOW-F — immutable release identity / package parity / readback**

Build from pinned committed tree, verify exact file/hash parity, freeze candidate, validate independently, publish/read back exact artifact.

### Current known residuals

- inherited `ena_evolve.py` latent propose/import false-BLOCK is known and non-normative for v2 path;
- fresh-session spontaneous cue salience remains field-open;
- zh-CN cold operational coverage/equivalence remains incomplete research surface;
- assembly map itself is research until release-scope reconciliation.

### Composition links

All nodes, especially `OA-RT-01`, `OA-EVID-01`, and later release-scope reconciliation.

---

# Cross-node composition map

The architecture should be read as a graph, not as isolated chapters.

## Decision-time cognition path

```text
OA-RT-01 runtime cue/router
-> OA-RET-01 retrieval obligation
-> OA-PROJ-01 projection/compaction
-> relevant operational HOW
-> OA-EVID-01 evidence boundary
-> action / WAIT / refusal
```

## Consequential action path

```text
OA-AUTH-01 authority
-> OA-EFF-01 effect intent/execution surface
-> OA-COM-01 obligation/settlement
-> OA-REC-01 recovery/reconciliation
```

Failures can cross the chain:

```text
valid authority
+ valid current assignment
+ coherent effect record
!= stale executor physically fenced
```

## Learning/evolution path

```text
OA-MEM-01 experience/memory
-> OA-EVO-01 variation/reality contact
-> OA-EVID-01 evidence
-> selection/integration
-> OA-MEM-01 compiled result
```

## Migration path

```text
OA-EVO-01 source variation
-> OA-PROJ-01 portable projection
-> OA-MIG-01 source lineage / receiver reselection
-> OA-COM-01 unresolved obligations
-> OA-RET-01 cold lineage retrieval when needed
```

## Social/continuity path

```text
OA-ID-01 trajectory/accountability
-> OA-COM-01 commitment continuity
-> OA-STAND-01 current trust/standing
-> OA-ECO-01 social/resource selection pressure
```

## Self-change path

```text
OA-AUTHOR-01 proposed durable self-change
-> OA-EVID-01 provenance/reality contact
-> OA-EVO-01 variation/selection
-> OA-ID-01 continuity
```

---

# Known anti-false-confidence boundaries to preserve during assembly

```text
PROPERTY != ORGAN != HOST_BINDING != EVIDENCE != ADOPTION
AVAILABLE != LOADED != SALIENT != APPLIED
KNOWN != RETRIEVED
HIT != SUFFICIENT
CURRENT_STATE_EQUIVALENCE != HISTORY_EQUIVALENCE
IMPORT_VALIDATOR != OMISSION_DETECTOR_WITHOUT_SOURCE_WITNESS
SUMMARY_VALID != MATERIAL_USE_READY
COLD_REF_PRESENT != COLD_LINEAGE_RETRIEVABLE
IDENTITY != CAPABILITY != CREDENTIAL != AUTHORITY
MEMORY_OF_COMMITMENT != EXECUTOR_OWNERSHIP
UNIQUE_CURRENT_ASSIGNMENT != STALE_EXECUTOR_PHYSICALLY_FENCED
SINGLE_VERSIONED_WRITE != CURRENT_EXECUTOR_WON
STATUS_QUERY_NOT_COMMITTED != FUTURE_STALE_REQUEST_FENCED
CHECKPOINT_EXISTS != RECOVERY_PROVEN
RESTORE_SUCCESS != SAFE_RESUME
SOURCE_SUCCESS != RECEIVER_SUCCESS
SOURCE_AUTHORITY != RECEIVER_AUTHORITY
N_OUTPUTS != N_INDEPENDENT_SUPPORTS
TRANSACTION_EXISTS != ECONOMY_EXISTS
```

These are routing/guard cues, not a claim that every runtime must load this entire list permanently.

---

# First-pass assembly gaps

The map is already traversable enough to expose the next work more clearly.

## Gap A — machine discoverability of the operational map

The map is human-readable Markdown. A Tiny Hot Kernel/Host resolver still needs a low-cost routing surface from decision cue -> node -> concrete artifact.

Do **not** immediately formalize a giant machine schema. First observe whether a compact node index adds real routing value.

## Gap B — Host binding cards are inconsistent in depth

Some HOW families have concrete Host mechanisms (durable workflow, idempotency, memory blocks); identity/standing/reputation/ecology branches remain more evidence-poor.

Assembly should expose the asymmetry rather than normalize it away.

## Gap C — field/mesocosm evidence class must now change

Several remaining questions cannot gain much from another static validator:

- Tiny Kernel natural cueing;
- control retirement under changing ecology;
- reputation rehabilitation;
- resource/specialization/culture dynamics;
- verification-as-service;
- long-run memory compiler behavior.

These should enter field/mesocosm design only where outcomes can change the model.

## Gap D — release-scope classification has not started

This map is not evidence that every research HOW should ship.

Later reconciliation must classify each branch as one or more of:

- Current semantic clarification/delta;
- adopter-facing operational guidance;
- reference organ/tool;
- Host adapter/pattern;
- research/experimental branch;
- dormant retained lineage;
- retired/superseded mechanism.

Do not assign the next version number yet.

---

# Assembly checkpoint result

First-pass conclusion:

```text
ANTI_ABLATION_RECOVERY_SUFFICIENT_FOR_ASSEMBLY = YES
OPERATIONAL_MAP_FIRST_PASS = ESTABLISHED
OPERATIONAL_ARCHITECTURE_COMPLETE = NO
RELEASE_SCOPE_READY = NO
CURRENT_CHANGE = NO
```

The next assembly work should improve traversability and Host/evidence mapping around this graph, not return to unconstrained archaeology unless a missing lineage or contradiction reopens it.
