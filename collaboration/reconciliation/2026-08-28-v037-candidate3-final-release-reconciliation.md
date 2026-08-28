# ENA v0.3.7 candidate.3 — Final Release Reconciliation

Date: 2026-08-28

Status: `CANDIDATE_SUCCESSION_STOP / RELEASE_PREPARATION_SUPPORTED / NOT_YET_CURRENT / NOT_YET_RELEASED`

## Reconciler role

`PROJECT_MANAGER / HOST_SIDE_RECONCILER / RELEASE_DECISION_COLLABORATOR / NOT_FRESH_INDEPENDENT_VALIDATOR`

This reconciliation does not relabel exact gates, author/project-side replay, or targeted post-freeze revalidation as fresh search-space-independent validation.

## Inputs

### Active Current

- version: `v0.3.6 / CURRENT / FIELD_VALIDATION`
- Current subtree: `7dcbb3934883ffa6cc5292a662588cafc1533cff`

### Frozen candidate.2 independent cycle

- source: `bda470e0a6b170cec61225a905957a501454a2fe`
- subtree: `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`
- A-S SHA-256: `0e6bb214cc3398b34c13fc6a3bebd1f548ae00ea067b4c338e8ce88f42ad955f`
- A-P SHA-256: `80987d24a80c2aff90fddd96bc1891ee03c6ac02b25381d8af2a22418ebbe1db`
- Phase-B verdict: `NEEDS_REVISION / CANDIDATE_3_REQUIRED`

Candidate.2 supplied the deliberately bounded final fresh search-space-independence cycle for this release line.

### Frozen candidate.3

- identity: `v0.3.7-candidate.3`
- frozen source: `b7e88d7adb70396bd671ca97066daf2c120e0adc`
- frozen subtree: `e3a9a20d16cecd78df7f32f19fca56e21159e810`
- files observed: `118`
- exact pre-freeze run: `33150269264` — SUCCESS
- repair reconciliation: `collaboration/reconciliation/2026-08-28-v037-candidate3-successor-repair-reconciliation.md`
- freeze record: `collaboration/reconciliation/2026-08-28-v037-candidate3-freeze.md`

### Targeted post-freeze revalidation

Record:

`collaboration/reconciliation/2026-08-28-v037-candidate3-targeted-postfreeze-revalidation.md`

Run:

`33150553992` — SUCCESS.

Role:

`TARGETED_PRIOR_FALSIFIER_REVALIDATION / NOT_FRESH_A_S_A_P`

All six material candidate.2 Phase-B repair classes were closed on exact frozen candidate.3:

1. composed Authority richer represented semantics — CLOSED;
2. terminal Effect downgrade/retry defect — CLOSED;
3. transferred-source integration chronology/snapshot defect — CLOSED;
4. regression implementation provenance defect — CLOSED;
5. active package lineage/birth-base/history defect — CLOSED;
6. zh-CN identity/status contradiction — CLOSED.

No repair-induced regression was observed in inherited contracted behavior:

- inherited composed corpus `164/164` zero flips;
- successor closure `61/61`;
- v2 record selftest `35`;
- Effect Lifecycle fixture corpus `25` PASS.

## Reconciliation finding

The decision-changing candidate succession cycle has converged.

Candidate.0, candidate.1, and candidate.2 remain immutable occurrence truth showing successive independent or targeted falsification pressure. Candidate.3 closes the material candidate.2 blockers without reopening unrelated design space and without introducing observed inherited valid-contract regressions.

No new `MATERIAL_RELEASE_BLOCKER` has been demonstrated after candidate.3 freeze.

Therefore:

`CANDIDATE_SUCCESSION_STOP = YES`

Candidate.4 is not justified by the currently observed evidence.

A future candidate.4 would require new material evidence that changes the release decision or requires post-freeze candidate-byte correction. It is not a ceremonial next step.

## Compatibility disposition

Candidate succession is not defined as all-input behavioral identity.

The relevant compatibility contract is:

```text
LEGITIMATE_PREDECESSOR_CONTRACT_BEHAVIOR -> PRESERVE
KNOWN_INVALID_FALSE_OK / FALSE_CONFIDENCE / CONTRADICTION -> TIGHTEN
CANDIDATE_SELF_IDENTITY -> SUCCESSOR_PROJECTION
```

