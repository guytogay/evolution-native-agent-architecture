# v0.3.7 pre-promotion release-readiness alignment

Date: 2026-08-28

Status: `PREPROMOTION_ALIGNMENT / RELEASE_READY_EVIDENCE_RECORDED / NOT_CURRENT / NOT_PROMOTED`

## Purpose

This record closes the project-state drift created after candidate.3 freeze/hardening advanced into governed release packaging, release-control reconciliation, and exact-head validation while the main-visible control surfaces still described release identity transformation and the release PR as pending.

This alignment does **not** promote v0.3.7.

```text
ALIGNMENT_COMPLETE != RELEASE_AUTHORIZED
RELEASE_READY != CURRENT
GREEN_GATE != PROMOTION_AUTHORITY
```

## Current authority before promotion

Current remains singular on `main`:

```text
version  = v0.3.6
status   = CURRENT
maturity = FIELD_VALIDATION
tree     = 7dcbb3934883ffa6cc5292a662588cafc1533cff
```

Main observed immediately before this alignment branch was created:

`13c8a3e359fe6702ebc15dad982c655e2a3ca7a9`

That main commit includes PR #145, the Selection Qualification oracle-control correction, and does not change Current/candidate/release payload bytes.

## Frozen release source

```text
identity = v0.3.7-candidate.3
source   = b7e88d7adb70396bd671ca97066daf2c120e0adc
subtree  = e3a9a20d16cecd78df7f32f19fca56e21159e810
```

Evidence lineage:

- exact pre-freeze run `33150269264` — PASS;
- targeted post-freeze run `33150553992` — PASS;
- release hardening run `33152201566` — PASS;
- candidate succession — STOP;
- candidate.4 — not justified by current evidence;
- frozen candidate.3 mutation — forbidden.

## Release packaging lineage

The release sequence preserves two different occurrences:

1. byte-exact transplant of frozen candidate.3 into `releases/current/` at `8e4e25a8ba1940560fc55d7528ad31ef89a7f135`;
2. later release-only identity/status/adopter/Operational/zh-CN/reference-wrapper projection.

The prospective v0.3.7 Current payload now has:

```text
release branch           = release/v0.3.7
release PR               = #144 / OPEN DRAFT
promotion                = NOT AUTHORIZED / NOT STARTED
prospective Current tree = f33e73ed997c1b66a4572685ab5474182e136e97
Current file count       = 118
package SHA-256          = 40d4dde277d54ce8252e0402e32f900fa7ab4fb0aeaa638b898073d0f02f848c
```

The exact validated release head before this alignment is:

`bcda18a28141f572688f9a1b15cfd820dea02f97`

## Exact-head validation evidence

On that exact release head:

| Check | Result | Run |
|---|---|---:|
| ENA v0.3.7 Exact Release Gate | PASS | `33161514271` |
| Current validate/package | PASS | `33161516641` |
| Main Gate | PASS | `33161516581` |
| Selection Qualification Research | PASS | `33161516591` |
| research helper selftest | PASS | `33161516586` |
| CodeQL | PASS | `33161516568` |

The Exact Release Gate established, among other bounded claims:

- exact frozen source/tree binding;
- 50 non-projection frozen-byte parity checks;
- identity-only semantic projection boundary checks;
- 38 Constitution IDs and release-local relative-link integrity;
- evolution-record v2 selftest `35`;
- practical helper selftest `13`;
- inherited composed-valid corpus `164/164` with zero flips;
- successor closure corpus `61/61`;
- explicit legacy compatibility regressions;
- all 8 bundled optional-reference selftests;
- optional/default-off/non-normative reference packaging boundaries;
- English/zh-CN Operational routing structure;
- 24 Python files compile cleanly;
- deterministic exact-head 118-file package and readback parity.

The gate explicitly leaves these boundaries open:

```text
attack_cardinality = OPEN
external_truth = NOT_ESTABLISHED_BY_RELEASE_GATE
natural_host_salience = FIELD_EVIDENCE
host_applicability = FIELD_EVIDENCE
bilingual_behavioral_equivalence = FIELD_OR_INDEPENDENT_EVIDENCE
promotion_authority = NOT_ASSIGNED_BY_VALIDATION
```

## Selection Qualification oracle occurrence truth

PR #144 initially exposed a Selection Qualification failure. Inspection showed the 16-case reference rules themselves passed; the failing control treated `templates/evolution-record.v2.json` as an already instantiated machine-valid record even though candidate.1 had intentionally established:

```text
TEMPLATE != INSTANTIATED_RECORD
REPLACE_WITH_RFC3339_TIMESTAMP = deliberate uninstantiated placeholder
```

The failure was classified as:

