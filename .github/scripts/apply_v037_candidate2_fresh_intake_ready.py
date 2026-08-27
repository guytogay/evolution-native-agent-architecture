#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def replace_once(path: str, old: str, new: str) -> None:
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{path}: expected exactly one anchor, got {count}: {old!r}")
    p.write_text(text.replace(old, new, 1), encoding="utf-8")

# ACTIVE-RESEARCH
p = "research/ACTIVE-RESEARCH.yaml"
replace_once(p,
'  state: "V0_3_7_CANDIDATE2_FROZEN / FRESH_BLIND_SEMANTIC_VIEW_PREPARATION_NEXT / NOT_CURRENT / NOT_RELEASED"',
'  state: "V0_3_7_CANDIDATE2_FROZEN / FRESH_A_S_INTAKE_READY / NOT_CURRENT / NOT_RELEASED"')
replace_once(p,
'  blind_semantic_view_preparation_next: true\n  fresh_candidate2_review_completed: false',
'''  blind_semantic_view_preparation_next: false
  blind_semantic_view_manifest: "collaboration/reconciliation/2026-08-28-v037-candidate2-blind-semantic-view.yaml"
  neutral_entry: "collaboration/reconciliation/2026-08-28-v037-candidate2-blind-semantic-entry.md"
  blind_view_audit_record: "collaboration/reconciliation/2026-08-28-v037-candidate2-blind-view-preparation.md"
  validation_branch: "validation/v037-c2-blind-semantic-primary"
  validation_view_head: "d020d82d442156b75c667ee9f987f2654d814561"
  fresh_intake_issue: 137
  fresh_a_s_intake_ready: true
  fresh_candidate2_review_completed: false''')
replace_once(p,
'  current_state: CANDIDATE2_FROZEN_FRESH_BLIND_SEMANTIC_VIEW_PREPARATION_NEXT',
'  current_state: CANDIDATE2_FROZEN_FRESH_A_S_INTAKE_READY')
replace_once(p,
'    - post-freeze independence decision authorizes one fresh blind successor review cycle based on measured search-space information gain\n  next_required_steps:',
'''    - post-freeze independence decision authorizes one fresh blind successor review cycle based on measured search-space information gain
    - candidate.2 blind semantic view prepared from exact frozen source; source-to-view audit observed 31 declared removals + 2 intake additions and 0 retained-byte modifications
    - candidate.2 information-role audit additionally withheld 08-RELEASE-DISCIPLINE.md after detecting predecessor-finding/repair-narrative self-priming
    - fresh independent intake Issue 137 created for validation/v037-c2-blind-semantic-primary
  next_required_steps:''')
replace_once(p,
'''    - "prepare a declared candidate.2 blind semantic view bound to the exact frozen source/blob identities"
    - "prepare a neutral fresh A-S -> A-P intake without author repair maps or project-manager context"
    - "have a genuinely fresh reviewer seal A-S before A-P opens withheld candidate-local history/oracles"''',
'''    - "have a genuinely fresh reviewer use Issue 137 / validation/v037-c2-blind-semantic-primary and seal A-S before opening withheld candidate-local history/oracles"
    - "only after the A-S seal, permit A-P against the exact frozen-source withheld package/oracle surfaces"''')
replace_once(p,
'  state: FROZEN_FRESH_BLIND_SEMANTIC_VIEW_PREPARATION_NEXT\n  frozen: true',
'''  state: FROZEN_FRESH_A_S_INTAKE_READY
  frozen: true''')
