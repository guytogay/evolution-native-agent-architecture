#!/usr/bin/env python3
from pathlib import Path
import importlib.util
import json

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "projection_composition",
    ROOT / "evaluate_projection_composition.py",
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

doc = json.loads((ROOT / "cases.json").read_text(encoding="utf-8"))
results = module.evaluate_document(doc)
by_id = {result["case_id"]: result for result in results}

failed = []
for case in doc["cases"]:
    case_id = case["case_id"]
    expected = case["expected"]
    actual = by_id[case_id]["outcome"]
    if by_id[case_id]["errors"]:
        failed.append(
            (case_id, "unexpected evaluator errors", by_id[case_id]["errors"])
        )
    elif actual != expected:
        failed.append((case_id, expected, actual))

if failed:
    print("PROJECTION_COMPOSITION_01_SELFTEST_FAIL")
    for failure in failed:
        print(failure)
    raise SystemExit(1)

print(f"PROJECTION_COMPOSITION_01_SELFTEST_PASS {len(doc['cases'])}")
