#!/usr/bin/env python3
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[2]
ACTIVE=ROOT/'research/ACTIVE-RESEARCH.yaml'
PROGRESS=ROOT/'research/plans/PROGRESS.yaml'
HANDOFF=ROOT/'research/handoffs/CURRENT-HANDOFF.yaml'
START=ROOT/'research/RESEARCH-START-HERE.md'

RECORD='2026-08-28-v037-candidate3-frozen-release-preparation'
SOURCE='b7e88d7adb70396bd671ca97066daf2c120e0adc'
TREE='e3a9a20d16cecd78df7f32f19fca56e21159e810'
CURRENT_TREE='7dcbb3934883ffa6cc5292a662588cafc1533cff'
HARDENING='33152201566'
NEXT='MAIN_VISIBLE_CHECKPOINT_THEN_CREATE_RELEASE_V0_3_7_AND_TRANSPLANT_FROZEN_CANDIDATE3'
HARD_REC='collaboration/reconciliation/2026-08-28-v037-candidate3-release-hardening-reconciliation.md'
FINAL_REC='collaboration/reconciliation/2026-08-28-v037-candidate3-final-release-reconciliation.md'
FREEZE_REC='collaboration/reconciliation/2026-08-28-v037-candidate3-freeze.md'
TARGET_REC='collaboration/reconciliation/2026-08-28-v037-candidate3-targeted-postfreeze-revalidation.md'

# ACTIVE
s=ACTIVE.read_text()
s=s.replace('V0_3_7_CANDIDATE2_FROZEN / A_S_SEALED / A_P_SEALED / PHASE_B_NEEDS_REVISION / CANDIDATE3_REQUIRED / NOT_CURRENT / NOT_RELEASED',
'''V0_3_7_CANDIDATE3_FROZEN / EXACT_PREFREEZE_PASS / TARGETED_POSTFREEZE_PASS / RELEASE_HARDENING_PASS / CANDIDATE_SUCCESSION_STOP / RELEASE_PREPARATION_SUPPORTED / NOT_CURRENT / NOT_RELEASED''')
latest=f'''latest_transition:\n  event: "V0_3_7_CANDIDATE3_RELEASE_HARDENING_PASS_RELEASE_PREPARATION_SUPPORTED"\n  current_changed_by_transition: false\n  next_version: "v0.3.7"\n  active_candidate_identity: "v0.3.7-candidate.3"\n  active_candidate_branch: "candidate/v0.3.7-candidate.3"\n  candidate_state: FROZEN_NOT_CURRENT_NOT_RELEASED\n  exact_prefreeze_run: 33150269264\n  targeted_postfreeze_run: 33150553992\n  release_hardening_run: {HARDENING}\n  frozen_source: "{SOURCE}"\n  frozen_subtree: "{TREE}"\n  current_subtree_same_source: "{CURRENT_TREE}"\n  freeze_record: "{FREEZE_REC}"\n  targeted_postfreeze_record: "{TARGET_REC}"\n  final_release_reconciliation: "{FINAL_REC}"\n  release_hardening_reconciliation: "{HARD_REC}"\n  candidate_succession_stop: true\n  release_preparation_supported: true\n  candidate4_currently_justified: false\n  attack_cardinality: OPEN\n  immediate_next_action: {NEXT}\n\n'''
s,n=re.subn(r'latest_transition:\n.*?\ncandidate_validation_transition:\n',latest+'candidate_validation_transition:\n',s,flags=re.S)
if n!=1: raise SystemExit(f'ACTIVE latest transition replacement count={n}')
cv=f'''candidate_validation_transition:\n  current_state: CANDIDATE3_FROZEN_RELEASE_HARDENING_PASS_RELEASE_PREPARATION_SUPPORTED_NOT_CURRENT_NOT_RELEASED\n  completed:\n    - candidate.0, candidate.1, and candidate.2 remain immutable predecessor occurrence truth\n    - candidate.2 fresh A-S/A-P Phase B required bounded candidate.3 repair\n    - candidate.3 exact pre-freeze run 33150269264 PASS\n    - candidate.3 external freeze binds source {SOURCE} / subtree {TREE}\n    - targeted post-freeze run 33150553992 closed all six candidate.2 Phase-B material repair classes\n    - release hardening run {HARDENING} PASS without a demonstrated material frozen candidate-byte defect\n    - candidate succession stop reaffirmed; candidate.4 is not justified by current evidence\n  next_required_steps:\n    - "{NEXT}"\n\n'''
s,n=re.subn(r'candidate_validation_transition:\n.*?\nfrozen_candidate0:\n',cv+'frozen_candidate0:\n',s,flags=re.S)
if n!=1: raise SystemExit(f'ACTIVE candidate transition replacement count={n}')
if 'successor_candidate3:' not in s:
    s += f'''\n\nsuccessor_candidate3:\n  identity: "v0.3.7-candidate.3"\n  branch: "candidate/v0.3.7-candidate.3"\n  state: FROZEN_RELEASE_HARDENING_PASS_RELEASE_PREPARATION_SUPPORTED\n  frozen: true\n  current: false\n  released: false\n  frozen_source: "{SOURCE}"\n  frozen_subtree: "{TREE}"\n  exact_prefreeze_run: 33150269264\n  targeted_postfreeze_run: 33150553992\n  release_hardening_run: {HARDENING}\n  candidate_succession_stop: true\n  candidate4_currently_justified: false\n  immediate_next_action: {NEXT}\n'''
