# ENA Reconstruction-to-Release Master Plan

Status: `ACTIVE_MASTER_PLAN / MAIN_VISIBLE_PROJECT_CONTROL / V0_3_7_CANDIDATE0_FROZEN / INDEPENDENT_FALSIFICATION_PREPARATION / CURRENT_UNCHANGED`

Updated: 2026-08-27

This is the stable long-horizon plan for moving ENA from the v0.3.6 semantic trunk through concrete Operational Architecture and, only when candidate evidence justifies it, to a new Current release.

Fast-moving execution state lives in `research/plans/PROGRESS.yaml` on the branch named by `research/ACTIVE-RESEARCH.yaml`.

Latest standardized session handoff is routed by:

`research/handoffs/CURRENT-HANDOFF.yaml`

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
3. `research/handoffs/CURRENT-HANDOFF.yaml` and the pointed handoff package;
4. `research/ACTIVE-RESEARCH.yaml`;
5. `research/methodology/README.md` and canonical focused methods;
6. this master plan;
7. active-branch `research/RESEARCH-START-HERE.md`;
8. active-branch `research/plans/PROGRESS.yaml`;
9. the exact candidate/reconciliation/evidence artifacts required by the next action.

Do not infer active work from branch names, recency, or old PR numbers.

## Current aligned posture — 2026-08-27

Current remains:

```text
v0.3.6 / CURRENT / FIELD_VALIDATION
```

Next release line:

`v0.3.7`

Candidate.0 exists and is frozen:

```text
candidate = v0.3.7-candidate.0
frozen source = d0e793593184740d9732902e948afd48ed96ae2f
frozen candidate subtree = cffbf76fe1448b020b637c78d1f7ae46e4c0115b
```

External freeze record:

`collaboration/reconciliation/2026-08-27-v037-candidate0-freeze.md`

Exact pre-freeze validation run:

`33011823923 / SUCCESS`

Fresh independent semantic falsification is pending.

The canonical convergence/divergence method was added after the user challenged an unverified author claim that reducing an observed 1080 pass conditions to 188 structured pass conditions was epistemically better.

```text
COMPRESS REPRESENTATION != COMPRESS POSSIBILITY SPACE
PROVEN_BEHAVIORAL_EQUIVALENCE -> MAY_COMPRESS
UNPROVEN_EQUIVALENCE -> DO_NOT_COLLAPSE
UNKNOWN_SPACE -> EXPAND
```

Immediate next action:

**tree-external 1080 -> 188 author-harness anti-ablation audit** before independent falsification.

## Project State Alignment Gate

Use `research/methodology/PROJECT-STATE-ALIGNMENT-GATE.md` after material transitions such as:

- branch handoff/cleanup;
- session/project-manager handoff;
- checkpoint merge to main;
- directory/canonical-path changes;
- material methodology/master-plan phase change;
- candidate freeze/succession/release/promotion state change.

```text
INDIVIDUAL_FILE_CORRECT != PROJECT_STATE_COHERENT
MATERIAL_TRANSITION -> ALIGN -> RESUME
```

The gate is transition-triggered, not ritual after every ordinary commit.

## Phase 1 — Research continuity and repository control

State: `BASELINE_ESTABLISHED / HANDOFF_STANDARDIZED / MAINTAIN_AS_INVARIANT`

Goal: a fresh session can identify Current, current handoff, active research branch, methodology, plan, progress, candidate identity, and next permitted work without reconstructing old conversations.

Canonical session succession method:

`research/methodology/SESSION-HANDOFF-DISCIPLINE.md`

## Phase 2 — Anti-ablation archaeology / variation recovery

State: `RECOVERY_SUFFICIENT_FOR_CURRENT_SELECTION / REOPENABLE`

Correct sequence:

```text
historical problem/HOW recovery
-> durable variation map
-> WHAT / WHY / HOW[0..N] / EVIDENCE reconstruction
-> selection only after recovery is sufficient for the decision
```

This is not a completeness proof. Reopen when new history, missing lineage, assembly contradiction, validation evidence, or field evidence changes the engineering map.

## Phase 3 — HOW branch expansion

State: `ACTIVE_WHEN_NEW_DECISION_RELEVANT_GAP_APPEARS`

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

External popularity is never selection proof.

## Phase 5 — Host binding

State: `PARTIAL / CONTINUES_WITH_FIELD_OR_CANDIDATE_NEED`

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

Prefer deterministic falsification when failure is statically reachable. Use field/mesocosm evidence only where reality can reveal decision-relevant structure not already encoded.

## Phase 7 — Operational Architecture assembly

State: `ASSEMBLED_IN_CANDIDATE0 / REOPENABLE_IF_NEW_MATERIAL_GAP_APPEARS`

Research source lives under:

`research/operational-architecture/`

Candidate.0 contains release-local traversal:

