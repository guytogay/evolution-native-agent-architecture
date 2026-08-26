# Field Use 001 — Stale Registry Design Question

Status: `NATURALISTIC_REFERENCE_TRACE / NOT_CURRENT_BASELINE / NOT_AUTHORITY`

## Real research question

This trace was not authored as a benchmark case.

The live design question was:

> Does a stale memory scope registry require retrieval-specific freshness semantics, or should existing ENA Current applicability/revalidation semantics handle it?

## Cold resolver result

Using the reference resolver without loading the registry into hot R0 state:

Initial selected scopes:

1. `current-runtime-semantics`
2. `restore-continuity`

Ranking also placed:

3. `retrieval-obligation`

with the same lexical score as `restore-continuity`; deterministic tie-breaking selected restore first.

Bounded neighbor expansion from the initial scopes included:

- `retrieval-obligation`
- `security-boundary`

## What the selected Current material established

`releases/current/02-SELF-POSITIONING-AND-LOCAL-PROJECTION.md` already says:

- revalidate only dimensions that matter to the next decision;
- Local Projection includes the Host's effective loaded surface and known gaps;
- projection staleness should refresh affected facts when Host/runtime/tooling and other material surfaces change;
- do not use a universal TTL merely to make caches look fresh.

`releases/current/05-CORE-OPERATIONAL-CONTRACTS.md` already says:

- material Host/tool/route/configuration changes are applicability boundaries for affected evidence;
- after interruption/restore/Host change, revalidate decision-relevant dimensions whose applicability may have changed;
- governance continues only while another bounded check can plausibly change a material decision;
- `READY` is bounded by completeness of represented material inputs.

Therefore this natural design question does **not** currently justify a retrieval-specific freshness rule.

Registry freshness is better treated as affected Host/resolver-state applicability plus external evidence, not a new Memory Metabolism TTL/epoch subsystem.

## Useful resolver imperfection

The initial top-2 scope plan was not ideal.

`retrieval-obligation` was arguably more directly relevant than `restore-continuity`, but both received equal lexical score and the simple reference resolver chose restore by tie-break.

This is useful field signal:

> initial scope ranking can be imperfect even when the generic retrieval invocation is correct.

The trace did not become a material miss because:

- `current-runtime-semantics` already contained enough applicable semantics to answer the design question;
- bounded neighbor expansion would reach `retrieval-obligation` without Search-All.

Classification:

`SCOPE_PRIORITY_AMBIGUITY / RECOVERABLE_BY_BOUNDED_EXPANSION`

## Do not overfit

Do not immediately tune registry wording or lexical weights to make this one trace rank perfectly.

That would turn naturalistic evidence back into an authored benchmark.

Retain the imperfection and watch whether similar scope-priority ambiguity recurs in future real project use.

## Architectural implication

This trace supports only a narrow feasibility observation:

`generic hot intent -> imperfect cold scope plan -> bounded adjacent expansion`

can still reach useful durable state without requiring the Agent to keep a domain catalog hot.

It does not prove general resolver quality or model-independent recall.
