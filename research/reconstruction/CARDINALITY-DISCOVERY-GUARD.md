# ENA Reconstruction — Cardinality Discovery Guard

Status: `RESEARCH_GOVERNANCE / ANTI_DISTORTION_GUARD / NOT_CURRENT`

Related: #89, #90, PR #82, Mechanism Retention Ledger.

## Problem

LLM prompts, reports, reviews, and test fixtures often request a fixed number of outputs:

```text
list 5 mechanisms
give top 10 findings
summarize into 3 points
provide 4 implementation options
```

That number may be a presentation preference rather than a property of reality.

If the requested number is treated as structural truth, two opposite distortions appear:

```text
reality has 8 materially distinct parts
-> prompt asks for 5
-> merge / omit / flatten until 5 remain
```

or:

```text
reality has 2 materially distinct parts
-> prompt asks for 5
-> split / pad / invent distinctions until 5 exist
```

Both are forms of reality distortion.

## Core rule

> **Cardinality must be discovered when cardinality is itself an empirical or architectural question. Do not preallocate reality into prompt-sized slots.**

```text
REQUESTED_N != DISCOVERED_N
PRESENTATION_N != ONTOLOGY_N
CURRENTLY_OBSERVED_N != FINAL_N
```

A count is normative only when the domain itself makes it normative.

Examples of legitimate fixed cardinality include:

- a protocol requires exactly two signatures;
- a schema defines exactly three states;
- a benchmark intentionally evaluates top-k retrieval;
- a UI has a hard bounded slot count.

Even then, the fixed count applies to that interface or contract, not automatically to the underlying world model.

## Reconstruction discipline

When reconstructing ENA mechanisms, properties, failure modes, or HOW lineages:

1. **Discover before counting.** Enumerate materially distinct items without targeting a preferred total.
2. **Do not stop because the prompt-sized quota is full.** If a sixth or eleventh material item appears, keep it.
3. **Do not pad because the quota is not full.** If two mechanisms are sufficient, keep two.
4. **Do not merge solely to hit a smaller number.** Merge only when the merged items are functionally or semantically equivalent enough that the merge preserves decision value.
5. **Do not split solely to hit a larger number.** Split only when the distinction changes behavior, evidence, applicability, failure mode, or selection.
6. **Treat counts as provisional observations.** `four HOWs exist today` must not become `the architecture has four HOW slots`.
7. **Allow new phenotype growth.** A fifth HOW appearing from Host evidence is not taxonomy failure; it may be evidence that the previous taxonomy was incomplete.
8. **Allow contraction.** If reality later shows that five categories reduce to two without function loss, contraction is valid only with parity evidence, not because a shorter list looks cleaner.

## Presentation vs discovery

A fixed-count user request can still be useful for communication. The safe sequence is:

```text
unconstrained discovery
-> preserve full inventory
-> rank / cluster / select for presentation
-> disclose that presentation is a projection when material items were omitted or grouped
```

For example:

```text
13 material findings discovered
-> user asks for top 5
-> present top 5 as a ranking/projection
-> do not rewrite the underlying record as if only 5 findings existed
```

Likewise:

```text
2 materially distinct causes discovered
-> user asks for 5 causes
-> report that only 2 are supported
-> do not manufacture 3 weak distinctions to satisfy format symmetry
```

## HOW plurality implication

HOW plurality is not a target count.

```text
multiple HOWs are allowed
!= produce exactly N HOWs
```

The correct number of HOWs for a property may be:

- one local winner;
- two complementary organs;
- five currently known phenotypes;
- an open-ended family.

The selection question is fitness/applicability, not slot completion.

## Test and machine-contract guidance

Avoid tests such as:

```text
assert len(hows) == 4
```

unless `4` is genuinely normative.

Prefer property tests such as:

```text
assert every retained HOW has a distinct supported applicability/failure rationale
assert adding a new valid HOW does not invalidate existing valid HOWs
assert no HOW is required merely to satisfy a target count
assert grouping does not erase retained implementation behavior
```

A benchmark may intentionally use top-k or bounded slots, but its evidence should not be narrated as proof that the underlying architecture has exactly k relevant items.

## Degradation alarms

Raise an explicit warning when any of these occurs:

- an unconstrained discovery task is rewritten as `find exactly N` for convenience;
- a list shrinks to N without a recorded reason for omitted/merged material items;
- a list grows to N through weakly differentiated padding;
- fixture expectations hard-code an accidental current count;
- documentation says `the N mechanisms` when evidence only supports `N mechanisms currently identified`;
- taxonomy symmetry is preferred over a real Host phenotype;
- a new category is rejected primarily because it breaks an existing count.

## Current field/reconstruction trigger

During finite-context adoption reconstruction, four HOW lineages had been developed. DSH field evidence did not fit those four without semantic distortion. Rather than forcing DSH into the closest existing bucket, reconstruction allowed a fifth lineage:

`HOW-E — Native Host Organ Rebind / Mapping-Only Adoption`.

This is a concrete example of the guard working as intended:

```text
observed phenotype breaks current count
-> expand model
not
observed phenotype breaks current count
-> compress phenotype
```

The same guard also permits the opposite result: if only two materially distinct mechanisms survive reality contact, do not preserve five merely because five slots once existed.

## Compact rule

> **Numbers may constrain presentation. They must not silently constrain ontology.**

`CARDINALITY_DISCOVERY = ACTIVE`

`PROMPT_SLOT_COUNT != REALITY_STRUCTURE`

`NO_PADDING_FOR_SYMMETRY`

`NO_MERGING_FOR_QUOTA`

`CURRENT_MUTATION = NO`