ACTIVE.write_text(s)

# PROGRESS
s=PROGRESS.read_text()
s=re.sub(r'^status: .*$', 'status: V0_3_7_CANDIDATE3_FROZEN_RELEASE_HARDENING_PASS_RELEASE_PREPARATION_SUPPORTED_NOT_CURRENT_NOT_RELEASED', s, count=1, flags=re.M)
if 'candidate3_release_preparation:' not in s:
    s += f'''\n\ncandidate3_release_preparation:\n  identity: v0.3.7-candidate.3\n  frozen_source_commit: {SOURCE}\n  frozen_candidate_subtree: {TREE}\n  current_subtree_same_source: {CURRENT_TREE}\n  exact_prefreeze_run: 33150269264\n  targeted_postfreeze_run: 33150553992\n  release_hardening_run: {HARDENING}\n  freeze_record: {FREEZE_REC}\n  targeted_postfreeze_record: {TARGET_REC}\n  final_release_reconciliation: {FINAL_REC}\n  release_hardening_reconciliation: {HARD_REC}\n  candidate_succession_stop: true\n  release_preparation_supported: true\n  candidate4_currently_justified: false\n  release_packaging_rule: BYTE_EXACT_TRANSPLANT_THEN_IDENTITY_ONLY_TRANSFORM\n  immediate_next_action: {NEXT}\n  attack_cardinality: OPEN\n'''
else:
    raise SystemExit('PROGRESS candidate3_release_preparation already exists; refuse ambiguous update')
PROGRESS.write_text(s)

# CURRENT HANDOFF: switch the active record and replace completed fresh-review block with release state.
s=HANDOFF.read_text()
record=f'''current_handoff_record:\n  id: "{RECORD}"\n  state: HANDOFF_READY_FOR_SESSION_SUCCESSION\n  record_root: "research/handoffs/records/{RECORD}/"\n  start_here: "research/handoffs/records/{RECORD}/HANDOFF-START-HERE.md"\n  manifest: "research/handoffs/records/{RECORD}/HANDOFF-MANIFEST.yaml"\n  project_state: "research/handoffs/records/{RECORD}/PROJECT-STATE.md"\n  recent_three_rounds: "research/handoffs/records/{RECORD}/RECENT-THREE-ROUNDS.md"\n  file_catalog: "research/handoffs/records/{RECORD}/FILE-CATALOG.md"\n  post_merge_readback: "research/handoffs/records/{RECORD}/HANDOFF-READBACK.md"\n\n'''
s,n=re.subn(r'current_handoff_record:\n.*?\ncurrent_project_authorities:\n',record+'current_project_authorities:\n',s,flags=re.S)
if n!=1: raise SystemExit(f'HANDOFF current record replacement count={n}')
release_block=f'''release_preparation_boundary:\n  active_target_identity: v0.3.7-candidate.3\n  frozen_source: {SOURCE}\n  frozen_subtree: {TREE}\n  current_subtree: {CURRENT_TREE}\n  exact_prefreeze_run: 33150269264\n  targeted_postfreeze_run: 33150553992\n  release_hardening_run: {HARDENING}\n  candidate_succession_stop: true\n  release_preparation_supported: true\n  candidate4_currently_justified: false\n  candidate_mutation_forbidden: true\n  current_mutation_before_release_merge: true\n  packaging_rule: BYTE_EXACT_TRANSPLANT_THEN_IDENTITY_ONLY_TRANSFORM\n  freeze_record: {FREEZE_REC}\n  targeted_postfreeze_record: {TARGET_REC}\n  final_release_reconciliation: {FINAL_REC}\n  release_hardening_reconciliation: {HARD_REC}\n  immediate_next_action: {NEXT}\n  attack_cardinality: OPEN\n  external_truth_established: false\n  fresh_candidate3_a_s_a_p_claimed: false\n\n'''
s,n=re.subn(r'fresh_independent_validation_boundary:\n.*?\ncompletion_evidence:\n',release_block+'completion_evidence:\n',s,flags=re.S)
if n!=1: raise SystemExit(f'HANDOFF review boundary replacement count={n}')
s=s.replace('  immediate_next_action: CREATE_AND_REPAIR_V0_3_7_CANDIDATE3_FROM_FROZEN_CANDIDATE2\n',f'  immediate_next_action: {NEXT}\n')
if 'candidate3_frozen_source:' not in s:
    anchor='completion_evidence:\n'
    addition=anchor+f'''  candidate3_frozen_source: {SOURCE}\n  candidate3_frozen_subtree: {TREE}\n  candidate3_exact_prefreeze_run: 33150269264\n  candidate3_targeted_postfreeze_run: 33150553992\n  candidate3_release_hardening_run: {HARDENING}\n  candidate3_release_preparation_supported: true\n'''
    s=s.replace(anchor,addition,1)
