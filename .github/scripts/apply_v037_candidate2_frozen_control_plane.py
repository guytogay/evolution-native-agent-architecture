#!/usr/bin/env python3
from pathlib import Path

ROOT = Path('.')


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding='utf-8')


def write(rel: str, text: str) -> None:
    (ROOT / rel).write_text(text, encoding='utf-8')


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected exactly one anchor, observed {count}')
    return text.replace(old, new, 1)


def replace_block(text: str, start: str, end: str, new_block: str, label: str) -> str:
    a = text.find(start)
    if a < 0:
        raise SystemExit(f'{label}: start marker missing')
    b = text.find(end, a + len(start))
    if b < 0:
        raise SystemExit(f'{label}: end marker missing')
    return text[:a] + new_block.rstrip() + '\n\n' + text[b:]


# ---------------------------------------------------------------------------
# ACTIVE-RESEARCH: authoritative active phase pointer.
# ---------------------------------------------------------------------------
rel = 'research/ACTIVE-RESEARCH.yaml'
t = read(rel)
t = replace_once(t, 'updated_at: "2026-08-27"', 'updated_at: "2026-08-28"', 'active updated_at')
t = replace_once(
    t,
    '  state: "V0_3_7_CANDIDATE1_NEEDS_REVISION / CANDIDATE2_FOCUSED_REPAIR_NEXT / NOT_CURRENT / NOT_RELEASED"',
    '  state: "V0_3_7_CANDIDATE2_FROZEN / FRESH_BLIND_SEMANTIC_VIEW_PREPARATION_NEXT / NOT_CURRENT / NOT_RELEASED"',
    'active state',
)
t = replace_block(
    t,
    'latest_transition:\n',
    'candidate_validation_transition:\n',
    '''latest_transition:
  event: "V0_3_7_CANDIDATE2_EXACT_PREFREEZE_PASS_EXTERNALLY_FROZEN_FRESH_BLIND_REVIEW_WARRANTED"
  current_changed_by_transition: false
  next_version: "v0.3.7"
  active_candidate_identity: "v0.3.7-candidate.2"
  active_candidate_branch: "candidate/v0.3.7-candidate.2"
  candidate_state: FROZEN_NOT_CURRENT_NOT_RELEASED
  final_candidate_cargo_commit: "aba6f12cabc84146c92809bd7d8293a3c907dc55"
  exact_prefreeze_run: 33095987843
  frozen_source: "bda470e0a6b170cec61225a905957a501454a2fe"
  frozen_subtree: "d5fefc8c786d7e40b3e9a59211ee7045bccee5bf"
  current_subtree_same_source: "7dcbb3934883ffa6cc5292a662588cafc1533cff"
  repair_reconciliation_record: "collaboration/reconciliation/2026-08-28-v037-candidate2-successor-repair-reconciliation.md"
  freeze_record: "collaboration/reconciliation/2026-08-28-v037-candidate2-freeze.md"
  postfreeze_independence_decision: FRESH_BLIND_SUCCESSOR_REVIEW_WARRANTED_ONE_CYCLE
  independence_decision_record: "collaboration/reconciliation/2026-08-28-v037-candidate2-post-freeze-independence-decision.md"
  blind_semantic_view_preparation_next: true
  fresh_candidate2_review_completed: false
  fresh_candidate2_review_by_current_project_manager_allowed: false
  attack_cardinality: OPEN
''',
    'active latest transition',
)
t = replace_block(
    t,
    'candidate_validation_transition:\n',
    'frozen_candidate0:\n',
    '''candidate_validation_transition:
  current_state: CANDIDATE2_FROZEN_FRESH_BLIND_SEMANTIC_VIEW_PREPARATION_NEXT
  completed:
    - candidate.0 and candidate.1 remain immutable frozen occurrence truth
    - candidate.1 fresh A-S/A-P plus Phase B required candidate.2
    - candidate.2 focused repair run 33090294820 PASS; cargo commit 613c1e8be898865ce674199118618c0f9389da97
    - nearby open-branch probe 33090585653 exposed two homologous decision-changing gaps
    - candidate.2 round-2 repair run 33091573678 PASS; cargo commit 34458c2ba0b94b82d182afe2606efe48e741bcda
    - committed readback re-probe 33091652046 PASS
    - status-only prefreeze transition run 33095122958 PASS; final candidate cargo commit aba6f12cabc84146c92809bd7d8293a3c907dc55
    - exact candidate.2 pre-freeze run 33095987843 PASS on source bda470e0a6b170cec61225a905957a501454a2fe / subtree d5fefc8c786d7e40b3e9a59211ee7045bccee5bf
    - external freeze record binds the exact tested tree without rewriting candidate cargo
    - post-freeze independence decision authorizes one fresh blind successor review cycle based on measured search-space information gain
  next_required_steps:
    - "prepare a declared candidate.2 blind semantic view bound to the exact frozen source/blob identities"
    - "prepare a neutral fresh A-S -> A-P intake without author repair maps or project-manager context"
    - "have a genuinely fresh reviewer seal A-S before A-P opens withheld candidate-local history/oracles"
    - "stop fresh reviewer before Phase B; project manager reconciles only after independent artifacts persist"
    - "keep attack cardinality open and Current v0.3.6 unchanged"
''',
    'active validation transition',
)
t = replace_block(
    t,
    'successor_candidate2:\n',
    'handoff:\n',
    '''successor_candidate2:
  identity: "v0.3.7-candidate.2"
  branch: "candidate/v0.3.7-candidate.2"
  branch_head_is_freeze_identity: false
  state: FROZEN_FRESH_BLIND_SEMANTIC_VIEW_PREPARATION_NEXT
  frozen: true
  current: false
  frozen_source: "bda470e0a6b170cec61225a905957a501454a2fe"
  frozen_subtree: "d5fefc8c786d7e40b3e9a59211ee7045bccee5bf"
  current_subtree_at_freeze: "7dcbb3934883ffa6cc5292a662588cafc1533cff"
  exact_prefreeze_run: 33095987843
  final_candidate_cargo_commit: "aba6f12cabc84146c92809bd7d8293a3c907dc55"
  repair_reconciliation: "collaboration/reconciliation/2026-08-28-v037-candidate2-successor-repair-reconciliation.md"
  freeze_record: "collaboration/reconciliation/2026-08-28-v037-candidate2-freeze.md"
  independence_decision_record: "collaboration/reconciliation/2026-08-28-v037-candidate2-post-freeze-independence-decision.md"
  postfreeze_independence_decision: FRESH_BLIND_SUCCESSOR_REVIEW_WARRANTED_ONE_CYCLE
  fresh_review_completed: false
  mutable_in_place: false
  material_change_requires_successor: "v0.3.7-candidate.3"
  attack_cardinality: OPEN
''',
    'active candidate2 block',
)
write(rel, t)


