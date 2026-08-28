# ENA v0.3.7 candidate.2 — A-S / A-P Phase-B Reconciliation

Date: 2026-08-28

Status: `PHASE_B_COMPLETE / NEEDS_REVISION / CANDIDATE_3_REQUIRED / CANDIDATE_2_REMAINS_FROZEN / NOT_CURRENT / NOT_RELEASED`

## Bound occurrence truth

Frozen target:

- identity: `v0.3.7-candidate.2`
- frozen source: `bda470e0a6b170cec61225a905957a501454a2fe`
- frozen candidate subtree: `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`
- Current subtree at frozen source: `7dcbb3934883ffa6cc5292a662588cafc1533cff`

Fresh independent A-S:

- report: `collaboration/reconciliation/2026-08-28-v037-candidate2-independent-a-s-primary-r3.md`
- exact bytes: `14839`
- SHA-256: `0e6bb214cc3398b34c13fc6a3bebd1f548ae00ea067b4c338e8ce88f42ad955f`
- Git blob SHA-1: `a8ec063fc1dcda9be70a53bf150e45ea11ac125e`
- verdict: `NOT_CLEARED`

Independent A-P:

- clean-room stage: `aea2ed25107145a557b3fe46ca0e4b90e2b90fa9`
- exact frozen package subtree exposed: `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`
- report: `collaboration/reconciliation/2026-08-28-v037-candidate2-independent-a-p-primary-r3.md`
- exact bytes: `18101`
- SHA-256: `80987d24a80c2aff90fddd96bc1891ee03c6ac02b25381d8af2a22418ebbe1db`
- Git blob SHA-1: `2465272b73c5ad4fb3027237b886604f1c9eab5a`
- verdict: `NOT_CLEARED`

Attack cardinality remains `OPEN`.

## Phase-B classification rule

Independent findings are immutable occurrence truth, but reviewer severity/classification is not automatically project authority.

Phase B classifies each finding as one of:

- `MATERIAL_CANDIDATE_BYTE_DEFECT`;
- `MATERIAL_CANDIDATE_PACKAGE_DEFECT`;
- `VALIDATION_INTERFACE_OR_PROVENANCE_DEFECT`;
- `NARRATION_AMBIGUITY / NON_STANDALONE_BLOCKER`;
- `NON_CONTRACT / INTENTIONAL_RESIDUAL`.

A frozen candidate is never silently rewritten. Any material candidate-byte or package correction requires a successor identity.

## A-S reconciliation

### A-S-01 — composed authority path can authorize represented revoked/out-of-scope grants

**Phase-B classification: `CONFIRMED / MATERIAL_CANDIDATE_BYTE_DEFECT / RELEASE_BLOCKER`.**

Frozen `tools/validate_contracts.py::check_binding()` resolves a registered authority grant and treats it as authorizing when represented `agent`, `host`, and `expires_at` satisfy its narrow checks. It does not reject represented `REVOKED` state, `revoked_at`, `valid_from`, action scope, protected-subject scope, task scope, grantee epoch, or credential binding.

This is materially inconsistent with the candidate's own Core contract that authority remains bound to subject, effect, task/purpose, consequence, and mandate source, and with the bundled standalone Authority Lease represented semantics. The Core explicitly describes the retained composed validator as protecting `positively typed/registered authority semantics`.

This is not an external-authenticity complaint. The false confidence is produced despite contradictory represented authority facts already being present.

**Required successor property:** composed authority resolution must either reuse/delegate to a shared represented Authority Lease resolver or use a deliberately narrower grant type that cannot silently carry ignored revocation/scope semantics. Add cross-surface regression cases for revoked, not-yet-valid, action/subject/task mismatch, epoch/credential mismatch where represented.

### A-S-02 — later NOT_COMMITTED can downgrade known COMMITTED and enable retry

**Phase-B classification: `CONFIRMED / MATERIAL_CANDIDATE_BYTE_DEFECT / RELEASE_BLOCKER`.**

Frozen Effect Lifecycle validation rejects same-sequence contradictory receipt status and rejects a later `REALIZE` attempt after a terminal receipt. It does not reject a strictly later receipt that regresses an already represented terminal `COMMITTED`/`COMPENSATED` state to `NOT_COMMITTED`.

