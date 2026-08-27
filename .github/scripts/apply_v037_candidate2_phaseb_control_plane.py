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


update("research/ACTIVE-RESEARCH.yaml", [
    ('  state: "V0_3_7_CANDIDATE1_FROZEN / BLIND_SEMANTIC_VIEW_READY / FRESH_A_S_A_P_NEXT / NOT_CURRENT / NOT_RELEASED"',
     '  state: "V0_3_7_CANDIDATE1_NEEDS_REVISION / CANDIDATE2_FOCUSED_REPAIR_NEXT / NOT_CURRENT / NOT_RELEASED"', 'active state'),
    ('  event: "V0_3_7_CANDIDATE1_BLIND_SEMANTIC_VIEW_READY_A_S_A_P_NEXT"',
     '  event: "V0_3_7_CANDIDATE1_A_S_A_P_PHASE_B_NEEDS_REVISION_CANDIDATE2_REQUIRED"', 'latest event'),
    ('  candidate_state: FROZEN_FRESH_A_S_A_P_NEXT',
     '  candidate_state: FROZEN_NEEDS_REVISION_SUPERSEDED_BY_CANDIDATE2', 'candidate state'),
    ('  exact_prefreeze_next: false\n\ncandidate_validation_transition:\n  current_state: CANDIDATE1_FROZEN_BLIND_SEMANTIC_VIEW_READY_FRESH_A_S_A_P_NEXT',
     '  exact_prefreeze_next: false\n  fresh_a_s_seal: "2e6b46aeedc1945a03aac93620ad36aa1ccbd70f"\n  final_a_p_commit: "b970148fe9596ea9cad0a2817a3b399a1d2b75f5"\n  phase_b_record: "collaboration/reconciliation/2026-08-27-v037-candidate1-a-s-a-p-phase-b-reconciliation.md"\n  phase_b_verdict: NEEDS_REVISION\n  successor_required: "v0.3.7-candidate.2"\n\ncandidate_validation_transition:\n  current_state: CANDIDATE1_FROZEN_NEEDS_REVISION_CANDIDATE2_FOCUSED_REPAIR_NEXT', 'latest evidence block'),
    ('    - Issue 131 prepared for fresh A-S then A-P independent validation\n',
     '    - Issue 131 prepared for fresh A-S then A-P independent validation\n    - fresh A-S sealed at 2e6b46aeedc1945a03aac93620ad36aa1ccbd70f with four deterministic semantic findings\n    - A-P committed at b970148fe9596ea9cad0a2817a3b399a1d2b75f5 and confirmed all four A-S findings plus one package self-description drift\n    - Phase B independently reproduced the four semantic defects from frozen candidate.1 bytes and classified them as shared blind spots rather than oracle errors\n    - candidate.1 verdict is NEEDS_REVISION; frozen bytes remain immutable and candidate.2 is required\n', 'completed A-S/A-P'),
    ('  next_required_steps:\n    - "fresh reviewer performs A-S from Issue 131 / blind semantic entry only"\n    - "persist and verify the A-S seal before opening withheld candidate-local history/oracle surfaces"\n    - "same independent reviewer performs A-P package/self-description audit, then stops before Phase B"\n    - "project manager verifies both independent commits and frozen candidate identity before reconciliation"\n    - "material candidate-byte correction requires candidate.2; validation-interface defects alone do not"\n    - "keep attack cardinality open and Current v0.3.6 unchanged"',
     '  next_required_steps:\n    - "repair A-S-01 through A-S-04 on candidate/v0.3.7-candidate.2 only; never mutate frozen candidate.1"\n    - "repair A-P-05 active package/self-description drift without rewriting historical freeze occurrence truth"\n    - "add mutation-sensitive regressions plus legitimate-behavior false-BLOCK controls"\n    - "rerun inherited candidate checks and focused nearby open-branch probes"\n    - "run exact candidate.2 prefreeze validation only after focused repairs reconcile"\n    - "keep attack cardinality open and Current v0.3.6 unchanged"', 'next steps'),
    ('successor_candidate1:\n  identity: "v0.3.7-candidate.1"\n  branch: "candidate/v0.3.7-candidate.1"\n  branch_head_is_freeze_identity: false\n  observed_head: "ae6903464133cb5bcf3cd8909ecae1215fe0b9ba"\n  observed_subtree: "c0458e0d7ea417b841cbf4c8bf6e64e4aff37319"\n  state: FROZEN_FRESH_A_S_A_P_NEXT',
     'successor_candidate1:\n  identity: "v0.3.7-candidate.1"\n  branch: "candidate/v0.3.7-candidate.1"\n  branch_head_is_freeze_identity: false\n  observed_head: "ae6903464133cb5bcf3cd8909ecae1215fe0b9ba"\n  observed_subtree: "c0458e0d7ea417b841cbf4c8bf6e64e4aff37319"\n  state: FROZEN_NEEDS_REVISION_SUPERSEDED_BY_CANDIDATE2', 'candidate1 block state'),
    ('  remaining_visible_residuals:\n    - "source/receiver candidate_id namespace collision remains allowed absent a universal cross-environment uniqueness contract"\n\nhandoff:',
     '  fresh_a_s_seal: "2e6b46aeedc1945a03aac93620ad36aa1ccbd70f"\n  final_a_p_commit: "b970148fe9596ea9cad0a2817a3b399a1d2b75f5"\n  phase_b_verdict: NEEDS_REVISION\n  release_decision: NOT_RELEASED_NEEDS_REVISION\n  remaining_visible_residuals:\n    - "source/receiver candidate_id namespace collision remains allowed absent a universal cross-environment uniqueness contract"\n\nsuccessor_candidate2:\n  identity: "v0.3.7-candidate.2"\n  branch: "candidate/v0.3.7-candidate.2"\n  created_from_frozen_candidate1_source: "ae6903464133cb5bcf3cd8909ecae1215fe0b9ba"\n  state: FOCUSED_SUCCESSOR_REPAIR_NEXT\n  frozen: false\n  current: false\n  phase_b_basis: "collaboration/reconciliation/2026-08-27-v037-candidate1-a-s-a-p-phase-b-reconciliation.md"\n  repair_scope:\n    - "integration requires represented reality contact at/before commit while preserving unresolved UNKNOWN semantics"\n    - "durable migration provenance duplicate claims cannot contradict"\n    - "Authority NOT_REQUIRED cannot be poisoned by irrelevant malformed grants"\n    - "same-sequence conflicting effect receipts cannot create input-order-dependent replay"\n    - "active candidate self-description/status projection repaired"\n\nhandoff:', 'candidate2 block'),
])

