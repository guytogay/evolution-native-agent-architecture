# Projection Composition Falsification 0.1

Status: `RESEARCH_FIXTURE / ISSUE_85 / NOT_CURRENT_BASELINE / NOT_AUTHORITY / NOT_RELEASE_CANDIDATE`

Related: #73, #82, #85.

This fixture tests one narrow cross-prototype question without modifying Retrieval Obligation 0.5 or Memory Metabolism iteration 0.6:

> **When may a retrieval-sufficiency assessment survive transformation into a bounded Decision Projection, and when must the Host re-evaluate because the effective decision subject changed materially?**

It does **not** define a universal projection protocol, context format, or final-readiness certificate.

## Reference outcomes

- `TRANSFER_OK` — the represented transformation preserves the decision-material effect of the retrieval subject strongly enough that this fixture finds no reason to invalidate the prior sufficiency assessment.
- `REASSESS_REQUIRED` — the represented transformation may have changed the decision-material subject; the prior sufficiency assessment must not transfer automatically.

Neither outcome proves semantic truth. In particular, a Host declaration that a compacted projection `PRESERVES_DECISION_EFFECT` remains an external semantic claim.

## Narrow property

`retrieval-sufficient subject != automatically decision-sufficient projection`

More precisely:

> **Sufficiency does not automatically survive a material lossy subject transformation.**

The desired response is not `retrieve everything into prompt`.

A bounded projection may legitimately:

- omit non-material exploratory hits;
- remove redundant records;
- replace several records with one compact representation;
- preserve only the decision-material subset.

But if a material limitation, contradiction, obligation, or prerequisite is omitted or represented with unknown/lossy effect, transfer of the prior sufficiency assessment is not justified.

## Reference representation

Each retrieved result declares only whether it is decision-material for this fixture.

Each projection item may cover one or more retrieved results with one of:

- `EXACT`
- `PRESERVES_DECISION_EFFECT`
- `UNKNOWN`
- `LOSSY`

`EXACT` and `PRESERVES_DECISION_EFFECT` count as represented preservation.

The evaluator does **not** prove those declarations are true.

The fixture also carries:

- `assessed_projection_subject_ref`
- `effective_projection_subject_ref`

If they differ, the prior assessment is stale for the current effective projection even if the previous projection was lossless.

This is reference subject binding, not a normative hashing/identity protocol.

## Anti-bureaucracy rule

Do not turn this fixture into:

`retrieval certificate -> projection certificate -> interpretation certificate -> salience certificate -> application certificate`

Stage-local states are diagnostic evidence.

The consequential boundary should reason from the **effective subject actually used**.

## Current relationship

No new ENA rule is proposed.

Current already provides parent semantics through:

- effective loaded surface / truncation / selective loading / known gaps;
- claim != evidence != support relation;
- governance closure bounded by represented material inputs;
- composition creates a new selection/verification subject;
- whole effect surface.

This fixture exists only to falsify/reference the handoff between the two research prototypes.

## Cases

`cases.json` contains both false-OK and false-BLOCK controls:

1. material omission after retrieval sufficiency -> reassess;
2. omission of a non-material redundant hit -> transfer allowed;
3. decision-effect-preserving compaction -> transfer allowed;
4. dropped contradiction -> reassess;
5. broad exploratory retrieval projected down to the material subset -> transfer allowed;
6. non-material decision with harmless omission -> transfer allowed;
7. effective projection changes after assessment -> reassess;
8. unknown fidelity for material content -> reassess;
9. exact full projection -> transfer allowed.

Run:

```bash
python evaluate_projection_composition.py cases.json
python selftest.py
```

The selftest is deterministic. Passing it does not validate natural-language semantic fidelity, Host truthfulness, or final-world decision correctness.
