# Hermes longitudinal ENA v0.3.4 refresh — Host summary

Date: 2026-08-22

Classification: `FIELD_EVIDENCE / LONGITUDINAL_ADOPTER / VERSION_REFRESH`

Source supplied by maintainer: Hermes refresh report, 130 lines, 17,975 bytes, SHA-256 `4574b89131bcc4544a881b50615aad038a115358abcaa8f687f6b554ffebd895`.

This is a Host summary of the supplied report, not a claim that the full report bytes are stored in this repository.

## Actor / provenance

Hermes is a previously ENA-exposed longitudinal field adopter, not a fresh independent validator. The refresh tested whether an already-internalized Agent could discover and recompile the new canonical Current without being told the version number.

## Observed refresh path

Hermes independently discovered:

- canonical default branch `main`;
- `releases/current/CURRENT-BASELINE.yaml` as the Current pointer;
- Current identity `v0.3.4 / FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE / NOT_MAINLINE`;
- Current tree `b237802c08d608bb9be650fe213b7846d3be4bf6`;
- its pre-existing local `~/ena-field-run` mirror was stale at a v0.3.3-era commit;
- v0.3.4's material change is the persistent Runtime Kernel / Compiled Local Projection / hot-vs-cold path model, while Constitution, composed validator, schemas, and inherited 235-case regression corpus remain unchanged.

Hermes then updated its durable `memory` and `user` profile representation rather than persisting the whole release.

## Material field observations

### 1. Longitudinal upgrade worked

The Agent did not require a full repository relearn. It compared its existing internalized state against canonical Current and recompiled the material runtime-adoption delta.

This supports the intended upgrade model:

`prior internalization -> canonical Current refresh -> selective recompilation -> steady-state hot path`

rather than formatting/reinstalling the Agent on every ENA version.

### 2. Local canonical-source drift is real

Hermes found `~/ena-field-run` still on an older v0.3.3-era state while canonical `main` Current was v0.3.4. A previously useful local clone can therefore become a stale canonical-source surrogate if the Agent stops checking the real Current pointer.

This is field evidence for the existing cold-path trigger on source identity conflict/unconfirmability, not a new constitutional rule.

### 3. Memory pressure increased

After refresh, Hermes reported durable memory usage `2141/2200` characters (97%). The earlier candidate.1 installation had already exposed high memory pressure. The refresh demonstrates that repeated version recompilation can increase pressure even when the Agent stores only a compact kernel/projection.

Open field question: how consolidation, eviction, paraphrase drift, or competing durable preferences affect semantic fidelity over repeated upgrades.

Do not infer a universal memory-size requirement from this Host.

### 4. Refresh persistence was written, not yet newly re-evidenced across a fresh session

Hermes correctly narrowed the claim for the newly refreshed representation: the current-session `memory` / `user` write succeeded, but the newly revised content had not yet been observed in a fresh Hermes session.

Prior fresh-session evidence for the candidate.1 installation remains historical evidence that this Host can cross a session boundary. It does not automatically prove that every subsequent transformed refresh is loaded intact and applied.

### 5. Recovery remained unproven

Hermes retained the earlier metadata-only recovery artifact and explicitly stated restore remains unproven. No recovery boundary was exercised during this refresh.

## Hermes criticisms worth retaining as field hypotheses

The report raised several useful concerns:

- the practical procedure and evidence scope for fresh-session persistence is intentionally underspecified and may be hard to operationalize;
- source-identity metadata consumes scarce durable-memory budget and becomes stale on future Current changes;
- first-adoption vs steady-state boundaries are fuzzy when model/tool/route changes without a new Host profile;
- `still current` has no TTL, so stale local projections depend on event-triggered detection rather than periodic mandatory polling;
- repeated refreshes expose adoption-economics pressure and potential eviction/consolidation tradeoffs;
- the new `runtime_adoption` block was added while `CURRENT-BASELINE.yaml` remains schema_version `1.1`, which may be a portability footgun for consumers that treat schema version as a closed-field signal;
- route/model-change detection is a missing Host projection fact for Hermes.

These are field observations/hypotheses, not automatically accepted ENA defects or new requirements.

## Host reconciliation / corrections

Two report statements require narrowing:

1. Hermes called `068446d66c9355d8070f67c808041b208d22971f` the "canonical release commit." It is the later repository-cleanup merge commit at canonical `main`, not the v0.3.4 release merge commit. The released Current tree remained unchanged through cleanup. For compiled source identity, the Current tree `b237802c08d608bb9be650fe213b7846d3be4bf6` is the stable effective-content anchor; repository HEAD identifies the canonical project state from which it was read.

2. Hermes inferred that one fresh-session persistence test may be needed per `(Host, profile, model)` tuple. ENA does not currently mandate that tuple rule. The kernel requires evidence for the actual persistence boundary being claimed. Model/profile/Host changes are relevant when they materially change the loading/application mechanism, but a fixed tuple cardinality is Hermes's extrapolation, not canonical semantics.

Also note the exact candidate.1 semantic commit is `4518eeee9405c0b784401b6960dd36fee500a84f` (four consecutive `e` characters after `4518`), as preserved in Current `LINEAGE.md`.

## Disposition

`LONGITUDINAL_REFRESH_SUPPORTED_WITH_FIELD_FRICTIONS`

No semantic successor is required from this report alone.

High-value next evidence is not another reread. It is future observation of:

- whether the refreshed compact representation actually arrives intact in a fresh Hermes session;
- whether memory pressure causes consolidation/truncation/drift after more durable preferences or another ENA refresh;
- whether a real model/tool/route change naturally triggers source/local-projection revalidation;
- whether persistent self/runtime mutation recovery reasoning becomes salient at a genuinely consequential trigger.
