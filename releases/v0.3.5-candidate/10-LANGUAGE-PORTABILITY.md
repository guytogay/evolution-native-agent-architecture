# 10. Language Portability and Semantic Projection

ENA must not depend on English proficiency to remain ENA.

A language version is a **semantic projection** of one ENA semantic identity, not a separate Constitution.

## 10.1 Stable identity

Across languages:

- `ENA-CON-*`, `ENA-CAP-*`, contract/schema IDs remain unchanged;
- canonical effective-content identity remains traceable;
- a projection declares its source identity and language tag;
- translated wording may differ to preserve meaning.

Literal translation is not the goal.

Example:

`capability != authority`

A literal Chinese phrase such as `能力 ≠ 权威` can be misleading.

A better semantic rendering is:

`有能力做到某件事 ≠ 被授权可以这样做`

## 10.2 Projection manifest

A language projection should declare:

- language tag;
- source ENA candidate/release identity;
- projection version;
- covered files/concepts;
- untranslated/partial areas;
- glossary version/identity where used;
- structural validation status;
- behavioral semantic-conformance status.

A projection is stale when its relevant source semantics changed and it has not been reconciled.

Do not label a projection behaviorally validated merely because the files parse or the Constitution IDs line up.

## 10.3 Semantic glossary

High-risk terms should have:

- stable concept key;
- preferred rendering;
- operational definition;
- common misleading renderings where useful;
- related ENA IDs.

Do not rely on one-word dictionaries for terms such as:

`agency | authority | mandate | evidence | support | recovery | rollback | compensation | variation | adaptation | evolutionary subject | protected subject | emergence`

## 10.4 Cross-language conformance

Validate **decision meaning**, not literary similarity.

Use equivalent scenarios in multiple languages and compare whether the model preserves material judgments such as:

- capability versus authority;
- internal permission mutation versus external mandate;
- variation versus improvement claim;
- UNKNOWN versus bounded experiment;
- claim/evidence/support;
- recovery/history/privacy;
- migration/local applicability;
- composition/emergence;
- continuity;
- governance closure.

This candidate includes paired English/zh-CN fixtures in:

`language-projections/semantic-fixtures.v1.yaml`

The file states expected semantic properties and related stable Constitution IDs. CI can verify fixture structure and pairing. **Only an actual model/Host/language experiment can provide behavioral conformance evidence.**

Back-translation may help review but is not sufficient proof.

## 10.5 Local Projection

Where language can materially affect interpretation, record:

- operating/adoption language;
- projection identity;
- source semantic identity;
- model/Host/language combination;
- material semantic limitations.

`same model != same semantic performance across languages`

Language change can be an applicability boundary for evidence when it can change a decision.

## 10.6 Supported candidate projections

This candidate ships:

- canonical English source;
- Simplified Chinese (`zh-CN`) hot-path projection.

The Chinese hot-path projection is intentionally smaller than the entire canonical package. Exact cold-path semantics remain reachable by stable IDs.

Current candidate evidence distinguishes:

- **structural parity** — file/ID/manifest/fixture structure can be mechanically checked;
- **behavioral semantic conformance** — remains unproven until exercised by a model across the paired language fixtures or equivalent real tasks.

> **Translate wording; preserve decisions.**
>
> **Language is an interface, not ENA's identity.**