`RESEARCH_ORACLE_DRIFT / NOT_CANDIDATE_DEFECT`

The control was repaired in PR #145 at exact head `38088150f03b91534b33f24375407741540dfb16`, merged to main at `13c8a3e359fe6702ebc15dad982c655e2a3ca7a9`, and synchronized into the release branch through PR #146. No candidate or prospective Current payload bytes were changed by that correction.

## Exact Release Gate trigger correction

A second release-control issue was found: the workflow named `ENA v0.3.7 Exact Release Gate` originally had a `paths:` restriction that caused automatic push execution only when the workflow file itself changed.

That was incompatible with an exact-head gate because later release-head changes could otherwise inherit an older green run.

The release control was corrected so every push to `release/v0.3.7` runs the exact gate. The correction produced release head `bcda18a28141f572688f9a1b15cfd820dea02f97`; the prospective Current tree remained `f33e73ed997c1b66a4572685ab5474182e136e97`, and the exact gate then passed on that head.

## Open issue disposition

Eight open issues were live during this alignment.

### Keep open while their research obligations remain meaningful

- #89 — whole-system reconstruction umbrella;
- #90 — architecture and decision lineage;
- #91 — test/self-hosting/operational execution model;
- #92 — contributor/adoption/public usability contract;
- #93 — governance/versioning/maturity/release discipline;
- #94 — research collaboration/external insight provenance;
- #104 — archaeology/drift/preserved variation recovery.

These are durable research/work trackers. Open issue count is not a release quality metric, and they are not release blockers merely because they remain open. Their references to Current/release phase must be aligned after promotion where necessary.

### Version-bound field stream

- #70 — v0.3.6 FIELD_VALIDATION ecosystem/runtime discovery stream.

Disposition: do not close merely to prepare release. After v0.3.7 promotion, supersede, retitle, or reframe it so the canonical field-validation stream cannot be mistaken for the new Current version.

## Branch disposition

Branch state and issue state have different semantics.

```text
OPEN_RESEARCH_ISSUE = durable unresolved work/research obligation
SHORT_LIVED_BRANCH = temporary isolation mechanism
```

### Keep through the next release transition

- `main` — permanent project control plane;
- `research/ena-reconstruction` — active research continuation surface while named by `research/ACTIVE-RESEARCH.yaml`;
- `release/v0.3.7` — active packaging/promotion surface until promotion/readback closes;
- `candidate/v0.3.7-candidate.3` — exact frozen-source locator through promotion and post-merge release-lineage readback;
- `integration/v037-prepromotion-alignment` — temporary until this alignment is merged/read back.

### Clear deletion candidates once a real delete-ref action is available

- `research/selection-qualification-v037-template-oracle-fix` — merged PR #145, durable lineage already on main/PR/reconciliation;
- `tmp/noop-check`;
- `tmp/noop-check-2`.

The tmp refs are operator noise/non-authority and have exhausted their purpose.

### Require one more durable-lineage confirmation before deletion is classified as safe

- candidate.0, candidate.1, candidate.2 branch names;
- historical/invalidated validation branch names for candidate.0/.1/.2.

Their branch names are not long-term archives, but deletion should follow exact confirmation that their decision-relevant occurrence truth is reachable through immutable commits/trees, PRs, freeze/reconciliation records, validation reports/seals, and Git history.

### Connector capability boundary

The currently available GitHub connector exposes branch creation/movement but no genuine branch/ref deletion operation. Therefore:

- no branch is claimed deleted in this alignment;
- force-moving refs is **not** an acceptable substitute for deletion;
- cleanup disposition is persisted so a later repository-maintenance action can delete only refs whose lifecycle is actually closed.

## Pre-promotion alignment decision

The project is release-ready in the bounded engineering/evidence sense represented above, while remaining explicitly not promoted.

The first permitted next sequence after this record and companion state projections reach `main` is:

```text
merge pre-promotion alignment to main
-> sync aligned main into release/v0.3.7
-> rerun exact release + ordinary PR gates on resulting exact release head
-> prove prospective Current tree/package digest stability
-> present exact reviewed head + residual evidence boundaries
-> obtain explicit promotion authorization
```

Only after explicit promotion authorization may PR #144 merge.

After merge, the project must independently read back Current from `main`, align Current metadata/history/issue routing/branch lifecycle/handoff surfaces, and run the Project State Alignment Gate again.

## Bottom line

```text
v0.3.7 RELEASE PAYLOAD = READY FOR FINAL PREPROMOTION REBIND + EXACT-HEAD REVIEW
v0.3.7 CURRENT = FALSE
PROMOTION AUTHORIZED = FALSE
CANDIDATE4 REQUIRED = FALSE BY CURRENT EVIDENCE
ATTACK CARDINALITY = OPEN
```
