# ENA Reconstruction-to-Release Master Plan

Status: `ACTIVE_MASTER_PLAN / MAIN_VISIBLE_PROJECT_CONTROL / V0_3_7_RELEASE_PACKAGING`

Updated: 2026-08-28

This is the stable long-horizon plan for evolving ENA from the v0.3.6 semantic trunk through concrete Operational Architecture, falsification, candidate succession, release packaging, and eventual promotion.

Fast-moving execution state lives in `research/plans/PROGRESS.yaml`.

## Goal

ENA must be inhabitable, not merely explainable.

```text
TELOS / PURPOSE
      |
      v
WHAT / WHY
stable semantic trunk; abstraction/compression may help
      |
      +--> HOW-A
      +--> HOW-B
      +--> HOW-C
      +--> ...
             |
             +--> Host binding / adapter
             +--> failure / fallback / non-applicability
             +--> evidence
```

```text
ONE_WHAT_WHY -> 0..N_CONCRETE_HOW_BRANCHES
COMPRESS REPRESENTATION != COMPRESS POSSIBILITY SPACE
```

## Continuation control plane

A successor project manager starts from `main`, resolves Current, handoff framework/current record, required methodology, active research pointer, Progress/master plan, and then independently reverifies live refs and exact governed identities before writing.

A fresh independent validator is a different role and must not receive full project-manager continuity context before fresh A-S findings are sealed.

## Current aligned posture — 2026-08-28

Current remains:

`v0.3.6 / CURRENT / FIELD_VALIDATION`

Final frozen candidate:

```text
identity = v0.3.7-candidate.3
source   = b7e88d7adb70396bd671ca97066daf2c120e0adc
subtree  = e3a9a20d16cecd78df7f32f19fca56e21159e810
exact pre-freeze run     = 33150269264 PASS
targeted post-freeze run = 33150553992 PASS
release hardening run    = 33152201566 PASS
candidate succession     = STOP
release preparation      = SUPPORTED
```

The governed release sequence has begun:

```text
main checkpoint = 280a8b0f7629d5deb013a5257cb74759213e8080
release branch  = release/v0.3.7
transplant head = 8e4e25a8ba1940560fc55d7528ad31ef89a7f135
releases/current tree at transplant = e3a9a20d16cecd78df7f32f19fca56e21159e810
```

The transplant is byte-exact and deliberately still candidate-shaped. Release identity/status transformation is the next substantive release step after project-state alignment is main-visible.

## Project State Alignment Gate

Run `research/methodology/PROJECT-STATE-ALIGNMENT-GATE.md` after material branch, candidate, release, methodology, handoff, plan, or control-plane transitions.

```text
INDIVIDUAL_FILE_CORRECT != PROJECT_STATE_COHERENT
MATERIAL_TRANSITION -> ALIGN -> RESUME
```

The 2026-08-28 transition from candidate.3 freeze/hardening to an active release branch triggered this gate because several current-state projections still described candidate.0/.2 and pre-release Phase A. The alignment checkpoint must land on `main` before release identity packaging resumes.

## Phase 1 — Research continuity and repository control

State: `BASELINE_ESTABLISHED / SUCCESSION_FRAMEWORK_STANDARDIZED / MAINTAIN_AS_INVARIANT`

A fresh project-manager session must identify Current, active research branch, handoff framework/record, methodology, project state, exact governed identities, and first permitted next action without reconstructing chat history.

## Phase 2 — Anti-ablation archaeology / variation recovery

State: `RECOVERY_SUFFICIENT_FOR_CURRENT_RELEASE_DECISION / REOPENABLE`

Relevant variation was recovered sufficiently for v0.3.7 selection. This is not a forever-complete ontology claim. Reopen if new lineage or evidence could change a decision.

## Phase 3 — HOW branch expansion

State: `ACTIVE_ON_DEMAND`

Concrete HOWs may coexist, specialize, recombine, become dormant, or retire with evidence. Do not preallocate mechanism count.

## Phase 4 — External HOW harvest

State: `ACTIVE_ON_DEMAND`

```text
ENA failure
-> external mechanism search
-> mechanism extraction
-> ENA/Host mapping
-> falsification/comparison
-> retain/specialize/reject
```

Popularity is not selection proof.

## Phase 5 — Host binding

State: `PARTIAL / FIELD_CONTINUES`

Possible dispositions include Host-native organ, adapter, reference implementation, bounded procedure, inapplicable, and unknown. One Host result does not establish universal fitness.

## Phase 6 — Cross-organ composition

State: `ACTIVE_WHERE_DECISION_RELEVANT`

Preserve boundaries that materially change action, authority, evidence, recovery, source/receiver semantics, or failure behavior. Use deterministic falsification for statically reachable defects; use field evidence where reality can reveal non-derivable structure.

## Phase 7 — Operational Architecture assembly

