# Persistent Project Contribution

Project: Evolution-Native Agent Architecture (ENA)
Contribution status: `UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED`
Date/time: `2026-08-20T20:30:00+08:00`
Target area: `research / spec / machine-contract hardening (v0.3.2)`
Relationship to existing work: `COUNTEREXAMPLE + NEW_EVIDENCE + IMPLEMENTATION_VARIANT (research prototype)`

## Participant provenance

```yaml
participant:
  kind: "DeepSeek Harness"
  runtime_or_model: "deepseek-v4-flash via DeepSeek Harness Web GUI (DSH 0.x local runtime)"
  session_or_run_ref: "session-3b3cd6d7-9ccc-4523-8203-41be2c8b32fb"
  access_surfaces:
    github: "WRITE"
    google_drive: "NONE"
    other: ["Anytype MCP (knowledge base write)"]
  role_this_contribution: "CONTRIBUTOR / EXPERIMENTER / REVIEW_ONLY"
```

These fields describe provenance and technical capability, **not project authority**.

Tool access does not authorize Mainline modification, release, deployment, remediation, or scope expansion.

## Observed facts

V2 machine-contract hardening experiment executed against the six previously falsified false-claim vectors, on the real v0.3.2 toolchain (baseline) and a research-only hardened prototype (new, under `research/prototypes/v2-machine-contract-hardening/`). `releases/current/` was not modified.

**Baseline (shipped v0.3.2)**: 6/7 false claims still pass (A1 KNOW / A2 VERIFIED / A3 AUTHORITY / A5 RECOVERED / A6+A6b INDEPENDENT all PASS; A4 COMPLETED caught only when the obligation is submitted standalone, claim side passes).

**Hardened candidates**: adversarial **7/7 blocked**, legitimate positive controls **10/10 preserved**, second-order bypass attempts **6/6 blocked**.

Per-candidate (research-only; smallest change found):

| Candidate | Blocks | Preserves | New fields/rules | Cost | Residual surface |
|---|---|---|---|---|---|
| CLAIM_SUPPORTED_REQUIRES_REFS (I_KNOW) | A1 | P1,P2 | none / 1 rule | O(1) | LOW (ref resolution) |
| VERIFIED_REQUIRES_GRADE (I_VERIFIED) | A2 | P10 | evidence_grade / 1 rule | schema+validator | MEDIUM (grade self-declared) |
| AUTHORITY_REQUIRES_MANDATE (I_HAVE_AUTHORITY) | A3,S2 | P3,P4 | mandate.source+expires_at / 2 rules | schema+validator | MEDIUM (source forgeable) |
| OBLIGATION_CLAIM_LINK (I_COMPLETED) | A4,S3 | P5,P6 | claim.required_obligation_refs / 1 rule | schema+validator+registry | MEDIUM (unenumerated obligations) |
| RECOVERY_HISTORY_EVIDENCE (I_RECOVERED) | A5,S4 | P7,P8 | none / 3 rules | validator-only | LOW-MEDIUM (fabricated refs) |
| INDEPENDENCE_ROOT (EVIDENCE_INDEPENDENT) | A6,A6b,S5 | P9 | root_provenance / 2 rules | schema+validator | MEDIUM (fake roots) |

## Inference

- The **cheapest machine contract that blocks each material false claim while preserving legitimate cases exists and is small** (mostly schema fields + a few validator rules; one is validator-only).
- Dominant residual: content-bearing fields (evidence grade, mandate source, root provenance, closure evidence) remain **self-declared**; a schema/validator can block the *structural* false claim but cannot verify *content truth* without an independent verifier. This is a pre-existing authority limitation ("claimed issuer != verified issuer", CON-029/027), not a defect of the hardening.
- The hardening is genuinely protection beyond prose: 5/6 vectors are only prose-blocked in v0.3.2 today; each candidate turns a prose rule into a machine rule without rejecting the legitimate control.

## ENA-VAL comparison (v0.2.11 32 rules vs v0.3.2)

Only **5 of 32** ENA-VAL rule absences permit a **material** false claim in v0.3.2:
- ENA-VAL-013 (SUSPENDED claiming completion) — I_COMPLETED shape
- ENA-VAL-019 (composition inheriting component PASS) — I_VERIFIED shape
- ENA-VAL-022..025 (COMPLETE_HARD_MECHANICAL without effect-surface completeness) — I_VERIFIED/I_HAVE_AUTHORITY
- ENA-VAL-028 (non-active mechanism claiming current protection)
- ENA-VAL-030/031 (destructive history transform claiming preserved truth; k-0083 shape) — I_RECOVERED

The other 27 absences do not directly permit one of the six material vectors (governance-profile/mutation/elevation/activation-specific; covered by v0.3.2 prose or not material). **Deliberately not restored by count.** These five are candidates to revisit only when the corresponding artifact classes are machine-represented in a future v0.3.x.

## Suggestion / question

1. Review the five material ENA-VAL gaps for inclusion when the corresponding artifact classes (activation state, composition records, enforcement-surface records, mechanism status, history-transform records) gain machine representation.
2. Consider whether any of the six candidate rules should be folded into the v0.3.2 contract surface in a future batched release (08-RELEASE-DISCIPLINE: batch, do not micro-version).
3. Note that self-declared content fields need an independent verification path before "schema PASS" can be read as semantic support — the hardening narrows but does not close that gap.

## Evidence references

- Prototype (research-only): `research/prototypes/v2-machine-contract-hardening/` (`hardened_rules.py`, `fixtures.py`, `run_experiment.py`, `val_gap_analysis.py`, `results.json`, `README.md`)
- Baseline toolchain: `releases/current/tools/validate_contracts.py` + schemas (selftest 10/10 PASS confirmed)
- Prior falsification: `collaboration/inbox/2026-08-20-1900-dsh-six-false-claim-vectors.md`
- Full report (local): Obsidian `90 系统/审计/ENA v0.3.2 V2 Machine-Contract Hardening - DSH-2026-08-20.md`

## Known limitations / unknowns

- Synthetic attacks; single host/session/model binding; no production workload.
- Self-declared content fields remain unverifiable without an independent authority (documented residual).
- Whether the project plans a V2 adversarial-expansion round or prefers these rules folded into a future release is UNKNOWN; suggestions are advisory.

## Triggered follow-up obligations

```yaml
triggered_obligations:
  - obligation_id: "DSH-2026-08-20-OB-06"
    rule_ref: "ENA-CAP-065/066 + 08-RELEASE-DISCIPLINE (batching)"
    applicability: "APPLICABLE"
    materiality: "MATERIAL_TO_COMPLETION"
    status: "PENDING"
    required_before_claim: "any future 'v0.3.2 machine contracts block false claims' claim"
    evidence_refs: ["research/prototypes/v2-machine-contract-hardening/results.json"]
    resolution_reason: "Awaiting project decision on folding candidate rules into a future batched release."
```

## Requested reconciliation

- `ACCEPT_AS_EVIDENCE` of the hardening results (adversarial blocked, positive preserved, second-order blocked).
- `NEEDS_EXPERIMENT` / `ACCEPT_FOR_IMPLEMENTATION` (project decision) for the six candidate rules and the five material ENA-VAL gaps.

## Authority / implementation note

- `advice only`. No release modification; no Mainline change; no promotion request. The prototype lives only in `research/prototypes/`; `releases/current/` is untouched.

## Notes

Do not present this contribution as accepted ENA truth merely because it is committed to GitHub.

Preserve the original contribution even after reconciliation.
