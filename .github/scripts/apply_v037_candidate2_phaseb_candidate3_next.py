#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACTIVE = ROOT / 'research/ACTIVE-RESEARCH.yaml'
PROGRESS = ROOT / 'research/plans/PROGRESS.yaml'
HANDOFF = ROOT / 'research/handoffs/CURRENT-HANDOFF.yaml'
START = ROOT / 'research/RESEARCH-START-HERE.md'
METHOD = ROOT / 'research/methodology/INDEPENDENT-VALIDATION-CAPSULE-CARRIER.md'
CHANGELOG = ROOT / 'research/methodology/METHOD-CHANGELOG.md'

OLD_RECORD = '2026-08-28-v037-candidate2-ap-cleanroom-ready'
NEW_RECORD = '2026-08-28-v037-candidate2-phaseb-needs-revision-candidate3-next'
AS_SHA = '0e6bb214cc3398b34c13fc6a3bebd1f548ae00ea067b4c338e8ce88f42ad955f'
AP_SHA = '80987d24a80c2aff90fddd96bc1891ee03c6ac02b25381d8af2a22418ebbe1db'
AP_BLOB = '2465272b73c5ad4fb3027237b886604f1c9eab5a'
AP_REPORT = 'collaboration/reconciliation/2026-08-28-v037-candidate2-independent-a-p-primary-r3.md'
AP_SEAL = 'collaboration/reconciliation/2026-08-28-v037-candidate2-independent-a-p-primary-r3-seal.yaml'
PHASE_B = 'collaboration/reconciliation/2026-08-28-v037-candidate2-a-s-a-p-phase-b-reconciliation.md'
SELF_HASH_INCIDENT = 'research/methodology/incidents/2026-08-28-INDEPENDENT-REPORT-SELF-HASH-RECURSION-INCIDENT.md'
NEXT = 'CREATE_AND_REPAIR_V0_3_7_CANDIDATE3_FROM_FROZEN_CANDIDATE2'

# ---- ACTIVE ----
t = ACTIVE.read_text(encoding='utf-8')
t = t.replace(
    'V0_3_7_CANDIDATE2_FROZEN / A_S_SEALED_NOT_CLEARED_A_P_CLEAN_ROOM_READY / A_P_WITHHELD / NOT_CURRENT / NOT_RELEASED',
    'V0_3_7_CANDIDATE2_FROZEN / A_S_SEALED / A_P_SEALED / PHASE_B_NEEDS_REVISION / CANDIDATE3_REQUIRED / NOT_CURRENT / NOT_RELEASED'
)
t = t.replace('event: "V0_3_7_CANDIDATE2_ISOLATED_REVIEW_CARRIER_R3_FINALIZED"',
              'event: "V0_3_7_CANDIDATE2_PHASE_B_NEEDS_REVISION_CANDIDATE3_REQUIRED"')
t = t.replace('a_p_delivery_state: A_P_CLEAN_ROOM_READY_NOT_STARTED', 'a_p_delivery_state: A_P_SEALED_PHASE_B_COMPLETE')
t = t.replace('fresh_candidate2_review_completed: false', 'fresh_candidate2_review_completed: true')
t = t.replace('CANDIDATE2_FROZEN_A_S_SEALED_NOT_CLEARED_A_P_CLEAN_ROOM_READY_NOT_CURRENT_NOT_RELEASED',
              'CANDIDATE2_FROZEN_A_S_SEALED_A_P_SEALED_PHASE_B_NEEDS_REVISION_CANDIDATE3_REQUIRED_NOT_CURRENT_NOT_RELEASED')
t = t.replace('FROZEN_A_S_SEALED_NOT_CLEARED_A_P_CLEAN_ROOM_READY',
              'FROZEN_A_S_SEALED_A_P_SEALED_PHASE_B_NEEDS_REVISION')
# Replace stale next-required block wholesale.
start_marker = '  next_required_steps:\n'
end_marker = '\nfrozen_candidate0:\n'
if start_marker in t and end_marker in t:
    a, rest = t.split(start_marker, 1)
    _, b = rest.split(end_marker, 1)
    t = a + start_marker + f'    - "{NEXT}"\n' + end_marker + b
