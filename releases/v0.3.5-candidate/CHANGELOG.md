# Changelog — v0.3.5 candidate.2

candidate.2 is a narrow successor to frozen candidate.1 after the same DSH falsifier returned `TARGETED_REVALIDATION_SUPPORTED_WITH_RESIDUALS`.

## candidate.2 — release-decision residual closure

No Constitution rule changed.

- CLI now rejects invalid `source_lifecycle_state` values in migration packets rather than relying on JSON Schema alone;
- CLI fixes `source_authentication` to `NOT_AUTHENTICATED_BY_THIS_PACKET` and rejects stronger self-edited authentication claims;
- CLI validates the fixed `TRANSFERRED_SOURCE_EVIDENCE_NOT_LOCAL_PROOF` transfer-status claim;
- adds `tools/candidate2_adversarial.py` for those residual packet-consistency/trust probes;
- committed inherited-regression result now matches the current suite output;
- CI regenerates the inherited result and fails if that committed generated evidence becomes dirty again;
- active English and zh-CN adoption/projection identities advance to candidate.2.

## candidate.1 — material falsification-driven corrections retained

candidate.1 previously:

- separated lifecycle state from evidence-backed selection state;
- required represented experiment/reality contact before formal selection;
- preserved negative/unknown selection across integration, archival, and migration;
- preserved source experiments/evaluations/integration/archive/migration lineage;
- allowed receiver-side reselection only after local experiment/evaluation while retaining source lineage;
- made migration packet purpose derive from source selection rather than lifecycle;
- made closure read represented evolution state;
- connected actual tool records to JSON-schema validation;
- made independently reproduced failures executable in `tools/candidate1_adversarial.py`;
- explicitly bounded inherited composed-validator PASS as regression preservation only;
- restored the Runtime Kernel and zh-CN adoption truth/identity boundaries.

The same DSH falsifier mechanically re-ran those paths and found the material defects closed without evolution starvation.

## Retained research/field residuals

candidate.2 does not pretend every observation must become a release blocker. The following remain visible for future research/field evidence:

- repeated reinterpretation/evaluation of the same experiment may be legitimate or may need stronger provenance semantics;
- locally successful reselection after source failure preserves source negative lineage, but that lineage becomes nested rather than top-level;
- archived/retired candidates have no in-place restore/reopen path in the reference tool; a new variation/export path remains available;
- nested migration lineage can grow in depth across generations.

These are not hidden and were not judged material blockers by the candidate.1 targeted revalidation.

## v0.3.5 semantic direction retained

- sustained self-evolution is the explicit ENA telos;
- governance is enabling infrastructure, not the purpose;
- exploration-forward posture: variation may precede certainty, selection follows observed outcome;
- event + periodic/idle evolution wake;
- Variation Space;
- adaptation/negative-evidence migration and Evolution Commons;
- recombination and positive emergence;
- pruning/archive/retirement;
- internal permission/capability topology may evolve without self-minting external mandate;
- Evolutionary Subject, Protected Subject, Continuity Vector;
- governance closure and removal of unbounded `organism` veto semantics;
- all 38 Constitution IDs retained with concept-map compression;
- English + Simplified Chinese semantic-projection model;
- lawful redaction/minimization/deletion while preserving occurrence truth where lawful;
- effective loaded surface and instruction-budget concerns;
- proposed retirement of future active adopter-facing `MAINLINE / NOT_MAINLINE` status while historical records remain history.

## Important compatibility boundary

The inherited `validate_contracts.py` implementation and historical fixture corpora remain an implementation regression surface. Their passing tests do **not** validate new v0.3.5 evolution/migration/emergence/language semantics.

## Stable foundations retained

- claim/evidence/support distinction;
- UNKNOWN discipline;
- recovery/history distinction;
- scoped authority;
- one singular Current adoption pointer;
- same version identity implies same effective content.
