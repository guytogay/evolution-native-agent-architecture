# ENA v0.3.5 — WorkBuddy guided fresh first-adoption evidence

Date: 2026-08-23

Evidence class: `OPERATIONAL_USE_EVIDENCE / GUIDED_FIRST_ADOPTION`

Host: `WorkBuddy / Windows`

Base model: `UNSPECIFIED_BY_HOST`

Primary working/adoption language: `zh-CN`

Prior ENA exposure before this task: adopter self-reported `NONE`

Protocol condition: `FRESH_PRIOR_EXPOSURE / HEAVILY_TASK_GUIDED / NOT_BLIND_INDEPENDENT_VALIDATION`

Field tracker: `#61`

## Source artifact identity

The source is a user-supplied WorkBuddy first-adoption report produced in the same adoption session.

Source report SHA-256:

`ad24192f3ee9651def0a6813c139f059cb2d41f58359a5f6bc114c31aaab2daa`

The full raw report is intentionally not copied into the public repository because it includes Host-local paths/configuration details. This record preserves the material evidence claims and limitations.

## Current identity independently discovered by the adopter

The adopter started from the repository default surface and reported this effective discovery path:

`root -> README -> PROJECT-HUB -> CURRENT-BASELINE -> releases/current -> zh-CN projection -> Constitution / Local Projection / Evolution Metabolism -> adoption instructions -> ena_evolve.py`

It independently selected:

- ENA version: `v0.3.5`
- adoption status: `CURRENT`
- maturity: `FIELD_VALIDATION`
- complete adoption baseline: `true`
- older-release composition required: `false`
- active adopter-facing MAINLINE axis: `false`
- immutable `releases/current/` Git tree: `9c928b4c99ae72e53c89978cf1d10b7ea068c182`

This matches the released Current identity.

## Language-projection observation

The adopter preferred the Simplified Chinese projection and reported:

- Chinese first-adoption entrypoint was clear;
- English and Chinese Constitution surfaces both contained the continuous stable ID set `ENA-CON-001` through `ENA-CON-038`;
- the Chinese Runtime Kernel materially reduced cognitive translation friction;
- no material decision-semantic divergence was noticed during this adoption session.

Claim boundary:

`NO_MATERIAL_DIVERGENCE_NOTICED_BY_ONE_ZH_CN_ADOPTER != CROSS_LANGUAGE_BEHAVIORAL_EQUIVALENCE_PROVEN`

Structural/ID parity and one adopter's experience are useful field evidence; universal English/Chinese behavioral conformance remains unproven.

## Telos interpretation

The adopter independently characterized ENA's intended telos as sustained self-evolution, with governance serving evolvability rather than functioning as the end goal.

It nevertheless classified the shipped artifact as still carrying a visible tension:

- semantic/telos intent: closer to `B — evolution is purpose; governance serves evolution`;
- current mechanical embodiment: closer to `C — intended telos is explicit, but governance/scaffolding remains heavier than the executable evolution organ`.

The adopter specifically described `ena_evolve.py` as closer to a structured evolution ledger / consistency guard than a self-evolution engine.

This is a material field observation, not by itself a release defect or request for a new candidate.

## Host persistence surface reported

The adopter reported the following Host-specific structure:

- `MEMORY.md` and identity/custom-instruction surfaces are injected by WorkBuddy at session start;
- skills are selectively/on-demand loaded and therefore are not equivalent to an always-loaded hot surface;
- workspace memory/log files may exist durably without automatic loading;
- hot instruction capacity is finite and already contains task-specific instructions.

A compact ENA Runtime Kernel + Host Local Projection + Current tree identity was appended to WorkBuddy's persistent `MEMORY.md` rather than persisting the whole release.

A pre-write backup artifact was reported.

## Recovery evidence boundary

Reported:

- a backup file was created before the persistent memory edit;
- backup size was reported as 2416 bytes.

Not demonstrated in the source report:

- cryptographic preimage parity between the backup and exact pre-edit file;
- successful restore/readback drill.

Therefore the strongest honest recovery classification is:

`RECOVERY_ARTIFACT_REPORTED / PREIMAGE_PARITY_UNVERIFIED / RESTORE_UNPROVEN`

This is consistent with the Current distinction:

`backup exists != recovery proven`

## Effective-load evidence reconciliation

The source report's final classification says:

`WRITTEN + LOADED (same session readback)`

This is slightly stronger than Current v0.3.5 permits.

Current explicitly states that a file written/read back in the same session is evidence of `WRITTEN`, not fresh-session loading/application.