Observed machine support includes inherited composed-validator zero-flip controls and preserved valid directions for the repaired Effect and migration paths.

Thus candidate.0 through candidate.3 are **valid-contract compatible with intentional defect tightening**, not byte-identical or universally behavior-identical.

For adopters, the intended compatibility boundary is the singular Current transition from v0.3.6 to v0.3.7. Candidate identities are governed development lineage rather than separate adopter baselines.

## Visible residuals / evidence boundaries

The following remain visible and are not silently declared solved:

1. `attack_cardinality = OPEN`; corpus counts are observations, not completeness proofs;
2. external mandate authenticity is not established merely by represented Authority fields;
3. external Effect receipt authenticity and exactly-once execution are not established by the reference validator;
4. transferred source history consistency does not authenticate the source or convert imported evidence into receiver-local proof;
5. cross-environment `candidate_id` namespace uniqueness remains non-universalized absent a governing contract;
6. natural fresh-session cue salience / Host application remains field evidence;
7. structural and paired zh-CN fixtures do not prove universal natural-language behavioral equivalence;
8. Host-specific applicability and operational fitness remain environment-relative field evidence;
9. deferred/not-bundled mechanisms remain durable lineage rather than being silently retired.

These residuals are visible limitations or field-validation questions. No current evidence shows that another candidate byte round would resolve them at decision-relevant epistemic value.

`Governance must pay rent.`

## Why another full fresh A-S/A-P cycle is not required now

Candidate.2 fresh review materially changed the release decision and exposed author-missed defects; therefore that cycle paid substantial epistemic rent.

Candidate.3 is a bounded successor repairing those sealed findings. Exact pre-freeze and targeted post-freeze replay verify those repairs against the frozen bytes while honestly preserving the absence of fresh search-space independence.

Automatically demanding a new full fresh A-S/A-P cycle merely because candidate.3 exists would convert `attack_cardinality=OPEN` into an infinite ceremony without a new decision-changing hypothesis.

This does not forbid later independent evidence. It means release preparation is not blocked on ritual repetition absent a reason to expect new information.

## Release decision

Frozen candidate.3 is accepted as the semantic/operational source for preparing ENA v0.3.7 adopter-facing release packaging.

Decision:

`RELEASE_PREPARATION_SUPPORTED`

Target adopter-facing state:

`v0.3.7 / CURRENT / FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE`

This record does **not** itself change `releases/current/` and does not claim release completion.

## Release packaging constraints

Follow the established v0.3.6 release discipline rather than inventing a new shortcut.

At minimum:

1. create a governed `release/v0.3.7` surface from the main-visible reconciled project state;
2. transplant the exact frozen candidate.3 subtree byte-for-byte into `releases/current/` as an auditable packaging start;
3. record the transplant commit/tree before identity transformation;
4. transform candidate identity/status metadata into `v0.3.7 / CURRENT / FIELD_VALIDATION` without silently changing validated material semantics;
5. replace `CANDIDATE-BASELINE.yaml` with a truthful `CURRENT-BASELINE.yaml`;
6. preserve all 38 Constitution IDs and retained semantic-trunk meaning;
7. preserve candidate.3 Authority / Effect / migration repairs and inherited valid-contract compatibility;
8. rebind English/zh-CN adopter-facing identity to immutable v0.3.7 release identity while preserving explicit behavioral evidence boundaries;
9. keep optional references optional/default-off and Host-native equivalents allowed where specified;
10. preserve visible residuals / field-evidence boundaries in release lineage/baseline rather than erasing them;
11. remove the candidate directory from the final adopter-facing repository surface if the established release packaging model requires singular Current only;
12. run exact-head release validation, Main Gate, CodeQL, regression, identity, file-set/hash/package checks;
13. read back exact package/current-tree evidence before merge;
14. merge only after explicit release authorization on the exact reviewed release head;
15. post-merge reverify `releases/current/` identity/tree and published/readback evidence before claiming release complete;
16. update project control, handoff, history, and Project State Alignment Gate after promotion.

## Next action

`PREPARE_V0_3_7_RELEASE_BRANCH_FROM_EXACT_FROZEN_CANDIDATE3`

Current remains v0.3.6 until the governed release branch passes its release checks and is explicitly promoted.
