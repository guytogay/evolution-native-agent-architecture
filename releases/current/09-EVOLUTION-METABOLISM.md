# 9. Evolution Metabolism — v0.3.5

This document turns ENA's evolutionary purpose into an actionable reference loop. It is a reference mechanism, not a mandatory universal implementation.

## 9.1 The metabolism

A viable evolutionary system needs these functions:

1. **Observe** — collect corrections, failures, friction, contradictions, successes, environmental/capability changes, curiosity, and opportunities.
2. **Wake** — create an opportunity to review signals.
3. **Vary** — formulate one or more concrete mutation candidates.
4. **Experiment** — let candidates meet reality inside a suitable Variation Space.
5. **Evaluate** — record observed outcomes, counterevidence, unknowns, and tradeoffs.
6. **Select** — retain, adapt, retry, reject, or keep unknown.
7. **Integrate** — move a selected or explicitly unresolved variation into intended persistent/shared state when the actual authority/consequence boundary permits it.
8. **Prune** — archive, retire, replace, or lawfully delete stale/harmful adaptive material without rewriting its selection history.
9. **Migrate/Recombine** — share source experiments/evaluations/adaptations/negative evidence and combine them into new variation.
10. **Repeat** — selected adaptations change the next search space.

A Host lacking one function may still evolve, but should not narrate the missing function as present.

`variation != improvement`

`experiment != integration`

`lifecycle state != selection state`

`source result != receiver proof`

## 9.2 Wake policy

Use event wake and, where useful, a periodic/idle fallback.

Typical event signals:

`USER_CORRECTION | REPEATED_FAILURE | FRICTION | CONTRADICTION | REPEATED_SUCCESS | CAPABILITY_CHANGE | ENVIRONMENT_CHANGE | OPPORTUNITY | STALE_ADAPTATION`

ENA does not mandate a universal number of turns, hours, or days. A Host chooses cadence proportionate to task tempo, cost, memory pressure, environmental change, dormancy, and the value of missed adaptation opportunities.

**The timer triggers review, not mandatory mutation.**

A review that finds no worthwhile mutation is a valid evolutionary outcome.

## 9.3 Variation Space

A Variation Space answers:

> Where can this uncertain change become real enough to learn from without requiring us to already know it is good?

Examples include a branch/fork, sandbox, disposable VM/container, shadow execution, canary scope, test Agent, reversible local configuration, isolated skill version, or simulation/replay environment.

The space may permit meaningful internal permission/capability changes. Its boundary should expose what may change, who/what bears consequence, what escapes, recovery/cleanup reality, and what external authority remains required.

A Variation Space is not automatically risk-free. It is a deliberately bounded place where uncertainty can contact reality.

## 9.4 Candidate record: two independent state axes

Lifecycle:

`PROPOSED | EXPERIMENTED | INTEGRATED | ARCHIVED | RETIRED`

Selection:

`UNASSESSED | SUPPORTED | PARTIAL | NOT_SUPPORTED | HARMFUL | UNKNOWN`

Examples:

- `INTEGRATED + UNKNOWN` means a bounded unresolved variation was integrated; integration did not prove improvement.
- `ARCHIVED + HARMFUL` means it left the active set but remains harmful evidence.
- `ARCHIVED + SUPPORTED` means a previously supported adaptation is no longer active; archival does not negate its historical selection result.

A useful record also preserves hypothesis, change, expected outcome dimensions, Variation Space, relevant Evolutionary/Protected Subjects, environment, dependencies, unknowns, experiments, evaluations, integration history, and migration provenance.

## 9.5 Evaluation and selection

Record material outcomes as:

`IMPROVED | DEGRADED | UNCHANGED | UNKNOWN`

A result may be mixed.

Any evidence-backed selection verdict other than `UNASSESSED` follows at least one represented experiment. A positive or negative selection claim cannot be manufactured from intention, imported text, or a successful state write alone.

For `SUPPORTED` / `PARTIAL`, represent at least one improved dimension and evidence reference. For `HARMFUL`, represent at least one degraded dimension and evidence reference. The reference tool records these references but does not establish their external truth.

Do not erase failed candidates merely because another candidate won. Do not let a current winner make itself immune to future variation.

## 9.6 Integration

Integration is different from experimentation and from selection.

A candidate that worked in a Variation Space may face a new consequence/authority boundary when entering durable, shared, or production state.

The reference tool requires at least one represented experiment plus a current explicit evaluation before integration. `SUPPORTED` and `PARTIAL` may integrate within actual authority. `UNKNOWN` may integrate only with explicit `--allow-unknown`, preserving `selection_state=UNKNOWN`. Negative or unassessed candidates do not integrate as retained adaptations.