# ---------------------------------------------------------------------------
# PROGRESS: phase and immediate next action.
# ---------------------------------------------------------------------------
rel = 'research/plans/PROGRESS.yaml'
t = read(rel)
t = replace_once(t, 'as_of: "2026-08-27"', 'as_of: "2026-08-28"', 'progress date')
t = replace_once(
    t,
    'status: V0_3_7_CANDIDATE1_NEEDS_REVISION_CANDIDATE2_FOCUSED_REPAIR_NEXT',
    'status: V0_3_7_CANDIDATE2_FROZEN_FRESH_BLIND_SEMANTIC_VIEW_PREPARATION_NEXT',
    'progress status',
)
t = replace_block(
    t,
    'successor_candidate2:\n',
    'phase_state:\n',
    '''successor_candidate2:
  identity: v0.3.7-candidate.2
  state: FROZEN_FRESH_BLIND_SEMANTIC_VIEW_PREPARATION_NEXT
  candidate_branch: candidate/v0.3.7-candidate.2
  branch_head_is_frozen_identity: false
  created_from_candidate1_frozen_source: ae6903464133cb5bcf3cd8909ecae1215fe0b9ba
  frozen: true
  current: false
  frozen_source_commit: bda470e0a6b170cec61225a905957a501454a2fe
  frozen_candidate_subtree: d5fefc8c786d7e40b3e9a59211ee7045bccee5bf
  current_subtree_same_source: 7dcbb3934883ffa6cc5292a662588cafc1533cff
  final_candidate_cargo_commit: aba6f12cabc84146c92809bd7d8293a3c907dc55
  focused_repair_run: 33090294820
  nearby_open_branch_probe_run: 33090585653
  round2_repair_run: 33091573678
  committed_reprobe_run: 33091652046
  prefreeze_status_transition_run: 33095122958
  exact_prefreeze_run: 33095987843
  exact_prefreeze_validation: PASS
  repair_reconciliation_record: collaboration/reconciliation/2026-08-28-v037-candidate2-successor-repair-reconciliation.md
  freeze_record: collaboration/reconciliation/2026-08-28-v037-candidate2-freeze.md
  independence_decision_record: collaboration/reconciliation/2026-08-28-v037-candidate2-post-freeze-independence-decision.md
  postfreeze_independence_decision: FRESH_BLIND_SUCCESSOR_REVIEW_WARRANTED_ONE_CYCLE
  mutable_in_place: false
  material_change_requires_successor: v0.3.7-candidate.3
  attack_cardinality: OPEN
''',
    'progress candidate2 block',
)
t = replace_block(
    t,
    '  candidate_build:\n',
    '  author_validation:\n',
    '''  candidate_build:
    state: CANDIDATE2_FROZEN
    current_candidate_identity: v0.3.7-candidate.2
    predecessor_frozen_identity: v0.3.7-candidate.1
    mutable_in_place: false
    exact_prefreeze_validation: PASS
    exact_prefreeze_run: 33095987843
    frozen_source: bda470e0a6b170cec61225a905957a501454a2fe
    frozen_subtree: d5fefc8c786d7e40b3e9a59211ee7045bccee5bf
''',
    'progress candidate build',
)
t = replace_block(
    t,
    '  author_validation:\n',
    '  validation_method_reconciliation:\n',
    '''  author_validation:
    state: CANDIDATE2_EXACT_PREFREEZE_PASS_WITH_SUCCESSOR_AND_INHERITED_REPLAY
    candidate2_exact_prefreeze_run: 33095987843
    candidate2_focused_repair_run: 33090294820
    candidate2_round2_repair_run: 33091573678
    candidate2_committed_reprobe_run: 33091652046
    author_evidence_is_independent_evidence: false
    attack_cardinality: OPEN
''',
    'progress author validation',
)
t = replace_block(
    t,
    '  independent_falsification:\n',
    '  handoff_framework:\n',
    '''  independent_falsification:
    state: CANDIDATE2_FROZEN_FRESH_BLIND_VIEW_PREPARATION_NEXT
    candidate1_a_s_seal: 2e6b46aeedc1945a03aac93620ad36aa1ccbd70f
    candidate1_a_p_commit: b970148fe9596ea9cad0a2817a3b399a1d2b75f5
    candidate1_phase_b_verdict: NEEDS_REVISION
    candidate2_exact_prefreeze_run: 33095987843
    candidate2_frozen_source: bda470e0a6b170cec61225a905957a501454a2fe
    candidate2_frozen_subtree: d5fefc8c786d7e40b3e9a59211ee7045bccee5bf
    candidate2_fresh_review_decision: FRESH_BLIND_SUCCESSOR_REVIEW_WARRANTED_ONE_CYCLE
    candidate2_fresh_review_completed: false
    current_project_manager_is_fresh_candidate2_reviewer: false
    sequence_required: A-S_THEN_A-P_THEN_STOP_BEFORE_PHASE_B
    attack_cardinality: OPEN
''',
    'progress independent validation',
)
t = replace_block(
    t,
    'immediate_next_action:\n',
    'candidate2_repair_path:\n',
    '''immediate_next_action:
  id: PREPARE_CANDIDATE2_BLIND_SEMANTIC_VIEW_AND_FRESH_INTAKE
  target: FROZEN_V0_3_7_CANDIDATE2
  objective: >-
    Construct a declared blind semantic view of the exact frozen candidate.2 tree,
    withholding candidate-local history/oracle roles before A-S while preserving
    retained executable semantic bytes unchanged; then prepare one genuinely fresh
    A-S -> A-P intake and stop the fresh reviewer before Phase B.
  frozen_source: bda470e0a6b170cec61225a905957a501454a2fe
  frozen_subtree: d5fefc8c786d7e40b3e9a59211ee7045bccee5bf
  exact_prefreeze_run: 33095987843
  current_project_manager_may_claim_fresh_a_s: false
  current_must_remain: v0.3.6
  do_not_promote: true
''',
    'progress immediate next',
)
t = replace_block(
    t,
    'candidate2_repair_path:\n',
    'candidate1_rule:\n',
    '''candidate2_postfreeze_path:
  - prepare exact frozen-source blind semantic view with declared information-role exclusions
  - verify every retained candidate byte equals frozen source and view exclusions are not release ablation
  - prepare neutral fresh intake without predecessor findings, repair narrative, or author oracle
  - require A-S artifact persistence/seal before withheld candidate-local history/oracles open
  - permit A-P only after A-S seal and stop independent reviewer before Phase B
  - keep attack cardinality open and preserve Current v0.3.6
''',
    'progress candidate2 path',
)
if '  - EDIT_FROZEN_CANDIDATE2_IN_PLACE\n' not in t:
    t = replace_once(t, '  - EDIT_FROZEN_CANDIDATE1_IN_PLACE\n', '  - EDIT_FROZEN_CANDIDATE1_IN_PLACE\n  - EDIT_FROZEN_CANDIDATE2_IN_PLACE\n', 'progress frozen candidate2 forbid')
