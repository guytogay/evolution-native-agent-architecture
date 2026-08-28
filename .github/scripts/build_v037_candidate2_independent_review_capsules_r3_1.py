#!/usr/bin/env python3
"""Run the candidate.2 r3 isolated capsule builder with stricter interface semantics.

Two distinctions are enforced here:
1. Generic semantic vocabulary such as "False BLOCK" belongs to the object under
   review and is not itself an author attack map.
2. A manifest cannot truthfully contain a stable hash of its own final bytes.
   Manifest self-hashes are therefore excluded by definition; every other listed
   payload file is verified, while the outer capsule ZIP is bound by SHA-256.
"""
from __future__ import annotations

import importlib.util
import json
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


def finalize_manifest(root_name: str, manifest_name: str) -> None:
    root = module.OUT / root_name
    path = root / manifest_name
    doc = json.loads(path.read_text(encoding="utf-8"))
    doc["files"] = [row for row in doc.get("files", []) if row.get("path") != manifest_name]
    doc["inventory_policy"] = {
        "manifest_self_hash": "EXCLUDED_BY_DEFINITION",
        "reason": "A final manifest cannot recursively contain a stable hash of its own final bytes.",
        "payload_file_hashes": "SHA256_VERIFIED",
        "outer_capsule_binding": "SHA256",
    }
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for row in doc["files"]:
        target = root / row["path"]
        observed = module.sha256(target)
        if observed != row["sha256"]:
            raise SystemExit(
                f"{manifest_name}: payload inventory mismatch for {row['path']}: "
                f"expected {row['sha256']} observed {observed}"
            )


def rebuild_final_capsules() -> dict[str, str]:
    finalize_manifest("candidate2-as-capsule-r3", "MANIFEST-A-S.json")
    finalize_manifest("candidate2-ap-supplement-r3", "MANIFEST-A-P.json")

    as_zip = module.OUT / "candidate2-as-capsule-r3.zip"
    ap_zip = module.OUT / "candidate2-ap-supplement-r3.zip"
    module.deterministic_zip(module.OUT / "candidate2-as-capsule-r3", as_zip)
    module.deterministic_zip(module.OUT / "candidate2-ap-supplement-r3", ap_zip)
    hashes = {
        "candidate2-as-capsule-r3.zip": module.sha256(as_zip),
        "candidate2-ap-supplement-r3.zip": module.sha256(ap_zip),
    }
    (module.OUT / "CAPSULE-HASHES.json").write_text(json.dumps(hashes, indent=2) + "\n", encoding="utf-8")
    return hashes


if __name__ == "__main__":
    print("A_S_PRIMING_DETECTOR=HISTORY_SPECIFIC")
    print("SEMANTIC_FAILURE_VOCABULARY_NE_AUTHOR_ATTACK_MAP")
    module.main()
    hashes = rebuild_final_capsules()
    print("MANIFEST_SELF_HASH_POLICY=EXCLUDED_BY_DEFINITION")
    print("PAYLOAD_INVENTORY_HASH_VERIFICATION=PASS")
    print("CANDIDATE2_REVIEW_CAPSULE_R3_FINALIZATION=PASS")
    print(json.dumps(hashes, indent=2))