HANDOFF.write_text(s)

# START HERE: replace current posture through core research direction.
s=START.read_text()
posture=f'''## Current project posture\n\nCurrent remains:\n\n```text\nv0.3.6 / CURRENT / FIELD_VALIDATION\n```\n\nNext release line: `v0.3.7`.\n\nFrozen candidate lineage now culminates in:\n\n```text\ncandidate.3 = {SOURCE} / {TREE}\nstate = FROZEN / EXACT_PREFREEZE_PASS / TARGETED_POSTFREEZE_PASS / RELEASE_HARDENING_PASS\ncandidate succession = STOP\nrelease preparation = SUPPORTED\nCurrent changed = NO\n```\n\nKey evidence:\n\n- exact pre-freeze run `33150269264` — SUCCESS;\n- targeted post-freeze run `33150553992` — SUCCESS;\n- release hardening run `{HARDENING}` — SUCCESS;\n- freeze record `{FREEZE_REC}`;\n- final release reconciliation `{FINAL_REC}`;\n- release hardening reconciliation `{HARD_REC}`.\n\nThe hardening audit found no material frozen candidate-byte defect requiring candidate.4. It confirmed adopter traversal, v0.3.6 compatibility/legacy relocation, release identity projection readiness, visible evidence boundaries, 38 stable Constitution IDs, 164/164 inherited zero-flip behavior, and 61/61 successor closure behavior.\n\n`attack_cardinality = OPEN` and external/field truth remain evidence boundaries, not completeness claims.\n\n## Immediate next action\n\n`{NEXT}`\n\nRequired sequence:\n\n```text\nMAIN-VISIBLE CANDIDATE.3 CHECKPOINT\n-> CREATE release/v0.3.7 FROM EXACT MAIN\n-> BYTE-FOR-BYTE TRANSPLANT frozen candidate.3 INTO releases/current\n-> RECORD TRANSPLANT IDENTITY\n-> RELEASE IDENTITY/PACKAGING TRANSFORM ONLY\n-> EXACT RELEASE GATES + MAIN GATE + CODEQL + PACKAGE READBACK\n-> EXPLICIT RELEASE AUTHORIZATION\n-> MERGE / POST-MERGE CURRENT READBACK\n```\n\nDo not modify frozen candidate.3. Candidate.4 is permitted only if new evidence demonstrates a material defect in the frozen candidate bytes/semantics rather than in release packaging or field evidence.\n\n'''
s,n=re.subn(r'## Current project posture\n.*?\n## Core research direction\n',posture+'## Core research direction\n',s,flags=re.S)
if n!=1: raise SystemExit(f'START posture replacement count={n}')
START.write_text(s)

# Final assertions
joined='\n'.join(p.read_text() for p in [ACTIVE,PROGRESS,HANDOFF,START])
for x in [RECORD,SOURCE,TREE,HARDENING,NEXT,'RELEASE_HARDENING_PASS','RELEASE_PREPARATION_SUPPORTED']:
    if x not in joined: raise SystemExit('missing active marker '+x)
for stale in ['CREATE_AND_REPAIR_V0_3_7_CANDIDATE3_FROM_FROZEN_CANDIDATE2','A_P_CLEAN_ROOM_READY_NOT_STARTED']:
    if stale in '\n'.join([ACTIVE.read_text(),HANDOFF.read_text(),START.read_text()]):
        raise SystemExit('stale active marker remains '+stale)
print('CANDIDATE3_RELEASE_READY_CONTROL_PLANE=READY')
