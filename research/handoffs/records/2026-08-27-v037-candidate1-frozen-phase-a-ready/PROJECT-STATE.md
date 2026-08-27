# Project state — ENA v0.3.7 candidate.1 frozen / fresh Phase A next

Date: 2026-08-27

## Authority posture

This is a project-manager handoff projection, not project authority.

When any value here disagrees with a canonical surface, use the authority hierarchy in `research/handoffs/HANDOFF-PROTOCOL.md` and reverify live GitHub state.

## Current adopter baseline

- version: `v0.3.6`
- adoption status: `CURRENT`
- maturity: `FIELD_VALIDATION`
- authority: `releases/current/CURRENT-BASELINE.yaml`
- mutation authorized by current research transition: **no**

The candidate.1 freeze does not alter Current.

## Frozen v0.3.7 candidate.1

- identity: `v0.3.7-candidate.1`
- candidate branch: `candidate/v0.3.7-candidate.1`
- branch head is frozen identity: **no**
- exact frozen source: `ae6903464133cb5bcf3cd8909ecae1215fe0b9ba`
- exact frozen candidate subtree: `c0458e0d7ea417b841cbf4c8bf6e64e4aff37319`
- subtree path: `releases/v0.3.7-candidate/`
- Current subtree at the same source: `7dcbb3934883ffa6cc5292a662588cafc1533cff`
- exact pre-freeze workflow run: `33055811978` — SUCCESS
- freeze record: `collaboration/reconciliation/2026-08-27-v037-candidate1-freeze.md`
- frozen: **yes, by external exact-tree record**
- Current: **no**
- released: **no**

The candidate package was not rewritten after validation merely to set an internal frozen flag. The external record binds the exact tested bytes.

Any material candidate-byte correction now requires a successor identity such as `v0.3.7-candidate.2`.

## Predecessor occurrence truth

Frozen candidate.0 remains immutable lineage:

- identity: `v0.3.7-candidate.0`
- frozen source: `d0e793593184740d9732902e948afd48ed96ae2f`
- frozen subtree: `cffbf76fe1448b020b637c78d1f7ae46e4c0115b`
- fresh blind Phase-A seal: `5ba3d241efa460fe170253860ad67045aa1d96a5`
- Phase-B verdict: `NEEDS_REVISION / CANDIDATE_1_REQUIRED`
- release disposition: `NOT_RELEASED / SUPERSEDED_BY_SUCCESSOR`

## Candidate.1 repair evidence

Known predecessor findings were repaired in two bounded rounds:

- round 1: `583ac8133350bdf70a6a87fc8f0b070943f0aca1`
- round 2: `bc8be8bc02a2b2515cfa1b7eee2c4bd3c2a37f90`

Final same-falsifier evidence before exact freeze:

- targeted successor run `33052764739` — SUCCESS
- focused open-branch run `33052764661` — SUCCESS
- reconciliation: `collaboration/reconciliation/2026-08-27-v037-candidate1-successor-repair-reconciliation.md`

These checks establish known repair behavior but are not a second fresh Phase A.

## Exact pre-freeze evidence

Workflow:

`ENA v0.3.7 Candidate.1 Exact Pre-Freeze Gate`

Run:

`33055811978`

Result:

`SUCCESS`

The gate bound one exact source and candidate subtree, preserved Current isolation, reran inherited candidate checks, replayed still-applicable author/anti-ablation failure shapes, ran successor A–D regressions and focused open-branch regressions, checked language projection/runtime self-containment, compiled candidate Python, and verified tree cleanliness.

The workflow explicitly did **not** claim independent semantic support, external truth, possibility-space completeness, or freeze authority.

## Post-freeze independence decision

Record:

`collaboration/reconciliation/2026-08-27-v037-candidate1-post-freeze-independence-decision.md`

Decision:

`FRESH_BLIND_SUCCESSOR_REVIEW_WARRANTED / ONE_REVIEW_CYCLE / NOT_RELEASE_AUTHORITY`

Reason: candidate.1 changed executable/validator semantics on chronology, migration provenance, represented history, and integration consistency; predecessor fresh review had already demonstrated shared author-side blind spots. One blind successor review therefore pays epistemic rent. This is not a universal rule requiring endless fresh review after every successor.

## Fresh candidate.1 Phase-A intake

- issue: `#128` — `Fresh blind Phase A — v0.3.7 candidate.1`
- validation branch: `validation/v037-c1-blind-phase-a-primary`
- branch base: exact frozen source `ae6903464133cb5bcf3cd8909ecae1215fe0b9ba`
- intake head: `bac074097579ad930b2e90c46c00773f6f20c86d`
- blind entry: `collaboration/reconciliation/2026-08-27-v037-candidate1-blind-phase-a-entry.md`
- required report: `collaboration/reconciliation/2026-08-27-v037-candidate1-independent-phase-a-primary.md`
- report state at handoff creation: `NOT_YET_SEALED`

The intake commit adds only the blind entry outside the candidate subtree. The validation branch still contains the exact frozen candidate subtree and unchanged Current subtree.

Fresh-validator stop condition:

`REPORT_COMMITTED -> PHASE_A_SEALED -> STOP`

The project manager then independently verifies the seal before any Phase-B author context is opened.

## Visible residuals and open space

The source/receiver `candidate_id` collision remains an explicitly visible namespace residual.

Current rule:

`NO_CURRENT_CONTRACT -> DO_NOT_INVENT_UNIVERSAL_RULE`

It is not automatically a release blocker because no current ENA contract establishes cross-environment global candidate-ID uniqueness.

Attack cardinality remains `OPEN`. Successful exact machine validation is not a proof that no unknown failure shapes remain.

## Branch roles

Expected live branches relevant to this transition:

- `main` — adopter-facing project control plane / default integration authority;
- `research/ena-reconstruction` — long-lived active research integration surface;
- `candidate/v0.3.7-candidate.0` — frozen predecessor lineage;
- `candidate/v0.3.7-candidate.1` — frozen successor occurrence lineage;
- `validation/v037-c0-blind-phase-a-primary` — sealed predecessor fresh Phase-A occurrence truth;
- `validation/v037-c1-blind-phase-a-primary` — candidate.1 fresh Phase-A intake, not yet sealed at this record snapshot.

Always live-reverify these refs. Branch names and latest heads do not replace exact frozen identity.

## Immediate next action

`CANDIDATE1_FRESH_BLIND_PHASE_A`

A genuinely fresh reviewer must inspect the exact frozen candidate.1 bytes using only the minimal blind entry before sealing its report.

After seal:

1. project manager verifies report commit, exact target source/subtree, and no candidate mutation;
2. only then open author-side evidence for Phase B;
3. material candidate-byte defect -> candidate.2, never in-place mutation of candidate.1;
4. non-contract residual/oracle/boundary findings are reconciled without manufacturing rules merely for closure;
5. release/promotion is considered only after evidence reconciliation.

## Forbidden now

- modify `releases/current/`;
- claim `v0.3.7` is Current or released;
- mutate frozen candidate.0 or candidate.1 in place;
- call targeted/same-falsifier evidence fresh independent validation;
- prime the candidate.1 fresh reviewer with this handoff, repair narratives, predecessor findings, author attack maps, or expected verdicts before Phase-A seal;
- merge historical PR #115 as release/promotion authority;
- close attack cardinality because the exact gate passed;
- invent a universal candidate-ID uniqueness rule solely to eliminate a residual.
