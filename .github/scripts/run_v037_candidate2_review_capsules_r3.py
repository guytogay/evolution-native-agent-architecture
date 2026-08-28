#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import re
from pathlib import Path

builder_path = Path(__file__).with_name('build_v037_candidate2_independent_review_capsules_r3.py')
spec = importlib.util.spec_from_file_location('ena_c2_r3_builder', builder_path)
if spec is None or spec.loader is None:
    raise SystemExit('cannot load r3 capsule builder')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

# Priming means author/history/search-map leakage, not the candidate's own
# contract vocabulary such as "false BLOCK". Do not censor semantic attack
# surfaces merely because the validator is expected to falsify them.
mod.HIGH_SIGNAL = re.compile(
    r"candidate[ ._-]*1|NEEDS_REVISION|Phase[ -]*B|pre[- ]?freeze|author[- ]side|"
    r"prior[- ]falsifier|PR #[0-9]+|fixes P[0-9]+|REVALIDATION_BY|"
    r"INDEPENDENT_IMPLEMENTATION_VALIDATION|workflow_run_id|330[0-9]{7,}|"
    r"independent review of [0-9]|repair reconciliation|regression-results",
    re.I,
)

mod.main()
