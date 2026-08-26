# ENA Operational Architecture Reference Pointer Matrix

Status: `EXECUTION_ROUTING_SURFACE / FIRST_PASS / OPEN_CARDINALITY / RESEARCH_ONLY / NOT_CURRENT`

Date: 2026-08-27

Parent map: `OPERATIONAL-ARCHITECTURE-MAP.md`

Entry router: `CUE-INDEX.md`

Evidence: `EXECUTION-DEPTH-AUDIT-001.md`

## Purpose

This file is a thin bridge from Operational Architecture nodes/HOW families to exact durable implementation/reference surfaces.

It exists because:

```text
HOW_HAS_A_NAME
!=
AGENT_CAN_FIND_THE_IMPLEMENTATION
```

Do not duplicate full WHAT/WHY/HOW prose here. Follow the linked README/schema/tool when execution depth is needed.

Gap/depth labels are descriptive and open-cardinality.

| Node | Primary durable surface(s) | Current depth | Use / next action |
|---|---|---|---|
| `OA-RT-01` Runtime routing | `releases/current/RUNTIME-ADOPTION-KERNEL.md`; `research/prototypes/tiny-hot-kernel/`; `research/prototypes/finite-context-adoption/`; `research/prototypes/memory-metabolism/naturalistic-validation-0.1/` | `POINTER_PARTIAL / HOST_ADAPTER_REQUIRED / FIELD_EVIDENCE_REQUIRED` | Choose Host routing mechanism; do not assume one universal hot kernel. |
| `OA-MEM-01` Memory Metabolism | `research/prototypes/memory-metabolism/README.md`; `memory-set.schema.json`; `RETRIEVAL-MODEL.md`; `RESTORE-MODEL.md`; `host-integration-0.1/` | `POINTER_READY / HOST_ADAPTER_REQUIRED / FIELD_EVIDENCE_REQUIRED` | Use compiler/archive/retrieval architecture; validate long-run Host behavior separately. |
| `OA-RET-01` Retrieval Obligation | `research/prototypes/memory-metabolism/retrieval-obligation-0.5/README.md`; schema; `reference-runtime.json`; validator/selftest | `POINTER_READY / HOST_ADAPTER_REQUIRED / FIELD_EVIDENCE_REQUIRED` | Bind scope, effective content identity, freshness and sufficiency; bounded no-hit/WAIT remains valid. |
| `OA-PROJ-01` Projection/Compaction | `research/prototypes/memory-metabolism/projection-composition-0.1/`; `research/prototypes/lineage-compaction-contract/`; `research/prototypes/lineage-compaction-retrieval-composition/`; `research/reconstruction/PORTABLE-SNAPSHOT-LINEAGE-SURVIVAL-MAP.md` | `POINTER_READY / COMPOSITION_REQUIRED` | Preserve/refer decision-material lineage; route cold dependency to `OA-RET-01`. |
| `OA-WAIT-01` WAIT/Pause | `research/prototypes/wait-state/README.md`; validator/selftest; `.github/workflows/wait-state-research.yml` | `POINTER_READY / HOST_ADAPTER_REQUIRED` | Map wait/callback/interrupt/polling to Host; preserve wake/timeout/evidence/escalation. |
| `OA-AUTH-01` Authority | `research/prototypes/authority-lease/README.md`; `authority-lease.v0.1.json`; validator/selftest | `POINTER_READY / HOST_ADAPTER_REQUIRED` | Resolve grant scope/validity; use `NOT_REQUIRED` for genuinely non-authority-bearing actions rather than manufacturing grants. |
| `OA-EFF-01` Effect Lifecycle | `research/prototypes/effect-lifecycle/README.md`; contract/validator/selftest; `research/prototypes/execution-surface-fencing/` | `POINTER_READY / HOST_ADAPTER_REQUIRED` | Select idempotency/fencing/version/status/gateway/compensation/WAIT according to target semantics; do not collapse them. |
| `OA-COM-01` Commitment/Settlement | `research/prototypes/commitment-settlement-recovered/`; `research/prototypes/migration-settlement-composition/` | `POINTER_READY / COMPOSITION_REQUIRED` | Separate obligation subject, executor, effect and settlement; compose physical fencing through `OA-EFF-01`. |
| `OA-REC-01` Recovery | `research/prototypes/recovery-adapter/README.md`; `recovery-adapter.v0.1.json`; validator/selftest | `POINTER_READY / HOST_ADAPTER_REQUIRED` | Check recovery path/drill only where required; after restore consume world-settlement + authority outputs before resume. |
| `OA-ID-01` Identity/Trajectory | #92; `research/prototypes/memory-metabolism/RESTORE-MODEL.md`; conditional epoch binding in Authority Lease; external identity HOW research | `REFERENCE_PROCEDURE_MISSING / HOST_ADAPTER_REQUIRED` | Use purpose-relative continuity reasoning now; do not invent mandatory trajectory/epoch schema until a concrete reference branch earns rent. |
| `OA-AUTHOR-01` Contested Authorship | `research/prototypes/contested-authorship/README.md`; contract/validator/selftest | `POINTER_READY / HOST_ADAPTER_REQUIRED` | Use for material durable self-change; ordinary memory/cache/task state may return out-of-scope/lightweight path. |
| `OA-STAND-01` Standing/Rehabilitation | #92 reconstruction/closure lineage; external selective-disclosure/reputation mechanisms | `REFERENCE_PROCEDURE_MISSING / FIELD_EVIDENCE_REQUIRED` | Standing Input is a candidate small reference procedure; rehabilitation remains environment evidence/policy; no global trust score. |
| `OA-EVID-01` Evidence/Provenance | `research/prototypes/evidence-envelope/README.md`; envelope contract/validator/selftest; `research/prototypes/evidence-dependency-map/README.md`; validator/selftest; Current contracts/fixtures | `POINTER_READY / HOST_ADAPTER_REQUIRED` | Keep support/applicability/witness/activation/projection/dependency claims separate; machine PASS remains represented consistency. |
| `OA-EVO-01` Evolution | `releases/current/09-EVOLUTION-METABOLISM.md`; `releases/current/schemas/evolution-record.v2.schema.json`; `releases/current/tools/validate_evolution_record_v2.py`; `research/prototypes/evolution-record-progressive-envelope/` | `POINTER_READY / RESEARCH_ALTERNATIVE_ACTIVE` | Current v2 remains adopter baseline; progressive event/enrichment is research branch. |
| `OA-MIG-01` Migration/Commons | `releases/current/schemas/adaptation-packet.v2.schema.json`; `research/prototypes/migration-settlement-composition/`; lineage survival map; projection/compaction research | `POINTER_READY / HOST_ADAPTER_REQUIRED / COMPOSITION_REQUIRED` | Preserve source lineage and receiver-local selection; use A2A/Host protocol for active coordination rather than treating packet as protocol. |
| `OA-ECO-01` Ecology/Resources | #93; `research/evolution-inbox/NETWORK-PROTOCOL-DESIGN-EXTRACTION.md`; `research/reconstruction/RECOVERED-VARIATION-VERIFICATION-AS-SERVICE.md`; mesocosm/community research | `POINTER_PARTIAL / FIELD_EVIDENCE_REQUIRED / MESOCOSM_REQUIRED / DORMANT_RESEARCH` | Reuse mature external mechanisms where fitting; do not complete ecology by inventing a universal schema. |
| `OA-ADOPT-01` Adoption/Language/Release | `releases/current/00-READ-ME-FIRST.md`; `RUNTIME-ADOPTION-KERNEL.md`; `LITE-ADOPTION-INSTRUCTION.md`; `07-ADOPTION-AND-FIELD-VALIDATION.md`; `08-RELEASE-DISCIPLINE.md`; `10-LANGUAGE-PORTABILITY.md`; Current schemas/tools/projections | `POINTER_READY / FIELD_EVIDENCE_REQUIRED_FOR_SALIENCE_AND_EQUIVALENCE` | Resolve Current first, adopt minimal effective surface, preserve immutable release identity, test fresh-session/language behavior separately. |

