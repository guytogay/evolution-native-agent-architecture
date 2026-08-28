#!/usr/bin/env python3
from pathlib import Path
import runpy

here = Path(__file__).resolve().parent
src = (here / 'apply_v037_candidate2_capsule_control_plane.py').read_text(encoding='utf-8')

old_section = 'next_after_candidate1_phase_a:'
new_section = 'candidate2_postfreeze_path:'
if src.count(old_section) != 2:
    raise SystemExit(f'expected two obsolete progress section anchors, found {src.count(old_section)}')
patched = src.replace(old_section, new_section)

old_call = "t=rep(t,'- candidate.2 = frozen at `bda470e0...` / `d5fefc8c...`, with fresh A-S intake Issue #137 ready on `validation/v037-c2-blind-semantic-primary`;','- candidate.2 = frozen at `bda470e0...` / `d5fefc8c...`; Issue #137 is interface-aborted history; active A-S carrier is isolated capsule hash `ee80ac82...`;')"
new_call = "t=rep(t,'- candidate.2 = frozen at `bda470e0...` / `d5fefc8c...`, with fresh A-S intake Issue #137 ready on `validation/v037-c2-blind-semantic-primary`;','- candidate.2 = frozen at `bda470e0...` / `d5fefc8c...`; Issue #137 is interface-aborted history; active A-S carrier is isolated capsule hash `ee80ac82...`;','start inheritance')"
if patched.count(old_call) != 1:
    raise SystemExit(f'expected one unlabeled Start-Here replacement, found {patched.count(old_call)}')
patched = patched.replace(old_call, new_call, 1)

temp = here / '_patched_candidate2_capsule_control_plane.py'
temp.write_text(patched, encoding='utf-8')
try:
    runpy.run_path(str(temp), run_name='__main__')
finally:
    temp.unlink(missing_ok=True)
