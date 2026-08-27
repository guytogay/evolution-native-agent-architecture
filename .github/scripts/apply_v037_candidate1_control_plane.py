#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one anchor, found {count}")
    return text.replace(old, new, 1)


def sub_once(text: str, pattern: str, repl: str, label: str) -> str:
    out, count = re.subn(pattern, repl, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one regex anchor, found {count}")
    return out


def update_active() -> None:
    path = ROOT / "research" / "ACTIVE-RESEARCH.yaml"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        '  state: "V0_3_7_CANDIDATE0_FROZEN / BLIND_PHASE_A_METHOD_MAIN_INTEGRATED / INDEPENDENT_FALSIFICATION_PR_115_OPEN / FRESH_BLIND_PHASE_A_NEXT / NOT_CURRENT"',
        '  state: "V0_3_7_CANDIDATE1_SUCCESSOR_REPAIR_RECONCILED / EXACT_PREFREEZE_NEXT / NOT_FROZEN / NOT_CURRENT"',
        "active state",
    )
    latest = '''latest_transition:
  event: "V0_3_7_CANDIDATE1_SUCCESSOR_REPAIR_RECONCILED"
  current_changed_by_transition: false
  next_version: "v0.3.7"
  predecessor_candidate_identity: "v0.3.7-candidate.0"
  predecessor_frozen_source: "d0e793593184740d9732902e948afd48ed96ae2f"
  predecessor_frozen_subtree: "cffbf76fe1448b020b637c78d1f7ae46e4c0115b"
  predecessor_phase_a_seal: "5ba3d241efa460fe170253860ad67045aa1d96a5"
  predecessor_verdict: NEEDS_REVISION
  active_candidate_identity: "v0.3.7-candidate.1"
  active_candidate_branch: "candidate/v0.3.7-candidate.1"
  active_candidate_observed_head: "b76bb9e7d0d2ee820d7dcc3a7f72f20fefe363e6"
  active_candidate_observed_subtree: "25d068d158ee37e4e43481c345cce9281febddd1"
  successor_reconciliation_record: "collaboration/reconciliation/2026-08-27-v037-candidate1-successor-repair-reconciliation.md"
  final_targeted_run: 33052764739
  final_open_branch_probe_run: 33052764661
  candidate_state: SUCCESSOR_REPAIR_RECONCILED_EXACT_PREFREEZE_NEXT
  exact_prefreeze_next: true

'''
    text = sub_once(
        text,
        r"latest_transition:\n.*?\ncandidate_validation_transition:\n",
        latest + "candidate_validation_transition:\n",
        "latest transition block",
    )
    validation = '''candidate_validation_transition:
  current_state: CANDIDATE1_SUCCESSOR_REPAIR_RECONCILED_EXACT_PREFREEZE_NEXT
  completed:
    - release scope stabilized and v0.3.7 assigned
    - candidate.0 assembled, exact-pre-freeze validated, and externally frozen
    - blind Phase-A information boundary integrated before independent review
    - fresh blind Phase A sealed at 5ba3d241efa460fe170253860ad67045aa1d96a5
    - Phase B classified four deterministic candidate.0 byte defects as shared blind spots
    - candidate.0 verdict reconciled as NEEDS_REVISION / CANDIDATE_1_REQUIRED
    - candidate.1 created as a successor rather than mutating frozen candidate.0
    - first successor repair closed Phase-A findings A-D while preserving false-BLOCK controls
    - open-branch probes expanded beyond A-D and exposed integration-chronology and shallow-source-history defects
    - second focused repair closed those demonstrated defects without forcing post-commit current-state immutability
    - final targeted run 33052764739 PASS; record selftest observed 24, helper selftest observed 13, targeted conditions 16
    - final open-branch run 33052764661 PASS; repaired shapes rejected, post-commit reselection control retained
    - candidate-ID collision remains a visible namespace residual because no universal uniqueness contract is established
  next_required_steps:
    - "run an exact candidate.1 pre-freeze gate bound to one exact source commit and candidate subtree"
    - "include Current isolation, inherited candidate checks, sealed-Phase-A successor regressions, and focused open-branch regressions"
    - "freeze candidate.1 only if the exact-source gate passes; bind source/subtree externally without rewriting tested cargo"
    - "after freeze, explicitly reconcile whether any additional independent review is warranted; do not silently equate targeted revalidation with fresh Phase A"
    - "keep attack cardinality open and visible residuals durable; do not convert unknown namespace policy into universal law"
    - "do not modify or promote releases/current/ during candidate.1 validation/freeze"

'''
    text = sub_once(
        text,
        r"candidate_validation_transition:\n.*?\nfrozen_candidate:\n",
        validation + "frozen_candidate0:\n",
        "candidate validation block",
    )
    old_frozen_body_pattern = r"frozen_candidate0:\n.*?\nhandoff:\n"
    frozen_and_successor = '''frozen_candidate0:
  identity: "v0.3.7-candidate.0"
  branch: "candidate/v0.3.7-candidate.0"
  branch_head_is_identity: false
  source_commit: "d0e793593184740d9732902e948afd48ed96ae2f"
  subtree_sha: "cffbf76fe1448b020b637c78d1f7ae46e4c0115b"
  subtree_path: "releases/v0.3.7-candidate/"
  mutable_in_place: false
  independent_falsification: SEALED_NEEDS_REVISION
  phase_a_seal: "5ba3d241efa460fe170253860ad67045aa1d96a5"
  release_decision: NOT_RELEASED_SUPERSEDED_BY_SUCCESSOR

successor_candidate1:
  identity: "v0.3.7-candidate.1"
  branch: "candidate/v0.3.7-candidate.1"
  branch_head_is_freeze_identity: false
  observed_head: "b76bb9e7d0d2ee820d7dcc3a7f72f20fefe363e6"
  observed_subtree: "25d068d158ee37e4e43481c345cce9281febddd1"
  state: SUCCESSOR_REPAIR_RECONCILED_EXACT_PREFREEZE_NEXT
  frozen: false
  current: false
  targeted_revalidation_run: 33052764739
  open_branch_reprobe_run: 33052764661
  attack_cardinality: OPEN
  remaining_visible_residuals:
    - "source/receiver candidate_id namespace collision remains allowed absent a universal cross-environment uniqueness contract"

handoff:
'''
    text = sub_once(text, old_frozen_body_pattern, frozen_and_successor, "frozen/successor block")
    path.write_text(text, encoding="utf-8")


