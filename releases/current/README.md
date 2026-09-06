# ENA v0.3.10 — Current

Status: **CURRENT / FIELD_VALIDATION**

v0.3.10 is the current adopter-facing ENA release.

It is an R0 publication-coherence successor to v0.3.9. The 38-ID Constitution and core behavior remain inherited; the change removes stale active release identity from stable cold surfaces and prevents that defect class from recurring.

## One default hot payload

For an Agent, the only ENA text that should be resident by default is:

`RUNTIME-ADOPTION-KERNEL.md`

Everything else is cold/on-demand capability.

```text
DEFAULT_AGENT_HOT_PAYLOAD = RUNTIME-ADOPTION-KERNEL.md
AVAILABLE_RESOURCE != DEFAULT_HOT_PAYLOAD
```

- Human integration guidance: `ADOPTER-QUICKSTART.md`
- Bootstrap launcher: `AGENT-ADOPTION-INSTRUCTION.md`
- Problem routing: `operational/CUE-INDEX.md`
- HOW library: `operational/HOW-MAP.md`
- Enforcement classification: `ENFORCEMENT-MAP.yaml`
- Conformance evidence: semantic fixtures / executable validators
- Deep semantics / lineage / research: retrieve only when decision-material

## What changed from v0.3.9

Issue #208 F-208-03 showed that Current still contained stable English cold surfaces labeled as `v0.3.7 Current` and one active-sounding `v0.3.6 candidate` narration.

v0.3.10 therefore:

- makes stable English cold semantics version-neutral by default;
- preserves source-version text only where it is genuine historical provenance;
- removes the stale active candidate narration from the Capability Map;
- extends Current validation to reject old `vX.Y.Z Current` labels on designated version-neutral cold surfaces;
- refines R0 protected-byte checks so release-label metadata can change without silently changing capability IDs or evolution-record schema behavior.

No new Constitution IDs are introduced and no Metamemory fixture policy is promoted into doctrine.

## Evidence boundary

Machine PASS proves only the exercised representation and regressions. Natural future-session salience, external authority/effect/recovery truth, universal Host fitness, and bilingual behavioral equivalence remain field evidence.

A new bounded defect should create the smallest justified successor rather than silently rewrite v0.3.10.

> **Version the identity surface; keep stable cold semantics stable.**
