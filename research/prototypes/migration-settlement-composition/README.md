# Migration Projection × Commitment/Settlement composition harness

Status: `RESEARCH_COMPOSITION_HARNESS / SOURCE_AWARE_PROJECTION / NOT_CURRENT / NOT_RELEASE_CANDIDATE`

Related: #91, #104, `PORTABLE-SNAPSHOT-LINEAGE-SURVIVAL-MAP.md`, progressive evolution-record prototype.

## Trigger

Current v0.3.6 adaptation packets preserve substantial source history, but local evolution records can contain `triggered_obligation_refs` while the portable packet has no first-class obligation/settlement carrier.

The first question is **not** "which new packet field should be added?"

It is:

> At what boundary can omission of decision-material obligation lineage actually be detected?

## Static result

A receiver that sees only the already-projected packet cannot infer a source obligation that was completely omitted.

```text
IMPORT_VALIDATOR
!=
OMISSION_DETECTOR_WITHOUT_SOURCE_WITNESS
```

Therefore at least one viable HOW must make the projection/export step accountable to source material.

## Harness HOW branches

The source-aware harness compares:

1. **bare packet** — demonstrates packet-only false-OK epistemic limit;
2. **raw source ref** — preserves that a source reference existed, but cannot self-assert receiver resolution;
3. **source obligation shadow** — preserves unresolved state without minting local authority/executor ownership;
4. **typed Commitment/Settlement carrier** — composes evolution migration with a separate commitment organ;
5. **source/projection digest witness** — binds the tested source record and portable packet so post-projection mutation is detectable within represented inputs.

The harness deliberately does not declare any branch universally superior.

## Deterministic findings

- packet-only import can appear plausible while source obligation lineage is absent;
- source-aware projection can reject omission;
- raw refs preserve occurrence but not resolvability;
- source shadow cannot create receiver authority/executor ownership;
- an OPEN typed commitment survives migration but still requires receiver WAIT/NARROW/local rebind;
- a typed commitment that is already SETTLED with represented evidence need not remain an active blocker;
- source/packet digest mismatch is detectable in the represented projection witness.

## External HOW relatives

Current external provenance/tracing systems provide related mechanisms:

- **in-toto Statement** binds attestations to immutable subjects by digest and allows typed predicates/referenced documents;
- **OpenTelemetry Span Links** preserve causal relationships that do not fit a single parent tree, including asynchronous/batch/fork-join relationships.

These are mechanism relatives, not evidence that ENA should copy their schemas.

## Verification boundary

This harness does not authenticate:

- source record truth;
- commitment carrier authenticity;
- counterparty acceptance;
- transfer authority;
- receiver authority;
- external settlement.

It only tests represented omission/survival and conservative receiver behavior.

`CURRENT_CHANGE = NO`
