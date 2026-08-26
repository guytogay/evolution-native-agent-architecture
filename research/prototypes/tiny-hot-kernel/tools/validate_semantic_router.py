#!/usr/bin/env python3
"""Validate the research-only ENA Semantic Router.

This checks represented structure and exact Current target reachability only.
It does not prove trigger quality, semantic sufficiency, salience, or safe action.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys

EXPECTED_FAMILIES = {
    "evolution-agency",
    "authority-power",
    "evidence-truth",
    "recovery-history",
    "diversity-portability",
    "composition-effects",
    "governance-evolution",
}


def main() -> int:
    here = Path(__file__).resolve()
    prototype_root = here.parents[1]
    repo_root = here.parents[4]
    router_path = prototype_root / "semantic-router.v0.1.json"

    errors: list[str] = []

    try:
        router = json.loads(router_path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"FAIL: cannot load router: {exc}")
        return 1

    families = router.get("families")
    if not isinstance(families, dict):
        errors.append("families must be an object")
        families = {}

    family_ids = set(families)
    if family_ids != EXPECTED_FAMILIES:
        errors.append(
            f"family set mismatch: expected={sorted(EXPECTED_FAMILIES)} got={sorted(family_ids)}"
        )

    target_count = 0
    section_count = 0
    for family_id, family in families.items():
        targets = family.get("targets") if isinstance(family, dict) else None
        if not isinstance(targets, list) or not targets:
            errors.append(f"{family_id}: targets must be a non-empty array")
            continue
        for target in targets:
            target_count += 1
            if not isinstance(target, dict):
                errors.append(f"{family_id}: target must be an object")
                continue
            rel_path = target.get("path")
            sections = target.get("sections")
            if not isinstance(rel_path, str) or not rel_path.startswith("releases/current/"):
                errors.append(f"{family_id}: invalid canonical target path {rel_path!r}")
                continue
            file_path = repo_root / rel_path
            if not file_path.is_file():
                errors.append(f"{family_id}: missing target file {rel_path}")
                continue
            text = file_path.read_text(encoding="utf-8")
            if not isinstance(sections, list) or not sections:
                errors.append(f"{family_id}: {rel_path} requires at least one section")
                continue
            for section in sections:
                section_count += 1
                if not isinstance(section, str) or section not in text:
                    errors.append(f"{family_id}: section not found in {rel_path}: {section!r}")

    routes = router.get("routes")
    if not isinstance(routes, list) or not routes:
        errors.append("routes must be a non-empty array")
        routes = []

    seen_routes: set[str] = set()
    for route in routes:
        if not isinstance(route, dict):
            errors.append("route must be an object")
            continue
        route_id = route.get("route_id")
        if not isinstance(route_id, str) or not route_id:
            errors.append("route_id must be a non-empty string")
            continue
        if route_id in seen_routes:
            errors.append(f"duplicate route_id: {route_id}")
        seen_routes.add(route_id)

        decision_shapes = route.get("decision_shapes")
        if not isinstance(decision_shapes, list) or not decision_shapes:
            errors.append(f"{route_id}: decision_shapes must be non-empty")

        route_families = route.get("families")
        if not isinstance(route_families, list) or not route_families:
            errors.append(f"{route_id}: families must be non-empty")
        else:
            unknown = set(route_families) - EXPECTED_FAMILIES
            if unknown:
                errors.append(f"{route_id}: unknown families {sorted(unknown)}")

        fallback = route.get("fallback")
        if not isinstance(fallback, dict) or not fallback.get("material") or not fallback.get("non_material"):
            errors.append(f"{route_id}: material/non_material fallback required")

    source = router.get("source_current", {})
    if source.get("ena_version") != "v0.3.6":
        errors.append("source_current.ena_version must be v0.3.6 for this prototype")
    if source.get("current_tree") != "7dcbb3934883ffa6cc5292a662588cafc1533cff":
        errors.append("source_current.current_tree does not match the reviewed v0.3.6 Current tree")

    print(
        "router summary:",
        f"families={len(families)}",
        f"routes={len(routes)}",
        f"targets={target_count}",
        f"sections={section_count}",
    )

    if errors:
        print(f"FAIL: {len(errors)} represented router error(s)")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: represented router structure and exact target sections are reachable")
    print("verification_scope=REPRESENTED_STRUCTURE_AND_TARGET_REACHABILITY_ONLY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
