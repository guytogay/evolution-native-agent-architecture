# ENA v0.3.7 candidate.3 — Successor Repair Reconciliation

Date: 2026-08-28

Status: `SUCCESSOR_REPAIR_RECONCILED / EXACT_PREFREEZE_PASS / FREEZE_ELIGIBLE / NOT_CURRENT / NOT_RELEASED`

## Successor identity

Candidate.3 was born directly from frozen candidate.2 source:

- predecessor identity: `v0.3.7-candidate.2`
- predecessor frozen source: `bda470e0a6b170cec61225a905957a501454a2fe`
- predecessor frozen subtree: `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`
- candidate.2 Phase-B verdict: `NEEDS_REVISION / CANDIDATE_3_REQUIRED`

Candidate.3 branch:

`candidate/v0.3.7-candidate.3`

## Bounded repair scope

Candidate.3 did not reopen the full v0.3.7 design space. It repaired the material candidate.2 findings classified in Phase B:

1. composed Authority represented-semantic parity;
2. terminal Effect settlement monotonicity;
3. transferred-source integration chronology/snapshot parity;
4. inherited regression harness/result provenance truthfulness;
5. candidate lineage/changelog/birth-base self-description;
6. zh-CN reconciliation-status narration;
7. historical predecessor narration clarity without rewriting occurrence truth.

Validation-interface defects from the candidate.2 cycle — report self-hash recursion and the earlier clean-room wrapper SHA attribution error — remain method/provenance history and were not falsely counted as candidate.3 semantic repairs.

## Round 1 — executable / provenance repair

Workflow run: `33149597432` — SUCCESS.

Gated cargo commit:

`55e08740fa2e4b033cfb5bd9e8f7a4214a479f08`

Observed:

- legacy minimal composed Authority grants remain valid;
- explicitly represented richer Authority revocation/time/scope/credential/epoch semantics become decision-bearing rather than silently ignored;
- five first-round Authority targeted conditions PASS;
- later non-terminal Effect receipts cannot silently erase known `COMMITTED` / `COMPENSATED` occurrence truth;
- predecessor legal direction `NOT_COMMITTED -> later COMMITTED` remains valid;
- transferred source `INTEGRATED` history now shares represented at/before-commit experiment/evaluation and selection/expression snapshot consistency with local history;
- imported/source evidence is not upgraded to receiver-local proof;
- v2 record selftest expanded from 32 to 35 represented cases;
- inherited composed-validator regression remains 164/164 with zero flips;
- successor closure remains 61/61;
- Current isolation PASS.

## Round 2 — package identity / lineage / projection truth

Workflow run: `33149924866` — SUCCESS.

Gated cargo commit:

`c4966eeb156795c018bf324e1d296e43d12bd91f`

Round 2 first snapshotted the seven Round-1 semantic/fixture/provenance files and proved their SHA-256 values unchanged after package reconciliation.

Observed:

- active candidate identity is `v0.3.7-candidate.3`;
- exact candidate.3 birth base points to frozen candidate.2 source `bda470...` rather than the older release-scope checkpoint;
- `LINEAGE.md` and `CHANGELOG.md` preserve candidate.2 as predecessor occurrence truth while presenting candidate.3 as active successor;
- Release Discipline makes candidate.0 pre-freeze wording explicitly historical rather than treating it as present canonical state;
- candidate identity/status-bearing zh-CN surfaces are reconciled to candidate.3;
- the stale zh-CN “still require identity/status reconciliation before freeze” claim is removed/replaced with truthful intentional-inheritance wording;
- curated active identity surfaces carry no stale candidate.2 identity;
- inherited behavior controls remain green;
- Current isolation PASS.

## Clean candidate source before exact gate

Completed one-time candidate.3 observation/repair workflow and transform scaffolds were removed from the candidate branch before exact pre-freeze validation. These removals did not alter the candidate subtree.

Clean exact pre-freeze target:

- source commit: `b7e88d7adb70396bd671ca97066daf2c120e0adc`
- candidate subtree: `e3a9a20d16cecd78df7f32f19fca56e21159e810`
- Current subtree: `7dcbb3934883ffa6cc5292a662588cafc1533cff`

## Exact pre-freeze gate

Workflow:

`ENA v0.3.7 Candidate.3 Exact Pre-Freeze Gate`

Run:

`33150269264` — SUCCESS.

The gate was executed from the research control plane against detached exact candidate source `b7e88...`, so validation tooling did not mutate or redefine the candidate source under test.

Observed machine evidence:

- exact source/tree/Current binding PASS;
- retained semantic-trunk byte parity PASS;
- bounded Core identity projection PASS;
- evolution-record schema differs from frozen candidate.2 only by active package title PASS;
- Operational routing/optionality/deferred-lineage checks PASS;
- composed validator selftest 10/10;
- inherited composed corpus 164/164 zero flips;
- successor closure corpus 61/61;
- v2 record selftest 35 PASS;
- v2 helper selftest 13 PASS;
- v2 CLI roundtrip PASS;
- all bundled reference selftests PASS;
- relocated legacy compatibility regressions PASS;
- inherited author replay 132 conditions PASS;
- inherited anti-ablation replay 103 observations PASS;
- candidate.1 targeted successor replay 16 PASS;
- candidate.1 open-branch observations 9 matched expected states;
- candidate.3 Authority targeted observations 10 PASS;
- candidate.3 Effect targeted observations 3 PASS;
- candidate.3 migration targeted observations 3 PASS;
- candidate package-truth checks 52 PASS;
- zh-CN paired fixture structure 12 PASS;
- candidate Python files observed 24, compile failures 0;
- candidate files observed 118;
- target remained clean after validation;
- Current isolation remained exact.

The gate explicitly emitted:

- `CANDIDATE3_EXACT_PREFREEZE_VERDICT=PASS`
- `attack_cardinality=OPEN`
- `fresh_independent_candidate3_review_by_this_gate=NO`
- `external_truth=NOT_ESTABLISHED`
- `freeze_authority=NOT_ASSIGNED_BY_THIS_WORKFLOW`

## Compatibility disposition

Candidate.3 preserves legitimate predecessor behavior rather than every predecessor acceptance outcome.

```text
VALID_PREDECESSOR_BEHAVIOR -> PRESERVE / ZERO_FLIP_WHERE CONTRACTED
SEALED_FALSE_OK_OR_CONTRADICTION -> INTENTIONALLY_BREAK
CANDIDATE_IDENTITY_TEXT -> SUCCESSOR_PROJECTION
```

Thus candidate.0 -> candidate.3 is best described as **valid-contract compatibility plus defect tightening**, not arbitrary byte/behavior identity.

The final v0.3.7 release, if approved, is intended as a self-contained successor to `v0.3.6 Current`; older candidate identities are research/release lineage, not adopter baselines that must themselves remain deployable.

## Reconciliation verdict

`EXACT_PREFREEZE_PASS / FREEZE_ELIGIBLE`

No material correction is authorized in candidate.3 before external freeze based on the evidence presently observed.

Attack cardinality remains open. This does not create an infinite validation requirement.
