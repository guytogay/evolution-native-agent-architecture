# ENA Reconstruction-to-Release Master Plan

Status: `ACTIVE_MASTER_PLAN / MAIN_VISIBLE_PROJECT_CONTROL / RELEASE_SCOPE_READY / CURRENT_UNCHANGED_UNTIL_RELEASE`

Updated: 2026-08-27

This is the stable long-horizon plan for moving ENA from the v0.3.6 semantic trunk through concrete Operational Architecture and, only when release scope and validation justify it, to a new Current release.

Fast-moving execution state lives in `research/plans/PROGRESS.yaml` on the branch named by `research/ACTIVE-RESEARCH.yaml`.

## Goal

ENA must be inhabitable, not merely explainable.

```text
TELOS / PURPOSE
      |
      v
WHAT / WHY
stable semantic trunk; abstraction/compression may be useful
      |
      +--> HOW-A
      |     +--> concrete organ/process/tool/protocol/procedure
      |     +--> Host binding / adapter
      |     +--> failure / fallback / non-applicability
      |     +--> evidence
      |
      +--> HOW-B
      +--> HOW-C
      +--> ...
```

```text
ONE_WHAT_WHY -> 0..N_CONCRETE_HOW_BRANCHES
```

The final test is whether an Agent can actually live by the architecture.

## Continuation control plane

A successor session should start from `main` and resolve, in order:

1. `PROJECT-HUB.md`;
2. `releases/current/CURRENT-BASELINE.yaml`;
3. `research/ACTIVE-RESEARCH.yaml`;
4. `research/methodology/README.md` and canonical methodology;
5. this master plan;
6. active-branch `research/RESEARCH-START-HERE.md`;
7. active-branch `research/plans/PROGRESS.yaml`;
8. the relevant Operational Architecture / release-scope artifacts.

Do not infer active work from branch names, recency, or old PR numbers.

## Current aligned posture — 2026-08-27

Current remains:

```text
v0.3.6 / CURRENT / FIELD_VALIDATION
```

Long-lived topology remains:

```text
main
research/ena-reconstruction
```

PR #109 was merged to `main` as a research checkpoint at:

`3e5862998200770c37a6c67ed1789c12a852739c`

The active research branch was fast-forwarded to that exact merge commit after the checkpoint, so `main` and `research/ena-reconstruction` began the next phase from identical content.

PR #109 changed research/workflow surfaces only; `releases/current/` remained unchanged.

Phase summary:

- research continuity/control plane: `BASELINE_ESTABLISHED / MAINTAIN`;
- anti-ablation archaeology: `RECOVERY_SUFFICIENT / REOPENABLE`;
- HOW branch expansion: `ACTIVE_DURING_SELECTION`;
- external HOW harvest: `ACTIVE_ON_DEMAND`;
- Host binding: `PARTIAL / CONTINUES`;
- cross-organ composition: `ACTIVE_WHERE_DECISION_RELEVANT`;
- Operational Architecture assembly: `ASSEMBLY_SUFFICIENT_FOR_RELEASE_SCOPE / CONTINUES_IN_PARALLEL`;
- release-scope entry gate: `PASS_WITH_OPEN_FIELD_RESIDUALS`;
- release-scope reconciliation: `READY_TO_START`;
- candidate build/validation: `NOT_STARTED`;
- promotion: `NOT_STARTED`;
- next version: `UNASSIGNED`.

## Project State Alignment Gate

Use `research/methodology/PROJECT-STATE-ALIGNMENT-GATE.md` after material transitions such as:

- branch handoff/cleanup;
- checkpoint merge to main;
- directory/canonical-path changes;
- material methodology or master-plan phase change;
- Current/candidate/release-state change.

```text
INDIVIDUAL_FILE_CORRECT != PROJECT_STATE_COHERENT
MATERIAL_TRANSITION -> ALIGN -> RESUME
```

The gate is transition-triggered, not ritual after every ordinary commit.

## Phase 1 — Research continuity and repository control

State: `BASELINE_ESTABLISHED / MAINTAIN_AS_INVARIANT`

