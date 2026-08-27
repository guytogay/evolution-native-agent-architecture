# ENA Session Handoffs

Status: `CANONICAL_SUCCESSION_SURFACE / MAIN_VISIBLE / FRAMEWORK_PLUS_RECORDS`

This directory is the stable home for **project-manager/session succession**.

It deliberately separates reusable succession method from time-bounded handoff records.

```text
HANDOFF FRAMEWORK
!=
HANDOFF RECORD
!=
PROJECT METHODOLOGY
```

## Directory layout

```text
research/handoffs/
├─ README.md
├─ CURRENT-HANDOFF.yaml
├─ HANDOFF-PROTOCOL.md
├─ REQUIRED-TAKEOVER-CONTEXT.yaml
├─ PROJECT-MANAGEMENT-DISCIPLINE.md
└─ records/
   ├─ README.md
   └─ <handoff-id>/
      ├─ HANDOFF-START-HERE.md
      ├─ HANDOFF-MANIFEST.yaml
      ├─ PROJECT-STATE.md
      ├─ RECENT-THREE-ROUNDS.md
      ├─ FILE-CATALOG.md
      └─ HANDOFF-READBACK.md
```

## Layer 1 — reusable handoff framework

These files govern **every** future succession:

- `HANDOFF-PROTOCOL.md` — how the outgoing session hands over and how the incoming session takes over; both directions have equal continuity importance;
- `REQUIRED-TAKEOVER-CONTEXT.yaml` — machine-readable mandatory context, including project methodology;
- `PROJECT-MANAGEMENT-DISCIPLINE.md` — reusable project-management rules and promoted lessons;
- `CURRENT-HANDOFF.yaml` — stable current-record pointer plus takeover contract.

Do not bury reusable method inside one dated record.

## Layer 2 — handoff records

`records/<handoff-id>/` stores one succession occurrence: project state, recent decisions, file map, exact next action, and readback evidence.

A record is a bootstrap projection and lineage artifact, not project authority.

```text
HANDOFF_RECORD != CANONICAL_PROJECT_STATE
```

Older records remain useful for history, but only `CURRENT-HANDOFF.yaml` identifies the intended current record.

## Layer 3 — project methodology

ENA research methodology remains under:

`research/methodology/`

It is intentionally separate from handoff framework because it governs **how ENA is researched**, not only how sessions are replaced.

However, project methodology is mandatory takeover context. `REQUIRED-TAKEOVER-CONTEXT.yaml` makes that requirement explicit so a successor cannot inherit project state while silently dropping the method that produced it.

## Start here

For any new project-manager/session:

1. read `CURRENT-HANDOFF.yaml`;
2. read `HANDOFF-PROTOCOL.md`;
3. read `REQUIRED-TAKEOVER-CONTEXT.yaml`;
4. read `PROJECT-MANAGEMENT-DISCIPLINE.md`;
5. read the current record pointed to by `CURRENT-HANDOFF.yaml`;
6. independently reverify Current, live refs, exact frozen/released identities, methodology, Progress, and plan before substantive work.

## Promotion rule for lessons

When one handoff discovers a reusable lesson:

```text
instance incident
-> preserve occurrence evidence in record/history
-> promote reusable rule to framework or research methodology
```

Do not make the next session rediscover a method because it was trapped inside a dated directory.
