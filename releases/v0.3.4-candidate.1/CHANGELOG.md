# CHANGELOG — v0.3.4-candidate.1

Status: `IMPLEMENTATION_CANDIDATE / NOT_CURRENT / NOT_MAINLINE / NOT_PROMOTED`.

This is the corrected successor to the frozen `v0.3.4-candidate`. It does not rewrite the original freeze or its independent validation result.

## Independent validation input

Fresh independent runtime-adoption validation of the original frozen candidate returned:

`INDEPENDENT_RUNTIME_ADOPTION_VALIDATION_SUPPORTED_WITH_RESIDUALS`

The validator independently verified:

- frozen commit/tree/path/branch identity;
- self-contained candidate packaging;
- byte-identity of Constitution, roles, capability map, core contracts, schemas, templates, validator, fixtures, and regression runner against v0.3.3 Current;
- inherited 235-case regression PASS with zero unexpected verdicts/exceptions and zero inherited flips;
- sound profile-intensity, recovery, no-fake-task, hot/cold-path, convenience-bias, and fear-bias semantics.

The decisive residuals were:

### D14 — persisted source identity/drift

The original Compiled Local Projection required an ENA candidate/version identity but did not require an immutable commit/tree/package digest. A mutable label/branch could therefore become an inadequate integrity anchor, and a transformed persisted kernel could drift without explicit source-lineage/read-back semantics.

### D2 — persistence-boundary claim strength

The original wording said to test persistence across the claimed boundary only `where decision-critical`. For a cross-session persistent-adoption claim, the successor now makes the claimed boundary evidence requirement explicit: writing a persistence object in the current session does not prove a fresh session receives/applies it.

## Corrections in candidate.1

- Compiled Local Projection now records both human-readable version/candidate label and the **immutable canonical source identity actually compiled from** (Git commit/tree or package digest).
- Mutable branch/version label alone is explicitly insufficient as an integrity anchor.
- Source-identity change/conflict/unconfirmability is a cold-path retrieval/revalidation trigger when decision-relevant.
- Transformed/paraphrased persisted kernels preserve source/transformation lineage; successful storage is not semantic-fidelity proof.
- Cross-session/equivalent persistent-adoption claims require evidence across the actual claimed boundary.
- The genuine fresh-session persistence experiment remains open evidence work; this wording correction does not manufacture that evidence.

## Deliberately unchanged

- Constitution IDs/content: unchanged from v0.3.3 and original v0.3.4-candidate.
- Core composed claim-pack validator semantics: unchanged.
- Schemas: unchanged.
- 235-case regression corpus and runner: unchanged.
- Optional self-hosted recovery-root hardening remains a residual/field concern; it is not promoted into a new mandatory mechanism here.
- Open research #11/#15 and tooling drift #45 remain separate.

## Validation target

Next actor: the **same independent validator that identified D14/D2**, now acting as a prior-falsifier targeted revalidator.

It should verify:

1. original frozen candidate remains immutable and recoverable;
2. candidate.1 changes only the intended adoption-layer surfaces plus candidate identity/lineage;
3. D14 is actually closed without self-referential digest logic;
4. D2 cross-session claim strength is closed;
5. no new over-governance, per-task reread, or false-persistence path was introduced;
6. inherited mechanical semantics remain unchanged;
7. genuine fresh-session persistence evidence remains UNKNOWN/UNAVAILABLE when the Host cannot test it.

---

# Inherited lineage

v0.3.3 Current remains the released predecessor. The original `v0.3.4-candidate` remains frozen at semantic commit `ccc66233c1abe6778177a38950af1f7bb2356b93`, candidate-directory tree `61cb33562626c3b8f590919c87f4637416f1ee8f`, with its negative/residual evidence preserved rather than edited away.
