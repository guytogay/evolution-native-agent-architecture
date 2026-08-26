# Progressive Projector — Deterministic Self-Test Results

Date: 2026-08-26

Status: `EXECUTED_RESEARCH_EVIDENCE / REPRESENTED_STATIC_BEHAVIOR / NOT_CURRENT / NOT_RELEASE_AUTHORITY`

Prototype:

- `progressive_projector.py`
- `selftest_progressive_projector.py`

## Execution result

The current deterministic corpus executed successfully:

```text
PASS case_latent_without_variation_space
PASS case_extension_sidecar_does_not_change_core_projection
PASS case_unknown_non_core_event_is_retained_as_residual
PASS case_unknown_core_affecting_event_is_rejected
PASS case_duplicate_event_identity_is_rejected
PASS case_non_increasing_event_sequence_is_rejected
PASS case_snapshot_can_hide_distinct_negative_history
PASS case_progressive_lifecycle_projection
```

Corpus size: 8 cases.

```text
8_CASES = CURRENT_CORPUS_FACT
8_CASES != COMPLETENESS_THRESHOLD
8_CASES != EVIDENCE_INDEPENDENCE
8_CASES != MATURITY_SCORE
```

## What the run establishes

Within this represented prototype logic:

1. a `PROPOSED / LATENT / UNASSESSED` occurrence can project with `variation_space = null`;
2. Host extension metadata can alter represented occurrence history / extension sidecar without altering Core projection bytes;
3. unknown non-Core events can remain visible as unresolved projection residuals;
4. an unknown event cannot silently alter Core projection merely by asserting that it should;
5. duplicate event identity is rejected;
6. non-increasing supplied event sequence is rejected;
7. **distinct histories can project to the same Core aggregate snapshot**;
8. a progressive experiment/evaluation/integration/archive sequence can reconstruct a v2-style current aggregate shape.

## Key falsification

Case 7 intentionally demonstrates:

```text
HISTORY_A != HISTORY_B
HISTORY_DIGEST_A != HISTORY_DIGEST_B

while

CORE_PROJECTION_A == CORE_PROJECTION_B
PROJECTION_DIGEST_A == PROJECTION_DIGEST_B
```

One history contains an additional negative occurrence; the current Core projection does not represent it.

Therefore the naive branch:

```text
progressive history
-> current aggregate snapshot
-> discard history
```

is falsified whenever negative/provenance/settlement/authority history remains decision-material.

This connects directly to older ENA projection and negative-lineage failure classes:

```text
CURRENT_STATE_EQUIVALENCE
!= HISTORY_EQUIVALENCE
```

## Positive boundary

The Host-extension case demonstrates a useful separation:

```text
HOST_EXTENSION_PRESENT
-> extension sidecar/history changes
-> Core projection unchanged
```

This supports the representational feasibility of:

```text
STRICT_PORTABLE_CORE
+ EXPLICIT_HOST_EXTENSION_SURFACE
```

without granting Host-local fields automatic Core authority.

It does not yet establish namespace governance, portability, trust, or material-decision semantics for extensions.

## Evidence boundary

This execution establishes only behavior of the research projector/test corpus under represented inputs.

It does **not** establish:

- external occurrence truth;
- history completeness;
- event authenticity;
- real causal ordering;
- authority validity;
- effect settlement;
- universal fitness;
- lower Host cost;
- superiority over the Current aggregate HOW.

## Current disposition

```text
PROGRESSIVE_EVENT_HOW = RETAIN_FOR_FURTHER_FALSIFICATION
NAIVE_SNAPSHOT_ONLY_BRANCH = FALSIFIED_FOR_DECISION-MATERIAL_HISTORY
HOST_EXTENSION_SEAM = REPRESENTATIONALLY_VIABLE / GOVERNANCE_UNSOLVED
CURRENT_CHANGE = NO
```

Next static question:

> Which occurrence/history classes must survive projection or accompany a portable snapshot so that current-state equivalence cannot launder materially different lineage?

That question should be answered by lineage/evidence/authority/settlement analysis before adding more event types.
