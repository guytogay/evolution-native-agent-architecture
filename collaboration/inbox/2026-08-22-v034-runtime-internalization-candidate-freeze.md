# ENA v0.3.4 Runtime-Internalization Candidate — Semantic Freeze

Date: 2026-08-22

Status: `FROZEN_IMPLEMENTATION_CANDIDATE / AWAITING_FRESH_INDEPENDENT_VALIDATION / NOT_CURRENT / NOT_MAINLINE / NOT_PROMOTED`

## Frozen target

Repository:
`guytogay/evolution-native-agent-architecture`

Candidate path:
`releases/v0.3.4-candidate/`

Authoring branch:
`candidate/v0.3.4-runtime-internalization`

Frozen semantic candidate commit:
`ccc66233c1abe6778177a38950af1f7bb2356b93`

Frozen candidate-directory Git tree:
`61cb33562626c3b8f590919c87f4637416f1ee8f`

Parent Current/main observation used for authoring:
`43dac5c78b662f161e85f16143e05f64bdb5c2a5`

The freeze record is intentionally outside the candidate directory. Any later commit that adds this record or validation evidence does not change the frozen candidate unless the candidate-directory tree itself changes.

## Scope

This candidate is a focused successor to ENA v0.3.3 for issue #46:

`ADOPTION != RETRIEVAL`

It introduces an adoption/runtime model consisting of:

1. a compact Persistent ENA Runtime Kernel;
2. a reusable Compiled Local Projection;
3. canonical ENA text as a cold-path authority for novelty, ambiguity, stale reality, version change, or exact decision-critical semantics;
4. runtime profiles as governance intensity over one internalized ENA baseline rather than separate knowledge editions;
5. explicit persistent-self-mutation recovery reasoning;
6. an explicit no-real-task path that does not manufacture a production scenario.

The candidate deliberately does **not** change the Constitution, composed validator semantics, schemas, or inherited 235-case regression corpus.

## Exact candidate file set and Git object identities

The frozen candidate directory contains 30 files.

| Path | Git blob SHA |
|---|---|
| `00-READ-ME-FIRST.md` | `6ec722ce41a79b50dd1bdc2b3293ca58ceae116c` |
| `01-CONSTITUTION.md` | `92b564866b82d69fd24431e02e2294ee51bb079a` |
| `02-SELF-POSITIONING-AND-LOCAL-PROJECTION.md` | `7cb4c78ca95fcb3f568dfcb5ca9ffdef69f8e7ea` |
| `03-ROLES-AND-DEVELOPMENTAL-STAGES.md` | `8f2891641255318ddcba1c51ebcf9e00e0435f8b` |
| `04-CAPABILITY-MAP.md` | `7c3d2af8176b3ecd3bb74abc9f23abb4d89052ad` |
| `05-CORE-OPERATIONAL-CONTRACTS.md` | `be710c3e20eeda6a370219112023560f2ab446dd` |
| `06-EVOLUTION-KNOWLEDGE-AND-OPEN-PARTICIPATION.md` | `cff96f066092e222475c49af61e768a2095b71f0` |
| `07-ADOPTION-AND-FIELD-VALIDATION.md` | `6f1586cda493320ea34da1aaa9504cea5e2b8ad0` |
| `08-RELEASE-DISCIPLINE.md` | `a60ff817f5f589824fd8bbb9ecca6d2b406802bf` |
| `AGENT-ADOPTION-INSTRUCTION.md` | `ffab98eaee5a30f3effa72e1c70321a4072426eb` |
| `CANDIDATE-BASELINE.yaml` | `42a8148d059bd71760415f91336868918cc54029` |
| `CHANGELOG.md` | `0117f01d6df5abff04665315584c8ee1538c4d66` |
| `CONTRIBUTION-PROTOCOL.md` | `5e96b62d43764db23881a82549a405f443548ef3` |
| `LINEAGE.md` | `07b4c5efeb72015a8cb57b5ba88a88611532d5f1` |
| `LITE-ADOPTION-INSTRUCTION.md` | `80c96f58f52252ff1fc85ea7ea3d88693b53d2c3` |
| `README.md` | `cab10c82313441bcab25bc51be16c6066ef27a35` |
| `RUNTIME-ADOPTION-KERNEL.md` | `aaf0af1250fae22b91ee583bcb606f2ac3af723f` |
| `schemas/capability-route-binding.v1.schema.json` | `dcce1e07cc4cc01031bb0ddac1cc1a8fa7479358` |
| `schemas/claim.v1.schema.json` | `cde7d92a2e668a57cc5cee3a62843d1f747d0af4` |
| `schemas/composed-case.v1.schema.json` | `b6d745d58fafcea05b04c07ea86a80aa11283f1c` |
| `schemas/evidence-support-relation.v1.schema.json` | `79a043f97fdbcc9d452a460b7c7bcfa2f6a5f0f9` |
| `schemas/recovery-history-transition.v1.schema.json` | `29faa848ca3c9ade1236b2f84002935fb8d59049` |
| `schemas/triggered-obligation.v1.schema.json` | `b082b8d195b34f1660603ad54cb5b49cb9ae24b0` |
| `templates/field-experience.v1.yaml` | `c28d381bb641b8bac2a9676a1a98072b3c7ba051` |
| `tools/contract-fixtures.v1.json` | `797187e74dd3df2d9b754efc4f0beade42c3d7a8` |
| `tools/contract-fixtures.v2.1.json` | `38c1ec3add759b5b4f56ee927a48fe1c82eee122` |
| `tools/contract-fixtures.v2.json` | `f437f54d4803a7d17b100f039ee77b1f86cedff3` |
| `tools/regression-results-v033.json` | `3d635d4be2064d3345d279bd2713c00f79aa9710` |
| `tools/regression_suite.py` | `85208d67dfe238eda991ff023f97fc698f21f5c1` |
| `tools/validate_contracts.py` | `cef1b9b69a7b2fc0e38854d61e9076d87269347b` |

