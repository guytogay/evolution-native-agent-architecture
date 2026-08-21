# Persistent Project Contribution

Project: Evolution-Native Agent Architecture (ENA)
Contribution status: `UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED`
Date/time: `2026-08-21T11:30:00+08:00`
Target area: `research / independent-finding reconciliation + successor candidate (v0.3.2 V2.4)`
Relationship to existing work: `RECONCILIATION + SUCCESSOR_CANDIDATE`（reconciles PR #23 validation of frozen V2.3 8eb5a9a；successor v2.4 47e0e1b；frozen candidate and releases/current/ UNTOUCHED）

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

V2.4 reconciled the independent validation (PR #23, GPT-5.6 Sol, verdict NEEDS_REVISION) of the frozen V2.3 candidate and built a successor.

**Phase 1 — reconciliation (every finding independently reproduced at frozen ref 8eb5a9a, `reproduce_v23.py` → `reproduction-v23.json`):**

- 16 × CONFIRMED_MATERIAL_DEFECT: false OK × 12 (I01–I05, I08–I13), false BLOCK × 2 (I06, I07 = composition failures CF-1/CF-2), applicability regression CF-3 (I04/I05), exceptions × 2 (I15/I16), oracle design defect (O01–O04).
- 1 × SEMANTIC_CHALLENGE / NEEDS_EXPERIMENT (I14, PARTIAL support) — treated separately; minimal machine rule implemented, full assertion-narrowing semantics documented as open.
- 0 × NOT_REPRODUCED; 0 × CONFIRMED_BUT_EXPECTED_BOUNDARY.
- No remediation adopted merely because it came from the independent validator; each was confirmed against frozen code + shipped baseline before implementation. Full per-finding records: `RECONCILIATION.md`.

**Phase 2 — successor (`v2.4/successor_contract.py`): ONE canonical typed-resolution layer** (`typed_resolve` + `normalize_registry`) replacing the frozen candidate's 7 ad-hoc mechanisms; protections R1–R11 (typed refs; support→claim binding; registry tri-state absent|present-missing|malformed with NO raw fallback; full 8-dim baseline applicability envelope; identity-ambiguity duplicates; dict/list representation composition; claim-aware obligations; state+history evidence for full recovery; positive mandate typing or authority_registry; PARTIAL→UNKNOWN with explicit narrowing marker; REGISTRY_MALFORMED never-exception).

**Phase 3 — regression discipline (98-fixture accumulated corpus through ONE successor):**

| Corpus | Count | Result |
|---|---|---|
| Frozen V2.3 (unchanged) | 53 | **53/53 verdicts preserved (ZERO flips)** |
| Independent I01–I16 + O01–O04 | 20 | **20/20 matched; oracle vs independent expectations 20/20 consistent** |
| Successor controls (15 pos / 10 neg) | 25 | **25/25** |
| TOTAL | 98 | **UNEXPECTED_VERDICTS: 0** (BLOCK 55 / OK 40 / UNKNOWN 3) |

Exceptions: 0. Composition failures CF-1/2/3 fixed. New trust boundaries: 8 (evidence-existence posture; mandate-source vocabulary; registry truth self-declared; eval_time caller-controlled; PARTIAL narrowing marker; hardened_rules stale-path defect ELIMINATED from successor import surface; research-only; corpus authorship).

**Phase 4 — freeze:** successor code ref `47e0e1b121b1ef1e8911c59980c99805ded5a963`; freeze record `5f5dfca` (FREEZE-MANIFEST-V24.md: exact file set + SHA-256, corpus manifest, reconciliation summary, reproduction command, 8 trust boundaries, complexity cost). Pushed `550437b..5f5dfca`.

## Inference

1. **Success is not "fix every validator complaint" — it is coherence.** The successor is smaller and more coherent: 528 lines / 45 distinct codes vs frozen 550 lines / 57 codes; 1 canonical resolver vs 7 ad-hoc mechanisms; no raw-string fallback inversion; machine-specific path defect eliminated.
2. **Zero frozen verdict flips is the strongest regression statement**: all 53 accepted V2.3 semantics survive intact while 16 confirmed defects are fixed — local protections compose without weakening each other.
3. **The independent validator's ground truth constrained the design** (e.g., I06's OK expectation forced the evidence-existence posture: absent registry → no evidence verdict on support/capability/transfer/closure paths; supplied registry → strict resolution). I14 remains the honest open semantic question.
4. **The successor is NOT independently validated.** It is a frozen research candidate awaiting independent validation; the candidate author did not and will not self-validate.

