# FREEZE-MANIFEST-V241 — ENA v0.3.2 V2.4.1 Residual Closure (research successor)

> **Status: RESEARCH CANDIDATE — UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED.**
> The frozen V2.4 successor `47e0e1b121b1ef1e8911c59980c99805ded5a963` and
> `releases/current/` were NOT modified. No v0.2.12 / v0.3.3 created. Promotion
> is never autonomous.
>
> This successor is **NOT independently validated**. The intended next step is
> **targeted revalidation by the prior F1 falsifier (WorkBuddy validator)** —
> not another open-ended adversarial expansion. On zero unexpected verdicts
> this round closes the independently discovered residual without reopening
> prior protections; the V2.x research loop then STOPS and the result is handed
> toward implementation (Host decision).

## 1. Identity

| Field | Value |
|---|---|
| Repository | `guytogay/evolution-native-agent-architecture` (private) |
| Branch | `main` |
| Successor code ref (immutable) | `daacab1f042c38f3856ef4d0366febd1b5e47600` (H_code241) |
| Freeze record ref | the commit containing this manifest (repo tip at freeze time; recorded in `collaboration/inbox/`) |
| Closed against | WorkBuddy Independent Validator (ENA-IV-WB), PR #30 merged `371e983`, verdict `INDEPENDENT_VALIDATION_SUPPORTED_WITH_RESIDUALS` |
| Prior candidates (frozen, untouched) | V2.4 `47e0e1b` (freeze `5f5dfca`); V2.3 `8eb5a9a` (freeze `89d5f97`) |
| Successor implementation | `research/prototypes/v2-machine-contract-hardening/v2.4.1/successor_contract_v241.py` |

## 2. Candidate file set — exact digests

SHA-256 over **committed blob content (LF-normalized)** at
`daacab1f042c38f3856ef4d0366febd1b5e47600`. Verify with `git show <ref>:<path> |
sha256sum` (any platform) or `python .../v2.4.1/freeze_hashes_v241.py <ref>`.

| SHA-256 (blob, LF) | Repo-relative path |
|---|---|
| `1390112d62bd27eecb2b6d68d7032fd6cf4d28fd977e1c600de9f0043496566a` | `research/prototypes/v2-machine-contract-hardening/v2.4.1/successor_contract_v241.py` (**the successor candidate**) |
| `b7735289a0835d44aabcf4dfb841293335fed719ceccee0eaed7d8c80bfd8689` | `research/prototypes/v2-machine-contract-hardening/v2.4.1/acceptance_semantics_v241.py` (structural oracle) |
| `71c972a6cd4694dea32b0b6ac9c61a7668b67f2819f2b591dc56ac15e0e25bf8` | `research/prototypes/v2-machine-contract-hardening/v2.4.1/wb_fixtures.py` (IND-01..17, provenance WB, verbatim) |
| `b821293e3308e12859fff8db34713d0d898eb1362341a997b23b637645290298` | `research/prototypes/v2-machine-contract-hardening/v2.4.1/f1_controls.py` (25 F1/F2 closure controls) |
| `1fa74a1f01e52ec010d032c977cf7271de875d2b3c5ba7394276a625ed9541f9` | `research/prototypes/v2-machine-contract-hardening/v2.4.1/run_v241.py` (accumulated-corpus replay) |
| `dfa4ab040afd35d3cc7b5264e49ed698b8d4e6020e0d9980f4c4e19154a57c8e` | `research/prototypes/v2-machine-contract-hardening/v2.4.1/reproduce_f1.py` (F1/F2 reproduction runner) |
| `b73a8d744b5caf889833bc9758dda768e57eaa4ea354e8d0e299a835ff9ef699` | `research/prototypes/v2-machine-contract-hardening/v2.4.1/reproduction-f1.json` (reproduction evidence) |
| `d1e83e25d541e360c03696fbdbdd59da45b19f2f92d477d7999d54ee3989e09b` | `research/prototypes/v2-machine-contract-hardening/v2.4.1/results-v241.json` (148-fixture replay evidence) |

