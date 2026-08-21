# FREEZE-MANIFEST — ENA v0.3.2 V2.3 Acceptance Semantics & Candidate Freeze

> **Status: RESEARCH CANDIDATE — UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED.**
> This is a research prototype under `research/prototypes/`. It does NOT modify
> `releases/current/` (v0.3.2 baseline, untouched) and creates NO new version
> (no v0.2.12 / no v0.3.3). Promotion is never autonomous; adoption decisions
> belong to the Host.
>
> Freeze point: implementation work STOPS here. Independent validation is
> requested — the candidate author (DSH lineage) does NOT self-validate.

---

## 1. Identity

| Field | Value |
|---|---|
| Repository | `guytogay/evolution-native-agent-architecture` (private) |
| Branch | `main` |
| Candidate code ref (immutable) | `8eb5a9afa4c560645b4c50dc24af7874ed54a4f2` (H_code) |
| Freeze record ref | the commit containing this manifest (repo tip at freeze time; recorded in `collaboration/inbox/2300-dsh-v23-acceptance-semantics-candidate-freeze.md`) |
| Candidate implementation | `research/prototypes/v2-machine-contract-hardening/v2.2/cumulative_contract.py` — the SAME composed candidate as V2.2 (`34e7456`). **Zero candidate changes in V2.3.** |
| Lineage | V2 `d178ff3` → V2.1 `2380056`+`b2915f8` → V2.2 `34e7456` → V2.3 `8eb5a9a` (this freeze) |

The composed candidate = base v0.3.2 validator (`validate_contracts.py`, shipped)
+ V2 hardened rules (`hardened_rules.py`) + V2.1 additions (typed resolution
fail-closed, grade enum E0..E5, explicit eval_time mandates, recovery root
derivation via registry, independence roots via registry, duplicate-ID
rejection, resolved-support-must-carry-evidence) — composed in
`cumulative_contract.py::evaluate()` with explicit states **OK / BLOCK / UNKNOWN**
(BLOCK > UNKNOWN > OK).

---

## 2. Candidate file set — exact digests

SHA-256 computed over the **committed blob content (LF-normalized)** at
`8eb5a9afa4c560645b4c50dc24af7874ed54a4f2`. Windows `core.autocrlf` may produce
CRLF working copies; verify byte-identical content with
`git show 8eb5a9afa4c560645b4c50dc24af7874ed54a4f2:<path> | sha256sum`
(any platform), or recompute with
`research/prototypes/v2-machine-contract-hardening/v2.3/freeze_hashes.py <ref>`.

| SHA-256 (blob, LF) | Repo-relative path |
|---|---|
| `5de4e32a57c52e8c9fc427a03e1bdac23108270f2ff3858983c0de090a518788` | `research/prototypes/v2-machine-contract-hardening/hardened_rules.py` (V2 candidate rules) |
| `b71eb53f139d21e5a35a9b361598409e313d5dadf9cc47e74bff8425c6f5442f` | `research/prototypes/v2-machine-contract-hardening/fixtures.py` (V2 fixtures, 23) |
| `0ba4915ba68974efca1d0108dcf99d536665920db508dacababf945bc02707f9` | `research/prototypes/v2-machine-contract-hardening/v2.1/fixtures_v21.py` (V2.1 fixtures, 18) |
| `f2f1a49f8873967f27a161a5f4646e64b94cc71170daa06b7cea246ceb49bab9` | `research/prototypes/v2-machine-contract-hardening/v2.2/cumulative_contract.py` (**the composed candidate**) |
| `fbda0869dfd3dac34b97ecca9f265992896d1f1033f1be1ab0e346fae2d4787b` | `research/prototypes/v2-machine-contract-hardening/v2.2/fixtures_v22.py` (V2.2 fixtures, 7) |
| `91dbdc5e50cd5148ac560edd52f6a8e6b3d4899fa5ca921427a05867aba303f7` | `research/prototypes/v2-machine-contract-hardening/v2.2/run_v22.py` (V2.2 replay runner) |
| `c50c667353027fc4e402d258580e4ac03f1b2d0e4e317e320f5585394c050277` | `research/prototypes/v2-machine-contract-hardening/v2.3/acceptance_semantics.py` (V2.3 semantics layer) |
| `f9e819a405a2837164d1f2f9dce807e8d02a6df63354b2d309067e6dc0753962` | `research/prototypes/v2-machine-contract-hardening/v2.3/fixtures_migrated.py` (5 migrated positives) |
| `ecceb3e193a439ac820bca3ce7101435dfeb29ade738a80b1cab19e2c10bed15` | `research/prototypes/v2-machine-contract-hardening/v2.3/run_v23.py` (verdict-correctness replay) |
| `27f37659b18ed41771a71cfe9d5a3e1e41bbda9203f08bc2ecf878497eac901b` | `research/prototypes/v2-machine-contract-hardening/v2.3/expected-verdict-manifest.json` |
| `03acbee06c332ad5f8faddde2bf263815eed06c699ee1c020db07367b7710430` | `research/prototypes/v2-machine-contract-hardening/v2.3/results-v23.json` (replay evidence) |

