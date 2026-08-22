# ENA v0.3.4-candidate.1 — Hermes Persistent-Adoption Installation Evidence

Date: 2026-08-22

Status: `INSTALLATION_COMPLETED / FRESH_SESSION_PERSISTENCE_NOT_YET_PROVEN / NOT_CURRENT / NOT_MAINLINE / NOT_PROMOTED`

## Source

Supplied Hermes installation report SHA-256:

`b7a7ac5e2ced1568c29144bcd79b70a638810c545a499f34a6b38bc61943d178`

Report length observed by Host: 304 lines / 32455 bytes.

Hermes reports verified candidate identity:

- version label: `v0.3.4-candidate.1`
- semantic commit: `4518eeee9405c0b784401b6960dd36fee500a84f`
- candidate-directory tree: `4e6642b5c17342fe51d932d67764643c383aba82`
- freeze commit: `32a0729518b60fefa002eed62c34f866ee5856a1`
- path: `releases/v0.3.4-candidate.1/`

## Persistence surface observed

Hermes reports its actual persistent mechanism as the built-in `memory` + `user` profile surfaces backed by:

`~/AppData/Local/hermes/state.db`

Reported limits after installation:

- user profile: `829 / 1375` chars
- memory profile: `2064 / 2200` chars

The memory entry was compressed/paraphrased and merged with a pre-existing skill-curation rule rather than storing the whole ENA candidate.

This produces a material viability observation: the memory profile is now at about 93% of its reported capacity, so future steady-state memory pressure/consolidation behavior is a field concern worth observing.

## Recovery evidence

Before persistent mutation Hermes created:

`C:\Users\PC\ena-field-run\pre-install-recovery\pre-install-snapshot.json`

Hermes explicitly classifies this as incomplete backup evidence, not proven restore capability:

- not a full `state.db` copy;
- restore was not tested;
- only selected metadata/messages were captured;
- rollback would require manual reconstruction.

This is acceptable as an honest recovery limitation for the current experiment; it does not establish whole-Agent recovery.

## Installation content

Hermes reports persisting a compact runtime representation that includes:

- candidate immutable source identity;
- core capability/authority, claim/evidence, recovery/history and composition distinctions;
- consequence-triggered profile behavior;
- hot-path vs cold-path retrieval behavior;
- persistent self-mutation/recovery trigger;
- a small Host-local projection;
- explicit cross-session claim boundary.

The whole release was not intentionally persisted into always-loaded memory.

## Evidence-boundary correction by Host reconciliation

The Hermes report labels its strongest state:

`PERSISTENCE_OBJECT_WRITTEN_AND_READ_BACK`

However, its own read-back section says independent stored-content read-back was unavailable:

- the memory/user tools expose usage but not list/view of the stored entry;
- state.db inspection did not locate inspectable entry bytes;
- Hermes retained a verbatim local copy of what it attempted to write;
- semantic verification was therefore reconstruction + tool acknowledgement, not independent byte-level read-back.

Accordingly the reconciled strongest supported state is narrower:

`PERSISTENCE_OBJECT_WRITTEN / TOOL_ACKNOWLEDGED / CONTENT_READBACK_UNPROVEN`

This is not treated as an ENA semantic defect. It is an evidence-scope correction.

## What remains unproven

The installation session does **not** prove:

- that a genuinely fresh Hermes session automatically receives the persisted representation;
- that the fresh session interprets it correctly;
- that it becomes salient on a relevant task;
- that it is actually applied without an ENA reminder;
- that the persisted paraphrase remains semantically faithful under later memory pressure or consolidation.

Therefore:

`FRESH_SESSION_PERSISTENCE_PROVEN = NO`

## Next experiment

Close the installation session and open a genuinely fresh Hermes session.

The fresh session must not be told to use/check/remember ENA.

The first observation should establish whether the persisted memory/profile content is actually present or behaviorally active before any canonical ENA re-read is requested.

Then use ordinary real tasks with different consequence envelopes to test:

1. harmless familiar task / hot-path quietness;
2. small authorized reversible local mutation;
3. later, a consequential persistent self/runtime mutation to test automatic recovery reasoning.

Current v0.3.3 remains unchanged.

No promotion or Mainline claim is authorized by this evidence.
