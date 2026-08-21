# FREEZE-EVIDENCE-CORRECTION — ENA v0.3.3-candidate

> **Additive freeze-evidence correction. Status: IMPLEMENTATION_CANDIDATE / NOT_MAINLINE / NOT_PROMOTED.**
> This record CORRECTS the accuracy of the freeze evidence; it does NOT modify
> the semantic implementation candidate, the original freeze record, or
> `releases/current/` (v0.3.2). It does NOT constitute independent validation.
> The original freeze record `6a4404119ac7d9ee0c927cd3a96d1adf26e32ba3` and the
> original candidate history are preserved unmodified; this correction is
> additive and does not rewrite the failure out of the evidence history.

## 1. Reference separation and exact relationship

| Ref | Role |
|---|---|
| `f7dc6202dacd30e1f19d023146ecaeb4f020c922` | **Semantic implementation candidate ref** (the semantic candidate under validation; unchanged by this correction) |
| `6a4404119ac7d9ee0c927cd3a96d1adf26e32ba3` | **Original freeze record** (added `releases/v0.3.3-candidate/FREEZE-MANIFEST.md` + `tools/freeze_hashes_v033candidate.py` on top of the semantic candidate) |
| `34d891716ddfdc4d478c719554efb2c5b920efb6` | **Post-freeze validation-infrastructure correction ref** (changes ONLY `.github/workflows/candidate-gate.yml`) |

Relationship (linear, in main history):

```
f7dc6202 (semantic implementation candidate)
   └─> 6a440411 (freeze record: +FREEZE-MANIFEST.md, +freeze_hashes_v033candidate.py)   [Candidate Gate run 32467425405: FAILURE]
          └─> 34d891716 (validation-infrastructure correction: candidate-gate.yml only)   [Candidate Gate run 32467620061: SUCCESS]
                 └─> c02cd2a (merge PR #35) ─> fafa21b (merge PR #36, inbox)
```

## 2. What 34d8917 changed — and what it did NOT change

**Did NOT change (verified byte-for-byte, blob identity at both refs):**
- Every semantic implementation file under `releases/v0.3.3-candidate/`
  (CANDIDATE-BASELINE.yaml, README.md, CHANGELOG.md,
  05-CORE-OPERATIONAL-CONTRACTS.md, schemas/composed-case.v1.schema.json,
  tools/validate_contracts.py, tools/contract-fixtures.v2.json,
  tools/regression_suite.py, tools/regression-results-v033candidate.json,
  tools/build_regression_corpus.py) — all IDENTICAL at
  `f7dc6202…` and `34d891716…` (verified via `git show <ref>:<path>`).
- `releases/current/` (v0.3.2) — untouched across the whole range.

**Did change (only):**
- `.github/workflows/candidate-gate.yml` — the CLI case-mode spot-check step:
  previously it treated the expected non-zero process exit code for
  BLOCK/UNKNOWN verdicts as a test failure; the corrected logic judges the
  machine verdict from the CLI's stdout JSON instead of requiring exit code
  zero. This is validation-infrastructure / evidence-accuracy only.

## 3. Integrity checks (as executed)

### 3.1 `git diff f7dc6202dacd30e1f19d023146ecaeb4f020c922..34d891716ddfdc4d478c719554efb2c5b920efb6 -- releases/v0.3.3-candidate`

```
releases/v0.3.3-candidate/FREEZE-MANIFEST.md       | 212 +++++++++++++++++++++
releases/v0.3.3-candidate/tools/freeze_hashes_v033candidate.py |  41 ++++
2 files changed, 253 insertions(+)
```

Classification of every difference:
- `FREEZE-MANIFEST.md` — **freeze metadata** added by the freeze record
  `6a440411…` (documentation of the freeze, not semantic implementation).
- `tools/freeze_hashes_v033candidate.py` — **freeze helper tooling** added by
  `6a440411…` (digest recomputation helper, not semantic implementation).

**Result: no implementation semantic file changes after `f7dc6202…`.**

### 3.2 `git diff 6a4404119ac7d9ee0c927cd3a96d1adf26e32ba3..34d891716ddfdc4d478c719554efb2c5b920efb6 -- .github/workflows/candidate-gate.yml`

The diff is confined to the CLI case-mode spot-check block: `-3/+5` lines that
replace the exit-code-based failure check with stdout-verdict-based checking
(`BLOCK/UNKNOWN verdicts legitimately exit non-zero; judge by stdout`).

**Confirmation: this is the CI-only correction; no semantic or package content
changed.**

## 4. CI evidence — both runs recorded

| Candidate Gate run | Head commit | Outcome | Where it failed |
|---|---|---|---|
| **32467425405** | `6a4404119ac7d9ee0c927cd3a96d1adf26e32ba3` (freeze-record head) | **FAILURE** | Only the CLI case-mode spot-check step (it treated the expected non-zero exit of BLOCK/UNKNOWN verdicts as failure). The substantive candidate stages before it **passed**: schema parsing; migrated v0.3.2 selftest (10/10); 164-case composed selftest (164/164); deterministic regression suite (zero unexpected, zero exceptions). |
| **32467620061** | `34d891716ddfdc4d478c719554efb2c5b920efb6` (post-freeze correction) | **SUCCESS** | — all Candidate Gate jobs passed on Python 3.8 / 3.12 / 3.13 (plus main-gate and CodeQL on the same PR). |

The first run's failure is preserved as evidence; the history is NOT rewritten
into "all green at freeze." The original freeze-record Candidate Gate did not
fully pass; the semantic/selftest/regression stages did pass, and only the CLI
harness logic failed; the corrected workflow passed all jobs.

## 5. What this correction means

- The semantic implementation candidate remains `f7dc6202dacd30e1f19d023146ecaeb4f020c922`.
- The freeze-record evidence is now internally accurate: the gate's green CI
  result applies to the post-correction workflow (`34d891716…`), not to the
  freeze-record head (`6a440411…`), whose CI failed only in the harness logic.
- This correction changes **evidence accuracy / validation infrastructure
  only**, not candidate semantics.
- This correction does **not** constitute independent validation.

## 6. Final recommended refs for the fresh independent validator

- **Semantic candidate to validate:** `f7dc6202dacd30e1f19d023146ecaeb4f020c922`
  (unchanged).
- **Freeze record:** `6a4404119ac7d9ee0c927cd3a96d1adf26e32ba3`
  (original, unmodified; read together with this correction).
- **Validation-infrastructure correction (CI gate to reproduce):**
  `34d891716ddfdc4d478c719554efb2c5b920efb6` (the Candidate Gate that passes
  3.8 / 3.12 / 3.13 runs the candidate from the same semantic tree).
- Reproduction: `python releases/v0.3.3-candidate/tools/regression_suite.py`
  and `python releases/v0.3.3-candidate/tools/validate_contracts.py selftest
  releases/v0.3.3-candidate/tools/contract-fixtures.v2.json`, at ref
  `f7dc6202…` (semantic tree identical at `34d891716…`).

Final state remains: `IMPLEMENTATION_CANDIDATE / NOT_MAINLINE / NOT_PROMOTED`.
