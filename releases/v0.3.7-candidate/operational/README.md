# Operational Architecture — v0.3.7 candidate.0

Status: `WORKING_CANDIDATE / STAGE_1_SHELL / NOT_CURRENT / NOT_FROZEN`

This directory is the candidate-local practical HOW layer.

Its job is not to restate the whole Constitution. Its job is to help an adopter move from a real problem to one or more usable implementation branches without reading `research/`.

## Intended traversal

```text
ordinary cue / failure / decision
-> consequence-first routing
-> CUE-INDEX
-> HOW-MAP
-> REFERENCE-INDEX
-> bounded procedure / optional reference / Host pattern
-> concrete action, WAIT, UNKNOWN, REFUSE, or not-applicable
```

Stage 1 creates only this entry surface. The remaining operational files are explicitly pending in `../CANDIDATE-BASELINE.yaml`; their absence is not completion.

## Architecture rule

The compression boundary sits before HOW:

```text
WHAT / WHY
-> may converge, abstract, deduplicate

HOW
-> may branch, specialize, remain plural, and become Host-specific
```

`HOW_VARIATION != SEMANTIC_DUPLICATION`

One property may legitimately map to multiple concrete mechanisms. For example, consequential effect control can map to provider idempotency, assignment fencing, optimistic concurrency, status query, compensation, or WAIT depending on the target semantics.

## Hot/cold rule

The complete HOW library is cold capability, not mandatory active prompt content.

```text
HOT_KERNEL
-> recognize the problem
-> retrieve relevant operational branch
-> filter by applicability/Host
-> act

HOT_KERNEL != HOW_LIBRARY
```

## Candidate reference boundary

Selected reference organs live under `../references/` when later stages assemble them.

They are examples and reusable machine surfaces, not a required ENA organ inventory.

```text
REFERENCE_EXISTS != UNIVERSAL_APPLICABILITY
PACKAGE_INCLUDED != DEFAULT_ACTIVE
HOST_NATIVE_IMPLEMENTATION != NONCOMPLIANT
```

See `../references/REFERENCE-MANIFEST.yaml` for machine-readable packaging roles.

## Concrete HOW quality

A useful HOW should change what an Agent can actually do. Depending on the mechanism it may include:

- applicability / trigger conditions;
- ordered actions or state transitions;
- tool/schema/template/resolver;
- Host capability dependency;
- effect/authority boundary;
- failure symptoms;
- fallback / WAIT / REFUSE / recovery;
- evidence maturity;
- explicit non-applicability.

This is not a fixed mandatory checklist. A HOW that merely paraphrases the principle remains operational debt.

## Evidence rule

Evidence belongs to branches, not only parent claims:

```text
WHAT_WHY_SUPPORTED
!= HOW_A_SUPPORTED
!= HOW_B_SUPPORTED
!= HOW_A_SUPPORTED_ON_HOST_X
```

A Host success does not create universal fitness.

## Anti-ablation rule

Not selected for this candidate does not mean disproven or retired.

Alternative/dormant/research branches remain durable in project lineage. Candidate assembly must not erase them from ENA research merely because they are not adopter cargo.

> **Compress the semantic trunk; let concrete HOWs branch.**
