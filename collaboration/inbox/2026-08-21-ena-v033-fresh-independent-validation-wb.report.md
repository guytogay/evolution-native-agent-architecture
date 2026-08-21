# ENA v0.3.3-candidate — Fresh Independent Implementation Validation Report

**Validator role:** `FRESH_INDEPENDENT_IMPLEMENTATION_VALIDATOR`
**Subject:** `releases/v0.3.3-candidate/` @ `f7dc6202dacd30e1f19d023146ecaeb4f020c922`
**Status of subject (unchanged by this run):** `IMPLEMENTATION_CANDIDATE / NOT_MAINLINE / NOT_PROMOTED`

---

## 1. Validator / provider / model

- **Provider / model family:** WorkBuddy (Hy3). This is the **same provider family** as the prior WorkBuddy revalidation branch `independent-validation/v24-wb-20260821` present in this repository.
- **Disclosure (per gate rules):** Same provider family does **not** automatically invalidate this run. This is a **new, isolated session**: fresh full clone, no imported context from any prior ENA session, no copied probes, no copied conclusions, no reused oracle assumptions. I explicitly did **not** open or read the previously-committed probe `collaboration/inbox/2026-08-21-ena-v24-independent-validation-wb.probe.py` (its existence is recorded below as a repo artifact only).
- **Run identifier:** `ena-validation/run-20260821T1900Z` (workspace `C:\Users\PC\WorkBuddy\ena-validation\`, session started 2026-08-21 19:00 GMT+8).

## 2. Independence declaration

I did **not** participate in ENA V2, V2.1–V2.4.1, the historical adversarial fixtures, prior GPT-5.6 Sol / WorkBuddy validation, DSH/DeepSeek authoring, acceptance-semantics design, reconciliation, candidate authoring, or release/promotion decisions. Blind implementation inspection and all probes were performed **before** consulting the author oracle (`contract-fixtures.v2.json`, `regression-results-v033candidate.json`, freeze claims).

## 3. Execution-gate evidence (actual, not simulated)

| Check | Result |
|---|---|
| `pwd` | `/c/Users/PC/WorkBuddy/ena-validation/repo` |
| `git status --short` | clean (detached at candidate during inspection; branch created later via remote refspec) |
| `git rev-parse HEAD` | `f7dc6202dacd30e1f19d023146ecaeb4f020c922` |
| ref `f7dc620…` | resolves |
| ref `6a44041…` (original freeze record) | resolves |
| ref `34d8917…` (CI correction) | resolves |
| ref `5f5e905…` (freeze-evidence correction) | resolves |
| `python --version` | Python 3.13.14 (managed 3.13.12 also available) |
| candidate impl exists | `releases/v0.3.3-candidate/tools/validate_contracts.py` (35,517 bytes) |
| fresh workspace | separate clone; prior probe present in tree but **not read** (see §2) |

> Note: the initial `git checkout -q f7dc620` left a stale index entry and did not populate the working tree; a subsequent `git checkout -f f7dc620` resolved it. This is a normal environment quirk, diagnosed and corrected — not a fabrication.

## 4. Workspace / environment

- OS: win32 (Git Bash). Git 2.55.0. Python 3.13.14.
- Fresh clone of `guytogay/evolution-native-agent-architecture` into `C:\Users\PC\WorkBuddy\ena-validation\repo`.
- Probe harness developed in an **isolated directory** (`C:\Users\PC\WorkBuddy\ena-validation\my-probes\`) outside the repo, to avoid inheriting any prior probe content.

## 5. Exact refs (all resolved)

- Semantic candidate: `f7dc6202dacd30e1f19d023146ecaeb4f020c922`
- Original freeze record: `6a4404119ac7d9ee0c927cd3a96d1adf26e32ba3`
- Post-freeze CI correction: `34d891716ddfdc4d478c719554efb2c5b920efb6`
- Additive freeze-evidence correction: `5f5e90558609deaf903053f59249de0e25a4ed5c`

## 6. Independently recomputed freeze hash result

I recomputed SHA-256 over committed blobs at `f7dc620` for all 11 files declared in `FREEZE-MANIFEST.md` (read from the freeze-record commit `6a44041`) and compared to the declared digests.

**Result: ALL 11 DIGESTS MATCH.** The freeze manifest accurately reflects the candidate's released files. No discrepancy.

| File | Match |
|---|---|
| `releases/v0.3.3-candidate/CANDIDATE-BASELINE.yaml` | ✅ |
| `releases/v0.3.3-candidate/README.md` | ✅ |
| `releases/v0.3.3-candidate/CHANGELOG.md` | ✅ |
| `releases/v0.3.3-candidate/05-CORE-OPERATIONAL-CONTRACTS.md` | ✅ |
| `releases/v0.3.3-candidate/schemas/composed-case.v1.schema.json` | ✅ |
| `releases/v0.3.3-candidate/tools/validate_contracts.py` | ✅ |
| `releases/v0.3.3-candidate/tools/contract-fixtures.v2.json` | ✅ |
| `releases/v0.3.3-candidate/tools/regression_suite.py` | ✅ |
| `releases/v0.3.3-candidate/tools/regression-results-v033candidate.json` | ✅ |
| `releases/v0.3.3-candidate/tools/build_regression_corpus.py` | ✅ |
| `.github/workflows/candidate-gate.yml` | ✅ |

## 7. Independent probe count

**43 independent probes** designed from a blind read of the implementation only, then executed against the real candidate. Manifest: `2026-08-21-ena-v033-fresh-independent-validation-wb.probe-manifest.md`; executable harness: `2026-08-21-ena-v033-fresh-independent-validation-wb.probe-harness.py`; machine-readable results: `2026-08-21-ena-v033-fresh-independent-validation-wb.probe-results.json`.

## 8. Full independent probe manifest

See the companion `.probe-manifest.md` (43 entries with predicted verdict/code, rationale, and observed result). Summary of execution: **33 PASS / 10 CHALLENGE**. Of the 10 challenges, **3 are genuine implementation defects** and 7 are harness prediction errors (field naming / code-ordering / missing claim refs in my own fixtures — not candidate bugs).

## 9. Expected vs actual results

| Probe | Property | Predicted | Actual | Verdict |
|---|---|---|---|---|
| P01 | SUPPORTED happy path | OK | OK | PASS |
| P02 | SUPPORTED w/o refs | BLOCK | BLOCK | PASS |
| P03 | support CONTRADICTS | BLOCK | BLOCK | PASS |
| P04 | empty support status | BLOCK | BLOCK | PASS |
| P05 | PARTIAL, claim not narrowed | UNKNOWN | UNKNOWN | PASS |
| P06 | PARTIAL, claim narrowed | OK | OK | PASS |
| P07 | evidence ref, registry absent | OK | OK | PASS |
| P08 | evidence ref missing in registry | BLOCK | BLOCK | PASS |
| P09 | empty evidence_refs + registry | BLOCK | BLOCK | PASS |
| **P10** | **top-level support w/o id (FLAG-A)** | **OK** | **BLOCK/REGISTRY_MALFORMED** | **CHALLENGE → defect** |
| P11 | top-level support w/ id | OK | OK | PASS |
| P12 | duplicate conflicting (unreferenced) | BLOCK | OK | harness error |
| P13 | duplicate identical | OK | OK | PASS |
| P14 | independence overclaim (str) | BLOCK | BLOCK | PASS |
| P15 | independence w/o roots | BLOCK | BLOCK | PASS* |
| P16 | independence count ok, root reg absent | UNKNOWN | BLOCK | harness/defect† |
| P17 | independence ok, roots distinct | OK | BLOCK | harness/defect† |
| P18 | obligation status outside vocab | BLOCK | BLOCK | PASS |
| P19 | completion w/o obl refs | BLOCK | BLOCK | PASS* |
| P20 | completion + bound PENDING | BLOCK | BLOCK | PASS* |
| P21 | SATISFIED w/o closure | BLOCK | BLOCK | PASS* |
| P22 | SATISFIED + closure, reg absent | OK | BLOCK | harness error |
| P23 | USER_EXPLICIT_GRANT | OK | OK | PASS |
| P24 | unknown source, no registry | BLOCK | BLOCK | PASS |
| P25 | registry grant valid | OK | OK | PASS |
| P26 | registry grant expired | BLOCK | BLOCK | PASS |
| P27 | mandate.expires_at expired | BLOCK | BLOCK | PASS |
| P28 | capability E0/E1 only | BLOCK | BLOCK | PASS |
| P29 | capability E3 valid | OK | OK | PASS |
| P30 | capability invalid grade | BLOCK | BLOCK | PASS |
| P31 | recovery STATE_ONLY | OK | OK | PASS |
| P32 | recovery STATE_AND_HISTORY ok | OK | OK | PASS |
| P33 | recovery shared roots | BLOCK | BLOCK | PASS |
| P34 | recovery same evidence | BLOCK | BLOCK | PASS |
| P35 | R12 key≠id | BLOCK | BLOCK | PASS |
| P36 | malformed registry | BLOCK | BLOCK | PASS |
| P37 | list entry w/o id | BLOCK | BLOCK | PASS |
| P38 | empty payload + eval_time | OK | OK | PASS |
| P39 | missing eval_time | BLOCK | BLOCK | PASS |
| P40 | malformed eval_time | BLOCK | BLOCK | PASS |
| P41 | claim_ref mismatch | BLOCK | BLOCK | PASS |
| **P42** | **bound PENDING obl, non-completion (FLAG-D)** | **BLOCK** | **OK** | **CHALLENGE → defect (false OK)** |
| P43 | capabilities w/o authority envelope | OK | OK | PASS (boundary) |

\* verdict correct; only my predicted *code* differed due to ordering/missing refs in my fixture.
† P16/P17 actually manifest the **independence composition defect** (below).

## 10. False-OK findings

**D1 (P42) — bound obligation does not gate non-completion claims (material false OK).**
A non-completion claim (e.g. `claim_type:"FACT"`) carrying a material, `PENDING` obligation that names it in `required_before_claim_refs` returns **OK**. Root cause: `check_obligation_path()` executes `if claim.get("claim_type") not in COMPLETION_TYPES: return out` **before** the bound-obligation loop, so obligations bound to the claim are never evaluated unless the claim is a completion type. This violates stated mechanism **R7** ("only obligations referenced by the claim **or bound to it** gate the claim") and the cardinal acceptance rule *materially false/invalid consequential claim → BLOCK*. This is the most serious finding (false OK in the dangerous direction), and it is **not covered by any of the 164 corpus fixtures** (0 non-completion claims with a bound obligation exist in the corpus).

## 11. False-BLOCK findings (viability damage, fail-closed)

**D2 (P10, FLAG-A) — top-level `support` object without explicit id → `REGISTRY_MALFORMED`.**
`_support_sources()` always folds the top-level `support` field into the normalization set; `normalize_registry(list)` then requires every entry to declare `support_id`/`id`. A self-contained, unreferenced top-level support dict (a representation explicitly sanctioned by R6) is therefore rejected as `REGISTRY_MALFORMED`. This diverges from v0.3.2, whose `validate_support(claim, support)` accepted a bare support dict. Legitimate minimal representations are unnecessarily rejected. Not covered by the corpus (0 id-less top-level support fixtures).

**D3 (independence composition) — root-provenance-backed independence falsely blocked by legacy `source_origins` check.**
`check_support_path()` calls the shipped `validate_support()`, whose independence overclaim check keys on `source_origins` (string list). The v0.3.3 composed independence mechanism `check_independence()` keys on `root_provenance` + root registry. A support that legitimately declares independence via `root_provenance` (verified distinct origins in the root registry) but omits `source_origins` is **falsely BLOCKed** with `INDEPENDENCE_OVERCLAIMED` by the legacy check. The corpus contains **0 supports with `independence_basis` at all**, so this path is entirely unexercised and the defect hides.

## 12. Unnecessary-UNKNOWN findings

None. The candidate does not convert resolvable situations into UNKNOWN, nor does it suppress a determinable result into UNKNOWN. (The one UNKNOWN-expectation probe, P16, actually surfaced as a BLOCK via D3, i.e. a false BLOCK, not an unnecessary UNKNOWN.)

## 13. Exception / EVALUATOR_FAULT findings

None observed. Malformed inputs are handled as machine verdicts, never uncaught exceptions:
- payload `"not-an-object"` → `REGISTRY_MALFORMED` (matches corpus fixture `IMP-03-payload-not-object`).
- malformed registry (non-dict value, list entry without id, dict key≠inner id) → `REGISTRY_MALFORMED`.
- string `support`/`claim`/`transition`/`binding` as non-dict → `REGISTRY_MALFORMED` / caught by `EVALUATOR_FAULT` fail-closed.
R11 (never-exception) holds.

## 14. API / CLI composition findings

CLI `case` mode returns **exit code 2** for `BLOCK`/`UNKNOWN` verdicts (the CLI `main()` maps `not ok → 2`). This is correct behavior but is the **direct cause of the original Candidate Gate failure** (see §24): the original `candidate-gate.yml` treated any non-zero exit as a job failure, so legitimate BLOCK/UNKNOWN spot-checks failed the gate. The composed `validate_case()` API behaves correctly; the CLI contract simply must be read via stdout JSON, not exit code.

## 15. Schema / semantic composition findings

`composed-case.v1.schema.json` is a **shape** contract; the semantic validator (`validate_case`) is authoritative. The 164 corpus drives `validate_case` directly via `input` dicts. I did not assume schema-PASS implies semantic support. The schema and the implementation agree on registry dict/list forms and R12 key/id rules, but the schema cannot express the semantic defects D1–D3 (they are logic, not shape).

## 16. Registry representation findings

- Dict-form registries: R12 enforced (dict key authoritative; inner id must equal key else `REGISTRY_MALFORMED`; missing inner id backfilled) — verified (P35).
- List-form registries: each entry must declare inner id — verified (P37).
- Top-level `support` (R6) without id triggers D2.
- Duplicate ids: conflicting → `DUPLICATE_REF_ID` when referenced (verified via a claim-referencing variant); unreferenced duplicates are inert and not flagged (acceptable, since they cannot affect a verdict).

## 17. Authority / obligation / recovery findings

- **Authority:** `USER_EXPLICIT_GRANT` and registry grants both work; expired grant → `AUTHORITY_MANDATE_SOURCE_NOT_AUTHORIZING`; mandate horizon expiry → `MANDATE_EXPIRED`; invalid grade / E0-E1-only → blocks. Consistent.
- **Obligation gating gap (D1):** only completion claims are gated; bound obligations to non-completion claims are ignored → false OK.
- **Recovery:** `STATE_AND_HISTORY` correctly requires distinct state+history evidence, delta capture, no shared evidence refs, no shared provenance roots (verified P32–P34). `STATE_ONLY` supported. Consistent.
- **Capability without authority envelope (boundary, P43):** a `binding` may declare `VERIFIED_*` capabilities with no `authority_envelope`; capability grade/evidence checks still run. Acceptable retained boundary (grades/evidence self-declared), but note `VERIFIED` does not require an authority envelope — a trust scope worth Host awareness.

## 18. Author 10-case replay

`python validate_contracts.py selftest contract-fixtures.v1.json` → **`ok=true`, `SELFTEST_PASS`, total=10, failed=0**. Matches author claim (10/10).

## 19. Author 164-case replay

`python validate_contracts.py selftest contract-fixtures.v2.json` → **`ok=true`, `SELFTEST_PASS`, total=164, failed=0**. Matches author claim (164/164, zero unexpected).

## 20. Regression-suite result

`python regression_suite.py` → **PASS — zero unexpected verdicts (0), zero uncaught exceptions (0), migrated v0.3.2 selftests 10/10 preserved.** By provenance: DSH historical 53/53, GPT56SOL 20/20, WORKBUDDY 25/25, DSH controls 50/50, migrated 10/10, impl controls 6/6. `git status` clean after run (runner rewrote `regression-results-v033candidate.json` with identical content → no real mutation).

## 21. Determinism result

The regression suite was run twice; both runs produced identical `RESULT: PASS` with identical verdict counts (`BLOCK:87, OK:61, UNKNOWN:6, None:10`) and identical per-provenance tallies. Deterministic.

## 22. Actual CI failure RCA (run `32467425405`)

- **Confirmed via GitHub API:** run `32467425405` → `conclusion=failure`, `head_sha=6a4404119ac7d9ee0c927cd3a96d1adf26e32ba3`. Run `32467620061` → `conclusion=success`, `head_sha=34d891716ddfdc4d478c719554efb2c5b920efb6`.
- **Cause (derived from the actual workflow diff, not the correction doc):** the original `candidate-gate.yml` CLI spot-check block did `if out.returncode != 0: sys.exit(1)`. But `validate_case` CLI mode exits **2** for legitimate `BLOCK`/`UNKNOWN` verdicts. So every CLI spot-check whose expected verdict was BLOCK/UNKNOWN failed the job — a **false-negative in the CI harness**, not a candidate defect. The correction changed it to judge by parsed `stdout` verdict (`assert res['verdict'] == exp_verdict`), tolerating non-zero exit.

## 23. CI correction assessment

The change between `6a44041` and `34d8917` touches **only** `.github/workflows/candidate-gate.yml` (8 lines). It is **CI-infrastructure-only**, does **not** alter candidate semantics, and is an **acceptable additive evidence correction**. Independently verified: between `f7dc620` and `34d8917` the only changed files are `candidate-gate.yml` (8 lines) plus the freeze-record documents (`FREEZE-MANIFEST.md`, `freeze_hashes_v033candidate.py`) — no semantic candidate file changed.

## 24. Freeze-evidence correction assessment

`5f5e905` separates `f7dc620` / `6a44041` / `34d8917` and documents integrity diffs ("zero semantic file changes after f7dc620; candidate-gate.yml CI-only; releases/current untouched"). My independent verification **confirms** this: all 11 declared digests match at `f7dc620`; semantic tree is invariant to `34d8917`. The correction is accurate and additive (evidence-accuracy only, not independent validation).

## 25. Author-oracle challenges

The 164/164 PASS demonstrates *implementation ↔ author-oracle agreement*, **not** semantic correctness in untested regions. Corpus coverage gaps (verified by scanning all 154 `case`-mode fixtures):
- **0** non-completion claims with a bound (`required_before_claim_refs`) obligation → D1 hides.
- **0** supports declaring independence via `root_provenance` without `source_origins` → D3 hides.
- **0** supports with `independence_basis` at all → the entire independence path is unexercised.
- **0** top-level `support` objects without an id → D2 hides.

Thus the corpus does not expose the three defects; `164/164` is consistent with the implementation agreeing with an oracle that shares the same blind spots.

## 26. Retained trust boundaries (acceptable)

- `eval_time` required, caller-controlled, never silently defaulted.
- Absent evidence registry → baseline (no existence verdict); absent root registry → `UNKNOWN`; absent authority registry → `BLOCK`.
- Registry content truth, evidence grades, mandate content, observed scope are self-declared (external attestation outside the validator) — documented and acceptable.
- These are deliberate external boundaries, not defects.

## 27. Residuals / material findings

- **D1 (false OK)** — non-completion claims with bound open obligations are not gated. Material.
- **D2 (false BLOCK)** — id-less top-level `support` rejected as malformed. Real but low-severity, fail-closed.
- **D3 (false BLOCK)** — root-provenance independence blocked by legacy `source_origins` check. Real, fail-closed.
- **Corpus blind-spot risk** — the 164-corpus cannot demonstrate semantic correctness in independence, non-completion-obligation, or id-less-support regions; Host should not read `164/164` as full semantic validation.

## 28. Final independent verdict

**`INDEPENDENT_IMPLEMENTATION_VALIDATION_NEEDS_REVISION`**

Rationale: a material implementation defect (D1, a false OK on a materially invalid consequential claim) exists, directly violating the core acceptance principle; two additional fail-closed false-BLOCK defects (D2, D3) exist. The implementation thesis (composed `validate_case` over a byte-identical v0.3.2 core implementing the V2.4.1 mechanism set) remains **viable** — all defects are localized, fixable without redesign, and most are fail-closed. Advancement to Host promotion should be **gated on remediation of D1** (and ideally D2/D3).

## 29. Should anything block Host promotion consideration?

**Yes — D1 should block promotion until revised.** D1 permits a materially false/invalid consequential claim to reach `OK`, which is the cardinal failure mode a validator must prevent. D2/D3 are friction (fail-closed) and are recommended fixes but are lower priority.

---

### Evidence categories (kept distinct)

- **Fresh independent findings (this run):** D1, D2, D3 (§10–§11); 43-probe manifest; hash recomputation; CI RCA; corpus blind-spot analysis.
- **Author regression reproduction:** 10/10, 164/164, 0 unexpected, 0 exceptions, deterministic (§18–§21).
- **Historical evidence (inspected only after blind work):** V2.x lineage via repository branches; freeze/freeze-evidence correction documents; GitHub Actions runs 32467425405 / 32467620061.

**Candidate status remains `IMPLEMENTATION_CANDIDATE / NOT_MAINLINE / NOT_PROMOTED`.** This validator does not promote, merge, or remediate the candidate.
