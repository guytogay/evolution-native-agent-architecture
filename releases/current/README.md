# ENA v0.3.7 candidate.3 — Operational Architecture successor candidate

Status: **WORKING_CANDIDATE / REPAIR_RECONCILED / EXACT_PREFREEZE_NEXT / NOT_CURRENT / NOT_FROZEN / NOT_RELEASED**

The active adopter baseline remains `releases/current/` = `v0.3.6 / CURRENT / FIELD_VALIDATION`.

Do **not** adopt this directory as Current. Candidate.3 successor repairs are reconciled; exact pre-freeze validation is next, followed only on PASS by external freeze and explicit post-freeze independence/release reconciliation.

## Candidate thesis

v0.3.7 is a practical Operational Architecture candidate, not a manufactured Constitution expansion.

```text
v0.3.6 semantic trunk
+
concrete HOW navigation
+
optional reference organs
+
Host implementation patterns
+
candidate-local minimal v2 tooling
+
decision-bearing zh-CN operational projection
```

```text
NEW_CONSTITUTION_IDS = 0
NEW_CORE_SEMANTIC_DELTA_REQUIRED = 0_DEMONSTRATED
PRACTICAL_OPERATIONAL_RELEASE_VALUE = MATERIAL
```

## Minimum adopter traversal

A reviewer/adopter should not need to inspect `research/` to reach a usable mechanism.

```text
00-READ-ME-FIRST.md
-> RUNTIME-ADOPTION-KERNEL.md
-> operational/CUE-INDEX.md
-> operational/HOW-MAP.md
-> operational/REFERENCE-INDEX.yaml
-> bounded procedure / optional reference / Host pattern
-> action / WAIT / UNKNOWN / REFUSE / NOT_APPLICABLE
```

For the rationale and package boundary of this layer, see `operational/README.md`.

The HOW library is cold capability, not mandatory active context.

`HOW_LIBRARY_SIZE != ACTIVE_CONTEXT_SIZE`

## What is now assembled

### Operational routing

`operational/CUE-INDEX.md` is the ordinary-problem router. `operational/HOW-MAP.md` preserves plural concrete implementation branches. `operational/REFERENCE-INDEX.yaml` binds those branches to exact candidate-local procedures, references, and patterns.

```text
ordinary cue / failure / decision
-> consequence-first routing
-> CUE-INDEX
-> HOW-MAP
-> REFERENCE-INDEX
-> bounded procedure / optional reference / Host pattern
-> action / WAIT / UNKNOWN / REFUSE / NOT_APPLICABLE
```

### Optional reference library

Selected reusable references are bundled under `references/` with machine-readable policy in `references/REFERENCE-MANIFEST.yaml`.

```text
BUNDLED_REFERENCE
!= REQUIRED_FOR_COMPLETE_ADOPTION
!= DEFAULT_ACTIVE
!= UNIVERSALLY_APPLICABLE
!= NORMATIVE_ONTOLOGY
```

A Host-native implementation may satisfy the same property without instantiating the bundled schema.

### Evolution tooling

Primary candidate practical path:

`tools/ena_evolve_v2.py`

It provides a narrow candidate-local v2 path for latent records and packet-v2 export/import/validation. It delegates record semantics to the candidate-local v2 validator rather than implementing a second semantic engine.

The inherited v1.2 tool is retained only as:

`tools/legacy/ena_evolve_v1_2.py`

It is compatibility history, not an equally prominent default.

### zh-CN operational projection

Decision-bearing operational surfaces are available under:

`language-projections/zh-CN/operational/`

Machine reference bytes remain single/canonical; Chinese adopters use `language-projections/zh-CN/REFERENCE-GUIDE.md` rather than a second translated machine implementation.

`language-projections/semantic-fixtures.v3.yaml` defines paired candidate operational decision expectations. Fixture structure is machine-checked; natural bilingual behavior remains field/independent evidence.

## Machine assembly evidence

Stage 3 exact head `8ba109528ecb14f9a22a372c897ac8d9ea1759f3` passed Assembly Gate run `33004330491`.

Stage 4 exact head `7a59ac9b10e18f804ce7141b0beae2aef5e75cf6` passed Assembly Gate run `33007647412`, including zh-CN operational-route checks.

Machine PASS establishes exercised represented consistency and packaging facts. It does not establish external truth, universal Host applicability, future salience, or independent semantic support.

## Deferred without ablation

The recovered Commitment/Settlement machine prototype remains durable research lineage but is not bundled in candidate.3; deferral remains reversible if renewed candidate-critical evidence warrants it.

```text
NOT_BUNDLED != RETIRED
SILENT_DISSOLUTION != EVIDENCE_BACKED_RETIREMENT
```

## Lineage

Candidate branch:

`candidate/v0.3.7-candidate.3`

Exact candidate.3 birth base / predecessor frozen source:

`bda470e0a6b170cec61225a905957a501454a2fe`

Predecessor frozen candidate.2 subtree:

`d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`

Candidate.3 was created directly from frozen candidate.2 after candidate.2 fresh A-S/A-P and Phase B required a material successor. Candidate.2 remains immutable occurrence truth; candidate.3 does not rewrite it.

Round-1 successor repair gate `33149597432` passed and committed bounded Authority, Effect Lifecycle, transferred-source chronology, and regression-provenance repairs at `55e08740fa2e4b033cfb5bd9e8f7a4214a479f08` while preserving inherited valid behavior.

## What remains before freeze

1. finish candidate.3 package identity/lineage/zh-CN reconciliation without expanding executable semantic scope;
2. rerun inherited/targeted machine checks without treating their counts as completeness;
3. run exact-head candidate.3 pre-freeze machine validation;
4. bind the exact immutable source/tree with an external governed freeze record;
5. targeted post-freeze reconciliation must verify the sealed candidate.2 blockers are closed; another full fresh A-S/A-P cycle is not automatic;
6. if no material blocker remains, perform explicit v0.3.7 release reconciliation and promotion decision.

Any material correction after freeze requires a successor candidate identity.

> **Compress the semantic trunk; let concrete HOWs branch.**
>
> **Assembled is not independently supported.**
