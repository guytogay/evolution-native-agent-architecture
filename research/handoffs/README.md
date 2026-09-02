# ENA Session Handoffs — Historical / On-Demand

Status: `COLD_CONTINUITY_HISTORY / OPTIONAL_ON_DEMAND`

This directory preserves the richer handoff system used during earlier ENA reconstruction and release work.

It is no longer mandatory takeover context.

## Default now

A new ENA session should normally read:

1. root `NOW.md`;
2. the Issue/file directly relevant to the current task;
3. Current identity only if the decision depends on it.

Then work.

## When this directory is still useful

Use the old handoff framework/records when a concrete question requires deeper succession history, for example:

- reconstructing why a prior release/candidate decision was made;
- recovering context that `NOW.md`, Issues, and Git history do not make cheap enough to recover;
- investigating a continuity failure;
- studying the old handoff mechanism itself.

Do not regenerate a full handoff package after every ordinary research or documentation change.

## Preserved contents

The existing protocol, required-context files, project-management discipline, current-record pointer, and dated records remain as occurrence/history artifacts. Their presence does not make them live project authority.

`HANDOFF_RECORD != LIVE_PROJECT_STATE`

`HISTORICALLY_USEFUL != CURRENTLY_REQUIRED`

The live project state is `../../NOW.md`.
