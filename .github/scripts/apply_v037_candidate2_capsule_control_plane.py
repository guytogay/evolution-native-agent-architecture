#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]


def rep(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise SystemExit(f'{label}: expected one anchor, found {n}')
    return text.replace(old, new, 1)


def sub(text, pattern, repl, label):
    out, n = re.subn(pattern, repl, text, count=1, flags=re.S)
    if n != 1:
        raise SystemExit(f'{label}: expected one regex anchor, found {n}')
    return out


def active():
    p=ROOT/'research/ACTIVE-RESEARCH.yaml'; t=p.read_text()
    t=rep(t,'  state: "V0_3_7_CANDIDATE2_FROZEN / FRESH_A_S_INTAKE_READY / NOT_CURRENT / NOT_RELEASED"','  state: "V0_3_7_CANDIDATE2_FROZEN / ISOLATED_A_S_CAPSULE_READY / A_P_WITHHELD / NOT_CURRENT / NOT_RELEASED"','active state')
    t=sub(t,r'  blind_semantic_view_preparation_next: false\n.*?  attack_cardinality: OPEN\n\ncandidate_validation_transition:', '''  invalidated_repository_intake_issue: 137
  invalidated_repository_intake_result: A_S_ABORTED_BOUNDARY_CROSSING_NOT_SEALED
  carrier_method: "research/methodology/INDEPENDENT-VALIDATION-CAPSULE-CARRIER.md"
  carrier_incident: "research/methodology/incidents/2026-08-28-CANDIDATE2-GITHUB-NATURAL-NAVIGATION-PRIMING-INCIDENT.md"
  carrier_reconciliation: "collaboration/reconciliation/2026-08-28-v037-candidate2-isolated-capsule-intake-reconciliation.md"
  capsule_build_run: 33131665994
  capsule_artifact_id: 9670480727
  a_s_capsule_sha256: "ee80ac827dedff7a8de9d10f0a9cbcd70c66f3b7b885296f9e2335af6ec92131"
  a_p_supplement_sha256: "b3e2222c591a2760b976e6791f18e2494c17063ddfe539291f1cd8799fd54bcd"
  a_p_delivery_state: WITHHELD_UNTIL_A_S_CONTENT_SEAL
  fresh_a_s_intake_ready: true
  fresh_candidate2_review_completed: false
  fresh_candidate2_review_by_current_project_manager_allowed: false
  attack_cardinality: OPEN

candidate_validation_transition:''','latest carrier')
    t=rep(t,'  current_state: CANDIDATE2_FROZEN_FRESH_A_S_INTAKE_READY','  current_state: CANDIDATE2_FROZEN_ISOLATED_A_S_CAPSULE_READY_A_P_WITHHELD','validation state')
    t=sub(t,r'  next_required_steps:\n(?:    - .*\n)+\nfrozen_candidate0:', '''  next_required_steps:
    - "deliver only the isolated A-S capsule and expected SHA-256 to a genuinely fresh reviewer"
    - "reviewer completes A-S, hashes the exact completed report, reports the digest, and stops"
    - "project manager verifies/persists A-S report + digest before separately delivering A-P supplement"
    - "same reviewer completes A-P and stops before project-manager Phase B"
    - "keep attack cardinality open and Current v0.3.6 unchanged"

frozen_candidate0:''','active next')
    t=rep(t,'  state: FROZEN_FRESH_A_S_INTAKE_READY\n  frozen: true','  state: FROZEN_ISOLATED_A_S_CAPSULE_READY_A_P_WITHHELD\n  frozen: true','candidate2 state')
    t=sub(t,r'  blind_view_manifest: "collaboration/reconciliation/2026-08-28-v037-candidate2-blind-semantic-view.yaml"\n.*?  attack_cardinality: OPEN\n\nhandoff:', '''  invalidated_repository_intake_issue: 137
  invalidated_repository_intake_branch: "validation/v037-c2-blind-semantic-primary"
  invalidated_repository_intake_result: A_S_ABORTED_BOUNDARY_CROSSING_NOT_SEALED
  capsule_carrier_method: "research/methodology/INDEPENDENT-VALIDATION-CAPSULE-CARRIER.md"
  capsule_build_run: 33131665994
  capsule_artifact_id: 9670480727
  a_s_capsule_sha256: "ee80ac827dedff7a8de9d10f0a9cbcd70c66f3b7b885296f9e2335af6ec92131"
  a_p_supplement_sha256: "b3e2222c591a2760b976e6791f18e2494c17063ddfe539291f1cd8799fd54bcd"
  a_p_delivery_state: WITHHELD_UNTIL_A_S_CONTENT_SEAL
  fresh_a_s_report_sha256: NOT_YET_CREATED
  final_a_p_report_sha256: NOT_YET_CREATED
  fresh_review_completed: false
  mutable_in_place: false
  material_change_requires_successor: "v0.3.7-candidate.3"
  attack_cardinality: OPEN

handoff:''','successor carrier')
    p.write_text(t)


def progress():
    p=ROOT/'research/plans/PROGRESS.yaml'; t=p.read_text()
    t=rep(t,'status: V0_3_7_CANDIDATE2_FROZEN_FRESH_A_S_INTAKE_READY','status: V0_3_7_CANDIDATE2_FROZEN_ISOLATED_A_S_CAPSULE_READY_A_P_WITHHELD','progress status')
    t=rep(t,'  independent_validation_information_boundary: research/methodology/INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md','  independent_validation_information_boundary: research/methodology/INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md\n  independent_validation_capsule_carrier: research/methodology/INDEPENDENT-VALIDATION-CAPSULE-CARRIER.md','progress method pointer')
    t=rep(t,'  state: FROZEN_FRESH_A_S_INTAKE_READY\n  candidate_branch: candidate/v0.3.7-candidate.2','  state: FROZEN_ISOLATED_A_S_CAPSULE_READY_A_P_WITHHELD\n  candidate_branch: candidate/v0.3.7-candidate.2','progress successor state')
    t=sub(t,r'  blind_view_manifest: collaboration/reconciliation/2026-08-28-v037-candidate2-blind-semantic-view.yaml\n.*?  attack_cardinality: OPEN\n\nphase_state:', '''  invalidated_repository_intake_issue: 137
  invalidated_repository_intake_result: A_S_ABORTED_BOUNDARY_CROSSING_NOT_SEALED
  capsule_carrier_method: research/methodology/INDEPENDENT-VALIDATION-CAPSULE-CARRIER.md
  capsule_incident: research/methodology/incidents/2026-08-28-CANDIDATE2-GITHUB-NATURAL-NAVIGATION-PRIMING-INCIDENT.md
  capsule_reconciliation: collaboration/reconciliation/2026-08-28-v037-candidate2-isolated-capsule-intake-reconciliation.md
  capsule_build_run: 33131665994
  capsule_artifact_id: 9670480727
  a_s_capsule_sha256: ee80ac827dedff7a8de9d10f0a9cbcd70c66f3b7b885296f9e2335af6ec92131
  a_p_supplement_sha256: b3e2222c591a2760b976e6791f18e2494c17063ddfe539291f1cd8799fd54bcd
  a_p_delivery_state: WITHHELD_UNTIL_A_S_CONTENT_SEAL
  fresh_a_s_report_sha256: NOT_YET_CREATED
  final_a_p_report_sha256: NOT_YET_CREATED
  attack_cardinality: OPEN

phase_state:''','progress candidate carrier')
    t=sub(t,r'  independent_falsification:\n.*?\n  handoff_framework:', '''  independent_falsification:
    state: CANDIDATE2_FROZEN_ISOLATED_A_S_CAPSULE_READY_A_P_WITHHELD
    candidate2_frozen_source: bda470e0a6b170cec61225a905957a501454a2fe
    candidate2_frozen_subtree: d5fefc8c786d7e40b3e9a59211ee7045bccee5bf
    candidate2_repository_intake_issue: 137
    candidate2_repository_intake_result: A_S_ABORTED_BOUNDARY_CROSSING_NOT_SEALED
    candidate2_capsule_build_run: 33131665994
    candidate2_a_s_capsule_sha256: ee80ac827dedff7a8de9d10f0a9cbcd70c66f3b7b885296f9e2335af6ec92131
    candidate2_a_p_supplement_sha256: b3e2222c591a2760b976e6791f18e2494c17063ddfe539291f1cd8799fd54bcd
    candidate2_a_p_delivery_state: WITHHELD_UNTIL_A_S_CONTENT_SEAL
    candidate2_fresh_review_completed: false
    current_project_manager_is_fresh_candidate2_reviewer: false
    sequence_required: A-S_CONTENT_SEAL_THEN_SEPARATE_A-P_THEN_STOP_BEFORE_PHASE_B
    attack_cardinality: OPEN

  handoff_framework:''','progress independent')
    t=sub(t,r'immediate_next_action:\n.*?\nnext_after_candidate1_phase_a:', '''immediate_next_action:
  id: DELIVER_CANDIDATE2_ISOLATED_A_S_CAPSULE_ONLY
  target: PHYSICALLY_ISOLATED_A_S_CAPSULE_R3
  objective: >-
    Give only the deterministic A-S capsule to a genuinely fresh reviewer, verify its expected
    SHA-256, obtain a completed A-S report plus content hash, and do not expose the A-P supplement
    until that content seal is verified/persisted.
  frozen_source: bda470e0a6b170cec61225a905957a501454a2fe
  frozen_subtree: d5fefc8c786d7e40b3e9a59211ee7045bccee5bf
  capsule_build_run: 33131665994
  a_s_capsule_sha256: ee80ac827dedff7a8de9d10f0a9cbcd70c66f3b7b885296f9e2335af6ec92131
  a_p_supplement_sha256: b3e2222c591a2760b976e6791f18e2494c17063ddfe539291f1cd8799fd54bcd
  a_p_delivery_state: WITHHELD
  current_must_remain: v0.3.6
  do_not_promote: true

next_after_candidate1_phase_a:''','progress next')
    p.write_text(t)


def handoff():
    p=ROOT/'research/handoffs/CURRENT-HANDOFF.yaml'; t=p.read_text()
    t=rep(t,'schema_version: "2.9"','schema_version: "3.0"','handoff schema')
    t=rep(t,'  independent_validation_information_boundary: research/methodology/INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md','  independent_validation_information_boundary: research/methodology/INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md\n  independent_validation_capsule_carrier: research/methodology/INDEPENDENT-VALIDATION-CAPSULE-CARRIER.md','handoff method pointer')
    t=sub(t,r'current_handoff_record:\n.*?\ncurrent_project_authorities:', '''current_handoff_record:
  id: "2026-08-28-v037-candidate2-isolated-as-capsule-ready"
  state: HANDOFF_READY_FOR_SESSION_SUCCESSION
  record_root: "research/handoffs/records/2026-08-28-v037-candidate2-isolated-as-capsule-ready/"
  start_here: "research/handoffs/records/2026-08-28-v037-candidate2-isolated-as-capsule-ready/HANDOFF-START-HERE.md"
  manifest: "research/handoffs/records/2026-08-28-v037-candidate2-isolated-as-capsule-ready/HANDOFF-MANIFEST.yaml"
  project_state: "research/handoffs/records/2026-08-28-v037-candidate2-isolated-as-capsule-ready/PROJECT-STATE.md"
  recent_three_rounds: "research/handoffs/records/2026-08-28-v037-candidate2-isolated-as-capsule-ready/RECENT-THREE-ROUNDS.md"
  file_catalog: "research/handoffs/records/2026-08-28-v037-candidate2-isolated-as-capsule-ready/FILE-CATALOG.md"
  post_merge_readback: "research/handoffs/records/2026-08-28-v037-candidate2-isolated-as-capsule-ready/HANDOFF-READBACK.md"

current_project_authorities:''','handoff record')
    t=sub(t,r'fresh_independent_validation_boundary:\n.*?\ncompletion_evidence:', '''fresh_independent_validation_boundary:
  active_target_identity: v0.3.7-candidate.2
  active_target_source: bda470e0a6b170cec61225a905957a501454a2fe
  active_target_subtree: d5fefc8c786d7e40b3e9a59211ee7045bccee5bf
  active_target_frozen: true
  invalidated_repository_intake_issue: 137
  invalidated_repository_intake_result: A_S_ABORTED_BOUNDARY_CROSSING_NOT_SEALED
  active_carrier: PHYSICALLY_ISOLATED_A_S_CAPSULE_R3
  carrier_method: research/methodology/INDEPENDENT-VALIDATION-CAPSULE-CARRIER.md
  carrier_build_run: 33131665994
  carrier_artifact_id: 9670480727
  a_s_capsule_sha256: ee80ac827dedff7a8de9d10f0a9cbcd70c66f3b7b885296f9e2335af6ec92131
  a_p_supplement_sha256: b3e2222c591a2760b976e6791f18e2494c17063ddfe539291f1cd8799fd54bcd
  a_p_delivery_state: WITHHELD_UNTIL_A_S_CONTENT_SEAL
  fresh_a_s_report_sha256: NOT_YET_CREATED
  final_a_p_report_sha256: NOT_YET_CREATED
  sequence: A-S_CONTENT_SEAL_THEN_SEPARATE_A-P_THEN_STOP_BEFORE_PHASE_B
  project_manager_takeover_context_is_validator_a_s_context: false
  current_project_manager_can_claim_fresh_a_s: false
  same_repository_issue_is_active_a_s_entrypoint: false
  a_s_findings_must_be_content_sealed_before_a_p: true
  independent_artifacts_must_be_persisted_before_phase_b: true

completion_evidence:''','handoff boundary')
    t=rep(t,'  candidate2_state: FROZEN_FRESH_A_S_INTAKE_READY','  candidate2_state: FROZEN_ISOLATED_A_S_CAPSULE_READY_A_P_WITHHELD','completion state')
    t=rep(t,'  candidate2_fresh_intake_issue: 137\n  immediate_next_action: GET_GENUINELY_FRESH_REVIEWER_TO_RUN_CANDIDATE2_A_S','  candidate2_invalidated_repository_intake_issue: 137\n  candidate2_capsule_build_run: 33131665994\n  candidate2_a_s_capsule_sha256: ee80ac827dedff7a8de9d10f0a9cbcd70c66f3b7b885296f9e2335af6ec92131\n  candidate2_a_p_supplement_sha256: b3e2222c591a2760b976e6791f18e2494c17063ddfe539291f1cd8799fd54bcd\n  immediate_next_action: DELIVER_CANDIDATE2_ISOLATED_A_S_CAPSULE_ONLY','completion next')
    t=sub(t,r'candidate2_successor_state:\n.*?\nbranch_hygiene:', '''candidate2_successor_state:
  identity: v0.3.7-candidate.2
  branch: candidate/v0.3.7-candidate.2
  state: FROZEN_ISOLATED_A_S_CAPSULE_READY_A_P_WITHHELD
  frozen: true
  current: false
  frozen_source: bda470e0a6b170cec61225a905957a501454a2fe
  frozen_subtree: d5fefc8c786d7e40b3e9a59211ee7045bccee5bf
  exact_prefreeze_run: 33095987843
  invalidated_repository_intake_issue: 137
  invalidated_repository_intake_result: A_S_ABORTED_BOUNDARY_CROSSING_NOT_SEALED
  capsule_carrier_method: research/methodology/INDEPENDENT-VALIDATION-CAPSULE-CARRIER.md
  capsule_build_run: 33131665994
  capsule_artifact_id: 9670480727
  a_s_capsule_sha256: ee80ac827dedff7a8de9d10f0a9cbcd70c66f3b7b885296f9e2335af6ec92131
  a_p_supplement_sha256: b3e2222c591a2760b976e6791f18e2494c17063ddfe539291f1cd8799fd54bcd
  a_p_delivery_state: WITHHELD_UNTIL_A_S_CONTENT_SEAL
  fresh_a_s_report_sha256: NOT_YET_CREATED
  final_a_p_report_sha256: NOT_YET_CREATED
  fresh_review_completed: false
  material_change_requires_successor: v0.3.7-candidate.3
  attack_cardinality: OPEN

branch_hygiene:''','handoff c2')
    t=rep(t,'  candidate2_validation_branch_role: ACTIVE_FRESH_A_S_INTAKE_VIEW_NOT_CANDIDATE_NOT_RELEASE_AUTHORITY','  candidate2_validation_branch_role: INVALIDATED_REPOSITORY_UI_INTAKE_HISTORICAL_ONLY_NO_A_S_SEAL','branch role')
    p.write_text(t)


def start_here():
    p=ROOT/'research/RESEARCH-START-HERE.md'; t=p.read_text()
    t=rep(t,'   - `INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md` while independent validation is active;','   - `INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md` while independent validation is active;\n   - `INDEPENDENT-VALIDATION-CAPSULE-CARRIER.md` when repository navigation is not blind-safe;','start method')
    t=sub(t,r'## Immediate next action\n.*?\n## Core research direction', '''## Immediate next action

`DELIVER_CANDIDATE2_ISOLATED_A_S_CAPSULE_ONLY`

Issue #137 is historical and closed. Its reviewer correctly aborted before A-S seal because normal GitHub navigation crossed the declared boundary. Do not reuse the GitHub repository/branch UI as the candidate.2 A-S carrier.

Active carrier evidence:

- method `research/methodology/INDEPENDENT-VALIDATION-CAPSULE-CARRIER.md`;
- build/audit run `33131665994` — SUCCESS;
- A-S capsule SHA-256 `ee80ac827dedff7a8de9d10f0a9cbcd70c66f3b7b885296f9e2335af6ec92131`;
- A-P supplement SHA-256 `b3e2222c591a2760b976e6791f18e2494c17063ddfe539291f1cd8799fd54bcd`;
- A-P delivery state `WITHHELD_UNTIL_A_S_CONTENT_SEAL`.

Required sequence:

```text
FRESH REVIEWER RECEIVES ONLY A-S ZIP
-> READ INTAKE-A-S.md INSIDE ZIP
-> INDEPENDENT A-S
-> WRITE FINAL A-S REPORT
-> SHA-256 THAT EXACT REPORT
-> STOP
-> PROJECT MANAGER VERIFY/PERSIST CONTENT SEAL
-> SEPARATELY DELIVER A-P ZIP TO SAME REVIEWER
-> A-P
-> STOP BEFORE PHASE B
```

Do not provide the project repository as A-S review material. Do not attach, link, or otherwise expose the A-P supplement before the A-S report digest is fixed.

Candidate.2 remains frozen. Material candidate-byte correction requires candidate.3.

```text
FROZEN != INDEPENDENTLY_RECONCILED != RELEASED != CURRENT
ATTACK_CARDINALITY = OPEN
```

## Core research direction''','start immediate')
    t=rep(t,'- candidate.2 = frozen at `bda470e0...` / `d5fefc8c...`, with fresh A-S intake Issue #137 ready on `validation/v037-c2-blind-semantic-primary`;','- candidate.2 = frozen at `bda470e0...` / `d5fefc8c...`; Issue #137 is interface-aborted history; active A-S carrier is isolated capsule hash `ee80ac82...`;')
    p.write_text(t)

active(); progress(); handoff(); start_here(); print('CANDIDATE2_CAPSULE_CONTROL_PLANE_READY')
