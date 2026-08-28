#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OLD_AS='ee80ac827dedff7a8de9d10f0a9cbcd70c66f3b7b885296f9e2335af6ec92131'
NEW_AS='dfe15a686668440138bfd624453059d61a0b28625bb9a5e0c185b33eccf9c2da'
OLD_AP='b3e2222c591a2760b976e6791f18e2494c17063ddfe539291f1cd8799fd54bcd'
NEW_AP='427a1776aea199f5f27c4bea2827d3c827cf82fab2c8cd403da0e8cc1dd97649'
OLD_OUTER='104005b329cc042721da76a38f8a41c282c278bca3d2c424ecd7288ceeb1c357'

control_files = [
    ROOT/'research/ACTIVE-RESEARCH.yaml',
    ROOT/'research/plans/PROGRESS.yaml',
    ROOT/'research/handoffs/CURRENT-HANDOFF.yaml',
    ROOT/'research/RESEARCH-START-HERE.md',
]
method_files = [
    ROOT/'research/methodology/README.md',
    ROOT/'research/methodology/METHOD-CHANGELOG.md',
]
handoff_root = ROOT/'research/handoffs/records/2026-08-28-v037-candidate2-isolated-as-capsule-ready'
handoff_files = sorted(p for p in handoff_root.iterdir() if p.is_file())
if len(handoff_files) != 6:
    raise SystemExit(f'expected 6 retained handoff files, found {len(handoff_files)}')

# Upgrade the retained representation from superseded r3 build evidence to the
# final self-audited carrier evidence. The duplicate parallel method/handoff
# representation was already removed earlier in Git history.
for p in control_files + handoff_files:
    t = p.read_text(encoding='utf-8')
    t = t.replace('33131665994', '33131773164')
    t = t.replace(OLD_AS, NEW_AS)
    t = t.replace(OLD_AP, NEW_AP)
    t = t.replace('isolated capsule hash `ee80ac82...`', 'isolated capsule hash `dfe15a68...`')
    t = t.replace('  capsule_artifact_id: 9670480727\n',
                  '  a_s_artifact_id: 9670518379\n  a_p_artifact_id: 9670518708\n  hashes_artifact_id: 9670518979\n')
    t = t.replace('  carrier_artifact_id: 9670480727\n',
                  '  a_s_artifact_id: 9670518379\n  a_p_artifact_id: 9670518708\n  hashes_artifact_id: 9670518979\n')
    t = t.replace('  artifact_id: 9670480727\n',
                  '  a_s_artifact_id: 9670518379\n  a_p_artifact_id: 9670518708\n  hashes_artifact_id: 9670518979\n')
    t = t.replace('  outer_artifact_sha256: '+OLD_OUTER+'\n',
                  '  a_s_artifact_outer_sha256: 146c15bed53826fe8cce4738540c471127bda7c15cf5616cd20387f7e3567def\n'
                  '  a_p_artifact_outer_sha256: d5b2b1d67f300c087d3d3869e4a93148a89d75cb5d3860025bb340bcdc6c65f2\n'
                  '  hashes_artifact_outer_sha256: 8c48e9611e6f2ad57b4e353e9cce48d6dffa341bd9f918ee5647f7039061adfa\n')
    t = t.replace('artifact id `9670480727`',
                  'A-S artifact id `9670518379`, A-P artifact id `9670518708`, hashes artifact id `9670518979`')
    t = t.replace('artifact id: `9670480727`',
                  'A-S artifact id: `9670518379`; A-P artifact id: `9670518708`; hashes artifact id: `9670518979`')
    t = t.replace('outer artifact digest `'+OLD_OUTER+'`',
                  'A-S artifact outer digest `146c15bed53826fe8cce4738540c471127bda7c15cf5616cd20387f7e3567def`; A-P artifact outer digest `d5b2b1d67f300c087d3d3869e4a93148a89d75cb5d3860025bb340bcdc6c65f2`')
    t = t.replace(OLD_OUTER, '146c15bed53826fe8cce4738540c471127bda7c15cf5616cd20387f7e3567def')
    p.write_text(t, encoding='utf-8')

# Add explicit artifact split to canonical current surfaces when not already represented.
for p in control_files[:3]:
    t=p.read_text(encoding='utf-8')
    if 'a_s_artifact_id: 9670518379' not in t:
        anchor='  capsule_build_run: 33131773164\n'
        if t.count(anchor) < 1:
            raise SystemExit(f'{p}: final build-run anchor missing')
        t=t.replace(anchor, anchor+'  a_s_artifact_id: 9670518379\n  a_p_artifact_id: 9670518708\n  hashes_artifact_id: 9670518979\n', 1)
        p.write_text(t, encoding='utf-8')

# Fix methodology index/changelog links to the retained canonical representation.
for p in method_files:
    t=p.read_text(encoding='utf-8')
    t=t.replace('PHYSICALLY-ISOLATED-INDEPENDENT-REVIEW-CARRIER.md',
                'INDEPENDENT-VALIDATION-CAPSULE-CARRIER.md')
    t=t.replace('research/methodology/incidents/2026-08-28-CANDIDATE2-BLIND-CARRIER-LEAK-INCIDENT.md',
                'research/methodology/incidents/2026-08-28-CANDIDATE2-GITHUB-NATURAL-NAVIGATION-PRIMING-INCIDENT.md')
    p.write_text(t, encoding='utf-8')

# Ensure ACTIVE exposes the retained carrier method as a first-class pointer.
a=control_files[0]
t=a.read_text(encoding='utf-8')
anchor='  independent_validation_information_boundary_path: "research/methodology/INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md"\n'
if 'independent_validation_capsule_carrier_path:' not in t:
    if t.count(anchor)!=1: raise SystemExit('ACTIVE method path anchor mismatch')
    t=t.replace(anchor, anchor+'  independent_validation_capsule_carrier_path: "research/methodology/INDEPENDENT-VALIDATION-CAPSULE-CARRIER.md"\n', 1)
anchor2='  independent_validation_information_boundary: "research/methodology/INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md"\n'
if 'independent_validation_capsule_carrier:' not in t:
    if t.count(anchor2)!=1: raise SystemExit('ACTIVE project-control method anchor mismatch')
    t=t.replace(anchor2, anchor2+'  independent_validation_capsule_carrier: "research/methodology/INDEPENDENT-VALIDATION-CAPSULE-CARRIER.md"\n', 1)
a.write_text(t, encoding='utf-8')

# Final coherence assertions.
all_current = control_files + method_files + handoff_files
joined='\n'.join(p.read_text(encoding='utf-8') for p in all_current if p.exists())
for stale in [OLD_AS, OLD_AP, '33131665994', '9670480727', OLD_OUTER,
              'PHYSICALLY-ISOLATED-INDEPENDENT-REVIEW-CARRIER.md',
              'CANDIDATE2-BLIND-CARRIER-LEAK-INCIDENT.md']:
    if stale in joined:
        raise SystemExit(f'stale carrier representation remains: {stale}')
for required in [NEW_AS, NEW_AP, '33131773164', '9670518379', '9670518708', '9670518979',
                 'INDEPENDENT-VALIDATION-CAPSULE-CARRIER.md',
                 'CANDIDATE2-GITHUB-NATURAL-NAVIGATION-PRIMING-INCIDENT.md',
                 'candidate2-isolated-capsule-intake-reconciliation.md',
                 '2026-08-28-v037-candidate2-isolated-as-capsule-ready']:
    if required not in joined:
        raise SystemExit(f'final carrier authority missing: {required}')
print('CANDIDATE2_FINAL_CARRIER_REPRESENTATION=READY')
