# ENA Project Hub

Status: `PROJECT_ENTRYPOINT / CURRENT_POINTER / RESEARCH_CONTROL_POINTER / HANDOFF_POINTER`

Project: **Evolution-Native Agent Architecture (ENA)**

This is the stable entrypoint for adoption, project continuation, research, review, contribution, and release work.

## Canonical adoption pointer

For adoption, always start from repository `main` and read:

`releases/current/CURRENT-BASELINE.yaml`

Never infer Current from the highest-looking version, candidate/release branch, branch recency, handoff record, research state, or passing checks.

The active adopter-facing model is **Current + declared maturity/status**.

Current is now:

```text
v0.3.7 / CURRENT / FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE
Current tree = f33e73ed997c1b66a4572685ab5474182e136e97
```

## Project-manager continuation route

A successor session resolves, in order:

1. `releases/current/CURRENT-BASELINE.yaml`;
2. `research/handoffs/CURRENT-HANDOFF.yaml` plus the canonical handoff framework;
3. the current handoff record named by that pointer;
4. required methodology under `research/methodology/`;
5. `research/ACTIVE-RESEARCH.yaml`;
6. `research/plans/PROGRESS.yaml` and the master plan;
7. live refs/exact governed identities before writing;
8. the Project State Alignment Gate whenever current surfaces disagree.

```text
TAKEOVER = STATE + METHOD + GOVERNANCE + DECISION_LINEAGE + NEXT_ACTION
HANDOFF_RECORD != PROJECT_AUTHORITY
BRANCH_HEAD != FROZEN_IDENTITY
```

## v0.3.7 promotion/readback — 2026-08-28

```text
frozen candidate identity       = v0.3.7-candidate.3
frozen source                   = b7e88d7adb70396bd671ca97066daf2c120e0adc
frozen subtree                  = e3a9a20d16cecd78df7f32f19fca56e21159e810
candidate succession            = STOP
candidate.4                     = NOT JUSTIFIED BY CURRENT EVIDENCE
byte-exact transplant commit    = 8e4e25a8ba1940560fc55d7528ad31ef89a7f135
exact reviewed release head     = 3ef3605228ed427b2d25d7d586e4ffc378b7369e
release PR                      = #144 / MERGED
release merge commit            = 50a4bb06b98dc0dd719230f71ed1d47e42e1fad9
Current tree                    = f33e73ed997c1b66a4572685ab5474182e136e97
Current file count              = 118
package SHA-256                 = 40d4dde277d54ce8252e0402e32f900fa7ab4fb0aeaa638b898073d0f02f848c
Exact Release Gate              = 33162550145 PASS
post-merge Main Gate            = 33163171275 PASS
post-merge Current validation   = 33163171328 PASS
post-merge CodeQL               = 33163171289 PASS
active field-validation tracker = #150
predecessor field tracker       = #70 / CLOSED
```

Explicit promotion authorization was received before PR #144 was merged. Post-merge readback positively re-established the same v0.3.7 Current tree on `main`.

## Immutable-package erratum

The released `CURRENT-BASELINE.yaml` contains one stale pre-promotion sentence inside `accepted_residuals` saying v0.3.6 remains the only adopter-facing baseline until explicit promotion. Promotion has now occurred.

Do **not** silently edit the released 118-file v0.3.7 package merely to rewrite that sentence. v0.3.7 release discipline binds one version identity to one effective-content state. Treat the sentence as a release-metadata erratum; the top-level baseline identity, governed merge, and this project control plane establish v0.3.7 as Current. Correct the stale residual only under a future governed release identity.

## Issue and branch posture

Open issue count is not a release quality metric. `#89`–`#94` and `#104` remain durable reconstruction/research obligations while their scopes remain useful. `#150` is the active v0.3.7 field-evidence stream. The former v0.3.6 stream `#70` is closed as predecessor occurrence evidence.

Branches are lifecycle surfaces, not archives. `research/ena-reconstruction` remains the sole active research integration branch named by the canonical pointer. Release/candidate/validation/tmp/alignment/control-fix refs have durable lineage and are cleanup candidates after lifecycle closure. The currently available connector does not expose genuine delete-ref capability, so deletion must not be simulated by force-moving refs.

## Immediate permitted next action

The release/promotion lifecycle is closed. Resume reality-facing research through the active field and reconstruction surfaces:

```text
#150 field evidence + #89-#94/#104 unresolved research
-> select only bounded work that can change a decision
-> branch concrete HOWs where needed
-> preserve open failure variation
-> reconcile evidence back into main-visible project state
```

A new candidate/release is justified only by material decision-changing evidence; candidate.4 is not a ceremonial next step.

## Independent validation clean room

`guytogay/independent-validation-cleanroom` is reusable validation infrastructure, not an ENA-specific candidate repository.

```text
CLEAN_ROOM_REPOSITORY_IDENTITY = REUSABLE_VALIDATION_INFRASTRUCTURE
CLEAN_ROOM_CONTENT = CURRENT_STAGE_EPHEMERAL_REVIEW_SURFACE
```

It may be reused across ENA stages and unrelated projects. Occurrence truth belongs back in the source project; clean-room contents should be reset/replaced between validation occurrences.

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
EXPERIMENTS_MUST_PAY_EPISTEMIC_RENT
```

## Project knowledge surfaces

- Current adoption: `releases/current/`
- Project control: `main`
- Active research pointer: `research/ACTIVE-RESEARCH.yaml`
- Active research integration branch: `research/ena-reconstruction`
- Handoff framework/current pointer: `research/handoffs/`
- Research methodology: `research/methodology/`
- Long-horizon plan + fast state: `research/plans/`
- Branch governance/inventory: `research/BRANCH-GOVERNANCE.md`, `research/BRANCH-INVENTORY.yaml`
- Reconciliation/evidence: `collaboration/reconciliation/`, `evidence/`
- Active field evidence: GitHub Issue `#150`

## Authority boundary

`Contribution != Reconciliation != Release/Promotion Authority.`

GitHub write access, candidate authorship, validation work, or green CI does not by itself establish promotion authority.

> Preserve one legible Current, many recoverable experiments/candidates, and enough method that the next project manager can continue without reconstructing the project from chat.
