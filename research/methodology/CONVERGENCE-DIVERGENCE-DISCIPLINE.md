# Convergence / Divergence Discipline

Status: `CANONICAL_FOCUSED_METHOD_CANDIDATE / ANTI_ABLATION / OPEN_CARDINALITY / NON_NORMATIVE_TO_CURRENT`

This method exists because LLMs have a strong default tendency to present progress as **summary, simplification, convergence, compression, and closure**.

That tendency is often useful for communication. In ENA research it can also silently destroy the variation that must remain visible for engineering, falsification, Host specialization, and evolution.

The core rule is:

```text
COMPRESS REPRESENTATION
!=
COMPRESS POSSIBILITY SPACE
```

and:

```text
ABSTRACTION MAY COMPRESS DESCRIPTION.
IT MUST NOT SILENTLY REDUCE BEHAVIORALLY DISTINCT VARIATION.
```

## The direction depends on the layer

ENA does not have one universal optimization direction.

```text
WHAT / WHY
    -> abstraction, de-duplication, narrow semantic waist may help

HOW
    -> concretize, branch, specialize, recombine, preserve alternatives

FAILURE / ADVERSARIAL SPACE
    -> expand until materially distinct failure shapes are represented

EVIDENCE / APPLICABILITY
    -> preserve distinctions that change claim strength, transfer, or action

PRESENTATION
    -> summarize freely only if the underlying variation remains durably recoverable
```

A shorter document, smaller test harness, fewer categories, or fewer active organs is not evidence of improvement by itself.

A larger inventory, more branches, more fixtures, or more mechanisms is not evidence of improvement by itself either.

The question is always what decision-relevant structure was preserved, revealed, merged, or lost.

## When convergence/compression is legitimate

Compression is normally healthy when it removes **representation redundancy** without removing a behaviorally distinct possibility.

Examples include:

- duplicate wording that carries the same decision semantics;
- repeated assertions generated mechanically from one failure shape;
- two implementation details already demonstrated to be behaviorally equivalent for the relevant decision;
- a taxonomy axis that never changes routing, action, evidence, lifecycle, or Host binding;
- repeated copies of the same dependency relation;
- moving cold detail out of the hot context while keeping exact retrieval paths;
- retiring a mechanism after its failure coverage is demonstrably replaced and lineage is preserved.

Useful shorthand:

```text
PROVEN_BEHAVIORAL_EQUIVALENCE
    -> MAY_COMPRESS

REPRESENTATIONAL_DUPLICATION
    -> MAY_COMPRESS

NO_DECISION_DIFFERENCE
    -> MAY_MERGE_OR_DEMOTE
```

Even then, the proof/disposition should remain recoverable where future archaeology may need it.

## When divergence/growth is the safer default

Do not converge when the space is still epistemically open or behaviorally distinct.

Divergence is normally required when:

- HOW cardinality is unknown;
- failure cardinality is unknown;
- Host phenotype may change which mechanism works;
- two branches lead to different real actions;
- two branches require different authority, evidence, persistence, recovery, or consequence boundaries;
- a composition seam may create emergent failure not present in either organ alone;
- an untested implementation or abstraction is merely assumed equivalent;
- additional evidence could still change whether a branch is retained, specialized, dormant, retired, or selected;
- a new counterexample exposes structure outside the current categories;
- a translation/projection may preserve prose while changing decision behavior.

Useful shorthand:

```text
UNKNOWN_POSSIBILITY_SPACE
    -> EXPAND

UNPROVEN_EQUIVALENCE
    -> DO_NOT_COLLAPSE

DISTINCT_ACTION_OR_FAILURE
    -> KEEP_SEPARATE

NEW_COUNTEREXAMPLE
    -> ALLOW_MODEL_TO_GROW
```

## Compression requires a variation-disposition map

Before replacing a larger set with a smaller abstraction, map the old variation into the new representation.

For each materially distinct old branch, assertion family, attack, mechanism, or category, record one of:

