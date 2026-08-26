# Evolution Record Progressive Representation — Static Reconstruction Analysis

Date: 2026-08-26

Status: `STATIC_COMPARISON / HOW_BRANCH_RECOVERY / CURRENT_UNCHANGED / NOT_RELEASE_AUTHORITY`

Related: #104, RV-002/RV-004 in `RECOVERED-VARIATION-MAP.md`.

## Question

Do the recovered proportional-record and Host-extension variations still describe real v0.3.6 gaps, and what concrete HOW branches are already latent in Current/tooling?

This analysis uses the actual v0.3.6 schema/tool as source, not the historical critique's wording.

## Static findings

### 1. The historical “18 required fields” claim was imprecise

`evolution-record.v2.schema.json` currently requires 17 top-level keys:

```text
candidate_id
created_at
origin
lifecycle_state
expression_state
selection_state
signal_refs
hypothesis
change
variation_space
environment
experiments
evaluations
expression_history
integration_history
archive
migration
```

Several may be empty arrays or `null`, so the correct claim is not:

> every variation must already contain 17 substantive facts.

The narrower failure is:

> every portable candidate record must carry a future-complete container skeleton even when many lifecycle events have not happened.

This is still a real representational-cost question, but weaker than the historical critique claimed.

### 2. v2 already contains progressive history containers

`experiments`, `evaluations`, `expression_history`, and `integration_history` are appendable arrays. Lifecycle-specific requirements activate only when state makes them relevant.

Therefore v0.3.6 is **not** purely a flat static form. It is a monolithic aggregate containing progressive sub-histories.

### 3. The reference tool already contains an event-log embryo

`ena_evolve.py` initializes:

```text
signals
reviews
candidates
migration_imports
events
```

and appends events for operations such as initialization, observation, review, proposal, experiment, evaluation, etc.

This is important:

```text
EVENT_ORIENTED_OCCURRENCE_HISTORY
ALREADY_EXISTS_INSIDE_REFERENCE_TOOL
```

but it is not the canonical portable v2 record model.

The recovered external event/span patterns therefore may be **recombination with an existing ENA organ**, not an imported alien architecture.

### 4. Variation-Space false-BLOCK remains real in the inherited tool

The Current semantics permit latent variation before a material Variation Space is available, but `ena_evolve.py` still defines:

```text
propose --variation-space required=True
import  --variation-space required=True
```

The experiment command makes its `--variation-space` optional and can inherit the candidate's earlier value.

So the staged mismatch remains:

```text
SEMANTICALLY_LEGAL_LATENT_NOW
!= TOOL_CAN_CREATE_IT
```

This is already a known accepted residual; the recovered progressive-record work must not accidentally conflate it with the broader record-shape question.

### 5. Top-level extension surface is closed; nested surfaces are mixed

The v2 candidate schema ends with:

```text
additionalProperties: false
```

at the portable top level.

But several nested structures (`experiments`, `evaluations`, `expression_history`, `integration_history`, archive/migration objects) allow additional properties.

`environment` is also an open map, but values are restricted to primitives and its semantics are environment description, not generic Host extension metadata.

Therefore the accurate extension gap is:

```text
NO_EXPLICIT_PORTABLE_TOP_LEVEL_HOST_EXTENSION_SEAM
```

not:

```text
ALL_ENA_SCHEMA_OBJECTS_ARE_CLOSED
```

### 6. Adaptation packet v2 is also a closed aggregate snapshot

`adaptation-packet.v2.schema.json` requires source lifecycle/selection/expression state plus source history arrays and ends with `additionalProperties: false`.

This means a progressive/event-oriented local representation still needs a well-defined **snapshot/projection boundary** for migration/interoperability.

A new event-based HOW cannot simply replace the packet without proving that it can reconstruct the exact portable claim/evidence snapshot required at export time.

### 7. No generic `verification_boundary` carrier exists in Current

Current contains narrower evidence-boundary prose/fields (for example evaluation-level `evidence_boundary` in the inherited tool), but repository search finds no generic `verification_boundary` surface describing what a verifier itself checked.

RV-001 therefore remains potentially decision-distinct from Generic Evidence Envelope:

```text
EVIDENCE_ABOUT_CLAIM
!= VERIFIER_SCOPE_ABOUT_ITS_OWN_PASS
```

Whether it deserves a separate carrier remains open.

---

## Concrete HOW family now visible

### HOW-A — Current monolithic aggregate

```text
one candidate object
+ current lifecycle/expression/selection state
+ appendable history arrays
+ null/empty placeholders for not-yet-used surfaces
```

Strengths:

- local consistency checks are cheap;
- one object is easy to inspect/export;
- migration packet can snapshot from the aggregate;
- conditional schema rules can verify several state/history relationships directly.

Weaknesses/questions:

- fixed top-level skeleton on every candidate;
- extension friction at portable top level;
- current projection and occurrence history live in the same mutable aggregate;
- a large long-lived object may become expensive/noisy;
- tool/runtime and v2 record are not fully aligned.

Disposition: `EXISTING_CURRENT_HOW / BASELINE_FOR_COMPARISON`.

### HOW-B — Current tool candidate + internal event log

