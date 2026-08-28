# ENA v0.3.7 — Release-transplant Project State Alignment

Date: 2026-08-28

Status: `PROJECT_STATE_ALIGNMENT / LIVE_REVERIFICATION_COMPLETE / CONTROL_SURFACES_REPAIRED / RELEASE_BYTES_UNTOUCHED`

## Role

`SUCCESSOR_PROJECT_MANAGER / LIVE_STATE_REVERIFIER / NOT_FRESH_INDEPENDENT_VALIDATOR / NOT_RELEASE_PROMOTION_AUTHORITY`

This record captures the Project State Alignment Gate performed during session takeover after the candidate.3 release-preparation handoff.

## Trigger

The dated handoff record described the next action as:

`MAIN_VISIBLE_CHECKPOINT_THEN_CREATE_RELEASE_V0_3_7_AND_TRANSPLANT_FROZEN_CANDIDATE3`

Live GitHub inspection showed that all three of those operations had already happened after the handoff snapshot:

1. candidate.3 freeze/hardening/release-preparation state was merged to `main`;
2. `release/v0.3.7` was created from that exact main checkpoint;
3. frozen candidate.3 was transplanted byte-for-byte into the release branch `releases/current/` surface.

Several main-visible current-tense control documents still described candidate.0/candidate.2, fresh Phase A, or release preparation as not started. Therefore:

```text
INDIVIDUAL_FILE_CORRECT_AT_T != PROJECT_STATE_COHERENT_AT_T_PLUS_1
MATERIAL_TRANSITION -> ALIGN -> RESUME
```

## Independently reverified live facts

### Current

`v0.3.6 / CURRENT / FIELD_VALIDATION`

Current subtree:

`7dcbb3934883ffa6cc5292a662588cafc1533cff`

No release-preparation operation changed `main/releases/current/`.

### Main checkpoint

`280a8b0f7629d5deb013a5257cb74759213e8080`

Commit purpose:

`Candidate.3 freeze, hardening, and v0.3.7 release-preparation checkpoint`

### Frozen release source

- identity: `v0.3.7-candidate.3`
- frozen source / live candidate.3 branch head: `b7e88d7adb70396bd671ca97066daf2c120e0adc`
- frozen subtree: `e3a9a20d16cecd78df7f32f19fca56e21159e810`
- exact pre-freeze run: `33150269264` PASS
- targeted post-freeze run: `33150553992` PASS
- release hardening run: `33152201566` PASS
- candidate succession: STOP
- candidate.4 currently justified: NO

### Release packaging occurrence

Release branch:

`release/v0.3.7`

Created from exact main checkpoint:

`280a8b0f7629d5deb013a5257cb74759213e8080`

Byte-exact transplant commit:

`8e4e25a8ba1940560fc55d7528ad31ef89a7f135`

At that commit:

```text
releases/current tree
= e3a9a20d16cecd78df7f32f19fca56e21159e810
= frozen candidate.3 subtree
```

The release surface still contains `CANDIDATE-BASELINE.yaml` and does not yet contain `CURRENT-BASELINE.yaml`, confirming that the first release occurrence is the required pure transplant and that identity/status projection has not yet been mixed into it.

No release PR and no release-branch workflow run were observed at takeover verification time.

## Drift found

Current-tense drift existed in:

- `PROJECT-HUB.md`;
- `PROJECT-STRUCTURE.md`;
- `research/README.md`;
- `research/BRANCH-INVENTORY.yaml`;
- `research/plans/PROGRESS.yaml` internal phase projections;
- `research/plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md`;
- `research/ACTIVE-RESEARCH.yaml` immediate phase projection;
- `research/RESEARCH-START-HERE.md` immediate next action;
- `research/handoffs/CURRENT-HANDOFF.yaml` live next-action projection.

The dated handoff record remains unchanged as occurrence truth.

## Alignment repair

The active integration branch now projects one coherent current story:

```text
Current = v0.3.6
candidate.3 = frozen immutable release source
candidate succession = STOP
release/v0.3.7 = active packaging workspace
byte-exact transplant = COMPLETE
identity/status transform = PENDING
release authorization/promotion = NOT STARTED
next after main-visible alignment = RELEASE_IDENTITY_STATUS_PACKAGING_ON_RELEASE_V0_3_7
```

`PROGRESS.yaml` was deliberately compressed into a current fast-state projection because it explicitly is not complete history. Predecessor candidate/validator detail remains recoverable in handoff records, reconciliation files, issues, immutable commits/trees, and Git history.

```text
COMPRESS REPRESENTATION != COMPRESS POSSIBILITY SPACE
```

## Independent-validation infrastructure clarification

The reusable repository:

`guytogay/independent-validation-cleanroom`

is classified as:

`REUSABLE_CROSS_STAGE_CROSS_PROJECT_VALIDATION_INFRASTRUCTURE`

Its repository identity is reusable infrastructure. Its contents are disposable current-stage review state. It may be reset and reused for different ENA validation occurrences and for unrelated projects. Long-lived reports, seals, and occurrence truth belong back in the relevant source project rather than accumulating as authority in the clean room.

This clarification is consistent with the existing isolated-carrier method, which already requires clean-room stage reset and preventing previous-project context from leaking into a fresh review surface.

## Mutation boundary

This alignment changes project-control/research/handoff projections only.

It does **not** modify:

- `main/releases/current/`;
- frozen candidate.3 bytes;
- `release/v0.3.7` transplant commit or tree;
- any sealed validation occurrence.

## Closure condition

Before this alignment is considered main-visible complete:

1. compare the active integration head with main and verify only intended project-control/method/evidence files changed;
2. review the alignment PR exact head;
3. merge the alignment checkpoint to main;
4. read back exact main state;
5. only then resume release identity/status packaging on `release/v0.3.7`.

## Next permitted substantive action after alignment merge

`RELEASE_IDENTITY_STATUS_PACKAGING_ON_RELEASE_V0_3_7`

The release branch remains non-Current and non-authoritative until exact-head gates, explicit release authorization, merge, and post-merge Current readback complete.
