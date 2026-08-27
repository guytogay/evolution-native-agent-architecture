#!/usr/bin/env python3
from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly one anchor, observed {count}")
    return text.replace(old, new, 1)


def update(path: str, transforms):
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    for old, new, label in transforms:
        text = replace_once(text, old, new, f"{path}: {label}")
    p.write_text(text, encoding="utf-8")


update("research/plans/PROGRESS.yaml", [
    ('  candidate_build:\n    state: CANDIDATE2_FOCUSED_SUCCESSOR_REPAIR_NEXT\n    current_candidate_identity: v0.3.7-candidate.2\n    predecessor_frozen_identity: v0.3.7-candidate.1\n    mutable_in_place: true_until_candidate2_freeze\n    exact_prefreeze_validation: PASS\n    exact_prefreeze_run: 33055811978',
     '  candidate_build:\n    state: CANDIDATE2_FOCUSED_SUCCESSOR_REPAIR_NEXT\n    current_candidate_identity: v0.3.7-candidate.2\n    predecessor_frozen_identity: v0.3.7-candidate.1\n    mutable_in_place: true_until_candidate2_freeze\n    exact_prefreeze_validation: NOT_RUN\n    exact_prefreeze_run: null',
     'candidate2 prefreeze state'),
    ('    active_issue: 131\n    active_branch: validation/v037-c1-blind-semantic-primary',
     '    completed_issue: 131\n    sealed_branch: validation/v037-c1-blind-semantic-primary',
     'validation method intake status'),
    ('  current_method_transition:\n  id: CANDIDATE_SELF_PRIMING_TO_BLIND_SEMANTIC_VIEW\n  target: VALIDATION_INTERFACE_FOR_FROZEN_CANDIDATE1\n  result: BLIND_SEMANTIC_VIEW_READY_A_S_A_P_INTAKE_131',
     'current_method_transition:\n  id: CANDIDATE_SELF_PRIMING_TO_BLIND_SEMANTIC_VIEW\n  target: VALIDATION_INTERFACE_FOR_FROZEN_CANDIDATE1\n  result: BLIND_SEMANTIC_VIEW_COMPLETED_A_S_A_P_SEALED_PHASE_B_NEEDS_REVISION',
     'method transition result'),
    ('  active_issue: 131\n  active_branch: validation/v037-c1-blind-semantic-primary\n  candidate_bytes_changed: false\n  candidate2_required: false',
     '  completed_issue: 131\n  sealed_branch: validation/v037-c1-blind-semantic-primary\n  candidate_bytes_changed: false\n  candidate2_required_by_method_change: false\n  candidate2_required_by_phase_b_defects: true',
     'method transition active labels'),
])

update("research/handoffs/CURRENT-HANDOFF.yaml", [
    ('  candidate1_active_a_s_a_p_issue: 131', '  candidate1_completed_a_s_a_p_issue: 131', 'completion issue label'),
    ('  current_handoff_record_refresh: COMPLETE_CANDIDATE1_BLIND_SEMANTIC_READY',
     '  current_handoff_record_refresh: REQUIRED_AFTER_CANDIDATE2_FOCUSED_REPAIR',
     'handoff record refresh signal'),
])

print("candidate2 Phase-B readback correction PASS")
