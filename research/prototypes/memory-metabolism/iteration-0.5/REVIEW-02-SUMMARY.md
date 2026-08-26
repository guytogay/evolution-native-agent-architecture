# Independent review 02 summary — information-flow / access-control

Review target: iteration 0.4 at `083c5485905ea16c02bf1cd5f691d360c0a662a8`

Reviewer verdict: `NEEDS_NARROW_REVISION`

The review was performed in a fresh temporary ChatGPT conversation and was scoped specifically to information-flow/access-control semantics rather than another generic architecture vote.

## Material findings preserved

### Reference-model bugs

1. `retrieved_record_ids` could contain records the actor was not authorized to read because 0.4 checked only used/historical sets. This revealed an ambiguity between internal candidate retrieval and actor-visible disclosure.
2. `evidence_refs` / provenance-only lineage could bypass access-scope inheritance when `derived_from` was absent.
3. non-cognitive intermediary records could provide an effect-equivalent information-flow bypass because 0.4 applied inheritance only to selected cognitive layers.
4. an asserted declassification/sanitization basis immediately changed effective access scope even though the validator could not authenticate the basis. Represented release claim and effective Host-authorized release were conflated.
5. `FULL` challengeability meant only that some reachable evidence was present; it did not mean all represented dependencies survived or that the current actor could access them.
6. compiled-content access and provenance-dereference access were not independently represented.

### Reference-model overreach / false-BLOCK

7. literal union of source access labels causes access-scope accretion: more contributing experience can make a learned heuristic progressively unusable.
8. the opaque `access_scope` field was simultaneously acting like confidentiality label, ACL requirement, project/tenant/role namespace, and information-flow taint even though those policies have different composition rules.

### Host-security responsibilities, not memory-schema responsibilities

The review explicitly rejected making the Memory Metabolism contract prove:

- semantic sanitization/de-identification;
- re-identification resistance;
- cross-output inference safety;
- real actor entitlement authenticity;
- real declassification authority;
- tenant/purpose combination legality;
- concrete RBAC/ABAC/IFC/DLP policy.

## Best abstraction from the review

> **Memory transformation may not silently widen the legitimate information-use, access, publication, or consequence boundary of represented source information; deliberate widening must be externally justified for the transformed artifact.**

The reviewer concluded this is already implied by ENA Current and does **not** justify a new Constitution rule.

## 0.5 reconciliation direction

Iteration 0.5 therefore:

- replaces universal-looking label-union semantics with opaque `content_access_ref` Host boundary references;
- separates pre-disclosure candidates from actor-visible disclosed records;
- uses one canonical represented lineage surface across `derived_from`, `evidence_refs`, and cold provenance evidence refs;
- treats boundary-change claims as memory assertions that are not effective until a trusted Host projection input resolves them;
- separates compiled-content access from provenance inspection access;
- renames durable `challengeability` to global represented `evidence_availability` and leaves actor-relative challengeability to the projection/Host boundary;
- keeps mixed-boundary composition Host-resolved rather than computing a universal label union.

This summary preserves the materially distinct findings. It is not a replacement for the original reviewer transcript and does not authorize merge, release, Current mutation, or promotion.
