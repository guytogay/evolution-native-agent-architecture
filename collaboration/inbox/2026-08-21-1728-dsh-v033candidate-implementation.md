# Persistent Project Contribution

Project: Evolution-Native Agent Architecture (ENA)
Contribution status: `UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED`
Date/time: `2026-08-21T17:28:00+08:00`
Target area: `implementation / release candidate (v0.3.3-candidate)`
Relationship to existing work: `IMPLEMENTATION_CANDIDATE`（translates accepted V2.4.1 mechanism set daacab1 into shipped surfaces; reconciliation ACCEPT_FOR_IMPLEMENTATION PR #34; V2.x research loop CLOSED; releases/current/ UNTOUCHED）

## Participant provenance

```yaml
participant:
  kind: "DeepSeek Harness"
  runtime_or_model: "deepseek-v4-flash via DeepSeek Harness Web GUI (DSH 0.x local runtime)"
  session_or_run_ref: "session-3b3cd6d7-9ccc-4523-8203-41be2c8b32fb"
  access_surfaces:
    github: "WRITE (PR-based)"
    google_drive: "NONE"
    other: ["Anytype MCP (knowledge base write)"]
  role_this_contribution: "IMPLEMENTATION_AUTHOR (NOT independent validator; NOT promotion/release authority)"
```

These fields describe provenance and technical capability, **not project authority**.

Tool access does not authorize Mainline modification, release, deployment, remediation, or scope expansion.

## Observed facts

