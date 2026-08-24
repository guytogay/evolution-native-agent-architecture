# 10. Language Portability and Semantic Projection — v0.3.6 Current

ENA must not depend on English proficiency to remain ENA.

A language version is a **semantic projection** of one release semantic identity, not a separate Constitution.

## 10.1 Stable identity

Across languages:

- inherited `ENA-CON-*`, `ENA-CAP-*`, contract/schema IDs remain unchanged unless a governed version change explicitly changes them;
- release effective-content identity remains traceable;
- a projection declares source identity and language tag;
- wording may differ to preserve decision meaning.

Literal translation is not the goal.

Example:

`capability != authority`

A literal Chinese `能力 ≠ 权威` is weaker/ambiguous. Prefer the operational meaning:

`有能力做到某件事 ≠ 被授权可以这样做`

v0.3.6 adds additional high-risk distinctions such as:

`stimulus != mutation != improvement`

`stored != expressed != applied != selected`

`ARCHIVED/RETIRED != selection verdict`

`local selection != universal fitness`

`published != imported != locally selected`

These require semantic projection, not word substitution.

## 10.2 Projection manifest

A language projection declares:

- language tag;
- source release identity;
- projection version;
- covered files/concepts;
- untranslated/partial areas;
- glossary identity;
- structural validation status;
- behavioral semantic-conformance status.

The zh-CN projection shipped with Current is bound to v0.3.6 release semantics. A projection becomes stale when material source semantics change without reconciliation.

## 10.3 Semantic glossary

High-risk terms should carry an operational definition rather than rely on one-word dictionaries.

v0.3.6 glossary adds/clarifies:

`stimulus | mutation pressure | latent variation | expression | local selection | Evolution Commons | rescue plane | canonical lineage`

English terms may remain alongside Chinese where that reduces semantic drift, but Chinese users/Agents should not be forced to reason in English to access ENA meaning.

## 10.4 Cross-language conformance

Validate **decision meaning**, not literary similarity.

Included fixtures:

- `language-projections/semantic-fixtures.v1.yaml` — inherited v0.3.5 paired scenarios;
- `language-projections/semantic-fixtures.v2.yaml` — v0.3.6 ecology paired scenarios.

v2 covers:

- stimulus not automatically causing mutation/improvement;
- legitimate latent variation;
- stored not equal expressed;
- local selection not universal fitness;
- publisher/receiver autonomy;
- rescue not sovereignty;
- canonical lineage not self-declared Current;
- minimal intervention not externality waiver.

Fixture presence/structure is not behavioral proof. Only actual paired model/Host/language experiments provide such evidence.

## 10.5 Local Projection

Where language can materially affect interpretation, record:

- operating/adoption language;
- projection identity;
- source semantic identity;
- model/Host/language combination;
- material limitations.

`same model != same semantic performance across languages`

Language change can be an applicability boundary for evidence when it can change a decision.

## 10.6 Current projection status

v0.3.6 Current includes:

- canonical English authoring source;
- Simplified Chinese (`zh-CN`) hot-path projection;
- aligned glossary;
- inherited v1 and v0.3.6 v2 semantic fixture sets.

The predecessor v0.3.5 same-model 8/8 bilingual result remains predecessor evidence only; it does not prove v0.3.6 ecology semantics.

Current v0.3.6 behavioral semantic conformance: **UNPROVEN / FIELD EVIDENCE REQUIRED**.

> **Translate wording; preserve decisions.**
>
> **语言是接口，不是 ENA 的身份。**