Goal: a fresh session can identify Current, active research branch, methodology, plan, progress, and next permitted work without reconstructing old conversations.

## Phase 2 — Anti-ablation archaeology / variation recovery

State: `RECOVERY_SUFFICIENT_FOR_CURRENT_SELECTION / REOPENABLE`

Correct sequence:

```text
historical problem/HOW recovery
-> durable variation map
-> WHAT / WHY / plural HOW / EVIDENCE reconstruction
-> selection only after recovery is sufficient for the decision
```

This is not a completeness proof. Reopen when new history, missing lineage, assembly contradiction, or field evidence changes the engineering map.

## Phase 3 — HOW branch expansion

State: `ACTIVE_DURING_RELEASE_RECONCILIATION`

Valid HOW forms include state machines, workflows, protocols, resolvers, adapters, schemas, validators, bounded procedures, file/layout conventions, and Host-native mechanisms.

One property may retain multiple HOWs indefinitely.

A concrete HOW should expose both:

- how to invoke/use it;
- when it does not apply or should yield WAIT/UNKNOWN/lightweight path.

## Phase 4 — External HOW harvest

State: `ACTIVE_ON_DEMAND`

Use mature AI/distributed-systems/community mechanisms when a concrete execution-depth gap exists.

```text
ENA failure
-> external mechanism search
-> mechanism extraction
-> ENA/Host mapping
-> falsification/comparison
-> retain/specialize/reject
```

Recent useful families include durable workflows, Host memory/retrieval, A2A active task interoperability, OCI-style durable content registries, idempotency/fencing, provenance/attestation, and reversible lifecycle/retirement mechanisms.

External popularity is never selection proof.

## Phase 5 — Host binding

State: `PARTIAL / CONTINUES`

Possible dispositions:

```text
NATIVE_HOST_ORGAN
ADAPTER_REQUIRED
REFERENCE_IMPLEMENTATION
BOUNDED_PROCEDURE
INAPPLICABLE
UNKNOWN
```

Do not force every Host to instantiate every organ.

## Phase 6 — Cross-organ composition

State: `ACTIVE_WHERE_DECISION_RELEVANT`

High-value seams already established include:

```text
Memory -> Retrieval -> Projection/Compaction
Authority -> Effect -> Commitment/Settlement -> Recovery
Migration -> Source Lineage -> Obligation/Settlement
Assignment -> Idempotency/Fencing/Version/Status/Gateway/WAIT
Identity/Continuity -> Commitment -> Standing/Reputation
Commons substrate -> Active protocol -> Local selection
```

Preserve demonstrated boundaries such as:

```text
CURRENT_STATE_EQUIVALENCE != HISTORY_EQUIVALENCE
IMPORT_VALIDATOR != OMISSION_DETECTOR_WITHOUT_SOURCE_WITNESS
SUMMARY_VALID != MATERIAL_USE_READY
COLD_REF_PRESENT != RETRIEVAL_SUFFICIENCY_RESOLVED
UNIQUE_CURRENT_ASSIGNMENT != STALE_EXECUTOR_PHYSICALLY_FENCED
SINGLE_VERSIONED_WRITE != CURRENT_EXECUTOR_WON
ACTIVE_PROTOCOL != DURABLE_COMMONS
NO_INCIDENT != CONTROL_NOT_NEEDED
```

Prefer deterministic falsification when the failure is statically reachable. Use field/mesocosm evidence only where reality can reveal decision-relevant structure not already encoded.

## Phase 7 — Operational Architecture assembly

State: `ASSEMBLY_SUFFICIENT_FOR_RELEASE_SCOPE / CONTINUES_IN_PARALLEL`

Canonical research assembly lives under:

`research/operational-architecture/`

Current traversal:

```text
ordinary problem / semantic cue
-> consequence-first routing
-> CUE-INDEX
-> WHAT/WHY node
-> plural HOW branches
-> REFERENCE-POINTER-MATRIX
-> prototype / bounded procedure / pattern / Host mechanism
-> action or honest residual
```

Established bounded procedures/patterns include:

- purpose-relative continuity;
- Standing Input;
- Control Retirement;
- Commons transport/discovery layering.

