# Handoff Hierarchy Correction Incident — 2026-08-27

Status: `METHOD_INCIDENT / STRUCTURE_CORRECTION / MAIN_VISIBILITY_PENDING`

## Trigger

The first standardized session handoff mixed three semantically different things:

1. reusable rules for handing a project over and taking it over;
2. reusable cross-session project-management lessons;
3. one dated, project-state-specific handoff occurrence.

The root handoff directory contained a dated folder directly, while canonical handoff rules lived under `research/methodology/`, and `PROJECT-MANAGEMENT-LESSONS.md` lived inside the dated record.

The user explicitly challenged this hierarchy and clarified two requirements:

- **project methodology is as important as project state during takeover**;
- **the rules for handing over and the rules for taking over are themselves first-class project-continuity method**.

## Failure shape

The previous layout allowed a successor to infer the wrong ontology:

```text
research/handoffs/<dated-record>/
  PROJECT-MANAGEMENT-LESSONS.md

research/methodology/
  SESSION-HANDOFF-DISCIPLINE.md
```

This mixed record-local occurrence with reusable method and made mandatory takeover context only indirectly discoverable.

```text
DISCOVERABLE_SOMEWHERE != EXPLICITLY_REQUIRED_FOR_TAKEOVER
```

## Correction

The handoff system was split into three layers:

```text
HANDOFF FRAMEWORK
research/handoffs/

HANDOFF RECORDS
research/handoffs/records/<handoff-id>/

PROJECT METHODOLOGY
research/methodology/
```

Canonical root framework now includes:

- `research/handoffs/HANDOFF-PROTOCOL.md`;
- `research/handoffs/REQUIRED-TAKEOVER-CONTEXT.yaml`;
- `research/handoffs/PROJECT-MANAGEMENT-DISCIPLINE.md`;
- `research/handoffs/CURRENT-HANDOFF.yaml`.

The dated handoff directory was moved under `records/`. Reusable management lessons were promoted to root discipline instead of remaining trapped in the instance.

## New invariants

```text
HANDOFF_FRAMEWORK != HANDOFF_RECORD
HANDOFF_RECORD != PROJECT_METHODOLOGY
PROJECT_STATE_INHERITANCE_WITHOUT_METHOD_INHERITANCE = INCOMPLETE_TAKEOVER
INSTANCE_DISCOVERS_METHOD -> PROMOTE_METHOD -> KEEP_INSTANCE_AS_EVIDENCE
```

Outgoing and incoming succession protocols are treated as equally important halves of continuity.

## Additional alignment finding

During this structural correction, `research/RESEARCH-START-HERE.md` was also found stale: it still named the `1080 -> 188` anti-ablation audit as the next action after that audit had already completed and PR #115 had become the fresh independent Phase A review surface.

This reinforced:

```text
DIRECTORY_CLEANUP_WITHOUT_STATE_ALIGNMENT != SAFE_HANDOFF
```

## Practical effect

A successor can now see, before opening a dated record:

- how to take over;
- how an outgoing session should hand over;
- which project-management discipline must remain salient;
- which ENA research methodology is mandatory context;
- where the current record lives;
- which sources remain project authority.

The record accelerates takeover but no longer contains the canonical method needed for all future takeovers.
