# ENA Project Hub

Status: `PROJECT_ENTRYPOINT / CURRENT_POINTER / RESEARCH_CONTROL_POINTER / HANDOFF_POINTER`

Project: **Evolution-Native Agent Architecture (ENA)**

This is the stable entrypoint for adoption, project continuation, research, review, contribution, and release work.

## Canonical adoption pointer

For adoption, always start from repository `main` and read:

`releases/current/CURRENT-BASELINE.yaml`

Never infer Current from the highest-looking version, candidate/release branch, branch recency, handoff record, research state, or passing release checks.

The active adopter-facing model is **Current + declared maturity/status**.

Current remains:

```text
v0.3.6 / CURRENT / FIELD_VALIDATION
```

until an exact reviewed v0.3.7 release head is explicitly promoted, merged, and post-merge read back from `main`.

## Project-manager continuation route

A successor session must resolve, in order:

1. `releases/current/CURRENT-BASELINE.yaml`;
2. `research/handoffs/CURRENT-HANDOFF.yaml`;
3. `research/handoffs/HANDOFF-PROTOCOL.md`;
4. `research/handoffs/REQUIRED-TAKEOVER-CONTEXT.yaml`;
5. `research/handoffs/PROJECT-MANAGEMENT-DISCIPLINE.md`;
6. the current handoff record named by the pointer;
7. required project methodology under `research/methodology/`;
8. `research/ACTIVE-RESEARCH.yaml`;
9. `research/plans/PROGRESS.yaml` and the master plan;
10. live refs/exact frozen or release identities before writing.

```text
TAKEOVER = STATE + METHOD + GOVERNANCE + DECISION_LINEAGE + NEXT_ACTION
HANDOFF_RECORD != PROJECT_AUTHORITY
BRANCH_HEAD != FROZEN_IDENTITY
```

## Current project/release posture

Pre-promotion live state verified on 2026-08-28:

```text
Current                         = v0.3.6 / CURRENT / FIELD_VALIDATION
Current tree                    = 7dcbb3934883ffa6cc5292a662588cafc1533cff
main before this alignment      = 13c8a3e359fe6702ebc15dad982c655e2a3ca7a9
frozen candidate                = v0.3.7-candidate.3
frozen source                   = b7e88d7adb70396bd671ca97066daf2c120e0adc
frozen subtree                  = e3a9a20d16cecd78df7f32f19fca56e21159e810
candidate succession            = STOP
candidate.4                     = NOT JUSTIFIED BY CURRENT EVIDENCE
release branch                  = release/v0.3.7
release PR                      = #144 / OPEN DRAFT / NOT PROMOTED
byte-exact transplant commit    = 8e4e25a8ba1940560fc55d7528ad31ef89a7f135
prospective v0.3.7 Current tree = f33e73ed997c1b66a4572685ab5474182e136e97
validated release head          = bcda18a28141f572688f9a1b15cfd820dea02f97
package file count              = 118
package SHA-256                 = 40d4dde277d54ce8252e0402e32f900fa7ab4fb0aeaa638b898073d0f02f848c
release identity projection     = COMPLETE ON RELEASE BRANCH
release authorization           = NOT GRANTED
promotion                       = NOT STARTED
```

The release branch now contains a fully projected prospective `v0.3.7 / CURRENT / FIELD_VALIDATION` package. That package is **not** Current merely because its self-description is release-ready. Current authority remains the merged/read-back `releases/current/` on `main`.

Exact-head release evidence on `bcda18a28141f572688f9a1b15cfd820dea02f97`:

```text
ENA v0.3.7 Exact Release Gate = PASS / run 33161514271
Current validate/package      = PASS / run 33161516641
Main Gate                     = PASS / run 33161516581
Selection Qualification       = PASS / run 33161516591
research helper               = PASS / run 33161516586
CodeQL                        = PASS / run 33161516568
```

The Exact Release Gate now runs on every push to `release/v0.3.7`, so a later release-head change cannot silently inherit an older green gate.

## Issue and branch closure posture

Open issues are not required to reach zero for release. The reconstruction/workstream issues `#89`–`#94` and `#104` remain durable research obligations while their work remains open; their relation to Current must be aligned after promotion. Issue `#70` is the v0.3.6 field-validation stream and should be superseded or reframed after v0.3.7 promotion rather than treated as a pre-promotion blocker by default.

Branches are governed differently: short-lived branch names should end after their lifecycle is closed and durable lineage exists. `research/ena-reconstruction`, `release/v0.3.7`, and frozen candidate.3 still have live roles before promotion/readback. Merged, operator-noise, predecessor-candidate, and historical-validation refs are classified in `research/BRANCH-INVENTORY.yaml` for cleanup. The currently available GitHub connector does not expose branch/ref deletion, so deletion must not be simulated by force-moving refs.

## Immediate permitted next action

After this pre-promotion alignment is main-visible:

```text
sync aligned main into release/v0.3.7
-> rerun Exact Release Gate and ordinary PR checks on the resulting exact head
-> prove prospective Current tree/package stability
-> present exact reviewed head + open evidence boundaries
-> obtain explicit promotion authorization
```

Only after explicit authorization:

```text
merge PR #144
-> post-merge Current readback
-> update Current/project/history/field-validation routing
-> run Project State Alignment Gate again
-> close release/candidate/temporary branch lifecycles when safe
```

A material defect in frozen candidate.3 semantics/bytes would require candidate.4. A packaging/control defect is repaired on the release/control surface without rewriting frozen candidate.3 occurrence truth.

## Independent validation clean room

`guytogay/independent-validation-cleanroom` is reusable validation infrastructure, not an ENA-candidate-specific repository.

```text
CLEAN_ROOM_REPOSITORY_IDENTITY = REUSABLE_VALIDATION_INFRASTRUCTURE
CLEAN_ROOM_CONTENT = CURRENT_STAGE_EPHEMERAL_REVIEW_SURFACE
```

It may be reused across ENA stages and across unrelated projects. Occurrence truth belongs back in the source project; clean-room stage contents should be reset/replaced rather than accumulated as project history.

## Research direction

```text
WHAT / WHY -> may compress into a stable semantic trunk
HOW -> concretize / branch / specialize / recombine
FAILURE / ADVERSARIAL SPACE -> remain open while distinct shapes remain plausible
EVIDENCE -> bind to the concrete claim / HOW / Host / applicability scope it supports
```

```text
COMPRESS REPRESENTATION != COMPRESS POSSIBILITY SPACE
ANTI_CONVERGENCE != MAXIMIZE ARTIFACT COUNT
```

## Project knowledge surfaces

- Current adoption: `releases/current/`
- Project control: `main`
- Active research pointer: `research/ACTIVE-RESEARCH.yaml`
- Active research integration branch: `research/ena-reconstruction`
- Handoff framework/current pointer: `research/handoffs/`
- Research methodology: `research/methodology/`
- Project-state alignment: `research/methodology/PROJECT-STATE-ALIGNMENT-GATE.md`
- Long-horizon plan: `research/plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md`
- Fast execution state: `research/plans/PROGRESS.yaml`
- Branch governance/inventory: `research/BRANCH-GOVERNANCE.md`, `research/BRANCH-INVENTORY.yaml`
- Reconciliation/freeze/validation evidence: `collaboration/reconciliation/`

## Authority boundary

`Contribution != Reconciliation != Release/Promotion Authority.`

GitHub write access, candidate authorship, validation work, release-branch access, or green CI does not by itself establish promotion authority.

> Preserve one legible Current, many recoverable experiments/candidates, and enough method that the next project manager can continue without reconstructing the project from chat.