Many nodes already point to machine-checkable research organs.

Assembly acceptance criteria for release-scope reconciliation are now met on static/durable project evidence:

- route from problem/property to concrete HOW exists;
- applicability/Host/evidence boundaries are visible;
- pointer gaps are separated from organ gaps;
- plural/dormant/experimental branches remain visible;
- composition seams are discoverable;
- unresolved field questions remain explicitly unresolved.

This does not claim the Operational Architecture is complete forever.

## Phase 8 — Release scope reconciliation

State: `READY_TO_START`

Canonical workspace:

`research/release-scope/`

Entry gate:

`research/release-scope/RELEASE-SCOPE-ENTRY-GATE-001.md`

The reconciliation must classify actual deliverables separately:

```text
CURRENT_SEMANTIC_ANCHOR
ADOPTER_GUIDANCE_CANDIDATE
REFERENCE_ORGAN_CANDIDATE
HOST_ADAPTER_PATTERN
FIELD_OR_MESOCOSM_ONLY
MAINTENANCE_TOOLING_CANDIDATE
RESEARCH_EXPERIMENTAL
DORMANT_LINEAGE
SEMANTIC_DELTA_CANDIDATE
```

Working classes are navigation only, not ontology.

Key question:

> Which concrete HOW/navigation/reference/tooling surfaces materially improve an adopter's ability to live ENA, and which should remain optional, Host-specific, experimental, dormant, or research-only?

Important:

```text
NO_NEW_CORE_RULES != NO_RELEASE_VALUE
LARGE_RESEARCH_TREE != SHIP_EVERYTHING
```

A practical architecture release with zero new Constitution/Core IDs is valid if the release materially improves usable HOW without falsely universalizing research organs.

Known maintenance candidate to classify:

- inherited `tools/ena_evolve.py` requires `--variation-space` for `propose/import`, false-blocking Current v0.3.6 latent variation semantics. This is a tooling candidate, not demonstrated Core delta.

Do not assign the next version until release scope stabilizes.

## Phase 9 — Candidate build and validation

State: `NOT_STARTED`

After scope stabilizes:

1. build a self-contained candidate from an exact committed tree;
2. preserve immutable source identity;
3. run deterministic machine validation;
4. freeze candidate identity;
5. obtain independent falsification appropriate to the actual changes;
6. reconcile findings without mutating frozen identity;
7. create a successor candidate only for material correction;
8. stop succession when another round cannot plausibly change the decision.

## Phase 10 — Release and promotion

State: `NOT_STARTED`

Only after candidate evidence supports release:

- create the governed release surface/branch;
- package exact candidate bytes;
- verify file-set/hash parity and release identity;
- run required CI/security/regression checks;
- publish/read back artifacts where applicable;
- promote through release discipline;
- verify post-merge `releases/current/` identity;
- update project/history/control pointers;
- run the Project State Alignment Gate again.

Do not claim release complete on narrative confidence.

## Research-method invariants

```text
PROPERTY != ORGAN != HOST_BINDING != EVIDENCE != ADOPTION
WHAT_WHY_COVERAGE != HOW_COMPLETION
REQUESTED_N != DISCOVERED_N
WORKING_TAXONOMY != ONTOLOGY
EXPERIMENTS_MUST_PAY_EPISTEMIC_RENT
EXTERNAL_POPULARITY != SELECTION_PROOF
NO_CHANGE = VALID_OUTCOME
REMOVE_FROM_ACTIVE_ARCHITECTURE != ERASE_FROM_LINEAGE
HANDOFF_SUMMARY != PROJECT_STATE
MATERIAL_TRANSITION -> ALIGN -> RESUME
RECOVERY_SUFFICIENT_FOR_ASSEMBLY != ARCHAEOLOGY_COMPLETE_FOREVER
ASSEMBLY != CURRENT_PROMOTION
NO_NEW_CORE_RULES != NO_RELEASE_VALUE
```

## Progress carrier

Fast-moving execution belongs in:

`research/plans/PROGRESS.yaml`

This master plan changes only when the long-horizon phase model or closure criteria materially change.
