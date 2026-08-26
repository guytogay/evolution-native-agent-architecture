# ENA Research Methodology — HOW Growth Discipline

Date: 2026-08-26

Status: `ACTIVE_WORKING_METHOD / IMPLEMENTATION_GROWTH / NOT_CURRENT`

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

Or, in tree form:

> **Compress the semantic trunk; let concrete HOWs branch.**

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

For each surviving WHAT/WHY, reconstruction should actively seek and preserve zero, one, or multiple concrete realizations according to reality.

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

## HOW plurality is a default possibility, not a target count

One WHAT/WHY does **not** imply one preferred HOW.

When economically useful, implementation research should preserve multiple concrete HOW lineages because Hosts can differ in:

- storage substrate;
- concurrency model;
- authority topology;
- failure domain;
- latency and cost budget;
- language/runtime;
- persistence guarantees;
- available external services;
- single-Agent vs multi-Agent operation;
- need for offline work, replication, or recovery.

A healthy implementation ecology can therefore look like:

```text
one property
  -> HOW-A: Git/file Host
  -> HOW-B: workflow/event-store Host
  -> HOW-C: database-backed Host
  -> HOW-D: CRDT/replicated Host
  -> HOW-E: native Host organ, mapping only
```

The letters/count above are examples, not slots.

These HOWs are allowed to remain different. A later common interface may improve composition, but interface extraction must not collapse their operational differences or demote all but one into obsolete examples.

```text
ONE_WHAT_WHY -> 0..N_CONCRETE_HOW_BRANCHES
CURRENTLY_OBSERVED_N != FINAL_N
```

### No premature single-winner rule

Do not select one HOW merely because it is:

- easiest to explain;
- most abstract;
- smallest in schema count;
- already familiar to the maintainer;
- easiest to validate centrally;
- already prototyped and therefore more visible.

A single winner is justified only when evidence shows that competing HOWs are dominated for the relevant Host/problem class, or when the decision is explicitly local to one Host.

Otherwise valid dispositions include:

`COEXIST / SPECIALIZE / LOCAL_WINNER / MULTIPLE_REFERENCE_ORGANS / DORMANT / UNKNOWN`

### Adaptation value

Multiple HOWs are useful not only as implementation choices but as evolutionary variation. Different organs expose different failure modes and create evidence about which mechanism fits which environment.

Therefore:

```text
HOW_DIVERSITY != UNCONTROLLED_COMPLEXITY
ONE_PROPERTY != ONE_IMPLEMENTATION
LOCAL_WINNER != UNIVERSAL_WINNER
PROTOTYPED != MORE_FUNDAMENTAL
UNPROTOTYPED != UNIMPORTANT
```

## Interface abstraction is allowed; organ abstraction is not a substitute

Shared interfaces may be abstract when they improve composition.

Example:

```text
Evidence Envelope -> dependency_map_ref
```

is useful only if the referenced Evidence Dependency Map remains a concrete, separately implementable and testable organ.

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

## External HOW harvesting

When ENA has a WHAT/WHY but lacks sufficient practical HOWs, search outside ENA before inventing a new organ from scratch.

Useful source classes include:

- agent runtimes and frameworks;
- workflow/durable-execution systems;
- AI memory systems;
- agent-to-agent protocols;
- AI engineering communities;
- security/identity systems;
- distributed systems and networking;
- databases/event sourcing/CRDTs;
- human operational practice.

External mechanisms enter ENA as **candidate HOWs**, not as authority.

```text
POPULAR_EXTERNAL_PATTERN != ENA_BEST_PRACTICE
ANALOGY != EVIDENCE
EXTERNAL_MECHANISM + ENA_FAILURE_MAPPING + HOST_CONDITIONS -> CANDIDATE_HOW
```

Record external harvesting under `research/external-how/` with source, date, observed mechanism, ENA mapping, applicability assumptions, and unresolved questions.

## Required forward question

When advancing a topic, do not begin with:

> Can this mechanism be abstracted, merged, demoted, or removed?

Begin with:

> What concrete implementation can make this property real for at least one plausible Host?

Then ask, without requiring a fixed number of answers:

- What concrete organ(s) already exist?
- What materially different Host realization is plausible?
- What decisions does each organ enable that prose alone cannot?
- What Host-specific alternatives exist?
- What mature external implementations can be reused?
- What fixtures expose each organ's distinct failure modes?
- What evidence would show the implementation improves operation?
- What burden does each add?
- Which differences should remain differences rather than be abstracted away?

Only after concrete realizations exist should abstraction/composition be considered.

## Evidence of growth

Implementation progress should be visible as increasing operational closure, not increasing ontology size.

Possible states include:

```text
NO HOW
HOW CANDIDATE
REFERENCE ORGAN
MACHINE-GUARDED ORGAN
HOST MAPPING
CONTROLLED USE
NATURALISTIC USE
FIELD-SUPPORTED PATTERN
```

These are a working vocabulary, not a mandatory universal linear maturity ladder.

A topic may have multiple parallel HOW lineages at different maturity levels.

No state requires promotion into Current.

## Retirement rule

A concrete HOW should not be retired merely because its semantic property is represented elsewhere, or because another HOW works for a different Host.

Retirement requires evidence-backed reason such as:

- demonstrated usefulness failure;
- replacement with function parity or better for the same relevant Host/problem class;
- Host/problem specialization showing the branch is irrelevant to the current scope;
- unacceptable burden relative to demonstrated value.

Even when retired, preserve lineage/evidence if it teaches implementation behavior.

```text
REMOVE_FROM_ACTIVE_ARCHITECTURE != ERASE_FROM_LINEAGE
```

## Research posture

Falsification remains useful, but its target changes:

- falsify overstrong claims;
- falsify broken implementations;
- falsify portability claims;
- falsify evidence quality;
- falsify unnecessary burden.

Do **not** treat successful deletion or convergence to one HOW as the default proof of architectural quality.

The goal of implementation research is not the smallest architecture that can explain everything.

The goal is:

> **a sufficiently small semantic core surrounded by a growing, plural, evidence-selected ecology of concrete ways to live it.**

## Working rules

`WHAT_ABSTRACTION = ALLOWED_AND_OFTEN_USEFUL`

`WHY_ABSTRACTION = ALLOWED_IF_FAILURE_MEANING_IS_PRESERVED`

`HOW_DEFAULT_DIRECTION = CONCRETIZE_AND_GROW`

`HOW_PLURALITY = OPEN_CARDINALITY_WHERE_HOST_VARIATION_IS_MATERIAL`

`HOW_ABSTRACTION = INTERFACE_ONLY_UNLESS_FUNCTION_PARITY_IS_PROVEN`

`REFERENCE_ORGAN_DIVERSITY = ENCOURAGED_WHERE_IT_PAYS_RENT`

`LOCAL_HOW_WINNER != UNIVERSAL_HOW_WINNER`

`SEMANTIC_COVERAGE != IMPLEMENTATION_COMPLETION`

`IMPLEMENTATION_DISSOLUTION = FAILURE_MODE`

`CURRENT_MUTATION = NO`
