#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACTIVE = ROOT / 'research/ACTIVE-RESEARCH.yaml'
PROGRESS = ROOT / 'research/plans/PROGRESS.yaml'
HANDOFF = ROOT / 'research/handoffs/CURRENT-HANDOFF.yaml'
START = ROOT / 'research/RESEARCH-START-HERE.md'
FILES = [ACTIVE, PROGRESS, HANDOFF, START]

OLD_RECORD = '2026-08-28-v037-candidate2-as-sealed-ap-next'
NEW_RECORD = '2026-08-28-v037-candidate2-ap-cleanroom-ready'
WRONG_AS = '28dde50c9caaeee3b5cfabf51410083dbbb05a93'
ACTUAL_AS = '28dde50c9caaeee3b5c269e28a7be5f07ac29ae5'
AS_TREE = '42debebed620bd05e6e2635409057f20b57bfa9e'
AP_COMMIT = 'aea2ed25107145a557b3fe46ca0e4b90e2b90fa9'
AP_TREE = '08ac16303d69a6a268197ac26b23c5b20972b727'
CANDIDATE_TREE = 'd5fefc8c786d7e40b3e9a59211ee7045bccee5bf'
CORRECTION = 'collaboration/reconciliation/2026-08-28-v037-candidate2-cleanroom-wrapper-identity-correction-and-ap-stage.md'
NEXT = 'RETURN_SAME_FRESH_REVIEWER_TO_CANDIDATE2_A_P_CLEAN_ROOM'

for p in FILES:
    t = p.read_text(encoding='utf-8')
    t = t.replace(OLD_RECORD, NEW_RECORD)
    t = t.replace(WRONG_AS, ACTUAL_AS)
    t = t.replace('CANDIDATE2_FROZEN_A_S_SEALED_NOT_CLEARED_A_P_NEXT_NOT_CURRENT_NOT_RELEASED',
                  'CANDIDATE2_FROZEN_A_S_SEALED_NOT_CLEARED_A_P_CLEAN_ROOM_READY_NOT_CURRENT_NOT_RELEASED')
    t = t.replace('FROZEN_A_S_SEALED_NOT_CLEARED_A_P_NEXT',
                  'FROZEN_A_S_SEALED_NOT_CLEARED_A_P_CLEAN_ROOM_READY')
    t = t.replace('A_S_SEALED_NOT_CLEARED_A_P_NEXT', 'A_S_SEALED_NOT_CLEARED_A_P_CLEAN_ROOM_READY')
    t = t.replace('PREPARE_AND_DELIVER_CANDIDATE2_A_P_TO_SAME_FRESH_REVIEWER', NEXT)
    t = t.replace('a_p_delivery_state: A_S_SEAL_SATISFIED_PREPARE_SEPARATE_A_P',
                  'a_p_delivery_state: A_P_CLEAN_ROOM_READY_NOT_STARTED')
    t = t.replace('candidate2_a_p_delivery_state: A_S_SEAL_SATISFIED_PREPARE_SEPARATE_A_P',
                  'candidate2_a_p_delivery_state: A_P_CLEAN_ROOM_READY_NOT_STARTED')
    t = t.replace('candidate2_a_p_state: NOT_STARTED', 'candidate2_a_p_state: CLEAN_ROOM_READY_NOT_STARTED')
    p.write_text(t, encoding='utf-8')

# Replace active A-S clean-room tuple with explicit A-S history plus active A-P tuple.
def inject_cleanroom_tuple(text: str) -> str:
    old = (f'  cleanroom_commit: {ACTUAL_AS}\n'
           f'  cleanroom_tree: {AS_TREE}\n'
           '  cleanroom_commit_parent_count: 0\n')
    new = (f'  a_s_cleanroom_commit: {ACTUAL_AS}\n'
           f'  a_s_cleanroom_tree: {AS_TREE}\n'
           '  a_s_cleanroom_commit_parent_count: 0\n'
           f'  a_p_cleanroom_commit: {AP_COMMIT}\n'
           f'  a_p_cleanroom_tree: {AP_TREE}\n'
           '  a_p_cleanroom_commit_parent_count: 0\n'
           f'  a_p_cleanroom_package_subtree: {CANDIDATE_TREE}\n'
           f'  cleanroom_wrapper_identity_correction_record: {CORRECTION}\n')
    if old in text:
        text = text.replace(old, new)
    return text

for p in [ACTIVE, PROGRESS, HANDOFF]:
    t = inject_cleanroom_tuple(p.read_text(encoding='utf-8'))
    p.write_text(t, encoding='utf-8')

# ACTIVE transition and next steps.
t = ACTIVE.read_text(encoding='utf-8')
t = t.replace('V0_3_7_CANDIDATE2_A_S_SEALED_NOT_CLEARED_A_P_NEXT',
              'V0_3_7_CANDIDATE2_A_P_CLEAN_ROOM_READY')
if '  a_p_cleanroom_commit:' not in t:
    anchor = '  cleanroom_branch: main\n'
    if anchor not in t:
        raise SystemExit('ACTIVE cleanroom branch anchor missing')
    t = t.replace(anchor, anchor +
                  f'  a_s_cleanroom_commit: "{ACTUAL_AS}"\n'
                  f'  a_s_cleanroom_tree: "{AS_TREE}"\n'
                  f'  a_p_cleanroom_commit: "{AP_COMMIT}"\n'
                  f'  a_p_cleanroom_tree: "{AP_TREE}"\n'
                  f'  a_p_cleanroom_package_subtree: "{CANDIDATE_TREE}"\n'
                  f'  cleanroom_wrapper_identity_correction_record: "{CORRECTION}"\n', 1)
