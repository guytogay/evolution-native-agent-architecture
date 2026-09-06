# ENA v0.3.8 — Adopter Quickstart

Status: `CURRENT / FIELD_VALIDATION`

## What ENA is for

ENA is a design method and operational rule set for Agents that may learn, adapt, change working state, use tools, affect external systems, or pass adaptations to other Agents.

Its purpose is viable agency: continued useful evolution without turning every stimulus into truth, every capability into authority, every stored idea into action, or every local success into universal law.

## Ordinary adoption

You normally need only:

1. `RUNTIME-ADOPTION-KERNEL.md` for compact semantics/cues;
2. `operational/CUE-INDEX.md` for on-demand HOW retrieval;
3. `ENFORCEMENT-MAP.yaml` to identify where enforcement actually lives;
4. fixtures/validators for the claims that are mechanically testable.

Research history, handoffs, adjudications, and every optional reference are cold lineage, not default runtime payload.

## Integration

- Keep the hot surface small.
- Map ENA properties to existing Host controls when they already satisfy the boundary.
- Do not confuse a model instruction with a hard control.
- Retrieve a HOW only when the decision needs it.
- Treat `NOT_REQUIRED`, `NOT_APPLICABLE`, `WAIT`, `UNKNOWN`, and `REFUSE` as legitimate outcomes.
- Match claim strength to evidence: `PROSE_PRESENT | STRUCTURALLY_REPRESENTED | MACHINE_GUARDED | EXECUTED | EXTERNALLY_OBSERVED | INDEPENDENTLY_SUPPORTED`.

## Core distinctions

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

## Example

An adaptation worked well elsewhere. Import it as a possibility with source provenance; do not mark it locally `SUPPORTED` merely because it was popular or successful at the source. Check local applicability and consequence, then select from local reality contact.

> **Use the smallest sufficient ENA surface; enforce outside the model where the property actually lives; test the behavior you rely on.**
