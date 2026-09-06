# ENA v0.3.9 — Current

Status: **CURRENT / FIELD_VALIDATION**

v0.3.9 is the current adopter-facing ENA release.

It is an R0 adoption-surface successor to v0.3.8. The 38-ID Constitution, core contracts, schemas, and key machine behavior remain inherited; the change is about reducing default context and preventing release/adoption narration from drifting across entry surfaces.

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

## What changed from v0.3.8

Issue #208 exposed two R0 adoption defects:

1. ordinary first-use wording still made several cold resources look like a default load list, despite the hot/cold design;
2. root and zh-CN entry narration could remain on older release identities because those surfaces were outside the release-identity consistency gate.

v0.3.9 therefore:

- makes the Runtime Kernel the singular default resident Agent payload;
- turns the Agent adoption instruction into a disposable bootstrap launcher rather than a second semantic payload;
- makes Cue Index, HOW, Enforcement Map, and fixtures explicitly on-demand;
- repairs stale root and zh-CN adopter identity surfaces;
- makes the Current validator cover root identity, zh-CN entry identity, and the one-hot-payload contract.

No new Constitution IDs are introduced.

## Evidence boundary

Machine PASS proves only the exercised representation and regressions. Natural future-session salience, external authority/effect/recovery truth, universal Host fitness, and bilingual behavioral equivalence remain field evidence.

A new bounded defect should create the smallest justified successor rather than silently rewrite v0.3.9.

> **One hot kernel; cold capability on demand; preserve old releases and move Current quickly.**
