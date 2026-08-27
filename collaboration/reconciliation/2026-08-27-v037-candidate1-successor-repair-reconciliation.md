# ENA v0.3.7 candidate.1 — successor repair reconciliation

Status: `SUCCESSOR_REPAIR_RECONCILED / READY_FOR_EXACT_PREFREEZE_VALIDATION / NOT_FROZEN / NOT_CURRENT / ATTACK_CARDINALITY_OPEN`

Date: 2026-08-27

This record preserves the transition from the sealed fresh blind Phase A of frozen `v0.3.7-candidate.0` through author Phase-B reconciliation and targeted successor repair. It is not release authority and does not replace the sealed independent Phase-A occurrence.

## Immutable predecessor evidence

- frozen candidate.0 source: `d0e793593184740d9732902e948afd48ed96ae2f`
- frozen candidate.0 subtree: `cffbf76fe1448b020b637c78d1f7ae46e4c0115b`
- fresh blind Phase-A seal commit: `5ba3d241efa460fe170253860ad67045aa1d96a5`
- Phase-A report: `collaboration/reconciliation/2026-08-27-v037-candidate0-independent-phase-a-primary.md`
- Phase-B reconciliation commit on research branch: `cbdc2b00a4bdb490b83aff426db3cfe844e22490`
- candidate.0 reconciled verdict: `NEEDS_REVISION / CANDIDATE_1_REQUIRED`

The sealed Phase-A report remains immutable occurrence truth. Candidate.1 does not rewrite it.

## Why candidate.1 was required

Fresh Phase A independently found four deterministic candidate-byte defects that author validation had missed:

1. imported packet records did not durably retain represented source Variation Space / Evolutionary Subject / Protected Subjects;
2. packet expression-history consistency allowed tied latest timestamps that the record validator treated as ambiguous;
3. `archive.selection_state_preserved` could contradict the record selection state while still passing;
4. the shipped v2 template used a non-time placeholder for `created_at` while selftest treated the template as a machine-valid record.

Phase B classified all four as `CANDIDATE_DEFECT / SHARED_BLIND_SPOT`, not as intentional trust boundaries or wrong fresh-validator oracles.

Candidate.1 therefore exists under the frozen-candidate succession rule: material correction after candidate.0 freeze requires a successor identity rather than in-place mutation.

## Candidate.1 lineage

Branch:

`candidate/v0.3.7-candidate.1`

Candidate.0 remains immutable predecessor lineage.

### Repair round 1 — sealed Phase-A findings

The first exact-anchor transformation produced cargo commit:

`583ac81...` — `candidate1: apply sealed Phase A repairs`

The repair retained source applicability context inside migration provenance without laundering it into receiver-local applicability or selection; rejected tied latest packet expression timestamps; bound archive preservation metadata to represented selection; and made an uninstantiated template timestamp invalid while keeping helper-instantiated latent records valid.

Targeted successor validation after that repair:

- workflow: `ENA v0.3.7 Candidate.1 Targeted Repair Gate`
- run: `33051985315`
- result: `SUCCESS`
- record validator selftest: `20` observed cases at that point
- helper selftest: `11` observed cases at that point
- Phase-A-derived targeted conditions: `16 / PASS`
- `attack_cardinality=OPEN`
- `fresh_independent_phase_a_repeated=NO`

The observed counts are corpus facts, not completeness thresholds.

### Open-branch expansion after round 1

Instead of treating the four repairs as closure, focused probes followed still-open branches from the fresh Phase-A report.

Initial probe run:

- workflow: `ENA v0.3.7 Candidate.1 Open Branch Probes`
- run: `33052192384`
- result: `SUCCESS` as an observation workflow, not a release verdict

It demonstrated additional accepted shapes:

- integration history could claim `selection_state_at_commit=SUPPORTED` before supporting evaluation existed;
- integration history could disagree with the represented selection at commit time;
- a source packet claiming `SUPPORTED` could use structurally empty `source_experiments=[{}]` / `source_evaluations=[{}]` and still pass packet/import validation;
- source and receiver could share the same `candidate_id`.

