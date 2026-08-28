#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACTIVE = ROOT / 'research/ACTIVE-RESEARCH.yaml'
PROGRESS = ROOT / 'research/plans/PROGRESS.yaml'
HANDOFF = ROOT / 'research/handoffs/CURRENT-HANDOFF.yaml'
START = ROOT / 'research/RESEARCH-START-HERE.md'
FILES = [ACTIVE, PROGRESS, HANDOFF, START]

OLD_RECORD='2026-08-28-v037-candidate2-isolated-as-capsule-ready'
NEW_RECORD='2026-08-28-v037-candidate2-cleanroom-as-ready'
OLD_AS='ee80ac827dedff7a8de9d10f0a9cbcd70c66f3b7b885296f9e2335af6ec92131'
FINAL_AS='dfe15a686668440138bfd624453059d61a0b28625bb9a5e0c185b33eccf9c2da'
OLD_AP='b3e2222c591a2760b976e6791f18e2494c17063ddfe539291f1cd8799fd54bcd'
FINAL_AP='427a1776aea199f5f27c4bea2827d3c827cf82fab2c8cd403da0e8cc1dd97649'
CLEAN_REPO='guytogay/independent-validation-cleanroom'
CLEAN_URL='https://github.com/guytogay/independent-validation-cleanroom'
CLEAN_COMMIT='28dde50c9caaeee3b5cfabf51410083dbbb05a93'
CLEAN_TREE='42debebed620bd05e6e2635409057f20b57bfa9e'
NEXT='GET_GENUINELY_FRESH_REVIEWER_TO_RUN_CANDIDATE2_A_S_IN_DEDICATED_CLEAN_ROOM'

for p in FILES:
    t=p.read_text(encoding='utf-8')
    t=t.replace(OLD_RECORD, NEW_RECORD)
    t=t.replace('CANDIDATE2_FROZEN_ISOLATED_A_S_CAPSULE_READY_A_P_WITHHELD','CANDIDATE2_FROZEN_DEDICATED_CLEAN_ROOM_A_S_READY_A_P_WITHHELD')
    t=t.replace('FROZEN_ISOLATED_A_S_CAPSULE_READY_A_P_WITHHELD','FROZEN_DEDICATED_CLEAN_ROOM_A_S_READY_A_P_WITHHELD')
    t=t.replace('CANDIDATE2_FROZEN_ISOLATED_A_S_CAPSULE_READY_A_P_WITHHELD','CANDIDATE2_FROZEN_DEDICATED_CLEAN_ROOM_A_S_READY_A_P_WITHHELD')
    t=t.replace('ISOLATED_A_S_CAPSULE_READY','DEDICATED_CLEAN_ROOM_A_S_READY')
    t=t.replace('DELIVER_CANDIDATE2_ISOLATED_A_S_CAPSULE_ONLY',NEXT)
    t=t.replace('33131665994','33131773164')
    t=t.replace(OLD_AS,FINAL_AS)
    t=t.replace(OLD_AP,FINAL_AP)
    t=t.replace('isolated capsule hash `ee80ac82...`','clean-room commit `28dde50c...`')
    p.write_text(t,encoding='utf-8')

# ACTIVE: bind current reviewer-facing clean-room state while retaining capsule evidence.
t=ACTIVE.read_text(encoding='utf-8')
anchor='  carrier_reconciliation: "collaboration/reconciliation/2026-08-28-v037-candidate2-isolated-capsule-intake-reconciliation.md"\n'
insert=(anchor+
'  cleanroom_transition_record: "collaboration/reconciliation/2026-08-28-v037-candidate2-cleanroom-carrier-transition.md"\n'
'  active_a_s_delivery_mode: DEDICATED_CLEAN_ROOM_REPOSITORY\n'
'  cleanroom_repository: "'+CLEAN_REPO+'"\n'
'  cleanroom_url: "'+CLEAN_URL+'"\n'
'  cleanroom_branch: main\n'
'  cleanroom_commit: "'+CLEAN_COMMIT+'"\n'
'  cleanroom_tree: "'+CLEAN_TREE+'"\n'
'  cleanroom_commit_parent_count: 0\n')
if 'cleanroom_transition_record:' not in t:
    if t.count(anchor)!=1: raise SystemExit('ACTIVE cleanroom anchor mismatch')
    t=t.replace(anchor,insert,1)
