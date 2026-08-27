#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected one anchor, found {count}")
    return text.replace(old, new, 1)


def sub_once(text: str, pattern: str, repl: str, label: str) -> str:
    out, count = re.subn(pattern, repl, text, count=1, flags=re.S)
    if count != 1:
        raise SystemExit(f"{label}: expected one regex anchor, found {count}")
    return out


def update_active() -> None:
    p = ROOT / "research/ACTIVE-RESEARCH.yaml"
    t = p.read_text(encoding="utf-8")
    t = replace_once(t,
        '  state: "V0_3_7_CANDIDATE1_FROZEN / FRESH_BLIND_PHASE_A_NEXT / NOT_CURRENT / NOT_RELEASED"',
        '  state: "V0_3_7_CANDIDATE1_FROZEN / BLIND_SEMANTIC_VIEW_READY / FRESH_A_S_A_P_NEXT / NOT_CURRENT / NOT_RELEASED"',
        "active state")
    t = replace_once(t, '  candidate_state: FROZEN_FRESH_BLIND_PHASE_A_NEXT',
                     '  candidate_state: FROZEN_FRESH_A_S_A_P_NEXT', "latest candidate state")
    t = replace_once(t,
'''  fresh_phase_a_issue: 128
  fresh_phase_a_branch: "validation/v037-c1-blind-phase-a-primary"
  fresh_phase_a_entry: "collaboration/reconciliation/2026-08-27-v037-candidate1-blind-phase-a-entry.md"
''',
'''  invalidated_phase_a_issue: 128
  invalidated_phase_a_branch: "validation/v037-c1-blind-phase-a-primary"
  invalidated_phase_a_result: CANDIDATE_SELF_PRIMING_NO_SEAL
  fresh_a_s_a_p_issue: 131
  fresh_a_s_a_p_branch: "validation/v037-c1-blind-semantic-primary"
  fresh_a_s_a_p_entry: "collaboration/reconciliation/2026-08-27-v037-candidate1-blind-semantic-entry.md"
  blind_view_manifest: "collaboration/reconciliation/2026-08-27-v037-candidate1-blind-semantic-view.yaml"
  blind_view_repair_record: "collaboration/reconciliation/2026-08-27-v037-candidate1-blind-view-repair.md"
  self_priming_incident: "research/methodology/incidents/2026-08-27-CANDIDATE-SELF-PRIMING-INCIDENT.md"
''', "latest intake")
    t = replace_once(t, '  current_state: CANDIDATE1_FROZEN_FRESH_BLIND_PHASE_A_NEXT',
                     '  current_state: CANDIDATE1_FROZEN_BLIND_SEMANTIC_VIEW_READY_FRESH_A_S_A_P_NEXT',
                     "validation current state")
    t = replace_once(t,
        '    - blind validation branch and Issue 128 prepared without author attack-map priming\n',
        '    - Issue 128 invalidated after fresh reviewer detected candidate-local self-priming; no Phase-A seal exists\n'
        '    - blind semantic validation view audited as declared removals only with retained candidate bytes unchanged\n'
        '    - Issue 131 prepared for fresh A-S then A-P independent validation\n',
        "completed intake history")
    t = sub_once(t,
        r'  next_required_steps:\n(?:    - .*\n)+\nfrozen_candidate0:',
'''  next_required_steps:
    - "fresh reviewer performs A-S from Issue 131 / blind semantic entry only"
    - "persist and verify the A-S seal before opening withheld candidate-local history/oracle surfaces"
    - "same independent reviewer performs A-P package/self-description audit, then stops before Phase B"
    - "project manager verifies both independent commits and frozen candidate identity before reconciliation"
    - "material candidate-byte correction requires candidate.2; validation-interface defects alone do not"
    - "keep attack cardinality open and Current v0.3.6 unchanged"

frozen_candidate0:''', "active next steps")
    t = replace_once(t, '  state: FROZEN_FRESH_BLIND_PHASE_A_NEXT\n  frozen: true',
                     '  state: FROZEN_FRESH_A_S_A_P_NEXT\n  frozen: true', "successor state")
    t = replace_once(t,
'''  fresh_phase_a_issue: 128
  fresh_phase_a_branch: "validation/v037-c1-blind-phase-a-primary"
  fresh_phase_a_entry: "collaboration/reconciliation/2026-08-27-v037-candidate1-blind-phase-a-entry.md"
''',
'''  invalidated_phase_a_issue: 128
  fresh_a_s_a_p_issue: 131
  fresh_a_s_a_p_branch: "validation/v037-c1-blind-semantic-primary"
  fresh_a_s_a_p_entry: "collaboration/reconciliation/2026-08-27-v037-candidate1-blind-semantic-entry.md"
  blind_view_manifest: "collaboration/reconciliation/2026-08-27-v037-candidate1-blind-semantic-view.yaml"
''', "successor intake")
    p.write_text(t, encoding="utf-8")


