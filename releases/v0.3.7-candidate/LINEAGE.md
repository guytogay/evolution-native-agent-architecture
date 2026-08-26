# ENA v0.3.6 Lineage

Status: `CURRENT / FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE`.

## Parent baseline

- predecessor Current: `v0.3.5 / CURRENT / FIELD_VALIDATION`;
- predecessor Current tree: `9c928b4c99ae72e53c89978cf1d10b7ea068c182`;
- repository base commit: `f14855fdfd57b975195f0b1c261b754bd3058749`.

## Design / authoring lineage

- design seed: `f48b70f7cb82cd240a97d6d807874def37d67d70`;
- working candidate initialized: `5d4b5ea92c9d3bf8972f56e72c3487e03a598623`;
- full v0.3.5 baseline inherited into candidate without changing Current: `668a1be941045cb25c86008eaee620340a21b9a6`;
- ecology semantics, Runtime Kernel, v2 schema, bilingual fixtures, field template, and author self-attacks evolved through the candidate branch.

The detailed authoring history remains recoverable through PR #68 and Git; Current does not require ordinary adopters to replay every intermediate author checkpoint.

## candidate.0

Frozen source:

`3cb94d98882621acede189d0d47806efae44fb0f`

Frozen effective candidate tree:

`80f2da918811c26381d65eb5afa8e40f8410a32e`

Freeze-record commit:

`15e513a72d59e28f8d3050ef877746f85ab706ba`

PR:

`#68`, closed without merge.

Pre-freeze machine verification required three passes; the first two correctly preserved FAIL results before the third exact source passed. The frozen candidate then received a fresh independent semantic falsification.

Fresh independent verdict:

`NEEDS_REVISION`

Material release blockers:

- F-01 — v2 `integration_history` weakened predecessor representation strength;
- F-02 — array order could masquerade as chronological latest evidence/expression state.

The falsifier also identified successor repairs F-03 through F-09 and residual/research findings, while explicitly withdrawing three of its own initial attacks as false positives.

Independent report:

PR #68 comment `issuecomment-5389079667`.

## candidate.1

Successor branch:

`candidate/v0.3.6-candidate.1`

Frozen source:

`4af5d17a1cedcf2850b2b4dfe5446e132023369a`

Frozen effective candidate tree:

`52a0cc260ec33fc3e332f6ac0f98f5d1e98b565d`

Freeze-record commit:

`aa9a79b305d2ae8f8ff423df314af974e2e51d23`

PR:

`#69`, closed without merge after targeted revalidation/reconciliation.

candidate.1 repaired the representation/machine defects while intentionally preserving the independently supported Evolution Ecology semantic core.

### Exact-source machine evidence

On source `4af5d17a1cedcf2850b2b4dfe5446e132023369a`:

- ENA v0.3.6 Candidate Validate run `32677101732` — SUCCESS;
- Main Gate run `32677101720` — SUCCESS;
- CodeQL run `32677101753` — SUCCESS;
- v2 consistency selftest — `18/18`;
- inherited `ena_evolve.py` selftest — PASS, state/schema 1.2, 10 cases;
- inherited composed regression — `235/235`;
- unexpected verdicts — `0`;
- uncaught exceptions — `0`;
- Python compile — `7/7`;
- bytecode hygiene — PASS;
- Current isolation — PASS.

### Same-falsifier targeted revalidation

Role:

`SAME_FALSIFIER / TARGETED_REVALIDATION / NOT_FRESH / NOT_AUTHOR`

Report:

PR #69 comment `issuecomment-5389505830`.

Verdict:

`TARGETED_REVALIDATION_PASS_WITH_RESIDUALS`

Per-finding closure:

- F-01 CLOSED;
- F-02 CLOSED;
- F-03 CLOSED_WITH_RESIDUAL;
- F-04 CLOSED;
- F-05 CLOSED_WITH_RESIDUAL;
- F-06 CLOSED;
- F-07 CLOSED;
- F-08 CLOSED;
- F-09 CLOSED_BY_TRUTHFUL_BOUNDARY;
- F-10 CLOSED.

No material repair-induced regression was reported.

## Host-side final reconciliation

Durable record:

`collaboration/reconciliation/2026-08-24-v036-candidate1-final-reconciliation.md`

Commit:

`ac816471a0522d21494913a62a15bf0917d936ac`

Decision:

`CANDIDATE_SUCCESSION_STOP = YES unless new material evidence appears`

`RELEASE_PREPARATION_SUPPORTED`

No candidate.2 was justified by the remaining residuals.

## Release packaging lineage

Release branch:

`release/v0.3.6`

Packaging begins with a byte-for-byte transplant of frozen candidate.1 effective tree `52a0cc260ec33fc3e332f6ac0f98f5d1e98b565d` into `releases/current/`, then applies release-only identity/adoption/package transformations.

Release packaging is permitted to change identity labels, Current baseline metadata, projection bindings, adopter instructions, lineage/changelog, root status metadata, and release-validation/package machinery. It must not silently alter the validated material semantics closing candidate.1's findings.

The final release commit/tree/package digest and merge identity are recorded only after exact release PR checks and post-merge readback complete.

## Accepted residuals

Carry forward visibly:

1. F-03 — self-asserted `LOCAL` provenance is not external attestation;
2. F-05 — obligation references are represented but not authenticated merely by schema acceptance;
3. F-09 — inherited `ena_evolve.py` v1.2 false-BLOCKs the normative v0.3.6 latent propose/import path and remains explicitly non-normative for that path;
4. tied-latest timestamp rejection is conservative;
5. F-11 — fresh-session cue salience/application remains unproven field evidence;
6. F-12 — `experiment` versus broader `reality contact` terminology remains research wording.

Do not silently report these as solved.

## Constitution identity

All 38 inherited Constitution IDs remain unchanged.

`NEW_CONSTITUTION_IDS = 0`

## Canonical boundary

A local branch/fork may freely vary ENA but cannot self-promote by writing `CURRENT` into metadata.

Canonical admission requires governed lineage, validation/falsification evidence, reconciliation, immutable release identity, and explicit release promotion.

GitHub is the current project carrier for that lineage, not the metaphysical definition of ENA validity.

> **History is evidence, not a second runtime baseline.**
>
> **Variation first; selection by reality.**
