# Targeted Revalidation — ENA v0.3.3-candidate.1 (by Prior Implementation Falsifier)

**Provenance:** `REVALIDATION_BY_PRIOR_IMPLEMENTATION_FALSIFIER`
**Session:** same WorkBuddy session that produced fresh independent validation PR #38 (verdict `INDEPENDENT_IMPLEMENTATION_VALIDATION_NEEDS_REVISION`).
**Subject under revalidation:** `releases/v0.3.3-candidate.1/` @ `034b7895997dd0599a0bfea10de7acfac575f232` (immutable semantic successor).
**Prior PR (this validator):** #38 (closed D1/D2/D3 as falsifier findings).

> This is NOT a new blind independent-validation round. It re-runs THIS validator's original D1/D2/D3 falsifiers against the old and new candidates to determine whether the author's successor genuinely closes the three findings and introduces no directly-caused local regression.

---

## 1. Validator / environment

- Validator/provider/model: WorkBuddy (Hy3), fresh independent implementation validator session.
- Host OS: win32; shell: bash (Git Bash).
- Local validation workspace: `C:\Users\PC\WorkBuddy\ena-validation\repo` (fresh clone, fetched to latest).
- Working tree state: local HEAD is in a sandbox-induced orphan state from the prior session; **all validation performed via git object plumbing (`git show <ref>:<path>`)**, which is authoritative and unaffected. No conclusion depends on the checked-out tree.
- Python (managed, actually executed): **3.13.14** (used for every probe, selftest, and suite run).
- Reused artifacts: my own PR #38 probe harness definitions (`my-probes/probe_harness.py`, `probe_results.json`) — the original D1/D2/D3 falsifier payloads, NOT the author's repackaged `pr38_fixtures.py` / `d1d2d3_controls.py`.

## 2. Execution gate (actual evidence)

```
pwd        = /c/Users/PC/WorkBuddy/ena-validation/repo
git status = working tree in orphan state (read-only validation via plumbing; not used for conclusions)
HEAD       = (orphan; refs resolved explicitly below)
refs:
  f7dc6202dacd30e1f19d023146ecaeb4f020c922 -> resolved (old falsified candidate)
  034b7895997dd0599a0bfea10de7acfac575f232 -> resolved (new successor semantic candidate)
  fbefa9a77d9618ba98153291295588222c2cc78d -> resolved (freeze record)
  c1d29f63f351298a6752b22ff028de189c56789f -> resolved (PR #38 merge)
python     = Python 3.13.14
old impl   = releases/v0.3.3-candidate/tools/validate_contracts.py  (blob present)
new impl   = releases/v0.3.3-candidate.1/tools/validate_contracts.py (blob present)
```
All four required refs resolve; both candidate implementations are present in the object database. Gate satisfied.

## 3. Phase A — successor identity, freeze, hash, CI

- **Freeze record is a child of the semantic candidate:** `git diff --stat 034b789..fbefa9a` adds **only** `releases/v0.3.3-candidate.1/FREEZE-MANIFEST.md` (177 insertions, 0 deletions). No semantic file changed between the completed candidate and the freeze record → freeze record contains no untested semantic modification.
- **Freeze manifest location:** the manifest lives only at `fbefa9a` (not at `034b789`); the semantic candidate already contained the candidate workflow (`candidate-gate-v033c1.yml` present at `034b789`, confirmed) before freeze → correct freeze ordering.
- **Independent hash recomputation:** recomputed all **14** SHA-256 digests declared in `FREEZE-MANIFEST.md §12` over committed blobs at `034b789`. **All 14 MATCH** (CANDIDATE-BASELINE, README, CHANGELOG, 05-CORE-OPERATIONAL-CONTRACTS, composed-case schema, validate_contracts.py = `b97aef42…`, contract-fixtures.v2 = `9ab7400c…` (byte-identical to old v2), contract-fixtures.v2.1 = `31a30944…`, regression_suite.py, regression-results, build scripts, pr38_fixtures.py, d1d2d3_controls.py, candidate-gate-v033c1.yml). Manifest hashes accepted only after independent verification.
- **Old candidate unchanged:** old `validate_contracts.py` SHA-256 = `78c3ddeb1952826e90dadd1594afa3ae7690915de7127557bb68a04799a14e8c` — **identical to the digest recorded in PR #38**. The frozen original candidate is byte-for-byte unchanged.
- **`releases/current/` untouched:** the successor package is a flat new tree at `releases/v0.3.3-candidate.1/`; `034b789` introduces no path under `releases/current/` (v0.3.2 retained). Confirmed the new candidate ref does not modify `releases/current/`.
- **Exact-candidate CI run verified via GitHub API:**
  - Run **32486325485** → `conclusion=success`, `head_sha=034b7895997dd0599a0bfea10de7acfac575f232`, name "Candidate Gate (v0.3.3-candidate.1)". Jobs: validation surface on **Python 3.8 / 3.12 / 3.13** all `success`. The exact immutable candidate ref was tested before freeze.
  - Run **32486881934** → `conclusion=success`, `head_sha=fbefa9a…` (freeze record), recorded separately. Both gates SUCCESS; the later run does not substitute for proof that the exact candidate ref was tested (it was, by 32486325485).