old='    - "deliver only the isolated A-S capsule and expected SHA-256 to a genuinely fresh reviewer"\n'
new='    - "send only the dedicated clean-room repository/pinned A-S state to a genuinely fresh reviewer"\n'
if old in t: t=t.replace(old,new,1)
anchor2='  a_p_delivery_state: WITHHELD_UNTIL_A_S_CONTENT_SEAL\n'
if '  cleanroom_repository: '+CLEAN_REPO+'\n' not in t.split('successor_candidate2:',1)[-1]:
    pos=t.find('successor_candidate2:')
    tail=t[pos:]
    if tail.count(anchor2)!=1: raise SystemExit('ACTIVE candidate2 delivery anchor mismatch')
    tail=tail.replace(anchor2,anchor2+'  a_s_delivery_mode: DEDICATED_CLEAN_ROOM_REPOSITORY\n  cleanroom_repository: '+CLEAN_REPO+'\n  cleanroom_commit: '+CLEAN_COMMIT+'\n  cleanroom_tree: '+CLEAN_TREE+'\n',1)
    t=t[:pos]+tail
ACTIVE.write_text(t,encoding='utf-8')

# PROGRESS: expose clean-room as current A-S carrier HOW.
t=PROGRESS.read_text(encoding='utf-8')
anchor='  capsule_reconciliation: collaboration/reconciliation/2026-08-28-v037-candidate2-isolated-capsule-intake-reconciliation.md\n'
if '  cleanroom_transition_record:' not in t:
    if t.count(anchor)!=1: raise SystemExit('PROGRESS cleanroom anchor mismatch')
    t=t.replace(anchor,anchor+
        '  cleanroom_transition_record: collaboration/reconciliation/2026-08-28-v037-candidate2-cleanroom-carrier-transition.md\n'
        '  a_s_delivery_mode: DEDICATED_CLEAN_ROOM_REPOSITORY\n'
        '  cleanroom_repository: '+CLEAN_REPO+'\n'
        '  cleanroom_commit: '+CLEAN_COMMIT+'\n'
        '  cleanroom_tree: '+CLEAN_TREE+'\n',1)
anchor='    candidate2_a_p_delivery_state: WITHHELD_UNTIL_A_S_CONTENT_SEAL\n'
if '    candidate2_cleanroom_commit:' not in t:
    if t.count(anchor)!=1: raise SystemExit('PROGRESS independent-falsification anchor mismatch')
    t=t.replace(anchor,anchor+
        '    candidate2_a_s_delivery_mode: DEDICATED_CLEAN_ROOM_REPOSITORY\n'
        '    candidate2_cleanroom_repository: '+CLEAN_REPO+'\n'
        '    candidate2_cleanroom_commit: '+CLEAN_COMMIT+'\n'
        '    candidate2_cleanroom_tree: '+CLEAN_TREE+'\n',1)
PROGRESS.write_text(t,encoding='utf-8')

# CURRENT-HANDOFF: point succession and fresh boundary at the clean room.
t=HANDOFF.read_text(encoding='utf-8')
t=t.replace('  active_carrier: PHYSICALLY_ISOLATED_A_S_CAPSULE_R3\n','  active_carrier: DEDICATED_CLEAN_ROOM_REPOSITORY\n')
anchor='  carrier_method: research/methodology/INDEPENDENT-VALIDATION-CAPSULE-CARRIER.md\n'
if '  cleanroom_repository: '+CLEAN_REPO+'\n' not in t:
    if t.count(anchor)!=1: raise SystemExit('HANDOFF carrier anchor mismatch')
    t=t.replace(anchor,anchor+
        '  cleanroom_repository: '+CLEAN_REPO+'\n'
        '  cleanroom_url: '+CLEAN_URL+'\n'
        '  cleanroom_branch: main\n'
        '  cleanroom_commit: '+CLEAN_COMMIT+'\n'
        '  cleanroom_tree: '+CLEAN_TREE+'\n'
        '  cleanroom_commit_parent_count: 0\n',1)
