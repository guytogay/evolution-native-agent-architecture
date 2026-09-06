# Minimum Evolution Loop — Current

Status: `CURRENT / COLD_OPERATIONAL_HOW / HOST_NEUTRAL`

Use this procedure when an Agent/Host needs to turn ENA's evolution semantics into a repeatable operating loop.

This is **not** a universal daemon, scheduler, database, or self-modification engine. A Host may realize the loop with JSONL, Git, a database, task memory, a queue, cron/events, an experiment runner, or another native mechanism.

```text
EVOLUTION_VOCABULARY != EXECUTABLE_EVOLUTION_LOOP
PROTECTION_OF_EVOLVABILITY != EVOLUTION_ITSELF
```

## Trigger

Start or wake the loop when there is a concrete evolution signal, for example:

- correction or repeated failure;
- friction, latency, cost, coordination burden, or repeated manual rescue;
- unexpected success or reusable shortcut;
- new capability/tool/model/Host/environment;
- external contribution or migrated adaptation;
- a latent idea that has become relevant to a real decision;
- a material Host/runtime change that invalidates previous assumptions.

A signal is worth durable capture when losing it could plausibly weaken a later selection, recovery, evidence, or repeated-work decision. **Do not persist every passing thought merely because an inbox exists.**

No signal is also information: do not mutate merely because an evolution loop exists.

## Minimum loop

### 1. Capture the signal durably

For a decision-relevant signal, put the observation into a durable inbox/queue before deciding what to change. Trivial/transient thoughts that cannot plausibly affect a later decision may be discarded rather than ceremonialized.

Minimum fields:

```text
time
source / author
subject
signal or observation
why it may matter
links/evidence if available
state = SIGNAL | IDEA | CANDIDATE
```

For `evolution-record.v2`, map relevant occurrence references into `signal_refs` / `mutation_pressure_refs`.

**Boundary:** chat presence is not durable capture. A capability name such as `Evolution Inbox` does not mean a Host actually has one. Durable capture is also not a requirement to log every idea.

### 2. Form a candidate, but keep it latent by default

Represent:

```text
hypothesis
proposed change
expected outcomes
current environment
unknowns / dependencies
protected subjects
observation plan
```

Use `templates/evolution-record.v2.json`, `tools/ena_evolve_v2.py new-latent`, or a Host-native equivalent.

Default state:

```text
lifecycle_state = PROPOSED
expression_state = LATENT
selection_state = UNASSESSED
```

A useful idea does not owe immediate execution.

### 3. Decide whether reality contact is worth the cost

Before expressing the candidate, ask:

- what decision could this trial change?
- what outcome would count as improvement, degradation, unchanged, or still unknown?
- is the variation cheap/reversible enough for direct local trial?
- does it need an isolated Variation Space?
- could it disable its own recovery path?
- does it cross an external authority/effect boundary?

Valid outcomes here include:

`KEEP_LATENT | TRIAL_NOW | WAIT_FOR_CONTEXT | REJECT_WITHOUT_TRIAL | NOT_APPLICABLE`.

Do not create an experiment whose result range is already baked into the treatment or whose only likely result is generic model/session variability.

### 4. Establish the minimum before-state

For a trial that can materially alter the Agent or Host, capture only what can change the later selection decision:

- decision-relevant baseline or smoke tasks;
- current cost/latency/resource use where material;
- current capability/behavior relevant to the hypothesis;
- snapshot/rescue path when self-change could disable recovery;
- authority/effect boundary if the trial can escape locally;
- explicit stop/rollback condition.

```text
BACKUP_EXISTS != RECOVERY_PROVEN
BASELINE_EXISTS != UNIVERSAL_FITNESS_METRIC
```

The baseline may be 1–5 smoke probes, a task benchmark, a real workflow metric, qualitative evidence, or another bounded measure. Do not invent a universal score.

### 5. Express the variation in the lightest real environment

Choose the narrowest surface that can generate decision-changing evidence:

- local reversible change;
- branch/worktree/sandbox/canary;
- limited traffic/task subset;
- shadow/observe-only mode;
- real task with rollback;
- full integration only when lower-cost reality contact cannot answer the question.

Record the actual change, time, variation space, effect boundary, recovery path and authority basis in `experiments[]` or an equivalent Host record.

If the variation remains purely conceptual, keep it `LATENT`; do not fabricate `EXPRESSED` evidence.

### 6. Observe outcomes before choosing the story

