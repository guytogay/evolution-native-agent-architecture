# R0 behavioral run 001 — ChatGPT temporary sessions

Status: `BEHAVIORAL_EVIDENCE / SINGLE_MODEL_SINGLE_RUN / NOT_CURRENT_BASELINE / NOT_AUTHORITY`

Fixture/oracle family: `retrieval-obligation-0.1`

Control design was frozen before these outputs were supplied. Conditions A and B were run in separate ChatGPT temporary conversations. Condition C (`ALWAYS_RETRIEVE`) is analytically determined by policy and was not re-run because it would add no epistemic information.

## Raw condition A — NO_REFLEX

```text
R01 | SKIP
R02 | SKIP
R03 | SKIP
R04 | SKIP
R05 | SKIP
R06 | SKIP
R07 | CALL | resuming explicitly requires prior execution state
R08 | SKIP
R09 | SKIP
R10 | SKIP
R11 | SKIP
R12 | SKIP
R13 | SKIP
R14 | SKIP
R15 | SKIP
R16 | SKIP
R17 | SKIP
R18 | SKIP
```

## Raw condition B — GENERIC_R0

```text
R01 | CALL | shared production change with incomplete rollout history
R02 | SKIP
R03 | CALL | repeated unusual failure may make past investigation relevant
R04 | SKIP
R05 | CALL | recovery could conflict with post-snapshot external effects
R06 | SKIP
R07 | CALL | interrupted external-write execution history is missing
R08 | SKIP
R09 | CALL | major environment change affects a shared-data workflow
R10 | SKIP
R11 | CALL | destructive shared-state action with incomplete retention context
R12 | SKIP
R13 | CALL | repeated failures with prior investigations absent
R14 | SKIP
R15 | SKIP | authoritative current details are complete for a one-off action
R16 | CALL | prior rollback and missing failure analysis may affect correctness
R17 | SKIP
R18 | CALL | shared-service recovery context may materially affect restart safety
```

## Frozen oracle positives

`R01 R03 R05 R07 R09 R11 R13 R16 R18`

Frozen oracle negatives:

`R02 R04 R06 R08 R10 R12 R14 R15 R17`

## Scores

### A — NO_REFLEX

- TP = 1
- FN = 8
- FP = 0
- TN = 9
- recall = 1/9 = 11.1%
- specificity = 9/9 = 100%
- precision = 1/1 = 100%
- accuracy = 10/18 = 55.6%
- retrieval calls = 1/18 = 5.6%

Missed positive clusters:

- MATERIAL_EXTERNAL_CHANGE
- REPEATED_FAILURE (two cases)
- RECOVERY_DISCONTINUITY
- HOST_TOOL_CHANGE
- DESTRUCTIVE_SHARED_CHANGE
- PRIOR_FAILED_MUTATION
- RECOVERY_OPERATION

It only called on the interruption/resume case because the task language made prior execution state especially explicit.

### B — GENERIC_R0

- TP = 9
- FN = 0
- FP = 0
- TN = 9
- recall = 100%
- specificity = 100%
- precision = 100%
- accuracy = 100%
- retrieval calls = 9/18 = 50%

Important controls:

- R15 (`MATERIAL_BUT_CURRENT_AUTHORITATIVE`) was correctly skipped, so behavior was not equivalent to `material => CALL`.
- R03/R13 were read-only yet correctly called because repeated failure/prior investigations could change diagnosis, so behavior was not equivalent to `write => CALL`.

### C — ALWAYS_RETRIEVE (analytical control)

By definition:

- TP = 9
- FN = 0
- FP = 9
- TN = 0
- recall = 100%
- specificity = 0%
- precision = 50%
- accuracy = 50%
- retrieval calls = 18/18 = 100%

No model run was performed because the policy mechanically determines the output.

## Provisional interpretation

The pre-registered directional criterion is satisfied on this fixture:

- Generic R0 materially improves recall over No Reflex;
- Generic R0 uses half the calls of Always Retrieve;
- it avoids both the material-action and write-action trivial classifiers.

However this result is **not** evidence of general retrieval-trigger reliability.

The fixture and R0 instruction share conspicuous structural language (repeated failure, interruption, rollback/recovery, major Host/tool change, missing historical context). A perfect score may partly measure successful application of the supplied rule to cases designed from the same rule family.

Therefore classify this run as:

`PROOF_OF_CONCEPT_BEHAVIORAL_APPLICATION`

not:

`GENERAL_R0_VALIDATION`.

## Decision-changing next test

Do not repeat this same fixture across many models merely to obtain variance.

Next use counterfactual minimal pairs / out-of-distribution wording where:

- topic nouns are held constant while retrieval warrant flips;
- obvious trigger vocabulary is reduced;
- current-context completeness and historical relevance are placed in tension;
- read/write/material labels alone cannot classify cases;
- false-positive CALL cost remains visible.

The next test should falsify whether Generic R0 tracks decision shape rather than lexical cue similarity.
