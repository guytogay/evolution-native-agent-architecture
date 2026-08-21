# FREEZE-MANIFEST — ENA v0.3.3-candidate.1 (Implementation Successor)

> **Status: IMPLEMENTATION_CANDIDATE / NOT_MAINLINE / NOT_PROMOTED.**
> Role: IMPLEMENTATION AUTHOR (not independent validator, not promotion/release
> authority). The frozen original candidate (`releases/v0.3.3-candidate/` @
> f7dc620 / 6a44041) and `releases/current/` (v0.3.2) were NOT modified.
> This candidate is NOT called independently validated; the next actor is the
> SAME fresh WorkBuddy session that produced PR #38 in a closed-scope
> `REVALIDATION_BY_PRIOR_IMPLEMENTATION_FALSIFIER` round.

## 1. Version identity

`v0.3.3-candidate.1` — new self-contained successor candidate at
`releases/v0.3.3-candidate.1/` (per ENA release discipline: same ena_version
must bind the same effective content; the previous candidate identity was not
reused).

## 2. Immutable refs

| Ref | Commit | Role |
|---|---|---|
| **Successor semantic candidate ref** | `034b7895997dd0599a0bfea10de7acfac575f232` | complete semantic candidate + candidate workflow + regression corpora |
| **Freeze record ref** | the commit containing this manifest (child commit of the candidate ref) | freeze evidence |
| Base candidates (untouched) | `f7dc6202dacd30e1f19d023146ecaeb4f020c922` (v0.3.3-candidate), `6a44041…` (freeze), `34d8917…` (CI fix), `5f5e905…` (freeze-evidence correction) | historical evidence |
| Fresh independent validation (accepted) | PR #38, merge `c1d29f63f351298a6752b22ff028de189c56789f`, verdict `INDEPENDENT_IMPLEMENTATION_VALIDATION_NEEDS_REVISION` | evidence |

## 3. Exact changed-file list relative to f7dc6202dacd30e1f19d023146ecaeb4f020c922

The successor is a new flat package at `releases/v0.3.3-candidate.1/`. Changes
relative to the frozen v0.3.3-candidate semantic tree (`f7dc620…`, i.e. the
semantic files, excluding the old freeze metadata added later):

| Change | Path |
|---|---|
| NEW (whole package) | `releases/v0.3.3-candidate.1/` (self-contained flat package: v0.3.2 core docs/schemas carried forward) |
| MODIFIED vs f7dc620 semantic files | `tools/validate_contracts.py` (D1/D2/D3), `CANDIDATE-BASELINE.yaml`, `README.md`, `CHANGELOG.md`, `05-CORE-OPERATIONAL-CONTRACTS.md` (§5.13.9), `tools/regression_suite.py` |
| NEW (semantic) | `schemas/composed-case.v1.schema.json` (carried from base, unchanged), `tools/contract-fixtures.v2.json` (inherited 164, byte-identical), `tools/contract-fixtures.v2.1.json` (61), `tools/pr38_fixtures.py` (43 probes), `tools/d1d2d3_controls.py` (18), `tools/build_regression_corpus_v2_1.py`, `tools/regression-results-v033candidate1.json` |
| NEW (CI) | `.github/workflows/candidate-gate-v033c1.yml` |

D1/D2/D3 exact implementation changes (all inside `tools/validate_contracts.py`;
the shipped core functions remain byte-identical):

- **D1** — `check_obligation_path()`: removed the non-completion early return;
  the bound-obligation loop (obligations whose `required_before_claim_refs`
  name the claim) now runs for ALL claim types; completion claims keep the
  `required_obligation_refs` requirement and referenced-obligation gating; an
  obligation both referenced and bound is evaluated once.
- **D2** — `_support_sources()`: returns `(direct_entries, registry_entries)`;
  id-less top-level support entries are DIRECT (legitimate standalone, never
  resolving refs), id-carrying top-level entries + registries are
  REGISTRY-ADDRESSABLE; `_validate_case()` artifact-checks direct entries and
  normalizes registry entries as before (R12/backfill unchanged).
- **D3** — `check_support_path()`: when `independence_basis` declares
  `root_provenance`, a shallow copy with the legacy independence fields
  (`source_origins`, `claimed_independent_count`) stripped is passed to the
  shipped `validate_support` (core untouched), and the composed
  `check_independence()` on the original artifact is authoritative (five-state
  semantics).

## 4. Regression corpus totals and provenance breakdown

