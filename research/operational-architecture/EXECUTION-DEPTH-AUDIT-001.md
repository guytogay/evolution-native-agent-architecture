# Operational Architecture Execution-Depth Audit 001

Status: `STATIC_EXECUTION_DEPTH_AUDIT / FIRST_PASS / RESEARCH_ONLY / NOT_FIELD_EVIDENCE / CURRENT_UNCHANGED`

Date: 2026-08-27

Inputs:

- `CUE-INDEX.md`
- `OPERATIONAL-ARCHITECTURE-MAP.md`
- existing Current, research prototypes, reconstruction artifacts, and Host/external-HOW research.

## Question

After routing from an ordinary cue to a node and HOW branch, can an Agent continue to a durable implementation/reference surface and a concrete next action?

```text
CUE -> NODE -> HOW NAME
```

is not enough. The desired depth is:

```text
CUE
-> NODE
-> HOW
-> DURABLE ARTIFACT / REFERENCE PROCEDURE / HOST MECHANISM
-> CONCRETE NEXT ACTION
-> FAILURE / FALLBACK / EVIDENCE BOUNDARY
```

This audit distinguishes missing pointers from missing mechanisms. It does not require every HOW to become an ENA-owned executable tool.

## Gap labels used in this audit

Descriptive labels only; not a closed ontology:

- `POINTER_READY` — durable reference surface exists and can be linked directly;
- `POINTER_PARTIAL` — useful surfaces exist but routing/selection between them needs clarification;
- `REFERENCE_PROCEDURE_MISSING` — the HOW is more specific than a principle but lacks a reusable operational procedure/reference artifact;
- `HOST_ADAPTER_REQUIRED` — property/HOW is intentionally realized by Host-native machinery;
- `FIELD_EVIDENCE_REQUIRED` — static representation exists but behavior/value needs real Host evidence;
- `MESOCOSM_REQUIRED` — the unknown is interaction/ecology dynamics not derivable statically;
- `DORMANT_RESEARCH` — retained option/hypothesis, not an active implementation requirement.

## Node audit

### OA-RT-01 — Runtime adoption / semantic routing

Durable surfaces:

- `releases/current/RUNTIME-ADOPTION-KERNEL.md`;
- `research/prototypes/tiny-hot-kernel/`;
- `research/prototypes/finite-context-adoption/`;
- `research/prototypes/memory-metabolism/naturalistic-validation-0.1/`.

Depth:

`POINTER_PARTIAL + HOST_ADAPTER_REQUIRED + FIELD_EVIDENCE_REQUIRED`

Why not simply `POINTER_READY`:

The repository has cue/kernel experiments and naturalistic validation material, but no universal always-hot router should be selected from static evidence. Host-native hooks/index/search remain legitimate alternatives.

### OA-MEM-01 — Memory Metabolism

Durable surfaces:

- `research/prototypes/memory-metabolism/README.md`;
- `research/prototypes/memory-metabolism/memory-set.schema.json`;
- `research/prototypes/memory-metabolism/RETRIEVAL-MODEL.md`;
- `research/prototypes/memory-metabolism/RESTORE-MODEL.md`;
- `research/prototypes/memory-metabolism/host-integration-0.1/`;
- `research/prototypes/memory-metabolism/naturalistic-validation-0.1/`.

Depth:

`POINTER_READY + HOST_ADAPTER_REQUIRED + FIELD_EVIDENCE_REQUIRED`

The organ has substantially more implementation material than the first assembly map exposed. The remaining uncertainty is long-run Host behavior, not absence of a memory reference architecture.

### OA-RET-01 — Retrieval Obligation

Durable surfaces:

- `research/prototypes/memory-metabolism/retrieval-obligation-0.5/README.md`;
- `retrieval-obligation.schema.json`;
- `reference-runtime.json`;
- `validate_retrieval_obligation.py`;
- `selftest.py`.

Depth:

`POINTER_READY + HOST_ADAPTER_REQUIRED + FIELD_EVIDENCE_REQUIRED`

The reference organ explicitly covers effective content identity, decision-material freshness, logical resolver identity, scope/sufficiency, bounded no-hit and false-complete residuals.