update("research/plans/PROGRESS.yaml", [
    ('status: V0_3_7_CANDIDATE1_FROZEN_BLIND_SEMANTIC_VIEW_READY_FRESH_A_S_A_P_NEXT',
     'status: V0_3_7_CANDIDATE1_NEEDS_REVISION_CANDIDATE2_FOCUSED_REPAIR_NEXT', 'status'),
    ('successor_candidate1:\n  identity: v0.3.7-candidate.1\n  state: FROZEN_FRESH_A_S_A_P_NEXT',
     'successor_candidate1:\n  identity: v0.3.7-candidate.1\n  state: FROZEN_NEEDS_REVISION_SUPERSEDED_BY_CANDIDATE2', 'candidate1 state'),
    ('  release_decision: NOT_MADE\n  attack_cardinality: OPEN\n\nphase_state:',
     '  release_decision: NOT_RELEASED_NEEDS_REVISION\n  fresh_a_s_seal: 2e6b46aeedc1945a03aac93620ad36aa1ccbd70f\n  final_a_p_commit: b970148fe9596ea9cad0a2817a3b399a1d2b75f5\n  phase_b_record: collaboration/reconciliation/2026-08-27-v037-candidate1-a-s-a-p-phase-b-reconciliation.md\n  attack_cardinality: OPEN\n\nsuccessor_candidate2:\n  identity: v0.3.7-candidate.2\n  state: FOCUSED_SUCCESSOR_REPAIR_NEXT\n  candidate_branch: candidate/v0.3.7-candidate.2\n  created_from_candidate1_frozen_source: ae6903464133cb5bcf3cd8909ecae1215fe0b9ba\n  frozen: false\n  current: false\n  repair_basis: collaboration/reconciliation/2026-08-27-v037-candidate1-a-s-a-p-phase-b-reconciliation.md\n\nphase_state:', 'candidate2 insert'),
    ('    state: CANDIDATE1_FROZEN_BLIND_SEMANTIC_VIEW_READY_FRESH_A_S_A_P_NEXT\n    current_candidate_identity: v0.3.7-candidate.1\n    predecessor_frozen_identity: v0.3.7-candidate.0\n    mutable_in_place: false_frozen_successor_required_for_material_change',
     '    state: CANDIDATE2_FOCUSED_SUCCESSOR_REPAIR_NEXT\n    current_candidate_identity: v0.3.7-candidate.2\n    predecessor_frozen_identity: v0.3.7-candidate.1\n    mutable_in_place: true_until_candidate2_freeze', 'candidate build'),
    ('  independent_falsification:\n    state: CANDIDATE0_RECONCILED / CANDIDATE1_A_S_A_P_INTAKE_READY',
     '  independent_falsification:\n    state: CANDIDATE1_A_S_A_P_SEALED_PHASE_B_NEEDS_REVISION', 'independent state'),
    ('    active_candidate1_entry: collaboration/reconciliation/2026-08-27-v037-candidate1-blind-semantic-entry.md\n    a_s_report:',
     '    active_candidate1_entry: collaboration/reconciliation/2026-08-27-v037-candidate1-blind-semantic-entry.md\n    candidate1_a_s_seal: 2e6b46aeedc1945a03aac93620ad36aa1ccbd70f\n    candidate1_a_p_commit: b970148fe9596ea9cad0a2817a3b399a1d2b75f5\n    candidate1_phase_b_verdict: NEEDS_REVISION\n    candidate1_phase_b_record: collaboration/reconciliation/2026-08-27-v037-candidate1-a-s-a-p-phase-b-reconciliation.md\n    a_s_report:', 'independent evidence'),
    ('immediate_next_action:\n  id: CANDIDATE1_FRESH_A_S_A_P\n  target: V0_3_7_CANDIDATE1_FROZEN_VIA_BLIND_SEMANTIC_VIEW\n  objective: >-\n    Obtain one genuinely fresh A-S semantic falsification before candidate-local history/oracles open,\n    seal it, then obtain an independent A-P package/self-description audit and stop before Phase B.\n  candidate_identity: v0.3.7-candidate.1\n  frozen_source: ae6903464133cb5bcf3cd8909ecae1215fe0b9ba\n  frozen_subtree: c0458e0d7ea417b841cbf4c8bf6e64e4aff37319\n  validation_branch: validation/v037-c1-blind-semantic-primary\n  blind_entry: collaboration/reconciliation/2026-08-27-v037-candidate1-blind-semantic-entry.md\n  view_manifest: collaboration/reconciliation/2026-08-27-v037-candidate1-blind-semantic-view.yaml\n  issue: 131\n  a_s_report: collaboration/reconciliation/2026-08-27-v037-candidate1-independent-a-s-primary.md\n  a_p_report: collaboration/reconciliation/2026-08-27-v037-candidate1-independent-a-p-primary.md\n  current_must_remain: v0.3.6\n  do_not_promote: true',
     'immediate_next_action:\n  id: CANDIDATE2_FOCUSED_SUCCESSOR_REPAIR\n  target: V0_3_7_CANDIDATE2\n  objective: >-\n    Repair the four material frozen-candidate.1 semantic defects sealed by fresh A-S and confirmed by A-P/Phase B,\n    plus the deterministic active-package self-description drift, without mutating candidate.1 or Current.\n  candidate_identity: v0.3.7-candidate.2\n  candidate_branch: candidate/v0.3.7-candidate.2\n  predecessor_frozen_source: ae6903464133cb5bcf3cd8909ecae1215fe0b9ba\n  predecessor_frozen_subtree: c0458e0d7ea417b841cbf4c8bf6e64e4aff37319\n  phase_b_record: collaboration/reconciliation/2026-08-27-v037-candidate1-a-s-a-p-phase-b-reconciliation.md\n  current_must_remain: v0.3.6\n  do_not_promote: true', 'immediate action'),
    ('next_after_candidate1_phase_a:\n  - independently verify A-S seal, A-P report commit, and frozen subtree identity\n  - only then open author-side evidence for Phase B reconciliation\n  - material candidate-byte defect or required package correction requires candidate.2; do not mutate frozen candidate.1\n  - non-contract residuals remain visible rather than being universalized merely for closure\n  - only after evidence reconciliation consider release preparation/promotion',
     'candidate2_repair_path:\n  - implement narrow semantic repairs for A-S-01 through A-S-04\n  - repair A-P-05 active package/self-description drift\n  - add mutation-sensitive regressions and legitimate-behavior controls\n  - run focused nearby open-branch probes without pretending this is fresh A-S\n  - only after repair reconciliation run exact candidate.2 prefreeze validation\n  - preserve non-contract residuals rather than universalizing them for closure', 'post phase-a path'),
])

