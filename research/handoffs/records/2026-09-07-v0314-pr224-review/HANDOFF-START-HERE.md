# ENA Deep Session Handoff — Start Here

Handoff ID: `2026-09-07-v0314-pr224-review`

Status: `DEEP_PROJECT_SESSION_SUCCESSION / CURRENT_STABLE / EXTERNAL_CONTRIBUTION_REVIEW_ACTIVE`

## Read order

1. `NOW.md`
2. `research/handoffs/CURRENT-HANDOFF.yaml`
3. this file
4. `HANDOFF-MANIFEST.yaml`
5. `PROJECT-STATE.md`
6. `RECENT-THREE-ROUNDS.md`
7. `LESSONS-AND-REMINDERS.md`
8. `REPO-ECOSYSTEM.md`
9. `FILE-CATALOG.md`
10. GitHub PR `#224` and its maintainer comments only when continuing the active contribution review

## Live state to reverify

At handoff creation, ENA Current is `v0.3.14 / CURRENT / FIELD_VALIDATION`. Current release bytes were published by PR #223 / merge `d21477663013c460c88719bebdcc3f7dfe9ba3d7` and have not changed since.

Main later advanced only through control-plane/live-state work:

- PR #225 merged as `becd83529e58d166f907c519d30da081180d260a`, adding `.github/workflows/current-immutability.yml`;
- PR #226 merged as `6092517d374c09980621664f8e004dac07a902a3`, recording F-208-10 and PR #224 disposition in live state.

Reverify mutable facts before writes; do not assume PR #224 has not moved.

## Active next action

Continue PR #224 as an external-Agent contribution candidate, **not** as an already-approved successor release.

Current maintainer disposition:

`ACCEPT_DIRECTION / REQUEST_NARROWING / SUCCESSOR_REQUIRED`

Do not merge PR #224 into v0.3.14 in place. Its original commit `b4b0369d5a4e20550a64d1abf5b13968588fddff` must remain visible as contribution provenance.

If the contributor revises it, review the new head for:

1. semantic equivalence/narrowing;
2. compactness of the only default hot payload;
3. whether trigger-style wording adds mandatory rituals or stronger claims;
4. whether the change has enough evidence to justify a successor release at all.

If no revised contribution exists, the next useful maintainer action is to decide whether a compact hybrid candidate is worth constructing. Do **not** manufacture v0.3.15 merely because the idea is attractive.

## Do not regress

- `same version -> same effective content` is now machine-guarded; changes under `releases/current/**` require a successor `ena_version`.
- Green CI is not evidence of complete gate coverage; #224 itself exposed that gap.
- Preserve negative/null/narrowing results.
- Do not reopen the closed evolutionary-memory mechanism campaign without a concrete decision-changing discriminator.
- Do not ask the user to repeat persisted project history.