replace_once(p,
'  postfreeze_independence_decision: FRESH_BLIND_SUCCESSOR_REVIEW_WARRANTED_ONE_CYCLE\n  fresh_review_completed: false',
'''  postfreeze_independence_decision: FRESH_BLIND_SUCCESSOR_REVIEW_WARRANTED_ONE_CYCLE
  blind_view_manifest: "collaboration/reconciliation/2026-08-28-v037-candidate2-blind-semantic-view.yaml"
  neutral_entry: "collaboration/reconciliation/2026-08-28-v037-candidate2-blind-semantic-entry.md"
  blind_view_audit_record: "collaboration/reconciliation/2026-08-28-v037-candidate2-blind-view-preparation.md"
  validation_branch: "validation/v037-c2-blind-semantic-primary"
  validation_view_head: "d020d82d442156b75c667ee9f987f2654d814561"
  fresh_intake_issue: 137
  fresh_a_s_seal: NOT_YET_CREATED
  final_a_p_commit: NOT_YET_CREATED
  fresh_review_completed: false''')

# CURRENT-HANDOFF
p = "research/handoffs/CURRENT-HANDOFF.yaml"
replace_once(p, '  view_preparation_required: true', '  view_preparation_required: false')
replace_once(p,
'''  blind_view_manifest: NOT_YET_CREATED
  neutral_entry: NOT_YET_CREATED
  intake_issue: NOT_YET_CREATED
  validation_branch: NOT_YET_CREATED''',
'''  blind_view_manifest: collaboration/reconciliation/2026-08-28-v037-candidate2-blind-semantic-view.yaml
  neutral_entry: collaboration/reconciliation/2026-08-28-v037-candidate2-blind-semantic-entry.md
  blind_view_audit_record: collaboration/reconciliation/2026-08-28-v037-candidate2-blind-view-preparation.md
  intake_issue: 137
  validation_branch: validation/v037-c2-blind-semantic-primary
  validation_view_head: d020d82d442156b75c667ee9f987f2654d814561''')
replace_once(p,
'  candidate2_state: FROZEN_FRESH_BLIND_SEMANTIC_VIEW_PREPARATION_NEXT\n  immediate_next_action: PREPARE_CANDIDATE2_BLIND_SEMANTIC_VIEW_AND_FRESH_INTAKE',
'''  candidate2_state: FROZEN_FRESH_A_S_INTAKE_READY
  candidate2_blind_view_manifest: collaboration/reconciliation/2026-08-28-v037-candidate2-blind-semantic-view.yaml
  candidate2_neutral_entry: collaboration/reconciliation/2026-08-28-v037-candidate2-blind-semantic-entry.md
  candidate2_blind_view_audit: collaboration/reconciliation/2026-08-28-v037-candidate2-blind-view-preparation.md
  candidate2_validation_branch: validation/v037-c2-blind-semantic-primary
  candidate2_validation_view_head: d020d82d442156b75c667ee9f987f2654d814561
  candidate2_fresh_intake_issue: 137
  immediate_next_action: GET_GENUINELY_FRESH_REVIEWER_TO_RUN_CANDIDATE2_A_S''')
replace_once(p,
'  state: FROZEN_FRESH_BLIND_SEMANTIC_VIEW_PREPARATION_NEXT\n  frozen: true',
'''  state: FROZEN_FRESH_A_S_INTAKE_READY
  frozen: true''')
replace_once(p,
'  fresh_a_s_a_p_next: true\n  fresh_a_s_a_p_completed: false',
'''  fresh_a_s_a_p_next: true
  fresh_a_s_a_p_issue: 137
  fresh_a_s_a_p_branch: validation/v037-c2-blind-semantic-primary
  fresh_a_s_a_p_entry: collaboration/reconciliation/2026-08-28-v037-candidate2-blind-semantic-entry.md
  blind_view_manifest: collaboration/reconciliation/2026-08-28-v037-candidate2-blind-semantic-view.yaml
  blind_view_audit_record: collaboration/reconciliation/2026-08-28-v037-candidate2-blind-view-preparation.md
  validation_view_head: d020d82d442156b75c667ee9f987f2654d814561
  fresh_a_s_seal: NOT_YET_CREATED
  final_a_p_commit: NOT_YET_CREATED
  fresh_a_s_a_p_completed: false''')
