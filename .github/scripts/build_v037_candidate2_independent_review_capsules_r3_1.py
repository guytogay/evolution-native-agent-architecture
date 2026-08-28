#!/usr/bin/env python3
"""Run the candidate.2 r3 isolated capsule builder with a history-specific priming detector.

The first r3 build gate showed that generic semantic vocabulary such as
"False BLOCK" is part of the object under review and must not itself be treated
as author search-map leakage.  A-S blindness removes prior findings, repair
lineage, author evidence and oracle/status priming; it does not remove the
contract's own vocabulary for false-positive or false-negative behavior.
"""
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

BASE = Path(__file__).with_name("build_v037_candidate2_independent_review_capsules_r3.py")
spec = importlib.util.spec_from_file_location("candidate2_capsule_r3_base", BASE)
if spec is None or spec.loader is None:
    raise SystemExit("unable to load r3 capsule builder")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

module.HIGH_SIGNAL = re.compile(
    r"candidate[ ._-]*1|NEEDS_REVISION|Phase[ -]*B|pre[- ]?freeze|author[- ]side|"
    r"prior[- ]falsifier|PR #[0-9]+|fixes P[0-9]+|REVALIDATION_BY|"
    r"INDEPENDENT_IMPLEMENTATION_VALIDATION|workflow_run_id|330[0-9]{7,}|"
    r"independent review of [0-9]|repair reconciliation|regression-results|"
    r"targeted successor revalidation|fresh Phase A .* predecessor|"
    r"falsification/repair lineage",
    re.I,
)

if __name__ == "__main__":
    print("A_S_PRIMING_DETECTOR=HISTORY_SPECIFIC")
    print("SEMANTIC_FAILURE_VOCABULARY_NE_AUTHOR_ATTACK_MAP")
    module.main()
