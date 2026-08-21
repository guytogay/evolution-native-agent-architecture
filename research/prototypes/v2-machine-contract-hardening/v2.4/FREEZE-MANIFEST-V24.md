# FREEZE-MANIFEST-V24 — ENA v0.3.2 V2.4 Successor Candidate (post-reconciliation)

> **Status: RESEARCH CANDIDATE — UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED.**
> The frozen V2.3 candidate `8eb5a9afa4c560645b4c50dc24af7874ed54a4f2` and
> `releases/current/` were NOT modified. No v0.2.12 / v0.3.3 created. Promotion
> is never autonomous.
>
> This successor is **NOT independently validated** (independent validation of
> the successor is requested; the candidate author — DSH lineage — does not
> self-validate). It is a research candidate whose reconciled corpus has zero
> unexpected verdicts.

## 1. Identity

| Field | Value |
|---|---|
| Repository | `guytogay/evolution-native-agent-architecture` (private) |
| Branch | `main` |
| Successor code ref (immutable) | `47e0e1b121b1ef1e8911c59980c99805ded5a963` (H_code24) |
| Freeze record ref | the commit containing this manifest (repo tip at freeze time; recorded in `collaboration/inbox/`) |
| Prior candidate (frozen, untouched) | `8eb5a9afa4c560645b4c50dc24af7874ed54a4f2` (+ freeze record `89d5f97c71a762ec8b06e3a43cb385c96d2ad926`) |
| Independent validation (reconciled) | PR #23, GPT-5.6 Sol, `collaboration/inbox/2026-08-21-ena-v23-independent-validation-gpt56sol.md`, verdict NEEDS_REVISION |
| Successor implementation | `research/prototypes/v2-machine-contract-hardening/v2.4/successor_contract.py` — ONE canonical typed-resolution layer |
| Shipped baseline composed | `releases/current/tools/validate_contracts.py` (read-only reference; never modified) |

## 2. Candidate file set — exact digests

SHA-256 over **committed blob content (LF-normalized)** at `47e0e1b121b1ef1e8911c59980c99805ded5a963`. Verify with `git show <ref>:<path> | sha256sum` (any platform) or `python research/prototypes/v2-machine-contract-hardening/v2.4/freeze_hashes_v24.py <ref>`.

