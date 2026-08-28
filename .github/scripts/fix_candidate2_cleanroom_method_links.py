#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[2]
readme = root / 'research/methodology/README.md'
changelog = root / 'research/methodology/METHOD-CHANGELOG.md'

r = readme.read_text(encoding='utf-8')
r = r.replace('PHYSICALLY-ISOLATED-INDEPENDENT-REVIEW-CARRIER.md', 'INDEPENDENT-VALIDATION-CAPSULE-CARRIER.md')
readme.write_text(r, encoding='utf-8')

c = changelog.read_text(encoding='utf-8')
c = c.replace('`research/methodology/PHYSICALLY-ISOLATED-INDEPENDENT-REVIEW-CARRIER.md`', '`research/methodology/INDEPENDENT-VALIDATION-CAPSULE-CARRIER.md`')
c = c.replace('`research/methodology/incidents/2026-08-28-CANDIDATE2-BLIND-CARRIER-LEAK-INCIDENT.md`', '`research/methodology/incidents/2026-08-28-CANDIDATE2-GITHUB-NATURAL-NAVIGATION-PRIMING-INCIDENT.md`')
old = '''Correction:\n\n```text\nPROCEDURAL_RANGED_READ != INFORMATION_BOUNDARY\nPROCEDURAL_PATH_AVOIDANCE != INFORMATION_BOUNDARY\nSEMANTIC_FAILURE_VOCABULARY != AUTHOR_ATTACK_MAP\n```'''
new = '''Correction:\n\n```text\nPROCEDURAL_RANGED_READ != INFORMATION_BOUNDARY\nPROCEDURAL_PATH_AVOIDANCE != INFORMATION_BOUNDARY\nSEMANTIC_FAILURE_VOCABULARY != AUTHOR_ATTACK_MAP\nPHYSICALLY_ISOLATED_CARRIER != ZIP\nTRANSPORT_FORMAT != METHOD\n```'''
if old not in c:
    raise SystemExit('changelog correction anchor missing')
c = c.replace(old, new, 1)
old_bullet = '- when a repository/UI cannot enforce withholding, fresh A-S uses a physically isolated deterministic semantic capsule rather than a same-repository branch UI;'
new_bullet = '- when a repository/UI cannot enforce withholding, fresh A-S uses a physically isolated review carrier rather than relying on reviewer path restraint;'
if old_bullet not in c:
    raise SystemExit('changelog practical-effect anchor missing')
c = c.replace(old_bullet, new_bullet, 1)
needle = '- authoritative candidate.2 r3 carrier audit run `33131773164` passed deterministic build, physical isolation, exact A-P frozen-package equality and payload inventory checks;\n'
addition = needle + '- ZIP remains one audited construction/transport HOW; candidate.2 now uses reusable `guytogay/independent-validation-cleanroom` as the reviewer-facing A-S HOW, with stage contents resettable between validation occurrences or future projects;\n'
if needle not in c:
    raise SystemExit('changelog cleanroom insertion anchor missing')
c = c.replace(needle, addition, 1)
changelog.write_text(c, encoding='utf-8')

joined = readme.read_text(encoding='utf-8') + '\n' + changelog.read_text(encoding='utf-8')
if 'PHYSICALLY-ISOLATED-INDEPENDENT-REVIEW-CARRIER.md' in joined:
    raise SystemExit('stale method path remains')
if 'CANDIDATE2-BLIND-CARRIER-LEAK-INCIDENT.md' in joined:
    raise SystemExit('stale incident path remains')
for required in ['INDEPENDENT-VALIDATION-CAPSULE-CARRIER.md','CANDIDATE2-GITHUB-NATURAL-NAVIGATION-PRIMING-INCIDENT.md','PHYSICALLY_ISOLATED_CARRIER != ZIP','guytogay/independent-validation-cleanroom']:
    if required not in joined:
        raise SystemExit('required method marker missing: '+required)
print('CANDIDATE2_CLEANROOM_METHOD_LINKS=PASS')
