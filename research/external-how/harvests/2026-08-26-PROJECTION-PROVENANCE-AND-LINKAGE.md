# External HOW Harvest — Projection Provenance and Non-Tree Linkage

Date: 2026-08-26

Status: `EXTERNAL_HOW_HARVEST / RESEARCH_INPUT / NOT_SELECTION / CURRENT_UNCHANGED`

Trigger: #104 recovered variation archaeology and the migration × Commitment/Settlement composition seam.

## Problem being searched

A receiver cannot discover decision-material lineage that a source projection omitted completely.

```text
IMPORT_VALIDATOR
!=
OMISSION_DETECTOR_WITHOUT_SOURCE_WITNESS
```

Search target: mature mechanisms that bind a derived/projection artifact to source identity or preserve causal relationships that do not fit a single parent/current-state snapshot.

## in-toto Attestation Framework — subject digest + typed predicate/reference

Source class: `OPEN_SUPPLY_CHAIN_PROVENANCE_SPECIFICATION`

Sources:

- https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md
- https://github.com/in-toto/attestation/blob/main/spec/predicates/reference.md

Observed mechanisms:

- a Statement identifies the artifact(s) the attestation applies to as `subject` resources bound by digest;
- predicate type is explicitly identified rather than leaving one untyped metadata bag;
- predicate content can carry the specialized claim/evidence model;
- reference predicates can link additional evidence/documents by resource descriptors/digests rather than embedding everything into the subject artifact.

ENA mapping:

```text
source/projected subject identity
+ typed lineage predicate/carrier
+ digest-bound references
```

This is a concrete precedent for a **projection witness / typed lineage carrier** family.

Important boundary:

A digest binds represented bytes/identity; it does not prove source truth, authority, settlement, or completeness. A dishonest source can still omit a lineage class before attesting. Therefore source-aware export rules remain necessary.

Selection state: `RETAIN_AS_MECHANISM_RELATIVE / DO_NOT_COPY_SCHEMA`.

---

## OpenTelemetry — Span Links for causal relationships outside one parent tree

Source class: `OPEN_OBSERVABILITY_SPECIFICATION`

Sources:

- https://opentelemetry.io/docs/specs/otel/overview/
- https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/trace/api.md

Observed mechanisms:

- a Span can record zero or more links to causally related SpanContexts;
- links can cross trace boundaries;
- links model relationships such as batch/fan-in/fork-join where forcing one parent would be semantically wrong;
- link attributes can describe the relationship without changing the linked span's identity.

ENA mapping:

Some ENA lineage is not a strict ownership tree:

- one portable adaptation can depend on multiple evidence roots;
- a receiver result can relate to source history without becoming a child proof;
- one current projection may aggregate multiple causal occurrences;
- fork/recombine/settlement relations may require cross-links rather than pretending there is one canonical parent.

Candidate HOW role:

`NON_TREE_LINEAGE_LINK` as one optional representation pattern beneath Evidence Dependency / migration lineage / recombination.

Important boundary:

OpenTelemetry links represent causal association, not independent evidence, authority, obligation transfer, or settlement.

Selection state: `RETAIN_AS_MECHANISM_RELATIVE / DEPENDENCY_NOT_AUTHORITY`.

---

## Recombination implication for ENA

The external mechanisms support a plural family rather than one universal capsule schema:

```text
HOW-A  projection witness binding source + projected artifact digests
HOW-B  typed sidecar/attestation carrier for decision-material lineage
HOW-C  digest-bound reference to separately governed carriers
HOW-D  non-tree causal/dependency links when one parent relation is false
HOW-E  receiver WAIT/NARROW when referenced lineage cannot be resolved
```

The missing property is not "use in-toto" or "use OpenTelemetry".

The decision question is:

> Which lineage can change a target decision, and what is the cheapest truthful carrier that preserves it without minting new authority/evidence maturity?

`CURRENT_CHANGE = NO`