if '  - PRIME_CANDIDATE2_FRESH_VALIDATOR_WITH_AUTHOR_REPAIR_OR_ATTACK_CONTEXT\n' not in t:
    t = replace_once(t, '  - PRIME_CANDIDATE1_FRESH_VALIDATOR_WITH_AUTHOR_REPAIR_OR_ATTACK_CONTEXT\n', '  - PRIME_CANDIDATE1_FRESH_VALIDATOR_WITH_AUTHOR_REPAIR_OR_ATTACK_CONTEXT\n  - PRIME_CANDIDATE2_FRESH_VALIDATOR_WITH_AUTHOR_REPAIR_OR_ATTACK_CONTEXT\n', 'progress candidate2 priming forbid')
write(rel, t)


# ---------------------------------------------------------------------------
# RESEARCH-START-HERE: hot bootstrap current posture.
# ---------------------------------------------------------------------------
rel = 'research/RESEARCH-START-HERE.md'
t = read(rel)
t = replace_block(
    t,
    '## Current project posture\n',
    '## Core research direction\n',
    '''## Current project posture

Current remains:

```text
v0.3.6 / CURRENT / FIELD_VALIDATION
```

Next release line: `v0.3.7`.

Frozen candidate lineage:

```text
candidate.0 = d0e793593184740d9732902e948afd48ed96ae2f / cffbf76fe1448b020b637c78d1f7ae46e4c0115b / NEEDS_REVISION
candidate.1 = ae6903464133cb5bcf3cd8909ecae1215fe0b9ba / c0458e0d7ea417b841cbf4c8bf6e64e4aff37319 / NEEDS_REVISION
candidate.2 = bda470e0a6b170cec61225a905957a501454a2fe / d5fefc8c786d7e40b3e9a59211ee7045bccee5bf / FROZEN_NOT_CURRENT_NOT_RELEASED
```

Candidate.2 exact pre-freeze run `33095987843` passed. External freeze authority is recorded at:

`collaboration/reconciliation/2026-08-28-v037-candidate2-freeze.md`

Repair/exact reconciliation:

`collaboration/reconciliation/2026-08-28-v037-candidate2-successor-repair-reconciliation.md`

Post-freeze independence decision:

`collaboration/reconciliation/2026-08-28-v037-candidate2-post-freeze-independence-decision.md`

Decision:

`FRESH_BLIND_SUCCESSOR_REVIEW_WARRANTED / ONE_FINAL_SEARCH_SPACE_INDEPENDENCE_CYCLE`

This is not a ritual completeness claim. It is justified because candidate.1 fresh review found author-missed defects and candidate.2's author-side nearby probe then found additional homologous decision-changing gaps after the known repairs.

The current project-manager session is **not eligible** to perform fresh candidate.2 A-S because it has material exposure to predecessor findings, candidate.2 repairs, probes, and exact regression expectations.

## Immediate next action

`PREPARE_CANDIDATE2_BLIND_SEMANTIC_VIEW_AND_FRESH_INTAKE`

Use the repaired blind semantic view method from:

`research/methodology/INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md`

Required sequence:

```text
EXACT FROZEN CANDIDATE.2
-> DECLARED BLIND SEMANTIC VIEW
-> FRESH A-S
-> PERSIST / SEAL A-S
-> A-P OPENS WITHHELD CANDIDATE-LOCAL HISTORY / ORACLES
-> PERSIST A-P
-> STOP FRESH REVIEWER
-> PROJECT-MANAGER PHASE B
```

Before A-S seal, do not send the fresh reviewer through the project-manager handoff, predecessor findings, candidate.2 repair narratives, author attack maps, expected fixtures, or candidate-local history/oracle surfaces declared withheld by the new view manifest.

Candidate.2 is frozen. Any material candidate-byte correction after this point requires candidate.3; do not edit candidate.2 in place.

```text
FROZEN != INDEPENDENTLY_RECONCILED != RELEASED != CURRENT
ATTACK_CARDINALITY = OPEN
```
''',
    'start-here posture',
)
# refresh final inheritance bullets from stale candidate.2-repair wording
old = '- candidate.2 = active focused successor-repair workspace;'
if old in t:
    t = t.replace(old, '- candidate.2 = frozen exact successor at `bda470e0...` / `d5fefc8c...`, fresh blind semantic view preparation next;', 1)