```text
mutable candidate aggregate
+ separate append-only-ish operation events
```

Strengths:

- already exists in ENA tooling;
- event trail can record occurrences without expanding the portable schema immediately;
- low migration burden if v2 aggregate remains export projection.

Weaknesses/questions:

- event history is not currently canonical portable evidence;
- relationship between events and candidate aggregate can drift;
- no generic replay/projector contract is defined;
- `add_event` itself does not prove event authenticity or completeness.

Disposition: `EXISTING_LATENT_HOW / RECOMBINATION_CANDIDATE`.

### HOW-C — Minimal occurrence envelope + progressive event enrichment + v2 projection

External analogues: CloudEvents core/extension structure, OpenTelemetry events, Agent trace/span systems.

Possible shape:

```text
CandidateCreated
ExperimentObserved
EvaluationRecorded
ExpressionChanged
IntegrationAttempted
Archived/Retired
...
        |
        v
 deterministic/current projector
        |
        +--> v2-compatible aggregate snapshot
        +--> adaptation-packet export snapshot
```

Strengths:

- no future-event placeholders at occurrence time;
- immutable occurrence history can be separated from derived current state;
- supports low-cost append and richer later events;
- fits existing `ena_evolve.py` event embryo;
- can combine with Memory Metabolism occurrence-vs-derived distinction.

Weaknesses/questions:

- projector becomes decision-material machinery;
- missing/duplicated/reordered events can create false state;
- exact ordering/causality rules must have real authority;
- cross-event invariant checking may be more expensive than aggregate validation;
- migration/export requires reliable snapshot construction;
- event count can grow unbounded without compaction/checkpoint strategy.

Disposition: `HIGH_VALUE_REFERENCE_HOW_CANDIDATE / NOT_SELECTED`.

### HOW-D — Strict portable core + explicit Host extension namespace

External analogue: CloudEvents required/optional/extension context split.

Possible shape:

```text
portable ENA fields
+ host_extensions:
    namespace/version -> Host-local data
```

Strengths:

- preserves portable core validation;
- avoids schema fork for useful local data;
- experimental extension can exist without becoming Core.

Weaknesses/questions:

- material decisions may start depending on unvalidated extensions;
- namespace/version/authorship rules required;
- portable receiver may not understand extension semantics;
- extension data may carry protected/sensitive content.

Disposition: `HIGH_VALUE_EXTENSION_HOW_CANDIDATE / NOT_SELECTED`.

### HOW-E — Strict portable core + sidecar Host record

```text
ENA portable record
<-> typed/provenance-bearing reference
Host-local extension record
```

Strengths:

- strongest separation between portable semantics and Host-local state;
- Host extension schema can evolve independently;
- selective legibility/privacy can differ by sidecar.

Weaknesses/questions:

- reference resolution becomes a failure seam;
- portable decision may lose needed local context;
- stale/missing sidecar can create projection gaps;
- migration requires explicit inclusion/omission policy.

Disposition: `OPEN_CANDIDATE`.

---

## Recombination insight

The strongest new finding from this pass is not “replace the v2 record with event sourcing.”

It is:

```text
CURRENT V2 AGGREGATE
+ EXISTING TOOL EVENT LOG
+ MEMORY OCCURRENCE/DERIVED DISTINCTION
+ EXTERNAL CORE/EXTENSION + EVENT PATTERNS
```

can form a **plural HOW family** without changing the semantic trunk.

One plausible reference architecture is:

```text
occurrence/event layer
    -> immutable or append-only facts

projector/resolver
    -> current lifecycle/expression/selection view

portable v2-style snapshot
    -> interoperability / migration / bounded validation

Host extension surface
    -> namespaced or sidecar local details
```

This separates several jobs that are currently partly fused in one record.

But it also introduces new failure seams, so no selection is justified yet.

---

## Deterministic falsification questions

A prototype should be built only if it can answer at least these non-trivial questions:

1. Can the progressive HOW reconstruct all decision-material v2 aggregate invariants without hidden defaults?
2. Can two different event histories project to the same aggregate while carrying materially different negative history? If yes, snapshot-only export may launder history.
3. What happens on duplicate/reordered/tied events?
4. Can a Host extension influence selection/integration without an explicit understood mapping? It must not silently do so.
5. Can a receiver validate a portable snapshot without understanding Host extensions?
6. Can a minimal latent occurrence exist before Variation Space while still satisfying an honest later v2 projection?
7. Can compaction/checkpointing bound event-history cost without erasing provenance/negative evidence?
8. Does the progressive representation reduce real work, or merely move required work from record creation into projection/reconciliation?

These are deterministic/state-space questions first. Do not run stochastic multi-model experiments for them.

## Current decision

`NEW_CORE_PROPERTY_NEEDED = NOT_ESTABLISHED`

`REFERENCE_HOW_FAMILY_EXPANDED = YES`

`PROTOTYPE_JUSTIFIED = YES, IF LIMITED_TO_STATIC_PROJECTOR/EXTENSION_FAILURES`

`CURRENT_CHANGE = NO`

Next engineering step: build a small research-only progressive-envelope/projector prototype with adversarial fixtures, preserving the existing v2 aggregate as comparison/output rather than declaring a replacement.
