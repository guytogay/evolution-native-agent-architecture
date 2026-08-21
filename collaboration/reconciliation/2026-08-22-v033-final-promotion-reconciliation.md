# ENA v0.3.3 — Final Current Promotion Reconciliation

Date: 2026-08-22

```yaml
status: ACCEPTED
outcome: PROMOTED_TO_CURRENT_ADOPTION_BASELINE
release_workflow: COMPLETE
current_adoption_baseline: ENA v0.3.3
maturity: FIELD_VALIDATION
complete_adoption_baseline: true
mainline: false
mainline_claim_allowed: false
```

## Scope

This reconciliation closes the ENA v0.3.3 implementation, falsification, successor correction, targeted revalidation, Current authoring, merge, and published-artifact read-back chain.

It does **not** promote v0.3.3 to ENA Mainline. Historical Mainline status remains separate from the Current adoption baseline.

## Canonical lineage

- Accepted research mechanism source: V2.4.1 `daacab1f042c38f3856ef4d0366febd1b5e47600`; final research reconciliation PR #34.
- Original implementation candidate: `f7dc6202dacd30e1f19d023146ecaeb4f020c922`.
- Fresh independent implementation validation: PR #38, `INDEPENDENT_IMPLEMENTATION_VALIDATION_NEEDS_REVISION`.
- Corrected successor candidate `v0.3.3-candidate.1`: `034b7895997dd0599a0bfea10de7acfac575f232`; freeze `fbefa9a77d9618ba98153291295588222c2cc78d`.
- Prior-falsifier targeted revalidation: PR #41, `REVALIDATION_BY_PRIOR_IMPLEMENTATION_FALSIFIER_SUPPORTED`; evidence merge `8ac7e0ef13c3171d8e4c9bbcd8d492e2fe24f342`.
- Current release PR: #42.
- Final Current merge commit: `5b72010937b96c96d97c526f250f3e5a2c91bfa3`.

## Current identity

At final `main`, `releases/current/CURRENT-BASELINE.yaml` declares:

- `ena_version: v0.3.3`
- `status: FIELD_VALIDATION`
- `complete_adoption_baseline: true`
- `requires_older_release_composition: false`
- `mainline_claim_allowed: false`
- `package_scope: ALL_FILES_UNDER_RELEASES_CURRENT`

The Current wording is release-stable and does not claim that promotion authoring is still in progress.

## Final published-artifact evidence

Final post-merge workflow run:

- workflow: `Validate and package ENA Current`
- run ID: `32530963641`
- event: `push`
- branch: `main`
- head SHA: `5b72010937b96c96d97c526f250f3e5a2c91bfa3`
- conclusion: `success`

Published GitHub Actions artifact:

- artifact ID: `9463829189`
- artifact name: `ENA-v0.3.3-release-package`
- outer artifact SHA-256: `b64e006b1ea4a6767e3398d9e501e38cc84128224db7c2179d808cf644663977`

Downloaded artifact contents:

- `ENA-v0.3.3-CURRENT.zip`
- `ENA-v0.3.3-CURRENT.zip.sha256`
- `ENA-v0.3.3-RELEASE-EVIDENCE.json`

Release evidence reports canonical Current source commit:

`6da3991d0f1fd563dcf984937dcd5a40c6c64757`

This is the final release-branch commit that actually changed `releases/current/`. Git comparison from that source commit to the final merge commit `5b720109...` shows one merge commit ahead and **zero file differences**, so final `main` Current bytes are identical to the packaged canonical source bytes.

## Package read-back

Independent Host read-back of the downloaded final-main artifact verified:

- Current ZIP SHA-256: `e4983adee1b9ec6546b6712417c2ecf87ddecc8edf2016b9564ce36972bbf5d1`
- `.sha256` file matches the actual Current ZIP digest
- release-evidence JSON matches the actual Current ZIP digest
- file count: `29`
- exact ZIP file-set parity: PASS
- per-file SHA-256 read-back parity: `29/29` PASS
- mismatched files: `0`
- deterministic ZIP metadata: recorded true by the release workflow
- candidate/freeze/authoring-only artifacts were not introduced into Current

Therefore the final published distribution artifact is traceably derived from the same effective Current bytes now present on `main`.

## Validation closure

The v0.3.3 release carries the validated successor semantics after fresh independent falsification and correction:

- D1: claim-bound material obligations gate the claims they bind, including non-completion claims, without unrelated-obligation poisoning.
- D2: id-less top-level support remains a legitimate direct representation but cannot silently satisfy registry references.
- D3: root-provenance independence uses composed root-registry semantics without premature legacy `source_origins` rejection.

Inherited and closure regression evidence remains:

- migrated v0.3.2 selftests: 10/10
- inherited implementation corpus: 164/164, zero flips
- D1/D2/D3 closure corpus: 61/61
- total exercised semantic cases: 235
- unexpected verdicts: 0
- uncaught exceptions: 0

## Final reconciliation decision

The release-integrity obligations for v0.3.3 are satisfied:

1. validated semantic successor exists and is immutable;
2. the original falsifier confirmed D1/D2/D3 closure;
3. the release was flattened into one self-contained Current world;
4. Current identity is explicit and non-Mainline;
5. the final Current transition was merged through PR #42;
6. the final `main` push workflow succeeded;
7. the published artifact was downloaded and read back;
8. package digest, exact file set, and all per-file hashes matched;
9. canonical source bytes and final-main Current bytes are identical.

Final state:

> **ENA v0.3.3 = CURRENT / FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE / NOT_MAINLINE**
>
> **RELEASE_WORKFLOW_COMPLETE**

No further v0.3.3 implementation, validation, or release correction is required by this reconciliation. Future work should return to field validation and new evidence rather than extend this closed release loop without a new decision-worthy observation.
