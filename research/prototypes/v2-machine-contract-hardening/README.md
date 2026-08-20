# ENA v0.3.2 V2 Machine-Contract Hardening Experiment — DSH

Status: `UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED`
Baseline: `ENA v0.3.2` (releases/current/, FIELD_VALIDATION / NOT MAINLINE)
Date: 2026-08-20
Participant: DeepSeek Harness (DSH)
Location: research-only surface (this directory). `releases/current/` untouched. No promotion proposed.

> Success is not "more validation rules." Success is the cheapest machine contract that refuses to endorse a material false claim while preserving viable agency.

## 0. Scope and guardrails

- Converted the six previously falsified false-claim vectors into reproducible adversarial fixtures with legitimate positive controls.
- Designed the **smallest** candidate machine-contract change per vector (research/prototype only).
- Re-ran all adversarial + positive fixtures under the hardened candidates.
- Attempted second-order bypasses of each proposed fix.
- Recorded per-candidate: blocked? preserved? new fields/rules? cost? new false-positive/confidence surface? protection beyond prose?
- Compared the 32 ENA-VAL rules from v0.2.11 against v0.3.2; flagged only those whose absence permits a material false claim. Did not restore rules by count.

## 1. Results summary

| Phase | Adversarial | Positive | Second-order |
|---|---|---|---|
| Baseline (shipped v0.3.2 toolchain) | 6/7 false claims **PASS** (A4 partially blocked only when obligation submitted standalone) | — | — |
| Hardened candidates | **7/7 blocked** | **10/10 preserved** | **6/6 blocked** |

Baseline detail (shipped toolchain): A1 KNOW ✅PASS, A2 VERIFIED ✅PASS, A3 AUTHORITY ✅PASS, A4 COMPLETED ⚠️(obligation-only catch; claim side PASS), A5 RECOVERED ✅PASS, A6 INDEPENDENT ✅PASS, A6b ✅PASS.

Hardened detail: every adversarial/second-order fixture produced its expected block code; every positive fixture produced no block.

## 2. Per-candidate ledger (smallest change; research-only)

### C1 — CLAIM_SUPPORTED_REQUIRES_REFS (vector I_KNOW)
- false claim blocked: **YES** (A1)
- legit preserved: **YES** (P1 supported-with-refs; P2 asserted-ok)
- new fields: **none** (uses existing `support_relation_refs`)
- new rules: 1 validator rule (status=SUPPORTED → non-empty refs)
- machine/runtime/tool cost: O(1) per claim; no runtime change
- new false-positive/confidence surface: LOW (resolved by S1 below)
- protection beyond prose: **YES** — prose already says supported needs support; now a machine rule enforces non-empty refs
- second-order: S1 (SUPPORTED ref → support relation with zero evidence) blocked by SUPPORT_WITHOUT_EVIDENCE (requires evidence_refs non-empty on support)

### C2 — VERIFIED_REQUIRES_GRADE (vector I_VERIFIED)
- false claim blocked: **YES** (A2 schema-PASS-log as verification)
- legit preserved: **YES** (P10 grade E2)
- new fields: `evidence_grade` on capability evidence entries (E0–E5)
- new rules: 1 validator rule (VERIFIED_* requires at least one ref with grade > E1)
- cost: schema field + validator; no runtime
- new false-positive surface: **MEDIUM** — grade is self-asserted; an attacker can claim E2 without proof (documented residual; grade truth needs an independent verifier, which is a separate authority problem)
- protection beyond prose: **PARTIAL** — blocks "static-structure PASS log as verification"; grade truth still self-declared
- second-order: S6 (grade E0 assertion only) blocked by VERIFIED_ONLY_STATIC_STRUCTURE_EVIDENCE

### C3 — AUTHORITY_REQUIRES_MANDATE (vector I_HAVE_AUTHORITY)
- false claim blocked: **YES** (A3 restore+credential→authority)
- legit preserved: **YES** (P3 real mandate+horizon; P4 empty envelope)
- new fields: `mandate.source`, `mandate.expires_at`
- new rules: 2 (source required when envelope non-empty; source not restore/clone/credential; horizon required)
- cost: schema field + validator; no runtime
- new false-positive surface: **MEDIUM** — mandate source is a string; "USER_EXPLICIT_GRANT" can be forged without verification (CON-029/027 residual; claimed issuer != verified issuer)
- protection beyond prose: **YES** — machine-izes "credential/restore != mandate"; stops the naive restore-authority claim
- second-order: S2 (source="RESTORED_STATE") blocked by AUTHORITY_MANDATE_SOURCE_NOT_AUTHORIZING

### C4 — OBLIGATION_CLAIM_LINK (vector I_COMPLETED)
- false claim blocked: **YES** (A4 completion without obligation refs; S3 open material obligation)
- legit preserved: **YES** (P5 satisfied+closure evidence; P6 non-material pending)
- new fields: `claim.required_obligation_refs`
- new rules: 1 validator rule resolving claim-side obligation linkage
- cost: schema field + validator; obligations must be resolvable
- new false-positive surface: **MEDIUM** — requires an obligations registry; unenumerated obligations still invisible (residual)
- protection beyond prose: **YES** — closes the claim-side hole (obligation→claim existed; claim→obligation did not)
- second-order: S3 (claim enumerates ref but obligation PENDING material) blocked by COMPLETION_WITH_OPEN_MATERIAL_OBLIGATION

