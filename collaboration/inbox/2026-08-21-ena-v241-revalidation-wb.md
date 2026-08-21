# ENA V2.4.1 — Targeted Revalidation by Prior F1 Falsifier

**Provenance:** `REVALIDATION_BY_PRIOR_FALSIFIER`
**Scope:** Closed-scope, targeted, *not* a new blind independent-validation round, *not* an open-ended adversarial expansion.
**Author of this report:** WorkBuddy (independent validator; prior contribution = PR #30, V2.4 validation, which discovered **F1**).
**Date:** 2026-08-21

---

## 0. Subject and intent

The candidate author produced a **narrowly scoped, frozen** successor (`daacab1`) intended only to:

- **Close F1** — dict-key vs explicit inner-id registry identity ambiguity (the residual I discovered during V2.4 validation). The fix is **R12**: ONE consistent identity rule — the dict key is authoritative; an explicit inner id (`support_id` / `obligation_id` / `evidence_id` / `root_id` / `grant_id`) must equal the dict key, else `REGISTRY_MALFORMED`; a missing inner id is backfilled from the key. Applied uniformly to **all six** registry kinds and to `support_registry`/`support_relations` via `_support_sources`.
- **Defensively close F2** — a schema-valid-input precondition gate: any obligation status outside the shipped vocabulary → `BLOCK OBLIGATION_STATUS_OUTSIDE_VOCABULARY`. **Vocabulary NOT expanded.**

Frozen references:

| Artifact | Ref |
|---|---|
| V2.4.1 successor code (frozen) | `daacab1f042c38f3856ef4d0366febd1b5e47600` |
| Freeze record | `b3d16988b65ea189b7ee82fd4b665bdb8bbb1f84` |
| Prior V2.4 candidate (untouched) | `47e0e1b121b1ef1e8911c59980c99805ded5a963` |
| Prior V2.4 freeze (untouched) | `5f5dfca99a87812c35d4c07fd409bf6a8dc1d609` |
| This report branch | `wb-revalidation-v241` (based on `origin/main` `260b804`) |

**Candidate maturity / promotion status (preserved):** `UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED`. The V2.4.1 artifacts remain under `research/prototypes/v2-machine-contract-hardening/v2.4.1/`; `releases/current/` was **not** modified; and no Host promotion/adoption decision has occurred. This status is **unchanged by the GitHub `main` merge of PR #31** — see §7 for the distinction between the git default branch and the ENA semantic Mainline.

**Intent of this revalidation:** confirm that the previously discovered **F1** residual (and the defensive **F2** gate) is *genuinely closed* on the frozen commit — nothing more. It does **not** re-attest the entire V2.4 corpus as a fresh blind validation.

---

## 1. Phase A — Frozen identity & digest verification

**Method.** For each file listed in `FREEZE-MANIFEST-V241.md`, I computed SHA-256 over the `git show daacab1:<path>` blob content (LF-normalized, autocrlf-independent) and compared to the manifest's declared digest. I also enumerated the full `v2.4.1/` file set at `daacab1` to confirm the candidate contains *exactly* the frozen files, and confirmed the prior V2.4 candidate/freeze and `releases/current/` are untouched.

**Result — all 8 declared digests MATCH:**

| File | Declared SHA-256 | Match |
|---|---|---|
| `successor_contract_v241.py` | `1390112d…496566a` | ✅ |
| `acceptance_semantics_v241.py` | `b7735289…bfd8689` | ✅ |
| `wb_fixtures.py` | `71c972a6…0e25bf8` | ✅ |
| `f1_controls.py` | `b821293e…290298` | ✅ |
| `run_v241.py` | `1fa74a1f…ed9541f9` | ✅ |
| `reproduce_f1.py` | `dfa4ab04…54a57c8e` | ✅ |
| `reproduction-f1.json` | `b73a8d74…ff9ef699` | ✅ |
| `results-v241.json` | `d1e83e25…989e09b` | ✅ |

**Identity checks:**
- Candidate files = exactly those frozen: 9 files in `v2.4.1/` at `daacab1` (the 8 manifest files + `freeze_hashes_v241.py`, which is a helper and is *not* covered by the digest table — see §5).
- Prior V2.4 candidate `47e0e1b` and freeze `5f5dfca` are **untouched** (separate commits, not modified).
- `releases/current/` is **untouched** (research-only by design).

**Verdict:** Frozen identity verified; all hashes verified. ✅

---

## 2. Phase B — F1 direct revalidation (re-run the original falsifier)

**Method.** I loaded **both** the frozen V2.4 successor (`47e0e1b`) and the V2.4.1 successor (`daacab1`) as independent modules and re-ran the *same* F1 family that originally falsified V2.4 — for every registry kind, with the dict key ≠ the explicit inner id, in **both** directions (reference declared inner id; reference dict key).

**F1 reproduced on old V2.4 (silent failure):**

| Case | V2.4 verdict | V2.4.1 verdict |
|---|---|---|
| `IND-02E` evidence (E1≠E2, ref E2) | `EVIDENCE_REF_UNRESOLVABLE` (false BLOCK) | `REGISTRY_MALFORMED` (BLOCK) |
| `IND-02E-rev` (ref E1 resolves artifact declaring E2) | `OK` (identity confusion) | `REGISTRY_MALFORMED` (BLOCK) |
| `IND-02O` obligation (O1≠O2) | `OBLIGATION_REF_UNRESOLVABLE` | `REGISTRY_MALFORMED` |
| `IND-02R` root (R1≠R2) | `ROOT_REF_UNRESOLVABLE` | `REGISTRY_MALFORMED` |
| `IND-02A` authority (G1≠G2) | `AUTHORITY_MANDATE_SOURCE_NOT_AUTHORIZING` | `REGISTRY_MALFORMED` |
| `IND-02S` support (S1≠S9) | `SUPPORT_REF_UNRESOLVABLE` | `REGISTRY_MALFORMED` |
| `IND-02SR` support_relations (S1≠S9) | `SUPPORT_REF_UNRESOLVABLE` | `REGISTRY_MALFORMED` |

**F1 closed on V2.4.1:** every divergence → `REGISTRY_MALFORMED` (explicit, never silent). All six registry kinds, both directions. ✅

**Legitimate representations preserved on V2.4.1 (no false `REGISTRY_MALFORMED`):**

| Control | V2.4.1 verdict | Preserved |
|---|---|---|
| `L1` key == id | `OK` | ✅ |
| `L2` missing inner id (backfill) | `OK` | ✅ |
| `L3` valid list-form | `OK` | ✅ |
| `L4` duplicate/ambiguous id | `DUPLICATE_REF_ID` → BLOCK (existing protection, *not* `REGISTRY_MALFORMED`) | ✅ |
| `L5` obligation key == id | `OK` | ✅ |

**Verdict:** F1 reproduced on V2.4; F1 closed on V2.4.1; identity confusion eliminated; legitimate representations preserved. **OVERALL: PASS.** ✅

---

## 3. Phase C — F2 narrow revalidation (obligation status vocabulary gate)

**Vocabulary:** `{PENDING, SATISFIED, NOT_REQUIRED, DEFERRED_AUTHORIZED, FAILED, UNKNOWN}`.

**Outside-vocabulary rejected (F2 closed):**

| Case | V2.4.1 | V2.4 (gap reproduced) |
|---|---|---|
| `F2-OPEN` status=`OPEN` | `BLOCK OBLIGATION_STATUS_OUTSIDE_VOCABULARY` | `OK` (accepted) |
| `F2-GARBAGE` status=`GARBAGE` | `BLOCK OBLIGATION_STATUS_OUTSIDE_VOCABULARY` | `OK` (accepted) |

**In-vocabulary values NOT blocked by the gate (gate is defense-in-depth, not a new vocabulary):**

| Case | V2.4 | V2.4.1 |
|---|---|---|
| `F2-PENDING` | `BLOCK MATERIAL_OBLIGATION_BLOCKS_CLAIM` | same |
| `F2-SATISFIED` | `OK` | `OK` |
| `F2-FAILED` | `BLOCK MATERIAL_OBLIGATION_BLOCKS_CLAIM` | same |
| `F2-UNKNOWN` | `BLOCK MATERIAL_OBLIGATION_BLOCKS_CLAIM` | same |
| `F2-NOT_REQ` (`NOT_REQUIRED`) | `BLOCK CLOSURE_STATUS_REQUIRES_REASON` | `BLOCK CLOSURE_STATUS_REQUIRES_REASON` |
| `F2-DEFERRED` (`DEFERRED_AUTHORIZED`) | `BLOCK CLOSURE_STATUS_REQUIRES_REASON` | `BLOCK CLOSURE_STATUS_REQUIRES_REASON` |

**Critical check:** `NOT_REQUIRED` and `DEFERRED_AUTHORIZED` return `CLOSURE_STATUS_REQUIRES_REASON` on **both** versions — proving the *new* vocabulary gate is **NOT** what blocks them (it is the pre-existing baseline `resolution_reason` requirement). The gate does **not** accidentally treat these legitimate statuses as blocking. ✅

**Claim-aware narrow completion (I07) intact on V2.4.1:** `SATISFIED` bound → `OK`; `FAILED` bound → `BLOCK` via `MATERIAL_OBLIGATION_BLOCKS_CLAIM` (existing semantics, *not* the vocab gate). Orphan `OPEN` obligation → `OBLIGATION_STATUS_OUTSIDE_VOCABULARY`.

**Verdict:** F2 outside-vocabulary rejected; legitimate obligation statuses preserved; no false blocking introduced. **OVERALL: PASS.** ✅

---

## 4. Phase D — Accumulated-corpus replay (executed independently)

**Method.** I did **not** trust the committed `results-v241.json`. I extracted the complete frozen tree at `daacab1` via git objects (`git ls-tree -r` + `git show` per blob — **no working-tree checkout of the frozen commit, no mutation of the branch**) into a throwaway temp dir, then executed the candidate's own replay against that extracted frozen implementation:

```
python <tmp>/research/prototypes/v2-machine-contract-hardening/v2.4.1/run_v241.py
```

The replay re-derives every verdict from the frozen `successor_contract_v241.py` over the frozen corpus (fixtures from all `v2.x` dirs + `wb_fixtures` + `f1_controls`). This is fully reproducible via `collaboration/inbox/v241-harness/phaseD_replay.py`.

**Result:**

| Corpus | Count | Matched |
|---|---|---|
| `FROZEN_V24` | 98 | **98/98** |
| `WB_PROBE` | 25 | **25/25** |
| `F1_CONTROL` | 25 | **25/25** |
| **TOTAL** | **148** | — |

- `UNEXPECTED_VERDICTS`: **0**
- `exceptions`: **0** · `evaluator_fault`: **0**
- Frozen V2.4 verdict preservation (successor actual vs `results-v24.json` expected): **98/98** (zero flips)
- WB probe oracle consistency (oracle expected vs reconciled `wb_expect`): **25/25**
- Expected vs actual verdict counts identical: **`BLOCK 82 / OK 60 / UNKNOWN 6`**

**Independent verification of the committed artifact:** my freshly generated `results-v241.json` is **semantically identical** to the committed blob (deep JSON equality = `True`). The earlier raw-byte SHA-256 mismatch was a git content-normalization artifact (raw disk bytes vs git's canonical form) — `git diff HEAD` is empty and `git hash-object` of the earlier in-tree output equals the committed blob SHA-1 (`eb502fef`). No prior false-confidence protection was reopened.

**Verdict:** 148 replay reproduced exactly; 0 unexpected; no regression. ✅

---

## 5. Freeze / metadata discrepancies noted (all non-semantic, non-integrity)

1. **Manifest `"(private)"` is stale.** `FREEZE-MANIFEST-V241.md` line 19 describes the repo as private; it is now public. This is non-semantic — all digests are content-addressed and reproduced, so reproducibility/identity are unaffected.
2. **`freeze_hashes_v241.py` is undigested.** It exists in the `daacab1` `v2.4.1/` dir but is not covered by the manifest digest table (minor manifest-completeness gap; it is a helper, not a contracted artifact — no integrity impact).
3. **`run_v241.py` docstring is stale (149 / 26).** The script header states `TOTAL = 149` and `WB = 26`, but the *actual* computed counts are **148** and **25**. The committed `results-v241.json` and the `daacab1` commit message both state **148 / 25**. Resolved: the real corpus is **148 = 98 frozen + 25 WB + 25 F1 controls**; the docstring numbers are a leftover error, not a substantive discrepancy.

---

## 6. Required conclusion checklist

| # | Item | Result |
|---|---|---|
| 1 | Frozen identity verified? | ✅ (Phase A) |
| 2 | Hashes verified? | ✅ (8/8 SHA-256) |
| 3 | F1 reproduced on old V2.4? | ✅ (silent false BLOCK / identity confusion) |
| 4 | F1 closed on V2.4.1? | ✅ (`REGISTRY_MALFORMED`, all 6 kinds, both directions) |
| 5 | Identity confusion eliminated? | ✅ |
| 6 | Legitimate key==id controls preserved? | ✅ |
| 7 | Backfill preserved? | ✅ |
| 8 | F2 outside-vocabulary rejected? | ✅ (`OBLIGATION_STATUS_OUTSIDE_VOCABULARY`) |
| 9 | Legitimate obligation statuses preserved? | ✅ (`NOT_REQUIRED`/`DEFERRED_AUTHORIZED` not blocked by gate; I07 intact) |
| 10 | 98 frozen preserved? | ✅ (98/98, zero flips) |
| 11 | Original WB probes preserved? | ✅ (25/25) |
| 12 | 148 replay reproduced? | ✅ (semantically identical; 0 unexpected) |
| 13 | Any directly caused regression? | ❌ none |
| 14 | Freeze metadata discrepancies? | ⚠️ 3 minor notes (§5), all non-semantic / non-integrity |

---

## 7. Status note — git default branch `main` vs ENA semantic Mainline (transparency)

**Two distinct concepts must not be conflated:**

- **Git repository default branch (`main`)** — a git-tree concept. PR #31 (head `daacab1`) being *merged into GitHub `main`* is merely a code-merge event on the repository's default branch.
- **ENA semantic Mainline / promotion state** — the candidate's maturity in the agent-architecture sense (whether it has been promoted into `releases/current/` and adopted by a Host). **This is unchanged.**

**Corroboration:** the `daacab1` commit message itself records the status as *"research-only, releases/current untouched, UNRECONCILED/NOT_MAINLINE/NOT_PROMOTED"*. The V2.4.1 artifacts remain under `research/prototypes/v2-machine-contract-hardening/v2.4.1/`; `releases/current/` was **not** modified; and no Host promotion/adoption decision has occurred.

**Therefore the candidate status remains exactly:**

> `UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED`

**The GitHub `main` merge of PR #31 does NOT make `NOT_PROMOTED` outdated.** A research contribution landing on the git default branch is not an ENA promotion. I do **not** treat the merge as a promotion, and I do **not** retroactively mark the candidate as promoted/mainline.

(Separately, `git branch -r --contains daacab1` is empty and `origin/main` (`260b804`) does not contain the `v2.4.1` artifacts — i.e. the code-merge is not even reflected in the current `main` tree. This is orthogonal to the point above: whether or not the merge reaches the `main` tree, the ENA promotion state is unchanged.)

This report targets the **exact frozen commit `daacab1` by SHA** (content-addressed, fully reproducible) and is **independent of its merge status**. I did **not** perform, rely on, or alter that merge. Per the original brief, I do **not** modify the frozen candidate or `releases/current/`, and I do **not** promote it; this is an additive revalidation contribution.

---

## 8. Final verdict

> ## `REVALIDATION_BY_PRIOR_FALSIFIER_SUPPORTED`

The previously discovered **F1** residual (dict-key vs inner-id registry identity ambiguity) is **genuinely closed** on the frozen V2.4.1 successor `daacab1`: the original falsifier family now yields an explicit `REGISTRY_MALFORMED` (never a silent false BLOCK or identity confusion) across all six registry kinds and both reference directions, while all legitimate representations (key==id, backfill, list-form, duplicate/ambiguity protection, obligation key==id) remain `OK`. The defensive **F2** vocabulary gate is correctly scoped (outside-vocabulary rejected; in-vocabulary, including `NOT_REQUIRED`/`DEFERRED_AUTHORIZED`, not falsely blocked; claim-aware I07 intact). The 148-fixture accumulated corpus replays with **0 unexpected verdicts** and **zero flips** versus the frozen V2.4 baseline; my independent execution reproduces the committed `results-v241.json` exactly.

**This verdict verifies closure of the previously discovered residual — it is explicitly NOT a new blind independent-validation claim over the entire V2.4 corpus.** Minor, non-semantic metadata discrepancies (§5) do not affect the closure conclusion.

**Candidate status preserved:** this revalidation does **not** change the candidate's maturity. It remains `UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED` (see §7) — the GitHub `main` merge of PR #31 is a code-merge event, not an ENA promotion.

---

## Appendix — Harness artifacts (this report branch)

- `collaboration/inbox/v241-harness/verify_digests.py` — Phase A digest verification (git-object based, runs from any checkout).
- `collaboration/inbox/v241-harness/phaseB_revalidate.py` — Phase B F1 revalidation (loads V2.4 + V2.4.1 successors from git objects).
- `collaboration/inbox/v241-harness/phaseC_revalidate.py` — Phase C F2 revalidation (loads V2.4 + V2.4.1 successors from git objects).
- `collaboration/inbox/v241-harness/phaseD_replay.py` — Phase D independent 148-fixture replay reproduction (extracts the full frozen tree at `daacab1` via git objects, runs `run_v241.py`, compares the regenerated `results-v241.json` to the committed blob).
- `collaboration/inbox/v241-harness/README.md` — how to run.

**All four harnesses were executed this session and PASS:** Phase A (8/8 digests match), Phase B (`OVERALL: PASS`), Phase C (`PHASE C RESULT: PASS`), Phase D (`PHASE D RESULT: PASS`; 148 fixtures, 0 unexpected, semantic identity to committed blob).

All harnesses are self-contained: they extract the exact frozen modules via `git show <ref>:<path>` and re-exercise the falsifier family independently of the author's `f1_controls.py` / `results-v241.json`.
