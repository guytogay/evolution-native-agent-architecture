# ENA Reconstruction-to-Release Master Plan

Status: `ACTIVE_MASTER_PLAN / MAIN_VISIBLE_PROJECT_CONTROL / V0_3_7_PREPROMOTION_RELEASE_READINESS`

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

## Current aligned posture — 2026-08-28 pre-promotion

Current remains:

```text
v0.3.6 / CURRENT / FIELD_VALIDATION
Current tree = 7dcbb3934883ffa6cc5292a662588cafc1533cff
```

Final frozen candidate:

```text
identity = v0.3.7-candidate.3
source   = b7e88d7adb70396bd671ca97066daf2c120e0adc
subtree  = e3a9a20d16cecd78df7f32f19fca56e21159e810
exact pre-freeze run     = 33150269264 PASS
targeted post-freeze run = 33150553992 PASS
release hardening run    = 33152201566 PASS
candidate succession     = STOP
candidate.4              = NOT JUSTIFIED BY CURRENT EVIDENCE
```

The governed release sequence has advanced through packaging and exact-head validation:

```text
release branch                  = release/v0.3.7
release PR                      = #144 / OPEN DRAFT / NOT PROMOTED
byte-exact transplant commit    = 8e4e25a8ba1940560fc55d7528ad31ef89a7f135
prospective Current tree        = f33e73ed997c1b66a4572685ab5474182e136e97
exact validated release head    = bcda18a28141f572688f9a1b15cfd820dea02f97
prospective Current file count  = 118
package SHA-256                 = 40d4dde277d54ce8252e0402e32f900fa7ab4fb0aeaa638b898073d0f02f848c
Exact Release Gate              = 33161514271 PASS
Current validate/package        = 33161516641 PASS
Main Gate                       = 33161516581 PASS
Selection Qualification         = 33161516591 PASS
research helper                 = 33161516586 PASS
CodeQL                          = 33161516568 PASS
```

Release readiness does not change Current and does not mint promotion authority. The next material decision is explicit promotion on an exact release head that has been synchronized with this main-visible alignment and revalidated.

## Project State Alignment Gate

Run `research/methodology/PROJECT-STATE-ALIGNMENT-GATE.md` after material branch, candidate, release, methodology, handoff, plan, or control-plane transitions.

```text
INDIVIDUAL_FILE_CORRECT != PROJECT_STATE_COHERENT
MATERIAL_TRANSITION -> ALIGN -> RESUME
```

The 2026-08-28 release transition triggered this gate twice: first when the governed release branch/transplant became live, and again after identity projection, release PR creation, Selection Qualification oracle reconciliation, and exact release-gate hardening advanced beyond the main-visible state projections. This pre-promotion alignment must land on `main` before the final release head is presented for promotion authorization.

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

State: `PREPROMOTION_READY / PROSPECTIVE_CURRENT_PAYLOAD_VALIDATED / NOT_AUTHORIZED / NOT_PROMOTED`

Completed:

1. candidate.3 freeze/revalidation/hardening/control checkpoint merged to `main`;
2. governed `release/v0.3.7` created;
3. frozen candidate.3 transplanted byte-for-byte into `releases/current/` at commit `8e4e25a8ba1940560fc55d7528ad31ef89a7f135`;
4. byte-exact transplant tree verified against frozen candidate.3 subtree `e3a9a20d16cecd78df7f32f19fca56e21159e810`;
5. release identity/status/adopter/Operational/zh-CN/reference-wrapper projection completed while bounded frozen executable/reference-machine surfaces remained byte-bound to candidate.3;
6. `CANDIDATE-BASELINE.yaml` replaced by truthful prospective `CURRENT-BASELINE.yaml` on the release branch;
7. long-lived v0.3.7-aware Current validation/package machinery installed and construction-only release scripts removed;
8. release PR #144 opened as draft;
9. a Selection Qualification failure was classified as research oracle drift rather than candidate defect, repaired separately in PR #145, merged to `main`, and synchronized through PR #146 without changing the prospective Current tree;
10. Exact Release Gate trigger semantics hardened so every push to `release/v0.3.7` reruns the gate;
11. exact release head `bcda18a28141f572688f9a1b15cfd820dea02f97` passed Exact Release Gate, Current validate/package, Main Gate, Selection Qualification, research helper, and CodeQL;
12. the validated prospective Current tree is `f33e73ed997c1b66a4572685ab5474182e136e97`; deterministic 118-file package SHA-256 is `40d4dde277d54ce8252e0402e32f900fa7ab4fb0aeaa638b898073d0f02f848c`.

Remaining sequence:

1. merge the pre-promotion Project State Alignment checkpoint to `main`;
2. synchronize that aligned main control plane into `release/v0.3.7` without changing prospective Current payload semantics;
3. rerun Exact Release Gate and ordinary PR checks on the resulting exact release head;
4. reverify prospective Current tree and deterministic package digest stability;
5. present the exact reviewed release head plus open evidence boundaries for explicit promotion authorization;
6. only after explicit authorization merge PR #144;
7. reverify `releases/current/` identity/tree from `main`;
8. update Current metadata/history/field-validation routing, issue relations, branch lifecycle state, and handoff/control projections;
9. run Project State Alignment Gate again to close promotion.

Current remains v0.3.6 until step 6 is merged and step 7 is positively read back.

## Issue and branch closure

Open issue count is not a release quality metric. Reconstruction/workstream issues `#89`–`#94` and `#104` remain open while their research obligations remain meaningful. Issue `#70` is bound to the v0.3.6 field-validation stream and should be superseded or reframed after v0.3.7 promotion.

Branch names are short-lived lifecycle surfaces, not durable archives. Preserve decision lineage in commits/trees/PRs/reconciliation/evidence, then remove stale candidate/validation/tmp/integration/release refs when their lifecycle has ended. Do not delete the active research pointer branch or frozen candidate.3 before release lineage/readback is durable. The current GitHub connector lacks a true delete-ref operation, so cleanup disposition is recorded without simulating deletion through force-moves.

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
GREEN_RELEASE_GATE != PROMOTION_AUTHORITY
BYTE_EXACT_TRANSPLANT != RELEASE_IDENTITY_TRANSFORM
OPEN_RESEARCH_ISSUE != RELEASE_BLOCKER_BY_DEFAULT
BRANCH_EXISTS != CONTINUATION_AUTHORITY
```

## Closure rule

Research/release work stops or transitions because another bounded step no longer has plausible decision-changing value, not because an arbitrary count was reached.

> The final test remains whether an Agent can actually live by the architecture, while the release process remains truthful about exactly what has and has not been established.
