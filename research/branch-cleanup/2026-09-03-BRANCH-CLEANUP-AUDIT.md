# ENA Branch Cleanup Audit — 2026-09-03

Status: `PROJECT_HYGIENE / POSTMERGE_VERIFIED / NOT_CURRENT / NO_SEMANTIC_CHANGE`

Integration facts:

- cleanup/handoff PR: `#178`
- squash merge: `ec9255f147c866de3eeb44e7769285800a603afb`
- postmerge readback: `PASS`
- three unique `research/ena-reconstruction` artifacts: present on `main` with exact pre-migration blob identity

## Decision

The repository no longer needs a long-lived research integration branch.

Normal work has converged on the simpler path already introduced by PR #154:

```text
main / NOW.md
-> relevant issue or artifact
-> short-lived branch only when a PR/isolation surface is useful
-> merge to main
-> delete branch after lineage is durable
```

Branch names are lifecycle handles, not archives.

After PR #178 and its readback, **`main` is the only intended long-lived continuation branch**. Future research branches should normally be short-lived PR branches created from current `main`.

## Important exception discovered before cleanup — resolved

`research/ena-reconstruction` was not safe to delete at audit start.

Compared with `main @ e1e50ed1def69d4a088d670ca26dc54c3b747904`, it was 3 commits ahead / 23 behind and still carried three unique Agent Skills / runtime-routing research files:

1. `research/external-how/harvests/2026-08-28-AGENT-SKILLS-PROGRESSIVE-DISCLOSURE-AND-TRIGGERING.md`
2. `research/field-validation/host-adapters/agent-skills/ena-runtime-router/SKILL.md`
3. `research/field-validation/host-adapters/agent-skills/ena-runtime-router/TRIGGER-CASES.yaml`

PR #178 transplanted those files into a fresh main-based change without merging the stale branch wholesale.

Postmerge readback verified that all three files are present on `main` with the same blob identities observed on the old branch.

Therefore `research/ena-reconstruction` is now **delete-safe**.

This is the main branch-cleanup lesson:

```text
STALE_BRANCH != SAFE_TO_DELETE
UNIQUE_CONTENT_CHECK -> PRESERVE -> VERIFY -> THEN_RETIRE
```

## Keep

### Permanent

- `main`
  - project control plane;
  - sole long-lived continuation surface after this cleanup;
  - ENA Current remains only `releases/current/`, not all of `main`.

### Temporary only while active work is unmerged

A short-lived main-based branch may exist while a bounded PR/isolation task is active.

The current postmerge-readback branch is temporary and becomes delete-safe after its small completion PR merges.

## Former long-lived research branch — delete-safe

- `research/ena-reconstruction`
  - do **not** merge the diverged branch itself;
  - its three unique research files were preserved by PR #178;
  - exact blob identity was verified after merge;
  - delete the branch ref when convenient.

## Delete-safe refs

The following refs have completed their lifecycle and their decision-relevant lineage is already preserved in main history, merged/closed PRs, exact commits/trees, release/freeze records, validation records, or field-validation archives.

### v0.3.7 release/candidate/integration lifecycle

- `candidate/v0.3.7-candidate.0`
- `candidate/v0.3.7-candidate.1`
- `candidate/v0.3.7-candidate.2`
- `candidate/v0.3.7-candidate.3`
- `release/v0.3.7`
- `integration/v037-prepromotion-alignment`
- `integration/v037-postpromotion-alignment`
- `research/selection-qualification-v037-template-oracle-fix`

The old candidate.0 draft review PR #115 was explicitly closed during this audit because v0.3.7 has already completed candidate succession and release.

Frozen/released identity remains exact Git object lineage, not branch existence.

### historical validation refs

- `validation/v037-c0-blind-phase-a-primary`
- `validation/v037-c1-blind-phase-a-primary`
- `validation/v037-c1-blind-semantic-primary`
- `validation/v037-c2-blind-semantic-primary`
- `validation/v037-c2-blind-semantic-primary-r2`

These are occurrence carriers only. Their durable results are already in reconciliation/handoff/history.

### completed recent research PR heads

- `research/adaptive-inheritance-005`
- `research/agent-developmental-dynamics-007`
- `research/agent-developmental-succession-006`
- `research/archive-cleanroom-round-1`
- `research/boundary-memory-pilot-preregister`
- `research/boundary-memory-pilot-raw`
- `research/boundary-memory-pilot-results-final`
- `research/evolutionary-memory`
- `research/memory-convergence-validation-009`
- `research/memory-ecology-divergence-002`
- `research/memory-ecology-sleep-dreaming`
- `research/metamemory-regulation-003`
- `research/metamemory-sovereignty-004`
- `research/negative-boundaries-literature-008`
- `research/semantic-reachability-010`
- `research/semantic-reachability-baseline-011`
- `research/semantic-reachability-round2-preregister`
- `research/semantic-reachability-round2-results`
- `research/zhipu-propagation-occurrence`
- `simplify/reality-first-selection`
- `status/refresh-now-after-154`

Their meaningful content is already on main through merged PRs #154–#177 and earlier research PRs.

### stale/duplicate/intermediate research refs

- `research/negative-boundaries-viable-space-008`
  - contains the merged negative-boundary lineage plus a stale closed-unmerged continuation from PR #166;
  - the intended literature mapping was separately merged through PR #167;
  - do not merge this stale branch wholesale.

- `research/validation-coverage-map`
- `research/validation-coverage-map-v2`
  - intermediate working refs created while the coverage map and I/J/K/L result were being assembled;
  - authoritative coverage map and pilot result are already on main through PR #175 and #176;
  - do not merge either intermediate branch.

### completed handoff refs

- `handoff/2026-09-03-session-succession`
  - merged through PR #178;
  - delete-safe after successful postmerge readback.

- `handoff/2026-09-03-postmerge-readback`
  - temporary completion/readback branch;
  - delete after its small completion PR merges and main readback confirms the final state.

### operator noise

- `tmp/noop-check`
- `tmp/noop-check-2`

Delete without preservation beyond existing Git history.

## No additional branch should be merged wholesale

After migrating the three unique files from `research/ena-reconstruction`, this audit found no reason to merge another historical branch into current main.

The safe operation is:

```text
unique artifact needed
-> transplant/reconcile into fresh main-based PR

historical branch fully represented or superseded
-> delete branch ref
```

not:

```text
old diverged branch
-> merge everything back into main
```

The latter would reintroduce stale control-plane state and already-superseded versions of files.

## Why the branch count became large

The branch count is primarily residue from a period when ENA treated many research, release, validation, alignment, and evidence steps as separate durable branch surfaces.

The later project simplification demonstrated a cheaper pattern:

- one live status surface (`NOW.md`);
- main as durable truth;
- PRs/commits as lineage;
- Issues for open work;
- short-lived branches as temporary transport/isolation only.

The branch namespace should therefore be pruned rather than treated as an archive.

## Manual cleanup limitation

The GitHub connector available to this session does not expose a genuine delete-ref operation.

Do **not** simulate deletion by force-moving refs.

The user may delete every branch listed under **Delete-safe refs** through GitHub's branch UI/CLI. `research/ena-reconstruction` is now included because its unique material has been preserved and verified.

Expected stable topology afterward:

```text
main
```

plus only whatever short-lived branch is active for the next PR.

## Future rule

A research idea does not earn a permanent branch.

Use a branch when isolation/review makes the current change safer or clearer. Delete it after merge/abandonment once unique material is preserved.

```text
BRANCH = TEMPORARY WORK SURFACE
GIT HISTORY + MAIN ARTIFACTS = DURABLE LINEAGE
```