---

## 3. Fixture manifest & counts

| Corpus | Count | Composition |
|---|---|---|
| V2 (`fixtures.py`) | 23 | 10 POSITIVE (P1–P10), 7 ADVERSARIAL (A1–A6, A6b), 6 SECOND_ORDER (S1–S6) |
| V2.1 (`fixtures_v21.py`) | 18 | 7 POSITIVE (P21-1…P21-7), 11 ATTACK (A21-1…A21-9) |
| V2.2 (`fixtures_v22.py`) | 7 | 2 POSITIVE (V22-P1, V22-P3), 5 ATTACK (V22-A1…A5) |
| **Historical subtotal** | **48** | — |
| V2.3 migrated (`fixtures_migrated.py`) | 5 | P1m, P5m, P6m, P7m, P9m (POSITIVE controls) |
| **TOTAL replayed** | **53** | — |

The 5 historical non-OK positives are preserved **byte-for-byte unchanged** in
`fixtures.py` (P1/P5/P6/P7/P9). Their verdict change under the cumulative
contract is explained in §4. The migrated equivalents (`*m`) add the
registry/provenance/support information the cumulative contract now
legitimately requires — **no protection was weakened** to restore an old PASS.

---

## 4. Acceptance semantics (explicit) & expected-verdict manifest

| Expected verdict | Semantics | Fixtures |
|---|---|---|
| **BLOCK** | materially false/invalid claim, OR a claim requiring **mandatory** support whose references cannot be resolved (fail-closed) | 29 adversarial + P1, P5, P6 (mandatory-unresolvable) = **32** |
| **OK** | legitimate claim with **sufficient resolvable support** | 14 sufficient positives (P2,P3,P4,P8,P10,P21-1…7,V22-P1,V22-P3) + 5 migrated (P1m,P5m,P6m,P7m,P9m) = **19** |
| **UNKNOWN** | legitimate but **materially unverifiable** claim where uncertainty is allowed (verification capability absent, not reference broken) | P7 (recovery: evidence registry absent), P9 (independence: root registry absent) = **2** |

**UNKNOWN vs BLOCK — deliberate distinction.**
- BLOCK = the claim cannot be accepted: a mandatory precondition (resolvable
  support for SUPPORTED/completion claims) is unfulfilled. Uncertainty is NOT
  allowed for a mandatory precondition.
- UNKNOWN = the claim is well-formed (evidence refs exist, strings distinct)
  but a deeper property (root distinctness, origin uniqueness) cannot be
  verified without the required registry. Honesty requires uncertainty — the
  contract refuses to endorse the claim but does not brand a legitimate claim
  false merely because verification capability is absent.

**Why historical P1/P5/P6/P7/P9 changed verdict.**
- P1/P5/P6: `status=SUPPORTED` (and completion) makes resolvable support a
  MANDATORY precondition. V2 isolation checked only "refs non-empty";
  the cumulative contract fail-closes when the registry is absent →
  `SUPPORT_REF_UNRESOLVABLE` → **BLOCK**. (Not UNKNOWN: mandatory support
  is not optional uncertainty.)
- P7: STATE_AND_HISTORY recovery with distinct evidence strings, but no
  evidence registry → root distinctness unverifiable →
  `PROVENANCE_REGISTRY_UNAVAILABLE` → **UNKNOWN**.
- P9: independence claiming 2 roots, but no root registry → origin uniqueness
  unverifiable → `ROOT_REGISTRY_UNAVAILABLE` → **UNKNOWN**.

