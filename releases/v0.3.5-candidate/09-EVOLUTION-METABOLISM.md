# 9. Evolution Metabolism

This document turns ENA's evolutionary purpose into an actionable reference loop.

It is a reference mechanism, not a mandatory universal implementation.

## 9.1 The metabolism

A viable evolutionary system needs all of these functions:

1. **Observe** — collect corrections, failures, friction, contradictions, successes, environmental changes, capability changes, and opportunities.
2. **Wake** — create an opportunity to review signals.
3. **Vary** — formulate one or more concrete mutation candidates.
4. **Experiment** — let candidates meet reality inside a suitable Variation Space.
5. **Evaluate** — record observed outcomes and tradeoffs.
6. **Select** — retain, adapt, retry, reject, or keep unknown.
7. **Integrate** — move a selected adaptation into the intended persistent/shared state when actual authority and consequence permit it.
8. **Prune** — archive/dormant/retire stale or harmful adaptations.
9. **Migrate/Recombine** — share supported adaptations as migration candidates and combine them into new variation.
10. **Repeat** — selected adaptations change the next search space.

A Host lacking one function may still evolve, but should not narrate the missing function as present.

## 9.2 Wake policy

Use both kinds where useful:

### Event wake

Typical signals:

`USER_CORRECTION | REPEATED_FAILURE | FRICTION | CONTRADICTION | REPEATED_SUCCESS | CAPABILITY_CHANGE | ENVIRONMENT_CHANGE | OPPORTUNITY | STALE_ADAPTATION`

Event wake should be cheap enough that useful learning signals are not lost.

### Periodic/idle wake

Periodic review is a fallback against slow drift and missed patterns.

ENA does not mandate a universal number of turns/hours/days.

The Host should choose a cadence proportionate to:

- task tempo;
- cost;
- memory pressure;
- rate of environmental change;
- dormancy;
- value of missed adaptation opportunities.

**The timer triggers review, not mandatory mutation.**

## 9.3 Variation Space

A Variation Space is the answer to:

> Where can this uncertain change become real enough to learn from without requiring us to already know it is good?

Examples:

- branch or fork;
- sandbox;
- disposable VM/container;
- shadow execution;
- canary scope;
- test Agent;
- reversible local preference/configuration;
- isolated skill version;
- simulated or replay environment.

The space may permit meaningful internal permission changes.

The boundary should identify:

- what may change;
- who/what can bear consequence;
- what escapes the experiment;
- recovery/cleanup reality;
- what external authority still remains required.

## 9.4 Candidate record

A useful candidate states:

- signal(s) that motivated it;
- hypothesis;
- proposed change;
- expected outcome(s);
- Variation Space;
- Protected Subjects;
- source environment;
- material unknowns;
- how results will be observed.

Do not require a prediction of universal goodness.

## 9.5 Evaluation and selection

Evaluate the candidate against actual outcomes.

Record material dimensions as:

`IMPROVED | DEGRADED | UNCHANGED | UNKNOWN`

A result may be mixed.

Candidate selection state:

`SUPPORTED | PARTIAL | NOT_SUPPORTED | HARMFUL | UNKNOWN`

Do not erase failed candidates merely because another candidate won.

Do not let a current winner make itself immune to future variation.

## 9.6 Integration

Integration is different from experimentation.

A candidate that worked in a Variation Space may still face a new consequence/authority boundary when entering durable/shared/production state.

Internal self-structure may be autonomously integrated where the actual local mandate allows it.

External authority cannot be created by editing the Agent's own permission map.

## 9.7 Pruning and curation

Useful evolution requires forgetting from the active set.

Possible lifecycle:

`ACTIVE -> DORMANT -> ARCHIVED -> RESTORED/RETIRED`

Inputs may include:

- recency;
- actual use;
- observed value;
- conflicts;
- maintenance burden;
- replacement by stronger adaptation;
- user/owner protection;
- legal retention/deletion requirements.

Do not treat age or low usage as sufficient evidence for destructive deletion.

## 9.8 Migration packet

A transferable packet should preserve:

- candidate/adaptation identity;
- semantic intent;
- source Host/model/language/configuration;
- source evidence;
- improved/degraded/unknown dimensions;
- dependencies;
- authority assumptions;
- known failure modes;
- transfer unknowns.

The receiver imports it as a migration candidate.

Prefer differential local testing: test the material source/receiver differences rather than replaying the entire discovery history when not needed.

## 9.9 Recombination and emergence

Recombination is a first-class variation generator.

If A and B are locally useful, do not assume:

`A + B = A benefit + B benefit`

Observe:

- conflict;
- cancellation;
- amplification;
- new resource interaction;
- emergent capability;
- new authority/externality surface.

Positive emergence should be recorded as evidence, not treated as accidental noise.

## 9.10 Reference tool

`tools/ena_evolve.py` provides a small standard-library implementation:

```text
init
observe
review
propose
experiment
evaluate
integrate
archive
export
import
closure
status
selftest
```

The tool records evolution state. It deliberately does not execute arbitrary Host self-mutations and does not mint authority.

It is intended to be taken, modified, embedded, or replaced by Hosts that can implement the same properties better.

> **Do not worship the tool. Improve it.**