replace_once(p,
'    - validation/v037-c1-blind-semantic-primary\n    - tmp/noop-check',
'''    - validation/v037-c1-blind-semantic-primary
    - validation/v037-c2-blind-semantic-primary
    - tmp/noop-check''')
replace_once(p,
'  candidate2_branch_role: FROZEN_SUCCESSOR_OCCURRENCE_TRUTH_NOT_CURRENT_NOT_RELEASED',
'''  candidate2_branch_role: FROZEN_SUCCESSOR_OCCURRENCE_TRUTH_NOT_CURRENT_NOT_RELEASED
  candidate2_validation_branch_role: ACTIVE_FRESH_A_S_INTAKE_VIEW_NOT_CANDIDATE_NOT_RELEASE_AUTHORITY''')

# PROGRESS
p = "research/plans/PROGRESS.yaml"
replace_once(p,
'status: V0_3_7_CANDIDATE2_FROZEN_FRESH_BLIND_SEMANTIC_VIEW_PREPARATION_NEXT',
'status: V0_3_7_CANDIDATE2_FROZEN_FRESH_A_S_INTAKE_READY')
replace_once(p,
'  state: FROZEN_FRESH_BLIND_SEMANTIC_VIEW_PREPARATION_NEXT\n  candidate_branch:',
'''  state: FROZEN_FRESH_A_S_INTAKE_READY
  candidate_branch:''')
replace_once(p,
'  attack_cardinality: OPEN\n\nphase_state:',
'''  blind_view_manifest: collaboration/reconciliation/2026-08-28-v037-candidate2-blind-semantic-view.yaml
  neutral_entry: collaboration/reconciliation/2026-08-28-v037-candidate2-blind-semantic-entry.md
  blind_view_audit_record: collaboration/reconciliation/2026-08-28-v037-candidate2-blind-view-preparation.md
  validation_branch: validation/v037-c2-blind-semantic-primary
  validation_view_head: d020d82d442156b75c667ee9f987f2654d814561
  fresh_intake_issue: 137
  fresh_a_s_seal: NOT_YET_CREATED
  final_a_p_commit: NOT_YET_CREATED
  attack_cardinality: OPEN

phase_state:''')
replace_once(p,
'    state: CANDIDATE2_FROZEN_FRESH_BLIND_VIEW_PREPARATION_NEXT',
'    state: CANDIDATE2_FROZEN_FRESH_A_S_INTAKE_READY')
replace_once(p,
'    candidate2_fresh_review_completed: false\n    current_project_manager_is_fresh_candidate2_reviewer: false',
'''    candidate2_fresh_review_completed: false
    candidate2_blind_view_manifest: collaboration/reconciliation/2026-08-28-v037-candidate2-blind-semantic-view.yaml
    candidate2_blind_view_audit: collaboration/reconciliation/2026-08-28-v037-candidate2-blind-view-preparation.md
    candidate2_fresh_intake_issue: 137
    candidate2_validation_branch: validation/v037-c2-blind-semantic-primary
    candidate2_validation_view_head: d020d82d442156b75c667ee9f987f2654d814561
    candidate2_fresh_a_s_seal: NOT_YET_CREATED
    candidate2_final_a_p_commit: NOT_YET_CREATED
    current_project_manager_is_fresh_candidate2_reviewer: false''')