if 'candidate2_phase_b:' not in t:
    t += f'''\n\ncandidate2_phase_b:\n  a_s_sha256: "{AS_SHA}"\n  a_p_report: "{AP_REPORT}"\n  a_p_seal: "{AP_SEAL}"\n  a_p_sha256: "{AP_SHA}"\n  a_p_git_blob_sha1: "{AP_BLOB}"\n  phase_b_record: "{PHASE_B}"\n  verdict: NEEDS_REVISION\n  successor_required: v0.3.7-candidate.3\n  immediate_next_action: {NEXT}\n  candidate2_mutation_forbidden: true\n  current_mutation_forbidden: true\n  full_fresh_cycle_automatic_for_candidate3: false\n'''
ACTIVE.write_text(t, encoding='utf-8')

# ---- PROGRESS ----
t = PROGRESS.read_text(encoding='utf-8')
t = t.replace(OLD_RECORD, NEW_RECORD)
t = t.replace('A_P_CLEAN_ROOM_READY_NOT_STARTED', 'A_P_SEALED_PHASE_B_COMPLETE')
t = t.replace('FROZEN_A_S_SEALED_NOT_CLEARED_A_P_CLEAN_ROOM_READY', 'FROZEN_A_S_SEALED_A_P_SEALED_PHASE_B_NEEDS_REVISION')
t = t.replace('RETURN_SAME_FRESH_REVIEWER_TO_CANDIDATE2_A_P_CLEAN_ROOM', NEXT)
t = t.replace('final_a_p_report_sha256: NOT_YET_CREATED', f'final_a_p_report_sha256: {AP_SHA}')
if 'candidate2_phase_b_complete:' not in t:
    t += f'''\n\ncandidate2_phase_b_complete:\n  a_s_sha256: {AS_SHA}\n  a_p_report: {AP_REPORT}\n  a_p_seal: {AP_SEAL}\n  a_p_sha256: {AP_SHA}\n  a_p_git_blob_sha1: {AP_BLOB}\n  phase_b_record: {PHASE_B}\n  verdict: NEEDS_REVISION\n  candidate3_required: true\n  immediate_next_action: {NEXT}\n'''
PROGRESS.write_text(t, encoding='utf-8')

# ---- CURRENT HANDOFF ----
t = HANDOFF.read_text(encoding='utf-8')
t = t.replace(OLD_RECORD, NEW_RECORD)
t = t.replace('active_carrier: DEDICATED_CLEAN_ROOM_A_P_REPOSITORY', 'active_carrier: INDEPENDENT_REVIEW_COMPLETE_CLEANROOM_OCCURRENCE_PRESERVED')
t = t.replace('a_p_delivery_state: A_P_CLEAN_ROOM_READY_NOT_STARTED', 'a_p_delivery_state: A_P_SEALED_PHASE_B_COMPLETE')
t = t.replace('final_a_p_report_sha256: NOT_YET_CREATED', f'final_a_p_report_sha256: {AP_SHA}')
t = t.replace('FROZEN_A_S_SEALED_NOT_CLEARED_A_P_CLEAN_ROOM_READY', 'FROZEN_A_S_SEALED_A_P_SEALED_PHASE_B_NEEDS_REVISION')
t = t.replace('RETURN_SAME_FRESH_REVIEWER_TO_CANDIDATE2_A_P_CLEAN_ROOM', NEXT)
if 'phase_b_reconciliation_record:' not in t:
    anchor = f'  final_a_p_report_sha256: {AP_SHA}\n'
    addition = (anchor +
                f'  final_a_p_report_path: {AP_REPORT}\n'
                f'  final_a_p_seal_record: {AP_SEAL}\n'
                f'  final_a_p_git_blob_sha1: {AP_BLOB}\n'
                f'  phase_b_reconciliation_record: {PHASE_B}\n'
                '  phase_b_verdict: NEEDS_REVISION\n'
                '  successor_required: v0.3.7-candidate.3\n')
    if anchor in t:
        t = t.replace(anchor, addition, 1)
HANDOFF.write_text(t, encoding='utf-8')