def update_progress() -> None:
    p = ROOT / "research/plans/PROGRESS.yaml"
    t = p.read_text(encoding="utf-8")
    t = replace_once(t, 'status: V0_3_7_CANDIDATE1_FROZEN_FRESH_BLIND_PHASE_A_NEXT',
                     'status: V0_3_7_CANDIDATE1_FROZEN_BLIND_SEMANTIC_VIEW_READY_FRESH_A_S_A_P_NEXT',
                     "progress status")
    t = replace_once(t, '  state: FROZEN_FRESH_BLIND_PHASE_A_NEXT\n  candidate_branch:',
                     '  state: FROZEN_FRESH_A_S_A_P_NEXT\n  candidate_branch:', "progress successor state")
    t = replace_once(t,
'''  fresh_phase_a_issue: 128
  fresh_phase_a_branch: validation/v037-c1-blind-phase-a-primary
  fresh_phase_a_entry: collaboration/reconciliation/2026-08-27-v037-candidate1-blind-phase-a-entry.md
''',
'''  invalidated_phase_a_issue: 128
  invalidated_phase_a_branch: validation/v037-c1-blind-phase-a-primary
  fresh_a_s_a_p_issue: 131
  fresh_a_s_a_p_branch: validation/v037-c1-blind-semantic-primary
  fresh_a_s_a_p_entry: collaboration/reconciliation/2026-08-27-v037-candidate1-blind-semantic-entry.md
  blind_view_manifest: collaboration/reconciliation/2026-08-27-v037-candidate1-blind-semantic-view.yaml
''', "progress successor intake")
    t = replace_once(t, '    state: CANDIDATE1_FROZEN_FRESH_BLIND_PHASE_A_NEXT',
                     '    state: CANDIDATE1_FROZEN_BLIND_SEMANTIC_VIEW_READY_FRESH_A_S_A_P_NEXT',
                     "candidate build state")
    t = sub_once(t,
        r'  validation_method_reconciliation:\n.*?\n  independent_falsification:',
'''  validation_method_reconciliation:
    state: BLIND_SEMANTIC_VIEW_METHOD_REPAIRED_AFTER_CANDIDATE_SELF_PRIMING
    canonical_method: research/methodology/INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md
    external_priming_incident: research/methodology/incidents/2026-08-27-INDEPENDENT-VALIDATOR-PRIMING-INCIDENT.md
    candidate_self_priming_incident: research/methodology/incidents/2026-08-27-CANDIDATE-SELF-PRIMING-INCIDENT.md
    invalid_intake_issue: 128
    invalid_intake_phase_a_sealed: false
    active_entry: collaboration/reconciliation/2026-08-27-v037-candidate1-blind-semantic-entry.md
    active_view_manifest: collaboration/reconciliation/2026-08-27-v037-candidate1-blind-semantic-view.yaml
    active_issue: 131
    candidate_bytes_affected_by_method_change: false
    candidate2_required_by_method_change: false

  independent_falsification:''', "validation method block")
    t = sub_once(t,
        r'  independent_falsification:\n.*?\n  handoff_framework:',
'''  independent_falsification:
    state: CANDIDATE0_RECONCILED / CANDIDATE1_A_S_A_P_INTAKE_READY
    predecessor_phase_a_seal: 5ba3d241efa460fe170253860ad67045aa1d96a5
    candidate0_verdict: NEEDS_REVISION
    candidate1_targeted_revalidation_is_fresh_phase_a: false
    invalid_candidate1_intake_issue: 128
    invalid_candidate1_intake_result: REVIEWER_INELIGIBLE_AFTER_SELF_PRIMING_NO_SEAL
    active_candidate1_issue: 131
    active_candidate1_branch: validation/v037-c1-blind-semantic-primary
    active_candidate1_entry: collaboration/reconciliation/2026-08-27-v037-candidate1-blind-semantic-entry.md
    independent_sequence: A-S_THEN_A-P_THEN_STOP_BEFORE_PHASE_B
    attack_cardinality: OPEN

  handoff_framework:''', "independent block")
    t = sub_once(t,
        r'current_method_transition:\n.*?\nimmediate_next_action:',
'''current_method_transition:
  id: CANDIDATE_SELF_PRIMING_TO_BLIND_SEMANTIC_VIEW
  target: VALIDATION_INTERFACE_FOR_FROZEN_CANDIDATE1
  result: BLIND_SEMANTIC_VIEW_READY_A_S_A_P_INTAKE_131
  method: research/methodology/INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md
  incident: research/methodology/incidents/2026-08-27-CANDIDATE-SELF-PRIMING-INCIDENT.md
  reconciliation: collaboration/reconciliation/2026-08-27-v037-candidate1-blind-view-repair.md
  invalid_issue: 128
  active_issue: 131
  active_branch: validation/v037-c1-blind-semantic-primary
  candidate_bytes_changed: false
  candidate2_required: false

immediate_next_action:''', "current method transition")
    t = sub_once(t,
        r'immediate_next_action:\n.*?\nnext_after_candidate1_phase_a:',
'''immediate_next_action:
  id: CANDIDATE1_FRESH_A_S_A_P
  target: V0_3_7_CANDIDATE1_FROZEN_VIA_BLIND_SEMANTIC_VIEW
  objective: >-
    Obtain one genuinely fresh A-S semantic falsification before candidate-local history/oracles open,
    seal it, then obtain an independent A-P package/self-description audit and stop before Phase B.
  candidate_identity: v0.3.7-candidate.1
  frozen_source: ae6903464133cb5bcf3cd8909ecae1215fe0b9ba
  frozen_subtree: c0458e0d7ea417b841cbf4c8bf6e64e4aff37319
  validation_branch: validation/v037-c1-blind-semantic-primary
  blind_entry: collaboration/reconciliation/2026-08-27-v037-candidate1-blind-semantic-entry.md
  view_manifest: collaboration/reconciliation/2026-08-27-v037-candidate1-blind-semantic-view.yaml
  issue: 131
  a_s_report: collaboration/reconciliation/2026-08-27-v037-candidate1-independent-a-s-primary.md
  a_p_report: collaboration/reconciliation/2026-08-27-v037-candidate1-independent-a-p-primary.md
  current_must_remain: v0.3.6
  do_not_promote: true

next_after_candidate1_phase_a:''', "immediate next")
    t = replace_once(t,
'''next_after_candidate1_phase_a:
  - independently verify the Phase-A seal and frozen subtree identity
  - only then open author-side evidence for Phase B reconciliation
  - material candidate-byte defect requires candidate.2; do not mutate frozen candidate.1
''',
'''next_after_candidate1_phase_a:
  - independently verify A-S seal, A-P report commit, and frozen subtree identity
  - only then open author-side evidence for Phase B reconciliation
  - material candidate-byte defect or required package correction requires candidate.2; do not mutate frozen candidate.1
''', "post independent next")
    if '  - REUSE_INVALIDATED_ISSUE_128_AS_ACTIVE_FRESH_INTAKE\n' not in t:
        t = replace_once(t, '  - EDIT_FROZEN_CANDIDATE1_IN_PLACE\n',
                         '  - EDIT_FROZEN_CANDIDATE1_IN_PLACE\n  - REUSE_INVALIDATED_ISSUE_128_AS_ACTIVE_FRESH_INTAKE\n',
                         "forbidden issue reuse")
    p.write_text(t, encoding="utf-8")


