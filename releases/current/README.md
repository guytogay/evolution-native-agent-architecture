# ENA Current

Status: **CURRENT / FIELD_VALIDATION**

The authoritative numeric release identity is `CURRENT-BASELINE.yaml`. This directory is the complete adopter-facing Current package.

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

## Version identity and stable semantics

Stable semantic/adoption instructions should not duplicate the mutable numeric Current version unless their meaning genuinely depends on that identity.

```text
COLD_SEMANTIC_SURFACE != RELEASE_ID_LABEL_MAINTENANCE_BURDEN
HISTORICAL_PROVENANCE != ACTIVE_RELEASE_IDENTITY
```

Use `CURRENT-BASELINE.yaml` for active release identity and `CHANGELOG.md` / `LINEAGE.md` for release-specific history.

## Evidence boundary

Machine PASS proves only the exercised representation and regressions. Natural future-session salience, external authority/effect/recovery truth, universal Host fitness, and bilingual behavioral equivalence remain field evidence.

A known decision-bearing defect should not remain in the shareable Current merely because the previous version is immutable. Preserve the defective release as occurrence truth and move Current through the smallest justified successor.

> **Version the identity surface; keep stable semantics stable; do not knowingly ship a defect you already understand how to fix.**
