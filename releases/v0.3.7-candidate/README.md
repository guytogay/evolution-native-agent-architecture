# ENA v0.3.7 candidate.0 — Operational Architecture working candidate

Status: **WORKING_CANDIDATE / ASSEMBLY_IN_PROGRESS / NOT_CURRENT / NOT_FROZEN / NOT_RELEASED**

Current remains `v0.3.6 / CURRENT / FIELD_VALIDATION` under `releases/current/`.

Do **not** adopt this directory as Current while candidate assembly, author attacks, machine validation, freeze, and independent falsification are incomplete.

## Candidate thesis

v0.3.7 is being built as a practical Operational Architecture release rather than a manufactured Constitution expansion.

```text
v0.3.6 semantic trunk
+
concrete HOW navigation
+
optional reference organs
+
Host implementation patterns
+
minimal v2 practical tooling
+
operational zh-CN projection
```

No new Constitution ID is currently planned.

```text
NEW_CONSTITUTION_IDS = 0
NEW_CORE_SEMANTIC_DELTA_REQUIRED = 0_DEMONSTRATED
PRACTICAL_OPERATIONAL_RELEASE_VALUE = MATERIAL
```

## Why this candidate exists

v0.3.6 already carries strong WHAT/WHY semantics, but an adopter should not need repository archaeology or researcher memory to answer:

> What concrete mechanism can I use here, what are the alternatives, when does this mechanism not apply, and what evidence boundary remains?

The candidate therefore adds a release-local Operational Architecture layer while keeping the hot runtime surface small.

```text
HOT CUE
-> operational routing
-> plural HOW branches
-> procedure / optional reference / Host pattern
-> concrete action or honest WAIT / UNKNOWN / not-applicable
```

`HOW_LIBRARY_SIZE != ACTIVE_CONTEXT_SIZE`

## Working package layers

- semantic trunk — inherited from v0.3.6 unless a material contradiction is found;
- `operational/` — candidate-local cue/HOW/pattern/procedure navigation;
- `references/` — optional reference organs, never automatic runtime requirements;
- `tools/` — candidate-local practical v2 evolution path plus explicit legacy compatibility boundary;
- `language-projections/` — decision-bearing zh-CN operational projection target.

## Reference-library rule

A reference being bundled means only that ENA provides a concrete reusable implementation pattern.

```text
BUNDLED_REFERENCE
!= REQUIRED_FOR_COMPLETE_ADOPTION
!= DEFAULT_ACTIVE
!= UNIVERSALLY_APPLICABLE
!= NORMATIVE_ONTOLOGY
```

A Host-native implementation may satisfy the same operational property without instantiating the bundled reference schema.

## Assembly state

This first candidate commit is intentionally only a truthful shell.

`CANDIDATE-BASELINE.yaml` records exactly what is assembled and what remains pending. Some inherited semantic files still contain their v0.3.6 Current identity wording during Stage 1; therefore this subtree is **not freeze-ready**.

Freeze will be allowed only after:

1. operational cargo is self-contained;
2. selected reference paths exist and pass their machine tests;
3. the candidate-local v2 helper no longer depends on `releases/current/`;
4. zh-CN decision-bearing operational surfaces are present;
5. candidate identity wording is reconciled across the candidate subtree;
6. author adversarial checks and exact candidate validation pass.

## Lineage

Candidate branch:

`candidate/v0.3.7-candidate.0`

Correct candidate birth base:

`0ad263178ab8b7c21c150012b3c06a5c41a4f41c`

That main commit is the merged release-scope checkpoint where scope stability and version selection were already durable before candidate authoring began.

Branch mutability before freeze is workspace behavior. Frozen identity, if reached, will be the exact source commit + candidate subtree tree bound by an external freeze record.

> **Compress the semantic trunk; let concrete HOWs branch.**
>
> **Candidate assembly is not candidate proof.**