| Corpus | Count | Provenance |
|---|---|---|
| v0.3.2 migrated selftests (v1) | 10 | DSH_MIGRATED_V032 |
| Inherited v2 (frozen v0.3.3-candidate) | 164 | DSH_HISTORICAL_V2 23 · V21 18 · V22 7 · V23_MIGRATED 5 · GPT56SOL_INDEPENDENT 20 · WORKBUDDY_INDEPENDENT 25 · DSH_V24_CONTROLS 25 · DSH_V241_CONTROLS 25 · DSH_IMPLEMENTATION_CONTROLS 6 · DSH_MIGRATED_V032 10 |
| Closure v2.1 | 61 | WORKBUDDY_FRESH_VALIDATOR_PR38 43 (payloads verbatim) · DSH_V033C1_CONTROLS 18 |
| **TOTAL exercised** | **235** | provenance preserved; no historical fixture rewritten; Workbuddy expectations not retroactively edited |

## 5. Old 164-case preservation result

**164/164 passed, ZERO verdict flips** vs the frozen v0.3.3-candidate corpus
(verified via the candidate CLI selftest and the deterministic regression
suite). Migrated v0.3.2 selftests: 10/10 (exact codes, shipped core
byte-identical).

## 6. New closure-control results

**61/61 passed**: 43 PR #38 probes (D1 P42 → BLOCK, D2 P10/P11 → OK, D3
P16 → UNKNOWN, P17 → OK, plus the other 40 with their reconciled semantic
expectations) + 18 D1/D2/D3 closure controls. Zero unexpected, zero uncaught
exceptions. No new false-confidence path introduced (positive controls remain
viable: C1-D1-02/03, C1-D2-01/02, C1-D3-02/06/07 all OK; adversarial controls
all BLOCK/UNKNOWN as expected).

## 7. Supported Python CI results and run IDs (recorded truthfully)

| Candidate Gate run | Head commit | Outcome |
|---|---|---|
| **32486325485** | `034b7895997dd0599a0bfea10de7acfac575f232` (the immutable candidate ref) | **SUCCESS** — candidate.1 validation surface passed on Python 3.8 / 3.12 / 3.13 (plus main-gate and CodeQL on the same PR) |

The gate ran on the exact candidate ref before the freeze record was created
(correct freeze order). The CLI gate judges machine verdicts from stdout JSON
(BLOCK/UNKNOWN legitimately exit non-zero) — the previous freeze-evidence
mistake is not repeated.

## 8. Determinism result

The regression suite was run twice locally; both runs produced byte-identical
`regression-results-v033candidate1.json` and identical verdict counts
(BLOCK 123 / OK 83 / UNKNOWN 9 / None 20 across all three corpora). Deterministic.

## 9. Retained trust boundaries (unchanged)

Registry content truth, evidence grades, mandate content, and observed scope
remain self-declared; `eval_time` is caller-controlled and explicitly required
(never silently defaulted); schema PASS remains distinct from semantic support;
the evidence-existence posture (absent registry → baseline for
support/capability/transfer/closure, absent → UNKNOWN for recovery/independence
provenance) is unchanged. See 05-CORE-OPERATIONAL-CONTRACTS.md §5.13.8–5.13.9.

## 10. Implementation/governance cost delta (vs frozen v0.3.3-candidate)

| Metric | Delta |
|---|---|
| Validator | 3 localized fixes in the composed layer (+~40 lines); shipped core byte-identical; no new dependencies |
| New explicit codes | 0 (reuses existing codes: MATERIAL_OBLIGATION_BLOCKS_CLAIM, REGISTRY_MALFORMED, INDEPENDENCE_OVERCLAIMED, ROOT_REGISTRY_UNAVAILABLE) |
| Corpus | 164 → 235 cases (closure corpus 61) |
| CI | +1 gate workflow (candidate-gate-v033c1.yml) |
| Governance | no new roles/machinery; no vocabulary expansion; no external attestation; no eval_time default |

## 11. Confirmation — old releases untouched

- `releases/v0.3.3-candidate/` (frozen original candidate incl. freeze records
  and corrections): **untouched** (immutable historical evidence).
- `releases/current/` (v0.3.2): **untouched**.

## 12. Digests (SHA-256 over committed blobs at 034b7895997dd0599a0bfea10de7acfac575f232)