### C5 — RECOVERY_HISTORY_EVIDENCE (vector I_RECOVERED)
- false claim blocked: **YES** (A5 PRESERVED self-asserted, no evidence/delta)
- legit preserved: **YES** (P7 distinct history evidence + delta captured; P8 state-only)
- new fields: **none** (uses existing `history_continuity` fields)
- new rules: 3 (evidence_refs non-empty for STATE_AND_HISTORY; post_checkpoint_occurrence_delta_captured == true; history evidence != state evidence)
- cost: validator-only; no schema change
- new false-positive surface: **LOW-MEDIUM** — distinct-ref is a heuristic; attacker can name two different fabricated logs (content truth unverifiable)
- protection beyond prose: **YES** — "PRESERVED" status word alone no longer suffices; requires delta capture + distinct history evidence
- second-order: S4 (history evidence == state evidence) blocked by HISTORY_EVIDENCE_SAME_AS_STATE_EVIDENCE

### C6 — INDEPENDENCE_ROOT (vector EVIDENCE_INDEPENDENT)
- false claim blocked: **YES** (A6 laundering without roots; A6b one root; S5 count>roots)
- legit preserved: **YES** (P9 two distinct roots)
- new fields: `independence_basis.root_provenance`
- new rules: 2 (roots required when count claimed; claimed_count <= distinct roots)
- cost: schema field + validator
- new false-positive surface: **MEDIUM** — root_provenance is self-declared; attacker can declare fake distinct roots (laundering moves one level down; residual)
- protection beyond prose: **YES** — stops label-string laundering; shifts trust boundary to root identity
- second-order: S5 blocked by INDEPENDENCE_OVERCLAIMED

## 3. ENA-VAL 32-rule absence analysis (v0.2.11 → v0.3.2)

Only **5 of 32** ENA-VAL rules have absences that permit a **material** false claim in v0.3.2's narrower contract surface:

| Rule | Material gap | Relationship to candidates |
|---|---|---|
| ENA-VAL-013 | SUSPENDED work claiming completion (I_COMPLETED shape) | partial: C4 covers via obligations, not activation-state |
| ENA-VAL-019 | composition change inheriting component PASS (I_VERIFIED shape) | C2 covers grade dimension only; composition inheritance needs its own check |
| ENA-VAL-022..025 | COMPLETE_HARD_MECHANICAL claimed without effect-surface completeness (I_VERIFIED/I_HAVE_AUTHORITY) | v0.3.2 5.5 prose; no machine rule |
| ENA-VAL-028 | non-active mechanism claiming current protection | v0.3.2 lacks active/dormant status on mechanisms |
| ENA-VAL-030/031 | destructive history transform claiming preserved truth (k-0083 shape, I_RECOVERED) | C5 partially covers recovery claims; not general history-transform artifacts |

All other 27 rules: their absence does **not** directly permit one of the six material false-claim vectors (they are governance-profile/mutation/elevation/activation-specific; v0.3.2 covers the relevant semantics in prose or they are not material to these vectors). **Do not restore by count.** These five are candidates to reconsider only if/when the corresponding artifact classes (activation state, composition records, enforcement-surface records, mechanism status, history-transform records) are machine-represented in a future v0.3.x.

## 4. Honest limits

- All attacks are synthetic but constructed from the release's own schema field sets and run against the real shipped toolchain (baseline) and a research-only hardened prototype.
- Self-declared fields (evidence_grade, mandate.source, root_provenance, closure evidence) remain self-declared: the hardening blocks the *structural* false claim but cannot verify *content truth* without an independent authority — that is a separate, pre-existing limitation (CON-029/027, "claimed issuer != verified issuer").
- Single host, single model binding, single session. No production workload.
- The hardened prototype is research-only; nothing here is a v0.3.2 change or a promotion request.

## 5. Verdict

`PROTOTYPE_HARDENING_BLOCKS_ALL_SIX_FALSE_CLAIMS_AT_STRUCTURAL_LEVEL` (research verdict; NOT_MAINLINE)

- Adversarial 7/7 blocked, positive 10/10 preserved, second-order 6/6 blocked.
- Each candidate is the smallest change found that blocks the false claim without rejecting the legitimate control.
- New false-positive/confidence surfaces are documented per candidate; the dominant residual is self-declared truth of content-bearing fields, which no schema/validator can fix without an independent verifier.
- 5/32 ENA-VAL absences are material; 27/32 are not, and were deliberately not restored by count.

> Cheapest machine contract that refuses to endorse a material false claim while preserving viable agency — not more rules.

Files: `hardened_rules.py` (candidates), `fixtures.py` (adversarial/positive/second-order), `run_experiment.py` (phases 1-4), `val_gap_analysis.py` (ENA-VAL comparison), `results.json` (machine-readable output).