write(rel, t)


# ---------------------------------------------------------------------------
# CURRENT-HANDOFF: current project-manager succession pointer.
# ---------------------------------------------------------------------------
rel = 'research/handoffs/CURRENT-HANDOFF.yaml'
t = read(rel)
t = replace_once(t, 'schema_version: "2.8"', 'schema_version: "2.9"', 'handoff schema')
t = replace_once(t, 'updated_at: "2026-08-27"', 'updated_at: "2026-08-28"', 'handoff date')
t = replace_block(
    t,
    'current_handoff_record:\n',
    'current_project_authorities:\n',
    '''current_handoff_record:
  id: "2026-08-28-v037-candidate2-frozen-blind-view-next"
  state: HANDOFF_READY_FOR_SESSION_SUCCESSION
  record_root: "research/handoffs/records/2026-08-28-v037-candidate2-frozen-blind-view-next/"
  start_here: "research/handoffs/records/2026-08-28-v037-candidate2-frozen-blind-view-next/HANDOFF-START-HERE.md"
  manifest: "research/handoffs/records/2026-08-28-v037-candidate2-frozen-blind-view-next/HANDOFF-MANIFEST.yaml"
  project_state: "research/handoffs/records/2026-08-28-v037-candidate2-frozen-blind-view-next/PROJECT-STATE.md"
  recent_three_rounds: "research/handoffs/records/2026-08-28-v037-candidate2-frozen-blind-view-next/RECENT-THREE-ROUNDS.md"
  file_catalog: "research/handoffs/records/2026-08-28-v037-candidate2-frozen-blind-view-next/FILE-CATALOG.md"
  post_merge_readback: "research/handoffs/records/2026-08-28-v037-candidate2-frozen-blind-view-next/HANDOFF-READBACK.md"
''',
    'handoff current record',
)
t = replace_block(
    t,
    'fresh_independent_validation_boundary:\n',
    'completion_evidence:\n',
    '''fresh_independent_validation_boundary:
  active_target_identity: v0.3.7-candidate.2
  active_target_source: bda470e0a6b170cec61225a905957a501454a2fe
  active_target_subtree: d5fefc8c786d7e40b3e9a59211ee7045bccee5bf
  active_target_frozen: true
  postfreeze_decision: FRESH_BLIND_SUCCESSOR_REVIEW_WARRANTED_ONE_CYCLE
  decision_record: collaboration/reconciliation/2026-08-28-v037-candidate2-post-freeze-independence-decision.md
  view_preparation_required: true
  blind_view_manifest: NOT_YET_CREATED
  neutral_entry: NOT_YET_CREATED
  intake_issue: NOT_YET_CREATED
  validation_branch: NOT_YET_CREATED
  fresh_a_s_seal: NOT_YET_CREATED
  final_a_p_commit: NOT_YET_CREATED
  sequence: A-S_THEN_A-P_THEN_STOP_BEFORE_PHASE_B
  project_manager_takeover_context_is_validator_a_s_context: false
  current_project_manager_can_claim_fresh_a_s: false
  validator_must_not_read_full_project_handoff_before_a_s: true
  validator_must_not_receive_author_attack_map_before_a_s: true
  validator_must_not_open_withheld_candidate_local_history_or_oracles_before_a_s_seal: true
  a_s_findings_must_be_persisted_before_a_p: true
  independent_artifacts_must_be_persisted_before_phase_b: true
  predecessor_candidate1_a_s_seal: 2e6b46aeedc1945a03aac93620ad36aa1ccbd70f
  predecessor_candidate1_a_p_commit: b970148fe9596ea9cad0a2817a3b399a1d2b75f5
  prior_invalidated_self_primed_issue: 128
  information_boundary_method: research/methodology/INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md
''',
    'handoff fresh boundary',
)
t = replace_block(
    t,
    'completion_evidence:\n',
    'candidate1_successor_state:\n',
    '''completion_evidence:
  current_reverified: "v0.3.6 / CURRENT / FIELD_VALIDATION"
  current_subtree: 7dcbb3934883ffa6cc5292a662588cafc1533cff
  candidate0_frozen_source: d0e793593184740d9732902e948afd48ed96ae2f
  candidate0_frozen_subtree: cffbf76fe1448b020b637c78d1f7ae46e4c0115b
  candidate1_frozen_source: ae6903464133cb5bcf3cd8909ecae1215fe0b9ba
  candidate1_frozen_subtree: c0458e0d7ea417b841cbf4c8bf6e64e4aff37319
  candidate1_a_s_seal: 2e6b46aeedc1945a03aac93620ad36aa1ccbd70f
  candidate1_a_p_commit: b970148fe9596ea9cad0a2817a3b399a1d2b75f5
  candidate1_phase_b_verdict: NEEDS_REVISION
  candidate2_branch: candidate/v0.3.7-candidate.2
  candidate2_frozen_source: bda470e0a6b170cec61225a905957a501454a2fe
  candidate2_frozen_subtree: d5fefc8c786d7e40b3e9a59211ee7045bccee5bf
  candidate2_final_cargo_commit: aba6f12cabc84146c92809bd7d8293a3c907dc55
  candidate2_focused_repair_run: 33090294820
  candidate2_open_branch_probe_run: 33090585653
  candidate2_round2_repair_run: 33091573678
  candidate2_committed_reprobe_run: 33091652046
  candidate2_prefreeze_status_transition_run: 33095122958
  candidate2_exact_prefreeze_run: 33095987843
  candidate2_exact_prefreeze_result: PASS
  candidate2_reconciliation_record: collaboration/reconciliation/2026-08-28-v037-candidate2-successor-repair-reconciliation.md
  candidate2_freeze_record: collaboration/reconciliation/2026-08-28-v037-candidate2-freeze.md
  candidate2_independence_decision_record: collaboration/reconciliation/2026-08-28-v037-candidate2-post-freeze-independence-decision.md
  candidate2_state: FROZEN_FRESH_BLIND_SEMANTIC_VIEW_PREPARATION_NEXT
  immediate_next_action: PREPARE_CANDIDATE2_BLIND_SEMANTIC_VIEW_AND_FRESH_INTAKE
  current_handoff_record_refresh: COMPLETE
''',
    'handoff completion evidence',
)
t = replace_block(
    t,
    'candidate2_successor_state:\n',
    'branch_hygiene:\n',
    '''candidate2_successor_state:
  identity: v0.3.7-candidate.2
  branch: candidate/v0.3.7-candidate.2
  predecessor_identity: v0.3.7-candidate.1
  state: FROZEN_FRESH_BLIND_SEMANTIC_VIEW_PREPARATION_NEXT
  frozen: true
  current: false
  frozen_source: bda470e0a6b170cec61225a905957a501454a2fe
  frozen_subtree: d5fefc8c786d7e40b3e9a59211ee7045bccee5bf
  current_subtree_at_freeze: 7dcbb3934883ffa6cc5292a662588cafc1533cff
  exact_prefreeze_validation: PASS
  exact_prefreeze_run: 33095987843
  final_candidate_cargo_commit: aba6f12cabc84146c92809bd7d8293a3c907dc55
  repair_reconciliation: collaboration/reconciliation/2026-08-28-v037-candidate2-successor-repair-reconciliation.md
  freeze_record: collaboration/reconciliation/2026-08-28-v037-candidate2-freeze.md
  independence_decision_record: collaboration/reconciliation/2026-08-28-v037-candidate2-post-freeze-independence-decision.md
  fresh_a_s_a_p_next: true
  fresh_a_s_a_p_completed: false
  targeted_revalidation_is_fresh_a_s: false
  material_change_requires_successor: v0.3.7-candidate.3
  attack_cardinality: OPEN
  remaining_visible_residuals:
    - candidate-id cross-environment namespace uniqueness is not universalized without a governing contract
''',
    'handoff candidate2 state',
)
t = replace_once(
    t,
    '  candidate2_branch_role: ACTIVE_SUCCESSOR_REPAIR_WORKSPACE_NOT_CURRENT',
    '  candidate2_branch_role: FROZEN_SUCCESSOR_OCCURRENCE_TRUTH_NOT_CURRENT_NOT_RELEASED',
    'handoff candidate2 branch role',
)
write(rel, t)

print('CANDIDATE2_FROZEN_CONTROL_PLANE_TRANSFORM_PASS')