def update_progress() -> None:
    path = ROOT / "research" / "plans" / "PROGRESS.yaml"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "status: V0_3_7_CANDIDATE0_FROZEN_BLIND_FRESH_PHASE_A_READY",
        "status: V0_3_7_CANDIDATE1_SUCCESSOR_REPAIR_RECONCILED_EXACT_PREFREEZE_NEXT",
        "progress status",
    )
    candidate_blocks = '''frozen_candidate0:
  identity: v0.3.7-candidate.0
  state: FROZEN_NEEDS_REVISION_SUPERSEDED_BY_CANDIDATE1
  candidate_branch: candidate/v0.3.7-candidate.0
  branch_head_is_frozen_identity: false
  frozen_source_commit: d0e793593184740d9732902e948afd48ed96ae2f
  frozen_candidate_subtree: cffbf76fe1448b020b637c78d1f7ae46e4c0115b
  subtree_path: releases/v0.3.7-candidate/
  freeze_record: collaboration/reconciliation/2026-08-27-v037-candidate0-freeze.md
  blind_phase_a_entry: collaboration/reconciliation/2026-08-27-v037-candidate0-blind-phase-a-entry.md
  phase_a_report: collaboration/reconciliation/2026-08-27-v037-candidate0-independent-phase-a-primary.md
  phase_a_seal_commit: 5ba3d241efa460fe170253860ad67045aa1d96a5
  phase_b_reconciliation_commit: cbdc2b00a4bdb490b83aff426db3cfe844e22490
  independent_semantic_falsification: SEALED_NEEDS_REVISION
  release_decision: NOT_RELEASED
  successor_required: true

successor_candidate1:
  identity: v0.3.7-candidate.1
  state: SUCCESSOR_REPAIR_RECONCILED_EXACT_PREFREEZE_NEXT
  candidate_branch: candidate/v0.3.7-candidate.1
  branch_head_is_frozen_identity: false
  observed_head: b76bb9e7d0d2ee820d7dcc3a7f72f20fefe363e6
  observed_candidate_subtree: 25d068d158ee37e4e43481c345cce9281febddd1
  current_subtree_same_head: 7dcbb3934883ffa6cc5292a662588cafc1533cff
  reconciliation_record: collaboration/reconciliation/2026-08-27-v037-candidate1-successor-repair-reconciliation.md
  targeted_revalidation_run: 33052764739
  open_branch_reprobe_run: 33052764661
  exact_prefreeze_validation: PENDING
  frozen: false
  release_decision: NOT_MADE
  attack_cardinality: OPEN

phase_state:
'''
    text = sub_once(
        text,
        r"frozen_candidate0:\n.*?\nphase_state:\n",
        candidate_blocks,
        "candidate blocks",
    )
    text = sub_once(
        text,
        r"  candidate_build:\n.*?\n  author_validation:\n",
        '''  candidate_build:\n    state: CANDIDATE1_SUCCESSOR_REPAIR_RECONCILED_EXACT_PREFREEZE_NEXT\n    current_candidate_identity: v0.3.7-candidate.1\n    predecessor_frozen_identity: v0.3.7-candidate.0\n    mutable_in_place: true_until_successor_freeze_only\n    exact_prefreeze_validation: PENDING\n\n  author_validation:\n''',
        "candidate build phase",
    )
    text = sub_once(
        text,
        r"  independent_falsification:\n.*?\n  handoff_framework:\n",
        '''  independent_falsification:\n    state: PHASE_A_SEALED_PHASE_B_RECONCILED_SUCCESSOR_TARGETED_REVALIDATED\n    review_pr: 115\n    phase_a_seal: 5ba3d241efa460fe170253860ad67045aa1d96a5\n    candidate0_verdict: NEEDS_REVISION\n    candidate1_targeted_revalidation_is_fresh_phase_a: false\n    candidate1_additional_independent_review_after_freeze: EXPLICIT_DECISION_PENDING\n    attack_cardinality: OPEN\n\n  handoff_framework:\n''',
        "independent falsification phase",
    )
    immediate = '''immediate_next_action:
  id: CANDIDATE1_EXACT_PREFREEZE_VALIDATION
  target: V0_3_7_CANDIDATE1_EXACT_SOURCE_AND_SUBTREE
  objective: >-
    Run the full candidate.1 pre-freeze validation on one exact committed source head,
    preserving Current isolation and combining inherited candidate gates with all
    successor repair regressions derived from sealed Phase A and later focused probes.
  candidate_identity: v0.3.7-candidate.1
  candidate_branch: candidate/v0.3.7-candidate.1
  observed_pre_gate_head: b76bb9e7d0d2ee820d7dcc3a7f72f20fefe363e6
  observed_pre_gate_subtree: 25d068d158ee37e4e43481c345cce9281febddd1
  predecessor_phase_a_seal: 5ba3d241efa460fe170253860ad67045aa1d96a5
  current_must_remain: v0.3.6
  do_not_promote: true

next_after_exact_prefreeze:
  - if exact-source validation fails, repair candidate.1 before freeze and rerun the exact gate
  - if it passes, bind the exact candidate.1 source commit and subtree in an external freeze record without rewriting tested cargo
  - explicitly decide whether additional independent post-freeze review is warranted; targeted same-falsifier revalidation is not fresh Phase A
  - reconcile visible residuals without treating every unknown as a release blocker
  - only after governed acceptance consider release preparation/promotion; Current remains v0.3.6 until then

candidate1_rule:
  creation_basis: MATERIAL_CANDIDATE_BYTE_CORRECTIONS_ESTABLISHED_BY_SEALED_PHASE_A_AND_PHASE_B
  candidate0_must_remain_frozen_lineage: true
  candidate1_may_mutate_before_freeze: true
  candidate1_material_change_after_freeze_requires_successor: true

'''
    text = sub_once(
        text,
        r"immediate_next_action:\n.*?\ncandidate1_rule:\n.*?\nhandoff:\n",
        immediate + "handoff:\n",
        "immediate next action",
    )
    if "successor_repair_transition:" not in text:
        marker = "\nforbidden_now:\n"
        addition = '''\nsuccessor_repair_transition:\n  id: CANDIDATE1_SUCCESSOR_REPAIR_RECONCILIATION\n  result: TARGETED_REPAIR_PASS_WITH_OPEN_RESIDUALS\n  record: collaboration/reconciliation/2026-08-27-v037-candidate1-successor-repair-reconciliation.md\n  first_repair_commit: 583ac81\n  focused_repair_commit: bc8be8bc02a2b2515cfa1b7eee2c4bd3c2a37f90\n  final_targeted_run: 33052764739\n  final_open_branch_run: 33052764661\n  exact_prefreeze_next: true\n  attack_cardinality: OPEN\n'''
        text = replace_once(text, marker, addition + marker, "successor transition insertion")
    path.write_text(text, encoding="utf-8")