Important boundary:

`REFERENCE_RUNTIME_EXISTS != R0_NATURALLY_FIRES`

### OA-PROJ-01 — Projection / compaction / lineage survival

Durable surfaces:

- `research/prototypes/memory-metabolism/projection-composition-0.1/`;
- `research/prototypes/lineage-compaction-contract/`;
- `research/prototypes/lineage-compaction-retrieval-composition/`;
- `research/reconstruction/PORTABLE-SNAPSHOT-LINEAGE-SURVIVAL-MAP.md`;
- migration-settlement composition for source omission/obligation lineage.

Depth:

`POINTER_READY + COMPOSITION_REQUIRED`

The main assembly improvement needed is not another compaction subsystem; it is explicit routing from cold references into the existing Retrieval Obligation path.

### OA-WAIT-01 — WAIT / refusal / pause

Durable surfaces:

- `research/prototypes/wait-state/README.md`;
- `research/prototypes/wait-state/tools/validate_wait_state.py`;
- `research/prototypes/wait-state/tools/selftest_wait_state.py`;
- `.github/workflows/wait-state-research.yml`.

Depth:

`POINTER_READY + HOST_ADAPTER_REQUIRED`

Callbacks, interrupts, durable workflow waits and polling/backoff remain Host-specific HOW branches rather than one universal WAIT implementation.

### OA-AUTH-01 — Authority binding / lease

Durable surfaces:

- `research/prototypes/authority-lease/README.md`;
- `authority-lease.v0.1.json`;
- `tools/validate_authority_lease.py`;
- `tools/selftest_authority_lease.py`;
- `.github/workflows/authority-lease-research.yml`.

Depth:

`POINTER_READY + HOST_ADAPTER_REQUIRED`

Important recovered execution property:

`NOT_REQUIRED` is a valid result for genuinely non-authority-bearing actions. The prototype already contains an authority-anxiety false-BLOCK guard, supporting the cue index's consequence-first pre-router.

### OA-EFF-01 — Effect Lifecycle / execution-surface control

Durable surfaces:

- `research/prototypes/effect-lifecycle/README.md`;
- `effect-lifecycle.v0.1.json`;
- `tools/validate_effect_lifecycle.py`;
- `tools/selftest_effect_lifecycle.py`;
- `research/prototypes/execution-surface-fencing/`;
- `.github/workflows/effect-lifecycle-research.yml`;
- `.github/workflows/execution-surface-fencing-research.yml`.

Depth:

`POINTER_READY + HOST_ADAPTER_REQUIRED`

Different HOWs remain materially distinct:

```text
provider idempotency
!= assignment fencing
!= optimistic concurrency
!= status query
!= gateway coverage
!= compensation
!= WAIT
```

### OA-COM-01 — Commitment / Settlement

Durable surfaces:

- `research/prototypes/commitment-settlement-recovered/`;
- `research/prototypes/migration-settlement-composition/`;
- progressive/migration lineage work.

Depth:

`POINTER_READY + COMPOSITION_REQUIRED`

The main Host gap is external authority/settlement binding, not the represented obligation/executor/settlement distinction itself.

### OA-REC-01 — Recovery Adapter

Durable surfaces:

- `research/prototypes/recovery-adapter/README.md`;
- `recovery-adapter.v0.1.json`;
- `tools/validate_recovery_adapter.py`;
- `tools/selftest_recovery_adapter.py`;
- `.github/workflows/recovery-adapter-research.yml`.

Depth:

`POINTER_READY + HOST_ADAPTER_REQUIRED`

The prototype already composes Effect Lifecycle and Authority Lease outputs instead of duplicating their semantics.

### OA-ID-01 — Identity / trajectory / lineage / accountability

Durable surfaces found:

- #92 durable reconstruction;
- `research/prototypes/memory-metabolism/RESTORE-MODEL.md` for restore-related continuity questions;
- Authority Lease supports conditional epoch binding without requiring universal epochs;
- external HOW research around workload identity/attestation/credential rotation.

Search for a standalone `trajectory_id + epoch_id + lineage_edges` reference organ did **not** surface an active prototype.

