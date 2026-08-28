# ENA Reconstruction-to-Release Master Plan

Status: `ACTIVE_MASTER_PLAN / MAIN_VISIBLE_PROJECT_CONTROL / V0_3_7_RELEASED_FIELD_VALIDATION`

Updated: 2026-08-28

This is the stable long-horizon plan for evolving ENA from a semantic trunk through concrete Operational Architecture, falsification, release, field evidence, and future evolution. Fast-moving execution state lives in `research/plans/PROGRESS.yaml`.

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

## Current aligned posture — 2026-08-28 post-promotion

```text
Current                         = v0.3.7 / CURRENT / FIELD_VALIDATION
Current tree                    = f33e73ed997c1b66a4572685ab5474182e136e97
Current file count              = 118
package SHA-256                 = 40d4dde277d54ce8252e0402e32f900fa7ab4fb0aeaa638b898073d0f02f848c
exact reviewed release head     = 3ef3605228ed427b2d25d7d586e4ffc378b7369e
release PR                      = #144 / MERGED
release merge commit            = 50a4bb06b98dc0dd719230f71ed1d47e42e1fad9
Exact Release Gate              = 33162550145 PASS
post-merge Main Gate            = 33163171275 PASS
post-merge Current validation   = 33163171328 PASS
post-merge CodeQL               = 33163171289 PASS
active field tracker            = #150
```

Frozen release-source lineage remains:

```text
identity = v0.3.7-candidate.3
source   = b7e88d7adb70396bd671ca97066daf2c120e0adc
subtree  = e3a9a20d16cecd78df7f32f19fca56e21159e810
exact pre-freeze run     = 33150269264 PASS
targeted post-freeze run = 33150553992 PASS
release hardening run    = 33152201566 PASS
candidate succession     = STOP
candidate.4              = NOT JUSTIFIED BY CURRENT EVIDENCE
attack cardinality       = OPEN
```

## Project State Alignment Gate

```text
INDIVIDUAL_FILE_CORRECT != PROJECT_STATE_COHERENT
MATERIAL_TRANSITION -> ALIGN -> RESUME
```

The v0.3.7 lifecycle required alignment during release preparation and again after promotion. Post-promotion alignment updates project/control/history/field routing while leaving the immutable released Current package unchanged.

## Phase 1 — Research continuity and repository control

State: `BASELINE_ESTABLISHED / SUCCESSION_FRAMEWORK_STANDARDIZED / MAINTAIN_AS_INVARIANT`

Project-manager continuity requires state + method + governance + decision lineage + next action. Handoff records accelerate succession but never override live project authorities.

## Phase 2 — Anti-ablation archaeology / variation recovery

State: `RECOVERY_SUFFICIENT_FOR_V0_3_7 / REOPENABLE`

Relevant historical variation was recovered sufficiently for the v0.3.7 decision. This is not a forever-complete ontology claim. Reopen when new lineage/evidence could change a decision.

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

State: `ACTIVE_FIELD_EVIDENCE`

Possible dispositions include Host-native organ, adapter, reference implementation, bounded procedure, inapplicable, and unknown. One Host result does not establish universal fitness.

## Phase 6 — Cross-organ composition

State: `ACTIVE_WHERE_DECISION_RELEVANT`

Preserve boundaries that materially change action, authority, evidence, recovery, source/receiver semantics, or failure behavior. Use deterministic falsification for statically reachable defects; use field evidence where reality can reveal non-derivable structure.

## Phase 7 — Operational Architecture assembly

State: `RELEASED_IN_V0_3_7 / REOPENABLE_IF_NEW_MATERIAL_GAP_APPEARS`

v0.3.7 provides consequence-first routing from cue/problem to WHAT/WHY, plural HOWs, references/procedures/Host mappings, and bounded action or honest residual.

## Phase 8 — Release scope reconciliation

State: `COMPLETE_FOR_V0_3_7`

v0.3.7 preserves all 38 Constitution IDs while adding operational, optional-reference, tooling, and zh-CN adoption value.

```text
NO_NEW_CORE_RULES != NO_RELEASE_VALUE
BUNDLED_REFERENCE != REQUIRED_RUNTIME_ORGAN
DEFERRED != RETIRED
```

## Phase 9 — Candidate build, freeze, validation, and succession

State: `COMPLETE / CANDIDATE3_FROZEN / SUCCESSION_STOP`

```text
candidate.0 -> candidate.1 -> candidate.2 -> candidate.3 -> STOP
```

