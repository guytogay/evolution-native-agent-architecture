# LINEAGE

Current adoption target in this release branch: `v0.3.3`.

Immediate predecessor: `v0.3.2` (historical field-validation baseline; its semantic core remains byte-identical in v0.3.3 and its selftests are intentionally preserved).

Historical promoted Mainline: `v0.2.11 MAINLINE`.

v0.3.3 is flattened and self-contained. It inherits still-effective semantics through reconciliation into its own files; adopters must not load or compose the predecessor to determine v0.3.3 behavior.

## v0.3.3 release lineage (truthful validation path)

The v0.3.3 Current baseline was authored from the validated implementation
successor lineage:

1. **Original v0.3.3 implementation candidate** — semantic candidate
   `f7dc6202dacd30e1f19d023146ecaeb4f020c922` (freeze `6a44041…`).
2. **Fresh independent implementation validation** — PR #38, verdict
   `INDEPENDENT_IMPLEMENTATION_VALIDATION_NEEDS_REVISION` (three defects D1/D2/D3,
   evidence merged `c1d29f6…`). The original candidate did NOT pass fresh
   independent validation; that negative evidence remains visible through
   `collaboration/inbox/` (probe harness/manifest/results) and Git history.
3. **Corrected successor** — v0.3.3-candidate.1, semantic candidate
   `034b7895997dd0599a0bfea10de7acfac575f232` (freeze `fbefa9a…`), closing
   D1/D2/D3 (PR #39, merged `15dc89d…`).
4. **Prior-falsifier targeted revalidation** — PR #41, verdict
   `REVALIDATION_BY_PRIOR_IMPLEMENTATION_FALSIFIER_SUPPORTED` (evidence merged
   `8ac7e0e…`).
5. **v0.3.3 release** — this Current baseline, authored from the validated
   successor under Host promotion-authoring authorization
   (`ACCEPT_FOR_PROMOTION_AUTHORING`).

The v0.3.3 composed claim-pack validation surface (05 §5.13, including the
D1/D2/D3 corrections of §5.13.9) is carried into Current; the regression corpus
is self-contained (`tools/contract-fixtures.v1/v2/v2.1.json` +
`tools/regression_suite.py`).

Historical ENA releases, experiments, research branches, candidates, validation
PRs, and superseded wording remain recoverable through Git history and durable
recovery archives. They are not runtime dependencies and are intentionally not
duplicated in Current.

> Preserve history durably; retrieve history selectively.
>
> A new version preserves lineage without making history a runtime layer.
