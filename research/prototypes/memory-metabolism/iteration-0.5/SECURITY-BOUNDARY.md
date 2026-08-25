# Iteration 0.5 security boundary

Status: `RESEARCH_PROTOTYPE / NOT_CURRENT_BASELINE / NOT_AUTHORITY`

## Shared property

> **Memory transformation must not silently widen the legitimate information-use, access, publication, or consequence boundary of represented source information.**

This is an application/recomposition of existing ENA Current semantics, not a proposed new Constitution ID.

## What the prototype represents

`content_access_ref` is an opaque Host policy-boundary reference. It is deliberately not defined as a universal RBAC role, ABAC attribute set, Bell-LaPadula label, DLP classification, tenant ID, purpose-control language, or IFC lattice.

The reference validator only detects these structural cases:

- one source boundary is preserved;
- one source boundary is represented as changed;
- multiple distinct source boundaries are represented as composed;
- a boundary-changing record is disclosed only after a trusted Host projection input says the transition has been resolved.

It does not decide what the correct target boundary should be.

## Candidate discovery != disclosure

`candidate_record_ids` may be produced by an internal retrieval/search organ before actor-visible access.

`disclosed_record_ids` are actor-visible and must satisfy the Host-resolved access boundary.

This avoids conflating search candidate discovery with permission to read.

## Boundary claim != authority

A record-level `boundary_transition_claim` means only that a Host/security decision is represented.

It becomes usable in a Decision Projection only when the record is included in `host_resolved_boundary_record_ids`.

The validator does not authenticate that Host input; it only keeps memory-authored claims distinct from Host-resolved enforcement input.

## Provenance access is separate

A public compiled lesson may point to a restricted `provenance_set` through an opaque `provenance_ref`.

Permission to use the compiled lesson does not imply permission to inspect the provenance.

`challengeable != universally readable`.

## Evidence availability is not actor-relative challengeability

`evidence_availability` describes the represented global availability of reachable evidence only.

It does not claim that the current actor may read that evidence, that the evidence is true, or that a semantic conclusion is fully contestable.

## Host-specific responsibilities

The Host/security/privacy organ remains responsible for:

- authentic actor entitlements;
- authentic declassification/publication authority;
- semantic sanitization/de-identification;
- purpose and tenant policy;
- inference/re-identification risk;
- composition/privacy policy;
- binding an approval to the exact artifact/version;
- concrete RBAC/ABAC/IFC/DLP enforcement.

The memory contract should not grow these into universal ENA machinery.
