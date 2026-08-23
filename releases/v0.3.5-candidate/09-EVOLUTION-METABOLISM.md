# 9. Evolution Metabolism

This document turns ENA's evolutionary purpose into an actionable reference loop.

It is a reference mechanism, not a mandatory universal implementation.

## 9.1 The metabolism

A viable evolutionary system needs these functions:

1. **Observe** — collect corrections, failures, friction, contradictions, successes, environmental/capability changes, curiosity, and opportunities.
2. **Wake** — create an opportunity to review signals.
3. **Vary** — formulate one or more concrete mutation candidates.
4. **Experiment** — let candidates meet reality inside a suitable Variation Space.
5. **Evaluate** — record observed outcomes, counterevidence, unknowns, and tradeoffs.
6. **Select** — retain, adapt, retry, reject, or keep unknown.
7. **Integrate** — move a selected adaptation into intended persistent/shared state when the actual authority/consequence boundary permits it.
8. **Prune** — archive, dormant, retire, replace, or lawfully delete stale/harmful adaptive material.
9. **Migrate/Recombine** — share evidence-bearing adaptations/negative evidence and combine them into new variation.
10. **Repeat** — selected adaptations change the next search space.

A Host lacking one function may still evolve, but should not narrate the missing function as present.

`variation != improvement`

`experiment != integration`

`source adaptation != receiver proof`

## 9.2 Wake policy

Use both kinds where useful.

### Event wake

Typical signals:

`USER_CORRECTION | REPEATED_FAILURE | FRICTION | CONTRADICTION | REPEATED_SUCCESS | CAPABILITY_CHANGE | ENVIRONMENT_CHANGE | OPPORTUNITY | STALE_ADAPTATION`

Event wake should be cheap enough that useful learning signals are not lost.

### Periodic/idle wake

Periodic review is a fallback against slow drift and missed patterns.

ENA does not mandate a universal number of turns, hours, or days. The Host should choose a cadence proportionate to task tempo, cost, memory pressure, environmental change, dormancy, and the value of missed adaptation opportunities.

**The timer triggers review, not mandatory mutation.**

A review that finds no worthwhile mutation is a valid evolutionary outcome.

## 9.3 Variation Space

A Variation Space answers:

> Where can this uncertain change become real enough to learn from without requiring us to already know it is good?

Examples include a branch/fork, sandbox, disposable VM/container, shadow execution, canary scope, test Agent, reversible local preference/configuration, isolated skill version, or simulation/replay environment.

The space may permit meaningful internal permission/capability changes. The boundary should identify:

- what may change;
- who/what can bear consequence;
- what escapes the experiment;
- recovery/cleanup reality;
- what external authority still remains required.

A Variation Space is not automatically a risk-free space. It is a deliberately bounded place where uncertainty can contact reality.

## 9.4 Candidate record

A useful candidate states:

- signal(s) that motivated it;
- hypothesis;
- proposed change;
- expected outcome dimensions;
- Variation Space;
- Evolutionary Subject where decision-relevant;
- Protected Subjects;
- source environment;
- dependencies;
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

A positive selection claim requires represented observed outcome(s) and evidence reference(s). The reference tool records those references but does not establish the external truth of the evidence itself.

Do not erase failed candidates merely because another candidate won. Do not let a current winner make itself immune to future variation.

## 9.6 Integration

Integration is different from experimentation.

A candidate that worked in a Variation Space may face a new consequence/authority boundary when entering durable, shared, or production state.

Internal self-structure may be autonomously integrated where the actual local mandate allows it. External authority cannot be created by editing the Agent's own permission map.

The reference tool normally records integration only for `SUPPORTED` or `PARTIAL` candidates. A genuinely unresolved candidate may be integrated only after it has actually been experimented/evaluated and the unresolved state plus narrowed consequence is explicit. A merely `PROPOSED` candidate cannot use uncertainty as a shortcut around reality contact.

At integration time, represent the actual authority basis and recovery/irreversibility boundary. The tool records these claims; it does not verify that the claimed mandate or recovery mechanism is real.

## 9.7 Pruning and curation

Useful evolution requires forgetting from the active set.

Possible lifecycle:

`ACTIVE -> DORMANT -> ARCHIVED -> RESTORED/RETIRED`

Inputs may include recency, actual use, observed value, conflicts, maintenance burden, replacement by a stronger adaptation, user/owner protection, and legal retention/deletion requirements.

Do not treat age or low usage alone as sufficient evidence for destructive deletion.

Pruning active behavior and deleting historical/regulated payload are separate decisions.

## 9.8 Migration packet and population learning

A transferable packet should preserve:

- candidate/adaptation identity;
- semantic intent/change;
- source selection status;
- whether the packet is a positive adaptation candidate, negative evidence, or unresolved variation;
- source Host/model/language/configuration;
- source evaluations/evidence references;
- improved/degraded/unknown dimensions;
- dependencies;
- authority/recovery assumptions where material;
- known failure modes;
- transfer unknowns;
- a content digest for internal consistency / accidental-change detection.

A packet-local digest is **not source authentication** and is not an external trust anchor: a party able to rewrite the packet can also recompute the digest. When source identity/authenticity changes a consequential decision, preserve or verify an external provenance/signature/channel/trust anchor appropriate to that decision.

The receiver does **not** inherit local proof by receiving a file.

`TRANSFERRED != LOCALLY_APPLICABLE != LOCALLY_SELECTED`

For a supported source adaptation, the receiver imports it as a migration candidate and may use differential local testing: test material source/receiver differences rather than replaying the entire discovery history when not needed.

A source `HARMFUL` or `NOT_SUPPORTED` result may still spread as valuable **negative evidence**, but must not be relabeled a positive adaptation merely because it crossed a Host boundary.

Migration is how individual learning can accelerate population evolution without pretending that one environment proves all environments.

## 9.9 Recombination and emergence

Recombination is a first-class variation generator.

If A and B are locally useful, do not assume:

`A + B = A benefit + B benefit`

Observe conflict, cancellation, amplification, new resource interaction, emergent capability, and new authority/externality surfaces.

Composition-level validation is also composition-level exploration. Positive emergence should be recorded as evidence, not dismissed as accidental noise; negative interaction remains equally real.

## 9.10 Governance closure during evolution

Do not recursively review merely because review is possible.

Continue governance when a bounded next check/action can plausibly change a material decision. Stop adding governance when represented decision-changing questions are resolved or honestly bounded and another review would only repeat known information.

Reference semantic outcomes:

`READY | NARROW_AND_PROCEED | EVIDENCE_NEEDED | STOP_OR_ESCALATE`

A generic tool cannot prove that a caller omitted no blocker. Therefore the reference tool reports the scope explicitly as `REPRESENTED_INPUTS_ONLY`; a `READY` output means ready **only if the represented inputs are materially complete**.

## 9.11 Reference tool

`tools/ena_evolve.py` provides a small standard-library reference implementation:

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

The tool records evolution state/evidence boundaries. It deliberately does not execute arbitrary Host self-mutations, verify external evidence truth, prove authority, prove recovery, authenticate migration source identity, or infer that unrepresented blockers do not exist.

It is intended to be taken, modified, embedded, or replaced by Hosts that can implement the same properties better.

> **Variation first; selection by reality.**
>
> **Do not worship the tool. Improve it.**
