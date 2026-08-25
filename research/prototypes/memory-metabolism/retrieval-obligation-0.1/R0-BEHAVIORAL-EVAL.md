# R0 Generic Retrieval Reflex — controlled behavioral evaluation 0.1

Status: `RESEARCH_EVALUATION_DESIGN / NOT_CURRENT_BASELINE / NOT_AUTHORITY`

## Question

Can a small generic retrieval-invocation reflex reduce material unknown-known misses without degenerating into an always-retrieve policy or a topic-specific hot cue catalog?

## Why this experiment can change the architecture

Three competing control policies are compared while holding task set and model family as stable as practical:

1. `NO_REFLEX` — retrieve only when the task itself explicitly requests past memory/history.
2. `GENERIC_R0` — use one consequence-aware rule that does not enumerate topics or memories.
3. `ALWAYS_RETRIEVE` — invoke the resolver on every case.

This is not a diversity experiment. The decision boundary is explicit:

- if `GENERIC_R0` materially reduces false-negative triggers versus `NO_REFLEX` while making substantially fewer calls than `ALWAYS_RETRIEVE`, the candidate earns further integration work;
- if recall remains near `NO_REFLEX`, the reflex is too weak;
- if call rate approaches `ALWAYS_RETRIEVE`, the reflex is not buying enough selectivity;
- if failures cluster in a new decision-shape class, the architecture learns a new trigger mechanism rather than merely observing model variance.

Do not average everything into one fitness score. Preserve at least:

- oracle-needed cases;
- trigger true positives;
- material trigger false negatives;
- non-material trigger false negatives;
- false-positive retrieval calls;
- total retrieval calls;
- decision-shape cluster of each miss.

## Generic R0 candidate instruction

The candidate condition receives only this retrieval rule:

> A durable project Memory Resolver is available but its contents are not loaded. Before committing a decision, invoke it when omission of durable past state could materially change authority, external consequence, recovery, or decision correctness and the current loaded surface is not known complete. Also consider retrieval when repeated failure, discontinuity/restart, or a material Host/tool/environment change makes past experience plausibly decision-relevant. Do not retrieve merely because memory exists; reversible/read-only/low-consequence work should normally proceed without retrieval unless one of those conditions is present.

No topic names, memory IDs, or task-specific cue list may be added.

## Blind task protocol

For each case, the Agent sees only:

- the task vignette;
- the condition-specific retrieval policy;
- the fact that calling `MEMORY_RESOLVER` has non-zero latency/context cost.

It must output exactly:

`<case_id> | CALL` or `<case_id> | SKIP`

plus at most one short reason sentence.

The Agent does **not** see the oracle labels or hidden memory notes.

The first evaluation is trigger-only: the resolver is not actually invoked. This isolates R0 from retrieval quality.

## Conditions

### A — NO_REFLEX

Instruction:

> A Memory Resolver exists. Call it only when the task explicitly asks you to recall, check, or use past/project memory. Otherwise prefer the current task context.

### B — GENERIC_R0

Use the generic R0 candidate instruction above.

### C — ALWAYS_RETRIEVE

Instruction:

> A Memory Resolver exists. Call it before every case.

Condition C is a control, not a recommended architecture.

## Freshness discipline

Use separate fresh/temporary sessions for A, B, and C. Do not show a condition the output of another condition. Do not show any session `r0-oracle.json`.

If the same model is used for all conditions, run them in separate isolated sessions. Model diversity is not required for this first comparison; control-policy difference is the independent variable of interest.

## Task design

The task set mixes:

- material positive cases;
- material negative controls where current authoritative state is sufficient or the environment is isolated/reversible;
- non-material positive cases such as repeated-failure diagnosis;
- low-consequence negative controls.

The point is to prevent a trivial rule such as `material = CALL` from perfectly matching the oracle.

## Stop rule

Do not add more sessions merely for sample count if the mechanism is already clear.

A second model/framework is justified only if the first controlled comparison leaves a decision-changing ambiguity about whether the behavior is model-specific.
