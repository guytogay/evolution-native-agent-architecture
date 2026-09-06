# Operational Architecture — v0.3.8-candidate.0

Status: `CANDIDATE / NOT_CURRENT / ASSEMBLED_OPERATIONAL_ARCHITECTURE`

Released Current remains v0.3.7. This directory is the candidate-local practical HOW layer.

Its job is not to restate the Constitution. Its job is to help an adopter move from a real problem to one or more usable implementation branches without reading `research/`.

## Traversal

```text
ordinary cue / failure / decision
-> consequence-first routing
-> CUE-INDEX
-> HOW-MAP
-> REFERENCE-INDEX when exact local path is needed
-> bounded procedure / optional reference / Host pattern
-> concrete action, WAIT, UNKNOWN, REFUSE, or NOT_APPLICABLE
```

Use `../ENFORCEMENT-MAP.yaml` when the implementation decision depends on whether the relevant property is a model cue, machine guard, external control, or field-evidence claim.

## Architecture rule

The compression boundary sits before HOW:

```text
WHAT / WHY
-> may converge, abstract, deduplicate

HOW
-> may branch, specialize, remain plural, and become Host-specific
```

`HOW_VARIATION != SEMANTIC_DUPLICATION`

One property may map to multiple concrete mechanisms. Consequential effect control, for example, can map to provider idempotency, assignment fencing, optimistic concurrency, status query, compensation, or WAIT depending on target semantics.

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

## Reference boundary

Selected reusable reference organs live under `../references/`.

They are examples/machine surfaces, not a required ENA organ inventory.

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
- enforcement class/evidence maturity;
- explicit non-applicability.

This is not a fixed checklist. A HOW that merely paraphrases the principle remains operational debt.

## Evidence rule

```text
WHAT_WHY_SUPPORTED
!= HOW_A_SUPPORTED
!= HOW_B_SUPPORTED
!= HOW_A_SUPPORTED_ON_HOST_X
```

A Host success does not create universal fitness.

## Anti-ablation rule

Not selected for candidate.0 does not mean disproven or retired. Alternative/dormant/research branches remain durable in project lineage. Candidate packaging must not erase them merely because they are not adopter cargo.

> **Compress the semantic trunk; let concrete HOWs branch.**
>
> **Retrieve the HOW; do not preload the history.**
