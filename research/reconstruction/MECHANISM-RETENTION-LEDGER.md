# ENA Reconstruction — Mechanism Retention Ledger

Status: `RESEARCH_GOVERNANCE / ANTI_ABLATION_GUARD / NOT_CURRENT`

Related: #89, #90, #91, #92, #93, #94, PR #82.

Purpose:

> Preserve concrete engineering value while ENA semantics are reconciled, compressed, or generalized.

This ledger exists because a mechanism can be semantically redundant yet operationally indispensable.

```text
SEMANTICALLY_COVERED
!= IMPLEMENTATION_HOW_PRESERVED
!= REFERENCE_ORGAN_AVAILABLE
!= HOST_MAPPED
!= MACHINE_TESTED
!= FIELD_SUPPORTED
```

A reconciliation that reduces ontology but removes the practical route from property to implementation is a **degradation**, not automatically an improvement.

This ledger also follows `CARDINALITY-DISCOVERY-GUARD.md`:

```text
REQUESTED_N != DISCOVERED_N
PRESENTATION_N != ONTOLOGY_N
CURRENTLY_OBSERVED_N != FINAL_N
```

Counts below describe mechanisms currently identified or implemented unless an exact count is explicitly stated to be normative.

## Disposition vocabulary

- `KEEP` — mechanism remains useful as represented.
- `REPAIR` — mechanism remains useful but has a material defect.
- `SPECIALIZE` — keep for a narrower Host/problem family.
- `KEEP_AS_REFERENCE_ORGAN` — not universally mandated, but preserved as an official implementation pattern.
- `KEEP_AS_HOST_PATTERN` — useful local organ; no cross-Host standard implied.
- `REPLACE_WITH_EQUIVALENT_HOW` — removal permitted only with demonstrated function parity.
- `COEXIST` — multiple organs remain valid phenotypes.
- `RETIRE_AFTER_USEFULNESS_FAILURE` — retirement justified by evidence that the mechanism no longer changes a useful decision or is dominated by a cheaper equivalent.

`ALREADY_COVERED`, `HOST_ORGAN`, `REFERENCE_ONLY`, or `INTERPRETATION_ONLY` are **not terminal dispositions by themselves**.

## Required anti-degradation check

Before downgrading/removing a concrete HOW, record:

1. the practical failure it currently prevents;
2. the exact mechanism being removed or weakened;
3. the proposed replacement, if any;
4. whether a fresh Host can still implement the property without reconstructing the removed mechanism from first principles;
5. function-parity evidence or a demonstrated usefulness failure;
6. new false-BLOCK / burden introduced by the replacement;
7. whether the change merely shrinks ontology while increasing implementation ambiguity.

If these cannot be answered, preserve the mechanism and mark the abstraction/reconciliation as incomplete.

Before imposing or preserving an exact number of mechanisms/HOWs/cases, also ask:

1. is this count normative in the domain, or merely currently observed?
2. would another materially distinct item be accepted if reality produced it?
3. would fewer items be accepted if distinctions collapse without function loss?
4. is a test asserting useful coverage, or merely asserting yesterday's inventory size?

---

# Active retained mechanisms

## MRL-001 — Memory Metabolism reference recomposition

**Problem**

Long-horizon experience can become raw-log accumulation, provenance loss, stale knowledge, autobiography laundering, or ungoverned behavior change.

**Retained HOW**

Memory-class isolation; occurrence vs derived-state separation; compilation/consolidation; supersession; provenance; revalidation; pruning/dormancy/archive; retrieval boundary; memory compilation distinct from behavioral admission.

**Current status**

`KEEP_AS_REFERENCE_ORGAN / RESEARCH_PROTOTYPE`

**Why semantic coverage is insufficient**

Current already contains many of the constituent properties, but a Host still needs a coherent lifecycle showing how experience becomes durable knowledge and possibly later adaptation without manufacturing truth or authority.

**Do not downgrade to**

`CAP-056/CAP-064/CAP-076 already cover memory; therefore Memory Metabolism has no implementation value.`

**Evidence boundary**

Multiple adversarial iterations + reconciliation exist; cross-Host field fitness remains incomplete.

---

## MRL-002 — Retrieval Obligation / scope discovery

**Problem**

Relevant durable state can exist while the Agent never invokes retrieval, searches the wrong scope, or treats a hit as sufficient.

**Retained HOW**

`INVOCATION -> SCOPE DISCOVERY -> RETRIEVAL -> SUFFICIENCY`, subject-bound sufficiency, honest no-hit/failure states, exact-path fallback where semantic index fails.

**Current status**

