# ENA Handoff Record — Recent Decision-Bearing Rounds

Status: `RECENT_DECISION_CONTEXT / BOOTSTRAP_LINEAGE / NOT_RAW_CHAT`

Handoff ID: `2026-08-27-v037-independent-review-ready`

`THREE_ROUNDS` is the minimum continuity window, not a completeness limit.

## Round 1 — user challenged premature convergence in validation

### User concern

The project-manager described the author adversarial harness reduction from an observed 1080 pass conditions to 188 structured pass conditions as an improvement. The user warned that LLMs habitually narrate success through summarization/convergence, while ENA sometimes requires the opposite: recover, enumerate, branch, and preserve materially distinct variation.

### Project correction

The project distinguished:

```text
COMPRESS REPRESENTATION
!=
COMPRESS POSSIBILITY SPACE
```

and made convergence/divergence a canonical method question rather than a stylistic preference.

### Durable effect

`research/methodology/CONVERGENCE-DIVERGENCE-DISCIPLINE.md` became canonical.

The 1080 -> 188 claim was downgraded from "improvement" to an unverified author interpretation requiring anti-ablation audit.

### Subsequent project result

The audit later completed and found both legitimate oracle repair and several materially distinct lost attack shapes. Lost shapes were restored tree-external; frozen candidate bytes remained unchanged.

## Round 2 — user requested standardized normal session succession

### User requirement

Because the current session was becoming unstable, the user asked for a normal, reusable project handoff system. Required continuity included project plan, methodology, progress, recent decision context, file organization, and implementation/management experience in GitHub so a successor could take over without reconstructing the project from chat.

### Project response

A standardized handoff surface was created with:

- stable `CURRENT-HANDOFF.yaml` pointer;
- handoff package/record;
- project-state alignment before succession;
- recent-three-round continuity;
- file catalog;
- management lessons;
- incoming/outgoing protocol;
- post-merge readback.

### Durable lesson

```text
PROJECT_CONTINUITY > SESSION_CONTINUITY
HANDOFF_PACKAGE != PROJECT_AUTHORITY
```

The repository, not the outgoing chat, must carry the project forward.

## Round 3 — user identified hierarchy/authority mixing in the handoff design

### User correction

The user explicitly stated that:

- methodology is as important as project state during takeover;
- the rules for **handing over** and **taking over** are themselves equally important;
- reusable methodology/management knowledge should not be mixed into a dated project-specific handoff directory;
- the existing root-level dated folder plus method files elsewhere made the handoff hierarchy confusing.

### Structural correction

The handoff model was redesigned as three distinct layers:

```text
HANDOFF FRAMEWORK
!=
HANDOFF RECORD
!=
PROJECT METHODOLOGY
```

Target structure:

```text
research/handoffs/
  HANDOFF-PROTOCOL.md
  REQUIRED-TAKEOVER-CONTEXT.yaml
  PROJECT-MANAGEMENT-DISCIPLINE.md
  CURRENT-HANDOFF.yaml
  records/<handoff-id>/...

research/methodology/
  ENA project research methods
```

The current pointer now explicitly requires inheritance of project methodology and handoff/takeover rules; methodology is no longer merely an indirect link inside an instance manifest.

### New durable rule

```text
PROJECT_STATE_INHERITANCE WITHOUT METHOD_INHERITANCE = INCOMPLETE_TAKEOVER
INSTANCE_DISCOVERS_METHOD -> PROMOTE_METHOD -> KEEP_INSTANCE_AS_EVIDENCE
```

### Current consequence

The older `2026-08-27-v037-candidate0-frozen` handoff becomes historical lineage under `records/`; a new current record reflects that anti-ablation is complete and fresh independent Phase A on PR #115 is the next project action.

## Context beyond these three rounds that remains decision-material

The frozen candidate identity remains exact and must not be inferred from branch head:

```text
source = d0e793593184740d9732902e948afd48ed96ae2f
tree   = cffbf76fe1448b020b637c78d1f7ae46e4c0115b
```

Current remains `v0.3.6 / CURRENT / FIELD_VALIDATION`.

Fresh independent Phase A must precede author-oracle comparison.
