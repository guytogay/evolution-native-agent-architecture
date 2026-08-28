#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FILES = [
    ROOT/'research/ACTIVE-RESEARCH.yaml',
    ROOT/'research/plans/PROGRESS.yaml',
    ROOT/'research/handoffs/CURRENT-HANDOFF.yaml',
    ROOT/'research/RESEARCH-START-HERE.md',
]

OLD_AS='ee80ac827dedff7a8de9d10f0a9cbcd70c66f3b7b885296f9e2335af6ec92131'
NEW_AS='dfe15a686668440138bfd624453059d61a0b28625bb9a5e0c185b33eccf9c2da'
OLD_AP='b3e2222c591a2760b976e6791f18e2494c17063ddfe539291f1cd8799fd54bcd'
NEW_AP='427a1776aea199f5f27c4bea2827d3c827cf82fab2c8cd403da0e8cc1dd97649'

for p in FILES:
    t=p.read_text(encoding='utf-8')
    t=t.replace('research/methodology/INDEPENDENT-VALIDATION-CAPSULE-CARRIER.md',
                'research/methodology/PHYSICALLY-ISOLATED-INDEPENDENT-REVIEW-CARRIER.md')
    t=t.replace('research/methodology/incidents/2026-08-28-CANDIDATE2-GITHUB-NATURAL-NAVIGATION-PRIMING-INCIDENT.md',
                'research/methodology/incidents/2026-08-28-CANDIDATE2-BLIND-CARRIER-LEAK-INCIDENT.md')
    t=t.replace('collaboration/reconciliation/2026-08-28-v037-candidate2-isolated-capsule-intake-reconciliation.md',
                'collaboration/reconciliation/2026-08-28-v037-candidate2-isolated-review-capsule-r3.md')
    t=t.replace('2026-08-28-v037-candidate2-isolated-as-capsule-ready',
                '2026-08-28-v037-candidate2-isolated-as-ready')
    t=t.replace('33131665994','33131773164')
    t=t.replace(OLD_AS,NEW_AS)
    t=t.replace(OLD_AP,NEW_AP)
    t=t.replace('isolated capsule hash `ee80ac82...`','isolated capsule hash `dfe15a68...`')
    # Replace single-artifact representation from the superseded duplicate carrier.
    t=t.replace('  capsule_artifact_id: 9670480727\n',
                '  a_s_artifact_id: 9670518379\n  a_p_artifact_id: 9670518708\n  hashes_artifact_id: 9670518979\n')
    t=t.replace('  carrier_artifact_id: 9670480727\n',
                '  a_s_artifact_id: 9670518379\n  a_p_artifact_id: 9670518708\n  hashes_artifact_id: 9670518979\n')
    t=t.replace('  capsule_artifact_id: 9670480727',
                '  a_s_artifact_id: 9670518379\n  a_p_artifact_id: 9670518708\n  hashes_artifact_id: 9670518979')
    p.write_text(t,encoding='utf-8')

# Correct methodology pointer naming in ACTIVE if it has only the older information-boundary pointer.
a=FILES[0]
t=a.read_text(encoding='utf-8')
anchor='  independent_validation_information_boundary_path: "research/methodology/INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md"\n'
if 'independent_validation_capsule_carrier_path:' not in t:
    if t.count(anchor)!=1: raise SystemExit('active method-path anchor mismatch')
    t=t.replace(anchor,anchor+'  independent_validation_capsule_carrier_path: "research/methodology/PHYSICALLY-ISOLATED-INDEPENDENT-REVIEW-CARRIER.md"\n',1)
anchor2='  independent_validation_information_boundary: "research/methodology/INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md"\n'
if 'independent_validation_capsule_carrier:' not in t:
    if t.count(anchor2)!=1: raise SystemExit('active project-control method anchor mismatch')
    t=t.replace(anchor2,anchor2+'  independent_validation_capsule_carrier: "research/methodology/PHYSICALLY-ISOLATED-INDEPENDENT-REVIEW-CARRIER.md"\n',1)
a.write_text(t,encoding='utf-8')

# Hard no-stale-authority check across canonical surfaces.
joined='\n'.join(p.read_text(encoding='utf-8') for p in FILES)
for stale in [OLD_AS, OLD_AP, '33131665994', '9670480727',
              'INDEPENDENT-VALIDATION-CAPSULE-CARRIER.md',
              'CANDIDATE2-GITHUB-NATURAL-NAVIGATION-PRIMING-INCIDENT.md',
              'candidate2-isolated-capsule-intake-reconciliation.md',
              'candidate2-isolated-as-capsule-ready']:
    if stale in joined:
        raise SystemExit(f'stale duplicate carrier authority remains: {stale}')
for required in [NEW_AS, NEW_AP, '33131773164',
                 'PHYSICALLY-ISOLATED-INDEPENDENT-REVIEW-CARRIER.md',
                 '2026-08-28-v037-candidate2-isolated-as-ready']:
    if required not in joined:
        raise SystemExit(f'authoritative carrier authority missing: {required}')
print('CANDIDATE2_AUTHORITATIVE_CAPSULE_CONTROL_PLANE=READY')