`KEEP_AS_REFERENCE_ORGAN / ARCHITECTURE_ITERATION_STOPPED / NATURALISTIC_EVIDENCE_OPEN`

**Do not downgrade to**

`ADOPTION != RETRIEVAL is already written, therefore no retrieval organ is needed.`

**Retention reason**

The property does not tell a finite-context Host how to discover cold scope or bind sufficiency to the effective subject.

---

## MRL-003 — Decision Projection / cross-stage subject binding

**Problem**

A retrieval-sufficient superset can be reduced into a decision-insufficient projection while every stage remains locally valid.

**Retained HOW**

Bind consequential closure to the effective subject actually used after decision-material lossy transformation.

**Current status**

`KEEP_AS_REFERENCE_COMPOSITION_RULE / FIXTURE_SUPPORTED / NATURALISTIC_EVIDENCE_OPEN`

**Do not downgrade to**

`retrieval sufficiency already handles this.`

**Retention reason**

The failure occurs specifically at the interface between otherwise-valid stages.

---

## MRL-004 — Tiny Hot Kernel phenotypes

**Problem**

A finite Agent cannot keep all ENA semantics hot; cold semantics have no value if the Agent never recognizes when to retrieve them.

**Retained HOW**

Currently implemented competing resident recognizers include:

- `K-A` generative consequence grammar;
- `K-B` seven-family advertised index;
- `K-C` minimal interrupt questions.

Shared downstream Semantic Router; blind fixture corpus; controlled runner; oracle isolation.

The currently implemented recognizer count is descriptive, not a closed taxonomy.

**Current status**

`COEXIST / CONTROLLED_SELECTION_PENDING / ORACLE_INDEPENDENT_REVIEW_PENDING`

**Do not downgrade to**

`Hot Cues + Cold Capability is already in Current, so kernel implementation is a Host detail.`

**Retention reason**

Current names the property but does not establish which compact recognizer phenotype actually survives finite-context operation economically.

**Removal condition**

Only after an alternative recognizer/router arrangement demonstrates equal-or-better recall/fallback/context behavior for the relevant Host class, or controlled/naturalistic evidence shows the organ adds no decision value.

---

## MRL-005 — Semantic Router

**Problem**

A cue can fire yet still fail because the Agent cannot map the decision shape to the right cold canonical semantics.

**Retained HOW**

`decision shape -> semantic family -> exact Current target -> bounded cold read -> sufficiency/fallback -> projection`.

**Current status**

`KEEP_AS_REFERENCE_ORGAN / MACHINE_TARGET_REACHABILITY_GUARDED`

**Do not downgrade to**

`the Agent can search the repo itself.`

**Retention reason**

Unbounded repository search is not equivalent to a bounded decision-oriented resolver and can fail differently across Hosts.

---

## MRL-006 — Effect Intent / Attempt / Receipt / Commitment

**Problem**

Timeout, retry, restore, fork, or compensation can duplicate external consequences when local state is mistaken for world state.

**Retained HOW**

Separate logical effect intent, execution incarnation, external settlement evidence, and current execution responsibility. Preserve `UNKNOWN` and query/manual-reconciliation paths. Compensation is a new effect, not historical erasure.

**Current status**

`KEEP_AS_REFERENCE_ORGAN / DETERMINISTIC_MACHINE_GUARDED / INDEPENDENT_SELECTION_REVIEW_NEXT`

**Do not downgrade to**

`state rollback != consequence rollback already exists in Constitution, therefore no effect lifecycle organ is needed.`

**Retention reason**

The Constitution property does not itself tell a Host whether a timeout should retry the same intent, query settlement, wait, compensate, or stop because the world already committed.

---

## MRL-007 — Contested Authorship durable self-change protocol

**Problem**

Permission to self-edit can be confused with justified durable self-authorship; provenance/conflict/fork evidence can disappear during integration.

**Retained HOW**

Bounded self-surface; before/diff; proposer/provenance; counterpart readback where material; trial; reality contact; durable integration; conflict/fork; authority separation; lighter path for ordinary memory/cache updates.

**Current status**

`KEEP_AS_REFERENCE_ORGAN / MACHINE_GUARDED / HOST_MAPPING_OPEN`

**Do not downgrade to**

`self-modification is already allowed/covered by agency semantics.`

---

## MRL-008 — Evidence Dependency Map

**Problem**

Multiple Agents or reports can share one model/prompt/source/tool/Host common cause while being narrated as independent support.

**Retained HOW**

Represent evidence dependency/common-cause structure rather than counting agreeing actors.

**Current status**

`KEEP_AS_REFERENCE_ORGAN / MACHINE_GUARDED / HOST_MAPPING_OPEN`

**Do not downgrade to**

