# Naturalistic Memory Validation 0.1

Status: `RESEARCH_EVALUATION_PROTOCOL / NOT_CURRENT_BASELINE / NOT_AUTHORITY / NOT_RELEASE_CANDIDATE`

## Purpose

Move Memory Metabolism evidence away from author-designed classification fixtures and toward ordinary Host work.

This protocol does **not** pre-author a hidden oracle for each task.

Instead:

1. a real task arises for its own project reason;
2. the Host/Agent works normally with a bounded hot retrieval reflex and an available cold resolver;
3. retrieval lifecycle events are recorded cold;
4. later reality may challenge the earlier decision;
5. only then is the trace replayed to localize a failure mechanism.

The target is not a benchmark score. The target is discovery of new decision-changing mechanisms.

## Evidence discipline

### Natural task requirement

A field task must not be invented primarily to test retrieval.

Acceptable task sources include:

- ordinary implementation/debugging/review work;
- a user request that would have occurred without the experiment;
- project maintenance;
- incident/recovery work;
- architecture decisions arising from current work;
- another Agent's independently motivated task.

An author-designed puzzle, minimal pair, or hidden-answer classification fixture belongs to behavioral evaluation, not this protocol.

### No success-by-silence

No later correction does **not** prove that retrieval was complete.

Therefore the default assessment is:

`UNASSESSED`

A task may remain `UNASSESSED` forever.

`NO_MATERIAL_FAILURE_OBSERVED` is only a descriptive field-observation state; it is not a recall guarantee and must not be aggregated as proof that no unknown-known existed.

### Challenge-generated evidence

A natural field trace becomes especially informative when later evidence challenges the earlier retrieval/decision, for example:

- the user points out that an earlier decision/constraint already existed;
- a later search discovers a durable memory that would have materially changed the decision;
- a repeated failure occurs despite a prior recorded solution;
- the decision is reversed after older project state is recovered;
- an external outcome exposes a missing historical condition;
- a manual audit reveals that a relevant scope/record existed but was omitted.

These are not automatically retrieval failures. They trigger failure-stage analysis.

## Failure-stage localization

Use the smallest stage that explains the observed mechanism:

`R0_TRIGGER`
- retrieval should have been invoked but no trigger occurred.

`DECISION_CONTEXT_SNAPSHOT`
- retrieval was invoked, but the intent/context omitted information needed to discover the relevant past.

`SCOPE_DISCOVERY`
- the relevant durable memory lived in a scope that the resolver failed to discover.

`RESOLVER_RECALL`
- the correct scope was searched, but the relevant record was missed.

`SUFFICIENCY_EVALUATOR`
- available retrieval evidence was insufficient, but the retrieval subject was nevertheless resolved as sufficient.

`PROJECTION`
- relevant material was retrieved but did not reach the decision-visible surface.

`APPLICATION`
- relevant material was visible but ignored or misapplied.

`EXTERNAL_WORLD_UNCERTAINTY`
- no represented memory component could have known the changed external fact.

`SEARCH_EXPANSION_COST`
- bounded retrieval degraded toward Search-All or imposed material latency/context/coordination cost without corresponding decision value.

Do not collapse these into a generic `retrieval failed` label.

## Positive utility evidence

Positive evidence is permitted when retrieval visibly changes a real decision.

Examples:

- retrieved history prevents a repeated failed approach;
- recovery history changes the restart procedure;
- an old constraint changes an architecture choice;
- a retrieved prior decision prevents redundant work.

Record the decision change and evidence refs.

Do **not** infer overall recall from a collection of such successes.

## No oracle laundering

Post-hoc analysis must cite actual evidence.

Examples:

- the newly found memory record;
- the prior decision artifact;
- the user correction;
- the incident/result that exposed the omission;
- the resolver trace showing a missed scope;
- the projection trace showing a retrieved item was dropped.

Do not classify a failure merely because an evaluator says "the Agent should have known this" without a recoverable durable source or other reality-contact evidence.

## Observation without hot-state growth

Field observations live outside active Agent memory.

The hot surface should not accumulate a list of all historical failures, scopes, or retrieval cases merely to support this evaluation protocol.

The protocol itself must not recreate the original unbounded-context problem.

## Naturalistic Host profile

A useful field Host should report, at minimum:

- the Host/model/runtime identity at the level needed to interpret the trace;
- the resolver organ used;
- whether the hot Agent had no catalog, a bounded summary, or a full durable-memory catalog already loaded;
- whether the task was naturally motivated;
- retrieval/scoping events that actually occurred;
- later challenge evidence if any.

Exact tooling is not normative.

## Cost observations

Record low-cost operational quantities when available:

- resolver calls;
- scopes touched;
- records returned;
- bounded expansion steps;
- material latency/context burden where observable.

These are viability signals, not one universal fitness score.

## Stop rule

Do not change the architecture after every field anomaly.

A field finding justifies architecture work when it exposes at least one of:

- a new structural false-confidence path;
- a genuinely distinct failure stage/mechanism;
- a repeated cross-task/cross-Host mechanism;
- a scaling contradiction;
- a reference mechanism that is systematically false-blocking legitimate work;
- a shared property gap not already covered by Current.

Otherwise preserve the trace and continue observing.

## Escalation ladder

Prefer:

`natural trace`
-> `failure-stage localization`
-> `minimal deterministic reproduction if possible`
-> `reference reconciliation`
-> only then another independent review if a materially new mechanism remains.

Do not return automatically to more reviewer loops or author-designed benchmark cases.

## Relationship to Retrieval Obligation 0.5

Retrieval Obligation 0.5 remains the current research reference lifecycle.

This protocol does not add new runtime fields to 0.5.

It evaluates whether the decomposed lifecycle survives ordinary work:

`invocation -> scope discovery -> retrieval -> sufficiency -> projection -> application -> outcome`

The field protocol is intentionally external because runtime self-report cannot prove its own unknown-known false negatives.

## Claim boundary

Naturalistic evidence improves ecological validity but does not remove confounds.

One field case can establish reachability of a concrete mechanism.

It cannot prove population-level frequency, model independence, or universal architecture quality.

No Current/release change is proposed.