Candidate.2 fresh A-S/A-P materially changed the release decision and required candidate.3. Candidate.3 completed bounded successor repairs, exact pre-freeze validation, external freeze, targeted post-freeze replay, and release hardening. Candidate.4 is justified only by new material candidate-byte evidence; it is not a ceremonial generation.

## Phase 10 — Release and promotion

State: `COMPLETE / V0_3_7_CURRENT / POSTMERGE_READBACK_PASS`

Completed sequence:

1. candidate.3 frozen and hardening evidence persisted;
2. governed `release/v0.3.7` created from main checkpoint;
3. frozen candidate.3 transplanted byte-for-byte into `releases/current/` at `8e4e25a8ba1940560fc55d7528ad31ef89a7f135`;
4. release-only identity/status/adopter/Operational/zh-CN/reference-wrapper projection applied without rewriting frozen candidate.3;
5. long-lived v0.3.7-aware Current validation/package machinery installed;
6. Selection Qualification oracle drift repaired separately rather than weakening v0.3.7 semantics;
7. Exact Release Gate hardened to rerun on every release-branch push;
8. final exact release head `3ef3605228ed427b2d25d7d586e4ffc378b7369e` passed required gates;
9. deterministic 118-file package read back at SHA-256 `40d4dde277d54ce8252e0402e32f900fa7ab4fb0aeaa638b898073d0f02f848c`;
10. explicit promotion authorization obtained;
11. PR #144 merged using exact-head protection as `50a4bb06b98dc0dd719230f71ed1d47e42e1fad9`;
12. main readback re-established Current tree `f33e73ed997c1b66a4572685ab5474182e136e97`;
13. post-merge Main Gate, Current validation/package, and CodeQL passed;
14. v0.3.7 field-validation tracker #150 opened; v0.3.6 tracker #70 closed as predecessor occurrence evidence.

## Released-package erratum

One sentence in `releases/current/CURRENT-BASELINE.yaml` under `accepted_residuals` still states the pre-promotion condition that v0.3.6 remains the sole adopter-facing baseline until explicit promotion. Promotion has occurred.

Do not silently mutate the released v0.3.7 118-file package. Its Release Discipline states `same ena_version -> same effective content`. The stale sentence is therefore recorded as a release-metadata erratum outside Current; top-level baseline identity plus governed promotion establishes v0.3.7 Current. Correct it only under a future governed release identity.

## Phase 11 — v0.3.7 field validation and next evolution

State: `ACTIVE / REALITY_CONTACT / OPEN_CARDINALITY`

Primary active field stream: GitHub Issue `#150`.

Still-open reconstruction/research trackers: `#89`–`#94`, `#104`.

Select work because it can expose a mechanism, failure boundary, Host dependency, operational economics result, or decision-changing counterexample—not to generate diverse-looking outputs or satisfy arbitrary counts.

High-value domains include natural cue -> cold-HOW retrieval/application, false-BLOCK controls, Purpose-Relative Continuity, Standing Input, Control Retirement, Evolution Commons, Host Mapping, optional reference applicability, Authority/Effect/Recovery composition, v2 practical helper behavior, EN/zh-CN operational behavior, and unexpected failure shapes.

## Issue and branch closure

Open issue count is not a release quality metric. Keep unresolved research obligations open while they remain useful.

Branch names are lifecycle surfaces, not archives. Preserve decision lineage in commits/trees/PRs/reconciliation/evidence, then remove stale release/candidate/validation/tmp/integration/control-fix refs when their lifecycle has ended. The active `research/ena-reconstruction` branch remains continuation authority because the canonical pointer names it. The current connector lacks true delete-ref support, so cleanup must not be simulated by force-moving refs.

## Independent validation infrastructure

`guytogay/independent-validation-cleanroom` is reusable validation infrastructure across ENA stages and unrelated projects. Its repository identity is reusable infrastructure; its stage contents are ephemeral. Durable occurrence truth returns to each source project.

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
MATERIAL_TRANSITION -> ALIGN -> RESUME
FROZEN != INDEPENDENTLY_VALIDATED != RELEASED != CURRENT
OPEN_RESEARCH_ISSUE != RELEASE_BLOCKER_BY_DEFAULT
BRANCH_EXISTS != CONTINUATION_AUTHORITY
```

## Closure rule

Research stops, transitions, or releases because another bounded step no longer has plausible decision-changing value—not because an arbitrary count was reached.

> The final test remains whether an Agent can actually live by the architecture, while the project remains truthful about exactly what has and has not been established.