The first two were classified as one **integration chronology / at-commit snapshot consistency** defect. The shallow source-history shape was classified as a **represented source-history structural consistency** defect. Candidate-ID collision was **not** automatically classified as a defect because no current contract establishes cross-environment global candidate-ID uniqueness.

This distinction prevents probe acceptance from being mechanically converted into new law.

### Repair round 2 — focused open-branch defects

The second exact-anchor transformation produced cargo commit:

`bc8be8bc02a2b2515cfa1b7eee2c4bd3c2a37f90` — `candidate1: repair focused open-branch defects`

Only three candidate tool files changed in this focused round.

The repair:

- validates integration `selection_state_at_commit` against represented evaluation history as of integration time, rather than against the mutable current state;
- applies the same at-commit reasoning to the parallel expression-state snapshot;
- preserves legitimate post-commit reselection, so later evidence may change current selection without rewriting the historical commit snapshot;
- validates represented source experiment/evaluation items against the already-existing record item schemas instead of accepting arbitrary empty objects;
- preserves the boundary that imported source evidence is represented source history, not receiver-local proof.

No new Constitution rule or Core semantic rewrite was introduced.

## Final successor revalidation

Final ordinary trigger head after the focused repair:

`b76bb9e7d0d2ee820d7dcc3a7f72f20fefe363e6`

Exact candidate.1 subtree at that head:

`25d068d158ee37e4e43481c345cce9281febddd1`

Current subtree observed at the same repository head remained:

`7dcbb3934883ffa6cc5292a662588cafc1533cff`

Therefore this repair sequence did not modify `releases/current/`.

### Final targeted regression

- workflow run: `33052764739`
- result: `SUCCESS`
- evolution-record v2 selftest: `24 / PASS`
- v2 helper selftest: `13 / PASS`
- sealed-Phase-A-derived targeted conditions: `16 / PASS`
- `attack_cardinality=OPEN`
- `fresh_independent_phase_a_repeated=NO`

Candidate.0 references remaining in candidate.1 identity census are predecessor/history references in baseline lineage, `LINEAGE.md`, release-discipline history, and `CHANGELOG.md`; they are not current candidate.1 self-identity leakage.

### Final open-branch re-probe

- workflow run: `33052764661`
- result: `SUCCESS`

Observed after repair:

- `integration_selection_at_commit_mismatch_accepted = false`
- `integration_supported_before_supporting_evaluation_accepted = false`
- `post_commit_reselection_control_accepted = true`
- `shallow_supported_source_packet_accepted = false`
- source-history structural errors are surfaced explicitly
- `source_receiver_candidate_id_collision_accepted = true`

The remaining candidate-ID collision branch is retained as a visible residual / Host-namespace question because current ENA contracts do not establish a universal cross-environment global-ID uniqueness law.

`VISIBLE_RESIDUAL != RELEASE_BLOCKER`

`NO_CURRENT_CONTRACT -> DO_NOT_INVENT_UNIVERSAL_RULE`

## Reconciled status

Candidate.1 has passed targeted repair evidence for all deterministic candidate-byte defects currently established by the sealed Phase-A + Phase-B expansion lineage.

This does **not** mean the possibility space is complete or that candidate.1 is released.

Current status:

`SUCCESSOR_REPAIR_RECONCILED / READY_FOR_EXACT_PREFREEZE_VALIDATION / NOT_FROZEN / NOT_CURRENT`

The attack space remains open. Unknown external truth, Host behavior, natural retrieval/salience, bilingual behavioral equivalence, and other field residuals remain outside what these deterministic repair gates prove.

## Next governed action

Run an exact candidate.1 pre-freeze validation bound to one exact source commit and one exact `releases/v0.3.7-candidate/` subtree. The gate must include inherited candidate checks plus the successor repair regressions and Current isolation.

Only if that exact pre-freeze gate passes may candidate.1 be frozen through an external record binding the exact source/subtree.

A same-falsifier targeted repair revalidation is sufficient to verify these specific corrections when labeled honestly; it is not a second fresh Phase A. Whether additional independent review is warranted after freeze is a separate reconciliation decision and must not be silently assumed either way.

Do not promote or modify `releases/current/` as part of this step.
