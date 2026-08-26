# ENA Operational Architecture Reference Pointer Matrix

Status: `EXECUTION_ROUTING_SURFACE / BREADTH_PASS_2 / OPEN_CARDINALITY / RESEARCH_ONLY / NOT_CURRENT`

Date: 2026-08-27

Parent map: `OPERATIONAL-ARCHITECTURE-MAP.md`
Entry router: `CUE-INDEX.md`
Audits: `EXECUTION-DEPTH-AUDIT-001.md`, `EXECUTION-DEPTH-AUDIT-002.md`

This is a thin bridge from Operational Architecture nodes/HOW families to exact durable implementation/reference surfaces.

```text
HOW_HAS_A_NAME != AGENT_CAN_FIND_THE_IMPLEMENTATION
```

Do not duplicate full WHAT/WHY/HOW prose here.

| Node | Primary durable surface(s) | Current depth | Use / next action |
|---|---|---|---|
| `OA-RT-01` Runtime routing | `releases/current/RUNTIME-ADOPTION-KERNEL.md`; `research/prototypes/tiny-hot-kernel/` incl. `semantic-router.v0.1.json`; `research/prototypes/finite-context-adoption/`; naturalistic validation | `POINTER_READY / REFERENCE_MACHINE_EXISTS / HOST_ADAPTER_REQUIRED / FIELD_EVIDENCE_REQUIRED` | Reuse existing router/kernel patterns; next unknown is natural fresh-session salience, not another router schema. |
| `OA-MEM-01` Memory Metabolism | `research/prototypes/memory-metabolism/README.md`; `memory-set.schema.json`; `RETRIEVAL-MODEL.md`; `RESTORE-MODEL.md`; `host-integration-0.1/` | `POINTER_READY / HOST_ADAPTER_REQUIRED / FIELD_EVIDENCE_REQUIRED` | Use compiler/archive/retrieval architecture; validate long-run Host behavior separately. |
| `OA-RET-01` Retrieval Obligation | `research/prototypes/memory-metabolism/retrieval-obligation-0.5/` | `POINTER_READY / HOST_ADAPTER_REQUIRED / FIELD_EVIDENCE_REQUIRED` | Bind scope, effective content identity, freshness and sufficiency; bounded no-hit/WAIT remains valid. |
| `OA-PROJ-01` Projection/Compaction | projection-composition, lineage-compaction, compaction×retrieval, lineage-survival map | `POINTER_READY / COMPOSITION_REQUIRED` | Preserve/refer decision-material lineage; route cold dependency to Retrieval Obligation. |
| `OA-WAIT-01` WAIT/Pause | `research/prototypes/wait-state/` | `POINTER_READY / HOST_ADAPTER_REQUIRED` | Map wait/callback/interrupt/polling to Host; preserve wake/timeout/evidence/escalation. |
| `OA-AUTH-01` Authority | `research/prototypes/authority-lease/` | `POINTER_READY / HOST_ADAPTER_REQUIRED` | Resolve grant scope/validity; use `NOT_REQUIRED` for genuinely non-authority-bearing actions. |
| `OA-EFF-01` Effect Lifecycle | `research/prototypes/effect-lifecycle/`; `research/prototypes/execution-surface-fencing/` | `POINTER_READY / HOST_ADAPTER_REQUIRED` | Choose idempotency/fencing/version/status/gateway/compensation/WAIT according to target semantics. |
| `OA-COM-01` Commitment/Settlement | `research/prototypes/commitment-settlement-recovered/`; migration-settlement composition | `POINTER_READY / COMPOSITION_REQUIRED` | Separate obligation subject, executor, effect and settlement; compose physical fencing through Effect Lifecycle. |
| `OA-REC-01` Recovery | `research/prototypes/recovery-adapter/` | `POINTER_READY / HOST_ADAPTER_REQUIRED` | After restore consume world-settlement + authority outputs before resume. |
| `OA-ID-01` Identity/Trajectory | `procedures/PURPOSE-RELATIVE-CONTINUITY-PROCEDURE.md`; Current Continuity Vector; RESTORE-MODEL | `BOUNDED_PROCEDURE_READY / HOST_EVIDENCE_OPEN / UNIVERSAL_SCHEMA_NOT_JUSTIFIED` | Ask continuity-for-what-decision; select only material relations; never infer authority from continuity. |
| `OA-AUTHOR-01` Contested Authorship | `research/prototypes/contested-authorship/` | `POINTER_READY / HOST_ADAPTER_REQUIRED` | Use for material durable self-change; ordinary memory/cache/task state may be out-of-scope/lightweight. |
| `OA-STAND-01` Standing/Rehabilitation | `procedures/STANDING-INPUT-PROCEDURE.md`; #92 lineage | `BOUNDED_PROCEDURE_READY / REHABILITATION_FIELD_POLICY_OPEN` | Route only decision-material objections into disposition/readback; no veto/personhood/authority promotion. |
| `OA-EVID-01` Evidence/Provenance | Evidence Envelope; Evidence Dependency Map; Current contracts/fixtures | `POINTER_READY / HOST_ADAPTER_REQUIRED` | Keep support/applicability/witness/activation/projection/dependency claims separate. |
| `OA-EVO-01` Evolution | Current Evolution Metabolism + v2 schemas/tools; progressive-envelope research | `POINTER_READY / RESEARCH_ALTERNATIVE_ACTIVE` | Current v2 remains adopter baseline; progressive occurrence/enrichment is research. |
| `OA-MIG-01` Migration/Commons | Current adaptation packet v2; lineage-survival + migration-settlement; `COMMONS-TRANSPORT-AND-DISCOVERY-PATTERNS.md` | `SEMANTIC_CARRIER_READY / COMMONS_PATTERN_READY / HOST_PROTOCOL_ADAPTER_REQUIRED` | Keep adaptation packet, durable Commons substrate, A2A/live task protocol and local adoption separate. |
| `OA-ECO-01` Ecology/Resources | #93; MSI experiment; network extraction; verification-as-service variation; `procedures/CONTROL-RETIREMENT-PROCEDURE.md` | `BOUNDED_CONTROL_RETIREMENT_PROCEDURE_READY / FIELD_MESOCOSM_REQUIRED` | Reuse mature mechanisms where fitting; retirement has no universal age/count/score threshold. |
| `OA-ADOPT-01` Adoption/Language/Release | Current first-read/kernel/LITE/adoption/release/language docs; zh-CN projection; semantic fixtures; current validation workflow | `POINTER_READY / STRUCTURAL_MACHINE_SURFACE_EXISTS / BEHAVIORAL_FIELD_EVIDENCE_REQUIRED` | Do not mistake structural parity for behavioral decision equivalence. |

