# V2.4.1 Revalidation Harness

Independent, self-contained revalidation harness used for the WorkBuddy
`REVALIDATION_BY_PRIOR_FALSIFIER` report (`2026-08-21-ena-v241-revalidation-wb.md`).

All scripts extract the exact frozen modules directly from git objects via
`git show <ref>:<path>` — **no local extraction directory is required**. Run them
from anywhere inside the repository clone.

## References verified

| Ref | Meaning |
|---|---|
| `daacab1f042c38f3856ef4d0366febd1b5e47600` | Frozen V2.4.1 successor (subject of revalidation) |
| `47e0e1b121b1ef1e8911c59980c99805ded5a963` | Prior V2.4 candidate (untouched; used as the "old" baseline to reproduce F1) |
| `260b8045332b8dfd75bb8a8f363414da88f639a0` | `origin/main` — shipped `releases/current/tools/validate_contracts.py` baseline |

## Scripts

### `verify_digests.py` — Phase A (frozen identity & digest verification)
Computes SHA-256 over each `git show daacab1:<path>` blob and compares to the
digests declared in `FREEZE-MANIFEST-V241.md`. Confirms all 8 declared digests
match and lists the full `v2.4.1/` file set at `daacab1`.

```
python collaboration/inbox/v241-harness/verify_digests.py
```
Expected: all 8 `[OK]`; undigested file = `freeze_hashes_v241.py` only.

### `phaseB_revalidate.py` — Phase B (F1 identity-ambiguity closure)
Loads the V2.4 and V2.4.1 successors as independent modules and re-runs the same
F1 divergence family (dict key ≠ explicit inner id) across all six registry kinds
and both reference directions. Confirms F1 reproduces on V2.4 (silent false
BLOCK / identity confusion) and is closed on V2.4.1 (`REGISTRY_MALFORMED`), while
legitimate representations (key==id, backfill, list-form, duplicate protection,
obligation key==id) remain `OK`.

```
python collaboration/inbox/v241-harness/phaseB_revalidate.py
```
Expected: `OVERALL: PASS`.

### `phaseC_revalidate.py` — Phase C (F2 obligation-status vocabulary gate)
Loads the V2.4 and V2.4.1 successors and exercises the obligation-status
vocabulary gate: outside-vocabulary (`OPEN`/`GARBAGE`) must be rejected on V2.4.1
but were accepted on V2.4; in-vocabulary values (incl. `NOT_REQUIRED` /
`DEFERRED_AUTHORIZED`) must not be falsely blocked by the gate; claim-aware
narrow completion (I07) intact; orphan `OPEN` blocked at the boundary.

```
python collaboration/inbox/v241-harness/phaseC_revalidate.py
```
Expected: `PHASE C RESULT: PASS`.

## Note on results-v241.json (Phase D)
Phase D is the candidate's own accumulated-corpus replay
(`research/.../v2.4.1/run_v241.py`). This revalidation **re-executed** it rather
than trusting the committed artifact, and confirmed the freshly generated output
is semantically identical to the frozen `results-v241.json` (TOTAL 148,
UNEXPECTED_VERDICTS 0, 98/98 + 25/25 + 25/25). The revalidation report documents
this; the harnesses above cover Phases A–C independently.