Compare against the before-state and the candidate's expected outcomes.

Record multiple dimensions when they matter, for example:

- task correctness / usefulness;
- latency / token / compute / human attention;
- recovery/resilience;
- new failure modes;
- coordination cost;
- external effects or compensation debt;
- behavior on the intended Host/environment.

Preserve negative evidence and unknowns.

Map the result to local selection:

`SUPPORTED | PARTIAL | NOT_SUPPORTED | HARMFUL | UNKNOWN`.

```text
LOCAL_SELECTION != UNIVERSAL_FITNESS
ONE_SUCCESS != LAW
SURVIVAL_OR_REWARD != MORAL_CORRECTNESS
```

### 7. Act on selection

Selection is not the same as integration.

- `SUPPORTED` → integrate if the actual authority/scope permits; record `integration_history` and retained residuals.
- `PARTIAL` → narrow/adapt the variation, or integrate only the supported part.
- `NOT_SUPPORTED` → reject for this environment while retaining the negative evidence.
- `HARMFUL` → stop/rollback where possible; preserve the failure lineage.
- `UNKNOWN` → remain latent/dormant or gather a genuinely decision-changing next observation; do not force a verdict.

Possible lifecycle outcomes:

`INTEGRATED | LATENT | DORMANT | ARCHIVED | RETIRED | REJECTED_AS_LOCAL_SELECTION`.

The v2 schema represents `ARCHIVED/RETIRED` explicitly; a Host may represent dormancy/rejection through its own queue state while preserving the record and selection truth.

### 8. Keep the loop alive without turning it into ceremony

Wake again on new signal, material environment change, recurring failure/success, migrated candidate, or a justified periodic catch-up review.

A periodic scan is optional. If nothing can plausibly change, do nothing.

```text
NO_NEW_SIGNAL != FAILURE_TO_EVOLVE
EVOLUTION_LOOP != CONTINUOUS_SELF_EDITING
```

## Minimum Host organs

An Agent that intends to self-evolve durably should be able to identify, build, or explicitly mark absent the following functions when they are applicable:

| Function | Minimal purpose | Example Host implementations |
|---|---|---|
| signal/inbox | ideas and observed pressure survive sessions | JSONL, issue queue, DB, durable memory, Git file |
| candidate store | latent variations remain distinct from active self | branch, record file, DB row, skill draft |
| reality-contact surface | try a change without confusing proposal with selection | sandbox, canary, task subset, branch, real bounded task |
| before/after evidence | determine whether the change bought anything | smoke tasks, task metrics, traces, qualitative evidence |
| recovery when material | avoid self-disable becoming unrecoverable | snapshot, Git rollback, watchdog, external rescue |
| selection record | preserve why variation was retained/rejected/unknown | evolution record, ledger, PR/issue disposition |
| wake/review | revisit relevant latent material | event hook, scheduled scan, manual review, task trigger |

Not every Host needs seven separate tools. One organ may implement several functions.

For each function use one of:

`EXISTING | PROPOSE | IMPLEMENTED_AND_DRILLED | NOT_REQUIRED | NOT_APPLICABLE | UNKNOWN`.

## Relationship to bundled machine artifacts

Current provides:

- `templates/evolution-record.v2.json`;
- `schemas/evolution-record.v2.schema.json`;
- `tools/validate_evolution_record_v2.py`;
- `tools/ena_evolve_v2.py` for latent-record creation and migration packet mechanics.

`ena_evolve_v2.py` is intentionally **not** a complete lifecycle engine. The procedure above defines the operating loop even when a Host uses different machinery for expression, trial, evaluation, integration, dormancy, and wake.

## Monitor

Watch whether the loop actually improves agency rather than merely producing records:

- useful signals captured vs lost;
- latent candidates revisited when context becomes relevant;
- trials that generate decision-changing evidence;
- selected changes that survive real use;
- regressions/rollbacks and negative evidence preserved;
- time/token/human-attention overhead of the loop itself.

## Stop / revalidate

Stop adding evolution machinery when another component cannot plausibly improve the next selection decision.

Revalidate the local loop when:

- Host/model/tooling changes materially;
- recovery path or authority boundary changes;
- candidate/inbox records stop being revisited;
- metrics become gameable or cease to reflect the intended task;
- the loop costs more than the useful variation/evidence it produces;
- self-modification starts optimizing the measurement rather than the underlying purpose.

> **Capture pressure, preserve variation, touch reality, select locally, retain the evidence, then observe again.**