old_step = '    - "prepare a separate A-P clean-room stage and return the same fresh reviewer only after the persisted A-S seal"\n'
new_step = '    - "return the same fresh reviewer to the separately exposed parentless A-P clean-room stage; collect report + external SHA-256 and stop before Phase B"\n'
if old_step in t:
    t = t.replace(old_step, new_step, 1)
ACTIVE.write_text(t, encoding='utf-8')

# CURRENT-HANDOFF active carrier and explicit correction/A-P readiness.
t = HANDOFF.read_text(encoding='utf-8')
t = t.replace('  active_carrier: A_S_STAGE_SEALED / PREPARING_SEPARATE_A_P_CLEAN_ROOM_STAGE\n',
              '  active_carrier: DEDICATED_CLEAN_ROOM_A_P_REPOSITORY\n')
if '  wrapper_identity_correction:' not in t:
    anchor = '  a_s_content_seal_verified_and_persisted: true\n'
    if anchor not in t:
        raise SystemExit('HANDOFF A-S seal anchor missing')
    t = t.replace(anchor, anchor +
                  '  wrapper_identity_correction: RECORDED_A_S_COMMIT_WRONG_TREE_CORRECT\n'
                  f'  wrapper_identity_correction_record: {CORRECTION}\n'
                  f'  actual_a_s_cleanroom_commit: {ACTUAL_AS}\n'
                  f'  actual_a_s_cleanroom_tree: {AS_TREE}\n'
                  f'  a_p_cleanroom_commit: {AP_COMMIT}\n'
                  f'  a_p_cleanroom_tree: {AP_TREE}\n'
                  f'  a_p_cleanroom_package_subtree: {CANDIDATE_TREE}\n'
                  '  a_p_cleanroom_ready: true\n', 1)
HANDOFF.write_text(t, encoding='utf-8')

# PROGRESS explicit A-P readiness.
t = PROGRESS.read_text(encoding='utf-8')
if '  a_p_cleanroom_ready: true' not in t:
    pos = t.find('successor_candidate2:')
    if pos < 0:
        raise SystemExit('PROGRESS successor_candidate2 missing')
    head, tail = t[:pos], t[pos:]
    anchor = '  final_a_p_report_sha256: NOT_YET_CREATED\n'
    if anchor not in tail:
        raise SystemExit('PROGRESS final A-P hash anchor missing')
    tail = tail.replace(anchor, anchor +
                        '  a_p_cleanroom_ready: true\n'
                        f'  a_p_cleanroom_commit: {AP_COMMIT}\n'
                        f'  a_p_cleanroom_tree: {AP_TREE}\n'
                        f'  a_p_cleanroom_package_subtree: {CANDIDATE_TREE}\n'
                        f'  cleanroom_wrapper_identity_correction_record: {CORRECTION}\n', 1)
    t = head + tail
PROGRESS.write_text(t, encoding='utf-8')

# START-HERE: make A-P stage the reviewer-facing next action and preserve the wrong SHA only as correction history.
t = START.read_text(encoding='utf-8')
marker = f'## Immediate next action\n\n`{NEXT}`\n'
if marker not in t:
    raise SystemExit('START A-P next-action marker missing')
if 'A-P clean-room stage is ready:' not in t:
    t = t.replace(marker, marker + f'''\nA-P clean-room stage is ready:\n\n- repository `https://github.com/guytogay/independent-validation-cleanroom`;\n- parentless A-P commit `{AP_COMMIT}`;\n- tree `{AP_TREE}`;\n- exact frozen package subtree `{CANDIDATE_TREE}`.\n\nA-S wrapper identity correction: the originally supplied SHA `{WRONG_AS}` was unresolvable; the actual parentless A-S commit is `{ACTUAL_AS}` and has the already-correct recorded tree `{AS_TREE}`. The independent A-S report remains unchanged.\n\nReturn the **same** fresh reviewer to A-P. Do not perform candidate repair or project-manager Phase B until the A-P report is returned and sealed.\n''', 1)
START.write_text(t, encoding='utf-8')

joined = '\n'.join(p.read_text(encoding='utf-8') for p in FILES)
for required in [NEW_RECORD, ACTUAL_AS, AS_TREE, AP_COMMIT, AP_TREE, CANDIDATE_TREE, CORRECTION, NEXT, 'A_P_CLEAN_ROOM_READY']:
    if required not in joined:
        raise SystemExit('missing A-P-ready control marker: ' + required)
# The wrong wrapper SHA is allowed only as historical correction narrative; it must not survive in active identity fields.
active_wrong_markers = [
    f'cleanroom_commit: {WRONG_AS}',
    f'actual_a_s_cleanroom_commit: {WRONG_AS}',
    f'a_s_cleanroom_commit: {WRONG_AS}',
]
for stale in [OLD_RECORD, 'PREPARE_AND_DELIVER_CANDIDATE2_A_P_TO_SAME_FRESH_REVIEWER', 'A_S_STAGE_SEALED / PREPARING_SEPARATE_A_P_CLEAN_ROOM_STAGE'] + active_wrong_markers:
    if stale in joined:
        raise SystemExit('stale active A-P-preparation marker remains: ' + stale)
if WRONG_AS not in START.read_text(encoding='utf-8'):
    raise SystemExit('historical wrapper correction evidence was accidentally erased')
print('CANDIDATE2_A_P_READY_CONTROL_PLANE=READY')