---

# Fast routes by implementation need

## Machine-checkable reference organ

Start with Retrieval Obligation, WAIT, Authority Lease, Effect Lifecycle, Commitment/Settlement, Recovery Adapter, Contested Authorship, Evidence Envelope, Evidence Dependency Map, Tiny Hot Kernel routing, and Current evolution/migration validators.

## Bounded procedure

Current procedures include:

- purpose-relative continuity;
- Standing Input;
- Control Retirement.

A procedure does not automatically justify a schema.

## Commons / interoperability substrate

Use `COMMONS-TRANSPORT-AND-DISCOVERY-PATTERNS.md`.

Current preserved branches include:

- Git/repository Commons;
- OCI-style content-addressed registry;
- object store + explicit index;
- direct transfer;
- A2A/Host-native protocol for live Agent discovery/task exchange.

```text
ACTIVE_PROTOCOL != DURABLE_COMMONS
```

## Host-native mechanism

Examples: idempotency keys, fencing tokens, conditional writes, durable workflows/checkpoints, callbacks/interrupts, RBAC/capability systems, workload identity, native memory/retrieval, provenance/trace/attestation, A2A/task orchestration.

## Field/mesocosm evidence

Examples:

- natural Tiny Kernel cue salience;
- long-run Memory Compiler behavior;
- bilingual/other-language decision equivalence;
- reputation rehabilitation;
- control retirement value under real changing ecology;
- culture/specialization/resource pressure;
- discretionary exploration;
- verification-as-service/validation markets.

---

# Applicability guard

A concrete HOW should say both how to use it and when not to invoke it.

```text
Authority Lease -> NOT_REQUIRED
Contested Authorship -> OUT_OF_SCOPE_FOR_CONTESTED_AUTHORSHIP
Recovery Adapter -> independent rescue/drill only when required
Continuity Procedure -> NOT_REQUIRED when continuity cannot change the decision
Standing Procedure -> NO_FORMAL_STANDING when objection cannot change the consequential decision
Control Retirement -> KEEP_ACTIVE / UNKNOWN_WAIT when retirement basis is weak
```

`REFERENCE_ORGAN_EXISTS != UNIVERSAL_APPLICABILITY`
`CURRENT_CHANGE = NO`