## 4. Phase B — reproduce D1/D2/D3 on OLD candidate (f7dc620)

Re-ran my original falsifiers against the OLD implementation; all three reproduced (`OLD_DEFECT_REPRODUCED`):

| Probe | Property | Old actual | Expected | Reproduced? |
|---|---|---|---|---|
| P42 (D1) | non-completion `FACT` claim + bound `MATERIAL/PENDING` obligation (`required_before_claim_refs:[c1]`, trigger observed) | `OK/OK` | `BLOCK` | **YES — material false OK** |
| P10 (D2) | top-level `support` dict without id | `BLOCK/REGISTRY_MALFORMED` | `OK` | **YES — false BLOCK** |
| P16 (D3) | coherent `root_provenance`, root registry absent | `BLOCK/INDEPENDENCE_OVERCLAIMED` | `UNKNOWN/ROOT_REGISTRY_UNAVAILABLE` | **YES — false BLOCK** |
| P17 (D3) | `root_provenance` + registered distinct origins | `BLOCK/INDEPENDENCE_OVERCLAIMED` | `OK` | **YES — false BLOCK** |

The old candidate's `check_obligation_path` early-returned for non-completion claims (D1), its `_support_sources` rejected id-less direct support (D2), and `check_independence`/`validate_support` over-blocked `root_provenance`-backed independence via the legacy `source_origins` check (D3).

## 5. Phase C/D/E — D1/D2/D3 closure on NEW candidate (034b789)

Ran the same P42/P10/P16/P17 plus extended directly-affected controls against the new implementation. **All close correctly:**

**D1 (obligation gating, non-completion claims):**
- D1-A bound `MATERIAL/PENDING` → `BLOCK/MATERIAL_OBLIGATION_BLOCKS_CLAIM` ✓
- D1-B bound `MATERIAL/FAILED` (observed) → `BLOCK` ✓
- D1-C bound `MATERIAL/UNKNOWN` (observed) → `BLOCK` ✓
- D1-D unrelated `MATERIAL/PENDING` (binds c2, not c1) → `OK` ✓ (positive control: unrelated obligation does not poison this claim)
- D1-E bound `SATISFIED` + closure evidence → `OK` ✓
- D1-F1 completion + PENDING bound (no `required_obligation_refs`) → `BLOCK` ✓ (completion behavior preserved)
- D1-F2 completion w/ `required_obligation_refs` satisfied → `OK` ✓
- D1-G obligation both referenced and bound → single `BLOCK` code, no duplicate effect ✓

  Gating rule confirmed in `validate_obligation` (line 121): blocks when `material AND trigger.observed AND status in {PENDING,FAILED,UNKNOWN}`. The fix removed the non-completion early-return so the bound loop runs for all claim types. (Initial D1-B/C/G probes omitting `trigger` returned `OK`; that was a harness-input omission, corrected — with `trigger.observed:true` all three statuses block.)

**D2 (direct vs registry-addressable support):**
- D2-A standalone id-less top-level support → `OK` ✓ (legitimate DIRECT representation)
- D2-B top-level support with id → `OK` ✓
- D2-C claim refs `s1` but only id-less direct support present → `BLOCK/SUPPORT_REF_UNRESOLVABLE` ✓ (direct id-less support cannot satisfy a referenced id — distinction preserved)
- D2-D list-form registry entry without id → `BLOCK/REGISTRY_MALFORMED` ✓
- D2-E dict registry key != inner id → `BLOCK/REGISTRY_MALFORMED` ✓
- D2-F dict registry missing inner id but key present → `OK` (R12 backfill) ✓
- D2-G malformed top-level support shape → `BLOCK/REGISTRY_MALFORMED` ✓ (fail-closed)

  No pseudo-ID invention: id-less direct entries remain id-less; only key-backed registry entries get R12 backfill.

