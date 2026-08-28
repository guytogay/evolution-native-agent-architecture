# ENA Release History

This is a compact retrieval index, **not** an adoption menu.

For adoption, always use `releases/current/` and read `releases/current/CURRENT-BASELINE.yaml`.

Historical releases and candidates remain recoverable through Git commits/trees, validation/reconciliation evidence, issues, PRs, and repository history. They are intentionally not duplicated as parallel release directories in the current repository surface.

## Formal released baselines

### v0.3.7

- release date: 2026-08-28
- exact reviewed release head: `3ef3605228ed427b2d25d7d586e4ffc378b7369e`
- release merge commit: `50a4bb06b98dc0dd719230f71ed1d47e42e1fad9`
- immutable release/Current tree at release: `f33e73ed997c1b66a4572685ab5474182e136e97`
- deterministic Current package SHA-256: `40d4dde277d54ce8252e0402e32f900fa7ab4fb0aeaa638b898073d0f02f848c`
- package file count: `118`
- Exact Release Gate: run `33162550145` — PASS
- post-merge Main Gate: run `33163171275` — PASS
- post-merge Current validate/package: run `33163171328` — PASS
- post-merge CodeQL: run `33163171289` — PASS
- frozen release source: candidate.3 commit/tree `b7e88d7adb70396bd671ca97066daf2c120e0adc` / `e3a9a20d16cecd78df7f32f19fca56e21159e810`
- release status: `CURRENT / FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE`
- release PR: `#144`
- post-release heterogeneous field validation: `#150`
- predecessor field-validation stream: `#70` closed as preserved v0.3.6 occurrence evidence
- candidate succession: STOP; candidate.4 not justified by release evidence

Release-metadata erratum: `releases/current/CURRENT-BASELINE.yaml` retains one pre-promotion sentence under `accepted_residuals` saying v0.3.6 remains the sole adopter-facing baseline until explicit promotion. Promotion has occurred. The immutable v0.3.7 package is not silently rewritten under the same version identity; this erratum is recorded outside Current and should be corrected under a future governed release identity.

### v0.3.6

- release merge commit: `74b790741653286e0f01a1483723cdeb065ec3df`
- immutable release/Current tree at release: `7dcbb3934883ffa6cc5292a662588cafc1533cff`
- release status at the time: `CURRENT / FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE`
- release PR: `#71`
- post-release heterogeneous field validation: `#70`
- succeeded by v0.3.7 on 2026-08-28; #70 remains predecessor occurrence evidence

### v0.3.5

- release merge commit: `a18ec89d0be3a9fbd872306aa2914a05adae5e62`
- immutable release/Current tree at release: `9c928b4c99ae72e53c89978cf1d10b7ea068c182`
- canonical Current source commit used by deterministic packaging: `32c57da7caf8f8edfdd2e85f252c14fddebcca3c`
- deterministic package SHA-256: `b4a0c1188729b10df9b4e68f67118e6679ffcc1c9007828e474522f6c5b4732d`
- package file count: `49`
- PR-head published workflow artifact: `9488870775` (`ENA-v0.3.5-release-package`)
- release status at the time: `CURRENT / FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE`
- active `MAINLINE / NOT_MAINLINE` adopter-facing axis retired beginning with this release; historical uses remain unchanged
- release PR: `#64`
- post-release heterogeneous field validation: `#61`

### v0.3.4

- release merge commit: `26f171dbc1e6c09c3a504dd67480f04fcd08e4c7`
- immutable release/Current tree at release: `b237802c08d608bb9be650fe213b7846d3be4bf6`
- package SHA-256: `6821480334ac961f1becd8d0a824bd4a9bce22f6fad01da4870190321e657e33`
- release status at the time: `CURRENT / FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE / NOT_MAINLINE`
- release PR: `#48`

### v0.3.3

- release merge commit: `5b72010937b96c96d97c526f250f3e5a2c91bfa3`
- Current tree at release: `8d85fbee0684e9993f8a2bb3741dd5f72534be57`
- package SHA-256: `e4983adee1b9ec6546b6712417c2ecf87ddecc8edf2016b9564ce36972bbf5d1`
- release status at the time: `CURRENT / FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE / NOT_MAINLINE`
- release PR: `#42`

## Earlier history

ENA predates this repository. Earlier promoted baselines, including historical `v0.2.11 MAINLINE`, remain recoverable through repository-adoption records, research/evidence, decisions, recovery artifacts, and Git-visible migration history where available.

See `REPOSITORY-ADOPTION.md` when that historical boundary is relevant.

## Candidate and validation lineage

Candidate identities are development/evidence artifacts, not released adoption choices. Exact commits/trees and validation outcomes are retained in reconciliation/handoff records, issues, PRs, sealed evidence, and Git history.

Do not enumerate or load candidate lineage during ordinary adoption unless a real regression, audit, provenance, or research question requires it.

> **Current is the hot path; history is the cold path.**
>
> **Preserve history durably; retrieve history selectively.**