update("research/handoffs/CURRENT-HANDOFF.yaml", [
    ('schema_version: "2.7"', 'schema_version: "2.8"', 'schema'),
    ('  active_issue: 131\n  active_branch: validation/v037-c1-blind-semantic-primary',
     '  completed_issue: 131\n  sealed_branch: validation/v037-c1-blind-semantic-primary', 'validation intake state'),
    ('  a_s_findings_must_be_persisted_before_a_p: true\n  independent_artifacts_must_be_persisted_before_phase_b: true',
     '  a_s_findings_must_be_persisted_before_a_p: true\n  independent_artifacts_must_be_persisted_before_phase_b: true\n  a_s_seal: 2e6b46aeedc1945a03aac93620ad36aa1ccbd70f\n  final_a_p_commit: b970148fe9596ea9cad0a2817a3b399a1d2b75f5\n  phase_b_record: collaboration/reconciliation/2026-08-27-v037-candidate1-a-s-a-p-phase-b-reconciliation.md\n  phase_b_verdict: NEEDS_REVISION', 'validation result'),
    ('  candidate1_state: FROZEN_BLIND_SEMANTIC_VIEW_READY_FRESH_A_S_A_P_NEXT\n  immediate_next_action: CANDIDATE1_FRESH_A_S_A_P',
     '  candidate1_state: FROZEN_NEEDS_REVISION_SUPERSEDED_BY_CANDIDATE2\n  candidate1_a_s_seal: 2e6b46aeedc1945a03aac93620ad36aa1ccbd70f\n  candidate1_a_p_commit: b970148fe9596ea9cad0a2817a3b399a1d2b75f5\n  candidate1_phase_b_verdict: NEEDS_REVISION\n  candidate2_branch: candidate/v0.3.7-candidate.2\n  immediate_next_action: CANDIDATE2_FOCUSED_SUCCESSOR_REPAIR', 'completion state'),
    ('  fresh_a_s_a_p_next: true\n  fresh_a_s_a_p_issue: 131',
     '  fresh_a_s_a_p_next: false\n  fresh_a_s_a_p_issue: 131\n  fresh_a_s_seal: 2e6b46aeedc1945a03aac93620ad36aa1ccbd70f\n  final_a_p_commit: b970148fe9596ea9cad0a2817a3b399a1d2b75f5\n  phase_b_verdict: NEEDS_REVISION\n  superseded_by_candidate2: true', 'candidate1 successor result'),
    ('  remaining_visible_residuals:\n    - candidate-id cross-environment namespace uniqueness is not universalized without a governing contract\n\nbranch_hygiene:',
     '  remaining_visible_residuals:\n    - candidate-id cross-environment namespace uniqueness is not universalized without a governing contract\n\ncandidate2_successor_state:\n  identity: v0.3.7-candidate.2\n  branch: candidate/v0.3.7-candidate.2\n  created_from_frozen_candidate1_source: ae6903464133cb5bcf3cd8909ecae1215fe0b9ba\n  state: FOCUSED_SUCCESSOR_REPAIR_NEXT\n  frozen: false\n  current: false\n  repair_basis: collaboration/reconciliation/2026-08-27-v037-candidate1-a-s-a-p-phase-b-reconciliation.md\n  current_must_remain: v0.3.6\n\nbranch_hygiene:', 'candidate2 handoff block'),
    ('    - candidate/v0.3.7-candidate.1\n    - validation/v037-c0-blind-phase-a-primary',
     '    - candidate/v0.3.7-candidate.1\n    - candidate/v0.3.7-candidate.2\n    - validation/v037-c0-blind-phase-a-primary', 'branch list candidate2'),
    ('  candidate1_validation_branch_role: FRESH_A_S_A_P_INTAKE_PREPARED_NOT_YET_SEALED',
     '  candidate1_validation_branch_role: SEALED_A_S_A_P_OCCURRENCE_TRUTH_NEEDS_REVISION', 'validation role'),
    ('  candidate1_branch_role: FROZEN_SUCCESSOR_OCCURRENCE_TRUTH',
     '  candidate1_branch_role: FROZEN_NEEDS_REVISION_PREDECESSOR_TO_CANDIDATE2\n  candidate2_branch_role: ACTIVE_SUCCESSOR_REPAIR_WORKSPACE_NOT_CURRENT', 'branch role'),
])

