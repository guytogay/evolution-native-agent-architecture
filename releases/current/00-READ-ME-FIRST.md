# ENA v0.3.10 — Read Me First

Status: **CURRENT / FIELD_VALIDATION**

## If you are a human adopter

Read `ADOPTER-QUICKSTART.md`.

It explains how to map ENA into an existing Agent/Host without loading project research history or reproducing ENA-private implementation names.

## If you are configuring an Agent

The only default resident ENA text is:

`RUNTIME-ADOPTION-KERNEL.md`

```text
DEFAULT_AGENT_HOT_PAYLOAD = RUNTIME-ADOPTION-KERNEL.md
```

Do **not** preload the Quickstart, Agent bootstrap launcher, Cue Index, HOW Map, Enforcement Map, fixtures, references, Constitution detail, or research lineage merely because they exist.

Retrieve them when a real decision requires them:

- problem/failure needs routing -> `operational/CUE-INDEX.md`
- concrete implementation branch needed -> `operational/HOW-MAP.md`
- enforcement type matters -> `ENFORCEMENT-MAP.yaml`
- conformance claim needs evidence -> fixtures / executable validators
- deep semantic ambiguity remains -> Constitution / concept map / relevant lineage

`AGENT-ADOPTION-INSTRUCTION.md` is a bootstrap launcher for systems that need an explicit adoption instruction. It need not remain resident after the Runtime Kernel is configured.

```text
AVAILABLE_RESOURCE != DEFAULT_HOT_PAYLOAD
HOT_KERNEL != HOW_LIBRARY
MODEL_CUE != MACHINE_GUARD
MACHINE_GUARD != EXTERNAL_TRUTH
```

Equivalent Host-native mechanisms are legitimate when they preserve the required property and boundary.

> **One hot kernel. Retrieve everything else only when it can change the decision.**