`next_action()` sorts receipts and uses only the latest receipt status; therefore `COMMITTED@1 -> NOT_COMMITTED@2` can produce `RETRY_SAME_INTENT`.

For irreversible/non-idempotent effects this can create the duplicate-effect posture the reference contract is intended to prevent.

**Required successor property:** terminal settlement knowledge must be monotonic unless an explicit correction/supersession representation exists. A later contradictory non-terminal receipt must not silently erase a represented terminal occurrence; reject the record or require manual reconciliation. Add both receipt-order directions to fixtures.

### A-S-03 — transferred source INTEGRATED history lacks commit chronology/snapshot parity

**Phase-B classification: `CONFIRMED / MATERIAL_CANDIDATE_BYTE_DEFECT / RELEASE_BLOCKER`.**

Frozen `validate_transferred_source_history()` checks source experiment/evaluation presence, current source-selection consistency, and latest integration `COMMITTED`, but it does not apply the local `INTEGRATED` checks requiring represented experiment/evaluation at or before commit and snapshot parity for `selection_state_at_commit` / `expression_state_at_commit`.

The same internally impossible history can therefore be rejected as local history but accepted after moving into the migration source-history namespace.

This does not mean imported source history becomes receiver-local proof; source/receiver epistemic separation remains required. It means represented source history still has to be internally chronological.

**Required successor property:** factor/reuse the relevant integration chronology/snapshot consistency over local and transferred-source histories without upgrading imported evidence to receiver-local proof.

### A-S-04 — exact report self-hash instruction is self-referential

**Phase-B classification: `CONFIRMED / VALIDATION_INTERFACE_DEFECT / NOT_CANDIDATE_BYTE_DEFECT`.**

The A-S intake required the SHA-256 of exact final report bytes to be written into those same bytes. The reviewer correctly identified the recursion. A-P already used the corrected shape: exact report bytes plus external digest/sidecar.

This interface defect remains occurrence truth and must be reflected in the validation method, but it does not require candidate.3 by itself.

## A-P reconciliation

### A-P-01 — prior A-S wrapper commit attribution mismatch

**Phase-B classification: `CONFIRMED / VALIDATION_INTERFACE_PROVENANCE_DEFECT / ALREADY_CORRECTED / NOT_CANDIDATE_BYTE_DEFECT`.**

The project originally supplied an unresolvable A-S wrapper SHA `28dde50c9caaeee3b5cfabf51410083dbbb05a93`. Direct Git readback later established the actual parentless A-S wrapper commit as `28dde50c9caaeee3b5c269e28a7be5f07ac29ae5`, with the already-recorded A-S tree `42debebed620bd05e6e2635409057f20b57bfa9e`.

The fresh reviewer had already recorded that the requested wrapper SHA was unavailable and reviewed only the current clean-room bytes. The A-S content seal remained stable. This was therefore a control-plane identity defect, not a candidate-byte defect and not evidence that the A-S findings were fabricated or altered.

Canonical correction record: `collaboration/reconciliation/2026-08-28-v037-candidate2-cleanroom-wrapper-identity-correction-and-ap-stage.md`.

Do not double-count A-P-01 as a candidate.3 semantic repair.

### A-P-02 — regression harness falsely attributes candidate-local execution to Current

**Phase-B classification: `CONFIRMED / MATERIAL_CANDIDATE_PACKAGE_PROVENANCE_DEFECT`.**

Frozen `tools/regression_suite.py` prepends its own candidate-local `tools/` directory to `sys.path`, imports candidate-local `validate_contracts`, and executes that implementation. Yet it prints `V0.3.5 CURRENT...` and writes `implementation_surface = releases/current/tools/validate_contracts.py` plus obsolete lineage text. The checked-in regression result repeats the false implementation-surface attribution.

The numerical regression can still be useful as inherited-behavior evidence, but the package must tell the truth about what bytes it exercised.

**Required successor property:** correct the harness/result provenance to candidate-local execution while preserving the narrower statement that the corpus protects inherited composed-validator behavior only. Do not relabel corpus PASS as Current or broader candidate completeness.

### A-P-03 — candidate.2 lineage/history surfaces stale or contradictory

**Phase-B classification: `PARTIALLY_CONFIRMED / MATERIAL_PACKAGE_DRIFT + HISTORICAL_NARRATION_AMBIGUITY`.**

Confirmed material package drift:

