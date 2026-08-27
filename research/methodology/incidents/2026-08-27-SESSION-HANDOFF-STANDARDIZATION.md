# Session Handoff Standardization Incident — 2026-08-27

Status: `METHODOLOGY_TRIGGER_EVIDENCE / PROJECT_CONTINUITY_INCIDENT / NON_NORMATIVE_TO_CURRENT`

## Trigger

The user intentionally decided to replace the current project-manager session because the session had become unstable and asked that project handoff become a standardized normal behavior for future Agents/sessions.

During handoff preparation, a live-state audit found that main-visible control surfaces still described v0.3.7 candidate.0 as not yet created, while the actual project had already:

- built candidate.0;
- completed author validation;
- frozen candidate.0 by exact source/subtree binding;
- prepared an independent falsification handoff;
- canonicalized a new convergence/divergence methodology correction.

The stale surfaces included at least:

- `research/ACTIVE-RESEARCH.yaml`;
- `research/plans/PROGRESS.yaml`;
- long-horizon master-plan current phase descriptions.

A plain chat summary would therefore have been insufficient and potentially misleading.

## Failure model

```text
PROJECT_WORK_PERSISTED
BUT
CONTROL_PLANE_STALE
+
SESSION_REPLACED
-> SUCCESSOR_REENTERS_OLD_PHASE
```

Also:

```text
CHAT_SUMMARY_ONLY
-> FAST_CONTEXT
BUT
NO_STANDARD_POINTER / NO_FILE_CATALOG / NO_LIVE_READBACK
-> RECONSTRUCTION_BURDEN + DRIFT
```

## Correction

Create a canonical session-handoff discipline and a stable current-handoff pointer.

```text
PROJECT_CONTINUITY > SESSION_CONTINUITY
HANDOFF = DURABLE_BOOTSTRAP_PROJECTION
HANDOFF != PROJECT_AUTHORITY
```

Required behavior now includes:

- persist material work before exit;
- reverify Current/live refs/frozen identities;
- align stale project-state surfaces;
- create a classified handoff package;
- preserve at least the latest three decision-bearing conversation rounds;
- publish a file catalog and machine-readable manifest;
- record exact next and forbidden actions;
- update `research/handoffs/CURRENT-HANDOFF.yaml`;
- integrate main-visible handoff/control-plane changes through PR/CI;
- incoming session reads handoff for speed, then verifies canonical sources/live refs before work.

Canonical method:

`research/methodology/SESSION-HANDOFF-DISCIPLINE.md`

## Why recent-three-rounds is a minimum, not an ontology

The user explicitly requested preservation of the project's recent three conversation rounds.

The standard adopts that as a minimum continuity window, while preserving open cardinality:

```text
THREE_ROUNDS = MINIMUM_CONTINUITY_WINDOW
THREE_ROUNDS != MAXIMUM_RELEVANT_HISTORY
```

Older decision rounds must be included when they remain necessary to explain current state or next action.

## Anti-convergence interaction

Handoff writing itself can trigger LLM summarization bias.

Therefore:

```text
COMPRESS_HANDOFF_PROSE = ALLOWED
COMPRESS_DECISION_RELEVANT_VARIATION = NOT_ALLOWED_WITHOUT_EQUIVALENCE_EVIDENCE
```

A clean executive summary must coexist with explicit residuals, deferred branches, exact identities, and a deeper file map.

## Practical effect

A future project-manager session should be able to start from `main`, follow one stable handoff pointer, verify reality, and continue the exact next action without asking the user to reconstruct the project from conversational memory.

```text
HANDOFF_WRITTEN != HANDOFF_APPLIED
```

The real success test is successor behavior.