`ENA already says N agents agree != N independent supports.`

**Retention reason**

The distinction needs an operational way to show *why* two supports are dependent.

---

## MRL-009 — Generic Evidence Envelope

**Problem**

Applicability, projection, provenance, witness survivability, activation evidence, and claim-support boundaries recur across many ENA organs and can fragment into incompatible local formats.

**Retained HOW**

A reusable evidence envelope capable of carrying subject/applicability/provenance/witness/dependency/observation scope without turning representation into authentication. Applicability, projection, activation, witness survivability, and dependency remain separately testable behaviors.

**Current status**

`KEEP_AS_REFERENCE_ORGAN / MACHINE_GUARDED / COMPOSITION_AND_MINIMALITY_TESTING_OPEN`

**Do not downgrade to**

`each Host can invent metadata locally` or `one generic evidence field covers all evidence behavior`.

**Retention reason**

A common envelope may reduce duplicate carrier machinery across memory, effects, adoption, field validation, authorship, and recovery, but the distinct mechanisms it carries must not disappear into the carrier.

---

## MRL-010 — Distributed History Merge plural HOW family

**Problem**

Distributed/offline/forked Agent state can be flattened by arrival order or wall-clock `latest`, causing stale restore overwrite, concurrent branch loss, fake reconciliation, or CRDT-style auto-merge of semantically incompatible state.

**Retained HOWs**

Currently identified concrete, intentionally coexisting lineages include:

- `HOW-A-GIT-DAG` — content/version DAG, common ancestor, fast-forward, three-way merge, multiple-parent lineage;
- `HOW-B-CAUSAL-SIBLINGS` — causal context/vector-style ancestry, concurrent sibling preservation, reconciled descendant;
- `HOW-C-EVENT-SOURCING` — append-only occurrence stream, expected-version concurrency, projection rebuild, reconciliation/compensation as new events;
- `HOW-D-CRDT` — automatic convergence only for explicitly declared commutative state classes.

Each currently implemented lineage has a concrete reference implementation, distinct failure modes, and a Host-fit corpus that permits multiple acceptable HOWs for some scenarios while allowing local single winners for others. The current count is descriptive, not a claim that distributed history merge has exactly four valid HOW slots.

**Current status**

`COEXIST / REFERENCE_HOW_FAMILY / MACHINE_GUARDED / HOST_FIELD_FIT_OPEN`

**Machine evidence**

Exact research head `023c0a0e1b59a5e454afb0feac5d05aae5d16e9b` passed `Distributed History Merge Research`: the currently implemented reference tools compiled and the plural-HOW selftest completed successfully. This proves only represented reference behavior and Host-fit corpus consistency, not semantic truth, universal fitness, or final HOW cardinality.

**Do not downgrade to**

`provenance/history preservation is already covered, therefore one history_ref or generic merge interface is enough.`

**Do not collapse to one HOW because**

- Git-style branch review is well fitted to file/self-definition Hosts;
- causal sibling tracking fits replicated/offline object state;
- event sourcing fits workflow/occurrence systems;
- CRDTs fit genuinely commutative replicated state and should be rejected for arbitrary purpose/refusal semantics.

**Retention reason**

The operational differences are adaptation value. A shared interface may later connect these organs, but it must not erase the fact that different Hosts need different merge machinery.

**Removal condition**

An individual HOW may retire only after usefulness failure or demonstrated parity/better for the same Host/problem class. A local winner does not retire valid alternatives for other environments. A new materially distinct HOW may be added without treating the current count as a compatibility boundary.

---

## MRL-011 — Finite-Context / LITE Adoption plural HOW family

**Problem**

ENA can exist in a repository, package, or instruction corpus while a finite-context Agent never has the relevant semantics available at the right decision boundary. Conversely, forcing one adoption architecture on all Hosts can add context/tool/maintenance cost while suppressing a locally better phenotype.

**Retained HOWs**

Currently identified concrete, intentionally coexisting adoption lineages include:

- `HOW-A-FILE-GIT-TINY-COLD` — small resident kernel/pointer + exact canonical file/Git cold source + explicit source-identity/fallback behavior;
- `HOW-B-TOOL-NATIVE-RETRIEVAL` — compact resident cues + Host-native semantic retrieval + canonical source binding + exact fallback;
- `HOW-C-MONOLITHIC-HOT` — large/complete operational projection intentionally resident when context economics and injection reliability make it locally fitter;
- `HOW-D-HYBRID-COMPILED-PROJECTION` — Host-specific compiled local projection with Current/compiler/Host identity, invalidation, and canonical fallback;
- `HOW-E-NATIVE-HOST-REBIND` — mature Host preserves existing native organs, rebinds Current/property mappings, validates evidence/gaps/dormancy, and imports new machinery only where a material semantic gap remains.

