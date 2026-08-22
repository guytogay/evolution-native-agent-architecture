# CHANGELOG — v0.3.4-candidate

Status: `IMPLEMENTATION_CANDIDATE / NOT_CURRENT / NOT_MAINLINE / NOT_PROMOTED`.

This candidate is a focused successor to ENA v0.3.3. It does not reopen the accepted v0.3.3 composed-claim validator semantics. It addresses a new field-adoption problem captured in issue #46: a first-adoption flow can leave ENA behaving like a per-task dictionary instead of a persistent operating model.

## Field inputs absorbed

### 1. Adoption != retrieval

Fresh adopters correctly selected low-consequence behavior during onboarding, but this exposed an ambiguity: selecting LITE for the onboarding task can be misread as learning only a LITE subset and re-learning ENA later whenever task consequence changes.

The candidate separates:

- one-time **first adoption / runtime compilation**;
- **steady-state task execution**;
- canonical **cold-path retrieval/revalidation**.

### 2. Partial selective retrieval can drift semantics

A fresh adopter intentionally avoided loading the whole repo, but omitted part of the declared minimum set and inferred profile boundaries from partial material, producing an over-conservative approximation (`any external side effect -> HIGH_ASSURANCE`).

The candidate therefore makes the cross-profile runtime kernel explicit and states that profiles are runtime governance intensity, not separate knowledge editions. A reversible low-consequence local side effect may remain LITE; actual consequence/recovery/authority/externality decide escalation.

### 3. No-real-task path

The candidate absorbs the field observation that an adopter receiving only ENA onboarding instructions should not invent a fake production task in order to manufacture positive evidence. It may complete real adoption/persistence work and then wait for a real task.

## Runtime adoption changes

- Added `RUNTIME-ADOPTION-KERNEL.md` as the compact persistent hot-path semantics for an adopted Agent.
- Added explicit **Compiled Local Projection** semantics: repeatedly relevant Host/persistence/authority/recovery/shared-effect facts should survive across tasks when the Host supports durable state.
- Reframed `LITE | STANDARD | HIGH_ASSURANCE | CUSTOM` as task/runtime governance intensity over one internalized ENA baseline.
- Canonical repository retrieval is now explicitly the cold path for version change, novelty, ambiguity, stale local reality, or exact decision-critical contract/schema/tool semantics.
- Re-reading ENA before every familiar task is not a compliance requirement and may count as governance friction.
- Persistent self-mutation now has an explicit adoption-level trigger: before changing durable instructions/memory/configuration/routing/tool authority/recovery surfaces, determine whether a credible pre-change recovery point exists and what it covers.
- `backup exists != recovery proven`; restore still does not erase occurrence history.

## What this candidate deliberately does NOT change

- Constitution IDs/content: unchanged from v0.3.3.
- Core composed claim-pack validator semantics: unchanged.
- Schemas: unchanged.
- 235-case regression corpus and runner: unchanged.
- Open research #11 (ecological governance) and #15 (cognitive modes): not promoted by this candidate.
- Research tooling drift #45: not papered over as part of this candidate.

## Validation target

The next actor should try to falsify at least these claims:

1. a fresh adopter can compile the kernel without needing the whole repo always loaded;
2. a new session can preserve ENA behavior when the Host has real persistence;
3. familiar LITE work does not require repeated ENA reads;
4. small reversible side effects do not cause automatic HIGH_ASSURANCE escalation;
5. persistent self-mutation triggers recovery reasoning without a user reminder;
6. novel/high-consequence ambiguity still causes canonical retrieval or explicit uncertainty;
7. persistence claims cannot be manufactured when the Host has no durable mechanism.

---

# Inherited v0.3.3 lineage

The v0.3.3 Current baseline remains the accepted predecessor while this candidate is under evaluation. Its composed claim-pack validation surface, schemas, tools, and regression corpus are copied into this candidate unchanged. Historical negative evidence from the original v0.3.3 candidate remains part of repository lineage and is not rewritten by this successor.