update("research/RESEARCH-START-HERE.md", [
    ('Frozen active successor candidate.1:', 'Frozen candidate.1 after independent A-S/A-P:' , 'candidate1 heading'),
    ('state    = FROZEN / NOT_CURRENT / NOT_RELEASED',
     'state    = FROZEN / NEEDS_REVISION / SUPERSEDED_BY_CANDIDATE2 / NOT_CURRENT / NOT_RELEASED', 'candidate1 state'),
    ('## Immediate next action\n\n`CANDIDATE1_FRESH_A_S_A_P`',
     '## Independent A-S/A-P result\n\nFresh A-S sealed at `2e6b46aeedc1945a03aac93620ad36aa1ccbd70f`.\n\nA-P completed at `b970148fe9596ea9cad0a2817a3b399a1d2b75f5`.\n\nPhase B reproduced four material semantic defects plus one deterministic package self-description drift. Candidate.1 is therefore `NEEDS_REVISION`; its frozen bytes remain immutable.\n\nReconciliation:\n\n`collaboration/reconciliation/2026-08-27-v037-candidate1-a-s-a-p-phase-b-reconciliation.md`\n\n## Immediate next action\n\n`CANDIDATE2_FOCUSED_SUCCESSOR_REPAIR`', 'immediate result'),
    ('Active independent intake:\n\n- Issue `#131 — Fresh independent A-S/A-P — v0.3.7 candidate.1`\n- branch `validation/v037-c1-blind-semantic-primary`',
     'Completed independent intake:\n\n- Issue `#131 — Fresh independent A-S/A-P — v0.3.7 candidate.1`\n- sealed branch `validation/v037-c1-blind-semantic-primary`', 'intake completion'),
    ('After A-P, the fresh reviewer stops before Phase B.',
     'After A-P, the fresh reviewer stopped before Phase B as required. Project-manager Phase B is now complete and candidate.2 is the active repair workspace.', 'phase b status'),
    ('## Decision after A-S/A-P', '## Candidate.2 successor repair', 'decision heading'),
    ('The project manager first verifies:\n\n- A-S seal commit;\n- A-P report commit;\n- candidate.1 frozen source/subtree unchanged;\n- Current remains v0.3.6;\n- the independent reviewer respected the declared information boundary.\n\nOnly then open author/project-manager evidence for Phase B reconciliation.\n\n```text\nmaterial candidate-byte/package defect -> candidate.2 may be required\nvalidation-interface defect alone      -> repair interface/method, not candidate identity\nno material defect                     -> do not manufacture successor for closure\n```',
     'Candidate.2 branch: `candidate/v0.3.7-candidate.2`, created from exact frozen candidate.1 source `ae6903464133cb5bcf3cd8909ecae1215fe0b9ba`.\n\nRepair only the sealed failure shapes and adjacent consistency needed to close them while retaining legitimate lightweight paths. Targeted repair/reprobe is author-side evidence, not another fresh A-S. Current remains v0.3.6.', 'decision body'),
    ('- Issue #131 = active fresh A-S/A-P intake;\n- fresh validator entry = blind semantic entry, not the full project-manager takeover context;\n- A-S must seal before A-P opens withheld candidate-local history/oracles;\n- A-P stops before Phase B;',
     '- Issue #131 = sealed A-S/A-P occurrence truth for candidate.1;\n- A-S seal = `2e6b46ae...`; A-P final = `b970148f...`;\n- candidate.1 = `NEEDS_REVISION`, immutable predecessor to candidate.2;\n- candidate.2 = active focused successor-repair workspace;\n- fresh validator entry remains blind semantic entry, not full project-manager context for any future independent intake;', 'inheritance test'),
])

