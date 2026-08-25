# Field Use 002 — Does HIT != Sufficiency Need a New ENA Rule?

Status: `NATURALISTIC_REFERENCE_TRACE / NOT_CURRENT_BASELINE / NOT_AUTHORITY`

## Real research question

After Retrieval Obligation 0.3 separated a retrieval HIT from retrieval sufficiency, a real architecture question followed:

> Does `retrieval HIT != retrieval sufficiency` require a new ENA invariant, or is it already covered by Current claim/evidence/support and closure semantics?

## Cold resolver result

Initial selected scopes:

1. `retrieval-obligation`
2. `current-runtime-semantics`

This was the direct scope combination needed for the question.

## Current cross-check

`releases/current/05-CORE-OPERATIONAL-CONTRACTS.md` already states:

- `claim != evidence != support relation`;
- evidence existence/validity alone does not establish support for a consequential claim;
- `SATISFIED` requires closure evidence appropriate to the obligation;
- `READY` is bounded by completeness of represented material inputs.

Therefore:

`retrieval HIT`

is evidence that retrieval returned something, but it does not automatically establish:

`retrieval obligation sufficiently resolved for this decision`.

## Disposition

No new ENA Constitution rule or capability is justified.

The 0.3 field:

`sufficiency_resolution_ref`

is best treated as **reference encoding** that prevents the prototype validator from minting sufficiency directly from a HIT.

It is a concrete projection of existing ENA semantics, not a new normative concept.

Short form:

> **Retrieval evidence is not retrieval-support sufficiency.**

This is explanatory synthesis only.

## Research boundary

Do not promote this reference field into Current merely because it is useful in the prototype.

The semantic-rent test does not establish a new bad decision that Current permits without a new rule.
