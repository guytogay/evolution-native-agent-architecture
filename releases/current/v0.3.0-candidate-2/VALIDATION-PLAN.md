# ENA v0.3.0 Candidate 2 — ROI Validation Plan

Status: `CANDIDATE / VALIDATION_PLAN`

## Validation funnel

Use the cheapest stage capable of changing the decision.

```text
V0  Reasoning / consistency
V1  Static or machine checks
V2  Historical Adversarial Replay / synthetic attack
V3  Cheap disposable host/model experiment
V4  Shadow production
V5  Canary enforcement
V6  Normal production
V7  Independent-host replication when decision-critical
```

Do not require every candidate family to reach V7 before production.

## Decision-branch requirement

Before an experiment, record:

- If PASS, what decision may change?
- If FAIL, what decision may change?
- If UNKNOWN, what decision or evidence request follows?

If no outcome can materially change a decision, defer the experiment.

## Validation order

### Batch 1 — Production Core

1. Claim ↔ Evidence Support
2. Triggered Material Obligation Closure
3. Recovery-History Monotonicity
4. Capability/Route Binding

These receive strong machine/static testing first because they directly affect consequential claims and recovery.

### Batch 2 — Shadow economics and behavior

Observe in real workloads:

- added model calls;
- added tool calls;
- token/API cost where observable;
- wall-clock delay;
- human review time;
- retries/rework;
- prevented failures;
- false positive friction;
- field feedback volume;
- evidence reuse.

Do not collapse these into one universal score.

### Batch 3 — Cross-host falsification

Promote or harden a candidate only when the decision requires it.

Prefer independent recurrence across different host/model/task topologies before adding new Universal semantics.

## Production feedback as evidence

Production observations are evidence with scope and provenance, not automatic global truth.

A field incident must not be generalized beyond the host/model/route/task/consequence envelope it actually supports unless a separate transfer/equivalence/invariance relation is evidenced.

## Stop conditions

Pause a candidate mechanism when it causes material false completion/safety claims, prevents legitimate recovery, silently erases history, creates unresolved obligation explosion, adds cost/latency that destroys viable agency without proportional value, or makes unsupported authority look justified.

## Success condition

The objective is not maximum validation.

The objective is the lightest evidence and governance that honestly support the consequence and claims required for useful production.