def update_handoff() -> None:
    p = ROOT / "research/handoffs/CURRENT-HANDOFF.yaml"
    t = p.read_text(encoding="utf-8")
    t = replace_once(t, 'schema_version: "2.6"', 'schema_version: "2.7"', "handoff schema")
    t = sub_once(t,
        r'current_handoff_record:\n.*?\ncurrent_project_authorities:',
'''current_handoff_record:
  id: "2026-08-27-v037-candidate1-blind-semantic-ready"
  state: HANDOFF_READY_FOR_SESSION_SUCCESSION
  record_root: "research/handoffs/records/2026-08-27-v037-candidate1-blind-semantic-ready/"
  start_here: "research/handoffs/records/2026-08-27-v037-candidate1-blind-semantic-ready/HANDOFF-START-HERE.md"
  manifest: "research/handoffs/records/2026-08-27-v037-candidate1-blind-semantic-ready/HANDOFF-MANIFEST.yaml"
  project_state: "research/handoffs/records/2026-08-27-v037-candidate1-blind-semantic-ready/PROJECT-STATE.md"
  recent_three_rounds: "research/handoffs/records/2026-08-27-v037-candidate1-blind-semantic-ready/RECENT-THREE-ROUNDS.md"
  file_catalog: "research/handoffs/records/2026-08-27-v037-candidate1-blind-semantic-ready/FILE-CATALOG.md"
  post_merge_readback: "research/handoffs/records/2026-08-27-v037-candidate1-blind-semantic-ready/HANDOFF-READBACK.md"

current_project_authorities:''', "handoff record")
    t = sub_once(t,
        r'fresh_independent_validation_boundary:\n.*?\ncompletion_evidence:',
'''fresh_independent_validation_boundary:
  project_manager_takeover_context_is_validator_a_s_context: false
  invalidated_issue: 128
  invalidated_branch: validation/v037-c1-blind-phase-a-primary
  invalidated_result: CANDIDATE_SELF_PRIMING_NO_PHASE_A_SEAL
  active_issue: 131
  active_branch: validation/v037-c1-blind-semantic-primary
  active_entry: collaboration/reconciliation/2026-08-27-v037-candidate1-blind-semantic-entry.md
  blind_view_manifest: collaboration/reconciliation/2026-08-27-v037-candidate1-blind-semantic-view.yaml
  a_s_report: collaboration/reconciliation/2026-08-27-v037-candidate1-independent-a-s-primary.md
  a_p_report: collaboration/reconciliation/2026-08-27-v037-candidate1-independent-a-p-primary.md
  sequence: A-S_THEN_A-P_THEN_STOP_BEFORE_PHASE_B
  validator_must_not_read_full_project_handoff_before_a_s: true
  a_s_findings_must_be_persisted_before_candidate_local_history_oracles_open: true
  previously_exposed_project_manager_can_claim_fresh_a_s: false

completion_evidence:''', "fresh boundary")
    t = replace_once(t,
'''  candidate1_fresh_phase_a_issue: 128
  candidate1_state: FROZEN_FRESH_BLIND_PHASE_A_NEXT
  immediate_next_action: CANDIDATE1_FRESH_BLIND_PHASE_A
  current_handoff_record_refresh: COMPLETE_CANDIDATE1_FROZEN_PHASE_A_READY
''',
'''  candidate1_invalidated_phase_a_issue: 128
  candidate1_active_a_s_a_p_issue: 131
  candidate1_blind_view_repair: collaboration/reconciliation/2026-08-27-v037-candidate1-blind-view-repair.md
  candidate1_state: FROZEN_BLIND_SEMANTIC_VIEW_READY_FRESH_A_S_A_P_NEXT
  immediate_next_action: CANDIDATE1_FRESH_A_S_A_P
  current_handoff_record_refresh: COMPLETE_CANDIDATE1_BLIND_SEMANTIC_READY
''', "completion next")
    t = replace_once(t,
'''  fresh_blind_phase_a_next: true
  fresh_blind_phase_a_issue: 128
''',
'''  fresh_blind_phase_a_next: false
  invalidated_phase_a_issue: 128
  fresh_a_s_a_p_next: true
  fresh_a_s_a_p_issue: 131
''', "successor next")
    t = replace_once(t,
'''    - validation/v037-c1-blind-phase-a-primary
  candidate0_validation_branch_role: SEALED_PREDECESSOR_PHASE_A_OCCURRENCE_TRUTH
  candidate1_validation_branch_role: FRESH_PHASE_A_INTAKE_PREPARED_NOT_YET_SEALED
''',
'''    - validation/v037-c1-blind-phase-a-primary
    - validation/v037-c1-blind-semantic-primary
  candidate0_validation_branch_role: SEALED_PREDECESSOR_PHASE_A_OCCURRENCE_TRUTH
  candidate1_invalid_validation_branch_role: INVALIDATED_SELF_PRIMED_INTAKE_NO_SEAL
  candidate1_validation_branch_role: FRESH_A_S_A_P_INTAKE_PREPARED_NOT_YET_SEALED
''', "branch roles")
    p.write_text(t, encoding="utf-8")


update_active()
update_progress()
update_handoff()
print("V037_BLIND_SEMANTIC_CONTROL_PLANE_READY")
