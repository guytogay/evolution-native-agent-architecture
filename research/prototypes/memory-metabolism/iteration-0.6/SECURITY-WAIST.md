# Memory Metabolism iteration 0.6 — Security Narrow Waist

Status: `RESEARCH_PROTOTYPE / SECURITY-SIDE STOP / NOT_CURRENT_BASELINE / NOT_AUTHORITY / NOT_RELEASE_CANDIDATE`

This iteration is not a new security architecture. It is the reconciliation endpoint after three independent structural/security reviews.

## Why 0.6 exists

Iteration 0.4 overfit the first access-flow finding into a positive-label inheritance model. Independent review showed that such literal scope accumulation could make memory less usable as experience grew.

Iteration 0.5 replaced that lattice with opaque Host boundary references, but a third independent formal/systems-boundary review found that the reference encoding still confused some mechanisms with universal semantics and retained deterministic bypass/overreach paths.

Iteration 0.6 therefore retreats again.

## The properties that still pay rent

1. **Actor-visible information consequences remain Host-governed.** Internal retrieval mechanics do not become an excuse to disclose information outside the Host-resolved legitimate boundary.
2. **Representation change does not manufacture an external boundary change.** A memory may represent that a transition exists; memory alone cannot make that transition legitimate/effective.
3. **External resolution must be current and bound to the relevant subject/effect.** A resolution for an old or different artifact cannot silently authorize a modified one.
4. **Effect-equivalent information-bearing paths cannot bypass the same semantic boundary merely by changing representation.** The reference encoding therefore has one canonical lineage surface.
5. **Provenance existence and provenance inspection are different.** A compiled lesson may remain usable while supporting provenance remains separately governed.
6. **Shared semantics do not require one universal security organ.** A simple one-user private Host need not instantiate RBAC/ABAC/IFC/DLP-shaped objects.

These are applications/recompositions of ENA Current semantics. They are **not candidate new Constitution IDs**.

## What 0.6 deliberately removes from the shared memory record

The memory record no longer contains a universal `content_access_ref` token whose equality is treated as policy semantics.

The shared projection no longer contains pre-disclosure retrieval candidates. Candidate/index metadata is a Host retrieval-organ concern until it crosses an actor-visible/effect boundary.

The prototype does not define policy ordering, tenant semantics, purpose limitation, policy epochs, declassification law, privacy budgets, DLP, noninterference, or cross-Host federation.

## Two reference projection modes

### `SINGLE_BOUNDARY_REFERENCE`

For simple Hosts where all represented memory is already inside one legitimate local/private boundary. No Host security-resolution objects are required.

This is not a claim that the world has no security policy. It means this reference encoding adds no decision value for that Host boundary.

### `HOST_RESOLVED_REFERENCE`

For Hosts that need explicit actor-visible disclosure/boundary/provenance mediation.

The prototype uses subject fingerprints and resolution references only as a **reference organ** to demonstrate the property:

> external resolution is bound to the exact represented subject/effect.

Another Host may satisfy the same property with capabilities, database views, an authorization service, signed policy decisions, process isolation, application logic, or another mechanism.

## Candidate vs visible information

Iteration 0.5 represented `candidate_record_ids`. That created an unnecessary ambiguity: a candidate may be purely Host-internal, or its metadata may itself cross a protected boundary.

Iteration 0.6 removes candidates from the shared Decision Projection.

The shared projection begins at:

`actor-visible record content`

Anything earlier belongs to the retrieval organ. If candidate metadata becomes observable outside that organ, it has become an information consequence and the Host must govern it accordingly.

## Provenance confidentiality

`provenance_ref` is storage/reconstruction metadata, not permission for every consumer to inspect provenance.

In `HOST_RESOLVED_REFERENCE`, actual provenance inspection is separately resolved.

The prototype does not claim that a provenance identifier is intrinsically safe to expose. A Host may use opaque handles or project only safe actor-visible fields.

## Evidence availability

0.5's `DEGRADED` term was too ambiguous. 0.6 uses only machine-checkable global existence states:

- `ALL_PRESENT`
- `SOME_PRESENT`
- `NONE_PRESENT`
- `UNKNOWN`

This says nothing about whether the current actor is allowed to inspect the surviving evidence.

## Security-side stop rule

After 0.6 deterministic reconciliation, do **not** continue generic security-review iterations unless a new shared structural mechanism is found.

Remaining hard questions such as semantic sanitization, re-identification, tenant/purpose policy, entitlement authenticity, policy composition, privacy inference, and DLP are Host/security/privacy-organ questions.

The Memory Metabolism research should now return to its central unresolved problem:

> **How can a bounded active Agent reliably discover that relevant cold memory exists and bring the right memory into the decision surface without loading the whole past?**

That is the Retrieval Reflex / Unknown-Known problem.
