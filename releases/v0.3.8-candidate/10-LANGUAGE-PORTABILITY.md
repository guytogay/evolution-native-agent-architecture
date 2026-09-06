# 10. Language Portability and Semantic Projection — v0.3.8-candidate.0

Status: `CANDIDATE / NOT_CURRENT / NOT_FROZEN / NOT_RELEASED / LANGUAGE_PROJECTION_RECONCILIATION`.

Released Current remains v0.3.7.

ENA must not depend on English proficiency to remain usable as ENA.

A language version is a **semantic projection** of one candidate/release identity, not a separate Constitution or a second machine implementation.

## 10.1 Stable identity and decision meaning

Across languages:

- inherited `ENA-CON-*`, `ENA-CAP-*`, contract/schema IDs remain stable unless a governed version change explicitly changes them;
- effective-content identity remains traceable;
- a projection declares source identity and language tag;
- wording may differ to preserve decision meaning;
- a shorter projection must not silently shrink decision-bearing applicability.

Literal translation is not the goal.

```text
TRANSLATE WORDING
PRESERVE DECISIONS
```

Representative high-risk distinctions include:

- `capability != authority`;
- `stimulus != mutation != improvement`;
- `stored != expressed != applied != selected`;
- `local selection != universal fitness`;
- `published/imported/source-supported != receiver-local selection`;
- `migration != local validation`;
- `cancel != rollback != compensation`;
- `restore/resume != complete history != restored authority`;
- `local validity/improvement != composed outcome`;
- `durable object exists != relevant bytes loaded != semantics available`;
- `bundled reference != required/default-active`;
- `cue match != applicability proven`;
- `being heard != sovereignty/authority`;
- `no incident != control not needed`.

## 10.2 Candidate projection manifest

The zh-CN projection declares candidate source identity, covered semantic/operational surfaces, machine-artifact policy, fixture sets, validation state, and known gaps in:

`language-projections/zh-CN/projection-manifest.yaml`

Candidate.0 is `NOT_CURRENT / NOT_FROZEN / NOT_RELEASED`; the projection must carry the same candidate identity and cannot self-promote.

If freeze later occurs, the projection must bind to the exact frozen candidate tree rather than a mutable branch name.

## 10.3 Decision-bearing projection

Chinese adopters should be able to reach the same decision-material surfaces without hidden English-only instructions.

The candidate includes zh-CN projection for the hot Runtime Kernel and the operational routing/HOW layer.

Root:

`language-projections/zh-CN/`

Operational root:

`language-projections/zh-CN/operational/`

Reference guide:

`language-projections/zh-CN/REFERENCE-GUIDE.md`

Issue #201 exposed that v0.3.7's Chinese hot surface omitted several English guardrails even though deeper prose retained some of them. Candidate.0 treats this as a projection defect to repair, not as permission to choose whichever wording is convenient.

## 10.4 One canonical machine surface

Candidate.0 intentionally does **not** translate every machine schema/tool/reference fixture into an independently evolving Chinese implementation.

```text
ONE_CANONICAL_MACHINE_SURFACE
+
MULTIPLE_SEMANTIC_USAGE_PROJECTIONS
```

Canonical machine bytes remain under `references/`, `schemas/`, `templates/`, and `tools/`.

This avoids two machine contracts drifting independently while still requiring language-facing decision semantics to remain usable.

## 10.5 Cross-language conformance

Validate **decision meaning**, not literary similarity.

Fixture sets:

- `semantic-fixtures.v1.yaml` — inherited v0.3.5 paired scenarios;
- `semantic-fixtures.v2.yaml` — inherited v0.3.6 ecology scenarios;
- `semantic-fixtures.v3.yaml` — inherited v0.3.7 operational cases plus v0.3.8-candidate.0 coverage additions.

The candidate v3 corpus now includes dedicated cases for:

- local vs universal fitness / moral correctness;
- composition/emergence;
- cancel vs rollback vs compensation;
- runtime availability vs salience/application;
- memory metabolism vs raw accumulation;
- projection/compaction with omitted material dependency;

in addition to inherited Retrieval, WAIT, Authority, Effect, Recovery, Continuity, Standing, Evidence dependency, Adoption, Migration, Control Retirement, and Authorship cases.

Fixture count is a corpus fact, not a completeness threshold.

Fixture presence/structure and route parity are not behavioral proof. Only observed paired model/Host/language behavior can support behavioral conformance claims.

```text
TRANSLATED != BEHAVIORALLY_EQUIVALENT
FIXTURE_DEFINED != MODEL_PASS
STRUCTURAL_PARITY != DECISION_PARITY
```

## 10.6 Local projection and applicability

Where language can materially affect interpretation, record as needed:

- operating/adoption language;
- projection identity;
- source semantic identity;
- model/Host/language combination;
- material limitations.

`same model != same semantic performance across languages`

Language change can be an applicability boundary for evidence when it can change a decision.

## 10.7 Enforcement and language

Language projection is not a hard security mechanism by itself.

`ENFORCEMENT-MAP.yaml` distinguishes:

- semantic/model cues;
- machine-guarded represented invariants;
- external controls required for outside-world truth/authority/effects;
- field evidence required for natural behavior.

A well-translated instruction still cannot authenticate an external credential or prove settlement truth.

## 10.8 Candidate evidence status

Candidate.0 has repaired identified hot-surface omissions and expanded paired fixtures, but it has **not yet** established natural bilingual behavioral equivalence.

Before freeze, targeted structural/semantic checks must verify at minimum:

- required zh-CN entry/hot/operational files exist;
- candidate status/identity is coherent;
- all expected v3 routes resolve in English and zh-CN surfaces;
- the Chinese Runtime Kernel retains the identified decision-bearing guardrails;
- machine-reference bytes remain single/canonical by policy;
- optional/default-off boundaries remain visible.

Fresh/field behavioral testing remains separate evidence.

> **语言是接口，不是 ENA 的身份。**
>
> **压缩文字，不压缩适用边界。**
