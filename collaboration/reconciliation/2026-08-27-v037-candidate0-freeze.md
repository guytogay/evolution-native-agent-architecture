# ENA v0.3.7 candidate.0 — Frozen candidate record

Status: `FROZEN_CANDIDATE_IDENTITY / EXTERNAL_RECORD / NOT_CURRENT / NOT_RELEASED / INDEPENDENT_FALSIFICATION_PENDING`

Date: 2026-08-27

## Freeze decision

This record assigns the frozen identity of **ENA v0.3.7 candidate.0** to an exact already-tested candidate subtree.

The candidate bytes are **not** rewritten to insert a post-hoc `frozen: true` marker. The authoritative freeze property is the external governed binding below.

```text
EXTERNAL_RECORD_BINDS_EXACT_IMMUTABLE_TREE
CANDIDATE_BRANCH != FROZEN_IDENTITY
FROZEN != RELEASED
FROZEN != CURRENT
```

## Exact frozen identity

Candidate identity:

`v0.3.7-candidate.0`

Candidate branch used during authoring:

`candidate/v0.3.7-candidate.0`

Exact frozen source commit:

`d0e793593184740d9732902e948afd48ed96ae2f`

Exact frozen candidate subtree:

`cffbf76fe1448b020b637c78d1f7ae46e4c0115b`

Candidate subtree path:

`releases/v0.3.7-candidate/`

Observed file count at pre-freeze validation:

`118`

The file count is descriptive evidence only. It is not the identity primitive and not a release threshold. The content-addressed source/subtree binding above is authoritative.

## Parent / Current boundary

Correct candidate birth base:

`0ad263178ab8b7c21c150012b3c06a5c41a4f41c`

Current remains:

`v0.3.6 / releases/current/ / CURRENT / FIELD_VALIDATION`

The frozen candidate does not alter, replace, or promote Current.

`CURRENT_CHANGE = NO`

## Exact pre-freeze machine evidence

Workflow:

`ENA v0.3.7 Candidate Exact Pre-Freeze Gate`

Run:

`33011823923`

Result:

`SUCCESS`

The workflow emitted:

```text
PREFREEZE_VERDICT=PASS
PREFREEZE_SOURCE_COMMIT=d0e793593184740d9732902e948afd48ed96ae2f
PREFREEZE_CANDIDATE_TREE=cffbf76fe1448b020b637c78d1f7ae46e4c0115b
PREFREEZE_CANDIDATE_FILE_COUNT=118
validation_scope=EXACT_REPRESENTED_CANDIDATE_MACHINE_PACKAGING_AND_AUTHOR_ATTACK_RECOMPOSITION
independent_semantic_support=NOT_ESTABLISHED
external_truth=NOT_ESTABLISHED
freeze_authority=NOT_ASSIGNED_BY_THIS_WORKFLOW
```

This external record, not the workflow itself, assigns the freeze identity after the exact workflow succeeded.

## What passed on the exact frozen bytes

The exact pre-freeze run recomposed the following on one source/tree rather than relying on green results from different historical heads:

- candidate baseline state and not-Current/not-frozen/not-released pre-freeze posture;
- `releases/current/` isolation;
- semantic-trunk preservation;
- 01–04 exact-byte parity with v0.3.6 Current;
- key v2 schema exact-byte parity with v0.3.6 Current;
- `05-CORE-OPERATIONAL-CONTRACTS.md` equality to Current except three explicitly allowed identity substitutions;
- Operational Architecture route-set integrity across Reference Index and English/zh-CN HOW maps;
- optional/default-off bundled-reference policy and Host-native equivalence;
- deferred Commitment/Settlement remains unbundled but preserved in lineage;
- inherited composed-validator selftest and regression corpus;
- v2 evolution-record validator selftest;
- candidate-local v2 helper selftest and real latent -> packet -> import CLI round trip;
- all eight bundled reference selftests;
- relocated legacy v1.2 tool selftest and candidate1/candidate2 historical adversarial regressions;
- phase-aware author adversarial suite on exact pre-freeze bytes;
- zh-CN operational projection and paired route fixtures;
- primary runtime/tool self-containment without `releases/current` or `research/` dependency in the v2 helper;
- all candidate Python compile;
- no candidate bytecode or symlink cargo;
- candidate subtree remained clean after validation;
- exact source/tree binding emitted by the workflow.

Observed inherited composed-regression corpus results included:

```text
migrated v0.3.2 selftests = 10/10
inherited corpus = 164/164
successor closure corpus = 61/61
unexpected verdicts = 0
uncaught exceptions = 0
```

Observed v2 evolution-record selftest count was `18` and candidate helper selftest count was `10`.

Observed candidate Python count was `24`, failures `0`.

These counts are occurrence/corpus facts, not ontological completeness claims or minimum release thresholds.

## Author-side falsification lineage before freeze

Durable author record:

`collaboration/reconciliation/2026-08-27-v037-candidate0-author-attacks.md`

Important real defects found and repaired before freeze included:

### A-01 — missing direct top-level Cue Index hop

The README described Operational Architecture but did not directly route an adopter to `operational/CUE-INDEX.md`.

Disposition: repaired before freeze.

