# FREEZE-MANIFEST — ENA v0.3.3-candidate (Implementation Candidate)

> **Status: IMPLEMENTATION_CANDIDATE / NOT_MAINLINE / NOT_PROMOTED.**
> Role: IMPLEMENTATION AUTHOR (not independent validator, not promotion/release
> authority). `releases/current/` (v0.3.2) was NOT modified. This candidate is
> NOT called independently validated; the next actor is a fresh independent
> validator outside the V2.x lineage and the implementation authoring.
> Do not treat this candidate as accepted ENA truth.

## 1. Identity

| Field | Value |
|---|---|
| Repository | `guytogay/evolution-native-agent-architecture` |
| Implementation candidate code ref (immutable) | `f7dc6202dacd30e1f19d023146ecaeb4f020c922` |
| Freeze record ref | the commit containing this manifest |
| Base | ENA v0.3.2 `releases/current/` (frozen, unmodified) |
| Accepted mechanism source | V2.4.1 research successor `daacab1f042c38f3856ef4d0366febd1b5e47600` (freeze `b3d16988b65ea189b7ee82fd4b665bdb8bbb1f84`; reconciliation ACCEPT_FOR_IMPLEMENTATION, PR #34; prior-falsifier revalidation supported, PR #33) |
| Composed validation surface | `releases/v0.3.3-candidate/tools/validate_contracts.py :: validate_case()` (CLI mode `case`) |
| Deterministic validation surface | `tools/regression_suite.py` + `.github/workflows/candidate-gate.yml` (Python 3.8/3.12/3.13 matrix) |

## 2. Exact changed-file list relative to v0.3.2

The candidate is a self-contained flat package at `releases/v0.3.3-candidate/`.
Changes relative to `releases/current/` (v0.3.2) + CI:

| Change | Path |
|---|---|
| MODIFIED | `releases/v0.3.3-candidate/tools/validate_contracts.py` (shipped core byte-identical; composed layer added) |
| MODIFIED | `releases/v0.3.3-candidate/05-CORE-OPERATIONAL-CONTRACTS.md` (section 5.13) |
| MODIFIED | `releases/v0.3.3-candidate/CHANGELOG.md` (candidate changelog) |
| MODIFIED | `releases/v0.3.3-candidate/README.md` (candidate identity) |
| NEW | `releases/v0.3.3-candidate/CANDIDATE-BASELINE.yaml` |
| DELETED (vs the v0.3.2 copy) | `releases/v0.3.3-candidate/CURRENT-BASELINE.yaml` (replaced by CANDIDATE-BASELINE.yaml) |
| NEW | `releases/v0.3.3-candidate/schemas/composed-case.v1.schema.json` |
| NEW | `releases/v0.3.3-candidate/tools/contract-fixtures.v2.json` (164-case regression corpus) |
| NEW | `releases/v0.3.3-candidate/tools/regression_suite.py` |
| NEW | `releases/v0.3.3-candidate/tools/regression-results-v033candidate.json` (test evidence) |
| NEW | `releases/v0.3.3-candidate/tools/build_regression_corpus.py` (build-time migration tool) |
| NEW | `releases/v0.3.3-candidate/tools/freeze_hashes_v033candidate.py` (freeze helper) |
| NEW | `.github/workflows/candidate-gate.yml` (candidate validation gate) |

All other files under `releases/v0.3.3-candidate/` are byte-identical to the
v0.3.2 package (self-contained flat copy).

### 2.1 Digests (SHA-256 over committed blobs at `f7dc6202dacd30e1f19d023146ecaeb4f020c922`)

| SHA-256 (blob, LF) | Path |
|---|---|
| `5c428faddeeb00b8b4bd592537b146167ee4241548c75948a2b4e82afc4aed5e` | `releases/v0.3.3-candidate/CANDIDATE-BASELINE.yaml` |
| `921c0d7766476035b6fb37f92cd4846a4315b9e216d0224a7c5e3ac43a5143c0` | `releases/v0.3.3-candidate/README.md` |
| `c8331215856fa70894c6a235cbc1afbf36ebf72c51d1fdf01bcd1d96ad4e3a10` | `releases/v0.3.3-candidate/CHANGELOG.md` |
| `6d77ab6d158ac79eb5af69f7e17e7a6f4efc9a8c6f722a6937614093a11f99cf` | `releases/v0.3.3-candidate/05-CORE-OPERATIONAL-CONTRACTS.md` |
| `64fff203765e8a91b23814f1e692107c2dd2507e31e1d3afa80c5e7bb1be5294` | `releases/v0.3.3-candidate/schemas/composed-case.v1.schema.json` |
| `78c3ddeb1952826e90dadd1594afa3ae7690915de7127557bb68a04799a14e8c` | `releases/v0.3.3-candidate/tools/validate_contracts.py` |
| `9ab7400c7eac2ab09e852d9064bcb3b1742e99f12af0cbc93f4e88e6c61ddd9e` | `releases/v0.3.3-candidate/tools/contract-fixtures.v2.json` |
| `34d301f7ada713a2b6cf63aad2fb1567a2efb6b88c9d569672aeb0cf8a58e5e7` | `releases/v0.3.3-candidate/tools/regression_suite.py` |
| `fb61e3f9130ee5dfe58c52d60d155e9126b9868c9f937b1154f54ae21a3d8aed` | `releases/v0.3.3-candidate/tools/regression-results-v033candidate.json` |
| `78cdcf24660bf1a1377125bf84f09b3bf069591801f96f5f2e755eaa917557bc` | `releases/v0.3.3-candidate/tools/build_regression_corpus.py` |
| `f89be8b15e15c964df4df482633a0b020eb9c7e89f5df4fef79bd9a0943cf665` | `.github/workflows/candidate-gate.yml` |

Verify: `git show <ref>:<path> | sha256sum`, or
`python releases/v0.3.3-candidate/tools/freeze_hashes_v033candidate.py <ref>`.

## 3. Research-mechanism → implementation-surface mapping

| Accepted mechanism (V2.4.1) | Implementation surface |
|---|---|
| Consequential refs resolve through coherent typed resolution | `validate_contracts.py :: typed_resolve()` + `normalize_registry()` — one canonical resolver for every consequential ref (R1) |
| Support binds to the actual target claim | `check_support_path()` → `SUPPORT_TARGET_MISMATCH` (R2; shipped `CLAIM_REF_MISMATCH` also retained) |
| Absent / present-missing / malformed registries distinguishable | `normalize_registry()` tri-state; absent → `ABSENT_POLICY`, missing → `{KIND}_REF_UNRESOLVABLE`, malformed → `REGISTRY_MALFORMED` (R3/R11) |
| No raw-reference fallback when a supplied registry cannot resolve | enforced in `typed_resolve()` (R3) |
| Complete applicability envelope preserved | shipped `SCOPE_KEYS` (8 dims) via unchanged `validate_support`; material missing observations are mismatches (R4) |
| Mandatory consequential evidence refs resolve | `check_evidence_refs()` on support/capability/transfer/recovery/closure paths when an evidence registry is supplied (R3) |
| Ambiguous duplicate identities fail closed | `typed_resolve()` fingerprint dedup vs `DUPLICATE_REF_ID`/`DUPLICATE_OBLIGATION_ID` (R5) |
| Top-level and registry support representations compose | `_support_sources()` (top-level + `support_registry` + `support_relations`, dict/list) (R6) |
| Obligation validation remains claim-aware | `check_obligation_path()` — only referenced or claim-bound obligations gate (R7) |
| Malformed registry inputs → machine verdicts, never exceptions | `REGISTRY_MALFORMED` + `EVALUATOR_FAULT` fail-safe in `validate_case()` (R11) |
| STATE_AND_HISTORY establishes state AND history evidence | `check_recovery_path()` — `STATE_RESTORE_WITHOUT_EVIDENCE` + history evidence + root distinctness (R8) |
| Authority source positively typed / explicitly bounded | `AUTHORIZING_MANDATE_SOURCES` + optional `authority_registry` grant verification (R9) |
| PARTIAL support remains narrowed | `check_support_path()` — `PARTIAL_SUPPORT_ONLY` unless `support_claim == "PARTIAL"` (R10) |
| R12 registry identity rule | `normalize_registry()` dict branch + `_support_sources()` dict branch (R12) |
| Obligation status outside shipped vocabulary rejected | `OBLIGATION_STATUS_VOCABULARY` gate in `_validate_case()` (F2; vocabulary NOT expanded) |
| Caller-controlled time, never silently defaulted | `validate_case()` requires `eval_time` (param or payload) → `EVAL_TIME_REQUIRED` |
| Contract semantics documentation | `05-CORE-OPERATIONAL-CONTRACTS.md` §5.13.1–5.13.8 |
| Input shape contract | `schemas/composed-case.v1.schema.json` (registries dict/list forms; R12 documented; semantics machine-enforced) |
| Deterministic validation/package surface | `tools/regression_suite.py` + `candidate-gate.yml` (3 Python versions) |

## 4. Regression corpus summary by provenance (`tools/contract-fixtures.v2.json`, 164 cases)

| Provenance | Count | Source |
|---|---|---|
| DSH_HISTORICAL_V2 | 23 | research V2 fixtures (frozen, payloads byte-for-byte) |
| DSH_HISTORICAL_V21 | 18 | research V2.1 fixtures |
| DSH_HISTORICAL_V22 | 7 | research V2.2 fixtures |
| DSH_HISTORICAL_V23_MIGRATED | 5 | research V2.3 migrated positives |
| GPT56SOL_INDEPENDENT | 20 | GPT-5.6 Sol probes I01–I16 + O01–O04 (PR #23) |
| WORKBUDDY_INDEPENDENT | 25 | WorkBuddy probes IND-01..17 (PR #30) |
| DSH_V24_CONTROLS | 25 | successor regression controls |
| DSH_V241_CONTROLS | 25 | F1/F2 closure controls |
| DSH_MIGRATED_V032 | 10 | shipped v0.3.2 selftests, intentionally migrated unchanged |
| DSH_IMPLEMENTATION_CONTROLS | 6 | implementation-level controls (eval-time requirement, exception safety, R12/F2 at implementation level) |
| **TOTAL** | **164** | provenance preserved; no historical fixture rewritten |

Expected verdicts for corpus cases are the frozen reconciled expectations from
the accepted V2.4.1 replay (`results-v241.json`); migrated v0.3.2 cases keep
their shipped ok/code expectations.

## 5. Test results (implementation candidate exercised through its real surface)

Run locally (Python 3.14, Windows) and enforced in CI
(`candidate-gate.yml`, Python 3.8/3.12/3.13):

| Check | Result |
|---|---|
| Shipped core functions byte-identical to v0.3.2 | verified (AST-level, 7/7 identical) |
| Migrated v0.3.2 selftests (v1 fixtures) | **10/10 passed** (exact codes, unchanged) |
| Composed corpus selftest (v2 fixtures, CLI path) | **164/164 passed** (`SELFTEST_PASS`, 0 failed) |
| Regression suite (deterministic runner) | **0 unexpected verdicts, 0 uncaught exceptions** |
| By-provenance | DSH historical 53/53 · GPT56SOL 20/20 · WORKBUDDY 25/25 · DSH controls 50/50 · migrated 10/10 · impl controls 6/6 |
| CLI `case` mode spot checks | pass (IMP-01 → OK; IND-02E → BLOCK REGISTRY_MALFORMED; IND-01 → BLOCK OBLIGATION_STATUS_OUTSIDE_VOCABULARY) |
| Determinism | double-run of regression_suite produces byte-identical results JSON |
| Candidate baseline pointer | `v0.3.3-candidate / IMPLEMENTATION_CANDIDATE / mainline_claim_allowed=false` |

Evidence: `tools/regression-results-v033candidate.json` (deterministic).

## 6. Retained trust boundaries (do not pretend eliminated)

1. Registry content truth, evidence grades, mandate content, and observed scope
   are **self-declared**; the validator verifies resolution/structure/
   consistency, not external attestation (CON-029/027).
2. `eval_time` is **caller-controlled** and explicitly required; it is never
   silently defaulted (deterministic, but not an independent clock).
3. Evidence-existence posture: when no evidence registry is supplied,
   support/capability/transfer/closure evidence existence is not verified
   (baseline posture, required to preserve legitimate top-level support);
   recovery/independence provenance keeps absent → UNKNOWN.
4. Mandate-source vocabulary (`AUTHORIZING_MANDATE_SOURCES`) must be maintained;
   `authority_registry` is the upstream-verification extension mechanism.
5. Schema PASS remains distinct from semantic support
   (`composed-case.v1.schema.json` is a shape contract; R12 and all semantics
   are machine-enforced by the validator).
6. The candidate is research-accepted mechanism, not production truth; status
   is IMPLEMENTATION_CANDIDATE / NOT_MAINLINE / NOT_PROMOTED.

## 7. Implementation / governance cost delta (vs v0.3.2)

| Metric | v0.3.2 | v0.3.3-candidate |
|---|---|---|
| Validator surface | 162 lines, 3 semantic checks | 162-line shipped core unchanged + composed layer (~430 lines added) |
| New public entry point | — | `validate_case(payload, eval_time)` + CLI mode `case` |
| New schemas | 5 | 6 (+1 composed-case shape contract) |
| New explicit codes | ~10 | +9 composed codes (tri-state resolution, R12, F2, partial, state evidence, etc.) |
| Regression corpus | 10 selftest cases | 164 cases (154 new) |
| CI gate | main-gate (current only) | + candidate-gate (3 Python versions) |
| Runtime dependencies | stdlib | stdlib (unchanged) |
| Governance cost | — | one authorizing-source vocabulary constant; eval_time caller discipline; corpus maintenance |

Rationale for the size: the composed layer is the smallest coherent production
translation of the accepted mechanisms — one resolver, one entry point, no new
governance machinery, no new runtime dependencies, no schema-vocabulary
expansion. Each mechanism answers: what false claim it prevents / what agency it
preserves / what it costs / why smallest — documented in the function docstrings
and 05-CORE-OPERATIONAL-CONTRACTS.md §5.13.

## 8. Deliberately NOT implemented (and why)

1. **Registry content self-declaration removal (external attestation)** — NOT
   implemented: out of scope for a validator; requires an external authority
   surface that this candidate does not own (retained trust boundary #1).
2. **New obligation statuses (e.g. OPEN as a real state)** — NOT implemented:
   the shipped schema vocabulary is the canonical input contract; expanding it
   was explicitly rejected (F2 closed as defense in depth, not vocabulary
   expansion).
3. **A default/ambient eval_time** — NOT implemented: would break determinism
   and reintroduce the hardcoded-date defect the V2.1 round eliminated.
4. **PARTIAL-assertion natural-language narrowing** — NOT implemented: the
   machine cannot parse assertion text; the explicit `support_claim` marker is
   the smallest machine-encodable narrowing (I14 open semantic challenge).
5. **Schema-level enforcement of R12** — NOT implemented: JSON Schema cannot
   express "inner id must equal key"; the validator machine-enforces it (shape
   contract + semantic enforcement split).
6. **New governance/role machinery** — NOT implemented: ENA preserves viable
   agency; the candidate adds a validation surface, not obedience machinery.

## 9. Recommendation for the fresh independent-validation actor

- Target: a fresh independent validator with NO V2.x lineage or implementation
  authoring participation (prior WorkBuddy revalidation was prior-falsifier
  closure evidence, not fresh blind validation of this candidate).
- Scope: (a) verify candidate identity/hashes at `f7dc6202dacd30e1f19d023146ecaeb4f020c922`;
  (b) reproduce `python releases/v0.3.3-candidate/tools/regression_suite.py`
  (expect PASS, zero unexpected, zero exceptions) and the CLI selftest of
  `contract-fixtures.v2.json`; (c) blind-semantic probing of
  `validate_case()` — new adversarial and legitimate composed cases, especially
  registry identity (R12), tri-state resolution, claim-aware obligations, and
  the evidence-existence posture; (d) challenge the composed-case input contract
  and the retained trust boundaries rather than only the author corpus.
- Success criterion for the candidate: the fresh validator finds no
  decision-changing false OK / new legitimate false BLOCK / unnecessary UNKNOWN /
  uncaught exception on the implementation surface.
- The V2.x research-hardening loop is CLOSED; further open-ended research
  expansion is not requested. Promotion remains a later Host decision after
  implementation-candidate validation.

## 10. Freeze declaration

The v0.3.3-candidate implementation candidate is frozen at code ref
`f7dc6202dacd30e1f19d023146ecaeb4f020c922` (+ freeze-record tip containing this
manifest). Status remains `IMPLEMENTATION_CANDIDATE / NOT_MAINLINE /
NOT_PROMOTED`. `releases/current/` (v0.3.2) is unmodified. The candidate is NOT
independently validated; the next actor is a fresh independent validator.
