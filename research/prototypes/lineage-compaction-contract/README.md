# Decision-Material Lineage Compaction Contract

Status: `RESEARCH_PROTOTYPE / COMPACTION_CONTRACT / NOT_CURRENT / NOT_RELEASE_CANDIDATE`

Related:

- #89 reconstruction master;
- #94 evidence/applicability/adoption;
- #104 archaeology pass;
- `PORTABLE-SNAPSHOT-LINEAGE-SURVIVAL-MAP.md`;
- Evidence Dependency Map;
- Commitment/Settlement recovered reconstruction;
- migration-settlement composition harness.

## Purpose

Test whether a proposed compact representation preserves the parts of represented history whose omission can change a later decision.

This prototype does **not** prescribe a summarizer, token budget, storage engine, retention period, or one universal compaction format.

```text
COMPACTION_ALGORITHM != COMPACTION_CONTRACT
```

The contract evaluates an already-proposed compact representation against its represented source lineage.

## Trigger

Progressive projection and migration archaeology established:

```text
CURRENT_STATE_EQUIVALENCE != HISTORY_EQUIVALENCE
IMPORT_VALIDATOR != OMISSION_DETECTOR_WITHOUT_SOURCE_WITNESS
```

But preserving every historical byte forever would create another failure:

```text
UNBOUNDED_LINEAGE
-> context/storage/transfer cost
-> adoption and retrieval pressure
```

Therefore a viable architecture needs both:

```text
RETENTION + COMPACTION
```

without converting important history into false confidence.

## Decision-material classes exercised by the current corpus

The deterministic corpus currently exercises:

- negative evidence;
- unresolved obligations;
- terminal obligations and settlement evidence;
- evidence source roots;
- derived/copied evidence relationships;
- source authority history vs receiver authority;
- source-lineage digest binding;
- digest-bound cold lineage references.

This list is not exhaustive and is not an ontology.

## HOW branches preserved

### HOW-A — Inline decision-material summary

The compact representation carries the required negative lineage, unresolved obligation, terminal settlement evidence, and evidence-dependency structure directly.

Benefit: material decisions can often proceed without a second retrieval.

Cost: larger portable/hot representation.

### HOW-B — Digest-bound cold lineage reference

The compact representation keeps a reference + digest to the full represented lineage instead of inlining all decision-material details.

Benefit: smaller active/portable surface.

Critical boundary:

```text
COLD_REF_PRESENT != COLD_LINEAGE_RETRIEVABLE
SUMMARY_VALID != MATERIAL_USE_READY
```

If a later material decision depends on omitted cold lineage, the correct action is to resolve/retrieve it before continuing.

### HOW-C — Mixed projection

Some decision-material facts remain inline while larger/less-frequently-used lineage stays behind a digest-bound cold reference.

The current validator supports this shape without assuming it is universally optimal.

## Properties guarded

The prototype rejects compaction that:

1. drops represented decision-material negative evidence with no valid cold reference;
2. drops represented unresolved obligations with no valid cold reference;
3. summarizes SETTLED/CANCELLED obligations without settlement evidence;
4. hides known evidence source roots or `derived_from` dependency edges when claiming inline corroboration;
5. manufactures `independent_support_count` or `independence_score` from compressed evidence;
6. transforms source authority history into receiver authority;
7. presents a cold lineage digest that does not match the represented source lineage;
8. presents a compact summary whose source digest no longer matches after represented source mutation.

## Deterministic result

Current local corpus: 12 cases PASS.

The number `12` is only the size of this current deterministic corpus.

```text
12_CASES != 12_REALITY_CLASSES
12_CASES != MATURITY_THRESHOLD
12_CASES != INDEPENDENT_EVIDENCE_COUNT
```

## Verification boundary

A PASS establishes only that the compact representation satisfies the represented contract implemented here.

It does **not** prove:

- source lineage is complete or externally true;
- a cold reference remains reachable/retrievable;
- evidence sources are authentic;
- a dependency edge is causally complete;
- settlement evidence is externally authentic;
- source authority was legitimate;
- receiver authority exists;
- the chosen compaction is efficient or useful on a real Host.

## Current conclusion

```text
COMPACTED != DISPOSABLE
COLD_REF_PRESENT != RETRIEVABLE
SUMMARY_VALID != MATERIAL_USE_READY
SOURCE_AUTHORITY != RECEIVER_AUTHORITY
DEPENDENCY_VISIBILITY_MUST_SURVIVE_WHEN_DECISION_MATERIAL
```

A compact representation may be structurally valid while still requiring cold-lineage resolution before a material decision.

`CURRENT_CHANGE = NO`
