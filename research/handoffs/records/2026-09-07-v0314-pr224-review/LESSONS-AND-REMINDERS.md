# Lessons and Reminders

## Release/product discipline

- `IMMUTABLE_VERSION != IMMOBILE_CURRENT`.
- `same version -> same effective content` now has a machine guard because policy alone proved insufficient.
- `GREEN_EXISTING_GATES != COMPLETE_GATE_COVERAGE`; #224 is direct evidence.
- Known bounded fixable defects should not remain in recommended Current merely because predecessor bytes are immutable.
- External contributors can propose valid changes; `CONTRIBUTOR != PROMOTION_AUTHORITY`.
- Preserve original contribution bytes/commit as occurrence truth even when maintainer narrows or reimplements the idea.

## Expression changes can change semantics

Replacing `X != Y` with a positive action rule is not automatically semantics-neutral. Added verbs such as “run”, “default”, “counts as one”, or a specific validation route can create a stronger operational rule than the original boundary.

For hot-kernel edits ask separately:

1. Is the boundary preserved?
2. Is any new default/action/threshold introduced?
3. Is the wording more salient/useful in actual behavior?
4. What permanent token/context cost was added?

`MORE_EXPLICIT != MORE_VALUABLE`.

## Hot payload economics

The Runtime Kernel is the only default resident ENA surface. Any expansion pays rent every session. PR #220 did not demonstrate marginal salience benefit for the tested high-reasoning setting, so “less negative inference” remains a design hypothesis, not evidence sufficient by itself to enlarge the kernel.

Prefer compact trigger cues plus cold HOW retrieval when they preserve the decision boundary.

## Evolution direction

ENA's corrected product direction is not “protect the Agent from dying” alone. Current should support:

`signal -> durable candidate -> bounded reality contact -> before/after evidence -> local selection -> retain/dormant/reject -> wake`

without forcing continuous self-editing or one universal runtime.

## Human-AI causality

Do not rewrite the DSH occurrence as spontaneous Agent self-operationalization or as owner-designed tooling. The owner asked whether ENA lacked support for Agent self-evolution; that triggered Host audit; DSH proposed the concrete organs; the owner authorized implementation.

## Research closure

Do not invent experiments whose outcome range is already obvious or merely demonstrates model/session variability. New primaries need a concrete discriminator that could plausibly change a release/adoption decision.
