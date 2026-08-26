# Lineage Compaction × Retrieval Obligation Composition

Status: `RESEARCH_COMPOSITION_HARNESS / NOT_CURRENT / NOT_RELEASE_CANDIDATE`

Related:
- `research/prototypes/lineage-compaction-contract/`
- `research/prototypes/memory-metabolism/retrieval-obligation-0.5/`
- `research/reconstruction/PORTABLE-SNAPSHOT-LINEAGE-SURVIVAL-MAP.md`
- #90, #94, #104

## WHAT

Test the boundary between a structurally honest compact lineage representation and a material decision that actually needs cold lineage content.

The composition deliberately **reuses** two existing organs:

```text
Lineage Compaction Contract
-> says whether omitted material lineage is represented inline or bound to a cold identity

Retrieval Obligation 0.5
-> says whether decision-material retrieval of a specific effective result is current/sufficient
```

No new `Lineage Retriever` organ is introduced.

## WHY

A digest-bound cold reference can make compaction honest while the referenced bytes remain unavailable, stale, searched in the wrong scope, or replaced behind an alias.

Therefore:

```text
COMPACTION_VALID
!= COLD_LINEAGE_RETRIEVED

COLD_REF_PRESENT
!= RETRIEVAL_SUFFICIENCY_RESOLVED

RETRIEVAL_RECORD_ALIAS_MATCH
!= EFFECTIVE_CONTENT_IDENTITY_MATCH

SUMMARY_VALID
!= MATERIAL_USE_READY
```

## Composition rule under test

For a compact representation that returns:

`VALID_COMPACTION_REQUIRES_COLD_RESOLUTION_BEFORE_MATERIAL_USE`

the material decision becomes ready only when Retrieval Obligation represents a current material HIT for:

```text
record_ref == cold_lineage_ref.ref
AND
content_identity_ref == sha256:<cold_lineage_ref.digest>
```

and that HIT participates in a valid current `RETRIEVAL_SUFFICIENCY_RESOLVED` closure for a material READY decision.

A bounded `NO_HIT` can be a valid retrieval conclusion while still failing to resolve this cold lineage subject.

An unresolved decision-material Commitment remains a blocker even when all relevant lineage is inline.

## Deterministic cases

The authored corpus currently checks:

- full inline material lineage can be used without cold retrieval;
- cold ref alone is not material-use readiness;
- exact cold subject + exact content identity + current sufficiency closes readiness;
- wrong content with a fresh sufficiency closure does not resolve the expected cold subject;
- content changes after sufficiency invalidate the retrieval closure;
- wrong scope is invalid;
- bounded no-hit is not successful cold-lineage resolution;
- wrong record alias is not successful resolution;
- unresolved obligation remains a blocker;
- invalid compaction is rejected before retrieval.

Corpus cardinality is descriptive and open.

## Verification boundary

PASS means only that the represented cross-organ rules compose for the authored cases.

It does not prove:

- that the cold store is really available outside the represented retrieval;
- that a registry is complete/current;
- that `content_identity_ref` is truthful;
- that a Host classified materiality correctly;
- that source lineage was complete/authentic;
- that real-world state remained fresh.

## Structural conclusion

The reusable composition is:

```text
compact lineage
    |
    +-- complete inline material lineage
    |      -> material use may continue
    |
    +-- digest-bound cold lineage
           -> Retrieval Obligation
           -> scope discovery
           -> effective content identity
           -> current material sufficiency
           -> material use
```

This is evidence for **recombining existing organs** rather than proliferating a new retrieval subsystem.

`CURRENT_CHANGE = NO`
