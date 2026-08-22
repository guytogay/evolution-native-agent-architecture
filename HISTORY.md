# ENA Release History

This is a compact retrieval index, **not** an adoption menu.

For adoption, always use `releases/current/` and read `releases/current/CURRENT-BASELINE.yaml`.

Historical releases and candidates remain recoverable through Git commits/trees, validation/reconciliation evidence, and repository history. They are intentionally not duplicated as parallel release directories in the current repository surface.

## Formal released baselines

### v0.3.4

- release merge commit: `26f171dbc1e6c09c3a504dd67480f04fcd08e4c7`
- immutable release/Current tree at release: `b237802c08d608bb9be650fe213b7846d3be4bf6`
- package SHA-256: `6821480334ac961f1becd8d0a824bd4a9bce22f6fad01da4870190321e657e33`
- release status: `CURRENT / FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE / NOT_MAINLINE`
- release PR: `#48`

### v0.3.3

- release merge commit: `5b72010937b96c96d97c526f250f3e5a2c91bfa3`
- Current tree at release: `8d85fbee0684e9993f8a2bb3741dd5f72534be57`
- package SHA-256: `e4983adee1b9ec6546b6712417c2ecf87ddecc8edf2016b9564ce36972bbf5d1`
- release status at the time: `CURRENT / FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE / NOT_MAINLINE`
- release PR: `#42`

## Earlier history

ENA predates this repository. Earlier promoted baselines, including the historical `v0.2.11 MAINLINE`, are preserved through repository-adoption records, research/evidence, decisions, recovery artifacts, and Git-visible migration history where available.

See `REPOSITORY-ADOPTION.md` when that historical boundary is relevant.

## Candidate and validation lineage

Candidate identities are development/evidence artifacts, not released adoption choices. Their exact commits/trees and validation outcomes are recorded under:

- `collaboration/inbox/`
- `collaboration/reconciliation/`
- Git history
- closed Pull Requests and Issues

Do not enumerate or load candidate lineage during ordinary adoption unless a real regression, audit, provenance, or research question requires it.

> **Current is the hot path; history is the cold path.**
>
> **Preserve history durably; retrieve history selectively.**
