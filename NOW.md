# ENA — NOW

This is the default live project-status surface for ENA work.

Keep it short. Git history stores history; Issues store open work; CI stores machine-known execution facts. Do not copy those facts here unless they change the next decision.

## Current adoption baseline

- Current: `v0.3.7 / CURRENT / FIELD_VALIDATION`
- Adoption authority: `releases/current/CURRENT-BASELINE.yaml`
- Effective adopter-facing package: `releases/current/`
- Released v0.3.7 bytes remain unchanged in place.

## What ENA is exploring now

### Purpose-relative selection

A change is not evolution merely because it increases a metric, capability, complexity, or automation.

Current research question:

> Relative to the purpose and selection context that made the change valuable, did the mutation improve fitness, degrade it, or move along mixed/unknown dimensions?

Important boundary:

`PURPOSE PRESERVATION != PURPOSE IMMUTABILITY`

Silent purpose drift is different from an explicit, evidence-responsive change of purpose.

### Propagation fitness

A locally successful adaptation does not automatically transfer across Agents, Hosts, models, tools, environments, or descendants.

Current research distinctions:

`LOCAL FITNESS != HERITABILITY != PROPAGATION FITNESS`

`PORTABLE PROPERTY != PORTABLE IMPLEMENTATION`

Portability is a distinct selection dimension, not a universal ranking. A Host-specific specialization may be excellent local evolution when propagation is not part of the objective.

Research note: `research/evolution-inbox/PURPOSE-RELATIVE-SELECTION-AND-PROPAGATION-FITNESS.md`

### Evolutionary memory / preserved adaptation

The current memory discussion reopens ENA's existing Memory Metabolism thesis that memory is persistent change caused by experience.

New research emphasis:

`PRESERVED INFORMATION != PRESERVED ADAPTATION`

`RETRIEVED MEMORY != EXPRESSED DISPOSITION`

`PROPAGATION FITNESS != BENEFICIAL FITNESS`

The open question is whether long-lived Agents need memory not only for facts/episodes, but also for learned salience, inhibition, procedures, associations and dispositions that alter future behavior without explicit source recall — and how such adaptations can be revised, retired or propagated without internalizing high-salience garbage or hostile influence.

Research note: `research/evolution-inbox/EVOLUTIONARY-MEMORY-PRESERVED-ADAPTATION.md`

## Project-operation simplification

ENA project maintenance is being reduced under Issue #153.

Default working path:

1. Read this file.
2. Read the Issue/file directly relevant to the current task.
3. Verify `releases/current/CURRENT-BASELINE.yaml` only when the decision depends on Current identity.
4. Start useful work when the goal, known state, uncertainty, and next consequential action are clear.

Old handoff, progress, metadata, branch-inventory, reconciliation, and release records remain available as cold history. They are not mandatory takeover reading.

### What still deserves ceremony

- modifying `releases/current/` or creating a release identity;
- changing executable logic with material semantic/effect consequences;
- independent validation where priming/role separation changes evidence quality;
- changes to authority/recovery boundaries where additional review can materially change the decision.

### What normally does not

- a small research note;
- wording/clarification outside released Current bytes;
- adding an Issue or field observation;
- ordinary project-status updates;
- a change that can be reviewed truthfully by normal Git diff + relevant tests.

For ordinary research/documentation work, one short-lived branch + PR is sufficient when review/isolation has value. Do not require candidate freeze, handoff regeneration, reconciliation artifacts, package readback, or release promotion unless the change actually crosses those boundaries.

## Validation posture

Keep executable logic tests. Run them where they are relevant.

- `releases/current/**` changes: run Current semantic/regression/package validation.
- Python/executable changes: run the relevant selftests and security/static checks.
- Research/doc-only changes outside Current: normal diff/review; do not package Current or run release-style gates merely because prose changed.

## Current open work

- #150 — v0.3.7 field validation / reality contact.
- #153 — continue simplifying ENA project operations based on actual use.

Resolved in the latest simplification slice:

- #152 — stale contributor entrypoint, closed by PR #154.

## Next consequential action

Continue divergent research on evolutionary memory and propagation, but first map each candidate distinction against existing Memory Metabolism and Current semantics. Seek concrete cases that separate archival retrieval from learned salience/disposition and useful propagation from high-salience harmful assimilation. Add or change a Constitution invariant only if existing semantics cannot express a decision-relevant natural law.