Frozen V2.4 corpus files are the immutable V2.4 files at `47e0e1b` (digests in
the V2.4 freeze manifest), replayed unchanged.

## 3. Corpus manifest & counts (148)

| Corpus | Count | Provenance |
|---|---|---|
| Frozen V2.4 corpus (V2 23 + V2.1 18 + V2.2 7 + migrated 5 + I01–I16/O01–O04 20 + controls 25) | 98 | DSH lineage + GPT-5.6 Sol (PR #23), frozen at `47e0e1b`, unchanged |
| WorkBuddy probes IND-01..IND-17 | 25 | ENA-IV-WB (PR #30, merged `371e983`), payloads verbatim |
| F1/F2 closure controls (6 adv + 4 pos + 4 backfill + 8 regression + 3 F2) | 25 | DSH V2.4.1 (new) |
| **TOTAL** | **148** | — |

Note: the WB report prose says "26 self-authored cases"; the executable probe
file contains **25** `add()` cases (the table in the report also lists 25).
This manifest records the executable count.

## 4. Closure summary

### F1 — dict-key vs inner-id identity ambiguity (CONFIRMED, closed)
- Reproduced against the frozen V2.4 candidate: `IND-02E/O/R/A` produced silent
  false BLOCK (`*_REF_UNRESOLVABLE` / `AUTHORITY_MANDATE_SOURCE_NOT_AUTHORIZING`);
  `IND-02E-rev` produced identity confusion (OK resolving an artifact whose
  declared id disagrees) — see `reproduction-f1.json`.
- **Smallest coherent correction (R12, ONE consistent identity rule for ALL
  registry kinds):** dict key is the authoritative identity; an entry's
  explicit inner id (`support_id` / `obligation_id` / `evidence_id` /
  `root_id` / `grant_id`) must EQUAL the dict key, else the registry is
  rejected as `REGISTRY_MALFORMED` (never guess which identity is
  authoritative); a missing inner id is backfilled from the key. Applied
  uniformly to `support_registry`, `support_relations`, `evidence_registry`,
  `root_registry`, `obligations`, `authority_registry` dict forms. List-form
  entries must declare their inner id (unchanged). This also resolves the
  IND-03Ea-vs-Eb representation inconsistency for support (dict backfill now
  consistent across all kinds).
- Result: `IND-02E/O/R/A` → `BLOCK REGISTRY_MALFORMED` (explicit verdict, not a
  silent false BLOCK); `IND-02E-rev` → `BLOCK REGISTRY_MALFORMED` (identity
  confusion eliminated); controls (key==id, backfill) all OK.

### F2 — OPEN obligation status reaching OK (clarified, closed as defense-in-depth)
- Reproduced: `IND-01` (material+observed+OPEN obligation bound to a completion
  claim) reached OK in the frozen candidate.
- The shipped `triggered-obligation.v1.schema.json` status enum is
  `{PENDING, SATISFIED, NOT_REQUIRED, DEFERRED_AUTHORIZED, FAILED, UNKNOWN}`;
  OPEN is not permitted. Per the Host instruction this is treated as an
  integration-precondition / defense-in-depth question, NOT a new semantic
  rule: the **schema-valid-input precondition is now machine-enforced at the
  semantic boundary** — any obligation status outside the shipped vocabulary →
  `BLOCK OBLIGATION_STATUS_OUTSIDE_VOCABULARY`. The vocabulary is **NOT
  expanded**. In-vocabulary behavior is unchanged (F2-P1, corpus fixtures).
- Result: `IND-01` → `BLOCK`; `F2-A2` (GARBAGE) → `BLOCK`; regression guards
  prove claim-aware obligation scoping (I07) is not reopened (F1-R4, F1-R5).

## 5. Reproduction command (repo-relative)

From repo root:

```
python research/prototypes/v2-machine-contract-hardening/v2.4.1/run_v241.py
```

- Replays all 148 fixtures through the ONE V2.4.1 implementation; expected
  verdicts from the structural oracle; success = `UNEXPECTED_VERDICTS: 0` +
  exit 0. Regenerates `v2.4.1/results-v241.json` (deterministic; double-run
  hash stable).
- F1/F2 reproduction against the frozen V2.4 candidate:

```
python research/prototypes/v2-machine-contract-hardening/v2.4.1/reproduce_f1.py
```

- Cross-check digests: `python .../v2.4.1/freeze_hashes_v241.py daacab1f042c38f3856ef4d0366febd1b5e47600`
- stdlib only; language level identical to the frozen candidates
  (3.8-compatible surface; independently tested window 3.8.18/3.12.14/3.13.12;
  this round tested on 3.14 Windows).

## 6. Replay result (frozen evidence — `results-v241.json`)

| Corpus | Expected | Actual | Matched |
|---|---|---|---|
| Frozen V2.4 (98) | per frozen semantics | identical | **98/98 (ZERO verdict flips vs frozen V2.4)** |
| WorkBuddy probes (25) | reconciled wb_expect | identical | **25/25; oracle vs wb_expect 25/25 consistent** |
| F1/F2 closure controls (25) | declared | identical | **25/25** |
| **TOTAL (148)** | **BLOCK 82 / OK 60 / UNKNOWN 6** | **identical** | **148/148 — UNEXPECTED_VERDICTS: 0** |

- Exceptions: **0**; `EVALUATOR_FAULT`: **0**.
- F1 findings closed with explicit `REGISTRY_MALFORMED`; F2 closed with
  `OBLIGATION_STATUS_OUTSIDE_VOCABULARY`.

## 7. Runtime / governance cost introduced

| Metric | Frozen V2.4 | V2.4.1 |
|---|---|---|
| Implementation lines (`successor_contract*.py`) | 527 | **544 (+17)** |
| New explicit codes | — | `OBLIGATION_STATUS_OUTSIDE_VOCABULARY` (+1; `REGISTRY_MALFORMED` pre-existed) |
| New constants | — | `OBLIGATION_STATUS_VOCABULARY` (mirrors shipped schema enum) |
| New rules | — | R12 identity rule (one consistent dict-form identity rule) + F2 vocabulary gate |
| Runtime dependencies | stdlib | stdlib (unchanged) |
| Governance cost | — | negligible: one vocabulary constant to keep in sync with the shipped schema enum |

The closure is the smallest coherent correction requested: one identity rule
applied uniformly, one vocabulary gate, no schema changes, no vocabulary
expansion, no new dependencies.

## 8. Trust boundaries (updated)

All V2.4 documented boundaries remain (evidence-existence posture; mandate
vocabulary; self-declared registry truth; caller-controlled `eval_time`;
PARTIAL narrowing marker; research-only; corpus authorship). Updates:
- **F1 is no longer a boundary**: registry identity is now canonical
  (dict key authoritative, divergence rejected) across all registry kinds.
- **F2 is closed as defense-in-depth**: obligation status vocabulary is
  machine-enforced at the semantic boundary; the shipped schema remains the
  canonical input contract.
- The IND-03Ea/Eb representation inconsistency is resolved for support
  (dict-form backfill now uniform with the other registry kinds).

## 9. Freeze declaration — end of the V2.x research loop

The V2.4.1 residual-closure successor is hereby **frozen for targeted
revalidation** at code ref `daacab1f042c38f3856ef4d0366febd1b5e47600` (+
freeze-record tip containing this manifest). Implementation work stops.

- **Intended next validation step:** targeted revalidation by the prior F1
  falsifier (WorkBuddy validator) — closed-scope recheck of F1/F2 closure, not
  another open-ended adversarial expansion.
- This candidate is **NOT called independently validated**; the candidate
  author (DSH lineage) does not perform the independent revalidation.
- **The V2.x research loop stops here.** On revalidation, the result is handed
  toward implementation — adoption/promotion decisions remain Host authority.
- Non-goals (unchanged): no `releases/current/` modification; no
  v0.2.12/v0.3.3; no promotion; all V2.4.1 work remains
  UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED.

Success criterion met: the independently discovered residual (F1) is closed
without reopening prior protections (98/98 frozen verdicts preserved), F2 is
clarified and closed as defense-in-depth, zero unexpected verdicts on the
148-fixture reconciled corpus, and the research loop terminates.
