# Evolution-Native Agent Architecture — v0.3.4-candidate.1

Status: **IMPLEMENTATION CANDIDATE / NOT CURRENT / NOT MAINLINE / NOT PROMOTED**

This directory is a self-contained corrected successor to ENA v0.3.4-candidate, which itself succeeded ENA v0.3.3. It preserves the runtime-internalization model while closing independent-validation residuals around source-identity drift and persistent-adoption claims.

Do not combine this candidate with `releases/current/`, older releases, other candidates, or research artifacts to determine its effective behavior.

An evaluator should be able to state simply:

`ENA candidate: v0.3.4-candidate.1`

## The key change

**First adoption and steady-state operation are different phases.**

On first adoption, establish a small persistent ENA Runtime Kernel and a truthful Compiled Local Projection. After that, familiar tasks should normally be governed from those internalized semantics without re-reading the ENA repository.

`LITE | STANDARD | HIGH_ASSURANCE | CUSTOM` are runtime governance-intensity projections over the same ENA baseline. They are not different books, different Constitutions, or different amounts of ENA that an Agent is allowed to know.

## First adoption / installation

1. Read this file.
2. Read `01-CONSTITUTION.md`.
3. Read `02-SELF-POSITIONING-AND-LOCAL-PROJECTION.md`.
4. Read `RUNTIME-ADOPTION-KERNEL.md` and compile its durable invariants/triggers into the Host's real persistent instruction/memory/configuration mechanism when one exists.
5. Establish the reusable local facts that materially affect future decisions: persistence surfaces, authority surfaces, recovery path, shared/external effect boundaries, credential/tool boundaries, and material limitations.
6. Record the immutable canonical source identity actually installed from (for example candidate commit/tree or package digest). A version label or mutable branch name alone is not an integrity anchor.
7. Read back the persisted representation where practical. If a transformed/paraphrased kernel is stored, preserve its source lineage and do not assume semantic fidelity merely because the write succeeded.
8. Do **not** persist the whole release into always-loaded context merely to claim adoption.
9. If no real task exists yet, do not invent a production scenario. Complete only the adoption work that is real, report the persistence limitation truthfully, and wait for a real task.

If the Host cannot persist the runtime kernel across sessions, report that limitation. A session-local understanding is useful, but it is not evidence of persistent adoption.

Before claiming that adoption survives a fresh-session or equivalent decision-critical boundary, evidence that actual boundary. Writing a memory/configuration object in the current session is not by itself evidence that a future fresh session receives and applies it.

## Steady-state operation

For each real task:

1. Let actual consequence, authority, reversibility, recovery, shared/external effect, credential, retry/concurrency, and material uncertainty determine the active governance intensity.
2. Use the internalized Runtime Kernel and Compiled Local Projection as the normal hot path.
3. Do not reload ENA merely to prove compliance when the task is familiar and the needed semantics are already current and unambiguous.
4. Retrieve the canonical candidate text when reality changed, the boundary is novel/ambiguous, local understanding may be stale, the immutable source identity changed/cannot be confirmed, or exact contract/schema/tool semantics are decision-critical.
5. Escalate or de-escalate governance when the consequence envelope changes. Convenience does not lower applicability; imagined risk does not justify universal escalation.

A low-consequence reversible local write may still be LITE. The mere existence of an external side effect does not automatically imply HIGH_ASSURANCE.

> **Protect Agency; govern Authority.**
>
> **Governance must pay rent.**
>
> **Adoption is not repeated retrieval.**
>
> **Canonical source is the cold path; internalized semantics are the hot path.**

---