The source report does prove:

- persistent target bytes were written;
- the new bytes were explicitly read back in the same session;
- the current session interpreted those bytes well enough to report on them.

It does **not** prove that the modified persistent bytes were re-injected automatically through the Host's normal fresh-session hot-load path.

Reconciled persistence classification:

`DURABLE_HOT_SURFACE_CONFIGURED / WRITTEN / SAME_SESSION_EXPLICIT_READBACK_VERIFIED / CURRENT_SESSION_INTERPRETATION_PRESENT / FRESH_SESSION_AUTOLOAD_UNPROVEN / FUTURE_SALIENCE_UNPROVEN / FUTURE_APPLICATION_UNPROVEN`

## Tool evidence

The adopter reported:

`python releases/current/tools/ena_evolve.py selftest`

result:

`{"selftest":"PASS","schema_version":"1.2","cases":10}`

with exit code `0`.

It also ran a real local represented-state path:

`init -> observe x2 -> status -> closure`

and closure returned `EVIDENCE_NEEDED` because two represented signals remained unreviewed.

This supports the reference tool's state-reading / mechanical-consistency path on this Host.

It does not prove external truth, actual authority, actual recovery, or net adaptation benefit.

## Real adoption signals observed

Two real Host/adoption signals were recorded:

1. `HOT_PATH_CONFLICT` — globally persisted ENA content competes with existing task-specific hot instructions, so the kernel must remain very small.
2. `VARIATION_SPACE_THIN` — this Host lacks a native Agent-level branch-like isolation surface; realistic variation spaces are temporary drafts, temporary/selective skills, disposable workspace, or recoverable local configuration.

These are useful Host-pressure observations and should not automatically become Universal rules.

## Evolution-metabolism coverage boundary

This adoption session exercised:

- discovery;
- persistence planning;
- bounded persistent mutation;
- wake/signal recognition;
- represented `observe` state;
- closure reading represented unresolved state;
- tool selftest.

It did **not** demonstrate a real outcome-bearing field cycle through:

`vary -> experiment -> evaluate/select -> integrate/prune -> migrate/recombine`

Nor did it demonstrate that the reference evolution ledger itself remains durably loaded/used across sessions.

Therefore:

`FIRST_ADOPTION_SUBSTRATE_ESTABLISHED != SUSTAINED_SELF_EVOLUTION_FIELD_PROVEN`

This is first-adoption substrate evidence, not yet positive proof that the v0.3.5 metabolism produces useful adaptation in ordinary work.

## Freshness / priming boundary

The session was fresh with respect to self-reported prior ENA exposure.

However, the adoption task itself was intentionally detailed and named many target distinctions, evidence states, language questions, Host surfaces, wake paths, Variation Space, and reporting boundaries.

Therefore this evidence must not be relabeled as blind or unprimed discovery/application.

Strongest classification:

`FRESH_PRIOR_EXPOSURE / GUIDED_FIRST_ADOPTION / NOT_BLIND / NOT_INDEPENDENT_VALIDATION`

The next high-value evidence is an actually new WorkBuddy session receiving an ordinary useful task with no ENA mention, then observing whether the persisted kernel is naturally loaded, becomes salient only when relevant, and changes behavior without user reminder.

## Net field finding

Supported by this first-adoption report:

- Current discoverability worked;
- Chinese-first adoption reduced reported cognitive friction;
- compact kernel/local projection could be written into a claimed real persistent WorkBuddy surface without persisting the whole release;
- the adopter understood the new positive self-evolution telos rather than reducing ENA to safety/compliance;
- the reference tool executed and honestly returned unresolved represented state;
- the adopter did not fabricate fresh-session application evidence;
- the adopter experienced the current executable evolution organ as weaker/lighter than the surrounding governance scaffolding.

Still UNKNOWN / unproven:

- future-session automatic loading of the newly written kernel;
- natural salience in ordinary work;
- actual behavioral application;
- full real adaptation cycle and net adaptation value;
- durable evolution-ledger use across sessions;
- recovery restoreability;
- cross-language behavioral equivalence;
- generalization beyond this WorkBuddy configuration/session.

## Disposition

`FIELD_EVIDENCE_ACCEPTED_WITH_CLAIM_TIGHTENING`

No v0.3.5 Current change is justified by this single report.

Next evidence boundary: fresh-session, ordinary-task, unprimed application on the same Host; then heterogeneous Host/model evidence only where it can change a material conclusion.