### A-02 — Core Operational Contracts stale Current identity

Exact-byte preservation of `05-CORE-OPERATIONAL-CONTRACTS.md` accidentally preserved a false statement that the candidate-local file was the v0.3.6 Current active surface.

Disposition: repaired with only three identity substitutions, while machine-checking semantic-body parity.

Key lesson:

`SEMANTIC_PRESERVATION != IDENTITY_BYTE_PRESERVATION`

### A-03 — stale OA-EVO-01 tool state

The Reference Index still reported `ASSEMBLY_PENDING_STAGE_3` after the candidate-local v2 tool had already been assembled and machine checked.

Disposition: repaired to `ASSEMBLED_MACHINE_CHECKED_STAGE_3`.

### A-04 — legacy regression probes broken by tool relocation

Historical candidate1/candidate2 regression probes still referenced top-level `tools/ena_evolve.py` after the v1.2 tool was demoted to `tools/legacy/ena_evolve_v1_2.py`.

Disposition: both probes were relocated beside the legacy v1.2 tool and executed successfully in exact pre-freeze validation. Broken top-level copies were removed.

## Validation-oracle occurrence truth

Author-side validation itself also produced false positives that were corrected rather than hidden:

- predecessor Current wording was initially mistaken for candidate self-identity;
- an exact freeze slogan was initially required instead of the actual freeze property;
- the first author harness overused raw-token/stale-marker scanning and later falsely treated historical occurrence text as current structured state.

The author harness was therefore narrowed to structured current state and decision-bearing boundaries.

On the final pre-freeze run it reported:

```text
AUTHOR_ATTACK_VERDICT=PASS
observed_pass_conditions=188
attack_cardinality=OPEN
oracle_style=STRUCTURED_CURRENT_STATE_PLUS_DECISION_BOUNDARIES
independent_semantic_support=NOT_ESTABLISHED
external_truth=NOT_ESTABLISHED
```

`188` is a script expansion fact, not a completeness threshold. Reducing noisy assertions was an improvement in oracle quality, not a loss of rigor.

## First pre-freeze failure preserved

The first Exact Pre-Freeze Gate run:

`33011588278`

failed only when re-running the earlier phase-locked author harness after all preceding material pre-freeze checks had passed.

This failure is preserved as occurrence truth. It led to the phase-aware author harness used by the successful exact run `33011823923`.

## Frozen candidate thesis

The candidate preserves the v0.3.6 semantic trunk while adding a practical release-local Operational Architecture:

```text
HOT CUE
-> CUE-INDEX
-> HOW-MAP
-> REFERENCE-INDEX
-> bounded procedure / optional reference / Host-native HOW
-> ACT / WAIT / UNKNOWN / REFUSE / NOT_APPLICABLE
```

The candidate does not claim that every HOW is universal or that all bundled reference organs must be active.

```text
BUNDLED_REFERENCE != REQUIRED_FOR_COMPLETE_ADOPTION
BUNDLED_REFERENCE != DEFAULT_ACTIVE
REFERENCE_SCHEMA != NORMATIVE_ONTOLOGY
HOST_NATIVE_IMPLEMENTATION != NONCOMPLIANT
HOT_KERNEL != HOW_LIBRARY
```

No new Constitution ID is introduced by candidate.0.

`NEW_CONSTITUTION_IDS = 0`

No new Core semantic delta was demonstrated as necessary merely to create this candidate.

## Frozen residuals / claims that remain unproven

Freeze does **not** establish:

- external authority truth;
- receipt/effect/world-state truth;
- evidence/provenance authenticity;
- recovery reality;
- universal Host applicability of any bundled reference;
- natural fresh-session retrieval/salience of the correct HOW;
- English/zh-CN behavioral equivalence across models/Hosts;
- universal fitness of a local adaptation;
- independent semantic support for this candidate;
- release readiness or Current promotion.

Commitment/Settlement recovered reconstruction remains durable but unbundled in candidate.0 pending fresh independent review or renewed candidate-critical need.

`NOT_BUNDLED != RETIRED`

## Immutability rule from this point

The frozen identity is the exact source/subtree binding in this record.

Do **not** materially edit `releases/v0.3.7-candidate/` and continue calling the result candidate.0.

If fresh independent falsification finds a material defect requiring candidate-byte repair:

```text
candidate.0 remains frozen occurrence truth
-> create successor candidate identity
-> candidate.1 carries the repair
-> revalidate/freeze/review the successor
```

A branch ref moving later does not rewrite the frozen identity bound here.

## Next required phase

`FRESH_INDEPENDENT_SEMANTIC_FALSIFICATION`

The independent validator must inspect the exact frozen source/tree above and must not accept the candidate author's expected interpretations, author attack PASS, or package narrative as the test oracle.

Only after independent falsification may the project reconcile:

- material blockers;
- false positives from the falsifier;
- residuals;
- need for candidate.1 versus candidate-succession stop;
- release preparation versus rejection/defer.

```text
FREEZE = ASSIGNED
INDEPENDENT_FALSIFICATION = PENDING
RELEASE_DECISION = NOT_MADE
CURRENT_CHANGE = NO
```
