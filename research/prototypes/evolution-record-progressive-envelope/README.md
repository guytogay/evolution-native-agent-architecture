# Progressive Evolution-Record Envelope Prototype

Status: `RESEARCH_PROTOTYPE / STATIC_FALSIFICATION / NOT_CURRENT / NOT_RELEASE_AUTHORITY`

Related:

- #104 archaeology tracker;
- `research/reconstruction/RECOVERED-VARIATION-MAP.md` RV-002 / RV-004;
- `research/reconstruction/EVOLUTION-RECORD-PROGRESSIVE-REPRESENTATION-ANALYSIS.md`;
- `research/external-how/harvests/2026-08-26-PROPORTIONAL-RECORD-AND-EXTENSION-SURFACES.md`.

## Purpose

Test a concrete HOW family in which evolution occurrences are recorded progressively, then projected into a current v2-style aggregate view.

This prototype does **not** claim that event sourcing should replace the current v2 record. It is designed to falsify or expose composition boundaries that are difficult to see when occurrence history, current state, portable snapshot, and Host-local metadata are fused together.

Working decomposition:

```text
occurrence/event layer
        |
        v
projector / resolver
        |
        +--> current v2-style aggregate projection
        +--> occurrence-history digest
        +--> Host extension sidecar
        +--> unresolved projection residuals
```

## Recombined source mechanisms

This HOW did not appear from nowhere. It recombines:

1. the existing v0.3.6 aggregate schema with appendable history arrays;
2. the inherited `ena_evolve.py` internal operation-event log;
3. ENA Memory Metabolism's occurrence-vs-derived distinction;
4. external patterns such as CloudEvents core/extensions, OpenTelemetry events, and Agent trace/span systems.

```text
EXTERNAL_PATTERN != ENA_AUTHORITY
RECOMBINATION != SELECTION
```

## Prototype contract

Input document:

```json
{
  "candidate_id": "var-...",
  "events": [
    {
      "event_id": "evt-...",
      "event_seq": 1,
      "type": "CANDIDATE_CREATED",
      "occurred_at": "...",
      "payload": {},
      "extensions": {}
    }
  ]
}
```

Rules explored here:

- event IDs must be unique;
- `event_seq` must strictly increase in the supplied stream;
- exactly one `CANDIDATE_CREATED` occurrence establishes explicit initial Core state;
- no hidden default mints lifecycle/expression/selection truth;
- known mapped events may update the Core projection;
- unknown non-Core events remain in occurrence history as projection residuals;
- an unknown event that claims to affect Core is rejected until an explicit mapper exists;
- Host extensions are preserved in a sidecar and do not automatically alter the Core projection;
- a latent candidate may exist with `variation_space = null` in this research representation;
- projection digest and occurrence-history digest are separate because identical current projections can arise from materially different histories.

## Deterministic corpus

`selftest_progressive_projector.py` currently exercises 8 cases. The number 8 is descriptive only; it is not a threshold, score, or completeness claim.

Cases:

1. latent candidate can be represented before Variation Space is known;
2. Host extension sidecar changes occurrence history but not Core projection;
3. unknown non-Core event is retained as a residual;
4. unknown event may not silently alter Core projection;
5. duplicate event identity is rejected;
6. non-increasing event sequence is rejected;
7. two histories can produce the same Core snapshot while one contains additional negative occurrence history;
8. experiment -> evaluation -> integration -> retirement can be progressively projected.

## Important falsification found

The prototype deliberately demonstrates:

```text
HISTORY_A != HISTORY_B
while
CORE_PROJECTION_A == CORE_PROJECTION_B
```

when one history contains a negative occurrence that is not mapped into the current aggregate Core fields.

This means:

```text
CURRENT_SNAPSHOT_IDENTITY
!= COMPLETE_HISTORY_IDENTITY
```

and therefore a migration/interoperability mechanism that transfers only the aggregate snapshot can erase decision-relevant negative lineage unless that lineage is separately preserved or projected.

This is not a new philosophical claim; it is a concrete composition failure to handle.

## Extension result

The prototype also demonstrates a useful positive boundary:

```text
HOST_EXTENSION_PRESENT
-> history/sidecar changes
-> Core projection digest unchanged
```

So a strict portable Core plus Host extension seam is representationally possible without granting Host-local fields automatic semantic authority.

But this does **not** solve extension governance. A later design still needs namespace/version/provenance/decision-dependency rules.

## What this prototype does not prove

It does not prove:

- that event sourcing is better than the current aggregate;
- that represented events are complete or authentic;
- that sequence numbers represent real causality;
- that an evaluation is true;
- that integration authority existed;
- that an external effect happened;
- that a snapshot is sufficient for every receiver;
- that Host extensions are safe/trustworthy;
- that progressive representation is cheaper in real Host operation.

## Decision after first prototype

The event/projection HOW is **not rejected**, because it exposes a real snapshot-history boundary and composes naturally with existing ENA tooling.

But the naive branch:

```text
EVENT_LOG -> CURRENT_AGGREGATE -> discard history
```

is falsified for any context where negative/provenance/settlement history remains decision-material.

A viable branch must instead look more like:

```text
occurrence history
+ current projection
+ explicit retained decision-material lineage
+ bounded compaction/checkpoint rules
```

or preserve enough occurrence history that a receiver can independently reconstruct the material boundary.

## Next falsification targets

Before any stronger prototype:

1. classify which historical facts must survive projection (`negative evidence`, `authority lineage`, `settlement`, `supersession`, etc.);
2. test duplicate/retry semantics beyond simple duplicate IDs;
3. test compaction/checkpointing without losing material lineage;
4. compare sidecar vs namespaced-extension failure behavior;
5. test whether progressive representation materially reduces work relative to current aggregate construction.

Do not run stochastic multi-model tests until a question remains whose answer can genuinely vary in an epistemically useful way.

`CURRENT_CHANGE = NO`
