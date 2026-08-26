#!/usr/bin/env python3
"""Validate a HOW-E native Host organ rebind mapping.

Input is a Host-local mapping artifact. The validator checks source freshness,
concrete native-organ evidence, gaps, dormancy, and redundant migration. It does
not authenticate the Host evidence and does not upgrade WRITTEN mapping to
APPLIED behavior.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

TOOLS = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS))

from native_host_rebind import NativeBinding, binding_posture, mapping_posture  # noqa: E402


def load_mapping(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("mapping must be an object")
    return data


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mapping", required=True, type=Path)
    parser.add_argument("--runtime-current-tree", required=True)
    args = parser.parse_args()

    data = load_mapping(args.mapping)
    declared = data.get("source_current_tree")
    if not isinstance(declared, str) or not declared:
        raise SystemExit("source_current_tree is required")

    raw_bindings = data.get("bindings")
    if not isinstance(raw_bindings, list):
        raise SystemExit("bindings must be a list")

    bindings: list[NativeBinding] = []
    for raw in raw_bindings:
        if not isinstance(raw, dict):
            raise SystemExit("each binding must be an object")
        bindings.append(
            NativeBinding(
                property_id=str(raw.get("property_id", "")),
                status=str(raw.get("status", "")),
                native_organ=raw.get("native_organ"),
                behavior_ref=raw.get("behavior_ref"),
                material=bool(raw.get("material", True)),
                duplicate_ena_organ=bool(raw.get("duplicate_ena_organ", False)),
            )
        )

    overall = mapping_posture(declared, args.runtime_current_tree, bindings)
    print("how=HOW-E-NATIVE-HOST-REBIND")
    print(f"declared_current_tree={declared}")
    print(f"runtime_current_tree={args.runtime_current_tree}")
    print(f"mapping_posture={overall}")
    print("mapping_evidence_level=WRITTEN_INTERPRETED_ONLY")
    print("behavioral_application=UNPROVEN")

    for binding in bindings:
        print(
            "binding="
            + json.dumps(
                {
                    "property_id": binding.property_id,
                    "status": binding.status,
                    "posture": binding_posture(binding),
                },
                sort_keys=True,
            )
        )

    if overall == "NATIVE_REBIND_ACCEPTABLE":
        return 0
    if overall in {
        "STALE_REBIND_REQUIRED",
        "MAPPING_EVIDENCE_INSUFFICIENT",
        "MATERIAL_GAP_REQUIRES_ORGAN_OR_ADAPTER",
        "REDUNDANT_MIGRATION_REVIEW",
    }:
        return 1
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
