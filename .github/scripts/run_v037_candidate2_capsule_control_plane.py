#!/usr/bin/env python3
from pathlib import Path
import runpy
import tempfile

src = Path(__file__).with_name('apply_v037_candidate2_capsule_control_plane.py').read_text(encoding='utf-8')
old = 'next_after_candidate1_phase_a:'
new = 'candidate2_postfreeze_path:'
if src.count(old) != 2:
    raise SystemExit(f'expected two obsolete progress section anchors, found {src.count(old)}')
patched = src.replace(old, new)
with tempfile.NamedTemporaryFile('w', suffix='.py', delete=False, encoding='utf-8') as f:
    f.write(patched)
    temp = f.name
runpy.run_path(temp, run_name='__main__')
