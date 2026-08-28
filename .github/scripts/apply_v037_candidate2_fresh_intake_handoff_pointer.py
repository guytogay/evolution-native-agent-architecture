#!/usr/bin/env python3
from pathlib import Path

p=Path(__file__).resolve().parents[2] / 'research/handoffs/CURRENT-HANDOFF.yaml'
text=p.read_text(encoding='utf-8')
old='2026-08-28-v037-candidate2-frozen-blind-view-next'
new='2026-08-28-v037-candidate2-fresh-as-intake-ready'
count=text.count(old)
if count != 7:
    raise SystemExit(f'expected 7 old handoff-record path/id occurrences, got {count}')
text=text.replace(old,new)
p.write_text(text,encoding='utf-8')
print('CANDIDATE2_FRESH_INTAKE_HANDOFF_POINTER_TRANSFORM=PASS')