```text
PRESERVED
MERGED_AS_PROVEN_EQUIVALENT
REPLACED_BY_STRONGER_ORACLE_OR_MECHANISM
RETAINED_AS_DORMANT
RETIRED_WITH_EVIDENCE
LOST
UNKNOWN
```

`LOST` and `UNKNOWN` are not acceptable to silently reinterpret as successful simplification.

```text
SMALLER_RESULT
!=
BETTER_COVERAGE
```

## Special rule for adversarial/falsification work

Tests and adversarial suites live close to HOW and EVIDENCE, not merely presentation.

Therefore their default optimization direction is **not** “fewer assertions”. It is:

> preserve or expand materially distinct attack shapes; compress only redundant execution/representation.

For an old suite with many assertions and a newer smaller suite, do not compare only counts.

Build:

```text
OLD_ASSERTIONS
    -> DISTINCT_FAILURE_SHAPES
    -> disposition per failure shape
    -> NEW_ORACLE_COVERAGE
```

The valid claim is not:

```text
1080 -> 188 -> improvement
```

It is only something like:

```text
old repeated assertions
-> same or stronger distinct failure-shape coverage
-> fewer redundant checks
-> improvement in oracle clarity
```

and that claim requires evidence.

A smaller oracle can be cleaner yet epistemically weaker.
A larger oracle can be broader yet mostly duplicated noise.
Count alone decides neither.

## Special rule for LLM-generated summaries

LLMs often signal confidence and success by producing a compact synthesis.

In ENA research, before accepting such a synthesis, ask:

```text
What disappeared from the previous representation?
Was it only wording, or a concrete HOW / failure / Host condition / residual?
Can every materially distinct predecessor branch still be recovered?
Did UNKNOWN become a neat category or conclusion without new evidence?
Did several mechanisms become one umbrella term merely because they share a parent property?
Did a failed/dormant branch disappear because it was inconvenient to summarize?
```

A summary is a projection, not an ontology.

```text
SUMMARY != COMPLETE_STATE
ELEGANT_SYNTHESIS != SAFE_ABLATION
```

## Growth is not automatically good either

This discipline does not reverse the bias into permanent expansion.

New branches, states, roles, fixtures, axes, and organs must still pay complexity or epistemic rent.

```text
NEW_VARIATION
-> keep when it changes behavior, failure, evidence, Host fit, or future decision
-> merge when equivalence is demonstrated
-> retire when replacement/irrelevance is evidenced
-> preserve lineage either way
```

The desired process resembles evolution rather than either bureaucracy or compression:

```text
EXPRESS
DIVERGE
FALSIFY
RECOMBINE
SPECIALIZE
SELECT
DORMANT
RETIRE
```

Selection happens **after** enough variation is visible to make selection meaningful.

## Operational guard before any major summary or simplification

Before saying a research surface is "cleaner", "simpler", "consolidated", "mature", or "successfully reduced", ask:

```text
1. What exactly is being compressed: text, storage, runtime context, taxonomy, HOWs, or failure space?
2. Which behaviorally distinct variants existed before?
3. Which of them still exist after the change?
4. For every removed distinction, where is the equivalence/replacement evidence?
5. Could any removed distinction still change a real Agent action or validator verdict?
6. Does the new abstraction preserve Host-specific and dormant alternatives?
7. Could new evidence still expand this space?
8. Is the smaller representation being mistaken for a smaller ontology?
```

If those questions cannot be answered, convergence is premature.

## Relationship to the ENA tree discipline

This file sharpens, rather than replaces, the existing rule:

> **Compress the semantic trunk; let concrete HOWs branch.**

More precisely:

```text
SEMANTIC_REDUNDANCY
    -> compress

ENGINEERING_VARIATION
    -> preserve / branch

UNKNOWN_SPACE
    -> explore / expand

PROVEN_EQUIVALENCE
    -> may converge

UNPROVEN_EQUIVALENCE
    -> preserve distinction
```

The purpose is not to maximize branch count.
It is to keep ENA capable of discovering and retaining the concrete variation required for an Agent to actually live by it.
