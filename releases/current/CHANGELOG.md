# CHANGELOG — v0.3.3

v0.3.3 is the successor Current adoption baseline. It is a flattened,
self-contained adoption world that does not require composition with v0.3.2,
any candidate package, or research artifacts at runtime. The v0.3.2 semantic
core is preserved byte-identical; the v0.3.2 selftests are intentionally
carried forward unchanged.

## Release lineage (truthful)

- Original v0.3.3 implementation candidate (`f7dc620…`) → **fresh independent
  implementation validation PR #38: `INDEPENDENT_IMPLEMENTATION_VALIDATION_NEEDS_REVISION`**
  (the original candidate did NOT pass; defects D1/D2/D3).
- Corrected successor v0.3.3-candidate.1 (`034b789…`, PR #39) closing D1/D2/D3.
- **Prior-falsifier targeted revalidation PR #41:
  `REVALIDATION_BY_PRIOR_IMPLEMENTATION_FALSIFIER_SUPPORTED`.**
- v0.3.3 Current release authored under Host promotion-authoring authorization
  (`ACCEPT_FOR_PROMOTION_AUTHORING`); NOT Mainline; promotion closure pending
  post-merge release evidence.

## Composed claim-pack validation

- Added `validate_case()` to `tools/validate_contracts.py` (CLI mode `case`):
  one composed validation surface over the unchanged shipped semantic core
  (validate_support / validate_obligation / validate_recovery).
- One canonical typed resolution layer; tri-state registries (absent /
  present-but-missing / malformed) with no raw-reference fallback; resolved
  support binds back to the target claim; the complete 8-dimension
  applicability envelope is preserved (material missing observations are
  mismatches); mandatory consequential evidence references resolve where the
  contract requires them; ambiguous duplicate identities fail closed; top-level
  and registry support representations compose; obligation blocking is
  claim-aware; STATE_AND_HISTORY recovery establishes both state and history
  evidence; authority source semantics are positively typed or registry-
  verified; PARTIAL support remains narrowed; registry identity rule R12
  (dict key authoritative; inner id must equal key else REGISTRY_MALFORMED);
  obligation status outside the shipped vocabulary is rejected without
  expanding it; malformed registry inputs produce machine verdicts, never
  uncaught exceptions; `eval_time` is explicitly required and caller-controlled.
- **D1** — bound obligations gate all claims (including non-completion claims):
  an obligation whose `required_before_claim_refs` names the claim blocks a
  material open state; unrelated obligations never poison; referenced-and-bound
  is evaluated once.
- **D2** — id-less top-level support is a legitimate DIRECT representation but
  cannot silently satisfy a registry reference; R12/list-ID/malformed rules
  unchanged.
- **D3** — root_provenance-backed independence uses the composed root-registry
  semantics (five states) without premature legacy `source_origins` rejection;
  the shipped core remains byte-identical.

## Regression (self-contained in Current)

- `tools/contract-fixtures.v1.json` — v0.3.2-migrated semantic selftests
  (10/10, unchanged);
- `tools/contract-fixtures.v2.json` — inherited 164-case implementation corpus
  (164/164, zero flips);
- `tools/contract-fixtures.v2.1.json` — 61-case closure corpus (43 PR #38 fresh
  probes + 18 D1/D2/D3 closure controls);
- `tools/regression_suite.py` — deterministic runner (zero unexpected, zero
  uncaught exceptions, deterministic results).

## Validation and packaging

- `.github/workflows/current-validate.yml` validates the ACTUAL final Current
  surface and builds a deterministic `ENA-v0.3.3-CURRENT.zip` from canonical
  committed bytes with exact file-set and per-file hash parity, internal ZIP
  read-back, package digest, and release-evidence JSON. Published-artifact
  read-back is a post-merge obligation.

## Release status

`FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE / NOT_MAINLINE`
(`mainline_claim_allowed: false`).

---

# CHANGELOG — v0.3.2

v0.3.2 is a flattened convergence/operationalization release. It preserves the useful constitutional spine of v0.3.1-BETA.1 while absorbing field/release findings and research that earned operational value. It does not require the older release at runtime.

## Release and adoption

- Simplified version identity to `v0.3.2`; maturity is separate metadata: `FIELD_VALIDATION / NOT_MAINLINE`.
- Made one version identity bind to one immutable effective content state.
- Added exact source/package parity and mirror read-back release discipline after the v0.3.1-BETA.1 distribution-identity counterexample.
- Added a batched release rhythm: accumulate meaningful issues/evidence, then publish the next flattened version rather than micro-versioning every small observation.
- Added explicit minimal branch discipline: research through Issues/artifacts; at most one short-lived active release branch when needed.

## Lower-cost adoption

- Turned `LITE` into a concrete low-overhead adoption path with a three-file default read set and task-triggered retrieval.
- Removed the requirement to enumerate the full role/capability/schema surface for low-consequence work when those objects do not change the decision.
- Kept LITE on the same Constitution; low ceremony does not mean reduced invariants.

## Operational-contract convergence

- Strengthened Claim ↔ Evidence with provenance independence, circular/derivative-support caution, causal-attribution limits, evidence-of-absence distinction, and positive closure where silence can mean interruption.
- Extended Capability/Model/Route Binding into explicit Authority/Subject/Mandate lifecycle semantics without creating a parallel authority subsystem.
- Added effect-level retry/parallel/failover/cancel semantics: idempotency, replay safety, commit ambiguity, reconciliation, duplicate elimination, reversibility/compensation, and externality.
- Clarified `cancel != rollback`, `state convergence != history completeness`, and `same identity != same execution incarnation` where material.
- Added composition-level control interaction risk, adaptive governance cadence, and ecosystem compensation/variety cost to viability economics.
- Applied minimum-sufficient-intervention research as a proportional selection heuristic, not a mandatory ladder or new Constitution rule.
- Clarified that temporary cognitive/operating modes do not change identity, role, qualification, or authority; no universal mode state machine was added.

## Architecture

- Strengthened the ENA narrow-waist criterion: standardize semantic properties required for truthful, viable interoperability while leaving Host/model/tool/cognitive implementation diversity outside the universal core when possible.
- Kept the Constitution at 38 machine-stable IDs and the capability map at 71 IDs; v0.3.2 deliberately avoids feature-count growth as a release goal.

## Validation tooling

- Added deterministic positive/negative validator fixtures and a `selftest` mode so documented semantic checks are reproducible.
- Kept schema PASS distinct from semantic support; did not add schemas merely to validate enums.
