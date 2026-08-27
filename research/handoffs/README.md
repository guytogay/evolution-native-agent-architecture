# ENA Session Handoffs

Status: `PROJECT_CONTINUITY_SURFACE / MAIN_VISIBLE / HANDOFF_HISTORY`

This directory stores standardized project-manager/session handoff packages.

A handoff is a fast bootstrap projection. It does **not** replace Current, branch authority, frozen candidate records, canonical methodology, or live repository state.

## Stable pointer

Always start with:

`research/handoffs/CURRENT-HANDOFF.yaml`

Do not infer the active handoff from directory names, timestamps, or commit recency.

## Directory layout

```text
research/handoffs/
├─ README.md
├─ CURRENT-HANDOFF.yaml
└─ <handoff-id>/
   ├─ HANDOFF-START-HERE.md
   ├─ PROJECT-STATE.md
   ├─ RECENT-THREE-ROUNDS.md
   ├─ FILE-CATALOG.md
   ├─ PROJECT-MANAGEMENT-LESSONS.md
   └─ HANDOFF-MANIFEST.yaml
```

The package shape is a default, not an ontology. Add another file only when it has a distinct continuity purpose.

## Meaning of each surface

- `HANDOFF-START-HERE.md` — shortest human takeover path and exact next action.
- `PROJECT-STATE.md` — detailed current-state projection with exact refs and invariants.
- `RECENT-THREE-ROUNDS.md` — minimum recent conversational decision lineage.
- `FILE-CATALOG.md` — categorized repository map and recommended read order.
- `PROJECT-MANAGEMENT-LESSONS.md` — management/method incidents the next session should operationally inherit.
- `HANDOFF-MANIFEST.yaml` — machine-readable handoff identity and pointers.

## Authority boundary

```text
HANDOFF_PACKAGE != CANONICAL_PROJECT_STATE
```

If a handoff conflicts with a live authoritative source, verify the authoritative source and repair the handoff/control plane before proceeding.

Canonical handoff method:

`research/methodology/SESSION-HANDOFF-DISCIPLINE.md`

Project-state realignment method:

`research/methodology/PROJECT-STATE-ALIGNMENT-GATE.md`

## Historical handoffs

Older handoff packages remain useful for lineage, incident reconstruction, and understanding why a later session changed direction.

```text
HISTORICAL_HANDOFF_PRESERVED != HISTORICAL_HANDOFF_ACTIVE
```