**D3 (composed root-provenance independence):**
- D3-A claimed count > distinct roots → `BLOCK/INDEPENDENCE_OVERCLAIMED` ✓
- D3-B independence claimed, no roots → `BLOCK/INDEPENDENCE_WITHOUT_ROOT_PROVENANCE` ✓
- D3-C coherent roots, root registry absent → `UNKNOWN/ROOT_REGISTRY_UNAVAILABLE` ✓ (P16 now UNKNOWN)
- D3-D registered roots resolve to distinct origins → `OK` ✓ (P17 now OK)
- D3-E 3 roots collapse to 1 actual origin → `BLOCK/INDEPENDENCE_OVERCLAIMED` ✓
- D3-F legacy `source_origins`-only → `BLOCK/INDEPENDENCE_WITHOUT_ROOT_PROVENANCE` (see residual note)
- D3-G both `source_origins` + `root_provenance`, roots collapse → `BLOCK/INDEPENDENCE_OVERCLAIMED` ✓ (composed check authoritative, no bypass)

**D1/D2/D3 are genuinely closed.**

## 6. Phase F — changed-semantic-surface composition review

Read `check_obligation_path`, `check_support_path`, `_support_sources`, `check_independence`, `_validate_case` in the new implementation.

- No directly-caused **false OK**: bound material observed obligations block for all claim types; unrelated obligations do not.
- No directly-caused **false BLOCK** beyond the pre-existing D3-F boundary (below); id-less direct support is accepted, referenced-id resolution still fails closed.
- No directly-caused **unnecessary UNKNOWN**: absence of root registry yields UNKNOWN only where the five-state semantics requires registry resolution (correct).
- No **uncaught exception**: `validate_case` wraps `_validate_case` in try/except (R11) returning `EVALUATOR_FAULT` on fault; no probe raised.
- No **representation bypass**: `check_support_path` strips legacy `source_origins`/`claimed_independent_count` only when `root_provenance` is present, passes a shallow copy to the byte-identical core, and runs `check_independence` on the ORIGINAL artifact as authoritative.
- No **double evaluation**: referenced+bound obligation evaluated once (completion path skips already-evaluated ids).
- No **ordering sensitivity**: single pass over registries; deterministic.

**Residual observation (not a defect, not caused by the correction):** D3-F — a `source_origins`-only independence declaration (no `root_provenance`) yields `INDEPENDENCE_WITHOUT_ROOT_PROVENANCE`. This is **identical in the old and new candidates** (verified: old also returns `INDEPENDENCE_WITHOUT_ROOT_PROVENANCE` for `source_origins`-only). It is a pre-existing retained boundary, not a regression introduced by the D3 fix. The composed five-state semantics intentionally require `root_provenance`; pure-legacy `source_origins` declarations are not honored by the composed layer in either candidate. Recorded as a retained trust boundary, not a blocking residual.

## 7. Phase G — inherited regression reproduction

Ran the successor's shipped validation surface (Python 3.13.14):

| Surface | Result | Expected |
|---|---|---|
| `selftest contract-fixtures.v1.json` (v0.3.2 migrated) | **10/10**, `SELFTEST_PASS` | 10/10 |
| `selftest contract-fixtures.v2.json` (inherited 164) | **164/164**, `SELFTEST_PASS`, 0 flips | 164/164 |
| `selftest contract-fixtures.v2.1.json` (closure 61) | **61/61**, `SELFTEST_PASS` | 61/61 |
| `regression_suite.py` | migrated 10/10 · inherited 164/164 (ZERO flips) · closure 61/61 · **total 235** · unexpected 0 · uncaught exceptions 0 · `RESULT: PASS` | as specified |

**Determinism:** ran the regression suite twice; both runs produced identical verdict counts (`BLOCK 123 / OK 83 / UNKNOWN 9 / None 20`) and `RESULT: PASS`. The frozen `regression-results-v033candidate1.json` digest was independently verified in Phase A (matches manifest). Total exercised semantic cases = 10 + 164 + 61 = **235** (no invented total).

## 8. Phase H — corpus-coverage discrepancy (metadata correction)

PR #38 stated the inherited corpus contained **0 supports with `independence_basis`**. The later DSH contribution asserted **20 occurrences**. Verified directly (counting `independence_basis` keys in the inherited v2 corpus at `034b789`):

- **Actual count in inherited v2 corpus: 20.**
- Forms: `source_origins_only` = 3; `both(root+source)` = 11; `root_provenance_only` = 6.
- **17 of the 20 exercise the exact `root_provenance` composition path** (the D3 surface).
- (In the v2.1 closure corpus: 11 occurrences, 9 with `root_provenance`.)

**Conclusion:** PR #38's "0 supports with independence_basis" was a **metadata error in my prior audit**; the true count is 20. This does **NOT** change the D3 defect conclusion, which was independently reproduced by my own P16/P17 probes (not by corpus coverage). The 20 cases passed 164/164 on the OLD candidate — i.e., the corpus's expected verdicts are *consistent with the buggy old behavior* (author oracle agrees with implementation), which is precisely why the semantic defect was not exposed by the corpus. My independent semantic expectation (root_provenance + registered distinct origins → OK) is what flagged it. D3 closure is confirmed by P16→UNKNOWN and P17→OK on the new candidate.