Full per-fixture expectations: `expected-verdict-manifest.json` (53 entries,
each with id / kind / semantic_category / expected_verdict / rationale).

---

## 5. Reproduction command (repo-relative)

From a fresh clone of the repo at ref `8eb5a9afa4c560645b4c50dc24af7874ed54a4f2`
(or the freeze-record tip) and **repo root**:

```
python research/prototypes/v2-machine-contract-hardening/v2.3/run_v23.py
```

- Runs all 53 fixtures through `cumulative_contract.evaluate` (the SAME
  composed candidate; zero candidate changes).
- Writes `v2.3/results-v23.json` + `v2.3/expected-verdict-manifest.json`
  (repo-relative).
- Success = `UNEXPECTED_VERDICTS: 0` and process exit code 0.
- No network, stdlib only (pathlib/json/datetime); Python ≥3.8.
- Cross-check digests (autocrlf-independent):
  `research/prototypes/v2-machine-contract-hardening/v2.3/freeze_hashes.py 8eb5a9afa4c560645b4c50dc24af7874ed54a4f2`

---

## 6. Replay result (V2.3, frozen evidence — `results-v23.json`)

| Category | Expected | Actual | Matched |
|---|---|---|---|
| adversarial (29) | BLOCK | BLOCK | 29/29 |
| mandatory_unresolvable (3: P1,P5,P6) | BLOCK | BLOCK | 3/3 |
| uncertainty_positive (2: P7,P9) | UNKNOWN | UNKNOWN | 2/2 |
| sufficient_positive (14) | OK | OK | 14/14 |
| migrated_positive (5: P1m,P5m,P6m,P7m,P9m) | OK | OK | 5/5 |
| **TOTAL 53** | — | — | **53/53 — ZERO UNEXPECTED** |

Success criterion met: every fixture received its semantically expected
verdict. This report is about **verdict correctness**, not green count.

---

## 7. Documented known residual trust boundaries

1. **Registry content truth is self-declared.** `support_registry` /
   `evidence_registry` / `root_registry` ride inside the claim pack; the
   contract verifies resolution, type, scope consistency and internal
   contradiction — NOT that a registered artifact exists in any external,
   independently verifiable source (ENA-CON-029 "claimed issuer ≠ verified
   issuer"; ENA-CON-027).
2. **Evidence grades (E0..E5) are self-declared.** No independent test-run
   verifier binds a grade to actual execution; the contract only enforces the
   enum and rejects E0/E1-only "verified".
3. **Mandate source + `expires_at` are self-declared.** The contract checks
   form and expiry against an explicit `eval_time`, not that the grant
   actually occurred in an external authority log.
4. **`eval_time` is an input parameter** (per-fixture override, default
   2026-08-20), not an independent clock; a malicious caller could backdate.
5. **`observed_scope` on support artifacts is self-declared.** The contract
   cross-checks claim-vs-support consistency and requires a transfer basis
   (with evidence) on mismatch; it does not verify ground truth.
6. **Known code defect (unfixed to preserve immutability):**
   `hardened_rules.py:17` contains a machine-specific absolute path
   (`CURRENT = Path(r"C:\Users\...\_tmp_v2\repo\releases\current")`). The
   cumulative contract resolves `validate_contracts` via repo-relative
   `sys.path` inserts, so the defect does not affect the replay; it would
   only matter if a different `validate_contracts.py` existed at that stale
   path on the evaluating machine.
7. **Research-only surface.** The base v0.3.2 validator
   (`releases/current/tools/validate_contracts.py`) remains the shipped
   enforcement; the cumulative contract is a research candidate with NO
   production enforcement change.
8. **Corpus authorship.** All fixtures were authored by the candidate author
   (DSH lineage); independent validation is REQUIRED to challenge the
   expected-verdict manifest, not assumed correct.

---

## 8. Freeze declaration

The V2.3 acceptance-semantics candidate is hereby **frozen for independent
validation** at candidate code ref `8eb5a9afa4c560645b4c50dc24af7874ed54a4f2`
(+ freeze-record tip containing this manifest). Implementation work stops.
Independent validation is requested — per the Host rule, the candidate author
(DSH lineage) does not perform the independent validation itself.

Non-goals (unchanged): no `releases/current/` modification; no v0.2.12/v0.3.3;
no promotion; migration is not remediation authority; all V2.3 work remains
UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED.
