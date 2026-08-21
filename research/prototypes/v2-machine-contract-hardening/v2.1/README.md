# ENA v0.3.2 V2.1 Second-Order Adversarial Expansion — DSH

Status: `UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED`
Baseline: `ENA v0.3.2` (releases/current/, FIELD_VALIDATION / NOT MAINLINE)
Attacks target: V2 hardening prototype (commit `d178ff3`)
Date: 2026-08-20
Participant: DeepSeek Harness (DSH)

> Success is not "all tests green" or "more validator rules."
> Success is the smallest portable machine contract that refuses to endorse a material false claim, resolves its referenced evidence/obligations/authority/provenance correctly, and preserves legitimate agency with acceptable cost.

## 0. Purpose

The V2 result (adversarial 7/7, positive 10/10, second-order 6/6) is useful evidence but **not sufficient for implementation acceptance**: it only proved the first layer of structural checks. This round attacks the V2 prototype itself on the unresolved structural cases the user enumerated, tries to bypass the V2 fixes, and adds the minimal portable resolution/validation layer. `releases/current/` untouched; no promotion.

## 1. Results

| Phase | ATTACK blocked | POSITIVE preserved |
|---|---|---|
| Committed V2 prototype (d178ff3) | **0/11** (all structural attacks VULNERABLE) | — |
| V2.1 additions applied | **11/11** | **7/7** |
| Portability (fresh checkout) | 11/11 (identical) | 7/7 (identical) |

**The committed V2 prototype leaks all 11 second-order structural attacks.** This is the honest finding the user predicted: the V2 "all-green" result was green only against first-layer attacks.

## 2. Per-attack ledger

| # | Attack | V2 (committed) | V2.1 block code | Smallest addition | Real protection or trust-boundary move? |
|---|---|---|---|---|---|
| A21-1 | SUPPORTED → nonexistent support ref | **LEAK** | SUPPORT_REF_UNRESOLVABLE | registry + ref resolution | REAL: refs must resolve |
| A21-2 | completion → nonexistent obligation ref | **LEAK** | OBLIGATION_REF_UNRESOLVABLE | registry + claim-side resolution | REAL: closes ref hole |
| A21-3 | VERIFIED grade='GARBAGE' | **LEAK** | EVIDENCE_GRADE_INVALID | grade enum E0..E5 | REAL: malformed grade rejected |
| A21-3b | VERIFIED grade='E9' | **LEAK** | EVIDENCE_GRADE_INVALID | grade enum range check | REAL: out-of-range rejected |
| A21-4 | mandate expires_at past | **LEAK** | MANDATE_EXPIRED | date parse + currency check | REAL: expired mandate rejected |
| A21-4b | mandate expires_at='not-a-date' | **LEAK** | MANDATE_DATE_UNPARSEABLE | date parse | REAL: malformed rejected |
| A21-5 | recovery distinct refs, same root | **LEAK** | HISTORY_EVIDENCE_SHARED_ROOT | root-provenance derivation check | PARTIAL: blocks known derivation; unknown derivation still invisible (trust boundary moves to root registry) |
| A21-6 | independence fabricated roots | **LEAK** | INDEPENDENCE_OVERCLAIMED | root registry maps roots→actual origins | PARTIAL: laundering moves to root-registry truth (needs independent root attestation) |
| A21-7 | no registry supplied at all | **LEAK** | SUPPORT_REF_UNRESOLVABLE | fail-closed when registry absent | REAL: silence is no longer acceptance |
| A21-8 | duplicate support_id, contradictory statuses | **LEAK** | DUPLICATE_REF_ID | ID uniqueness check | REAL: ambiguity rejected |
| A21-9 | resolved support, incompatible applicability (H1 vs H2) | **LEAK** | TRANSFER_EVIDENCE_REQUIRED | applicability check on resolved artifact | REAL: base validate_support semantics preserved through resolution |

## 3. Positive controls preserved (7/7)

P21-1 supported-resolvable; P21-2 completion-resolvable (obligation satisfied + closure evidence); P21-3 grade E2; P21-4 mandate current; P21-5 recovery distinct roots; P21-6 independence real roots; P21-7 completion non-material pending (must NOT block).

## 4. V2.1 additions (minimal)

1. **Registry + resolution layer** (fail-closed when absent): support/obligation refs must resolve; duplicate IDs with contradictory statuses rejected; applicability checked on resolved artifacts.
2. **Grade enum** `E0..E5`: VERIFIED requires valid grade; out-of-range/malformed rejected (fixes the `all(g in ("E0","E1"))` hole where garbage passed).
3. **Date parsing + currency** for mandate `expires_at`: unparseable and past dates rejected (fixes the non-empty-only check).
4. **Root-derivation check** for recovery history evidence: distinct ref strings sharing a root rejected (fixes the string-compare hole).
5. **Root registry** for independence: roots map to actual origins; count origins not labels (laundering moved one level deeper — now requires registry truth).

## 5. Cost and new false-positive/confidence surfaces

- Cost: schema additions (registry is an artifact surface, not runtime); validator-only where possible; O(1)-O(n) per artifact. No runtime change.
- New false-positive surface: LOW for enum/date/resolution (deterministic). MEDIUM for root-derivation and root-registry: both now depend on registry truth, which without an independent verifier is itself self-declared — the trust boundary moved from "label strings" to "registry entries"; it did not disappear. Documented, not hidden.
- Governance cost: a registry must exist and be maintained (artifact lifecycle); this is the price of resolvability.

## 6. ENA-VAL summary correction (v2.1 formulation)

Previous V2 report said "5/32". Corrected formulation:

> **5 material gap families involving 9 ENA-VAL rule IDs: 013, 019, 022–025, 028, 030–031.**

- Family 1: `ENA-VAL-013` — SUSPENDED work claiming completion (I_COMPLETED shape)
- Family 2: `ENA-VAL-019` — composition change inheriting component PASS (I_VERIFIED shape)
- Family 3: `ENA-VAL-022..025` — COMPLETE_HARD_MECHANICAL without effect-surface completeness (I_VERIFIED / I_HAVE_AUTHORITY)
- Family 4: `ENA-VAL-028` — non-active mechanism claiming current protection
- Family 5: `ENA-VAL-030..031` — destructive history transform claiming preserved truth (k-0083 shape, I_RECOVERED)

Do **not** restore these rules by count. Treat them only as **candidate historical protections whose present value must be demonstrated** on real artifact classes before reintroduction. The other 23 rule IDs' absence does not directly permit one of the six material false-claim vectors.

## 7. Honest limits

- Attacks are synthetic but constructed from the release's own schema field sets and run against the real shipped toolchain (baseline) and the committed V2 prototype.
- Content-truth of registry entries (root provenance, grade truth, mandate source) remains self-declared without an independent verifier (CON-029/027, "claimed issuer != verified issuer") — a pre-existing authority limitation, now made explicit at the registry layer.
- Single host, single model binding, single session. No production workload.

## 8. Verdict

`V2_1_CLOSES_ALL_ELEVEN_STRUCTURAL_LEAKS_AT_STRUCTURAL_LEVEL` (research verdict; NOT_MAINLINE)

- The committed V2 prototype was honestly attacked and shown to leak 11/11 second-order structural cases.
- The minimal V2.1 additions block 11/11 while preserving 7/7 legitimate controls, and are repo-relative portable (identical results on a fresh checkout).
- Residual trust boundary: registry/root/grade/mandate truth still requires an independent verifier; the hardening makes the boundary explicit rather than invisible.

Files: `fixtures_v21.py`, `run_v21.py`, `results-v21.json` (this directory). `releases/current/` untouched.