Depth:

`REFERENCE_PROCEDURE_MISSING + HOST_ADAPTER_REQUIRED`

Interpretation:

This is a real execution-depth gap, but not evidence that ENA needs one universal identity schema. A useful next branch may be a minimal purpose-relative continuity/lineage procedure or a Host mapping card rather than mandatory trajectory machinery.

### OA-AUTHOR-01 — Contested Authorship

Durable surfaces:

- `research/prototypes/contested-authorship/README.md`;
- `contested-authorship.v0.1.json`;
- `tools/validate_contested_authorship.py`;
- `tools/selftest_contested_authorship.py`;
- `.github/workflows/contested-authorship-research.yml`.

Depth:

`POINTER_READY + HOST_ADAPTER_REQUIRED`

The prototype explicitly separates durable self-change from ordinary memory/task/cache state and provides `OUT_OF_SCOPE_FOR_CONTESTED_AUTHORSHIP` false-BLOCK behavior.

### OA-STAND-01 — Standing / reputation / rehabilitation / selective legibility

Durable surfaces found:

- #92 reconstruction and closure/disposition material;
- external identity/reputation/selective-disclosure HOW research;
- no standalone `Standing Input` reference prototype surfaced;
- no standalone rehabilitation reference implementation surfaced.

Depth:

`REFERENCE_PROCEDURE_MISSING + FIELD_EVIDENCE_REQUIRED`

Sub-branches differ:

- `Standing Input`: likely small reusable procedure/reference carrier could be built and statically falsified;
- rehabilitation policy: environment/field evidence matters more than another universal schema;
- selective legibility: `HOST_ADAPTER_REQUIRED`, with external mature mechanisms available;
- global scalar reputation: intentionally not selected.

### OA-EVID-01 — Evidence / provenance / applicability / witness

Durable surfaces:

- `research/prototypes/evidence-envelope/README.md`;
- `evidence-envelope.v0.1.json`;
- `tools/validate_evidence_envelope.py`;
- `tools/selftest_evidence_envelope.py`;
- `research/prototypes/evidence-dependency-map/README.md`;
- its validator/selftest;
- Current claim/evidence/support operational contracts and fixtures.

Depth:

`POINTER_READY + HOST_ADAPTER_REQUIRED`

The reference surfaces already preserve applicability, activation, witness, projection and dependency behaviors as separate mechanisms rather than one `evidence=true` field.

### OA-EVO-01 — Evolution occurrence / variation / selection

Durable surfaces:

- `releases/current/schemas/evolution-record.v2.schema.json`;
- `releases/current/tools/validate_evolution_record_v2.py`;
- `releases/current/09-EVOLUTION-METABOLISM.md`;
- `research/prototypes/evolution-record-progressive-envelope/`;
- latent/Variation-Space/reality-contact lineage in #93/#89.

Depth:

`POINTER_READY + RESEARCH_ALTERNATIVE_ACTIVE`

Current aggregate v2 is the adopter baseline; progressive occurrence representation is a research HOW branch, not silently promoted replacement.

### OA-MIG-01 — Migration / Commons / receiver-local reselection

Durable surfaces:

- `releases/current/schemas/adaptation-packet.v2.schema.json`;
- Current evolution/Commons semantics;
- `research/prototypes/migration-settlement-composition/`;
- `research/reconstruction/PORTABLE-SNAPSHOT-LINEAGE-SURVIVAL-MAP.md`;
- projection/compaction prototypes;
- A2A/external coordination research.

Depth:

`POINTER_READY + HOST_ADAPTER_REQUIRED + COMPOSITION_REQUIRED`

Packet transport does not implement discovery/task lifecycle; active inter-Agent coordination remains Host/protocol-specific.

### OA-ECO-01 — Ecology / resources / coordination / specialization

Durable surfaces:

- #93 reconstruction and external HOW harvests;
- `research/evolution-inbox/NETWORK-PROTOCOL-DESIGN-EXTRACTION.md`;
- `research/reconstruction/RECOVERED-VARIATION-VERIFICATION-AS-SERVICE.md`;
- mesocosm/agent-community research lineage.

Depth:

`POINTER_PARTIAL + FIELD_EVIDENCE_REQUIRED + MESOCOSM_REQUIRED + DORMANT_RESEARCH`

This mixed depth is intentional. Quotas/leases/backoff are mature external mechanisms; control retirement, culture, specialization, discretionary agency and verification markets require environment interaction to reveal decision-relevant behavior.

A universal ecology schema would currently be premature.

### OA-ADOPT-01 — Adoption / language / tooling / release

Durable surfaces:

- `releases/current/00-READ-ME-FIRST.md`;
- `releases/current/RUNTIME-ADOPTION-KERNEL.md`;
- `releases/current/LITE-ADOPTION-INSTRUCTION.md`;
- `releases/current/07-ADOPTION-AND-FIELD-VALIDATION.md`;
- `releases/current/08-RELEASE-DISCIPLINE.md`;
- `releases/current/10-LANGUAGE-PORTABILITY.md`;
- Current schemas/tools/language projections;
- repository project-control and release-validation lineage.

Depth:

`POINTER_READY + FIELD_EVIDENCE_REQUIRED_FOR_SALIENCE/LANGUAGE_EQUIVALENCE`

The remaining problem is not absence of adoption/release machinery; it is natural fresh-session routing, complete cold-language projection, and evidence that the effective loaded surface changes behavior as intended.

---

# Cross-node result

## 1. The first map under-reported existing implementation depth

Several nodes already have executable reference organs with machine validation. Their primary assembly defect is **missing exact pointers in the navigational surface**, not missing HOWs.

High-confidence pointer-ready families include:

```text
Retrieval Obligation
WAIT state
Authority Lease
Effect Lifecycle
Commitment/Settlement
Recovery Adapter
Contested Authorship
Evidence Envelope
Evidence Dependency Map
Current evolution/migration/release machinery
```

## 2. Two gaps are materially different from pointer defects

### Identity/Trajectory

There is rich semantic/external HOW research, but no currently surfaced standalone purpose-relative trajectory/epoch reference procedure.

Do not jump straight to a mandatory identity schema.

### Standing Input

There is a simple candidate shape and strong operational motivation, but no standalone reusable reference procedure surfaced.

This looks more amenable to a bounded reference procedure/static falsification than reputation rehabilitation itself.

## 3. Ecology should not be “fixed” by schema completion

A large share of OA-ECO-01's uncertainty is exactly where mesocosm/field evidence can reveal non-derivable mechanisms.

```text
FIELD_EVIDENCE_REQUIRED != IMPLEMENTATION_FORGOTTEN
MESOCOSM_REQUIRED != ARCHITECTURE_INCOMPLETE_BY_DEFINITION
```

## 4. False-BLOCK guards already recur inside mature prototypes

Authority Lease and Contested Authorship both explicitly carry lightweight/out-of-scope paths. Recovery Adapter makes independent rescue/drill conditional.

This supports a broader assembly rule:

> Concrete HOWs should expose when they **do not apply**, not only how to activate them.

That is more useful than attaching one global risk score to every operation.

## 5. Next artifact should expose pointers without duplicating HOW semantics

A compact `REFERENCE-POINTER-MATRIX.md` is justified.

Its job:

```text
node / HOW family
-> exact durable path(s)
-> depth/gap class
-> what to do next
```

It should **not** restate every node's WHAT/WHY or copy every prototype README.

---

# Decision

```text
EXECUTION_DEPTH_AUDIT = ESTABLISHED_ON_REPRESENTATIVE_CURRENT_NODE_SET
POINTER_MISSING_IS_A_MAJOR_ASSEMBLY_DEFECT = YES
IDENTITY_TRAJECTORY_REFERENCE_DEPTH = REAL_GAP
STANDING_INPUT_REFERENCE_DEPTH = REAL_GAP
ECOLOGY_SCHEMA_COMPLETION = NOT_JUSTIFIED
FALSE_BLOCK_APPLICABILITY_GUARDS = IMPORTANT_CROSS_CUTTING_HOW_PROPERTY
NEXT_ARTIFACT = REFERENCE_POINTER_MATRIX
CURRENT_CHANGE = NO
```