| SHA-256 (blob, LF) | Path |
|---|---|
| `f224e1fea1b2316316d7b322ee7b1a5fae2a9ad4c8f5d6d8bbbe60dbd6242e35` | `releases/v0.3.3-candidate.1/CANDIDATE-BASELINE.yaml` |
| `1f82ced35c1c85e708e3cfdd96fd18647fdff0b24308bb1dd63b7d575d144fb7` | `releases/v0.3.3-candidate.1/README.md` |
| `6b2c8191a308b6c9c5736ae5f6edc5fa14518524474d810f69c5ab76ee492f1d` | `releases/v0.3.3-candidate.1/CHANGELOG.md` |
| `8b897916dd21f4868a3fb91b23cb87288c6b39d9b4367b4fb7392783c5180e12` | `releases/v0.3.3-candidate.1/05-CORE-OPERATIONAL-CONTRACTS.md` |
| `64fff203765e8a91b23814f1e692107c2dd2507e31e1d3afa80c5e7bb1be5294` | `releases/v0.3.3-candidate.1/schemas/composed-case.v1.schema.json` |
| `b97aef426300faf2f80088a1d52cfe8000c27cd82477319a7e313fd7721767bf` | `releases/v0.3.3-candidate.1/tools/validate_contracts.py` |
| `9ab7400c7eac2ab09e852d9064bcb3b1742e99f12af0cbc93f4e88e6c61ddd9e` | `releases/v0.3.3-candidate.1/tools/contract-fixtures.v2.json` (inherited 164) |
| `31a309444654ddd949245e31d7b72ac7ff607ad976643e5abedc10c6af6eb7fa` | `releases/v0.3.3-candidate.1/tools/contract-fixtures.v2.1.json` (closure 61) |
| `21c41d35535a4b9863ae5c9eb4141d27ca27718fea962be4ea2bd8d1e5893e45` | `releases/v0.3.3-candidate.1/tools/regression_suite.py` |
| `d73f862c4b7a69557d395e198141bb62d089c0f7c8f825de3722a56c576241cf` | `releases/v0.3.3-candidate.1/tools/regression-results-v033candidate1.json` |
| `298f1a844e22b80d5355359271fb61d535fa47d2666103a0e31aef228de1adf4` | `releases/v0.3.3-candidate.1/tools/build_regression_corpus_v2_1.py` |
| `f1c0cc5c8e0a731d9757cdbd9b3260c519f6369d886e9d5592b058d7ee7a19c1` | `releases/v0.3.3-candidate.1/tools/pr38_fixtures.py` |
| `a7a255dcb1494f2b0869acc322330bf14f18efb0333ddd54508332caf02c6794` | `releases/v0.3.3-candidate.1/tools/d1d2d3_controls.py` |
| `9768ef2cab00375baa88cf821e4f5e73a55f9c0ad2aa93f53381cebeb13ba18d` | `.github/workflows/candidate-gate-v033c1.yml` |

Verify: `git show <ref>:<path> | sha256sum`.

## 13. Reproduction (repo root)

```
python releases/v0.3.3-candidate.1/tools/regression_suite.py
python releases/v0.3.3-candidate.1/tools/validate_contracts.py selftest releases/v0.3.3-candidate.1/tools/contract-fixtures.v2.1.json
```
Success = `PASS - zero unexpected, zero exceptions, inherited 164 preserved` + exit 0.

## 14. Recommended targeted-revalidation scope (next actor)

Closed-scope `REVALIDATION_BY_PRIOR_IMPLEMENTATION_FALSIFIER` by the SAME
fresh WorkBuddy session that produced PR #38:
1. reproduce D1 (P42), D2 (P10), D3 (P16/P17) on the OLD candidate
   (`f7dc620…`) to confirm the defects existed;
2. confirm closure on `v0.3.3-candidate.1` (`034b789…`);
3. verify directly affected positive controls (P06/P11/P17, C1-D2-01/02,
   C1-D3-02/06/07, bound-satisfied);
4. reproduce inherited regression (164/164, v1 10/10);
5. ensure the fixes introduced no local regression.

This targeted revalidation is NOT a new blind independent validation.

## 15. Freeze declaration

The v0.3.3-candidate.1 successor is frozen at semantic candidate ref
`034b7895997dd0599a0bfea10de7acfac575f232` (+ freeze-record tip containing this
manifest). Status remains `IMPLEMENTATION_CANDIDATE / NOT_MAINLINE /
NOT_PROMOTED`. The candidate is NOT independently validated; the next actor is
the same WorkBuddy session (prior implementation falsifier). After this freeze,
the implementation author STOPS.