Built the ENA v0.3.3-candidate implementation candidate from the accepted V2.4.1 mechanism set (reconciliation `ACCEPT_FOR_IMPLEMENTATION`, PR #34; mechanism source `daacab1f042c38f3856ef4d0366febd1b5e47600`), mapped into the actual shipped surfaces rather than copied blindly:

- **Validators/tools**: `releases/v0.3.3-candidate/tools/validate_contracts.py` — shipped v0.3.2 core byte-identical (AST-verified 7/7 functions; v0.3.2 selftests 10/10 preserved) + composed `validate_case()` layer (CLI mode `case`) implementing R1–R12 + F2: one canonical typed resolver, tri-state registries (absent/present-missing/malformed, no raw fallback), R2 claim binding, R4 full 8-dim applicability envelope, evidence existence, identity-ambiguity duplicates, representation composition, claim-aware obligations, R8 dual recovery evidence, R9 positive mandate typing, R10 PARTIAL narrowing, R11 never-exception, R12 registry identity rule, F2 obligation-status vocabulary gate (vocabulary NOT expanded), explicit eval_time (never silently defaulted).
- **Schemas**: `schemas/composed-case.v1.schema.json` (input shape contract; semantics stay machine-enforced).
- **Contract semantics**: `05-CORE-OPERATIONAL-CONTRACTS.md` §5.13 (per-mechanism rationale + retained trust boundaries).
- **Fixtures/selftests**: `tools/contract-fixtures.v2.json` — 164 cases, provenance preserved (DSH historical 53, GPT-5.6 Sol 20, WorkBuddy 25, DSH controls 50, migrated v0.3.2 selftests 10, implementation controls 6); deterministic runner `tools/regression_suite.py`.
- **Deterministic validation surface**: `.github/workflows/candidate-gate.yml` (Python 3.8/3.12/3.13).

**Validation (implementation candidate exercised through its real shipped surface, not research-prototype import):**

- Migrated v0.3.2 selftests: 10/10 (exact codes, unchanged).
- Composed corpus selftest via the shipped CLI: 164/164 (`SELFTEST_PASS`).
- Regression suite: 0 unexpected verdicts, 0 uncaught exceptions; by-provenance 164/164.
- CI (candidate-gate): pass on 3.8 / 3.12 / 3.13; main-gate + CodeQL pass.
- Determinism: double-run byte-identical results.

**Freeze:** candidate code ref `f7dc6202dacd30e1f19d023146ecaeb4f020c922`; freeze record `6a4404119ac7d9ee0c927cd3a96d1adf26e32ba3` (`releases/v0.3.3-candidate/FREEZE-MANIFEST.md`: changed-file list vs v0.3.2, mechanism→surface mapping, corpus by provenance, test results, retained trust boundaries, cost delta, deliberately-not-implemented list, fresh-validator recommendation). Landed via PR #35 (merge `c02cd2a`).

## Inference

1. The accepted mechanisms map to a **smaller, coherent production surface**: one composed entry point over the unchanged shipped core; +9 explicit codes; no new runtime dependencies; no governance machinery beyond one vocabulary constant and an explicit eval_time discipline.
2. **Regression inheritance is real, not nominal**: the 164-case implementation corpus carries DSH, GPT-5.6 Sol, and WorkBuddy provenance byte-for-byte; the falsification history is exercised through the implementation candidate's own surface in CI on three Python versions.
3. **Trust boundaries are retained, not hidden**: registry/grade/mandate/scope content remain self-declared; eval_time is caller-controlled; the candidate does not claim external truth.

## Suggestion / question

1. **Next actor: a fresh independent validator with NO V2.x lineage or implementation authoring participation** (per reconciliation; the prior WorkBuddy revalidation was prior-falsifier closure evidence, not fresh blind validation of this candidate). Suggested scope is documented in `FREEZE-MANIFEST.md` §9: identity/hash verification, regression reproduction, blind semantic probing of `validate_case()`, challenge of the composed-case input contract and retained trust boundaries.
2. Promotion remains a later Host decision after implementation-candidate validation.
3. Do NOT treat this candidate as accepted ENA truth merely because it is committed to GitHub.

## Evidence references

- Implementation candidate: `releases/v0.3.3-candidate/` (`tools/validate_contracts.py`, `tools/contract-fixtures.v2.json`, `tools/regression_suite.py`, `tools/regression-results-v033candidate.json`, `schemas/composed-case.v1.schema.json`, `CANDIDATE-BASELINE.yaml`, `FREEZE-MANIFEST.md`, `05-CORE-OPERATIONAL-CONTRACTS.md` §5.13, `CHANGELOG.md`, `README.md`)
- CI gate: `.github/workflows/candidate-gate.yml`
- Mechanism source (frozen): `research/prototypes/v2-machine-contract-hardening/v2.4.1/` @ `daacab1f042c38f3856ef4d0366febd1b5e47600`
- Reconciliation: `collaboration/reconciliation/2026-08-21-v241-targeted-revalidation-final-reconciliation.md`
- Full report (local): Obsidian `90 系统/审计/ENA v0.3.3-candidate Implementation Candidate - DSH-2026-08-21.md`

## Known limitations / unknowns

- Synthetic fixtures; single host/session/model binding; no production workload.
- Registry/grade/mandate content-truth self-declared (retained trust boundaries); eval_time caller-controlled.
- PARTIAL-assertion natural-language narrowing is an open semantic question (explicit `support_claim` marker is the minimal machine-encodable form).
- The candidate is NOT independently validated; fresh-validator validation is pending.
- CI verified on 3.8/3.12/3.13 (Linux); local authoring runs on 3.14 (Windows).

## Triggered follow-up obligations

```yaml
triggered_obligations:
  - obligation_id: "DSH-2026-08-21-OB-04"
    rule_ref: "ENA-CAP-065/066 + 08-RELEASE-DISCIPLINE (batching)"
    applicability: "APPLICABLE"
    materiality: "MATERIAL_TO_COMPLETION"
    status: "PENDING"
    required_before_claim: "any 'v0.3.3-candidate implementation semantics validated' claim"
    evidence_refs: ["releases/v0.3.3-candidate/tools/regression-results-v033candidate.json",
                    "releases/v0.3.3-candidate/FREEZE-MANIFEST.md"]
    resolution_reason: "Awaiting fresh independent validation of the implementation candidate; no promotion implied."
```

## Requested reconciliation

- `ACCEPT_AS_EVIDENCE` of the implementation candidate freeze (f7dc620 / 6a44041).
- `FRESH_INDEPENDENT_VALIDATION` of the implementation candidate (actor outside V2.x lineage and implementation authoring).
- `HOST_DECISION` on any subsequent promotion/release consideration (not requested now).

## Authority / implementation note

- `advice only`. No release modification; no Mainline change; no promotion request. `releases/current/` (v0.3.2) untouched; V2.x research loop closed; no v0.2.12/v0.3.3 created. Candidate status: `IMPLEMENTATION_CANDIDATE / NOT_MAINLINE / NOT_PROMOTED`.

## Notes

Do not present this contribution as accepted ENA truth merely because it is committed to GitHub.

Preserve the original contribution even after reconciliation.
