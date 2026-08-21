# ENA v0.3.2 V2.2 Cumulative Contract Composition & Closure — DSH

Status: `UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED`
Baseline: `ENA v0.3.2` (releases/current/, FIELD_VALIDATION / NOT MAINLINE)
Composes: V2 (d178ff3) + V2.1 (2380056) protections
Date: 2026-08-20
Participant: DeepSeek Harness (DSH)

> Success is one portable cumulative machine-contract candidate whose protections remain valid when COMPOSED, not merely when tested in isolation. A discovered composition failure is valuable evidence.

## 0. What this round is

Not isolated fixes. One cumulative candidate validator that composes all accepted V2 and V2.1 protections into a single executable contract surface, then replays every historical fixture cumulatively (never reset). `releases/current/` untouched; no promotion.

## 1. Cumulative result

| Metric | Value |
|---|---|
| **TOTAL_ADVERSARIAL_BLOCKED** | **29 / 29** |
| ADVERSARIAL_UNKNOWN | 0 |
| ADVERSARIAL_LEAK | 0 |
| **TOTAL_POSITIVE_PRESERVED** | **14 / 19** |
| POSITIVE_UNKNOWN | 2 |
| POSITIVE_BLOCKED | 3 |

Fixture pool (never reset): V2=23 (6 original vectors + A6b + S1..S6 second-order + P1..P10 positive), V2.1=18 (A21-1..9 attacks + P21-1..7 positive), V2.2=7 (composition fixtures). TOTAL=48.

Portability: identical `29/29 + 14/19` on a fresh checkout (repo-relative; the V2 prototype's hardcoded absolute path is replaced by ancestor-based repo discovery).

## 2. Composition findings (valuable evidence, not hidden)

### F1 — V2 positives become BLOCKED under cumulative resolvability (cost of closure)
P1, P5, P6 were OK under V2's "trust raw ref strings" behavior. Under the cumulative contract's typed fail-closed resolution (no registry supplied → SUPPORT_REF_UNRESOLVABLE), they are BLOCKED.
**Interpretation**: this is the intended cost of "missing registries must not silently degrade into trusting raw strings", not a contract bug. Legitimate controls must also carry registries. The V2.1 positives (P21-*) demonstrate the correct pattern and are preserved.

### F2 — V2 positives become UNKNOWN (explicit, no silent label trust)
P7 (recovery) and P9 (independence) degrade to explicit UNKNOWN (PROVENANCE_REGISTRY_UNAVAILABLE / ROOT_REGISTRY_UNAVAILABLE) because the required registry is absent.
**Interpretation**: exactly the user requirement — provenance/root checks must NOT fall back to self-asserted labels when the registry is unavailable. They are neither wrongly blocked nor silently trusted.

### F3 — REAL composition regression found and fixed: S1 (SUPPORT_WITHOUT_EVIDENCE) was lost in composition
V2.1 blocked S1 (SUPPORTED → inline support with zero evidence) via SUPPORT_WITHOUT_EVIDENCE. In the first cumulative run this protection **leaked** (S1 passed OK) because the typed resolution layer checked resolvability+applicability but not "resolved support must carry evidence". This is a genuine composition failure: an individually valid V2.1 protection became invalid when composed. Fixed by adding the evidence check inside resolution. **This is the round's most important finding — all-green isolation does not imply all-green composition.**

### F4 — eval-time fixture defect (not a contract defect)
V22-A3's eval_time was in the wrong structure; once placed in payload, explicit eval-time correctly drives MANDATE_EXPIRED (eval 2026-08-22) while the identical mandate is OK at eval 2026-08-20 (V22-P3). No hardcoded development date.

### F5 — typed resolution + duplicate rejection work in composition
V22-A1 (support ref colliding with obligation id → SUPPORT_REF_UNRESOLVABLE), V22-A2 (duplicate obligation id → DUPLICATE_OBLIGATION_ID), V22-A4 (same-root via registry → HISTORY_EVIDENCE_SHARED_ROOT), V22-A5 (mirror roots → INDEPENDENCE_OVERCLAIMED) all blocked.

## 3. How the cumulative contract composes (calls actual implementations)

1. **Base v0.3.2** (`validate_contracts.py`, shipped): validate_support / validate_obligation / validate_recovery.
2. **V2** (`hardened_rules.py`, committed d178ff3): candidate_claim_supported_requires_refs, candidate_binding_authority_requires_mandate, candidate_verification_requires_grade, candidate_obligation_claim_link, candidate_recovery_history_requires_evidence, candidate_independence_requires_root.
3. **V2.1/V2.2 additions**: typed resolution (ref → correct artifact type, fail-closed on missing registry), grade enum E0..E5, mandate date+explicit eval-time, recovery root-derivation via registry (UNKNOWN if absent), independence origins via root registry (UNKNOWN if absent), duplicate-ID rejection, resolved-support-must-carry-evidence.

Explicit states: OK / BLOCK / UNKNOWN (BLOCK > UNKNOWN > OK). UNKNOWN is never silently upgraded to OK.

## 4. Cost

- Resolution layer: O(refs) per artifact; registries are an artifact surface (must exist and be maintained).
- No runtime change; validator/tooling only.
- New false-positive surface: LOW for enum/date/resolution (deterministic); MEDIUM for root/registry truth (self-declared without independent verifier; documented).

## 5. Honest limits

- Synthetic fixtures (all historical + new composition cases); single host/session/model; no production workload.
- Registry/root/grade/mandate content-truth still requires an independent verifier (CON-029/027).
- The 3 positive BLOCKs and 2 positive UNKNOWNs are real composition costs, reported not hidden.

## 6. Verdict

`CUMULATIVE_CONTRACT_CLOSES_29_29_ADVERSARIAL_WITH_5_DOCUMENTED_COMPOSITION_FINDINGS` (research; NOT_MAINLINE)

- 29/29 adversarial blocked, 0 leak, 0 unknown on adversarial.
- 14/19 positive preserved; 3 blocked + 2 unknown are explicit, documented composition costs (resolvability requirement + no silent registry trust).
- One real composition regression (S1) was found and fixed — evidence that isolation-green does not imply composition-green.
- Repo-relative, portable, calls actual implementations.

Files: `cumulative_contract.py`, `fixtures_v22.py`, `run_v22.py`, `results-v22.json` (this directory). `releases/current/` untouched.
