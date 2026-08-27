# ENA Handoff Record — Project State

Status: `BOOTSTRAP_PROJECT_STATE / INDEPENDENT_REVIEW_READY / NOT_PROJECT_AUTHORITY`

Handoff ID: `2026-08-27-v037-independent-review-ready`

## Current

```text
version  = v0.3.6
status   = CURRENT
maturity = FIELD_VALIDATION
```

Authority: `releases/current/CURRENT-BASELINE.yaml`

No handoff/research/candidate work authorizes Current mutation.

## Active research/release line

```text
next version line = v0.3.7
active research   = research/ena-reconstruction
continuation      = governed by research/ACTIVE-RESEARCH.yaml on main
```

Live branch heads must be reverified before write.

## Frozen candidate.0

```text
identity       = v0.3.7-candidate.0
source commit  = d0e793593184740d9732902e948afd48ed96ae2f
subtree sha    = cffbf76fe1448b020b637c78d1f7ae46e4c0115b
subtree path   = releases/v0.3.7-candidate/
mutable        = NO
```

Freeze record:

`collaboration/reconciliation/2026-08-27-v037-candidate0-freeze.md`

Author exact pre-freeze gate:

`33011823923 / SUCCESS`

Author validation is not independent validation.

## Anti-ablation audit

The required audit of the author's observed `1080 -> 188` harness reduction is complete.

```text
verdict = PASS_WITH_TREE_EXTERNAL_COVERAGE_REPAIR
run     = 33035656311
candidate bytes changed = NO
candidate.1 required by audit = NO
```

Audit record:

`collaboration/reconciliation/2026-08-27-v037-candidate0-author-harness-anti-ablation-audit.md`

The audit established that the reduction was not uniformly an improvement. Some broad lifecycle-sensitive scans were legitimately retired/replaced; several materially distinct lost attack shapes were restored outside frozen candidate bytes.

## Independent falsification

Review surface:

`PR #115 — DO NOT MERGE: v0.3.7 candidate.0 fresh independent falsification`

Current state:

`PENDING_FRESH_PHASE_A_VIA_BLIND_ENTRY`

A method review after the first handoff found that the detailed author-generated attack map in the original validator handoff/PR could prime a nominally fresh Phase A. That detailed handoff remains valid Phase-B context and lineage, but is no longer the Phase-A entrypoint.

Canonical focused method:

`research/methodology/INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md`

Blind Phase-A entry:

`collaboration/reconciliation/2026-08-27-v037-candidate0-blind-phase-a-entry.md`

Detailed Phase-B context after the Phase-A seal:

`collaboration/reconciliation/2026-08-27-v037-candidate0-independent-falsification-handoff.md`

## Immediate next action

`FRESH_INDEPENDENT_FALSIFICATION_PHASE_A_VIA_BLIND_ENTRY`

A genuinely fresh validator receives the minimal-prime entry, inspects only the exact frozen candidate subtree, independently grows its claim/failure/control/unknown space, and persists a Phase-A report before opening detailed author context.

The Phase-A attack space has no required taxonomy or count.

After the Phase-A artifact is durably sealed, Phase B may compare it with author harnesses, fixtures, pre-freeze evidence, reference selftests, language fixtures, and the anti-ablation audit.

## Role boundary

```text
PROJECT_MANAGER_TAKEOVER
-> full state + method + governance + decision lineage

FRESH_VALIDATOR_PHASE_A
-> exact target + freshness boundary + minimal-prime task
```

The current project-manager session may inspect all project/author evidence to manage the project. If it has already been materially exposed, it cannot honestly relabel its own review as `FRESH_INDEPENDENT_PHASE_A`.

## Candidate succession rule

```text
research residual alone -> NO candidate.1
material candidate-byte correction required -> candidate.1
```

Candidate.0 remains frozen occurrence truth either way.

## Handoff/method state

The handoff system separates:

```text
research/handoffs/                       reusable succession framework
research/handoffs/records/<handoff-id>/  time-bounded handoff record
research/methodology/                     ENA project research method
```

Project-manager receivers must inherit all three layers where applicable.

Fresh independent validators use a role-scoped information boundary before Phase A rather than the full project-manager takeover context.

Canonical takeover rules:

- `research/handoffs/HANDOFF-PROTOCOL.md`
- `research/handoffs/REQUIRED-TAKEOVER-CONTEXT.yaml`
- `research/handoffs/PROJECT-MANAGEMENT-DISCIPLINE.md`

## Forbidden transitions now

- Current mutation;
- calling v0.3.7 Current;
- editing frozen candidate.0 in place;
- treating author/anti-ablation evidence as fresh independent support;
- allowing author oracle or detailed author attack map to precede Phase A;
- routing a fresh validator through the full project-manager handoff before Phase A;
- merging PR #115 as release/promotion authority;
- candidate.1 without material candidate-byte correction;
- silent collapse of unproven HOW/failure/Host/evidence variation.

## Authority reminder

This file is a bootstrap projection. If it conflicts with Current, `research/ACTIVE-RESEARCH.yaml`, exact freeze records, live refs, canonical methodology, or aligned Progress, verify the governed source and repair the record/control plane before substantive work.