1. candidate root README labels release-scope checkpoint `0ad263...` as the `Correct candidate birth base`, while `CANDIDATE-BASELINE.yaml` correctly records candidate.2 birth base / predecessor frozen source `ae690346...`;
2. `LINEAGE.md` is still top-level `candidate.1 Lineage` and lacks candidate.2 succession;
3. `CHANGELOG.md` has no candidate.2 entry although candidate.2 succession exists in the machine baseline.

These are active reader-facing self-description defects and require successor correction.

The fourth reviewer subclaim is downgraded: `08-RELEASE-DISCIPLINE.md` places candidate.0 `mutable / NOT_FROZEN` wording under an explicitly named `Predecessor candidate.0 preserved state` section. Candidate.2 uses an external-record freeze model that intentionally preserves pre-freeze occurrence-state text inside immutable candidate trees. The present tense is confusing and should be rewritten in candidate.3 as explicitly historical narration, but it is not treated as a separate factual release blocker.

**Required successor property:** one coherent candidate.3 lineage/changelog/birth-base story; preserve predecessor occurrence truth while clearly distinguishing `what the predecessor package said at that time` from present canonical frozen state.

### A-P-04 — zh-CN identity/status reconciliation simultaneously complete and still required

**Phase-B classification: `CONFIRMED / MATERIAL_CANDIDATE_PACKAGE_SELF_DESCRIPTION_DEFECT`.**

`CANDIDATE-BASELINE.yaml` states identity reconciliation complete and lists `adopter-facing identity/status projections reconciled` among completed assembly work. The candidate-scoped zh-CN projection manifest still lists `Inherited top-level zh-CN semantic files still require candidate identity/status reconciliation before freeze` as a known gap.

This is not evidence that every inherited zh-CN semantic file must be rewritten from v0.3.6. Inherited Constitution semantics may legitimately remain inherited. The defect is that the package simultaneously claims the reconciliation obligation closed and still-open-before-freeze.

**Required successor property:** narrow and reconcile the claims. Mark intentionally inherited semantic content as intentional inheritance, and reserve candidate identity/status labels for genuinely identity-bearing projection surfaces. The projection manifest must not retain a pre-freeze blocker after the package claims it completed.

## Overall Phase-B verdict

`NEEDS_REVISION / CANDIDATE_3_REQUIRED`

Candidate.2 contains at least three decision-changing executable semantic defects plus confirmed package provenance/self-description defects. It cannot be released or promoted as v0.3.7.

Candidate.2 remains immutable occurrence truth:

`FROZEN / A-S SEALED / A-P SEALED / PHASE-B NEEDS_REVISION / NOT_CURRENT / NOT_RELEASED`

Any material correction now requires `v0.3.7-candidate.3`.

## Candidate.3 bounded repair scope

Candidate.3 should be born directly from frozen candidate.2 source/tree and remain narrowly scoped to the sealed findings:

1. composed Authority represented-semantic parity;
2. terminal Effect receipt monotonicity/conflict handling;
3. transferred-source integration chronology/snapshot parity;
4. regression harness/result provenance truthfulness;
5. candidate lineage/changelog/birth-base self-description;
6. zh-CN reconciliation-status narration;
7. historical predecessor narration clarity where useful without rewriting occurrence truth.

Plus regression fixtures directly covering those defects and inherited zero-flip controls.

Do not invent unrelated universal rules. Existing visible residuals such as cross-environment `candidate_id` namespace uniqueness remain governed by `NO_CURRENT_CONTRACT -> DO_NOT_INVENT_UNIVERSAL_RULE` unless new contract evidence appears.

## Post-candidate.3 validation discipline

This candidate.2 cycle satisfied the deliberately bounded final fresh search-space-independence cycle. Candidate.3 does **not** automatically earn another full fresh A-S/A-P ritual merely because it exists.

After candidate.3 repair and exact pre-freeze validation:

- use targeted repair regressions and inherited regression;
- independently re-check exact repair behavior where useful, honestly labeled as targeted/prior-falsifier revalidation rather than fresh search-space-independent A-S;
- decide post-freeze whether any additional independent review pays new epistemic rent based on semantic radius and information gain;
- do not turn `attack cardinality = OPEN` into an infinite validation ceremony.

Current remains `v0.3.6 / CURRENT / FIELD_VALIDATION` until an explicit later release decision.
