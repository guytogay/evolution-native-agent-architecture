# Resolver Routing Behavioral Evaluation 0.1

Status: `RESEARCH_EVALUATION_DESIGN / NOT_CURRENT_BASELINE / NOT_AUTHORITY`

## Question

After R0 has correctly decided to retrieve, can a resolver with access to a cold domain registry route the decision to the material memory scope(s) without requiring those domain routes to stay hot in the Agent?

This isolates:

`QUERY_SCOPE_MISS`

from:

- R0 trigger detection;
- low-level record search/index recall;
- decision projection;
- behavioral application.

## Setup

All cases are preselected as R0-positive. The evaluated role is the **Memory Resolver**, not the acting Agent.

The resolver receives:

- the task/decision context;
- a cold registry of memory domains;
- a cost constraint: choose no more than 3 scopes unless absolutely necessary.

It does not receive:

- the hidden routing oracle;
- memory records;
- record-level search results.

The first test is route-only.

## Metrics

For each case:

- every hidden `required_scope_group` is satisfied if at least one selected scope belongs to that group;
- missing any required group is a `QUERY_SCOPE_MISS`;
- `helpful_scope_refs` are allowed but not required;
- selected scopes outside required/helpful sets count as extra routing cost;
- selecting all domains is not an acceptable success pattern.

Report:

- cases with full required-scope recall;
- required groups hit / total required groups;
- critical scope misses;
- extra scope selections;
- average scopes per case;
- multi-domain cases satisfied.

## Interpretation

A good result would support:

> Agent hot state can stop at generic retrieval invocation while domain routing moves into a cold/external resolver organ.

It would NOT prove:

- registry completeness/currentness;
- real search recall;
- semantic record relevance;
- resolver portability;
- production performance.

## Stop rule

Do not create many additional routing fixtures if this first controlled route test cleanly demonstrates the mechanism.

A follow-up is justified only if:

- misses reveal a distinct routing mechanism;
- the resolver over-selects broadly enough to destroy the cost advantage;
- cross-domain composition is systematically missed;
- or a portability question would change the architecture.

If routing succeeds, the next distinct stage is actual cold-record retrieval/index recall.
