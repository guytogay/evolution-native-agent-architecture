# Reconciliation — Issue #85 projection composition seam

Status: `RESEARCH_RECONCILIATION / NOT_CURRENT_BASELINE / NOT_RELEASE_AUTHORITY`

## Deterministic result

Local authoring-host execution:

`PROJECTION_COMPOSITION_01_SELFTEST_PASS 9`

This proves only that the reference evaluator produces the intended structural dispositions for the nine frozen cases. It does not prove semantic fidelity, materiality classification, Host truthfulness, or naturalistic task correctness.

## What the fixture establishes

The cross-prototype failure mechanism is real at the interface level:

```text
retrieval subject {M1, M2}
-> retrieval sufficiency resolved for that subject
-> bounded projection transforms it
-> effective decision subject may no longer contain the material effect of M2
```

Therefore:

> **retrieval-stage sufficiency must not be treated as automatically transferable final decision readiness after a material lossy projection.**

The false-OK side is represented by:

- material omission;
- dropped contradiction/limitation;
- unknown/lossy fidelity;
- effective projection subject changing after assessment.

The false-BLOCK controls show that the correct property is **not** `retrieved == projected`.

Legitimate bounded transformations include:

- omitting non-material/redundant/exploratory hits;
- preserving only the decision-material subset;
- replacing several retrieved records with a compact representation that is externally represented as preserving their decision effect.

## Smallest reconciliation direction

### 1. Retrieval 0.5 closure is stage-local

Retrieval Obligation 0.5 should be interpreted as closing the retrieval lifecycle for its represented retrieval subject.

Its `decision.disposition = READY` field is a reference-level naming/level-of-abstraction hazard if consumers read it as final action readiness after later projection.

Do **not** mutate frozen Retrieval 0.5 merely to rename the field until a future interface revision is independently justified.

Working semantic clarification:

```text
retrieval lifecycle closed
!=
final consequential decision ready
```

### 2. Final decision closure reasons from the effective loaded subject

Current already carries this property through:

- Local Projection's effective loaded surface, truncation/selective loading, and known gaps;
- claim/evidence/support separation;
- composition revalidation;
- governance closure bounded by represented material inputs.

Therefore no new universal Memory certificate is required.

### 3. Lossy transformation is consequence-sensitive

A changed representation does not automatically require re-evaluation.

Re-evaluation is justified when the transformation may have changed a **decision-material effect** or when its preservation is `UNKNOWN`.

Exact identity preservation is not required if a bounded representation truthfully preserves the material decision effect.

This keeps compression possible and avoids reintroducing unbounded hot context.

## What this fixture intentionally does not solve

It does not prove:

- whether a record is actually decision-material;
- whether a summary truly preserves a limitation or contradiction;
- whether a Host's `PRESERVES_DECISION_EFFECT` assertion is trustworthy;
- whether an LLM will notice a projected limitation;
- whether a projected fact becomes salient/applied;
- whether the final external-world action is correct.

Those remain Host/evaluation/behavior questions.

## Constitution / Current disposition

`NEW_ENA_RULE = NOT_SUPPORTED`

`CURRENT_MUTATION = NOT_AUTHORIZED`

`RETRIEVAL_0_6 = NOT_JUSTIFIED`

`FORCE_ALL_RETRIEVED_CONTENT_HOT = REJECTED`

`REFERENCE_COMPOSITION_SEAM = CONFIRMED`

`SMALLEST_RECONCILIATION = STAGE_BOUNDARY + EFFECTIVE_SUBJECT_APPLICABILITY`

## Reviewer decision

A fresh reviewer is only justified if used as a **cross-prototype composition reviewer**, not another Retrieval-lifecycle or generic Memory reviewer.

The reviewer should attack one question:

> Does the proposed stage-boundary/effective-subject reconciliation actually prevent readiness laundering without forcing identity-preserving projection or a certificate ladder?

If no materially new mechanism is found, review should stop and #85 should remain a reference-level reconciliation plus future naturalistic observation target.
