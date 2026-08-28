#!/usr/bin/env python3
from pathlib import Path
import runpy

here = Path(__file__).resolve().parent
src = (here / 'apply_v037_candidate2_capsule_control_plane.py').read_text(encoding='utf-8')
old = 'next_after_candidate1_phase_a:'
new = 'candidate2_postfreeze_path:'
if src.count(old) != 2:
    raise SystemExit(f'expected two obsolete progress section anchors, found {src.count(old)}')
patched = src.replace(old, new)
temp = here / '_patched_candidate2_capsule_control_plane.py'
temp.write_text(patched, encoding='utf-8')
try:
    runpy.run_path(str(temp), run_name='__main__')
finally:
    temp.unlink(missing_ok=True)
