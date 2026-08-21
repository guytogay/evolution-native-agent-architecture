# Persistent Project Contribution

Project: Evolution-Native Agent Architecture (ENA)
Contribution status: `UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED`
Date/time: `2026-08-20T22:00:00+08:00`
Target area: `research / machine-contract composition (v0.3.2 V2.2)`
Relationship to existing work: `NEW_EVIDENCE + IMPLEMENTATION_VARIANT + COMPOSITION_FAILURE`（composes V2 d178ff3 + V2.1 2380056）

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

V2.2 built ONE cumulative candidate validator composing all accepted V2 + V2.1 protections into a single executable contract surface, then replayed every historical fixture cumulatively (never reset): V2=23 + V2.1=18 + V2.2=7 = **48 fixtures**. `releases/current/` untouched; no promotion.

**Cumulative result:**

| Metric | Value |
|---|---|
| TOTAL_ADVERSARIAL_BLOCKED | **29 / 29** |
| ADVERSARIAL_UNKNOWN / LEAK | 0 / 0 |
| TOTAL_POSITIVE_PRESERVED | **14 / 19** |
| POSITIVE_UNKNOWN | 2 |
| POSITIVE_BLOCKED | 3 |

Portability: identical 29/29 + 14/19 on a fresh checkout (repo-relative; V2's hardcoded absolute path replaced by ancestor-based repo discovery).

## Inference

1. **A real composition regression was found and fixed (F3)**: V2.1's SUPPORT_WITHOUT_EVIDENCE protection leaked in the first cumulative run (S1 passed OK) because the typed resolution layer checked resolvability+applicability but not "resolved support must carry evidence". This proves **isolation-green does not imply composition-green** — the round's most important finding.
2. **Positive BLOCKs/UNKNOWNs are explicit composition costs (F1, F2)**: P1/P5/P6 now BLOCK (no registry → fail-closed resolvability) and P7/P9 degrade to UNKNOWN (registry absent → no silent label trust). These are the intended consequences of the user's resolvability/no-silent-trust requirements, reported not hidden. Legitimate controls must carry registries (V2.1 positives demonstrate the correct pattern and are preserved).
3. Typed resolution + duplicate rejection + eval-time + root-derivation all function in composition (V22-A1/A2/A3/A4/A5).

## Suggestion / question

1. Before any implementation acceptance of a hardened contract surface, require a **cumulative composition replay** like this one, not round-level green counts: isolation-green can hide composition regressions (S1 is the proof).
2. Treat "14/19 positive preserved with 5 documented composition costs" as the honest acceptance baseline: resolvability requires registries; without independent verification, root/grade/mandate truth remains self-declared (CON-029/027).
3. Prefer repo-relative prototype paths (as here) for portability.

## Evidence references

- Prototype (research-only): `research/prototypes/v2-machine-contract-hardening/v2.2/` (`cumulative_contract.py`, `fixtures_v22.py`, `run_v22.py`, `results-v22.json`, `README.md`)
- Composed: V2 `research/prototypes/v2-machine-contract-hardening/` (d178ff3) + V2.1 `.../v2.1/` (2380056)
- Prior: `collaboration/inbox/2026-08-20-2100-dsh-v21-second-order-adversarial-expansion.md`
- Full report (local): Obsidian `90 系统/审计/ENA v0.3.2 V2.2 Cumulative Contract Composition - DSH-2026-08-20.md`

## Known limitations / unknowns

- Synthetic fixtures; single host/session/model binding; no production workload.
- Registry/root/grade/mandate content-truth still self-declared without an independent verifier (documented residual).
- The 5 composition findings are costs/findings, not bugs hidden; project decision required on whether resolvability-with-registry is the accepted direction.

## Triggered follow-up obligations

```yaml
triggered_obligations:
  - obligation_id: "DSH-2026-08-20-OB-08"
    rule_ref: "ENA-CAP-065/066 + 08-RELEASE-DISCIPLINE (batching)"
    applicability: "APPLICABLE"
    materiality: "MATERIAL_TO_COMPLETION"
    status: "PENDING"
    required_before_claim: "any future 'hardened v0.3.2 contracts remain valid when composed' claim"
    evidence_refs: ["research/prototypes/v2-machine-contract-hardening/v2.2/results-v22.json"]
    resolution_reason: "Awaiting project decision; V2.2 is evidence+recommendation only."
```

## Requested reconciliation

- `ACCEPT_AS_EVIDENCE` of the cumulative result (29/29 + 14/19) and the five composition findings.
- `NEEDS_EXPERIMENT` / `ACCEPT_FOR_IMPLEMENTATION` (project decision) for the cumulative-contract direction.

## Authority / implementation note

- `advice only`. No release modification; no Mainline change; no promotion request. V2.2 lives only under `research/prototypes/`; `releases/current/` untouched.

## Notes

Do not present this contribution as accepted ENA truth merely because it is committed to GitHub.

Preserve the original contribution even after reconciliation.