## Suggestion / question

1. Independent validation of the successor is requested: check out `47e0e1b` (or freeze-record tip `5f5dfca`), run from repo root `python research/prototypes/v2-machine-contract-hardening/v2.4/run_v24.py`; success = `UNEXPECTED_VERDICTS: 0`, exit 0. Challenge the structural oracle and the 25 remediation controls, not just the replay.
2. Project decision required on the canonical-typed-resolution direction (R1–R11) before any future hardening; the evidence-existence posture (R3) and mandate vocabulary (R9) are the key semantic choices to ratify.
3. Do NOT promote or adopt based on this contribution alone; promotion is Host authority.

## Evidence references

- Prototype (research-only): `research/prototypes/v2-machine-contract-hardening/v2.4/` (`successor_contract.py`, `acceptance_semantics_v24.py`, `independent_fixtures.py`, `successor_controls.py`, `run_v24.py`, `reproduce_v23.py`, `RECONCILIATION.md`, `reproduction-v23.json`, `results-v24.json`, `FREEZE-MANIFEST-V24.md`, `freeze_hashes_v24.py`)
- Frozen candidate (UNCHANGED): `.../v2.2/cumulative_contract.py` @ `8eb5a9a`
- Independent validation (reconciled): `collaboration/inbox/2026-08-21-ena-v23-independent-validation-gpt56sol.md` (PR #23, merged 550437b)
- Full report (local): Obsidian `90 系统/审计/ENA v0.3.2 V2.4 Independent-Finding Reconciliation & Successor Candidate - DSH-2026-08-21.md`

## Known limitations / unknowns

- Synthetic fixtures; single host/session/model binding; no production workload.
- Registry/grade/mandate content-truth still self-declared without an independent verifier (trust boundaries 3–4).
- Evidence-existence posture (R3) is a design choice constrained by the independent I06 expectation; a stricter absent-registry policy (absent → UNKNOWN/BLOCK for support evidence) remains an alternative to be evaluated.
- I14 (PARTIAL support assertion-level narrowing) is an open semantic question (NEEDS_EXPERIMENT).
- Successor tested locally on Python 3.14 (Windows); language level identical to frozen (stdlib, `from __future__ import annotations`); independent portability verification (3.8/3.12) requested.

## Triggered follow-up obligations

```yaml
triggered_obligations:
  - obligation_id: "DSH-2026-08-21-OB-02"
    rule_ref: "ENA-CAP-065/066 + 08-RELEASE-DISCIPLINE (batching)"
    applicability: "APPLICABLE"
    materiality: "MATERIAL_TO_COMPLETION"
    status: "PENDING"
    required_before_claim: "any future 'V2.4 successor semantics remain valid under independent validation' claim"
    evidence_refs: ["research/prototypes/v2-machine-contract-hardening/v2.4/results-v24.json",
                    "research/prototypes/v2-machine-contract-hardening/v2.4/FREEZE-MANIFEST-V24.md"]
    resolution_reason: "Awaiting independent validation of the successor; V2.4 is a frozen research candidate only."
```

## Requested reconciliation

- `ACCEPT_AS_EVIDENCE` of the reconciliation (16 confirmed defects, I14 open) and the zero-unexpected successor replay.
- `INDEPENDENT_VALIDATION` of the frozen successor candidate (candidate author excluded by lineage).
- `NEEDS_PROJECT_DECISION` for the canonical typed-resolution direction (R1–R11).

## Authority / implementation note

- `advice only`. No release modification; no Mainline change; no promotion request. V2.4 lives only under `research/prototypes/`; `releases/current/` untouched; frozen candidate `8eb5a9a` untouched; no v0.2.12 / v0.3.3 created.

## Notes

Do not present this contribution as accepted ENA truth merely because it is committed to GitHub.

Preserve the original contribution even after reconciliation.
