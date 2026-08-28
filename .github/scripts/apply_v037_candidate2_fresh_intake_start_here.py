#!/usr/bin/env python3
from pathlib import Path

p=Path(__file__).resolve().parents[2] / 'research/RESEARCH-START-HERE.md'
text=p.read_text(encoding='utf-8')
old="""## Immediate next action

`PREPARE_CANDIDATE2_BLIND_SEMANTIC_VIEW_AND_FRESH_INTAKE`

Use the repaired blind semantic view method from:

`research/methodology/INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md`

Required sequence:

```text
EXACT FROZEN CANDIDATE.2
-> DECLARED BLIND SEMANTIC VIEW
-> FRESH A-S
-> PERSIST / SEAL A-S
-> A-P OPENS WITHHELD CANDIDATE-LOCAL HISTORY / ORACLES
-> PERSIST A-P
-> STOP FRESH REVIEWER
-> PROJECT-MANAGER PHASE B
```

Before A-S seal, do not send the fresh reviewer through the project-manager handoff, predecessor findings, candidate.2 repair narratives, author attack maps, expected fixtures, or candidate-local history/oracle surfaces declared withheld by the new view manifest.
"""
new="""## Immediate next action

`GET_GENUINELY_FRESH_REVIEWER_TO_RUN_CANDIDATE2_A_S`

Fresh intake is ready:

- Issue `#137 — Fresh independent A-S/A-P — v0.3.7 candidate.2`
- validation branch `validation/v037-c2-blind-semantic-primary`
- neutral entry `collaboration/reconciliation/2026-08-28-v037-candidate2-blind-semantic-entry.md`
- blind view `collaboration/reconciliation/2026-08-28-v037-candidate2-blind-semantic-view.yaml`
- view audit `collaboration/reconciliation/2026-08-28-v037-candidate2-blind-view-preparation.md`

The source-to-view audit found 31 declared A-S removals plus the two intake files and **zero retained candidate-byte modifications**. The view is a projection, not a new candidate.

Required sequence:

```text
FRESH REVIEWER
-> A-S ON DECLARED BLIND VIEW
-> PERSIST / SEAL A-S
-> A-P OPENS WITHHELD CANDIDATE-LOCAL HISTORY / ORACLES FROM EXACT FROZEN SOURCE
-> PERSIST A-P
-> STOP FRESH REVIEWER
-> PROJECT-MANAGER PHASE B
```

Before A-S seal, do not send the fresh reviewer through the project-manager handoff, predecessor findings, candidate.2 repair narratives, author attack maps, expected fixtures, or candidate-local history/oracle surfaces declared withheld by the view manifest. The current project-manager session is not eligible to perform fresh candidate.2 A-S.
"""
if text.count(old) != 1:
    raise SystemExit(f'immediate-action anchor count={text.count(old)}')
text=text.replace(old,new,1)
old2='- candidate.2 = frozen exact successor at `bda470e0...` / `d5fefc8c...`, fresh blind semantic view preparation next;'
new2='- candidate.2 = frozen at `bda470e0...` / `d5fefc8c...`, with fresh A-S intake Issue #137 ready on `validation/v037-c2-blind-semantic-primary`;'
if text.count(old2) != 1:
    raise SystemExit(f'inheritance anchor count={text.count(old2)}')
p.write_text(text.replace(old2,new2,1),encoding='utf-8')
print('CANDIDATE2_FRESH_INTAKE_START_HERE_TRANSFORM=PASS')