---

# Fast routes by implementation need

## I need a machine-checkable reference organ now

Start with:

- Retrieval Obligation;
- WAIT State;
- Authority Lease;
- Effect Lifecycle;
- Commitment/Settlement;
- Recovery Adapter;
- Contested Authorship;
- Evidence Envelope;
- Evidence Dependency Map;
- Current evolution/migration schemas and validators.

These surfaces remain research/reference unless Current explicitly says otherwise.

## I need a Host-native mechanism

Common examples:

- idempotency keys;
- fencing tokens;
- conditional/versioned writes;
- durable workflows/checkpoints;
- callbacks/interrupts;
- RBAC/capability systems;
- workload identity/credential rotation;
- memory blocks/vector/index/exact-path retrieval;
- provenance/trace/attestation systems;
- A2A/task orchestration.

Use the Operational Map to preserve ENA boundaries while mapping to Host semantics.

## I reached a real reference-procedure gap

Current first-pass gaps:

- purpose-relative Identity/Trajectory operational procedure;
- Standing Input reusable reference procedure.

Do not infer that each gap requires a universal schema.

## I reached a field/ecology question

Examples:

- natural Tiny Kernel cue salience;
- long-run Memory Compiler behavior;
- reputation rehabilitation policy/value;
- control retirement thresholds;
- culture/specialization/resource pressure;
- discretionary exploration;
- verification-as-service/validation markets.

Use field/mesocosm evidence only where interaction/reality can produce decision-changing information.

---

# Applicability guard

Reference organ existence does not make it mandatory.

Several mature prototypes already encode out-of-scope/lightweight behavior:

```text
Authority Lease -> NOT_REQUIRED
Contested Authorship -> OUT_OF_SCOPE_FOR_CONTESTED_AUTHORSHIP
Recovery Adapter -> independent rescue/drill only when required
Evidence Envelope -> optional sections / low-risk false-BLOCK controls
```

Assembly should preserve this pattern:

> A concrete HOW should say both **how to use it** and **when not to invoke it**.

`CURRENT_CHANGE = NO`
