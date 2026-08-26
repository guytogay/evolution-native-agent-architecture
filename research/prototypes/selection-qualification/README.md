# Selection Qualification reference organ

Status: `RESEARCH_PROTOTYPE / NEXT_RELEASE_INPUT / NOT_CURRENT / NOT_RELEASE_CANDIDATE`

Related: #81, #84, #89, #93, #94, PR #82.

## WHAT

Preserve the qualification of a durable evolution-selection verdict without forcing every Host to manufacture a universal environment taxonomy.

The narrow problem is:

```text
selection_state = SUPPORTED | PARTIAL | NOT_SUPPORTED | HARMFUL | UNKNOWN
+
represented experiment/evaluation/evidence
+
selection scope no longer reconstructable
-> durable record still looks like a fully qualified selection verdict
```

Current v0.3.6 intentionally allows `environment: {}` and does not inspect selection scope in the v2 consistency validator. That is legitimate for an `UNASSESSED` latent candidate, but a long-lived non-`UNASSESSED` verdict can then lose the conditions under which the verdict was selected.

## WHY

The confirmed failure is **selection-scope provenance loss**, not automatic receiver-selection laundering.

Current migration semantics already prevent:

`source SUPPORTED -> receiver LOCALLY_SELECTED`

without receiver-side selection.

But a later reader may still inherit:

> `SUPPORTED somewhere / under conditions that are no longer reconstructable`

and be unable to compare environments, understand negative evidence, triage transfer, or know whether a result was narrowly local.

## Target property

> **A non-UNASSESSED selection verdict must either retain a represented decision-material scope basis, or explicitly preserve that its selection qualification is UNKNOWN/INCOMPLETE.**

This prototype deliberately does **not** require:

- Host/model/language on every record;
- a fixed environment vocabulary;
- `environment.minProperties >= 1`;
- fake metadata such as `{ "scope": "local" }`;
- proof that represented scope metadata is externally true;
- universal portability merely because qualification is represented.

## HOW — minimal overlay

The reference evaluator consumes:

1. an existing evolution-record-v2-shaped record; and
2. an optional `selection_qualification` overlay.

It does not replace the v2 record or Current validator.

Resolution states:

- `NOT_APPLICABLE` — selection is `UNASSESSED`; no qualification ceremony is required.
- `QUALIFIED_DIRECT` — non-empty `environment` supplies a represented direct scope basis.
- `QUALIFIED_REFERENCED` — direct environment is empty, but the overlay explicitly identifies one or more represented scope-basis references.
- `QUALIFICATION_UNKNOWN` — the record truthfully preserves that selection occurred but the material selection scope is unknown/incomplete.
- `UNQUALIFIED_SELECTION` — a non-UNASSESSED verdict has neither direct/referenced qualification nor explicit unknown/incomplete status.
- `INVALID_RECORD` — overlay representation contradicts itself or the record.

The distinction is intentionally claim-strength oriented:

```text
UNQUALIFIED_SELECTION
!= selection never happened
```

It means:

> do not narrate this durable verdict as scope-qualified.

Likewise:

```text
QUALIFICATION_UNKNOWN
!= BLOCK ALL USE
```

It means the occurrence/verdict can remain useful evidence while portability/applicability interpretation is narrowed.

## Overlay shape

Example referenced qualification:

```json
{
  "selection_qualification": {
    "status": "SCOPED",
    "scope_basis_refs": [
      "evaluation:eval-3:scope",
      "evidence:trace-local:scope"
    ]
  }
}
```

Example honest incomplete qualification:

```json
{
  "selection_qualification": {
    "status": "UNKNOWN",
    "note": "Historical result retained; material Host/model context was not preserved."
  }
}
```

Reference strings are represented links only. This prototype does not authenticate or dereference their external truth.

## Negative verdict symmetry

`HARMFUL` and `NOT_SUPPORTED` also require qualification or explicit UNKNOWN/INCOMPLETE.

A local negative result becoming a scope-free global prohibition can destroy useful variation just as a local positive result becoming a global recommendation can create false confidence.

```text
local failure != universal impossibility
```

## Migration/source selection

A source selection carried in migration needs the same interpretability property:

- represented `source_environment`; or
- represented source qualification basis refs; or
- explicit `UNKNOWN/INCOMPLETE` source qualification.

Receiver-side reselection remains required regardless. This organ improves historical/transfer interpretation; it does not mint receiver-local proof.

## False-BLOCK controls

The prototype must preserve:

1. `UNASSESSED + environment {}` as fully legitimate with no qualification object;
2. non-UNASSESSED + compact direct environment scope;
3. non-UNASSESSED + empty environment but explicit scope-basis references;
4. explicit UNKNOWN/INCOMPLETE qualification as a valid honest state;
5. negative verdicts with unknown scope as useful but narrowed evidence;
6. no requirement to populate irrelevant standard dimensions.

## Evidence boundary

Machine PASS means only that the qualification relation is represented coherently.

It does **not** prove:

- the environment fields are complete or externally true;
- a scope-basis reference actually contains the claimed scope unless another mechanism establishes that;
- the Host identified every material applicability dimension;
- source selection transfers to receiver selection;
- selection itself was externally correct.

```text
QUALIFICATION_REPRESENTED != QUALIFICATION_EXTERNALLY_COMPLETE
QUALIFICATION_UNKNOWN != SELECTION_FALSE
SOURCE_QUALIFIED != RECEIVER_SELECTED
```

## Intended next-release landing

This prototype exists to choose the cheapest next-release representation that closes #81.

Candidate integration forms include:

- a small optional `selection_qualification` field on evolution record / migration packet;
- equivalent validator semantics using existing scope-bearing fields plus an explicit unknown marker;
- another representation with the same property and lower migration cost.

The reference property, not this exact JSON overlay, is the candidate for absorption.

`CURRENT_CHANGE = NO`
