# Persistent Project Contribution

Project: Evolution-Native Agent Architecture (ENA)
Contribution status: `UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED`
Date/time: `2026-08-21T09:50:00+08:00`
Target area: `research / acceptance semantics + candidate freeze (v0.3.2 V2.3)`
Relationship to existing work: `NEW_EVIDENCE + SEMANTICS_LAYER + FROZEN_RESEARCH_CANDIDATE`（composes V2 d178ff3 + V2.1 2380056 + V2.2 34e7456；candidate implementation ZERO changes）

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
  role_this_contribution: "CONTRIBUTOR / EXPERIMENTER / CANDIDATE_AUTHOR (frozen; NOT independent validator)"
```

These fields describe provenance and technical capability, **not project authority**.

Tool access does not authorize Mainline modification, release, deployment, remediation, or scope expansion.

## Observed facts

V2.3 established EXPLICIT acceptance semantics and replayed the ENTIRE cumulative fixture corpus plus migrated positive controls through the SAME composed candidate implementation (`v2.2/cumulative_contract.py`, zero candidate changes — the identical validator frozen at V2.2 `34e7456`):

| Corpus | Count |
|---|---|
| V2 (`fixtures.py`) | 23 (10 POS, 7 ADV, 6 SECOND_ORDER) |
| V2.1 (`fixtures_v21.py`) | 18 (7 POS, 11 ATTACK) |
| V2.2 (`fixtures_v22.py`) | 7 (2 POS, 5 ATTACK) |
| V2.3 migrated (`fixtures_migrated.py`) | 5 (P1m, P5m, P6m, P7m, P9m) |
| **TOTAL** | **53** |

The five historical non-OK positives (P1/P5/P6 → BLOCK; P7/P9 → UNKNOWN) were preserved byte-for-byte unchanged. Migrated equivalents supply the registry/provenance/support information the cumulative contract legitimately requires (no protection weakened).

**Verdict-correctness result (53/53 matched, ZERO unexpected):**

| Category | Expected | Actual | Matched |
|---|---|---|---|
| adversarial (29) | BLOCK | BLOCK | 29/29 |
| mandatory-unresolvable (P1, P5, P6) | BLOCK | BLOCK | 3/3 |
| uncertainty-positive (P7, P9) | UNKNOWN | UNKNOWN | 2/2 |
| sufficient-positive (14) | OK | OK | 14/14 |
| migrated-positive (5) | OK | OK | 5/5 |

Frozen for independent validation: candidate code ref `8eb5a9afa4c560645b4c50dc24af7874ed54a4f2`; freeze record `89d5f97c71a762ec8b06e3a43cb385c96d2ad926` (contains FREEZE-MANIFEST.md with exact file set + SHA-256 + reproduction command + 8 residual trust boundaries). Both pushed to `main` (`34e7456..89d5f97`).

## Inference

1. **Acceptance semantics are now explicit and machine-checkable**: BLOCK = materially false/invalid OR mandatory support unresolvable (fail-closed); OK = legitimate with sufficient resolvable support; UNKNOWN = legitimate but materially unverifiable where uncertainty is allowed. UNKNOWN is deliberately NOT BLOCK — the contract refuses to endorse an unverifiable-but-legitimate claim without branding it false.
2. **The historical verdict changes are intended consequences, not regressions**: P1/P5/P6 BLOCK because SUPPORTED/completion makes resolvable support a MANDATORY precondition (uncertainty is not allowed for a mandatory precondition); P7/P9 UNKNOWN because the claims are well-formed but root distinctness/origin uniqueness cannot be verified without the required registry. The migrated controls (P1m/P5m/P6m/P7m/P9m) demonstrate the legitimate pattern and all reach OK.
3. **Verdict correctness over green count**: the success criterion (zero unexpected verdicts, 53/53) is about semantic expectation matching, not how many fixtures pass.

## Suggestion / question

1. Independent validation of the frozen candidate is requested: check out `8eb5a9a` (or freeze-record tip `89d5f97`), run from repo root `python research/prototypes/v2-machine-contract-hardening/v2.3/run_v23.py`; success = `UNEXPECTED_VERDICTS: 0`, exit 0. Challenge the expected-verdict manifest itself, not just the replay.
2. Project decision required on whether resolvability-with-registry (registries carried by the claim pack) is the accepted direction for a future hardened surface; the residual trust boundaries (registry/grade/mandate content-truth self-declared, CON-029/027) remain.
3. Do NOT promote or adopt based on this contribution alone; promotion is Host authority, not DSH's.

## Evidence references

- Prototype (research-only): `research/prototypes/v2-machine-contract-hardening/v2.3/` (`acceptance_semantics.py`, `fixtures_migrated.py`, `run_v23.py`, `expected-verdict-manifest.json`, `results-v23.json`, `FREEZE-MANIFEST.md`, `freeze_hashes.py`)
- Candidate (UNCHANGED): `research/prototypes/v2-machine-contract-hardening/v2.2/cumulative_contract.py` (`34e7456`)
- Prior: `collaboration/inbox/2026-08-20-2200-dsh-v22-cumulative-contract-composition.md`
- Full report (local): Obsidian `90 系统/审计/ENA v0.3.2 V2.3 Acceptance Semantics & Candidate Freeze - DSH-2026-08-21.md`

## Known limitations / unknowns

- Synthetic fixtures; single host/session/model binding; no production workload.
- Registry/root/grade/mandate content-truth still self-declared without an independent verifier (documented residual trust boundaries 1–5, 7 in FREEZE-MANIFEST.md).
- Known unfixed code defect: `hardened_rules.py:17` machine-specific absolute path (residual boundary 6) — does not affect the replay; left untouched to preserve candidate immutability.
- The candidate author (DSH) did NOT and will not perform the independent validation itself.

## Triggered follow-up obligations

```yaml
triggered_obligations:
  - obligation_id: "DSH-2026-08-21-OB-01"
    rule_ref: "ENA-CAP-065/066 + 08-RELEASE-DISCIPLINE (batching)"
    applicability: "APPLICABLE"
    materiality: "MATERIAL_TO_COMPLETION"
    status: "PENDING"
    required_before_claim: "any future 'V2.3 acceptance semantics remain valid under independent validation' claim"
    evidence_refs: ["research/prototypes/v2-machine-contract-hardening/v2.3/results-v23.json",
                    "research/prototypes/v2-machine-contract-hardening/v2.3/FREEZE-MANIFEST.md"]
    resolution_reason: "Awaiting independent validation; V2.3 is a frozen research candidate only."
```

## Requested reconciliation

- `ACCEPT_AS_EVIDENCE` of the zero-unexpected verdict-correctness result and the frozen candidate.
- `INDEPENDENT_VALIDATION` of the frozen candidate (candidate author excluded by lineage).
- `NEEDS_PROJECT_DECISION` for any future hardening direction based on this candidate.

## Authority / implementation note

- `advice only`. No release modification; no Mainline change; no promotion request. V2.3 lives only under `research/prototypes/`; `releases/current/` untouched; no v0.2.12 / v0.3.3 created.

## Notes

Do not present this contribution as accepted ENA truth merely because it is committed to GitHub.

Preserve the original contribution even after reconciliation.