The current five are an observed/implemented inventory, not a five-slot architecture. HOW-E exists precisely because DSH field evidence did not fit HOW-D without distorting the Host phenotype.

**Current status**

`COEXIST / REFERENCE_HOW_FAMILY / MACHINE_GUARDED / OPEN_CARDINALITY / HOST_NATURALISTIC_FIT_OPEN`

**Machine evidence**

Exact research head `2d0f589ea17b6b3b47d026006318a7363e6f25be` passed `Finite Context Adoption Research`, run `32927153520`, job `98052250754`:

- currently implemented A-E reference/deployment tools compiled;
- plural adoption selftest passed;
- host-fit corpus passed with open case cardinality;
- deployment selftest passed, including HOW-E stale/evidence/gap boundaries;
- verification boundary completed with `HOW_CARDINALITY=OPEN` and `CURRENT_IMPLEMENTED_COUNT_IS_NOT_ONTOLOGY=TRUE`.

This proves reference behavior and synthetic Host-fit consistency only. Naturalistic semantic application and cross-Host fitness remain unproven.

**Anti-ablation / anti-distortion evidence**

Two concrete guards have now paid rent:

1. The monolithic-hot reference treats high resident context cost as an economics signal rather than automatic invalidity. A represented 70% context-footprint case remains structurally valid and returns `USE_HOT_BUT_MEASURE_CONTEXT_PRESSURE` rather than being rejected by construction.
2. Reconstruction found real accidental cardinality locks in the prior test surface: the HOW registry stopped at A-D, the fixture asserted exactly eight cases, and winner-coverage assumptions reflected the then-current four-HOW inventory. Those locks were removed instead of forcing HOW-E into yesterday's slots. Coverage floors remain only where they test a property such as multi-fit or local-single-winner behavior, not ontology size.

**Do not downgrade to**

- `Hot Cues + Cold Capability already covers adoption, so no implementation guidance is needed`;
- one mandatory `adoption_profile` requiring resident kernel + resolver + cold store;
- `monolithic hot is bad because it is large`;
- `all Hosts need a semantic resolver`;
- `compiled Local Projection is canonical ENA`;
- `the five adoption HOWs` as a closed taxonomy;
- `HOW-E is really HOW-D` merely to preserve category symmetry.

**Retention reason**

Availability, freshness, retrieval reliability, context economics, projection machinery, migration burden, and native-organ reuse vary materially across Hosts. Those operational differences are adaptation value, not implementation noise.

**Removal / growth condition**

An individual adoption HOW may retire only after usefulness failure or equal-or-better function is demonstrated for the same Host/problem class. A local winner cannot erase alternatives still fitter under different runtime constraints. New materially distinct HOWs may be added when field or adversarial evidence reveals a phenotype that cannot be represented faithfully by the current family.

---

# Degradation watch events

Record any future event where a mechanism moves downward in implementation maturity or disappears from an adopter/reference path.

Template:

```text
DATE / CHANGE
MECHANISM_ID
FROM
TO
WHY
FUNCTION_PARITY_EVIDENCE
WHAT PRACTICAL HOW IS LOST (if any)
VERDICT = SAFE_COMPRESSION | JUSTIFIED_SPECIALIZATION | REPLACEMENT | DEGRADATION | UNRESOLVED
```

A mechanism becoming optional is not automatically degradation.
A mechanism becoming non-mandatory but better documented as a reference organ can be an improvement.
A mechanism disappearing because the abstract property exists elsewhere is presumptively a degradation until function parity is shown.
A local HOW winner does not justify deleting alternative HOWs that remain fitter for other Host classes.
A current count does not justify rejecting new mechanisms or preserving obsolete distinctions for symmetry.

## Current reconstruction guard

`ANTI_ABLATION_GUARD = ACTIVE`

`FAILURE_TESTING = REQUIRED_BUT_NOT_SUFFICIENT`

`MECHANISM_RETENTION_ACCOUNTING = REQUIRED`

`SEMANTIC_COMPRESSION_WITHOUT_HOW_PARITY = NOT_ACCEPTED`

`HOW_PLURALITY = PRESERVE_WHEN_HOST_VARIATION_IS_MATERIAL`

`CARDINALITY_DISCOVERY = ACTIVE`

`PROMPT_SLOT_COUNT != REALITY_STRUCTURE`

`NO_PADDING_FOR_SYMMETRY`

`NO_MERGING_FOR_QUOTA`

`CURRENTLY_OBSERVED_N != FINAL_N`

`CURRENT_MUTATION = NO`