# ---- START HERE ----
t = START.read_text(encoding='utf-8')
t = t.replace('RETURN_SAME_FRESH_REVIEWER_TO_CANDIDATE2_A_P_CLEAN_ROOM', NEXT)
if 'Candidate.2 Phase B is complete:' not in t:
    marker = f'## Immediate next action\n\n`{NEXT}`\n'
    if marker not in t:
        raise SystemExit('RESEARCH-START-HERE immediate action marker missing after replacement')
    t = t.replace(marker, marker + f'''\nCandidate.2 Phase B is complete:\n\n- A-S SHA-256 `{AS_SHA}`;\n- A-P SHA-256 `{AP_SHA}`;\n- Phase-B record `{PHASE_B}`;\n- verdict `NEEDS_REVISION / CANDIDATE_3_REQUIRED`.\n\nCandidate.2 remains frozen and must not be edited. Candidate.3 must be born directly from the frozen candidate.2 source/tree and remain bounded to the sealed Phase-B repair scope. Another full fresh A-S/A-P cycle is not automatic.\n''', 1)
START.write_text(t, encoding='utf-8')

# ---- METHOD: external digest rule ----
t = METHOD.read_text(encoding='utf-8')
old = 'A Git commit can be a seal when the reviewer has an authenticated write channel. When it does not, SHA-256 of the exact completed report bytes is sufficient if computed and recorded before A-P becomes reachable.\n'
new = 'A Git commit can be a seal when the reviewer has an authenticated write channel. When it does not, SHA-256 of the exact completed report bytes is sufficient when the digest is recorded **outside the bytes being hashed** before A-P becomes reachable.\n'
if old in t:
    t = t.replace(old, new, 1)
if 'EXACT_REPORT_HASH -> EXTERNAL_DIGEST_BY_DEFAULT' not in t:
    anchor = 'The project manager later verifies the report bytes against the recorded digest and persists the occurrence into the source project\'s canonical history.\n'
    addition = anchor + f'''\nThe seal requirement itself must be satisfiable. Do not require an exact report digest to be embedded inside the same exact bytes it hashes unless an explicit deterministic normalization/exclusion rule is defined. Default to an external sidecar, seal record, or signed envelope.\n\n```text\nEXACT_REPORT_SELF_HASH_WITHOUT_NORMALIZATION = SELF_REFERENTIAL\nEXACT_REPORT_HASH -> EXTERNAL_DIGEST_BY_DEFAULT\n```\n\nIncident: `{SELF_HASH_INCIDENT}`.\n'''
    if anchor not in t:
        raise SystemExit('method A-S seal anchor missing')
    t = t.replace(anchor, addition, 1)
METHOD.write_text(t, encoding='utf-8')

# ---- METHOD CHANGELOG ----
t = CHANGELOG.read_text(encoding='utf-8')
marker = '2026-08-28 — Independent report seal recursion correction'
if marker not in t:
    t += f'''\n\n## {marker}\n\n- Fresh candidate.2 A-S exposed a validation-interface defect: the intake required an exact-file SHA-256 to be embedded inside the same exact report bytes.\n- Canonical carrier method now requires external digest/sidecar/seal-record by default unless an explicit deterministic normalization excludes the seal field.\n- A-S occurrence remains sealed; this is method/interface correction, not a candidate-byte defect.\n- Incident: `{SELF_HASH_INCIDENT}`.\n'''
CHANGELOG.write_text(t, encoding='utf-8')

# ---- Assertions ----
joined = '\n'.join(p.read_text(encoding='utf-8') for p in [ACTIVE, PROGRESS, HANDOFF, START])
for required in [NEW_RECORD, AP_SHA, AP_REPORT, AP_SEAL, PHASE_B, 'NEEDS_REVISION', 'v0.3.7-candidate.3', NEXT]:
    if required not in joined:
        raise SystemExit('missing Phase-B control marker: ' + required)
for stale in [OLD_RECORD, 'RETURN_SAME_FRESH_REVIEWER_TO_CANDIDATE2_A_P_CLEAN_ROOM', 'A_P_CLEAN_ROOM_READY_NOT_STARTED', 'final_a_p_report_sha256: NOT_YET_CREATED']:
    if stale in joined:
        raise SystemExit('stale pre-Phase-B marker remains: ' + stale)
method_text = METHOD.read_text(encoding='utf-8')
if 'EXACT_REPORT_HASH -> EXTERNAL_DIGEST_BY_DEFAULT' not in method_text:
    raise SystemExit('external report digest method rule missing')
print('CANDIDATE2_PHASE_B_CONTROL_AND_METHOD=READY')
