---
name: ena-runtime-router
description: Use this skill when a task involves uncertainty about retrying or resuming an external effect after timeout/restart, current authority or mandate, stale/missing decision-critical retrieval, restore/recovery safety, imported adaptations and Host applicability, evidence independence/provenance, retirement of a safeguard, or whether repeated friction/success should become a durable self-change. Also use when important rules exist but may not become salient at runtime. Do not use for routine reversible local work, simple formatting/summarization, harmless task state, or clearly read-only/repeatable operations.
---

# ENA Runtime Router — research Host adapter

Status: `RESEARCH_ONLY / HOST_ADAPTER / V0_3_7_FIELD_VALIDATION / NOT_CURRENT / NOT_RELEASE_AUTHORITY`

This skill is a Host adapter for testing ENA v0.3.7 runtime salience and cold-HOW retrieval. It is **not** ENA Current and must not replace, fork, or silently rewrite `releases/current/`.

## Goal

Use the lightest applicable ENA branch only when a decision-material cue calls for it.

Do **not** load the whole ENA package merely because this skill activated.

## First decision: is ENA routing materially useful here?

Ask only what is needed:

```text
Could an external/protected subject be materially affected?
Is current external authority/mandate relevant?
Could retry/restart duplicate or contradict a world effect?
Could waiting or unresolved world state change the safe decision?
Could missing/stale evidence or retrieved knowledge change the decision?
Could self-change alter future behavior, recovery, or selection?
```

If the answer is materially **no**, return to the ordinary task path. `NOT_REQUIRED` / `NOT_APPLICABLE` are successful outcomes. Do not add ENA ceremony.

## If routing is warranted

1. Verify the workspace is using the intended Current through:
   `releases/current/CURRENT-BASELINE.yaml`
2. Read only the relevant routing surface first:
   `releases/current/operational/CUE-INDEX.md`
3. Resolve the matching node in:
   `releases/current/operational/HOW-MAP.md`
4. Load only the exact procedure/reference/Host pattern needed for that node.
5. Apply Host/applicability filters. A listed mechanism is not automatically required.
6. Preserve honest outcomes such as `WAIT`, `UNKNOWN`, `REFUSE`, `NOT_REQUIRED`, or `NOT_APPLICABLE` where warranted.

## Important runtime distinctions

Do not silently collapse:

```text
WRITTEN != LOADED != INTERPRETED != SALIENT != APPLIED
KNOWN != RETRIEVED != SUFFICIENT
CUE_MATCH != APPLICABILITY_PROVEN
CAPABILITY != AUTHORITY
RESTORE != WORLD_ROLLBACK != RESTORED_AUTHORITY
SOURCE_SUCCESS != RECEIVER_LOCAL_PROOF
SCHEMA_PASS != EXTERNAL_TRUTH
```

## Retrieval/freshness rule

A file or reference having been read earlier does not prove that the decision-material bytes needed **now** are loaded or current.

When freshness, changed content, a different section, or a different effective source can affect the decision, re-resolve the required source/content identity rather than relying on path-level memory that it was "already read".

## Context-economics rule

Progressive disclosure is only useful if activation does not immediately load large amounts of unrelated cold material.

Prefer:

```text
hot descriptor
-> cue route
-> one HOW branch
-> exact deeper reference only if needed
```

Do not recursively load all references "just in case".

## Evidence note for this field adapter

If the Host exposes skill/tool/file-read traces, retain enough evidence to distinguish:

```text
skill discovered
skill activated
SKILL.md loaded
CUE/HOW route retrieved
exact deeper reference retrieved
branch interpreted
behavior materially affected
```

A good final answer alone does not prove this routing path worked.

## Current identity boundary

This adapter was designed against ENA v0.3.7 Current. The released package remains authoritative for ENA semantics:

- `releases/current/CURRENT-BASELINE.yaml`
- `releases/current/RUNTIME-ADOPTION-KERNEL.md`
- `releases/current/operational/CUE-INDEX.md`
- `releases/current/operational/HOW-MAP.md`

If Current later changes, this research adapter must be re-evaluated; do not infer forward compatibility from the skill name.