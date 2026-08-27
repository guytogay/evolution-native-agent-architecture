# ENA Handoff Records

Status: `HANDOFF_INSTANCE_HISTORY / BOOTSTRAP_LINEAGE / NOT_PROJECT_AUTHORITY`

This directory contains time-bounded project-manager/session handoff occurrences.

Each child directory represents one handoff record. Records may contain project state, recent decision context, file catalogs, exact identities, next actions, and readback evidence.

Reusable succession rules do **not** belong here. They live at `research/handoffs/` root.

Reusable ENA research method does **not** belong here. It lives under `research/methodology/`.

```text
records/<handoff-id> = occurrence
research/handoffs/*.md|yaml = succession framework
research/methodology/ = ENA research method
```

Use `research/handoffs/CURRENT-HANDOFF.yaml` to discover the intended current record. Do not infer it from timestamps, directory names, or commit recency.

Historical records remain lineage and may intentionally describe project state that is no longer current.
