# ENA v0.3.3-candidate — Implementation Candidate

Status: `IMPLEMENTATION_CANDIDATE / NOT_MAINLINE / NOT_PROMOTED`

This directory is a self-contained flat implementation candidate for the next
release-candidate validation cycle. It is NOT a release and NOT the adoption
baseline. It does not require composing v0.3.2 at runtime.

- Base: ENA v0.3.2 (`releases/current/`, frozen, unmodified).
- Accepted mechanism source: frozen V2.4.1 research successor
  `daacab1f042c38f3856ef4d0366febd1b5e47600` (reconciliation
  `ACCEPT_FOR_IMPLEMENTATION`, PR #34).
- Composed validation surface: `tools/validate_contracts.py :: validate_case()`
  (CLI mode `case`).
- Regression corpus: `tools/contract-fixtures.v2.json` (164 cases, provenance
  preserved); deterministic runner `tools/regression_suite.py`.
- Contract semantics: `05-CORE-OPERATIONAL-CONTRACTS.md` section 5.13.
- Input shape contract: `schemas/composed-case.v1.schema.json`.

Do **not** treat this candidate as accepted ENA truth. The next actor is a
fresh independent validator outside the V2.x lineage and the implementation
authoring; promotion and release decisions remain Host authority.

## Start

For low-consequence bounded work, the v0.3.2 LITE reading set applies unchanged
(`00-READ-ME-FIRST.md`, `01-CONSTITUTION.md`, `LITE-ADOPTION-INSTRUCTION.md`).
The composed validation surface is opt-in: it is exercised by
`tools/regression_suite.py` and the `case` CLI mode.
