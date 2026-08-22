# ENA v0.3.4-candidate.1 — Runtime Internalization Corrected Candidate

Status: `IMPLEMENTATION_CANDIDATE / NOT_CURRENT / NOT_MAINLINE / NOT_PROMOTED`.

`releases/current/` remains ENA v0.3.3. This directory is a self-contained corrected candidate for targeted revalidation; do not substitute it for Current without later reconciliation.

## Why candidate.1 exists

The original frozen `v0.3.4-candidate` was independently validated with verdict:

`INDEPENDENT_RUNTIME_ADOPTION_VALIDATION_SUPPORTED_WITH_RESIDUALS`

The validator found the runtime-internalization model sound and non-regressive, but identified two adoption-layer residuals worth closing before promotion:

1. a Compiled Local Projection could record only a human-readable candidate/version label and therefore lack an immutable source-integrity anchor;
2. a Host could write a persistence object in the current session and overclaim cross-session adoption without evidencing the actual boundary.

This successor closes those two residuals while preserving the original candidate, its freeze identity, and its validation evidence.

## Candidate model

The three-layer model remains:

1. **Persistent ENA Runtime Kernel** — compact invariants and consequence/authority/recovery/retrieval triggers that become normal operating behavior.
2. **Compiled Local Projection** — repeatedly decision-relevant Host reality, persisted and selectively revalidated when material facts change.
3. **Canonical ENA Source** — cold-path authority for version/source changes, novel/ambiguous boundaries, stale local reality, and exact contract/schema/tool semantics.

Profiles remain runtime governance intensity over this same internalized baseline. LITE is not a smaller ENA education.

## candidate.1 corrections

- Persist the immutable canonical source identity actually compiled from (Git commit/tree or package digest); a mutable branch/version label alone is not sufficient as an integrity anchor.
- A source-identity change, conflict, or inability to confirm it becomes a canonical retrieval/revalidation trigger when it can change a decision.
- If the persisted kernel is transformed/paraphrased, preserve source/transformation lineage and do not infer semantic fidelity from a successful write alone.
- Before claiming cross-session or equivalent decision-critical persistent adoption, evidence the actual boundary being claimed. A current-session memory/configuration write is narrower evidence.

These corrections do not require self-referential hashes inside the candidate. The concrete immutable source identity is established by the external semantic freeze and recorded by the adopter at compilation time.

## Inherited surfaces

The Constitution, roles, capability map, core composed validator semantics, schemas, tools, and 235-case regression corpus remain inherited unchanged from v0.3.3 and from the original v0.3.4-candidate.

No validator/schema change is claimed by this successor. Its revalidation target is D14 source-integrity drift and D2 persistence-boundary claim strength.

## Next actor

Use the same independent validator that found the residuals as a **prior falsifier targeted revalidator**. It should verify the successor against the frozen original, confirm that D14/D2 are actually closed, seek regressions introduced by the fixes, and keep the genuine fresh-session persistence experiment explicitly open if its Host cannot perform it.

> **Canonical source is the cold path; internalized semantics are the hot path.**