update("research/BRANCH-INVENTORY.yaml", [
    ('    observed_head: "3312aabaf43d7cedf173b07a57d755ae504f2057"',
     '    observed_head: "eedb2823f3da99d7446b3d9f3600f5cf66f92b5f"', 'main observed head'),
    ('  - name: "validation/v037-c0-blind-phase-a-primary"',
     '  - name: "candidate/v0.3.7-candidate.2"\n    observed_head: "ae6903464133cb5bcf3cd8909ecae1215fe0b9ba"\n    role: ACTIVE_SUCCESSOR_REPAIR_WORKSPACE_NOT_CURRENT\n    lifecycle: ACTIVE_CANDIDATE_REPAIR\n    active_for_research_continuation: false\n    created_from_frozen_source: "ae6903464133cb5bcf3cd8909ecae1215fe0b9ba"\n    notes:\n      - "Material corrections belong here; frozen candidate.1 must not be edited in place."\n\n  - name: "validation/v037-c0-blind-phase-a-primary"', 'candidate2 branch'),
    ('    observed_head: "711a2028ae5644eefa90219e49e3f4325aadc903"\n    role: ACTIVE_FRESH_A_S_A_P_VALIDATION_INTAKE\n    lifecycle: OPEN_VALIDATION_INTAKE',
     '    observed_head: "b970148fe9596ea9cad0a2817a3b399a1d2b75f5"\n    role: SEALED_CANDIDATE1_A_S_A_P_OCCURRENCE_TRUTH\n    lifecycle: SEALED_VALIDATION_LINEAGE', 'validation sealed'),
    ('      - "Issue #131 is the active independent-validation intake."',
     '      - "Issue #131 completed A-S seal 2e6b46ae... then A-P b970148f... and stopped before Phase B."', 'validation note'),
])

print("candidate2 Phase-B control-plane transformation PASS")
