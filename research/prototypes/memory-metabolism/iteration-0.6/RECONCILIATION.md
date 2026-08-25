# Reconciliation — independent review 03 -> iteration 0.6

Reviewed target: `iteration-0.5 @ 6d1370cde1f119e813408dbca0dda77009ab1e30`

Independent verdict: `NEEDS_NARROW_REVISION`

Independent stopping verdict: **security-side review should STOP after deterministic reconciliation.**

## Material findings preserved

| Finding | 0.6 disposition |
|---|---|
| F1 `relations.DERIVED_FROM` bypasses canonical lineage | `FIXED_BY_ELIMINATING_DUPLICATE_LINEAGE_ENCODING`; `derived_from`/evidence/provenance evidence are canonical; relation form removed from 0.6 schema |
| F2 Host resolution not subject-bound | `FIXED_IN_REFERENCE_ENCODING`; complex-Host resolutions bind exact current record fingerprint + resolution ref; modified subject invalidates old resolution |
| F3 opaque-ref equality unsafe across Host/epoch | `REMOVED_FROM_SHARED_MEMORY_SEMANTICS`; 0.6 no longer interprets policy-token equality; current/local resolution is Host concern |
| F4 candidate metadata can leak | `BOUNDARY_REDEFINED`; pre-disclosure candidates removed from shared projection; if retrieval metadata becomes externally visible it is an information consequence governed by Host |
| F5 provenance handle can leak | `HOST_PROJECTION_BOUNDARY`; provenance existence does not grant inspection; complex-Host inspection is separately resolved; safe handle/display projection remains Host organ |
| F6 `DEGRADED` unconstrained | `FIXED_BY_PRECISE_VOCABULARY`; `ALL_PRESENT/SOME_PRESENT/NONE_PRESENT/UNKNOWN` have explicit global-existence semantics |
| F7 simple Host forced to invent security objects | `FIXED_BY_REFERENCE_MODES`; `SINGLE_BOUNDARY_REFERENCE` requires no Host resolution ceremony |
| F8 opaque alias inequality forced governance | `REMOVED_WITH_TOKEN_COMPARISON`; boundary token equality is no longer used as universal semantics |

## What was deliberately NOT solved

No universal policy ordering, policy epoch protocol, actor entitlement authentication, declassification mechanism, tenant/purpose language, DLP, sanitization proof, inference control, cross-Host federation, or privacy theorem was added.

Those were explicitly classified as Host/security/privacy organs or out of scope by the independent review.

## Semantic conclusion

No new ENA rule is justified.

Useful explanatory synthesis:

`internal representation change != external authority/boundary change`

This pays explanatory rent but not constitutional rent because ENA Current already carries the parent structure.

## Research transition

Security-specific structural review closes after 0.6 regression unless a materially new shared mechanism appears.

Next research frontier:

`UNKNOWN-KNOWN / RETRIEVAL REFLEX / BOUNDED DISCOVERY OF COLD MEMORY`
