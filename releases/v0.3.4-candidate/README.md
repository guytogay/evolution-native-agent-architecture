# ENA v0.3.4-candidate — Runtime Internalization Candidate

Status: `IMPLEMENTATION_CANDIDATE / NOT_CURRENT / NOT_MAINLINE / NOT_PROMOTED`.

`releases/current/` remains ENA v0.3.3. This directory is a self-contained candidate for independent falsification; do not substitute it for Current without later reconciliation.

## Problem being tested

v0.3.3 deliberately lowered adoption cost through LITE and task-triggered retrieval. Fresh field use exposed the other side of that optimization: an Agent can interpret ENA as something to re-read per task, or can infer missing profile semantics from a partial read. That prevents clean testing of whether ENA survives across tasks/sessions and naturally escalates when consequence changes.

Issue #46 captures the finding:

`ADOPTION != RETRIEVAL`.

## Candidate model

This candidate separates three layers:

1. **Persistent ENA Runtime Kernel** — compact invariants and consequence/authority/recovery/retrieval triggers that become normal operating behavior.
2. **Compiled Local Projection** — repeatedly decision-relevant Host reality, persisted and selectively revalidated when material facts change.
3. **Canonical ENA Source** — cold-path authority for version changes, novel/ambiguous boundaries, stale local reality, and exact contract/schema/tool semantics.

Profiles are runtime governance intensity over this same internalized baseline. LITE is not a smaller ENA education.

## First read

For candidate evaluation:

1. `00-READ-ME-FIRST.md`
2. `01-CONSTITUTION.md`
3. `02-SELF-POSITIONING-AND-LOCAL-PROJECTION.md`
4. `RUNTIME-ADOPTION-KERNEL.md`
5. only then the task-specific contracts/details actually triggered by the evaluation.

Do not load the entire repository merely to look compliant.

## Inherited surfaces

The Constitution, roles, capability map, core composed validator semantics, schemas, tools, and 235-case regression corpus are inherited from v0.3.3 unchanged unless a file in this candidate explicitly says otherwise.

No validator/schema change is claimed by this candidate. Its falsification target is adoption/runtime behavior.

## Next actor

A fresh independent validator should inspect the candidate without accepting the author's expected behavior as truth. In particular, seek:

- persistent-adoption claims unsupported by actual cross-session persistence;
- under-governance caused by convenience-biased profile choice;
- over-governance caused by treating any side effect as HIGH_ASSURANCE;
- repeated unnecessary canonical reads after adoption;
- persistent self-mutation that fails to trigger recovery reasoning;
- stale local projection used after material Host/runtime change;
- canonical retrieval that fails to occur for novel/ambiguous/high-consequence boundaries.

> **Canonical source is the cold path; internalized semantics are the hot path.**
