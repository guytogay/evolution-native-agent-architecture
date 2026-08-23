# ENA v0.3.5 Frozen Candidate — Post-Freeze Author Observation

Date: 2026-08-23

Applies to frozen candidate tree:
`f373e7695348c157dcd48d3ed243ea3079215b8f`

Status:
`POST_FREEZE_AUTHOR_OBSERVATION / NOT_INDEPENDENTLY_CONFIRMED / CANDIDATE_UNCHANGED`

This note intentionally does **not** modify the frozen candidate.

## PF-A1 — Lifecycle state may obscure selection state in migration export

While preparing the independent-falsification prompt after freeze, the author noticed a potential semantic/tooling defect in `tools/ena_evolve.py`.

The reference tool currently uses candidate `status` for several different state axes. `cmd_evaluate()` writes selection states such as:

`SUPPORTED | PARTIAL | NOT_SUPPORTED | HARMFUL | UNKNOWN`

Later lifecycle operations overwrite `status`, for example:

- committed integration -> `INTEGRATED`;
- archive -> `ARCHIVED`;
- retirement -> `RETIRED`.

`migration_packet()` derives `packet_purpose` primarily from the current `status`.

Potential false-confidence case:

1. candidate is explicitly evaluated `UNKNOWN`;
2. bounded unknown integration is permitted by the reference tool after experiment + explicit UNKNOWN evaluation;
3. integration changes candidate `status` to `INTEGRATED`;
4. migration export sees `INTEGRATED` and classifies it as `ADAPTATION_CANDIDATE`;
5. the source's unresolved selection state may therefore be obscured by a later lifecycle state.

The same general issue can affect archived/retired candidates: lifecycle state and evidence-backed selection state are conceptually different axes.

Candidate schema/template already partly distinguishes `status` and `selection`, which makes the tool's conflation more suspicious.

### Property at stake

`lifecycle state != selection/evidence state`

`integration != proof of improvement`

`migration must preserve source selection status`

### Possible minimal correction if independently confirmed

Preserve a separate `selection_state` (or derive source selection from the latest evaluation / integration evidence-state-at-commit) and compute migration `packet_purpose` from the evidence-backed selection axis rather than lifecycle status.

An `UNKNOWN` integration must remain `UNRESOLVED_VARIATION` when exported unless later evidence changes the selection state.

An archived/retired supported adaptation may remain a positive adaptation candidate with its lifecycle status separately represented; an archived harmful variation remains negative evidence.

## Independent-review protocol

To preserve falsification value, an independent validator should first inspect the frozen candidate itself **without reading this note as an oracle**. After completing an independent Phase A finding set, it may read this note and determine whether PF-A1 is:

- independently reproduced;
- a false alarm;
- partially valid;
- or evidence of a broader state-model problem.

No candidate.1 is authorized until the issue is independently assessed or otherwise reconciled.