| SHA-256 (blob, LF) | Repo-relative path |
|---|---|
| `c1933f996c8f30cd553f2c57d1babdc1dfe64516abb588b9fddb14df3d9deeb1` | `research/prototypes/v2-machine-contract-hardening/v2.4/successor_contract.py` (**the successor candidate**) |
| `fc762d3cd5bb1f5b0e5ce149ee575577df90c915a87cc7b3b68d1b8fcd37bf24` | `research/prototypes/v2-machine-contract-hardening/v2.4/acceptance_semantics_v24.py` (structural oracle) |
| `c203f1bddb943b0ccdadc1cdf2388d000a008ca01de6199f7056273372df5059` | `research/prototypes/v2-machine-contract-hardening/v2.4/independent_fixtures.py` (I01–I16, O01–O04; provenance GPT-5.6 Sol via PR #23) |
| `0b99e14bb8f7b4ab47ddf6227e1c541af83566af7e426dc98435bc4b5e8fa9a2` | `research/prototypes/v2-machine-contract-hardening/v2.4/successor_controls.py` (25 remediation controls) |
| `5f8d09f6d6e13c4445a709656671dbf8e5534424f4093f448573e2903a9c3603` | `research/prototypes/v2-machine-contract-hardening/v2.4/run_v24.py` (accumulated-corpus replay) |
| `f3cf951279c7749feb119cf5a432116484e241411f840e3398eaf0b75b3f62ff` | `research/prototypes/v2-machine-contract-hardening/v2.4/reproduce_v23.py` (Phase-1 reproduction runner) |
| `f7b258c87bb925119e9ce62170eff1231d1713e9c37f347d5fea1419b32927ce` | `research/prototypes/v2-machine-contract-hardening/v2.4/RECONCILIATION.md` (Phase-1 findings, I01–I16 + CF + oracle) |
| `fcedd05f318ca7645841a201d5187814d151a22e38451ccd5a96e1b13ea0fb27` | `research/prototypes/v2-machine-contract-hardening/v2.4/reproduction-v23.json` (DSH reproduction at frozen ref) |
| `081f88eafbae5af198eddc52562ef425f1d9030243625472b24a25ed4a6a0b5d` | `research/prototypes/v2-machine-contract-hardening/v2.4/results-v24.json` (98-fixture replay evidence) |

Frozen corpus files are NOT re-hashed here: they are the immutable V2.3 files
at `8eb5a9a` (digests in the V2.3 freeze manifest), replayed unchanged.

## 3. Corpus manifest & counts (98)

| Corpus | Count | Provenance |
|---|---|---|
| Frozen V2 (`fixtures.py`) | 23 | DSH lineage, committed at `d178ff3` (unchanged) |
| Frozen V2.1 (`fixtures_v21.py`) | 18 | DSH lineage, `2380056` (unchanged) |
| Frozen V2.2 (`fixtures_v22.py`) | 7 | DSH lineage, `34e7456` (unchanged) |
| Frozen V2.3 migrated (`fixtures_migrated.py`) | 5 | DSH lineage, `8eb5a9a` (unchanged) |
| **Frozen subtotal** | **53** | preserved intact, ZERO verdict flips |
| Independent I01–I16 | 16 | GPT-5.6 Sol, PR #23 CI probes (verbatim) |
| Oracle-consistency O01–O04 | 4 | GPT-5.6 Sol, PR #23 §6 probes |
| **Independent subtotal** | **20** | all 20 matched + oracle 20/20 consistent |
| Successor controls (positives/negatives) | 15 / 10 | DSH successor remediation controls (new) |
| **TOTAL** | **98** | — |

## 4. Reconciliation summary (Phase 1)

- **16 CONFIRMED_MATERIAL_DEFECT** (I01–I13, I15, I16, oracle O01–O04):
  false OK × 12 (I01–I05, I08–I13), false BLOCK × 2 (I06, I07 = composition
  failures CF-1, CF-2), applicability regression CF-3 (I04/I05), exceptions × 2
  (I15, I16), oracle design defect (O01–O04).
- **1 SEMANTIC_CHALLENGE / NEEDS_EXPERIMENT** (I14, PARTIAL support): minimal
  machine rule implemented (`UNKNOWN` for PARTIAL-only support of a full
  SUPPORTED claim; explicit narrowing marker `support_claim: "PARTIAL"` → OK);
  full assertion-level narrowing semantics left open and documented.
- **0 NOT_REPRODUCED; 0 CONFIRMED_BUT_EXPECTED_BOUNDARY** (every finding is
  beyond the documented freeze boundaries; the freeze boundaries themselves
  were confirmed by the independent validator).
- Every finding was independently reproduced by DSH at the exact frozen ref
  (`reproduce_v23.py` → `reproduction-v23.json`); no remediation was adopted
  merely because an independent validator proposed it. Full per-finding
  records (actual / expected / ENA semantics / category / smallest correction /
  governance cost / positive control): `RECONCILIATION.md`.

## 5. Successor design (Phase 2) — ONE canonical typed-resolution layer

`successor_contract.py` implements the reconciled protections R1–R11:
- R1 every consequential ref resolves in its own typed namespace
  (support/obligation/evidence/root/authority);
- R2 resolved support binds back to the current `claim_ref`;
- R3 registry tri-state — absent | present-but-missing | malformed — with NO
  raw-string fallback when a registry is present but incomplete; evidence
  resolution is enforced whenever an evidence registry is supplied (missing →
  `EVIDENCE_REF_UNRESOLVABLE`), and absent-registry keeps the baseline posture
  for support/capability/transfer/closure evidence (preserving I06's OK) while
  recovery/independence provenance keeps absent → `UNKNOWN` (preserving P7/P9);
- R4 full baseline applicability envelope (host, runtime_instance,
  model_binding, route, configuration, epoch, time_interval, task_scope) with
  missing-observed-as-mismatch (via shipped `validate_support`);
- R5 duplicate IDs rejected on identity ambiguity (fingerprint), dedup only for
  byte-identical entries;
- R6 top-level artifact and registry representations compose (dict/list forms;
  top-level support is a resolution source);
- R7 obligation blocking is claim-aware (referenced or claim-bound only);
- R8 full STATE_AND_HISTORY recovery requires state-restoration AND
  history-continuity evidence, adequately resolved;
- R9 mandate-source authorization is positively typed or verified via an
  optional `authority_registry` (upstream authority contract);
- R10 PARTIAL support cannot establish a full SUPPORTED claim (→ UNKNOWN)
  unless explicitly narrowed;
- R11 malformed registry shapes yield explicit `REGISTRY_MALFORMED`; residual
  faults fail closed (`EVALUATOR_FAULT`) — never an exception.

Resolution architecture: **1 canonical `typed_resolve` + `normalize_registry`**
replacing the frozen candidate's 7 ad-hoc mechanisms.

## 6. Reproduction command (repo-relative)

From repo root:

```
python research/prototypes/v2-machine-contract-hardening/v2.4/run_v24.py
```

- Replays all 98 fixtures through the ONE successor implementation; expected
  verdicts from the structural oracle; success = `UNEXPECTED_VERDICTS: 0` +
  exit 0. Regenerates `v2.4/results-v24.json` (deterministic; double-run hash
  stable).
- Phase-1 reproduction against the frozen candidate (optional re-verification):

```
git worktree add --detach /tmp/ena-v23 8eb5a9afa4c560645b4c50dc24af7874ed54a4f2
python research/prototypes/v2-machine-contract-hardening/v2.4/reproduce_v23.py /tmp/ena-v23
```

- Cross-check digests: `python .../v2.4/freeze_hashes_v24.py 47e0e1b121b1ef1e8911c59980c99805ded5a963`
- stdlib only (pathlib/json/datetime), `from __future__ import annotations`,
  no 3.10+ syntax — language level identical to the frozen candidate (which was
  independently verified on Python 3.8.18 / 3.12.14); successor tested locally
  on Python 3.14 (Windows); independent portability verification requested.

## 7. Replay result (Phase 3, frozen evidence — `results-v24.json`)

| Corpus | Expected | Actual | Matched |
|---|---|---|---|
| Frozen V2.3 (53) | BLOCK 32 / OK 19 / UNKNOWN 2 | identical | **53/53 (ZERO verdict flips vs frozen manifest)** |
| Independent (20) | per validator expectations | identical | **20/20**; oracle vs independent expectations **20/20 consistent** |
| Successor controls (25) | BLOCK 10 / OK 15 | identical | **25/25** |
| **TOTAL (98)** | **BLOCK 55 / OK 40 / UNKNOWN 3** | **identical** | **98/98 — UNEXPECTED_VERDICTS: 0** |

- Exceptions: 0 (I15/I16 NO_EXCEPTION satisfied; malformed shapes emit
  `REGISTRY_MALFORMED`; `EVALUATOR_FAULT` never triggered).
- Composition failures CF-1/CF-2/CF-3: fixed (I06/I07/I04-I05 now receive
  their semantically expected verdicts).

## 8. New trust boundaries (Phase 3)

1. **Evidence-existence posture**: when NO evidence registry is supplied,
   support/capability/transfer/closure evidence existence is not verified
   (baseline posture; required to keep I06's OK expectation). Supplying a
   registry enables verification (missing → BLOCK). A supplied-but-incomplete
   registry is never treated as proof of existence.
2. **Mandate source vocabulary**: `AUTHORIZING_MANDATE_SOURCES` must be
   maintained; `authority_registry` is the extension mechanism (upstream
   authority contract is an explicitly enforced dependency).
3. **Registry content truth is self-declared** (inherited from frozen;
   CON-029/027): registries ride in the claim pack; the contract verifies
   resolution/structure/consistency, not external attestation.
4. **`eval_time` is caller-controlled** (inherited).
5. **PARTIAL narrowing marker** (`support_claim: "PARTIAL"`) is a new explicit
   schema field; assertion-level narrowing beyond it remains an open semantic
   challenge (I14, NEEDS_EXPERIMENT).
6. **`hardened_rules.py:17` stale machine-specific path is NOT in the
   successor's import surface** (successor imports only the shipped
   `validate_contracts`) — the defect is eliminated, not merely documented.
7. **Research-only**: the shipped v0.3.2 validator remains the enforcement
   surface; the successor changes no production behavior.
8. **Corpus authorship**: frozen + control expectations are DSH-authored;
   independent fixtures carry GPT-5.6 Sol expectations; independent validation
   of the successor is still required.

## 9. Complexity / governance cost vs frozen candidate

| Metric | Frozen V2.3 candidate | Successor (v2.4) |
|---|---|---|
| Implementation surface | 391 (cumulative_contract.py) + 159 (hardened_rules.py) = **550 lines** | **528 lines** (successor_contract.py) |
| Distinct explicit codes | **57** | **45** |
| Resolution paths | **7 ad-hoc mechanisms** (`_typed_lookup`, `resolve_support_refs`, `resolve_obligation_refs`, `check_evidence_grades`, `check_mandate`, `check_recovery_history`, `check_independence`) | **1 canonical `typed_resolve` + `normalize_registry`** |
| Runtime dependencies | stdlib | stdlib (same) |
| New schema surface | — | 1 explicit narrowing marker (`support_claim`) + 1 authority vocabulary constant |
| Machine-specific path defect | present (`hardened_rules.py:17`) | eliminated |
| Governance cost | — | authorizing-source vocabulary maintenance (R9); registry-supply expectation for verification (R3) |

Governance story: the successor is **smaller and more coherent** — one resolver
instead of seven, fewer explicit codes, no raw-string fallback inversion, no
machine-specific path — at the cost of maintaining a positive mandate-source
vocabulary and documenting the evidence-registry verification posture.

## 10. Freeze declaration

The V2.4 successor candidate is hereby **frozen for independent validation** at
code ref `47e0e1b121b1ef1e8911c59980c99805ded5a963` (+ freeze-record tip
containing this manifest). Implementation work stops. Independent validation is
requested — per the Host rule, the candidate author (DSH lineage) does not
perform the independent validation itself, and this candidate is **NOT called
independently validated**.

Non-goals (unchanged): no `releases/current/` modification; no v0.2.12/v0.3.3;
no promotion; migration is not remediation authority; all V2.4 work remains
UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED.

Success criterion met: a smaller, more coherent machine contract in which
consequential references resolve consistently through one canonical layer,
local protections compose without weakening each other (all 53 frozen verdicts
preserved), and false confidence is reduced (16 confirmed defects fixed)
without destroying legitimate agency (25 remediation controls, all passing).
