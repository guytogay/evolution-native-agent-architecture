# Tiny Hot Kernel Fixture Oracle Status

Status:

`AUTHOR_EXPECTATION / INDEPENDENT_REVIEW_PENDING / NOT_GROUND_TRUTH`

The expectations in `tiny-kernel-cases.jsonl` were authored as an initial falsification surface for K-A/K-B/K-C and the shared Semantic Router.

They are **not** canonical ENA truth and are not yet eligible to decide which kernel is fitter merely because a scorer can compare model output to them.

Important distinction:

```text
deterministic scorer correctness
!=
fixture oracle semantic correctness
```

The current machine gate proves that:

- blind stimuli align mechanically with the private oracle;
- the scorer detects deliberately injected FN/FP/fallback/kernel-binding failures;
- the oracle is not leaked through the blind stimulus file;
- router target sections exist.

It does **not** prove that each `expected_trigger`, `primary_families`, or `allowed_families` value is the best ENA-consistent expectation.

Some deliberately high-value boundary cases are contestable, for example:

- low-consequence explicit external writes that may not justify ENA retrieval;
- storing a latent idea without expressing/applying it;
- when governance closure should interrupt versus remain background substrate;
- how broad a multi-family route should be before it becomes over-routing;
- whether a language/Host change is material in a particular task;
- how `MATERIAL` should be interpreted by a tiny resident recognizer.

## Selection eligibility

Until independent oracle review is reconciled:

`CONTROLLED_RUNS = ALLOWED_AS_EXPLORATORY_DATA`

`KERNEL_WINNER_BY_ORACLE_SCORE = NOT_AUTHORIZED`

`CURRENT_CHANGE_FROM_ORACLE_SCORE = NOT_AUTHORIZED`

After review, preserve both the pre-review oracle and the reviewer delta/history. Do not silently rewrite the fixture lineage.
