# Host Integration Reference 0.1 — Cold Scope Resolver

Status: `REFERENCE_ORGAN / RESEARCH_ONLY / NOT_CURRENT_BASELINE / NOT_AUTHORITY`

## Purpose

Demonstrate that Retrieval Obligation 0.3 can be implemented without placing a memory-domain catalog in the hot R0 surface.

Reference path:

`generic retrieval intent`
→ load cold `scope-registry.json`
→ select a small number of scopes
→ fetch only the referenced project files
→ if a no-hit remains decision-relevant, expand to a bounded set of neighboring scopes
→ stop when further expansion no longer plausibly changes the decision, or preserve uncertainty/narrow/abstain.

## What this is not

This is **not evidence that lexical retrieval is good enough**.

The provided resolver is intentionally simple and replaceable. A Host may use:

- file metadata;
- SQL;
- vector search;
- graph traversal;
- hybrid retrieval;
- tool routing;
- another mechanism.

The shared property being demonstrated is only:

> the hot Agent need not carry the scope catalog merely to invoke durable memory retrieval.

## Cold registry

The registry points to real ENA research and Current files and keeps scope adjacency out of hot context.

Reference scopes:

- memory contract;
- retrieval obligation / unknown-known;
- restore and continuity;
- security boundary;
- Current runtime semantics;
- evolutionary metabolism.

The registry may grow cold without requiring R0 to grow linearly with it.

## Bounded expansion

The example resolver can return up to two initial scopes.

On a no-hit, a Host may request a bounded neighbor expansion.

This is not a universal graph requirement. The neighbor list is one reference organ for showing how non-obvious adjacent domains can be explored without Search-All.

## Stop rule

Do not keep expanding merely because more scopes exist.

Reuse the existing ENA closure discipline:

> continue only while another bounded retrieval step can plausibly change the material decision.

If retrieval remains materially unresolved, narrow/abstain or preserve explicit uncertainty according to consequence.

## Trust boundary

This reference organ does not prove:

- registry freshness;
- semantic adequacy of scope descriptions;
- true retrieval recall;
- sufficiency of returned memories;
- model-independent routing quality.

Those remain Host/evaluation evidence.

## Evidence discipline

Do not benchmark this hand-authored registry and then call the result proof of the architecture.

Its purpose is feasibility:

`small hot invocation surface + cold growing registry` is implementable.

Future evidence should come from natural project use, an independently authored registry/task set, or a materially different Host implementation.
