# CHANGELOG — v0.3.3-candidate

v0.3.3-candidate is the implementation candidate for the next release-candidate
validation cycle, built from the accepted V2.4.1 mechanism set
(reconciliation `ACCEPT_FOR_IMPLEMENTATION`, PR #34; mechanism source
`daacab1f042c38f3856ef4d0366febd1b5e47600`). Status:
`IMPLEMENTATION_CANDIDATE / NOT_MAINLINE / NOT_PROMOTED`. It is a self-contained
flat package over the frozen v0.3.2 baseline; `releases/current/` is unmodified.

## Composed claim-pack validation (new in this candidate)

- Added `validate_case()` to `tools/validate_contracts.py`: one composed
  validation surface (CLI mode `case`) over the unchanged shipped semantic core
  (validate_support / validate_obligation / validate_recovery).
- One canonical typed resolution layer for every consequential reference
  (support / obligation / evidence / root / authority namespaces); absent /
  present-but-missing / malformed registries are distinguishable; no
  raw-reference fallback when a supplied registry cannot resolve the artifact.
- Resolved support binds back to the target claim (`claim_ref`); the complete
  v0.3.2 applicability envelope is preserved (material missing observations are
  mismatches, not matches).
- Mandatory consequential evidence references resolve where the contract
  requires them (enforced when an evidence registry is supplied); absent
  registry keeps the baseline posture for support/capability/transfer/closure
  evidence and absent→UNKNOWN for recovery/independence provenance.
- Ambiguous duplicate identities fail closed; top-level and registry support
  representations compose consistently; obligation blocking is claim-aware.
- `STATE_AND_HISTORY` recovery establishes both state and history evidence;
  authority source semantics are positively typed or verified via an optional
  authority registry; PARTIAL support remains narrowed.
- Registry identity rule (R12): for dict-form registries the dict key is
  authoritative; an explicit inner id must equal the key or the registry is
  REGISTRY_MALFORMED; missing inner ids are backfilled.
- Obligation status outside the shipped triggered-obligation vocabulary is
  rejected at the semantic boundary (OBLIGATION_STATUS_OUTSIDE_VOCABULARY)
  without expanding the vocabulary.
- Malformed registry inputs produce machine verdicts (REGISTRY_MALFORMED),
  never uncaught exceptions; residual faults fail closed (EVALUATOR_FAULT);
  eval_time is explicitly required and caller-controlled (never silently
  defaulted).

## Regression inheritance

- Added `tools/contract-fixtures.v2.json` (164 cases): migrated v0.3.2
  selftests (provenance DSH_MIGRATED_V032) + accumulated V2.x falsification
  corpus with provenance preserved (DSH historical V2/V2.1/V2.2/V2.3,
  GPT-5.6 Sol I01–I16/O01–O04, WorkBuddy IND-01..17, DSH V2.4/V2.4.1 controls)
  + implementation controls. Deterministic runner: `tools/regression_suite.py`.
- Result: 164/164 passed, zero unexpected verdicts, zero uncaught exceptions,
  v0.3.2 selftests preserved 10/10.

## Schemas

- Added `schemas/composed-case.v1.schema.json`: input shape contract for
  validate_case (registries dict/list forms; R12 identity rule documented;
  semantic enforcement stays in the validator).

## Retained trust boundaries

Registry content truth, evidence grades, mandate content, and observed scope
remain self-declared; eval_time is caller-controlled; schema PASS remains
distinct from semantic support. See 05-CORE-OPERATIONAL-CONTRACTS.md 5.13.8.

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
