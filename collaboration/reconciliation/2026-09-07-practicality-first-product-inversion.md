# Practicality-First Product Inversion — v0.3.15 candidate input

Status: `ACTIVE / ADVANCE_NOW / R1_CANDIDATE_INPUT`

Findings:

- `F-208-15_THEORY_FIRST_ADOPTER_SURFACE_WEAKENS_PRACTICAL_UTILITY`
- `F-208-16_DERIVATION_TAX_SPENDS_RUNTIME_ATTENTION_PROVING_BOUNDARIES_INSTEAD_OF_ENABLING_ACTION`

## Owner observation

ENA currently spends too much adopter-facing attention on theory and on explaining why distinctions are true. This can produce a package that is intellectually defensible but practically weak.

Analogy:

> A book may truthfully say that cabbage is not radish, rain is not flood, and Rome is not Romania. It can then spend pages proving why those distinctions are correct. The reader may agree with every sentence and still have no useful guidance for what to do.

The relevant product question is not whether a distinction is true. It is what problem the distinction helps an Agent solve and what action becomes possible because the distinction is known.

## Current evidence

Current `05-CORE-OPERATIONAL-CONTRACTS.md` opens with release-lineage inheritance narration and repeatedly develops distinctions such as:

```text
claim != evidence != support relation
restore != complete history
backup exists != recovery proven
local validity != composed validity
cancel != stop-new-work != revoke-authority != rollback != compensate
```

Many of these distinctions are important semantic boundaries, but substantial adopter-facing prose is spent explaining why the boundaries hold. That material is useful for research, audit, falsification, dispute resolution, and maintainer reasoning; it is not automatically useful as an operational interface.

`00-READ-ME-FIRST.md` and `ADOPTER-QUICKSTART.md` correctly keep research lineage cold, but the product still remains theory-centered: the default hot payload is a semantic cue surface and practical HOW is reached only after the Agent translates abstract semantics into an operational problem.

## F-208-15 — theory-first product architecture

Current practical path is effectively:

```text
SEMANTIC THEORY / BOUNDARY
-> AGENT INTERPRETS WHAT PROBLEM THIS MEANS
-> CUE-INDEX
-> HOW-MAP
-> PROCEDURE
-> HOST-LOCAL ACTION
```

Target product path should invert this:

```text
PROBLEM / GOAL
-> WHAT TO DO NOW
-> HOW TO TELL IF IT WORKED
-> WHEN TO STOP / REVALIDATE
-> OPTIONAL WHY / THEORY / LINEAGE
```

Theory is retained, but becomes cold explanatory/reference material rather than the primary adopter experience.

## F-208-16 — derivation tax

A distinction does not deserve repeated explanatory cost merely because it is true.

For adopter-facing surfaces, the default should be:

```text
BOUNDARY
-> ACTION CONSEQUENCE
-> OPTIONAL DEEP RATIONALE
```

not:

```text
BOUNDARY
-> MULTI-PARAGRAPH PROOF OF WHY THE BOUNDARY IS TRUE
-> ANOTHER BOUNDARY
-> ANOTHER PROOF
```

A rationale belongs in the practical surface only when at least one is true:

- the boundary is materially counterintuitive;
- misapplication is likely without the rationale;
- the rationale changes applicability, action, monitoring, or stop conditions;
- the rationale is necessary to preserve a high-consequence semantic property;
- there is no cheaper representation that preserves correct action.

Otherwise move the derivation to cold theory/lineage/reference material.

## Practical unit: action card

A primary adopter-facing ENA unit should normally answer:

```text
PROBLEM / TRIGGER
WHAT TO DO NOW
WHAT TO OBSERVE
WHAT COUNTS AS BETTER / WORSE / STILL UNKNOWN
WHEN TO STOP / ROLLBACK / REVALIDATE
OPTIONAL WHY / THEORY / PROVENANCE
```

The theory link may point to Constitution IDs, contract rationale, research evidence, lineage, or falsification history. It should not be required merely to execute the useful behavior.

Example:

```text
Problem: imported adaptation worked on another Host but not yet here.
Do now: keep it as a local candidate; identify material Host differences; run the cheapest receiver-local test that can change the adoption decision.
Observe: task outcome, compatibility, side effects, cost, recovery impact.
Stop/select: integrate supported scope; narrow partial value; reject harmful/not-supported result; preserve UNKNOWN when no useful next observation exists.
Why: source success != receiver-local proof. [cold theory link]
```

The final `Why` is supporting material, not the product center.

## Product-layer inversion

Candidate structure:

### Layer A — practical interface

Problem/goal/action cards and action routing. This should be the primary adopter experience.

### Layer B — compact semantic floor

Only boundaries that materially prevent wrong action or loss of future agency; each boundary should connect directly to an action bridge.

### Layer C — cold HOW library

Reusable procedures and Host-neutral implementation patterns.

### Layer D — cold theory / derivation / evidence / lineage

Constitution detail, semantic derivations, research history, falsification records, migration history, and why a rule exists.

```text
PRACTICE_FIRST != THEORY_DELETED
THEORY_AVAILABLE != THEORY_MUST_BE_READ
CORRECT_STATEMENT != USEFUL_PRODUCT_UNIT
DERIVATION_HISTORY != ADOPTION_REQUIREMENT
```

## Deletion / utility test for adopter-facing prose

For each paragraph in the primary adopter path ask:

1. What real problem does this help solve?
2. What action/decision changes because the Agent read it?
3. Would removing it materially increase wrong action, lost capability, or irrecoverable/evidence/authority error?
4. If the answer is only "it explains why the rule is true", can it move to cold theory/reference?

If no concrete action or protection changes, the paragraph has not demonstrated rent on the practical surface.

## Relation to F-208-13 / F-208-14 / PR #224

F-208-13 found defensive-first hot salience despite an agency-first Constitution.

F-208-14 found that `X != Y` distinctions do not uniquely determine HOW and require an Action Bridge.

F-208-15/16 broaden the diagnosis: the issue is not only the wording of the Runtime Kernel. The adopter-facing product architecture itself must become practice-first and stop charging derivation cost for theory that is not needed at the point of action.

PR #224 therefore should not be resolved by expanding nineteen distinctions into nineteen long trigger-rule explanations. The better direction is to reduce semantic prose, connect material boundaries to compact action bridges, keep real HOW cold/on-demand, and move deeper rationale to cold theory/evidence surfaces.

## Candidate success criteria

A v0.3.15 practical product candidate should let a capable fresh Agent answer, without research-history reading:

- What can ENA help me do?
- Which real problem am I facing?
- What is the smallest useful next action?
- Which HOW should I retrieve only if needed?
- How do I know whether the action helped?
- When should I stop, integrate, narrow, reject, rollback, or leave something unknown?

It should not require the Agent to read a derivation of every semantic distinction before gaining practical value.
