#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACTIVE = ROOT / 'research/ACTIVE-RESEARCH.yaml'
PROGRESS = ROOT / 'research/plans/PROGRESS.yaml'
HANDOFF = ROOT / 'research/handoffs/CURRENT-HANDOFF.yaml'
START = ROOT / 'research/RESEARCH-START-HERE.md'
FILES = [ACTIVE, PROGRESS, HANDOFF, START]

OLD_RECORD = '2026-08-28-v037-candidate2-cleanroom-as-ready'
NEW_RECORD = '2026-08-28-v037-candidate2-as-sealed-ap-next'
REPORT = 'collaboration/reconciliation/2026-08-28-v037-candidate2-independent-a-s-primary-r3.md'
SEAL = 'collaboration/reconciliation/2026-08-28-v037-candidate2-independent-a-s-primary-r3-seal.yaml'
SHA256 = '0e6bb214cc3398b34c13fc6a3bebd1f548ae00ea067b4c338e8ce88f42ad955f'
BLOB = 'a8ec063fc1dcda9be70a53bf150e45ea11ac125e'
NEXT = 'PREPARE_AND_DELIVER_CANDIDATE2_A_P_TO_SAME_FRESH_REVIEWER'

# Global state/pointer replacements.
for p in FILES:
    t = p.read_text(encoding='utf-8')
    t = t.replace(OLD_RECORD, NEW_RECORD)
    t = t.replace('CANDIDATE2_FROZEN_DEDICATED_CLEAN_ROOM_A_S_READY_A_P_WITHHELD',
                  'CANDIDATE2_FROZEN_A_S_SEALED_NOT_CLEARED_A_P_NEXT_NOT_CURRENT_NOT_RELEASED')
    t = t.replace('FROZEN_DEDICATED_CLEAN_ROOM_A_S_READY_A_P_WITHHELD',
                  'FROZEN_A_S_SEALED_NOT_CLEARED_A_P_NEXT')
    t = t.replace('DEDICATED_CLEAN_ROOM_A_S_READY', 'A_S_SEALED_NOT_CLEARED_A_P_NEXT')
    t = t.replace('GET_GENUINELY_FRESH_REVIEWER_TO_RUN_CANDIDATE2_A_S_IN_DEDICATED_CLEAN_ROOM', NEXT)
    t = t.replace('a_p_delivery_state: WITHHELD_UNTIL_A_S_CONTENT_SEAL',
                  'a_p_delivery_state: A_S_SEAL_SATISFIED_PREPARE_SEPARATE_A_P')
    t = t.replace('candidate2_a_p_delivery_state: WITHHELD_UNTIL_A_S_CONTENT_SEAL',
                  'candidate2_a_p_delivery_state: A_S_SEAL_SATISFIED_PREPARE_SEPARATE_A_P')
    t = t.replace('fresh_a_s_report_sha256: NOT_YET_CREATED', f'fresh_a_s_report_sha256: {SHA256}')
    t = t.replace('candidate2_fresh_a_s_report_sha256: NOT_YET_CREATED', f'candidate2_fresh_a_s_report_sha256: {SHA256}')
    p.write_text(t, encoding='utf-8')

# ACTIVE: record sealed A-S occurrence truth and transition.
t = ACTIVE.read_text(encoding='utf-8')
t = t.replace('  event: "V0_3_7_CANDIDATE2_DEDICATED_CLEAN_ROOM_A_S_READY"',
              '  event: "V0_3_7_CANDIDATE2_A_S_SEALED_NOT_CLEARED_A_P_NEXT"')
anchor = f'  fresh_a_s_report_sha256: {SHA256}\n'
insert = (anchor +
          f'  fresh_a_s_report_path: "{REPORT}"\n'
          f'  fresh_a_s_seal_record: "{SEAL}"\n'
          f'  fresh_a_s_git_blob_sha1: "{BLOB}"\n'
          '  fresh_a_s_verdict: NOT_CLEARED\n'
          '  fresh_a_s_findings: [A-S-01, A-S-02, A-S-03, A-S-04]\n')
if 'fresh_a_s_seal_record:' not in t:
    if t.count(anchor) < 1:
        raise SystemExit('ACTIVE A-S hash anchor missing')
    t = t.replace(anchor, insert, 1)
old = '    - "send only the dedicated clean-room repository/pinned A-S state to a genuinely fresh reviewer"\n'
new = '    - "prepare a separate A-P clean-room stage and return the same fresh reviewer only after the persisted A-S seal"\n'
if old in t:
    t = t.replace(old, new, 1)
ACTIVE.write_text(t, encoding='utf-8')

