# ENA Research Methodology — Cardinality Discovery Guard

Status: `ACTIVE_WORKING_METHOD / ANTI_DISTORTION_GUARD / NOT_CURRENT`

Related: #89, PR #82, `ENA-RESEARCH-DISCIPLINE.md`, `HOW-GROWTH-DISCIPLINE.md`.

## Problem

Prompts, reports, reviews, taxonomies, and fixtures often request a fixed number of outputs:

```text
list 5 mechanisms
give top 10 findings
summarize into 3 points
provide 4 implementation options
```

That number may be a presentation preference rather than a property of reality.

If the requested number is treated as structural truth, two opposite distortions appear:

```text
reality has more materially distinct parts than requested
-> merge / omit / flatten until the quota is met
```

or:

```text
reality has fewer materially distinct parts than requested
-> split / pad / invent distinctions until the quota is met
```

Both are reality distortion.

## Core rule

> **Cardinality must be discovered when cardinality is itself an empirical or architectural question. Do not preallocate reality into prompt-sized slots.**

```text
REQUESTED_N != DISCOVERED_N
PRESENTATION_N != ONTOLOGY_N
CURRENTLY_OBSERVED_N != FINAL_N
```

A count is authoritative only when the domain itself makes it authoritative.

Examples include a protocol-defined signature count, an interface with a real fixed slot count, a benchmark with explicit top-k identity, an ordered generation number, or another contract/physical/statistical constraint.

Even then, the fixed count applies to that interface or contract, not automatically to the underlying world model.

## Research discipline

When reconstructing ENA mechanisms, properties, failure modes, categories, or HOW lineages:

- discover before counting;
- do not stop because a presentation quota is full;
- do not pad because a presentation quota is not full;
- do not merge solely to hit a smaller number;
- do not split solely to hit a larger number;
- treat current counts as provisional observations unless a real contract fixes them;
- allow new phenotype growth when Host evidence breaks an old taxonomy;
- allow contraction when function/decision parity evidence supports it.

## Taxonomy implication

The same guard applies to categories and organ boundaries.

```text
CURRENT_CATEGORY_SET != ONTOLOGY
CURRENT_TOPIC_BOUNDARY != NATURAL_ORGAN_BOUNDARY
WORKING_TAXONOMY != EXHAUSTIVE_PARTITION
ENUMERATION != COMPLETENESS_PROOF
```

For example, reconstruction workstreams #90–#94 are organizational shelves, not proof that ENA naturally contains exactly those systems.

## HOW plurality implication

```text
multiple HOWs are allowed
!= produce exactly N HOWs
```

The correct number of HOWs for a property may be one local winner, several complementary organs, many Host phenotypes, or an open-ended family.

Selection concerns fitness and applicability, not slot completion.

## Presentation vs discovery

A fixed-count presentation request is allowed if the full discovery state remains intact.

Safe sequence:

```text
unconstrained discovery
-> preserve full inventory
-> rank / cluster / select for presentation
-> disclose material grouping/omission when it matters
```

Do not rewrite the underlying research record to match the presentation count.

## Test and machine-contract guidance

Avoid accidental ontology locks such as:

```text
assert len(hows) == 4
```

unless `4` has real domain authority.

Prefer checks such as:

```text
every retained HOW has a distinct supported applicability/failure rationale
adding a new valid HOW does not invalidate existing valid HOWs
no HOW is required merely to satisfy a target count
grouping does not erase retained implementation behavior
```

A frozen benchmark may intentionally retain an exact case count for comparison identity. That count is evidence about the benchmark corpus, not about reality's ontology.

## Numeric pseudo-science guard

Do not manufacture scientific appearance through arbitrary thresholds such as:

- minimum Host count for maturity;
- arbitrary pass percentage for promotion;
- fixed days before a latent variation must be resolved;
- fixed number of successful runs as proof of stability;
- fixed reviewer/model count as proof of independence.

A number must answer:

> **What gives this number authority?**

Legitimate sources may include statistical/error models, cost/risk curves, external contracts, capacity limits, physical constraints, protocol identity, or other domain-authoritative meaning.

```text
COUNTABLE != SHOULD_BE_QUANTIFIED
NUMERIC != MEANINGFUL_MEASUREMENT
N_OUTPUTS != N_INDEPENDENT_SUPPORTS
```

## Compact rule

> **Numbers may constrain presentation. They must not silently constrain ontology.**

`CARDINALITY_DISCOVERY = ACTIVE`

`PROMPT_SLOT_COUNT != REALITY_STRUCTURE`

`NO_PADDING_FOR_SYMMETRY`

`NO_MERGING_FOR_QUOTA`

`CURRENT_MUTATION = NO`
