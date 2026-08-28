# v0.3.7 Release Promotion and Post-Merge Readback

Date: 2026-08-28

Status: `PROMOTED / CURRENT / FIELD_VALIDATION / POSTMERGE_READBACK_PASS`

## Decision

The project owner explicitly authorized promotion of ENA v0.3.7 after the exact reviewed release head and its open evidence boundaries were presented. Promotion authority was not inferred from GitHub write access, green CI, candidate authorship, or release-branch access.

Release PR #144 was moved from draft to ready and merged with exact-head protection.

## Exact release identity

```text
frozen candidate identity       = v0.3.7-candidate.3
frozen source commit            = b7e88d7adb70396bd671ca97066daf2c120e0adc
frozen candidate subtree        = e3a9a20d16cecd78df7f32f19fca56e21159e810
byte-exact transplant commit    = 8e4e25a8ba1940560fc55d7528ad31ef89a7f135
exact reviewed release head     = 3ef3605228ed427b2d25d7d586e4ffc378b7369e
release PR                      = #144
release merge commit            = 50a4bb06b98dc0dd719230f71ed1d47e42e1fad9
Current tree                    = f33e73ed997c1b66a4572685ab5474182e136e97
Current file count              = 118
deterministic package SHA-256   = 40d4dde277d54ce8252e0402e32f900fa7ab4fb0aeaa638b898073d0f02f848c
```

PR #144 was merged with `expected_head_sha=3ef3605228ed427b2d25d7d586e4ffc378b7369e`, so a moved release head could not be silently promoted.

## Exact-head and post-merge evidence

Final release-head evidence:

```text
Exact Release Gate = 33162550145 / PASS
```

The corresponding GitHub Actions artifact was downloaded and read back. Its manifest reported the same release head, Current tree, 118-file package scope, `exact_file_set_parity=true`, and `zip_readback_hash_parity=true`. The inner deterministic package SHA-256 was `40d4dde277d54ce8252e0402e32f900fa7ab4fb0aeaa638b898073d0f02f848c`.

Post-merge evidence on `50a4bb06b98dc0dd719230f71ed1d47e42e1fad9`:

```text
Main Gate                    = 33163171275 / PASS
Current validate/package     = 33163171328 / PASS
CodeQL                       = 33163171289 / PASS
```

Post-merge tree readback established that `releases/current/` on `main` is exactly `f33e73ed997c1b66a4572685ab5474182e136e97` and its top-level baseline identifies `v0.3.7 / CURRENT / FIELD_VALIDATION`.

## Candidate succession

Candidate succession remains stopped.

```text
candidate.4 required by current evidence = NO
attack cardinality                        = OPEN
```

Stopping candidate succession does not claim all possible failures are known. A successor candidate requires new material evidence that demands candidate-byte correction.

## Evidence boundaries preserved after release

Promotion does not establish:

- closed attack cardinality;
- external authenticity of represented Authority/credential/mandate data;
- external authenticity or exactly-once truth merely from represented Effect receipts;
- universal source authenticity from import/source-consistency checks;
- universal cross-environment candidate-id uniqueness absent governing contract evidence;
- natural future-session cue salience/application;
- universal Host applicability or fitness;
- universal English/zh-CN behavioral equivalence;
- normativity or required activation of bundled optional/default-off references.

These remain field/independent evidence boundaries rather than hidden release claims.

## Field-validation succession

A new active field stream was opened as Issue #150:

`ENA v0.3.7 field validation: Operational Architecture on heterogeneous Hosts`

Issue #70, the v0.3.6 field-validation stream, was commented with the succession identity and closed as completed predecessor lifecycle. Its contents remain occurrence evidence and closure must not be reinterpreted as proof that all v0.3.6 field questions were exhausted.

Open reconstruction/research issues #89–#94 and #104 remain open because their obligations remain meaningful. Open issue count is not a release quality metric.

## Immutable-package erratum

Post-merge inspection found one stale pre-promotion sentence inside the released `releases/current/CURRENT-BASELINE.yaml` `accepted_residuals`: it states that v0.3.6 remains the only adopter-facing baseline until explicit promotion.

That precondition is now false because explicit promotion occurred.

Classification:

`RELEASE_METADATA_ERRATUM / NOT_CANDIDATE_SEMANTIC_DEFECT / DO_NOT_MUTATE_RELEASED_V0_3_7_BYTES_IN_PLACE`

Reason: v0.3.7 Release Discipline establishes `same ena_version -> same effective content`. Silently editing the 118-file package after release would destroy the exact release identity and invalidate the published deterministic digest. Therefore the erratum is documented outside Current, surfaced in Issue #150, and reserved for correction under a future governed release identity.

The stale residual sentence does not override the top-level v0.3.7 Current identity or the governed promotion/readback evidence.

## Branch lifecycle after promotion

`research/ena-reconstruction` remains the sole active research continuation branch named by `research/ACTIVE-RESEARCH.yaml`.

The following branch classes have completed their active lifecycle once this post-promotion alignment is main-visible:

- `release/v0.3.7`;
- candidate.0/.1/.2/.3 branch refs;
- historical validation refs;
- pre/post-promotion integration refs;
- merged Selection Qualification control-fix ref;
- `tmp/noop-check*` operator-noise refs.

Durable lineage exists through exact Git objects, PRs, reconciliation records, handoff records, issues, sealed validation evidence, and history. The current GitHub connector exposes no genuine delete-ref write action, so these refs are classified for cleanup but are not force-moved to simulate deletion.

## Project State Alignment disposition

This promotion is a material transition, so current-tense project surfaces must be aligned from pre-promotion state to v0.3.7 Current. Alignment modifies project/control/history/routing surfaces only; the released `releases/current/` tree is intentionally unchanged.

After alignment merge/readback, the permitted work resumes at:

```text
Issue #150 field evidence
+ Issues #89-#94 / #104 unresolved reconstruction research
-> choose the next bounded decision-changing step
```

> Release closure is not research closure. Preserve one immutable Current, keep evidence boundaries visible, and let future variation be selected by reality rather than by ceremonial version churn.