# PROGRESS: record seal and A-P-next state.
t = PROGRESS.read_text(encoding='utf-8')
anchor = f'  fresh_a_s_report_sha256: {SHA256}\n'
if '  fresh_a_s_seal_record:' not in t:
    pos = t.find('successor_candidate2:')
    if pos < 0:
        raise SystemExit('PROGRESS successor_candidate2 missing')
    head, tail = t[:pos], t[pos:]
    if anchor not in tail:
        raise SystemExit('PROGRESS successor A-S hash anchor missing')
    tail = tail.replace(anchor, anchor +
                        f'  fresh_a_s_report_path: {REPORT}\n'
                        f'  fresh_a_s_seal_record: {SEAL}\n'
                        f'  fresh_a_s_git_blob_sha1: {BLOB}\n'
                        '  fresh_a_s_verdict: NOT_CLEARED\n'
                        '  fresh_a_s_findings: [A-S-01, A-S-02, A-S-03, A-S-04]\n', 1)
    t = head + tail
anchor2 = f'    candidate2_fresh_a_s_report_sha256: {SHA256}\n'
if anchor2 in t and '    candidate2_fresh_a_s_verdict:' not in t:
    t = t.replace(anchor2, anchor2 +
                  f'    candidate2_fresh_a_s_report_path: {REPORT}\n'
                  f'    candidate2_fresh_a_s_seal_record: {SEAL}\n'
                  '    candidate2_fresh_a_s_verdict: NOT_CLEARED\n'
                  '    candidate2_a_p_state: NOT_STARTED\n', 1)
PROGRESS.write_text(t, encoding='utf-8')

# CURRENT-HANDOFF: point at the new succession record and sealed evidence.
t = HANDOFF.read_text(encoding='utf-8')
anchor = f'  fresh_a_s_report_sha256: {SHA256}\n'
if '  fresh_a_s_report_path:' not in t:
    if anchor not in t:
        raise SystemExit('HANDOFF A-S hash anchor missing')
    t = t.replace(anchor, anchor +
                  f'  fresh_a_s_report_path: {REPORT}\n'
                  f'  fresh_a_s_seal_record: {SEAL}\n'
                  f'  fresh_a_s_git_blob_sha1: {BLOB}\n'
                  '  fresh_a_s_verdict: NOT_CLEARED\n'
                  '  fresh_a_s_findings: [A-S-01, A-S-02, A-S-03, A-S-04]\n'
                  '  a_s_content_seal_verified_and_persisted: true\n', 1)
t = t.replace('  active_carrier: DEDICATED_CLEAN_ROOM_REPOSITORY\n',
              '  active_carrier: A_S_STAGE_SEALED / PREPARING_SEPARATE_A_P_CLEAN_ROOM_STAGE\n')
HANDOFF.write_text(t, encoding='utf-8')

# START-HERE: replace reviewer-facing A-S next action with A-P handoff boundary.
t = START.read_text(encoding='utf-8')
old = '''## Immediate next action\n\n`GET_GENUINELY_FRESH_REVIEWER_TO_RUN_CANDIDATE2_A_S_IN_DEDICATED_CLEAN_ROOM`\n'''
new = f'''## Immediate next action\n\n`{NEXT}`\n\nFresh A-S is complete and externally content-sealed:\n\n- report `{REPORT}`;\n- SHA-256 `{SHA256}`;\n- Git blob SHA-1 `{BLOB}`;\n- verdict `NOT_CLEARED`;\n- findings `A-S-01..A-S-04`;\n- A-P `NOT_STARTED`; Phase B `NOT_STARTED`.\n\nDo not repair candidate.2 before A-P. Prepare a separately exposed A-P stage for the **same** fresh reviewer, then require that reviewer to stop before project-manager Phase B.\n'''
if old in t:
    t = t.replace(old, new, 1)
else:
    # The global replacement may already have changed the action token; add evidence immediately after it.
    marker = f'## Immediate next action\n\n`{NEXT}`\n'
    if marker not in t:
        raise SystemExit('START immediate action marker missing')
    if 'Fresh A-S is complete and externally content-sealed:' not in t:
        t = t.replace(marker, marker + f'''\nFresh A-S is complete and externally content-sealed:\n\n- report `{REPORT}`;\n- SHA-256 `{SHA256}`;\n- Git blob SHA-1 `{BLOB}`;\n- verdict `NOT_CLEARED`;\n- findings `A-S-01..A-S-04`;\n- A-P `NOT_STARTED`; Phase B `NOT_STARTED`.\n\nDo not repair candidate.2 before A-P. Prepare a separately exposed A-P stage for the **same** fresh reviewer, then require that reviewer to stop before project-manager Phase B.\n''', 1)
START.write_text(t, encoding='utf-8')

# Final assertions.
joined = '\n'.join(p.read_text(encoding='utf-8') for p in FILES)
for required in [NEW_RECORD, REPORT, SEAL, SHA256, BLOB, 'NOT_CLEARED', NEXT]:
    if required not in joined:
        raise SystemExit('missing sealed A-S control marker: ' + required)
for stale in [OLD_RECORD, 'fresh_a_s_report_sha256: NOT_YET_CREATED',
              'GET_GENUINELY_FRESH_REVIEWER_TO_RUN_CANDIDATE2_A_S_IN_DEDICATED_CLEAN_ROOM']:
    if stale in joined:
        raise SystemExit('stale pre-seal marker remains: ' + stale)
print('CANDIDATE2_A_S_SEALED_CONTROL_PLANE=READY')
