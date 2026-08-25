# Iteration 0.5 reconciliation — after independent information-flow review

Status: `RESEARCH_PROTOTYPE / NOT_CURRENT_BASELINE / NOT_AUTHORITY / NOT_RELEASE_CANDIDATE`

Reviewed predecessor:

- iteration 0.4
- frozen review target: `083c5485905ea16c02bf1cd5f691d360c0a662a8`
- reviewer verdict: `NEEDS_NARROW_REVISION`

This iteration preserves the reviewed 0.4 artifacts and adds a new reference iteration rather than rewriting the reviewed target.

## Why 0.5 exists

The second independent review found that 0.4 correctly closed several direct access/supersession paths, but its `access_scope` model was doing too much at once: record-read requirement, derivation/information-flow label, possible project/tenant/role/compartment label, and implicit policy-composition rule.

Strong findings:

1. unauthorized records could appear in `retrieved_record_ids` because only used/historical records were access checked;
2. `evidence_refs` / provenance-only lineage bypassed the derived-scope rule when `derived_from` was absent;
3. non-cognitive intermediary records could bypass scope inheritance;
4. an asserted declassification/sanitization basis immediately changed effective scope even though the validator could not authenticate it;
5. `FULL` challengeability conflated evidence existence, completeness, and actor accessibility;
6. provenance access and compiled-content access were not independently represented;
7. literal scope-union semantics creates access-scope accretion as experience grows.

The review also concluded that these do **not** justify a new ENA Constitution rule. The high-level property is already implied by Current's scoped authority/confidentiality/publication/provenance/whole-effect-surface semantics.

## Main 0.5 change: one label set is not universal security semantics

Iteration 0.5 replaces the universal-looking `access_scope` / subset-union model with an opaque Host boundary reference:

`content_access_ref`

This is deliberately **not** declared to be RBAC, ABAC, Bell-LaPadula, IFC, DLP, tenant labels, purpose control, or any other universal policy lattice.

The shared property becomes:

> **Memory transformation must not silently widen the legitimate information-use/access/publication/consequence boundary of represented source information.**

The Host decides what a boundary reference means and whether a transformation legitimately moves between boundaries.

## Candidate vs disclosed

0.4's `retrieved_record_ids` mixed internal pre-access candidate discovery with actor-visible disclosure.

0.5 separates:

- `candidate_record_ids` — may be discovered internally before disclosure;
- `disclosed_record_ids` — actually exposed to the decision actor/context.

Access is enforced at disclosure.

## Boundary-change assertion != boundary-change authority

A record may carry `boundary_transition_claim` with `HOST_RESOLVED_CHANGE` or `HOST_RESOLVED_COMPOSITION` plus an external resolution reference.

That representation is only a **claim about an external Host/security decision**.

A Decision Projection must separately include the record in `host_resolved_boundary_record_ids` before a boundary-changed record may be disclosed.

`represented release/declassification claim != authenticated/effective release authority`

The validator still does not authenticate the Host resolution itself.

## Canonical lineage

Security/provenance checks now consume one canonical lineage surface:

`derived_from ∪ evidence_refs ∪ provenance_ref.evidence_refs`

This closes the 0.4 bypass where one rule treated `evidence_refs` as lineage while another ignored it.

The provenance/boundary rule is no longer limited to only `KNOWLEDGE | COMPILED | IDENTITY` layer names. If a record represents an information-bearing lineage edge, the edge participates regardless of layer.

## No universal literal union

If all direct lineage sources share one `content_access_ref` and the target keeps it, no security ceremony is required.

If the target changes a single source boundary, the change must be represented as `HOST_RESOLVED_CHANGE`.

If multiple distinct source boundaries are composed, the target requires `HOST_RESOLVED_COMPOSITION`.

The validator does **not** compute a union of labels and does not decide what the correct resulting boundary is.

That avoids:

`more experience -> more labels -> less usable learned memory`

and keeps policy composition Host-specific.

## Provenance confidentiality

`provenance_set` now has its own `content_access_ref`.

A public compiled lesson may keep an opaque `provenance_ref` to restricted evidence lineage. Using the lesson does not automatically grant permission to inspect that provenance.

This preserves:

`challengeable != universally readable`

## Evidence availability != actor challengeability

0.4 used `challengeability`, which could misleadingly mean some evidence exists globally, all necessary evidence exists, or this actor can access it.

0.5 renames the durable structural field to `evidence_availability`.

It is a global represented evidence-state property only. For `FULL`, all reachable represented EVIDENCE/ARCHIVE records must be `PRESENT`.

Actor-relative evidence/provenance access is handled at the projection/Host boundary.

## What 0.5 still does not solve

It does not prove semantic sanitization/de-identification, non-reidentification, cross-output inference safety, tenant/purpose combination legality, real actor entitlement authenticity, real declassification authority, exact-content binding of a Host resolution, real source independence, retrieval completeness, or policy correctness.

Those remain Host/security/privacy-organ responsibilities or field questions.

## Deterministic evidence

Local development selftests:

`MEMORY_METABOLISM_ITERATION_05_SELFTEST_PASS 20`

Second-review regression suite:

`MEMORY_METABOLISM_REVIEW2_REGRESSION_PASS 11`

These prove only represented structural reachability/blocking of the encoded cases.

## Reconciliation verdict

`ITERATION_0_4 = SUPERSEDED_RESEARCH_ITERATION / PRESERVED_FOR_REPRODUCIBILITY`

`ITERATION_0_5 = RESEARCH_CANDIDATE_FOR_NEXT_INDEPENDENT_REVIEW`

`NEW_CONSTITUTION_RULE = NOT_SUPPORTED`

`CURRENT_MUTATION = NOT_AUTHORIZED`

`HOST_INTEGRATION = NOT_YET`

Before Host integration, 0.5 should receive one narrow follow-up review focused on whether the new opaque-boundary / Host-resolution interface still contains false-OK or false-BLOCK paths and whether it has actually reduced security overreach rather than merely renaming it.