t=t.replace('  immediate_next_action: DELIVER_CANDIDATE2_ISOLATED_A_S_CAPSULE_ONLY\n','  immediate_next_action: '+NEXT+'\n')
anchor2='  a_p_delivery_state: WITHHELD_UNTIL_A_S_CONTENT_SEAL\n'
pos=t.find('candidate2_successor_state:')
if pos>=0 and '  cleanroom_commit: '+CLEAN_COMMIT+'\n' not in t[pos:]:
    tail=t[pos:]
    if tail.count(anchor2)!=1: raise SystemExit('HANDOFF candidate2 anchor mismatch')
    tail=tail.replace(anchor2,anchor2+'  a_s_delivery_mode: DEDICATED_CLEAN_ROOM_REPOSITORY\n  cleanroom_repository: '+CLEAN_REPO+'\n  cleanroom_commit: '+CLEAN_COMMIT+'\n  cleanroom_tree: '+CLEAN_TREE+'\n',1)
    t=t[:pos]+tail
HANDOFF.write_text(t,encoding='utf-8')

# START-HERE: reviewer-facing next action is the clean room, while ZIP remains construction evidence.
t=START.read_text(encoding='utf-8')
start=t.index('Active carrier evidence:\n')
end=t.index('\nRequired sequence:\n', start)
new_section='''Active review carrier:\n\n- method `research/methodology/INDEPENDENT-VALIDATION-CAPSULE-CARRIER.md`;\n- dedicated clean-room repo `https://github.com/guytogay/independent-validation-cleanroom`;\n- pinned A-S commit `28dde50c9caaeee3b5cfabf51410083dbbb05a93`;\n- tree `42debebed620bd05e6e2635409057f20b57bfa9e`;\n- commit parents `[]`;\n- A-P delivery state `WITHHELD_UNTIL_A_S_CONTENT_SEAL`.\n\nThe deterministic r3 ZIP build remains construction/integrity evidence (final audit run `33131773164`, A-S package SHA-256 `dfe15a686668440138bfd624453059d61a0b28625bb9a5e0c185b33eccf9c2da`), not a requirement that the reviewer consume a ZIP.\n'''
t=t[:start]+new_section+t[end:]
old_seq='''Required sequence:\n\n```text\nFRESH REVIEWER RECEIVES ONLY A-S ZIP\n-> READ INTAKE-A-S.md INSIDE ZIP\n-> INDEPENDENT A-S\n-> WRITE FINAL A-S REPORT\n-> SHA-256 THAT EXACT REPORT\n-> STOP\n-> PROJECT MANAGER VERIFY/PERSIST CONTENT SEAL\n-> SEPARATELY DELIVER A-P ZIP TO SAME REVIEWER\n-> A-P\n-> STOP BEFORE PHASE B\n```\n\nDo not provide the project repository as A-S review material. Do not attach, link, or otherwise expose the A-P supplement before the A-S report digest is fixed.\n'''
new_seq='''Required sequence:\n\n```text\nFRESH REVIEWER RECEIVES ONLY CLEAN-ROOM URL / PINNED A-S STATE\n-> READ ROOT README / INTAKE-A-S.md\n-> FREELY BROWSE / SEARCH / EXECUTE THE CLEAN-ROOM CONTENT\n-> INDEPENDENT A-S\n-> WRITE FINAL A-S REPORT\n-> SHA-256 THAT EXACT REPORT\n-> STOP\n-> PROJECT MANAGER VERIFY/PERSIST CONTENT SEAL\n-> ONLY THEN MAKE A-P MATERIAL REACHABLE TO SAME REVIEWER\n-> A-P\n-> STOP BEFORE PHASE B\n```\n\nDo not provide the ENA project repository as A-S review context and do not expose A-P before the A-S report digest is fixed.\n'''
if old_seq not in t: raise SystemExit('START sequence anchor mismatch')
t=t.replace(old_seq,new_seq,1)
t=t.replace('active A-S carrier is isolated capsule hash `dfe15a68...`','active A-S carrier is clean-room commit `28dde50c...`')
START.write_text(t,encoding='utf-8')

# Final hard assertions across current control surfaces.
joined='\n'.join(p.read_text(encoding='utf-8') for p in FILES)
for required in [CLEAN_REPO,CLEAN_COMMIT,CLEAN_TREE,NEW_RECORD,NEXT,'DEDICATED_CLEAN_ROOM_A_S_READY']:
    if required not in joined: raise SystemExit('missing cleanroom control-plane marker: '+required)
for stale in [OLD_RECORD,OLD_AS,OLD_AP,'33131665994','DELIVER_CANDIDATE2_ISOLATED_A_S_CAPSULE_ONLY']:
    if stale in joined: raise SystemExit('stale reviewer-facing carrier marker remains: '+stale)
print('CANDIDATE2_CLEANROOM_CONTROL_PLANE=READY')
