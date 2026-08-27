#!/usr/bin/env python3
"""Tree-external anti-ablation guard for ENA v0.3.7 candidate.0.

This script protects materially distinct failure shapes that were present in the
1080-condition author harness but were not all preserved in the later
phase-aware 188-condition harness. It deliberately does not restore the old
whole-tree stale-token scan, because that scan conflated historical occurrence
truth with active structured state.

The guard is author-side validation evidence only. It is not independent
semantic falsification and does not establish external truth.
"""
from __future__ import annotations

import copy
import re
import subprocess
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parents[2]
ROOT = REPO / "releases" / "v0.3.7-candidate"
OP = ROOT / "operational"
FROZEN_SOURCE = "d0e793593184740d9732902e948afd48ed96ae2f"
FROZEN_TREE = "cffbf76fe1448b020b637c78d1f7ae46e4c0115b"

failures: list[str] = []
observed: list[str] = []


def check(condition: bool, message: str) -> None:
    if condition:
        observed.append(message)
    else:
        failures.append(message)


def load_yaml(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise AssertionError(f"expected mapping: {path}")
    return value


def route_ids(text: str) -> set[str]:
    return set(re.findall(r"^## (OA-[A-Z]+-\d+)\b", text, flags=re.MULTILINE))


def resolve_primary_path(value: str) -> Path | None:
    """Resolve the path-bearing primary syntax used by REFERENCE-INDEX.

    Descriptive entries such as "general retrieval reference via OA-RET-01"
    intentionally remain non-path values.
    """
    base = value.split("#", 1)[0]
    if base.startswith("../") or base.startswith("procedures/") or base.startswith("patterns/"):
        return (OP / base).resolve()
    if base in {"CUE-INDEX.md", "HOW-MAP.md", "REFERENCE-INDEX.yaml"}:
        return (OP / base).resolve()
    return None


def router_rule_errors(index: dict[str, Any]) -> list[str]:
    rules = index.get("rules", {})
    expected = {
        "reference_exists_implies_applicable": False,
        "reference_exists_implies_required": False,
        "host_native_equivalent_allowed": True,
        "missing_reference_may_route_to_host_pattern_or_honest_residual": True,
    }
    return [
        f"{key}: expected {expected_value!r}, got {rules.get(key)!r}"
        for key, expected_value in expected.items()
        if rules.get(key) is not expected_value
    ]


def deferred_binding_errors(index: dict[str, Any], manifest: dict[str, Any]) -> list[str]:
    routes = index.get("routes", {})
    com = routes.get("OA-COM-01", {})
    value = com.get("deferred_reference")
    bundled = {r.get("id") for r in manifest.get("references", [])}
    deferred = {r.get("id") for r in manifest.get("deferred_not_bundled_first_candidate", [])}
    errors: list[str] = []
    if not isinstance(value, str) or not value:
        errors.append("OA-COM-01 deferred_reference missing or non-string")
    else:
        if value in bundled:
            errors.append(f"OA-COM-01 deferred_reference is accidentally bundled: {value}")
        if value not in deferred:
            errors.append(f"OA-COM-01 deferred_reference is absent from durable deferred lineage: {value}")
    return errors


def old_default_tool_path_present(text: str) -> bool:
    return "`tools/ena_evolve.py`" in text


def attack_exact_frozen_binding() -> None:
    tree = subprocess.check_output(
        ["git", "rev-parse", "HEAD:releases/v0.3.7-candidate"],
        cwd=REPO,
        text=True,
    ).strip()
    check(tree == FROZEN_TREE, f"candidate subtree remains exact frozen tree {FROZEN_TREE}")

    frozen_tree = subprocess.check_output(
        ["git", "rev-parse", f"{FROZEN_SOURCE}:releases/v0.3.7-candidate"],
        cwd=REPO,
        text=True,
    ).strip()
    check(frozen_tree == FROZEN_TREE, "recorded frozen source resolves to recorded frozen subtree")

    diff = subprocess.run(
        ["git", "diff", "--quiet", FROZEN_SOURCE, "HEAD", "--", "releases/v0.3.7-candidate"],
        cwd=REPO,
        check=False,
    )
    check(diff.returncode == 0, "tree-external validator repair does not mutate frozen candidate bytes")


def attack_primary_route_targets() -> None:
    index = load_yaml(OP / "REFERENCE-INDEX.yaml")
    routes = index.get("routes", {})
    en_how = route_ids((OP / "HOW-MAP.md").read_text(encoding="utf-8"))
    root_resolved = ROOT.resolve()

    for rid, route in routes.items():
        for value in route.get("primary", []) or []:
            check(isinstance(value, str), f"{rid}: primary entry is a string")
            if not isinstance(value, str):
                continue
            p = resolve_primary_path(value)
            if p is None:
                continue
            try:
                p.relative_to(root_resolved)
                inside = True
            except ValueError:
                inside = False
            check(inside, f"{rid}: primary path stays inside candidate subtree: {value}")
            check(p.exists(), f"{rid}: primary path exists: {value}")
            if "#" in value and p.name == "HOW-MAP.md":
                anchor_route = re.search(r"oa-[a-z]+-\d+", value.lower())
                check(anchor_route is not None, f"{rid}: HOW-MAP anchor identifies an OA route")
                if anchor_route:
                    check(
                        anchor_route.group(0).upper() in en_how,
                        f"{rid}: HOW-MAP anchor resolves to an existing route",
                    )

    # Mutation sensitivity for the two independent path failure shapes.
    traversal = resolve_primary_path("../../../outside-candidate.md")
    traversal_inside = False
    if traversal is not None:
        try:
            traversal.relative_to(root_resolved)
            traversal_inside = True
        except ValueError:
            traversal_inside = False
    check(not traversal_inside, "primary-path oracle detects a deliberate candidate-subtree escape")

    missing = resolve_primary_path("../THIS-PATH-MUST-NOT-EXIST.md")
    check(missing is not None and not missing.exists(), "primary-path oracle detects a deliberate missing target")


def attack_router_policy_and_deferred_binding() -> None:
    index = load_yaml(OP / "REFERENCE-INDEX.yaml")
    manifest = load_yaml(ROOT / "references" / "REFERENCE-MANIFEST.yaml")

    check(not router_rule_errors(index), "REFERENCE-INDEX router policy preserves optional/Host-native escape semantics")
    check(not deferred_binding_errors(index, manifest), "OA-COM-01 deferred_reference is coupled to manifest deferred lineage")

    rule_mutant = copy.deepcopy(index)
    rule_mutant["rules"]["reference_exists_implies_required"] = True
    check(bool(router_rule_errors(rule_mutant)), "router-policy oracle detects forced requirement mutation")

    deferred_mutant = copy.deepcopy(index)
    deferred_mutant["routes"]["OA-COM-01"]["deferred_reference"] = "not-a-real-deferred-reference"
    check(bool(deferred_binding_errors(deferred_mutant, manifest)), "deferred-binding oracle detects route/manifest decoupling")


def attack_primary_tool_relocation_surface() -> None:
    key_paths = [
        "README.md",
        "00-READ-ME-FIRST.md",
        "RUNTIME-ADOPTION-KERNEL.md",
        "AGENT-ADOPTION-INSTRUCTION.md",
        "LITE-ADOPTION-INSTRUCTION.md",
        "09-EVOLUTION-METABOLISM.md",
        "operational/CUE-INDEX.md",
        "operational/HOW-MAP.md",
        "language-projections/zh-CN/00-READ-ME-FIRST.md",
        "language-projections/zh-CN/RUNTIME-ADOPTION-KERNEL.md",
        "language-projections/zh-CN/09-EVOLUTION-METABOLISM.md",
    ]
    for rel in key_paths:
        text = (ROOT / rel).read_text(encoding="utf-8")
        check(not old_default_tool_path_present(text), f"no stale primary `tools/ena_evolve.py` route in {rel}")

    check(
        old_default_tool_path_present("ordinary text then `tools/ena_evolve.py`"),
        "primary-tool relocation oracle detects a deliberately reintroduced stale default path",
    )


def main() -> int:
    attack_exact_frozen_binding()
    attack_primary_route_targets()
    attack_router_policy_and_deferred_binding()
    attack_primary_tool_relocation_surface()

    if failures:
        print("ANTI_ABLATION_VERDICT=FAIL")
        for item in failures:
            print(f"FAIL: {item}")
        print(f"observed_pass_conditions={len(observed)}")
        print("attack_cardinality=OPEN")
        return 1

    print("ANTI_ABLATION_VERDICT=PASS")
    print(f"observed_pass_conditions={len(observed)}")
    print("attack_cardinality=OPEN")
    print("coverage_scope=RESTORED_DISTINCT_1080_TO_188_FAILURE_SHAPES")
    print("independent_semantic_support=NOT_ESTABLISHED")
    print("external_truth=NOT_ESTABLISHED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