For a committed integration, record the authority basis and recovery/irreversibility boundary. These are recorded claims, not proof that mandate or recovery is externally real.

`INTEGRATED != SUPPORTED`

## 9.7 Pruning and curation

Useful evolution requires forgetting from the active set.

Pruning changes lifecycle state; it does not overwrite selection history.

Do not treat age or low usage alone as sufficient evidence for destructive deletion. Removing an adaptation from active behavior and deleting historical/regulated payload are separate decisions.

## 9.8 Migration packet and population learning

A migration packet preserves, where represented:

- candidate identity and semantic change;
- source lifecycle state;
- source selection state;
- packet purpose: positive adaptation candidate, negative evidence, or unresolved variation;
- source environment and dependencies;
- source experiments and evaluations;
- source integration/archive/migration lineage;
- unknowns;
- content digest for internal consistency.

Packet purpose derives from the **selection axis**, never from lifecycle alone:

`SUPPORTED/PARTIAL -> ADAPTATION_CANDIDATE`

`NOT_SUPPORTED/HARMFUL -> NEGATIVE_EVIDENCE`

`UNASSESSED/UNKNOWN -> UNRESOLVED_VARIATION`

A packet-local digest is **not source authentication**. A party able to rewrite the packet can recompute the digest. Use an external provenance/signature/channel/trust anchor when source authenticity changes the decision.

The v0.3.5 reference CLI rejects three packet self-assertion/shape contradictions rather than relying on JSON Schema alone:

- `source_lifecycle_state` must be a valid lifecycle enum;
- `transfer_status` must remain `TRANSFERRED_SOURCE_EVIDENCE_NOT_LOCAL_PROOF`;
- `source_authentication` must remain `NOT_AUTHENTICATED_BY_THIS_PACKET`.

Changing `source_authentication` to a string such as `TOTALLY_TRUSTED` and recomputing the digest therefore cannot make the packet authenticate itself.

The receiver imports a packet with local `selection_state=UNASSESSED` while preserving source selection/evidence separately.

`TRANSFERRED != LOCALLY_APPLICABLE != LOCALLY_SELECTED`

A receiver may re-experiment even a source `HARMFUL` / `NOT_SUPPORTED` variation because environments differ. If local reality supports it, a new local positive selection may emerge **after local experiment/evaluation**, while the source negative lineage remains visible.

This is population learning without turning migration into conclusion copying.

## 9.9 Recombination and emergence

Recombination is a first-class variation generator.

If A and B are locally useful, do not assume `A + B = A benefit + B benefit`.

Observe conflict, cancellation, amplification, new resource interaction, emergent capability, and new authority/externality surfaces. Positive emergence is evidence when actually observed; expectation of emergence is not evidence.

## 9.10 Governance closure during evolution

Do not recursively review merely because review is possible.

The reference closure tool reads represented evolution state plus explicit caller inputs. Unreviewed signals or an experimented candidate still `UNASSESSED/UNKNOWN` become visible evidence obligations rather than disappearing because the caller omitted them.

Reference outcomes:

`READY | NARROW_AND_PROCEED | EVIDENCE_NEEDED | STOP_OR_ESCALATE`

Its evidence scope is `REPRESENTED_STATE_AND_INPUTS_ONLY`. Even `READY` does **not** prove that no unrepresented real-world blocker exists.

Stop adding governance when the represented decision-changing questions are resolved or honestly bounded and another check would only repeat known information.

## 9.11 Reference tool

`tools/ena_evolve.py` provides:

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

`tools/candidate1_adversarial.py` and `tools/candidate2_adversarial.py` are retained as historical regression fixtures for the validated implementation lineage. Their filenames preserve provenance; they are not active release identities.

The reference tool does not execute arbitrary Host self-mutations, prove external evidence truth, prove authority, prove recovery, or authenticate migration source identity. Machine-readable state is not stronger truth merely because a tool wrote it.

Hosts may modify, embed, or replace the tool if they preserve the required semantic properties better.

## 9.12 Retained field/research residuals

v0.3.5 intentionally carries several visible non-blocking research questions rather than converting every observation into a gate:

- repeated evaluation/reinterpretation of one represented experiment;
- nested visibility of source-negative lineage after receiver positive reselection;
- no in-place restore/reopen path for an archived/retired reference-tool candidate;
- migration-lineage depth growth across generations.

Escalate these only if field evidence demonstrates a material failure mode.

> **Variation first; selection by reality.**
>
> **Do not worship the tool. Improve it.**