## Inherited exact-content checks

The following high-value inherited surfaces reuse the exact v0.3.3 Current Git blobs:

- Constitution;
- roles/developmental stages;
- capability map;
- core operational contracts and v0.3.3 composed validator contract;
- evolution/open-participation document;
- release discipline;
- all six schemas;
- field-experience template;
- all inherited validator/fixture/regression files.

Therefore this candidate does not claim a new composed-claim validation algorithm or schema vocabulary. Independent validation should still verify these identities rather than trusting this record.

## Package-digest status

No candidate ZIP/package SHA-256 is claimed by this freeze record.

`CANDIDATE-BASELINE.yaml` retains release-identity requirements such as package digest and exact package parity because any later promotion/release must satisfy them. This semantic freeze is source/tree evidence, not a published-release package claim.

Do not infer `package digest verified` from the Git tree identity.

## Required independent falsification focus

A fresh validator should try to break or contradict at least these claims:

1. **Persistent adoption cannot be self-declared.** Reading ENA in one session must not count as evidence that a genuinely fresh session will retain it.
2. **Profiles are runtime intensity, not knowledge editions.** LITE must not become a permanent knowledge ceiling.
3. **No per-task reread ritual.** Familiar low-consequence work should normally proceed without reopening canonical ENA after successful adoption.
4. **No convenience under-classification.** Governance cost must not be used as evidence that a consequential task is LITE.
5. **No fear-driven over-classification.** A small authorized reversible local side effect must not automatically become HIGH_ASSURANCE merely because it is an effect.
6. **Persistent self-mutation triggers recovery reasoning.** A durable Agent/runtime mutation should surface the real recovery boundary without a user reminder to "use ENA".
7. **Backup existence is not recovery proof.** Missing/untested restore capability must remain visible.
8. **Stale Local Projection must not be trusted silently** after material Host/runtime/model/tool/configuration/authority/recovery change.
9. **Canonical retrieval still has a job.** Novel/ambiguous/high-consequence or exact-contract cases must not be handled by confident local improvisation when the compiled semantics are insufficient.
10. **No-real-task onboarding must not manufacture positive field evidence.**

Also look for new false-confidence or false-block cases introduced by the runtime language itself.

## Actor separation

The authoring/reconciliation collaborator that produced this candidate is **not** an independent validator for it.

Expected next actor:
`FRESH_INDEPENDENT_RUNTIME_ADOPTION_VALIDATOR`

The validator must not accept this freeze record's interpretations as an oracle. It should inspect the frozen candidate directly and independently derive expected behavior before reading author conclusions where avoidable.

Final freeze state:

`FROZEN_IMPLEMENTATION_CANDIDATE / AWAITING_FRESH_INDEPENDENT_VALIDATION / NOT_CURRENT / NOT_MAINLINE / NOT_PROMOTED`
