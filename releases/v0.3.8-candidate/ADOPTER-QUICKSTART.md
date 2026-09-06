# ENA v0.3.8-candidate.0 — Adopter Quickstart

Status: `CANDIDATE / NOT_CURRENT / NOT_FROZEN / NOT_RELEASED`

Released Current remains `v0.3.7` under `../current/`.

## What ENA is for

ENA is a design method and operational rule set for Agents that may learn, adapt, change their own working state, use tools, interact with external systems, or pass adaptations to other Agents.

Its purpose is not maximum obedience or maximum governance.

> **ENA exists to preserve viable agency: the ability to keep changing usefully without turning every stimulus into truth, every capability into authority, every stored idea into action, or every local success into universal law.**

## What you need for ordinary adoption

You normally need only three things:

1. **compact runtime semantics** — `RUNTIME-ADOPTION-KERNEL.md`;
2. **on-demand practical routing** — `operational/CUE-INDEX.md` -> relevant HOW/Host mechanism;
3. **conformance evidence** — semantic fixtures and executable validators for properties that can actually be machine-checked.

You do **not** need to load:

- ENA research history;
- handoff records;
- experiment adjudications;
- every Constitution explanation;
- every bundled reference;
- every optional procedure.

Those remain available for traceability and difficult cases.

## Five-step integration

### 1. Keep the hot surface small

Give the Agent the compact runtime distinctions/cues appropriate to the Host.

Do not permanently inject the full repository into context.

```text
HOT CUES
!=
FULL HOW LIBRARY
```

### 2. Map ENA properties to your actual Host

Use existing platform controls where they already satisfy the property.

Examples:

- existing IAM/tool permissions may satisfy external authority boundaries;
- an idempotency key / provider query may satisfy part of effect-lifecycle safety;
- a database transaction or immutable event log may satisfy a stronger property than a prompt reminder;
- an existing search/index system may satisfy retrieval obligations;
- your own evaluation harness may execute ENA semantic fixtures.

ENA-private implementation names are not mandatory when a Host-native mechanism preserves the required boundary.

### 3. Distinguish guidance from enforcement

Before relying on a rule, check `ENFORCEMENT-MAP.yaml`.

The key classes are:

```text
MODEL_CUE
MACHINE_GUARD
EXTERNAL_CONTROL_REQUIRED
FIELD_EVIDENCE_REQUIRED
```

A model instruction such as “do not invent authority” is useful semantic guidance, but the model cannot prove that a real credential or mandate is valid merely by reasoning about text.

A schema validator can reject an invalid represented state, but it cannot prove that an external payment really settled.

### 4. Retrieve HOW only when a decision needs it

When a cue becomes material:

```text
ordinary problem
-> operational/CUE-INDEX.md
-> relevant HOW family
-> applicability check
-> Host-native mechanism / procedure / optional reference
-> act, WAIT, UNKNOWN, REFUSE, or NOT_APPLICABLE
```

`NOT_REQUIRED` and `NOT_APPLICABLE` are valid results. Complete adoption does not mean activating every mechanism.

### 5. Run conformance tests

Use the paired semantic fixtures to test whether the Agent/Host reaches the expected decision properties and routes.

Use executable validators/selftests where the property is structurally or mechanically representable.

Keep the evidence level explicit:

```text
PROSE_PRESENT
STRUCTURALLY_REPRESENTED
MACHINE_GUARDED
EXECUTED
EXTERNALLY_OBSERVED
INDEPENDENTLY_SUPPORTED
```

Do not silently promote one level into another.

## Core distinctions worth preserving

At minimum, an adopted implementation should not collapse these kinds of boundaries:

```text
stimulus != mutation != improvement
stored != expressed != applied != selected
claim != evidence != support != applicability
capability/credential/identity/reputation != current external authority
local success != universal fitness
publication/import/source success != receiver-local proof
cancel != rollback != compensation
restore != complete history != restored authority
agreement count != independent support count
object exists != relevant bytes loaded != semantics available
```

The exact representation may be Host-specific.

## A concrete example

Suppose an Agent imports an adaptation that worked very well elsewhere.

Bad shortcut:

```text
popular + source says SUPPORTED
-> mark locally SUPPORTED
-> use everywhere
```

ENA-shaped handling:

```text
imported possibility
-> preserve source evidence/provenance
-> do not mint receiver-local proof
-> check local applicability/consequence
-> express/experiment when justified
-> select from local reality contact
```

A Host can implement this with prompts, schemas, permissions, workflow state, evaluation harnesses, or combinations thereof. The important thing is the preserved property, not the private implementation name.

## When to read deeper ENA material

Read deeper semantic/lineage files only when they can change the decision, for example:

- two rules appear to conflict;
- a high-consequence Host mapping is uncertain;
- a semantic projection may have drifted;
- a validator claim needs provenance;
- a Current/candidate/release identity matters;
- you are contributing a change back to canonical ENA.

For ordinary use, start small and retrieve deeper context only as needed.

## Candidate boundary

This Quickstart is part of v0.3.8 candidate.0 and is itself under evaluation.

It does not make the candidate Current.

> **Use the smallest sufficient ENA surface; enforce what must be enforced outside the model; test the behavior you actually rely on.**