replace_once(p,
'''immediate_next_action:
  id: PREPARE_CANDIDATE2_BLIND_SEMANTIC_VIEW_AND_FRESH_INTAKE
  target: FROZEN_V0_3_7_CANDIDATE2
  objective: >-
    Construct a declared blind semantic view of the exact frozen candidate.2 tree,
    withholding candidate-local history/oracle roles before A-S while preserving
    retained executable semantic bytes unchanged; then prepare one genuinely fresh
    A-S -> A-P intake and stop the fresh reviewer before Phase B.''',
'''immediate_next_action:
  id: GET_GENUINELY_FRESH_REVIEWER_TO_RUN_CANDIDATE2_A_S
  target: ISSUE_137_VALIDATION_V037_C2_BLIND_SEMANTIC_PRIMARY
  objective: >-
    Have a genuinely fresh reviewer inspect the prepared candidate.2 blind semantic view,
    persist/seal A-S before opening withheld candidate-local history/oracles, then perform
    A-P and stop before project-manager Phase B. The current project-manager session must
    not claim fresh A-S.''')
replace_once(p,
'''candidate2_postfreeze_path:
  - prepare exact frozen-source blind semantic view with declared information-role exclusions
  - verify every retained candidate byte equals frozen source and view exclusions are not release ablation
  - prepare neutral fresh intake without predecessor findings, repair narrative, or author oracle
  - require A-S artifact persistence/seal before withheld candidate-local history/oracles open''',
'''candidate2_postfreeze_path:
  - blind semantic view prepared and audited: 31 declared removals + 2 intake additions, 0 retained candidate-byte modifications
  - neutral fresh intake created as Issue 137 on validation/v037-c2-blind-semantic-primary
  - require A-S artifact persistence/seal before withheld candidate-local history/oracles open''')

# RESEARCH-START-HERE
p = "research/RESEARCH-START-HERE.md"
replace_once(p,
'## Immediate next action\n\n`PREPARE_CANDIDATE2_BLIND_SEMANTIC_VIEW_AND_FRESH_INTAKE`',
'''## Immediate next action

`GET_GENUINELY_FRESH_REVIEWER_TO_RUN_CANDIDATE2_A_S`''')
replace_once(p,
'After A-P, the fresh reviewer stopped before Phase B as required. Project-manager Phase B is now complete and candidate.2 is the active repair workspace.',
'After A-P, the fresh candidate.1 reviewer stopped before Phase B as required. Project-manager Phase B is complete and candidate.2 has since been repaired, exactly validated, externally frozen, and prepared for one fresh candidate.2 A-S/A-P cycle.')
replace_once(p,
'''## Candidate.2 successor repair

Candidate.2 branch: `candidate/v0.3.7-candidate.2`, created from exact frozen candidate.1 source `ae6903464133cb5bcf3cd8909ecae1215fe0b9ba`.

Repair only the sealed failure shapes and adjacent consistency needed to close them while retaining legitimate lightweight paths. Targeted repair/reprobe is author-side evidence, not another fresh A-S. Current remains v0.3.6.''',
'''## Candidate.2 frozen fresh-review intake

Candidate.2 is frozen occurrence truth at source `bda470e0a6b170cec61225a905957a501454a2fe` / subtree `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`.

Fresh intake:

- Issue `#137 — Fresh independent A-S/A-P — v0.3.7 candidate.2`
- validation branch `validation/v037-c2-blind-semantic-primary`
- neutral entry `collaboration/reconciliation/2026-08-28-v037-candidate2-blind-semantic-entry.md`
- blind view `collaboration/reconciliation/2026-08-28-v037-candidate2-blind-semantic-view.yaml`
- view audit `collaboration/reconciliation/2026-08-28-v037-candidate2-blind-view-preparation.md`

The prepared view is a projection, not a new candidate. Its source-to-view audit found 31 declared A-S removals plus the two intake files and **zero retained candidate-byte modifications**. The current project-manager session is not eligible to act as the fresh candidate.2 A-S reviewer. Current remains v0.3.6.''')
replace_once(p,
'- candidate.2 = active focused successor-repair workspace;',
'- candidate.2 = frozen at `bda470e0...` / `d5fefc8c...`, with fresh A-S intake Issue #137 ready on `validation/v037-c2-blind-semantic-primary`;')

print("CANDIDATE2_FRESH_INTAKE_CONTROL_PLANE_TRANSFORM=PASS")
