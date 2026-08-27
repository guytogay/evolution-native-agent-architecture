# ENA v0.3.7 candidate.1 freeze record

Date: 2026-08-27

## Status

`FROZEN_CANDIDATE.1 / EXACT_PREFREEZE_PASS / SUCCESSOR_REPAIR_RECONCILED / NOT_CURRENT / NOT_RELEASED / POST_FREEZE_INDEPENDENCE_DECISION_NEXT`

This record freezes the v0.3.7 successor candidate after the frozen candidate.0 received a fresh blind Phase-A review, Phase B classified four material shared blind spots, candidate.1 repaired those findings, focused open branches were probed and repaired where contract-backed, and one exact-source pre-freeze gate passed.

This freeze is an **external exact-tree binding**. The tested candidate cargo is not rewritten merely to say `frozen=true`.

Passing this gate is not fresh independent acceptance, does not close attack cardinality, and does not promote the candidate to Current.

## Frozen candidate.1 identity

Candidate identity:

`v0.3.7-candidate.1`

Source commit:

`ae6903464133cb5bcf3cd8909ecae1215fe0b9ba`

Effective candidate subtree:

`releases/v0.3.7-candidate/`

Git tree:

`c0458e0d7ea417b841cbf4c8bf6e64e4aff37319`

Current at the same source commit remains:

`releases/current/`

Git tree:

`7dcbb3934883ffa6cc5292a662588cafc1533cff`

No `releases/current/**` change is part of candidate.1.

## Predecessor occurrence truth

Frozen predecessor candidate.0 remains immutable:

- identity: `v0.3.7-candidate.0`
- frozen source: `d0e793593184740d9732902e948afd48ed96ae2f`
- frozen subtree: `cffbf76fe1448b020b637c78d1f7ae46e4c0115b`
- fresh blind Phase-A seal: `5ba3d241efa460fe170253860ad67045aa1d96a5`
- Phase-B verdict: `NEEDS_REVISION / CANDIDATE_1_REQUIRED`

candidate.0 was not mutated to absorb the repairs.

## candidate.1 repair lineage

Round 1 repair commit:

`583ac8133350bdf70a6a87fc8f0b070943f0aca1`

It repaired the four sealed fresh Phase-A findings:

1. import retains represented source Variation Space / Evolutionary Subject / Protected Subjects in migration provenance rather than laundering them into receiver-local applicability;
2. packet validation rejects tied latest expression timestamps consistently with record chronology;
3. `archive.selection_state_preserved` is bound to represented selection truth;
4. uninstantiated template `created_at` placeholders are not accepted as live record chronology.

Focused open-branch probing then exposed two additional contract-backed defects while preserving one non-contract residual:

- integration `selection_state_at_commit` / `expression_state_at_commit` needed historical at-commit consistency without blocking legitimate post-commit reselection/re-expression;
- represented source experiment/evaluation history could not remain structurally empty shells while claiming source history;
- source/receiver candidate-ID collision remained visible because no current ENA contract establishes cross-environment global candidate-ID uniqueness.

Round 2 focused repair commit:

`bc8be8bc02a2b2515cfa1b7eee2c4bd3c2a37f90`

Final successor reconciliation before exact pre-freeze validation:

`collaboration/reconciliation/2026-08-27-v037-candidate1-successor-repair-reconciliation.md`

## Evidence before freeze

### Fresh independent predecessor evidence

Fresh blind Phase A was performed against frozen candidate.0 and sealed at:

`5ba3d241efa460fe170253860ad67045aa1d96a5`

That review is independent predecessor evidence. It is **not** automatically relabeled as fresh independent review of candidate.1.

### Same-falsifier successor repair evidence

Final targeted successor run:

- workflow run `33052764739` — SUCCESS
- record selftest: 24 observed cases
- helper selftest: 13 observed cases
- targeted Phase-A-derived conditions: 16 observed pass conditions
- `attack_cardinality=OPEN`
- `fresh_independent_phase_a_repeated=NO`

Final focused open-branch run:

- workflow run `33052764661` — SUCCESS
- integration at-commit mismatch rejected;
- integration support before supporting evaluation rejected;
- legitimate post-commit reselection accepted;
- shallow represented source history rejected;
- source/receiver candidate-ID collision accepted and retained as a visible residual.

These runs demonstrate repair behavior but are not independent evidence.

### Exact pre-freeze gate

Workflow:

`ENA v0.3.7 Candidate.1 Exact Pre-Freeze Gate`

Run:

`33055811978`

Result:

`SUCCESS`

Exact run head/source:

`ae6903464133cb5bcf3cd8909ecae1215fe0b9ba`

Exact candidate subtree:

`c0458e0d7ea417b841cbf4c8bf6e64e4aff37319`

The gate passed all of its composed steps, including:

- exact source/candidate-tree binding and Current-tree isolation;
- candidate.1 structured pre-freeze identity;
- semantic-trunk byte parity and identity-only Core projection;
- operational routing, optional-reference policy, and deferred lineage;
- inherited composed-validator regression;
- v2 record/helper selftests and CLI roundtrip;
- bundled reference selftests;
- relocated legacy compatibility regressions;
- successor-aware replay of inherited author-side and anti-ablation behavioral checks;
- sealed Phase-A successor regressions;
- focused open-branch regressions;
- zh-CN projection/fixture checks;
- runtime self-containment and candidate.1 identity surfaces;
- candidate Python compilation, no bytecode/symlink cargo;
- exact candidate tree cleanliness after validation.

The gate explicitly retains:

- `attack_cardinality=OPEN`
- `fresh_independent_phase_a_repeated=NO`
- `candidate_id_collision_residual=VISIBLE_NO_CURRENT_CONTRACT`
- `independent_semantic_support_by_this_gate=NOT_ESTABLISHED`
- `external_truth=NOT_ESTABLISHED`
- `freeze_authority=NOT_ASSIGNED_BY_THIS_WORKFLOW`

This external record supplies the freeze authority after the exact gate passed.

## Visible residual

The source/receiver `candidate_id` collision remains accepted.

Current classification:

`VISIBLE_RESIDUAL / NO_CURRENT_GLOBAL_NAMESPACE_CONTRACT / NOT_AUTOMATIC_RELEASE_BLOCKER`

Rule:

`NO_CURRENT_CONTRACT -> DO_NOT_INVENT_UNIVERSAL_RULE`

This remains a visible Host/namespace research residual rather than an invented universal prohibition.

## Freeze rule

Tree `c0458e0d7ea417b841cbf4c8bf6e64e4aff37319` is now frozen occurrence truth for `v0.3.7-candidate.1`.

Any material correction to candidate cargo after this record requires a new successor identity, e.g. `v0.3.7-candidate.2`. Do not silently mutate this frozen tree and continue calling it candidate.1.

Validation tooling or research/control-plane records may evolve outside the frozen subtree, but they must not retroactively change what bytes were frozen.

## Required next decision

Perform an explicit **post-freeze independence decision** before release reconciliation.

The decision must not silently assume either of these extremes:

- `candidate.0 had fresh Phase A -> candidate.1 automatically has fresh independent acceptance`; or
- `every successor candidate mechanically requires endless fresh review regardless of semantic radius`.

Evaluate whether the material executable/validator repairs and the still-open possibility space warrant one fresh blind inspection of the exact frozen candidate.1 bytes. Record the rationale either way before any promotion decision.

Until that decision is reconciled:

- candidate.1 is `FROZEN / NOT_CURRENT / NOT_RELEASED`;
- Current remains `v0.3.6 / FIELD_VALIDATION`;
- PR/release authority is not assigned;
- attack cardinality remains open.
