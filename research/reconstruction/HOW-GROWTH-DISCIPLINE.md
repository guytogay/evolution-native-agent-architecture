# ENA Reconstruction — HOW Growth Discipline

Date: 2026-08-26

Status: `RESEARCH_METHOD / IMPLEMENTATION_GROWTH / NOT_CURRENT`

Related: #89, #88, #90–#94, PR #82.

## Core correction

ENA needs different optimization directions for different layers.

```text
WHAT / WHY
  may benefit from abstraction, semantic compression, de-duplication, and invariant discovery.

HOW
  must not use abstraction as its default improvement direction.
  HOW matures through concrete mechanisms, executable organs, Host mappings, recipes,
  adapters, fixtures, external implementation patterns, and observed operational behavior.

EVIDENCE
  binds claims about both semantics and implementation maturity.
```

A useful shorthand:

> **Compress WHAT. Grow HOW. Select by evidence.**

This is not an instruction to maximize mechanism count. It is an instruction not to confuse conceptual compression with implementation progress.

## Why the prior method drifted toward ablation

Several ENA research habits reward semantic compression:

- `Governance must pay rent`;
- avoid unnecessary Constitution IDs and capability IDs;
- `Standardize the property; discover the organ`;
- prefer minimal shared semantics;
- falsify false confidence and false-BLOCK;
- stop repeated architecture review when no new mechanism appears.

These are useful at the semantic floor, but if applied unchanged to HOW they create an unintended optimization pressure:

```text
specific failure
-> concrete mechanism
-> abstract property
-> Current already covers property
-> mechanism reclassified as Host detail/reference only
-> engineering work stops
-> later only the abstraction remains salient
```

That is not healthy abstraction. It is **implementation dissolution**.

## HOW growth rule

For each surviving WHAT/WHY, the reconstruction should actively seek and preserve one or more concrete realizations.

A HOW may be:

- a state machine;
- a resolver;
- an adapter;
- a workflow;
- a file/layout convention;
- a reference schema;
- an algorithm;
- a protocol mapping;
- a Host integration;
- a test/fixture harness;
- a mature external mechanism mapped to ENA semantics;
- a deliberately small manual procedure where automation is not justified.

A HOW is not complete merely because its interface can be described abstractly.

## Interface abstraction is allowed; organ abstraction is not a substitute

Shared interfaces may be abstract when they improve composition.

Example:

```text
Evidence Envelope -> dependency_map_ref
```

is a useful interface only if the referenced Evidence Dependency Map remains a concrete, separately implementable and testable organ.

The wrong completion claim is:

```text
Evidence Envelope contains dependency_map_ref
therefore Evidence Dependency is solved.
```

The right completion shape is:

```text
shared interface
+ concrete organ(s)
+ Host mapping(s)
+ fixtures/tests
+ evidence boundary
```

## Growth is not mandatory universalization

Growing HOW does not mean every Host must instantiate every organ.

Reference organs may coexist:

```text
one property
-> organ A for file/Git Host
-> organ B for workflow engine
-> organ C for database-backed Agent
-> native Host mechanism requiring only mapping/documentation
```

Diversity is useful information. A later shared interface may emerge from multiple working organs, but the interface does not erase the organs that revealed it.

## HOW plurality is a first-class adaptive property

A surviving WHAT/WHY does **not** need one privileged HOW.

Multiple HOWs are often preferable because Hosts differ in:

- persistence substrate;
- context budget;
- model behavior;
- available tools;
- latency and cost constraints;
- failure domain;
- concurrency model;
- consequence materiality;
- observability;
- organizational authority boundaries.

Therefore the preferred implementation research shape is:

```text
one WHAT / WHY
-> HOW-A
-> HOW-B
-> HOW-C
-> Host-local mapping and selection
-> controlled/naturalistic evidence
```

Examples:

```text
history continuity
-> Git/Merkle-DAG merge
-> causal sibling / dotted-version-vector merge
-> CRDT convergence
-> event-sourced append + reconciliation
```

or:

```text
Hot Cues + Cold Capability
-> generative resident grammar
-> family index
-> interrupt-question kernel
-> Host-native rule engine
```

The goal is not to force these into one universal mechanism. A shared interface may make them comparable or composable, but concrete HOW diversity is itself useful adaptation space.

A single reference organ is therefore **not** sufficient evidence that the HOW problem is closed when materially different Host phenotypes remain plausible.

Retiring HOW-B merely because HOW-A exists is invalid unless one of the normal retirement conditions is met.

## Required forward question

When advancing a topic, do not begin with:

> Can this mechanism be abstracted, merged, demoted, or removed?

Begin with:

> What concrete implementation can make this property real for at least one plausible Host?

Then ask:

1. Can we build or map one real organ?
2. What alternative HOW phenotypes could make the same property real under different Host constraints?
3. What decisions does each HOW enable that prose alone cannot?
4. What Host-specific alternatives exist?
5. What external mature implementations can be reused?
6. What fixtures expose each HOW's characteristic failure modes?
7. What evidence would show it improves operation?
8. What burden does it add?
9. Where should local selection choose among coexisting HOWs rather than universalizing one?

Only after concrete realizations exist should abstraction/composition be considered.

## Evidence of growth

Implementation progress should be visible as increasing operational closure, not increasing ontology size.

Possible growth indicators:

```text
NO HOW
-> HOW CANDIDATE
-> REFERENCE ORGAN
-> MACHINE-GUARDED ORGAN
-> HOST MAPPING
-> CONTROLLED USE
-> NATURALISTIC USE
-> FIELD-SUPPORTED PATTERN
```

A topic may have multiple parallel HOW lineages at different maturity levels.

No stage requires promotion into Current.

## Retirement rule

A concrete HOW should not be retired merely because its semantic property is represented elsewhere or because another HOW exists.

Retirement requires one of:

1. demonstrated usefulness failure;
2. replacement with function parity or better for the relevant Host/problem class;
3. Host/problem specialization proving it is no longer relevant outside that niche;
4. unacceptable burden relative to demonstrated value.

Even when retired, preserve lineage/evidence if it teaches implementation behavior.

## Research posture

Falsification remains useful, but its target changes:

- falsify overstrong claims;
- falsify broken implementations;
- falsify portability claims;
- falsify evidence quality;
- falsify unnecessary burden;
- compare competing HOW phenotypes without assuming one universal winner.

Do **not** treat successful deletion as the default proof of architectural quality.

The goal of implementation research is not the smallest architecture that can explain everything.

The goal is:

> **a sufficiently small semantic core surrounded by a growing, evidence-selected ecology of concrete ways to live it.**

## Working rules

`WHAT_ABSTRACTION = ALLOWED_AND_OFTEN_USEFUL`

`WHY_ABSTRACTION = ALLOWED_IF_FAILURE_MEANING_IS_PRESERVED`

`HOW_DEFAULT_DIRECTION = CONCRETIZE_AND_GROW`

`HOW_ABSTRACTION = INTERFACE_ONLY_UNLESS_FUNCTION_PARITY_IS_PROVEN`

`ONE_WHAT_MAY_HAVE_MULTIPLE_HOWS = YES`

`MULTIPLE_HOWS_MAY_COEXIST_LONG_TERM = YES`

`HOST_LOCAL_HOW_SELECTION = EXPECTED`

`REFERENCE_ORGAN_DIVERSITY = ALLOWED_AND_VALUABLE`

`ONE_REFERENCE_ORGAN != HOW_SPACE_CLOSED`

`SEMANTIC_COVERAGE != IMPLEMENTATION_COMPLETION`

`IMPLEMENTATION_DISSOLUTION = FAILURE_MODE`

`CURRENT_MUTATION = NO`
