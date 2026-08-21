# Persistent Project Contribution

Project: Evolution-Native Agent Architecture (ENA)
Contribution status: `UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED`
Date/time: `2026-08-21T21:32:00+08:00`
Target area: `implementation / release candidate successor (v0.3.3-candidate.1)`
Relationship to existing work: `IMPLEMENTATION_SUCCESSOR_CORRECTION`（closes PR #38 fresh-validation defects D1/D2/D3 on frozen v0.3.3-candidate f7dc620；old candidate and releases/current/ UNTOUCHED；V2.x research loop NOT reopened）

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

v0.3.3-candidate.1 is the narrow implementation-successor correction closing the three defects found by fresh independent implementation validation (PR #38, `INDEPENDENT_IMPLEMENTATION_VALIDATION_NEEDS_REVISION`):

- **D1 (P42, false OK)**: `check_obligation_path()` no longer exempts non-completion claim types from bound-obligation gating — a material PENDING/FAILED/UNKNOWN obligation whose `required_before_claim_refs` names the claim gates ANY claim type. Completion claims keep their `required_obligation_refs` requirement; referenced-and-bound is evaluated once; unrelated obligations never poison.
- **D2 (P10, false BLOCK)**: `_support_sources()` splits top-level support into DIRECT (id-less, standalone, legitimate) and REGISTRY-ADDRESSABLE (id-carrying) forms; id-less support never silently resolves a ref; R12/list-ID/malformed rules unchanged.
- **D3 (P16/P17, false BLOCK)**: when `independence_basis` declares `root_provenance`, the composed root-registry-backed check is authoritative; the legacy `source_origins` check is suppressed via a shallow copy (shipped core byte-identical); five-state composed semantics preserved; source_origins-only stays legacy-coherent.

**Regression (235 cases exercised through the successor's real shipped surface):**

| Corpus | Count | Result |
|---|---|---|
| v0.3.2 migrated selftests | 10 | 10/10 (exact codes) |
| Inherited v2 (frozen) | 164 | **164/164, ZERO flips** |
| Closure v2.1 (PR #38 probes 43 + D-controls 18) | 61 | **61/61** |
| Total | 235 | **0 unexpected, 0 exceptions, deterministic** |

Provenance preserved: WORKBUDDY_FRESH_VALIDATOR_PR38 (43, payloads verbatim) and DSH_V033C1_CONTROLS (18) recorded separately; no Workbuddy expectation retroactively edited; PR #38 harness/manifest/results untouched.

**CI (recorded truthfully):** run **32486325485** → SUCCESS on the exact candidate ref `034b789…` (3.8/3.12/3.13); run **32486881934** → SUCCESS on the PR head incl. freeze record. Gate created after the candidate (candidate-gate-v033c1.yml, stdout-verdict CLI judging).

**Freeze:** semantic candidate ref `034b7895997dd0599a0bfea10de7acfac575f232`; freeze record `fbefa9a77d9618ba98153291295588222c2cc78d` (child commit; FREEZE-MANIFEST.md with changed-file list vs f7dc620, D1/D2/D3 exact changes, corpus by provenance, CI runs, determinism, trust boundaries, cost delta, old-releases confirmations, targeted-revalidation scope). Landed via PR #39 (merge `15dc89d`).

## Inference

1. The three accepted defects are closed without reopening prior protections: 164/164 inherited verdicts preserved, 61/61 closure controls pass, shipped core byte-identical.
2. Correct freeze order was followed: candidate+workflow committed → gate green on the exact candidate ref → freeze record created as a child commit → both CI runs recorded truthfully (no "all green at freeze" fiction).
3. The successor remains `IMPLEMENTATION_CANDIDATE / NOT_MAINLINE / NOT_PROMOTED` and is NOT independently validated.

## Suggestion / question

1. **Next actor: the SAME fresh WorkBuddy session that produced PR #38**, in a closed-scope `REVALIDATION_BY_PRIOR_IMPLEMENTATION_FALSIFIER` round (per the task §10): reproduce D1/D2/D3 on the old candidate, confirm closure on v0.3.3-candidate.1, verify directly affected positive controls, reproduce inherited regression, ensure no local regression. This is NOT a new blind independent validation.
2. Promotion remains a later Host decision after revalidation.

## Evidence references

- Successor candidate: `releases/v0.3.3-candidate.1/` (`tools/validate_contracts.py` (D1/D2/D3), `tools/contract-fixtures.v2.json` (inherited 164), `tools/contract-fixtures.v2.1.json` (61), `tools/pr38_fixtures.py`, `tools/d1d2d3_controls.py`, `tools/regression_suite.py`, `tools/regression-results-v033candidate1.json`, `FREEZE-MANIFEST.md`, `CANDIDATE-BASELINE.yaml`, `05-CORE-OPERATIONAL-CONTRACTS.md` §5.13.9)
- CI gate: `.github/workflows/candidate-gate-v033c1.yml`
- Fresh validation (accepted): `collaboration/inbox/2026-08-21-ena-v033-fresh-independent-validation-wb.report.md` (+ probe harness/manifest/results, PR #38, merge c1d29f6)
- Full report (local): Obsidian `90 系统/审计/ENA v0.3.3-candidate.1 Successor Correction - DSH-2026-08-21.md`

## Known limitations / unknowns

- Synthetic fixtures; single host/session/model binding; no production workload.
- Retained trust boundaries unchanged (registry/grade/mandate/scope self-declared; eval_time caller-controlled).
- PR #38 report §25 undercounted independence_basis coverage in the inherited corpus (it contains 20 occurrences); the D3 defect itself was confirmed by independent reproduction (P16/P17) and is closed.
- The successor is NOT independently validated; targeted revalidation by the prior implementation falsifier (WorkBuddy) is pending.
- CI verified on 3.8/3.12/3.13 (Linux); authoring runs on 3.14 (Windows).

## Triggered follow-up obligations

```yaml
triggered_obligations:
  - obligation_id: "DSH-2026-08-21-OB-05"
    rule_ref: "ENA-CAP-065/066 + 08-RELEASE-DISCIPLINE (batching)"
    applicability: "APPLICABLE"
    materiality: "MATERIAL_TO_COMPLETION"
    status: "PENDING"
    required_before_claim: "any 'v0.3.3-candidate.1 semantics revalidated' claim"
    evidence_refs: ["releases/v0.3.3-candidate.1/tools/regression-results-v033candidate1.json",
                    "releases/v0.3.3-candidate.1/FREEZE-MANIFEST.md"]
    resolution_reason: "Awaiting closed-scope revalidation by the prior implementation falsifier (WorkBuddy); no promotion implied."
```

## Requested reconciliation

- `ACCEPT_AS_EVIDENCE` of the successor freeze (034b789 / fbefa9a) and the D1/D2/D3 closure.
- `TARGETED_REVALIDATION` by the prior implementation falsifier (WorkBuddy, PR #38 session) — closed scope, not a new blind validation.

## Authority / implementation note

- `advice only`. No release modification; no Mainline change; no promotion request. `releases/current/` (v0.3.2) and `releases/v0.3.3-candidate/` untouched; V2.x research loop not reopened; no new semantic research version created.

## Notes

Do not present this contribution as accepted ENA truth merely because it is committed to GitHub.

Preserve the original contribution even after reconciliation.
