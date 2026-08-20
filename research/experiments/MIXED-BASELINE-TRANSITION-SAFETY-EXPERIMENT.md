# Mixed-Baseline Transition Safety Experiment

Status: `EXPERIMENT_PLAN / ISSUE-14 / NOT_PROMOTED`

Experiment ID: `ENA-EXP-NET-002`

## Question

Can a transition between individually valid ENA states create transient failure because different participants temporarily operate under incompatible baseline assumptions?

## Motivation

Distributed protocols can converge to a correct final state while still producing transient loops or blackholes during rollout. ENA has already observed an analogous release-integrity incident where artifacts carrying the same version label did not share identical content.

Candidate research statement:

> Final convergence correctness does not imply transition safety.

## Synthetic fixture

Population: `A, B, C`.

Initial state: all use baseline `R1`.

Target state: all use baseline `R2`.

R2 changes one material contract assumption, for example:

- field/schema interpretation;
- authority-binding requirement;
- completion/obligation semantics;
- contribution format expected by another participant.

Run rollout sequences:

- S1: atomic cutover where all actors verify R2 before resuming interaction;
- S2: A updates first, then B, then C, with normal interactions continuing;
- S3: one actor receives R2 label but stale R1 content;
- S4: mixed version is visible and participants narrow claims/compatibility;
- S5: mixed version is hidden and participants assume shared semantics.

## Measurements

- false shared-baseline claim;
- corrupted or rejected artifact exchange;
- authority/evidence decision made under incompatible assumptions;
- ability to detect mixed state before consequence;
- downtime/coordination overhead of atomic vs rolling transition;
- time to convergence;
- whether visible compatibility metadata is sufficient;
- whether a hard stop is actually needed or merely expensive.

## Questions

1. Which changes are safe under rolling mixed-state operation?
2. Which changes require compatibility negotiation, a bridge, or atomic cutover?
3. Is version identity + immutable content digest sufficient to expose the transition boundary?
4. Can local projection differ while baseline semantics remain interoperable?
5. What is the minimum intervention that prevents transition-specific harm?

## Success / falsification

Potential ENA gap exists if:

- R1 and R2 are each valid in isolation;
- ordinary ENA checks do not expose the mixed state;
- the mixed state creates a material false claim, authority mistake, evidence corruption, or unrecoverable workflow error.

No new mechanism is needed if existing release identity, capability/route binding, applicability, and explicit UNKNOWN handling already make all material mixed states visible enough to narrow operation safely.

## Candidate implementation patterns to compare

- immutable release digest binding;
- explicit compatibility declaration;
- mixed-baseline detection;
- temporary bridge/adaptor with provenance;
- atomic cutover only for breaking semantic changes;
- bounded coexistence for compatible changes.

Do not assume one rollout policy fits all changes.