```text
ordinary problem / semantic cue
-> consequence-first routing
-> CUE-INDEX
-> WHAT/WHY node
-> plural HOW branches
-> REFERENCE-INDEX
-> bounded procedure / optional reference / Host-native HOW
-> action or honest residual
```

Bounded procedures/patterns include:

- Purpose-Relative Continuity;
- Standing Input;
- Control Retirement;
- Evolution Commons layering;
- Host mapping guidance.

Assembly being present in candidate.0 is not proof of universal Host fitness or fresh-session salience.

## Phase 8 — Release scope reconciliation

State: `STABLE_AND_REALIZED_IN_FROZEN_CANDIDATE0`

Canonical workspace:

`research/release-scope/`

v0.3.7 scope stabilized with no demonstrated need for new Constitution IDs merely to create the candidate.

Selected candidate classes include:

- adopter-facing Operational Architecture;
- optional general references: Retrieval, WAIT, Authority, Effect, Recovery;
- advanced/specialized optional references: Evidence Envelope, Evidence Dependency Map, Contested Authorship;
- minimal v2-compatible evolution helper as default practical tooling;
- legacy v1.2 tool/probes retained under explicit legacy packaging;
- zh-CN operational guidance and paired route fixtures.

Deferred is not retired. In particular recovered Commitment/Settlement remains durable research lineage and is not bundled in candidate.0.

```text
NO_NEW_CORE_RULES != NO_RELEASE_VALUE
LARGE_RESEARCH_TREE != SHIP_EVERYTHING
```

## Phase 9 — Candidate build, freeze, validation, and succession

State: `CANDIDATE0_FROZEN / VALIDATION_ANTI_ABLATION_AUDIT_NEXT / INDEPENDENT_FALSIFICATION_PENDING`

Completed:

1. candidate.0 built as a self-contained subtree outside `releases/current/`;
2. Operational Architecture/reference/tool/language cargo assembled;
3. deterministic machine validation executed;
4. author adversarial and identity/projection defects repaired while preserving occurrence truth;
5. exact pre-freeze validation recomposed on one exact source/tree;
6. external freeze record bound candidate.0 immutable identity;
7. fresh independent validator handoff prepared.

Current correction required before independent validation:

### Validation anti-ablation audit

The earlier and newer author harnesses produced observed pass-condition counts of 1080 and 188 respectively. Counts are not evidence of better or worse coverage.

Before independent review:

```text
recover materially distinct predecessor attack/failure shapes
-> map each to newer harness
-> explicit disposition
```

Valid dispositions include:

```text
PRESERVED
MERGED_AS_PROVEN_EQUIVALENT
REPLACED_BY_STRONGER_ORACLE
RETAINED_OUTSIDE_CURRENT_HARNESS
RETIRED_WITH_EVIDENCE
LOST
UNKNOWN
```

`LOST` and `UNKNOWN` are not successful simplification.

Do not modify frozen candidate.0 merely to repair validator coverage.

If restored attack coverage exposes a material candidate-byte defect:

```text
candidate.0 remains frozen lineage
-> candidate.1 only if candidate bytes require correction
```

If candidate.0 survives the recovered attack space, proceed to a clearly labeled `DO NOT MERGE / INDEPENDENT FALSIFICATION` review PR bound to the exact frozen source/tree.

Fresh validator protocol:

```text
Phase A: independent inspection before accepting author oracle
Phase B: compare independent findings with author evidence
```

Candidate succession stops only when another candidate round cannot plausibly change the release decision.

## Phase 10 — Release and promotion

State: `NOT_STARTED`

Only after independent falsification and reconciliation support release:

- decide candidate succession stop or create candidate.1 as evidence requires;
- create governed release surface/branch;
- package exact validated candidate bytes;
- verify file-set/hash parity and release identity;
- run required CI/security/regression checks;
- publish/read back artifacts where applicable;
- promote through release discipline;
- verify post-merge `releases/current/` identity;
- update project/history/control/handoff pointers;
- run Project State Alignment Gate again.

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
HANDOFF_PACKAGE != PROJECT_AUTHORITY
SESSION_CONTINUITY != PROJECT_CONTINUITY
MATERIAL_TRANSITION -> ALIGN -> RESUME
RECOVERY_SUFFICIENT_FOR_ASSEMBLY != ARCHAEOLOGY_COMPLETE_FOREVER
ASSEMBLY != CURRENT_PROMOTION
NO_NEW_CORE_RULES != NO_RELEASE_VALUE
COMPRESS_REPRESENTATION != COMPRESS_POSSIBILITY_SPACE
PROVEN_BEHAVIORAL_EQUIVALENCE_REQUIRED_BEFORE_MATERIAL_COLLAPSE
FROZEN != INDEPENDENTLY_VALIDATED != RELEASED != CURRENT
```

## Progress carrier

Fast-moving execution belongs in:

`research/plans/PROGRESS.yaml`

This master plan changes only when the long-horizon phase model or closure criteria materially change.