## 9. Required final conclusion checklist

- exact successor ref verified? **YES** (`034b789`, resolved, all 14 digests match).
- freeze record verified? **YES** (child of semantic candidate; only manifest added; no semantic change).
- hashes verified? **YES** (14/14 independently recomputed).
- exact-candidate CI run verified? **YES** (run 32486325485, head `034b789`, Py 3.8/3.12/3.13 success).
- freeze ordering verified? **YES** (candidate tested before freeze record; workflow present at `034b789`).
- old candidate unchanged? **YES** (impl digest `78c3ddeb…` == PR #38).
- `releases/current` unchanged? **YES** (successor adds only `v0.3.3-candidate.1/`; no `current/` modification).
- D1 reproduced on old? **YES** (P42 → OK, expected BLOCK).
- D1 closed on candidate.1? **YES** (P42 → BLOCK; D1-A/B/C all BLOCK).
- unrelated-obligation positive control preserved? **YES** (D1-D → OK).
- completion behavior preserved? **YES** (D1-F1/F2).
- duplicate referenced+bound coherent? **YES** (D1-G single code).
- D2 reproduced on old? **YES** (P10 → REGISTRY_MALFORMED, expected OK).
- D2 closed on candidate.1? **YES** (P10 → OK).
- direct vs registry-addressable distinction preserved? **YES** (D2-C blocks referenced id against id-less direct).
- id-less support unable to satisfy a referenced id? **YES** (D2-C).
- R12/list-ID protections preserved? **YES** (D2-D/E/F/G).
- D3 reproduced on old? **YES** (P16/P17 → INDEPENDENCE_OVERCLAIMED, expected UNKNOWN/OK).
- P16 now UNKNOWN? **YES** (`ROOT_REGISTRY_UNAVAILABLE`).
- P17 now OK? **YES**.
- root-collapse false independence blocked? **YES** (D3-A/E).
- `source_origins` legacy behavior preserved? **YES** (D3-F same old/new; retained boundary, not a new regression).
- dual-representation deterministic? **YES** (D3-G).
- v1 10/10 reproduced? **YES**.
- inherited v2 164/164 reproduced? **YES** (0 flips).
- closure v2.1 61/61 reproduced? **YES**.
- regression suite reproduced? **YES** (235 total, 0 unexpected, 0 exceptions).
- determinism reproduced? **YES** (two identical runs).
- directly caused local regression? **NONE** (only pre-existing D3-F boundary, identical old/new).
- actual independence_basis corpus count? **20** (corrects PR #38's "0").
- does the coverage correction change the D3 conclusion? **NO** (D3 independently reproduced by P16/P17).

## 10. Final verdict

**FINAL VERDICT: `REVALIDATION_BY_PRIOR_IMPLEMENTATION_FALSIFIER_SUPPORTED`**

This verifies closure of defects previously discovered by this same validator session (D1 material false OK, D2 false BLOCK, D3 false BLOCK on `root_provenance` independence). It is **not** a new blind independent-validation claim. The successor candidate.1 genuinely closes all three findings on the exact semantic ref `034b789`, with no directly-caused local regression in the changed semantic surface, and the inherited 235-case corpus (10 + 164 + 61) reproduces with zero unexpected verdicts and zero uncaught exceptions, deterministically.

Two metadata notes for the historical record (neither changes the verdict):
1. PR #38's "0 supports with independence_basis" was incorrect; the inherited corpus contains **20** such occurrences (17 exercising the D3 path). This is a corpus-coverage metadata correction only.
2. Legacy `source_origins`-only independence declarations yield `INDEPENDENCE_WITHOUT_ROOT_PROVENANCE` in both old and new candidates — a retained boundary, not a regression introduced by the correction.

**Candidate status remains:** `IMPLEMENTATION_CANDIDATE / NOT_MAINLINE / NOT_PROMOTED`. This revalidation does not promote the candidate; Host reconciliation decides promotion.

---

## Artifacts (additive, under `collaboration/inbox/`)
- `2026-08-21-ena-v033c1-targeted-revalidation-wb.report.md` (this file)
- `2026-08-21-ena-v033c1-targeted-revalidation-wb.closure-harness.py` (executable closure harness)
- `2026-08-21-ena-v033c1-targeted-revalidation-wb.closure-results.json` (machine-readable results)
- `2026-08-21-ena-v033c1-targeted-revalidation-wb.coverage-count.json` (Phase H coverage evidence)

Did not modify `releases/v0.3.3-candidate/`, `releases/v0.3.3-candidate.1/`, `releases/current/`, frozen research artifacts, or PR #38 evidence. Did not merge this PR or remediate any defect.
