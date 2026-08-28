# ENA Project Hub

Status: `PROJECT_ENTRYPOINT / CURRENT_POINTER / RESEARCH_CONTROL_POINTER / HANDOFF_POINTER`

Project: **Evolution-Native Agent Architecture (ENA)**

This is the stable entrypoint for adoption, project continuation, research, review, contribution, and release work.

## Canonical adoption pointer

For adoption, always start from repository `main` and read:

`releases/current/CURRENT-BASELINE.yaml`

Never infer Current from the highest-looking version, candidate/release branch, branch recency, handoff record, or research state.

Current remains:

```text
v0.3.6 / CURRENT / FIELD_VALIDATION
```

until an exact reviewed v0.3.7 release head is explicitly promoted and post-merge read back.

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

Live project state verified on 2026-08-28:

```text
Current                     = v0.3.6 / CURRENT / FIELD_VALIDATION
main release-prep checkpoint = 280a8b0f7629d5deb013a5257cb74759213e8080
frozen candidate             = v0.3.7-candidate.3
frozen source                = b7e88d7adb70396bd671ca97066daf2c120e0adc
frozen subtree               = e3a9a20d16cecd78df7f32f19fca56e21159e810
candidate succession         = STOP
release preparation          = SUPPORTED
release branch               = release/v0.3.7
byte-exact transplant commit = 8e4e25a8ba1940560fc55d7528ad31ef89a7f135
transplanted Current tree    = e3a9a20d16cecd78df7f32f19fca56e21159e810
release identity transform   = NOT YET APPLIED
release PR / promotion       = NOT YET AUTHORIZED
```

The first release-branch occurrence is deliberately still candidate-shaped: `releases/current/` contains the frozen candidate.3 bytes exactly, including `CANDIDATE-BASELINE.yaml`. That is packaging evidence, not Current adoption authority.

## Immediate permitted next action

After this project-state alignment is main-visible:

`RELEASE_IDENTITY_STATUS_PACKAGING_ON_RELEASE_V0_3_7`

Required sequence:

```text
BYTE-EXACT TRANSPLANT (already recorded)
-> identity/status-only release projection
-> CURRENT-BASELINE.yaml replaces CANDIDATE-BASELINE.yaml
-> exact-head release validation / Main Gate / CodeQL / regressions
-> package/tree/readback evidence
-> explicit authorization on the exact reviewed release head
-> merge
-> post-merge Current readback
-> project-control/handoff/history alignment
```

A material defect in frozen candidate.3 semantics/bytes would require candidate.4. A packaging defect is repaired on the release surface without rewriting frozen candidate.3 occurrence truth.

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

GitHub write access, candidate authorship, validation work, or release-branch access does not by itself establish promotion authority.

> Preserve one legible Current, many recoverable experiments/candidates, and enough method that the next project manager can continue without reconstructing the project from chat.
