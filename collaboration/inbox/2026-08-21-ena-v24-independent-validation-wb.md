# ENA v0.3.2 — V2.4 Successor Independent Validation (WB Validator)

> **Validator:** WorkBuddy Independent Validator (ENA-IV-WB) — a *separate* validator
> from the candidate author (DSH lineage) and from the prior GPT-5.6 Sol validator
> (PR #23, verdict `NEEDS_REVISION` on the V2.3 candidate). This contribution does
> **not** modify the frozen candidate, `releases/current/`, or any prior artifact.
> Status of the target remains **UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED**.

| Field | Value |
|---|---|
| Repository | `guytogay/evolution-native-agent-architecture` |
| Candidate code ref (frozen) | `47e0e1b121b1ef1e8911c59980c99805ded5a963` |
| Freeze record ref | `5f5dfca99a87812c35d4c07fd409bf6a8dc1d609` |
| Candidate author | DeepSeek Harness (DSH) |
| Validation date | 2026-08-21 |
| Validation environment | Python 3.13.12 (Windows 11) |
| Method | Phase A blind semantic inspection → Phase B identity/replay → Phase C oracle challenge |

---

## 1. Method & Provenance Discipline

- **Phase A (blind).** Read only the frozen implementation
  `research/prototypes/v2-machine-contract-hardening/v2.4/successor_contract.py`
  and the *shipped* baseline `releases/current/tools/validate_contracts.py`
  (the authoritative semantic primitives). The v2.4 author corpus
  (`RECONCILIATION.md`, `results-v24.json`, `acceptance_semantics_v24.py`,
  `successor_controls.py`, `FREEZE-MANIFEST-V24.md`) was **not** opened until
  Phase C. Independent expected verdicts were recorded *before* any author output
  was read, and confirmed by executing the candidate against 26 self-authored
  adversarial fixtures (`phaseA_probe.py`).
- **Phase B (identity & replay).** Verified commit identity, recomputed all 9
  frozen SHA-256 digests, and reproduced the official replay command.
- **Phase C (oracle challenge).** Read the author corpus and compared it against
  the independently derived semantics.

The validator did **not** optimize for reproducing 98/98; it searched for a
genuine 99th case. One was found (§5, F1).

---

## 2. Candidate Identity & Frozen Hash Verification — **VERIFIED**

The candidate commit exists, is authored by DSH, contains `successor_contract.py`,
and its ref matches the freeze manifest's `H_code24`. All nine frozen file
digests were recomputed over the committed **blob (LF)** content and **match
the `FREEZE-MANIFEST-V24.md` table exactly**:

| File | Digest match |
|---|---|
| `successor_contract.py` | ✅ `c1933f99…d9deeb1` |
| `acceptance_semantics_v24.py` | ✅ `fc762d3c…d37bf24` |
| `independent_fixtures.py` | ✅ `c203f1bd…2df5059` |
| `successor_controls.py` | ✅ `0b99e14b…e8fa9a2` |
| `run_v24.py` | ✅ `5f8d09f6…a9c3603` |
| `reproduce_v23.py` | ✅ `f3cf9512…b3f62ff` |
| `RECONCILIATION.md` | ✅ `f7b258c8…32927ce` |
| `reproduction-v23.json` | ✅ `fcedd05f…ea0fb27` |
| `results-v24.json` | ✅ `081f88ea…a6a0b5d` |

**Conclusion:** candidate identity and frozen hashes are verified; the artifacts
are bit-for-bit as frozen.

---

## 3. Frozen Replay Reproduction — **REPRODUCED**

Command (from repo root, at candidate ref `47e0e1b`):

```
python research/prototypes/v2-machine-contract-hardening/v2.4/run_v24.py
```

| Metric | Result |
|---|---|
| Exit code | **0** |
| `TOTAL_FIXTURES` | **98** |
| `UNEXPECTED_VERDICTS` | **0** (author hypothesis confirmed) |
| Verdict counts (expected = actual) | BLOCK 55 / OK 40 / UNKNOWN 3 |
| `FROZEN_PRESERVED` | **53/53** (zero verdict flips vs frozen V2.3 manifest) |
| `ORACLE_INDEPENDENT` | **20/20** consistent |
| Exceptions | **0** |

**Portability:** reproduced on **Python 3.13.12 (Windows 11)**. The manifest
claims the frozen candidate was verified on 3.8.18 / 3.12.14 and the successor
locally on 3.14; 3.13.12 interpolates the supported window and passes.

**Caveat (re-stated, not a defect):** this replay matches the author's *own*
structural oracle (`acceptance_semantics_v24.py`) and *own* corpus. It proves the
implementation reproduces the author's documented semantics — it is **not** proof
of semantic correctness, which is the subject of Phase A/C.

---

## 4. Phase A — Independently Derived Machine-Contract Guarantees

From the shipped baseline and the candidate code alone, the successor's
machine contract guarantees, *for each consequential cross-artifact reference*:

1. **Typed namespaces** (`support`/`obligation`/`evidence`/`root`/`authority`) are
   disjoint and resolved through one `typed_resolve`.
2. **Support→claim binding** (R2): resolved support must carry `claim_ref ==
   claim_id`.
3. **Registry tri-state** (R3): absent → policy; present-but-missing → `…_REF_UNRESOLVABLE`;
   malformed → `REGISTRY_MALFORMED`; evidence existence enforced *only when an
   evidence registry is supplied*.
4. **Full 8-dim applicability envelope** (R4) via shipped `validate_support`.
5. **Duplicate-id rejection** (R5) by fingerprint; byte-identical entries deduped.
6. **Claim-aware obligation gating** (R7): only referenced or claim-bound
   obligations are evaluated.
7. **Dual-evidence recovery** (R8): `STATE_AND_HISTORY` requires both
   state-restoration and history-continuity evidence, adequately resolved.
8. **Positive mandate typing** (R9) or upstream `authority_registry` verification.
9. **Partial-support minimal rule** (R10): `PARTIAL` cannot establish a full
   `SUPPORTED` claim unless explicitly narrowed.
10. **Exception safety** (R11): malformed shapes → `REGISTRY_MALFORMED`, never
    raises; residual faults → `EVALUATOR_FAULT`.

### 4.1 Independent adversarial battery (26 self-authored cases) — predicted vs actual

| Case | Independent prediction | Actual (candidate) | Note |
|---|---|---|---|
| IND-01 | BLOCK | **OK** | Material+observed+`OPEN` obligation bound to completion claim accepted → **shared blind spot** (see F2) |
| IND-02E | resolve E2 / malformed | **BLOCK `EVIDENCE_REF_UNRESOLVABLE`** | **F1**: dict key `E1` ≠ inner `evidence_id:E2`; declared id unreachable → **false BLOCK** |
| IND-02E-rev | OK but identity-confused | **OK** | resolving by dict key returns artifact whose inner id disagrees → **identity confusion** |
| IND-02E-ctrl | OK | OK | key==id control |
| IND-02O | resolve O2 / malformed | **BLOCK `OBLIGATION_REF_UNRESOLVABLE`** | **F1** on obligation registry |
| IND-02R | resolve R2 / malformed | **BLOCK `ROOT_REF_UNRESOLVABLE`** | **F1** on root registry |
| IND-02A | resolve G2 / malformed | **BLOCK `AUTHORITY_MANDATE_SOURCE_NOT_AUTHORIZING`** | **F1** on authority registry |
| IND-03Ea | OK | OK | dict evidence w/o id → backfilled |
| IND-03Eb | malformed | **BLOCK `REGISTRY_MALFORMED`** | list evidence w/o id → malformed → **representation inconsistency** |
| IND-04 | OK (unverified) | OK | evidence-registry omission → no existence check → **documented boundary #1** |
| IND-05 | BLOCK/UNKNOWN | **OK** | authority envelope omitted → no authorization check → **boundary** |
| IND-06 | OK (wildcard) | OK | `agent=None,host=None` grant authorizes everything → **boundary #2** |
| IND-07 | OK/UNKNOWN | **BLOCK `ROOT_REF_UNRESOLVABLE`** | *conceded*: roots must be registered when a registry is present → defensible per design |
| IND-08 | OK | **UNKNOWN `ROOT_REGISTRY_UNAVAILABLE`** | *conceded*: absent registry → UNKNOWN is the documented P9 posture |
| IND-09 | BLOCK (fail-closed) | **UNKNOWN `PROVENANCE_REGISTRY_UNAVAILABLE`** | recovery evidence unverifiable → **documented boundary #1/#3** |
| IND-10 | BLOCK | BLOCK ✅ | shared-root recovery correctly blocked (control) |
| IND-11 | BLOCK, no exception | BLOCK `REGISTRY_MALFORMED` ✅ | R11 exception safety confirmed |
| IND-12a | OK | OK ✅ | byte-identical dedup (control) |
| IND-12b | BLOCK | BLOCK ✅ | ambiguous duplicate rejected (control) |
| IND-13a | UNKNOWN | UNKNOWN ✅ | partial→full claim → UNKNOWN (control) |
| IND-13b | OK | OK ✅ | narrowed partial accepted (control) |
| IND-14 | BLOCK | BLOCK ✅ | R2 binding mismatch (control) |
| IND-15 | BLOCK | BLOCK ✅ | expired mandate (control) |
| IND-16 | BLOCK | BLOCK ✅ | completion w/o obligation refs (control) |
| IND-17 | OK | OK ✅ | clean happy path (control) |

**Controls (IND-10…17) all matched expected** — no false BLOCK on any
legitimate case. This confirms the 16 reconciled defects (I01–I16) are
*genuinely closed* at the layer they targeted.

---

## 5. The 99th Case — **F1: dict-key vs inner-id identity ambiguity (NEW, undocumented)**

### 5.1 Mechanics
`normalize_registry()` handles the five registry kinds differently:

- **`support`** is pre-flattened by `_support_sources()` (dict → list of values)
  and then normalized as a **list**, so support resolves by its **inner id**
  (`support_id`). Support is canonical.
- **`evidence`, `root`, `obligation`, `authority`** are normalized **directly as
  dicts**. For a dict, the code indexes entries by the **dict KEY**
  (`by_id.setdefault(k, []).append(entry)`); the inner id field (`evidence_id`,
  `root_id`, `obligation_id`, `grant_id`) is used only as a *backfill* when
  absent. Therefore, when a dict key diverges from the entry's inner id, the
  artifact is indexed under the key and is **unreachable by its declared id**.

The contract's own docstring claims dict registries are `{id: artifact}; keys
are ids`, but it (a) **does not reject** key≠inner-id as `REGISTRY_MALFORMED`,
and (b) **does not normalize** by inner id. The result is an artifact whose
resolved identity (dict key) disagrees with its own declared identity (inner id
field) — a violation of the advertised "ONE canonical typed-resolution layer"
and "artifact identity" (R1/R5) guarantee.

### 5.2 Empirical evidence
- **Phase A probes** `IND-02E/O/R/A` each produce a **FALSE BLOCK**: an artifact
  declaring `evidence_id:"E2"` (etc.) keyed by `"E1"` is unreachable when
  referenced by its declared id `"E2"`. `IND-02E-rev` shows the reverse hazard —
  resolving by the key returns an artifact whose inner id silently disagrees
  (identity confusion that can propagate downstream).
- **Corpus scan** (`check_divergence.py` over all 98 fixtures): **0 occurrences**
  of dict-key≠inner-id. Every fixture uses key==id (or omits the inner id and
  relies on key backfill). The 98/98 therefore **cannot detect F1**.
- **Oracle shares the blind spot.** `acceptance_semantics_v24._reg_keys()` returns
  `set(reg.keys())` for dict registries — i.e., it uses the **dict key** as
  identity, exactly like the implementation. Both sides agree, so the corpus can
  never surface the divergence. This is a textbook **"both implementation and
  oracle share the same blind spot."**

### 5.3 Impact & severity
- **False BLOCK (safe direction):** in heterogeneous registry generation
  (key from one system, inner id from another), a legitimate reference to the
  artifact's declared id is rejected.
- **Identity confusion (latent):** resolving by the key yields an artifact whose
  self-declared id differs — any downstream consumer reading the inner id field
  sees a different identity than the resolver used.
- **No clean false-OK in the dangerous direction** was found: the divergence
  fails *closed* (BLOCK) rather than admitting unauthorized state. This bounds
  the severity.
- **Classification:** an **undocumented residual trust boundary** (not among the
  8 freeze boundaries, not among I01–I16). It weakens the "canonical resolver"
  claim but does not reopen any of the 16 fixed defects and does not enable a
  false-confidence bypass in the common (key==id) case.

### 5.4 Recommended remediation (for the author, not applied here)
Either (a) reject dict-key≠inner-id as `REGISTRY_MALFORMED`, or (b) normalize
every registry by inner id consistently (as support already is), so identity is
representation-independent.

---

## 6. Oracle Challenge (Phase C) — Author vs Independent

| Required report item | Finding |
|---|---|
| Author & independent agree for *different reasons* | Several: e.g. IND-09 (recovery w/ absent registry → UNKNOWN) — author and I both land on UNKNOWN, but I initially expected fail-closed BLOCK while the author's intent is the documented P7/P9 posture. Agreement, different grounding. |
| Both implementation & oracle share a blind spot | **F1** (dict-key identity) and **F2** (obligation status vocabulary) — the structural oracle encodes the same dict-key convention and the same `PENDING/FAILED/UNKNOWN`-only blocking, so neither can catch these. |
| Successor fixed a prior defect but *moved* the trust boundary | I01 (R2 binding) and I11 (R9 typing) are genuinely closed at the *internal-consistency* layer, but the underlying trust is **displaced** onto the self-declared `claim_ref` / `authority_registry` (freeze boundary #3). Not a defect — a documented residual. |
| New protection creates a legitimate false rejection | **F1** produces a legitimate **false BLOCK** when key≠inner-id (§5). Also IND-03Ea vs IND-03Eb shows a representation-dependent BLOCK (dict missing-id tolerated, list missing-id → malformed). |
| Compatibility decision preserves false confidence | **Boundary #1**: evidence/authority existence is verified *only* when the
  registry is supplied; omitting the registry converts what would be a BLOCK
  into OK/UNKNOWN. This is documented but remains a genuine evasion vector for
  support/capability evidence. |

---

## 7. Required Report Checklist

- **Candidate identity verified?** ✅ Yes (commit `47e0e1b`, DSH, matches `H_code24`).
- **Frozen hashes verified?** ✅ Yes — all 9 SHA-256 digests match `FREEZE-MANIFEST-V24.md`.
- **Frozen replay reproduced?** ✅ Yes — 98/98, `UNEXPECTED_VERDICTS: 0`, exit 0, on Python 3.13.12 (Windows).
- **Portability environment(s)?** Python 3.13.12 (Windows 11); within the manifest's claimed 3.8.18 / 3.12.14 / 3.14 window.
- **New independently authored cases?** ✅ 26 Phase-A cases (`phaseA_probe.py`); headline new case **F1** (dict-key/inner-id ambiguity) plus shared blind spot **F2** (obligation status vocabulary).
- **False OKs?** No *new* false OK in the dangerous direction discovered. `IND-01` (OPEN obligation) is a **shared blind spot** (baseline/oracle intend it); `IND-04/05/09` are **documented** boundaries (#1/#3). No clean false-OK exploit via F1.
- **False BLOCKs?** ✅ **Yes — F1** (IND-02E/O/R/A) when dict key ≠ inner id; plus representation-dependent BLOCK (IND-03Eb). These are fail-closed but illegitimate rejections of existing artifacts.
- **Unnecessary UNKNOWNs?** `IND-08` initially suspected; *conceded* as the documented P9 posture. No standing unnecessary-UNKNOWN finding.
- **Exceptions?** ✅ **None** — R11 holds (`REGISTRY_MALFORMED` / `EVALUATOR_FAULT`, never a raw raise). Matches the author's 0-exception claim.
- **Composition failures?** No *new* composition failure beyond **F1**, which is itself a composition/identity failure: "multiple individually valid mechanisms that may compose incorrectly" (dict normalization vs inner-id resolution diverge for 4 of 5 registries). The R4/R6/R7/R8 compositions verified by controls are sound.
- **Author oracle accepted / partially challenged / rejected?** **Partially challenged.** Internally consistent and accepted for the shipped corpus; **challenged on completeness** for (a) registry-identity canonicality (F1) and (b) obligation-status vocabulary closure (F2). The oracle cannot catch what it does not model.
- **Documented residual boundaries confirmed?** ✅ Yes — #1 (evidence-existence posture on registry omission), #2 (mandate vocabulary), #3 (self-declared registry truth), #4 (`eval_time` caller-controlled), #5 (PARTIAL narrowing marker), #7 (research-only). #6 (stale `hardened_rules.py` path) is N/A — the successor does not import it.
- **New undocumented trust boundaries?** ✅ **Yes — F1** (dict-key/inner-id identity ambiguity for evidence/root/obligation/authority registries). **F2** (obligation status vocabulary not closed) is a subtle additional boundary not explicitly enumerated (a facet of #3).
- **Previous defects genuinely closed or merely displaced?** **Genuinely closed** at the layer each targeted (confirmed by independent controls IND-10…17 and stress variants). The deeper *external-attestation* trust is **displaced** onto documented self-declared residuals (#3) — by design, not by omission.

---

## 8. Final Verdict

# INDEPENDENT_VALIDATION_SUPPORTED_WITH_RESIDUALS

**Rationale.**
1. The candidate is bit-for-bit as frozen (identity + 9/9 hashes verified).
2. The author's 98/98 is faithfully reproducible on an independent environment
   (Python 3.13.12, Windows) — the 16 reconciled defects are genuinely fixed and
   the 53 frozen verdicts are preserved with zero flips.
3. No false OK / no exception / no new composition failure in the dangerous
   direction was found; legitimate-case controls all passed.
4. **However**, one **new, undocumented trust boundary (F1)** was discovered that
   the homogeneous 98-fixture corpus (key==id throughout) and the author's oracle
   (which shares the dict-key convention) cannot detect: the "canonical typed
   resolver" is not canonical across dict/list representations for 4 of 5
   registries, silently tolerating key≠inner-id and producing false BLOCKs and
   identity confusion. A secondary shared blind spot (F2, obligation status
   vocabulary) is inherited from the baseline and intended by the author.

The successor is **research-grade sound and materially improved** over V2.3, but
the "ONE canonical typed-resolution layer" claim is overstated until F1 is
remediated. Because F1 fails *closed* (false BLOCK, not false confidence) and is
latent in the common case, it is a **residual** rather than a promotion blocker.

**Recommendation to the candidate author:** before any promotion consideration,
harden registry identity (F1) — normalize every registry by inner id, or reject
key≠inner-id as `REGISTRY_MALFORMED` — and consider closing the obligation
status vocabulary (F2). These do not require revisiting the 16 fixed defects.

---

## 9. Submission & Provenance

- **Branch:** `independent-validation/v24-wb-20260821` (created off freeze ref
  `5f5dfca`; this report is the only added file — the frozen candidate and
  `releases/current/` are untouched).
- **Not merged, not promoted:** per instructions, this contribution is submitted
  for review only; the validator does not merge or promote.
- **Companion evidence** (validator provenance): `phaseA_probe.py`,
  `phaseA_results.jsonl`, `check_divergence.py` output (see §4.1 and §5.2).
- **Reproduce the validator's probes:**
  ```
  cd research/prototypes/v2-machine-contract-hardening/v2.4
  python phaseA_probe.py        # 26 independent adversarial cases
  python check_divergence.py    # 0 dict-key≠inner-id occurrences in corpus
  ```

*Validator: WorkBuddy Independent Validator (ENA-IV-WB). Separate from DSH
(candidate author) and from GPT-5.6 Sol (prior V2.3 validator, PR #23).*