def update_handoff() -> None:
    path = ROOT / "research" / "handoffs" / "CURRENT-HANDOFF.yaml"
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, 'schema_version: "2.4"', 'schema_version: "2.5"', "handoff schema")
    completion = '''completion_evidence:
  handoff_architecture_pr: 116
  blind_phase_a_method_pr: 119
  current_reverified: "v0.3.6 / CURRENT / FIELD_VALIDATION"
  frozen_candidate0_source: d0e793593184740d9732902e948afd48ed96ae2f
  frozen_candidate0_subtree: cffbf76fe1448b020b637c78d1f7ae46e4c0115b
  fresh_phase_a_seal: 5ba3d241efa460fe170253860ad67045aa1d96a5
  candidate0_phase_b_verdict: NEEDS_REVISION
  candidate1_branch: candidate/v0.3.7-candidate.1
  candidate1_observed_head: b76bb9e7d0d2ee820d7dcc3a7f72f20fefe363e6
  candidate1_observed_subtree: 25d068d158ee37e4e43481c345cce9281febddd1
  candidate1_reconciliation_record: collaboration/reconciliation/2026-08-27-v037-candidate1-successor-repair-reconciliation.md
  candidate1_final_targeted_run: 33052764739
  candidate1_final_open_branch_run: 33052764661
  candidate1_state: SUCCESSOR_REPAIR_RECONCILED_EXACT_PREFREEZE_NEXT
  immediate_next_action: CANDIDATE1_EXACT_PREFREEZE_VALIDATION
  current_handoff_record_refresh: REQUIRED_AFTER_NEXT_MATERIAL_GATE

candidate1_successor_state:
  identity: v0.3.7-candidate.1
  predecessor_identity: v0.3.7-candidate.0
  predecessor_phase_a_sealed: true
  predecessor_verdict: NEEDS_REVISION
  successor_frozen: false
  successor_current: false
  exact_prefreeze_validation: PENDING
  targeted_revalidation_is_fresh_phase_a: false
  attack_cardinality: OPEN
  remaining_visible_residuals:
    - candidate-id cross-environment namespace uniqueness is not universalized without a governing contract

branch_hygiene:
  cleanup_completed_and_reobserved: true
  live_branches_after_successor_transition:
    - main
    - research/ena-reconstruction
    - candidate/v0.3.7-candidate.0
    - candidate/v0.3.7-candidate.1
    - validation/v037-c0-blind-phase-a-primary
  validation_branch_role: SEALED_PHASE_A_OCCURRENCE_TRUTH
  candidate0_branch_role: FROZEN_PREDECESSOR_LINEAGE
  candidate1_branch_role: ACTIVE_SUCCESSOR_PREFREEZE_WORKSPACE

'''
    text = sub_once(
        text,
        r"completion_evidence:\n.*?\nbranch_hygiene:\n.*?\nrule: >-\n",
        completion + "rule: >-\n",
        "handoff completion/branch hygiene",
    )
    path.write_text(text, encoding="utf-8")


def main() -> None:
    update_active()
    update_progress()
    update_handoff()
    print("CANDIDATE1_CONTROL_PLANE_TRANSFORMATION_APPLIED")


if __name__ == "__main__":
    main()
