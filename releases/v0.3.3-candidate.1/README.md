# ENA v0.3.3-candidate.1 — Implementation Successor Candidate

Status: `IMPLEMENTATION_CANDIDATE / NOT_MAINLINE / NOT_PROMOTED`

This directory is a self-contained flat successor implementation candidate for
the next release-candidate validation cycle. It is NOT a release and NOT the
adoption baseline. It does not require composing v0.3.2 at runtime.

- Base: frozen v0.3.3-candidate `f7dc6202dacd30e1f19d023146ecaeb4f020c922`
  (freeze `6a4404119ac7d9ee0c927cd3a96d1adf26e32ba3`), which bases on ENA v0.3.2
  (`releases/current/`, frozen, unmodified).
- Closes the fresh independent implementation-validation findings (PR #38,
  `INDEPENDENT_IMPLEMENTATION_VALIDATION_NEEDS_REVISION`): **D1** (bound
  obligations gate all claims), **D2** (id-less top-level support is a
  legitimate direct representation), **D3** (root-provenance independence is
  authoritative over the legacy `source_origins` check).
- Composed validation surface: `tools/validate_contracts.py :: validate_case()`
  (CLI mode `case`).
- Regression: inherited 164-case corpus (`contract-fixtures.v2.json`, zero
  flips) + closure corpus (`contract-fixtures.v2.1.json`: 43 PR #38 probes +
  18 D1/D2/D3 closure controls); deterministic runner `regression_suite.py`.
- Candidate gate: `.github/workflows/candidate-gate-v033c1.yml` (Python
  3.8/3.12/3.13).
- Contract semantics: `05-CORE-OPERATIONAL-CONTRACTS.md` §5.13.9.

The previous `releases/v0.3.3-candidate/` package remains immutable historical
evidence. Do **not** treat this candidate as accepted ENA truth. The next actor
is the SAME fresh WorkBuddy session that produced PR #38, in a closed-scope
`REVALIDATION_BY_PRIOR_IMPLEMENTATION_FALSIFIER` round; promotion and release
decisions remain Host authority.

## Start

For low-consequence bounded work, the v0.3.2 LITE reading set applies unchanged
(`00-READ-ME-FIRST.md`, `01-CONSTITUTION.md`, `LITE-ADOPTION-INSTRUCTION.md`).
The composed validation surface is opt-in: exercised by `regression_suite.py`
and the `case` CLI mode.
