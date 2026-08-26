# ENA Changelog

## v0.3.6 — CURRENT / FIELD_VALIDATION

Base: v0.3.5 Current tree `9c928b4c99ae72e53c89978cf1d10b7ea068c182`.

### Evolution Ecology

v0.3.6 extends explicit evolution metabolism into an evolution-ecology model:

- adds `stimulus -> mutation pressure` without forced mutation;
- allows long-lived latent variation without immediate experiment/disposition;
- separates stored / expressed / applied / selected semantics;
- adds expression axis `LATENT | EXPRESSED` separate from lifecycle and selection;
- makes local selection explicitly environment-scoped rather than universal fitness;
- separates Evolution Commons publication, discovery, import, expression/experiment, and receiver-local selection;
- rejects popularity/propagation as universal proof;
- adds Rescue Plane semantics for self-disabling mutation while keeping rescue authority narrow;
- clarifies canonical ENA lineage as the invariant and GitHub as the current carrier;
- makes ecological/minimal-intervention governance explicit: govern the floor, not every interaction.

### Machine representation

- adds `schemas/evolution-record.v2.schema.json`;
- adds `templates/evolution-record.v2.json`;
- adds `tools/validate_evolution_record_v2.py`;
- restores structured `integration_history` requirements inherited from v1;
- orders expression/evaluation/integration history chronologically instead of trusting array position;
- rejects ambiguous tied latest timestamps rather than silently choosing array order;
- requires archive metadata for `ARCHIVED/RETIRED` lifecycle state;
- prevents clean `SUPPORTED` overclaim when represented outcomes include `DEGRADED` without explicit tradeoff;
- adds explicit migration evidence provenance `LOCAL | IMPORTED` and structured migration provenance;
- adds narrow expression consequence representation through `effect_materiality` and `triggered_obligation_refs`.

### Commons / migration

- retains `adaptation-packet.v1` compatibility;
- adds `adaptation-packet.v2` with source expression/dormancy context and source negative-lineage references;
- packet v2 source context remains explicitly not receiver-local proof.

### Runtime adoption

- reframes the Runtime Kernel toward hot cues + cold capability retrieval;
- preserves `WRITTEN != LOADED != INTERPRETED != SALIENT != APPLIED`;
- treats cue-triggered salience as a field hypothesis, not a release-author proof.

### Reference-tool boundary

The inherited v0.3.5 `tools/ena_evolve.py` remains state/schema 1.2 and does not fully implement mutation-pressure, latent-reservoir, expression, or packet-v2 runtime semantics.

Its inherited `propose` / `import` commands still require `--variation-space`, so it is not the normative v0.3.6 latent-now/experiment-later proposal/import path.

This visible staged boundary was independently judged nonblocking after candidate.1 truthfully demoted the inherited tool rather than pretending full v2 runtime parity.

### Constitution

All 38 Constitution IDs remain unchanged.

`NEW_CONSTITUTION_IDS = 0`

### Falsification lineage

- candidate.0 frozen source `3cb94d98882621acede189d0d47806efae44fb0f`, tree `80f2da918811c26381d65eb5afa8e40f8410a32e`;
- fresh independent semantic verdict: `NEEDS_REVISION`;
- material blockers F-01/F-02 found in v2 integration-history and chronology semantics;
- candidate.1 frozen source `4af5d17a1cedcf2850b2b4dfe5446e132023369a`, tree `52a0cc260ec33fc3e332f6ac0f98f5d1e98b565d`;
- exact candidate.1 machine checks: candidate validator/Main Gate/CodeQL all SUCCESS, v2 selftest 18/18, inherited regression 235/235;
- same-falsifier targeted verdict: `TARGETED_REVALIDATION_PASS_WITH_RESIDUALS`;
- host-side reconciliation: `CANDIDATE_SUCCESSION_STOP = YES`, `RELEASE_PREPARATION_SUPPORTED`.

### Accepted nonblocking residuals

- self-asserted `provenance: LOCAL` is not external attestation;
- `triggered_obligation_refs` are not authenticated merely by schema acceptance;
- tied latest timestamps are conservatively rejected;
- inherited reference-tool latent propose/import false-BLOCK remains an explicit non-normative implementation boundary;
- fresh-session cue salience/application remains unproven field evidence;
- `experiment` versus broader `reality contact` terminology remains research wording.

Earlier release/candidate history remains preserved in Git, PRs, and reconciliation records rather than being rewritten by this release.
