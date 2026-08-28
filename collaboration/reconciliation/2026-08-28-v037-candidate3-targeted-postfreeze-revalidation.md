# ENA v0.3.7 candidate.3 — Targeted Post-Freeze Revalidation

Date: 2026-08-28

Status: `TARGETED_POSTFREEZE_PASS / SEALED_CANDIDATE2_REPAIR_CLASSES_CLOSED / NOT_FRESH_A_S_A_P / RELEASE_RECONCILIATION_PERMITTED`

## Role and boundary

This is a targeted prior-falsifier/project-side repair revalidation against the exact frozen candidate.3 bytes.

It is **not** a new fresh search-space-independent A-S/A-P cycle and must not be cited as one.

The project deliberately paid for the bounded fresh search-space-independence cycle on candidate.2. Candidate.3 is a bounded successor whose job is to close the material candidate.2 Phase-B findings while preserving legitimate predecessor behavior.

## Exact frozen target

- identity: `v0.3.7-candidate.3`
- frozen source: `b7e88d7adb70396bd671ca97066daf2c120e0adc`
- frozen candidate subtree: `e3a9a20d16cecd78df7f32f19fca56e21159e810`
- Current subtree at frozen source: `7dcbb3934883ffa6cc5292a662588cafc1533cff`
- external freeze record: `collaboration/reconciliation/2026-08-28-v037-candidate3-freeze.md`

Predecessor candidate.2:

- frozen source: `bda470e0a6b170cec61225a905957a501454a2fe`
- frozen subtree: `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`
- Phase-B record: `collaboration/reconciliation/2026-08-28-v037-candidate2-a-s-a-p-phase-b-reconciliation.md`
- Phase-B verdict: `NEEDS_REVISION / CANDIDATE_3_REQUIRED`

## Revalidation workflow

Workflow:

`ENA v0.3.7 Candidate.3 Targeted Post-Freeze Revalidation`

Run:

`33150553992` — SUCCESS.

The workflow checked out exact frozen source `b7e88...` detached from the research control plane and verified the frozen tree and Current tree before replay.

## Sealed repair-class disposition

### A-S-01 — composed Authority richer represented semantics

Disposition: `CLOSED`.

Observed targeted conditions: `10`.

Revalidation confirmed:

- legacy minimal composed grant remains accepted when otherwise valid;
- represented revoked grant blocks;
- represented not-yet-valid grant blocks;
- represented action-scope mismatch blocks;
- represented host-scope mismatch blocks;
- represented protected-subject mismatch blocks;
- represented task-scope mismatch blocks;
- represented grantee-epoch mismatch blocks;
- represented credential binding mismatch blocks;
- fully represented compatible rich grant remains accepted.

The closure remains a represented-consistency claim, not external mandate authentication.

### A-S-02 — terminal Effect settlement downgrade into retry

Disposition: `CLOSED`.

Observed targeted conditions: `3`.

- `COMMITTED -> later NOT_COMMITTED` is rejected;
- `COMPENSATED -> later UNKNOWN` is rejected;
- predecessor legitimate direction `NOT_COMMITTED -> later COMMITTED` remains valid and resolves to no additional effect.

The reference still does not claim external exactly-once execution or receipt authenticity.

### A-S-03 — transferred source INTEGRATED chronology/snapshot parity

Disposition: `CLOSED`.

Observed targeted conditions: `4`.

- internally consistent represented source `SUPPORTED + INTEGRATED` history remains valid while receiver-local selection remains `UNASSESSED`;
- source integration preceding represented source experiment/evaluation is rejected;
- source selection snapshot mismatch at commit is rejected;
- source expression snapshot mismatch at commit is rejected.

Imported/source evidence remains source history rather than receiver-local proof.

### A-P-02 — inherited regression harness implementation provenance

Disposition: `CLOSED`.

Observed targeted conditions: `6`.

- harness describes candidate-local `validate_contracts.py` execution;
- harness and result identify `releases/v0.3.7-candidate/tools/validate_contracts.py` as the implementation surface;
- result lineage describes candidate-local successor validator behavior;
- inherited corpus remains `164/164`;
- successor closure remains `61/61`.

### A-P-03 — active package lineage / birth-base / history truth

Disposition: `CLOSED`.

Observed targeted conditions: `12`.

- root README presents candidate.3 identity;
- candidate.3 birth base is the frozen candidate.2 source, not the older release-scope checkpoint;
- `LINEAGE.md` presents candidate.3 succession while preserving candidate.2 occurrence truth;
- `CHANGELOG.md` presents candidate.3 and frozen candidate.2 histories;
- Release Discipline presents candidate.3 as active candidate and candidate.2 as predecessor;
- candidate.0 mutable/not-frozen narration is explicitly historical pre-freeze occurrence narration;
- candidate.4 is explicitly not an automatic validation step.

### A-P-04 — zh-CN identity/status reconciliation contradiction

Disposition: `CLOSED`.

Observed targeted conditions: `5`.

- projection identity is `v0.3.7-candidate.3.zh-CN.1`;
- source semantic identity is `v0.3.7-candidate.3`;
- stale claim that identity/status reconciliation is still required before freeze is absent;
- candidate.3 identity/status-bearing zh-CN surfaces are explicitly reconciled;
- projection remains `not_current: true` while still a candidate.

## Compatibility readback

The workflow additionally reran inherited valid behavior:

- inherited composed-validator corpus `164/164` — zero flips;
- successor closure corpus `61/61`;
- v2 record selftest `35`;
- Effect Lifecycle fixture corpus `25` PASS;
- target working tree remained clean;
- frozen subtree remained exactly `e3a9a20...`.

Therefore the observed compatibility posture remains:

```text
VALID_PREDECESSOR_CONTRACT_BEHAVIOR -> PRESERVED
SEALED_INVALID_FALSE_OK_OR_CONTRADICTION -> INTENTIONALLY_TIGHTENED
```

## Explicit non-claims

The workflow emitted and this record preserves:

- `fresh_search_space_independence=NOT_CLAIMED`;
- `attack_cardinality=OPEN`;
- `external_truth=NOT_ESTABLISHED`;
- release authority was not assigned by the revalidation script.

These are evidence boundaries, not hidden blockers by themselves.

## Verdict

`TARGETED_POSTFREEZE_PASS`

All six material candidate.2 Phase-B repair classes are closed under targeted replay on exact frozen candidate.3.

No repair-induced compatibility regression was observed in the inherited contracted corpus.

This result permits explicit release reconciliation. It does not itself promote Current.