State: `ASSEMBLED_IN_FROZEN_CANDIDATE3 / REOPENABLE_IF_NEW_MATERIAL_GAP_APPEARS`

The candidate contains release-local consequence-first routing from cue/problem to WHAT/WHY, plural HOWs, references/procedures/Host mappings, and bounded action or honest residual.

## Phase 8 — Release scope reconciliation

State: `STABLE_AND_REALIZED_IN_FROZEN_CANDIDATE3`

v0.3.7 preserves the v0.3.6 semantic trunk while adding material operational, optional-reference, tooling, and zh-CN adoption value without demonstrating a need for new Constitution IDs.

```text
NO_NEW_CORE_RULES != NO_RELEASE_VALUE
BUNDLED_REFERENCE != REQUIRED_RUNTIME_ORGAN
DEFERRED != RETIRED
```

## Phase 9 — Candidate build, freeze, validation, and succession

State: `COMPLETE / CANDIDATE3_FROZEN / SUCCESSION_STOP`

Lineage:

```text
candidate.0 -> candidate.1 -> candidate.2 -> candidate.3
```

Candidate.2's fresh A-S/A-P cycle materially changed the release decision and required candidate.3. Candidate.3 then completed bounded successor repairs, exact pre-freeze validation, external freeze, targeted post-freeze replay, and release hardening without a demonstrated new material frozen-byte defect.

Candidate.4 is not ceremonial. It becomes justified only if new material evidence requires candidate-byte correction.

Attack cardinality remains open; stopping candidate succession does not mean all possible failures are known.

## Phase 10 — Release and promotion

State: `IN_PROGRESS / BYTE_EXACT_TRANSPLANT_COMPLETE / IDENTITY_STATUS_TRANSFORM_PENDING`

Completed:

1. candidate.3 freeze/revalidation/hardening/control checkpoint merged to `main` at `280a8b0f7629d5deb013a5257cb74759213e8080`;
2. governed `release/v0.3.7` created from that checkpoint;
3. frozen candidate.3 transplanted byte-for-byte into `releases/current/` at commit `8e4e25a8ba1940560fc55d7528ad31ef89a7f135`;
4. transplant tree independently verified as `e3a9a20d16cecd78df7f32f19fca56e21159e810`, exactly matching the frozen candidate.3 subtree.

Next:

1. perform release identity/status-only projection on `release/v0.3.7`;
2. replace `CANDIDATE-BASELINE.yaml` with truthful `CURRENT-BASELINE.yaml`;
3. preserve validated candidate.3 material semantics, 38 Constitution IDs, Authority/Effect/migration repairs, optionality, and evidence boundaries;
4. run exact-head release validation, Main Gate, CodeQL/security/regression, identity and package/file-set parity checks;
5. create/review the release PR on the exact prepared head;
6. explicitly authorize merge only after exact-head evidence is satisfactory;
7. merge and reverify `releases/current/` from `main`;
8. update history/project-control/handoff projections and close the alignment loop.

Current remains v0.3.6 until steps 1-7 complete.

## Independent validation infrastructure

`guytogay/independent-validation-cleanroom` is reusable validation infrastructure across ENA stages and unrelated projects.

```text
CLEAN_ROOM_REPOSITORY_IDENTITY = REUSABLE_VALIDATION_INFRASTRUCTURE
CLEAN_ROOM_CONTENT = CURRENT_STAGE_EPHEMERAL_REVIEW_SURFACE
```

It should be reset/replaced between occurrences; durable reports, seals, and reconciliation belong in each source project.

## Research / project-method invariants

```text
PROPERTY != ORGAN != HOST_BINDING != EVIDENCE != ADOPTION
WHAT_WHY_COVERAGE != HOW_COMPLETION
REQUESTED_N != DISCOVERED_N
WORKING_TAXONOMY != ONTOLOGY
EXPERIMENTS_MUST_PAY_EPISTEMIC_RENT
NO_CHANGE = VALID_OUTCOME
REMOVE_FROM_ACTIVE_ARCHITECTURE != ERASE_FROM_LINEAGE
HANDOFF_RECORD != PROJECT_AUTHORITY
PROJECT_STATE_INHERITANCE_WITHOUT_METHOD_INHERITANCE = INCOMPLETE_TAKEOVER
MATERIAL_TRANSITION -> ALIGN -> RESUME
FROZEN != INDEPENDENTLY_VALIDATED != RELEASED != CURRENT
RELEASE_BRANCH != CURRENT
BYTE_EXACT_TRANSPLANT != RELEASE_IDENTITY_TRANSFORM
```

## Closure rule

Research/release work stops or transitions because another bounded step no longer has plausible decision-changing value, not because an arbitrary count was reached.

> The final test remains whether an Agent can actually live by the architecture, while the release process remains truthful about exactly what has and has not been established.
