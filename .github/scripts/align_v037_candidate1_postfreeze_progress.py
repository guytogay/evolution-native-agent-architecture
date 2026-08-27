#!/usr/bin/env python3
from pathlib import Path

p = Path('research/plans/PROGRESS.yaml')
text = p.read_text(encoding='utf-8')

def r(old: str, new: str) -> None:
    global text
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'expected one anchor, found {count}: {old!r}')
    text = text.replace(old, new, 1)

r(
'''  author_validation:
    state: PREFREEZE_MACHINE_PASS_PLUS_POSTFREEZE_TREE_EXTERNAL_ANTI_ABLATION_PASS
    exact_prefreeze_run: 33011823923
    anti_ablation_run: 33035656311
    author_evidence_is_independent_evidence: false
''',
'''  author_validation:
    state: CANDIDATE1_EXACT_PREFREEZE_PASS_WITH_INHERITED_AUTHOR_AND_ANTI_ABLATION_REPLAY
    candidate1_exact_prefreeze_run: 33055811978
    predecessor_candidate0_exact_prefreeze_run: 33011823923
    candidate0_anti_ablation_run: 33035656311
    author_evidence_is_independent_evidence: false
''')

r(
'''    blind_entry: collaboration/reconciliation/2026-08-27-v037-candidate0-blind-phase-a-entry.md
    detailed_author_handoff_disposition: RETAINED_AS_PHASE_B_CONTEXT
    candidate_bytes_affected_by_method_change: false
    candidate1_required_by_method_change: false
''',
'''    predecessor_blind_entry: collaboration/reconciliation/2026-08-27-v037-candidate0-blind-phase-a-entry.md
    active_blind_entry: collaboration/reconciliation/2026-08-27-v037-candidate1-blind-phase-a-entry.md
    candidate1_fresh_phase_a_issue: 128
    detailed_author_handoff_disposition: RETAINED_AS_PHASE_B_CONTEXT_ONLY
    candidate_bytes_affected_by_method_change: false
    candidate1_required_by_method_change: false
''')

r(
'''  independent_falsification:
    state: PHASE_A_SEALED_PHASE_B_RECONCILED_SUCCESSOR_TARGETED_REVALIDATED
    review_pr: 115
    phase_a_seal: 5ba3d241efa460fe170253860ad67045aa1d96a5
    candidate0_verdict: NEEDS_REVISION
''',
'''  independent_falsification:
    state: CANDIDATE0_PHASE_A_SEALED_PHASE_B_RECONCILED / CANDIDATE1_FRESH_PHASE_A_INTAKE_READY
    predecessor_review_pr: 115
    predecessor_phase_a_seal: 5ba3d241efa460fe170253860ad67045aa1d96a5
    candidate0_verdict: NEEDS_REVISION
''')

r(
'''current_method_transition:
  id: FRESH_VALIDATOR_INFORMATION_BOUNDARY
  target: VALIDATION_METHOD_OUTSIDE_FROZEN_CANDIDATE0
  result: BLIND_PHASE_A_ENTRY_PREPARED
  method: research/methodology/INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md
  incident: research/methodology/incidents/2026-08-27-INDEPENDENT-VALIDATOR-PRIMING-INCIDENT.md
  blind_entry: collaboration/reconciliation/2026-08-27-v037-candidate0-blind-phase-a-entry.md
  original_detailed_handoff_erased: false
  original_detailed_handoff_phase: PHASE_B_AFTER_PHASE_A_SEAL
  candidate_bytes_changed: false
  candidate1_required: false
''',
'''current_method_transition:
  id: FRESH_VALIDATOR_INFORMATION_BOUNDARY
  target: VALIDATION_METHOD_FOR_FROZEN_CANDIDATE1_SUCCESSOR_REVIEW
  result: CANDIDATE1_BLIND_PHASE_A_INTAKE_PREPARED
  method: research/methodology/INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md
  incident: research/methodology/incidents/2026-08-27-INDEPENDENT-VALIDATOR-PRIMING-INCIDENT.md
  predecessor_blind_entry: collaboration/reconciliation/2026-08-27-v037-candidate0-blind-phase-a-entry.md
  active_blind_entry: collaboration/reconciliation/2026-08-27-v037-candidate1-blind-phase-a-entry.md
  fresh_phase_a_issue: 128
  original_detailed_handoff_erased: false
  author_side_context_phase: PHASE_B_AFTER_CANDIDATE1_PHASE_A_SEAL
  candidate_bytes_changed: false
  successor_review_is_automatic_for_every_candidate: false
''')

p.write_text(text, encoding='utf-8')
print('CANDIDATE1_POSTFREEZE_PROGRESS_ALIGNMENT_READY')
