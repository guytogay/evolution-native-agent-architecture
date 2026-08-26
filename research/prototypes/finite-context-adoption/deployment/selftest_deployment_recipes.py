#!/usr/bin/env python3
"""Portable deployment selftest for currently implemented adoption HOWs.

Each deployment recipe is exercised through its own CLI surface. The test does
not normalize them into one adapter interface, select a universal winner, or
treat the current HOW count as an architectural constant.
"""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parent
PY = sys.executable
CURRENT_TREE = "7dcbb3934883ffa6cc5292a662588cafc1533cff"
MERGE = "74b790741653286e0f01a1483723cdeb065ec3df"


def run(cmd: list[str], expect: int = 0) -> str:
    proc = subprocess.run(cmd, text=True, capture_output=True)
    if proc.returncode != expect:
        print(proc.stdout)
        print(proc.stderr, file=sys.stderr)
        raise AssertionError(f"expected exit {expect}, got {proc.returncode}: {' '.join(cmd)}")
    return proc.stdout


def build_fake_current(root: Path) -> None:
    files = {
        "02-SELF-POSITIONING-AND-LOCAL-PROJECTION.md": "# 2\n\n## 2.3 Five operating boundaries plus Variation Space\nbody-23\n\n## 2.5 Compiled Local Projection\nbody-25\n",
        "05-CORE-OPERATIONAL-CONTRACTS.md": "# 5\n\n## 5.1 Claim ↔ Evidence ↔ Support\nbody-51\n\n## 5.5 Capability, Route, Credential, Mandate, and Authority\nbody-55\n\n## 5.10 Governance Value and Closure\nbody-510\n",
        "09-EVOLUTION-METABOLISM.md": "# 9\n\n## 9.2 Stimulus and mutation pressure\nbody-92\n\n## 9.8 Evaluation and local selection\nbody-98\n",
    }
    root.mkdir(parents=True, exist_ok=True)
    for name, content in files.items():
        (root / name).write_text(content, encoding="utf-8")


def test_file_git(tmp: Path, current: Path) -> None:
    kernel = tmp / "kernel.md"
    kernel.write_text("# tiny resident\nrecognize material decision shapes\n", encoding="utf-8")
    install = tmp / "install-a"
    out = run([
        PY,
        str(ROOT / "install_file_git_adoption.py"),
        "--kernel", str(kernel),
        "--cold-current-root", str(current),
        "--install-root", str(install),
    ])
    assert "how=HOW-A-FILE-GIT-TINY-COLD" in out
    pointer = json.loads((install / "ena-source.json").read_text(encoding="utf-8"))
    assert pointer["current_tree"] == CURRENT_TREE
    assert (install / "ENA-RESIDENT-KERNEL.md").is_file()

    bad_current = tmp / "bad-current"
    bad_current.mkdir()
    failed = subprocess.run([
        PY,
        str(ROOT / "install_file_git_adoption.py"),
        "--kernel", str(kernel),
        "--cold-current-root", str(bad_current),
        "--install-root", str(tmp / "install-bad"),
    ], text=True, capture_output=True)
    assert failed.returncode != 0
    print("PASS deployment HOW-A: real file layout + missing canonical-source rejection")


def write_result(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def test_tool_native(tmp: Path, current: Path) -> None:
    good = tmp / "retrieval-good.json"
    write_result(good, {
        "attempted": True,
        "tool_status": "SUCCESS",
        "source_current_tree": CURRENT_TREE,
        "candidates": [{"path": "05-CORE-OPERATIONAL-CONTRACTS.md", "section": "## 5.5 Capability, Route, Credential, Mandate, and Authority"}],
    })
    out = run([
        PY,
        str(ROOT / "gate_native_retrieval_result.py"),
        "--result", str(good),
        "--canonical-root", str(current),
    ])
    assert "retrieval_status=SUCCESS" in out

    stale = tmp / "retrieval-stale.json"
    write_result(stale, {
        "attempted": True,
        "tool_status": "SUCCESS",
        "source_current_tree": "old-tree",
        "candidates": [{"path": "05-CORE-OPERATIONAL-CONTRACTS.md"}],
    })
    out = run([
        PY,
        str(ROOT / "gate_native_retrieval_result.py"),
        "--result", str(stale),
        "--canonical-root", str(current),
    ], expect=2)
    assert "STALE_OR_WRONG_SOURCE" in out

    ambiguous = tmp / "retrieval-ambiguous.json"
    write_result(ambiguous, {
        "attempted": True,
        "tool_status": "PARTIAL",
        "source_current_tree": CURRENT_TREE,
        "candidates": [
            {"path": "05-CORE-OPERATIONAL-CONTRACTS.md"},
            {"path": "09-EVOLUTION-METABOLISM.md"},
        ],
    })
    out = run([
        PY,
        str(ROOT / "gate_native_retrieval_result.py"),
        "--result", str(ambiguous),
        "--canonical-root", str(current),
    ], expect=1)
    assert "PARTIAL_AMBIGUOUS" in out
    print("PASS deployment HOW-B: native result gating + stale/ambiguous honesty")


def test_monolithic_hot(tmp: Path) -> None:
    projection = tmp / "hot.md"
    projection.write_text("# hot ENA projection\n" + ("operational semantics\n" * 300), encoding="utf-8")

    out = run([
        PY,
        str(ROOT / "inspect_monolithic_hot_projection.py"),
        "--projection", str(projection),
        "--declared-source-tree", CURRENT_TREE,
        "--projection-revision", "hot-r1",
        "--context-budget-tokens", "100000",
        "--resident-tokens", "70000",
    ])
    assert "context_fraction=0.700000" in out
    assert "material_posture=USE_HOT_BUT_MEASURE_CONTEXT_PRESSURE" in out
    assert "size_is_not_automatic_failure=true" in out

    out = run([
        PY,
        str(ROOT / "inspect_monolithic_hot_projection.py"),
        "--projection", str(projection),
        "--declared-source-tree", "old-tree",
        "--projection-revision", "hot-r0",
    ], expect=1)
    assert "freshness=STALE" in out
    print("PASS deployment HOW-C: large-hot remains valid + stale projection detected")


def test_compiled_projection(tmp: Path, current: Path) -> None:
    selection = tmp / "selection.json"
    selection.write_text(json.dumps([
        {
            "path": "05-CORE-OPERATIONAL-CONTRACTS.md",
            "section": "## 5.5 Capability, Route, Credential, Mandate, and Authority",
        },
        {
            "path": "09-EVOLUTION-METABOLISM.md",
            "section": "## 9.8 Evaluation and local selection",
        },
    ], indent=2), encoding="utf-8")
    projection = tmp / "compiled.md"
    manifest = tmp / "compiled.json"
    out = run([
        PY,
        str(ROOT / "compile_local_projection.py"),
        "--canonical-root", str(current),
        "--selection", str(selection),
        "--output", str(projection),
        "--manifest", str(manifest),
        "--current-tree", CURRENT_TREE,
        "--compiler-revision", "compiler-r1",
        "--host-profile-digest", "host-profile-A",
    ])
    assert "canonical_status=LOCAL_PROJECTION_NOT_CURRENT" in out
    text = projection.read_text(encoding="utf-8")
    assert "body-55" in text and "body-98" in text
    data = json.loads(manifest.read_text(encoding="utf-8"))
    assert data["source_current_tree"] == CURRENT_TREE
    assert len(data["selection"]) == 2

    bad_selection = tmp / "bad-selection.json"
    bad_selection.write_text(json.dumps([
        {"path": "05-CORE-OPERATIONAL-CONTRACTS.md", "section": "## DOES NOT EXIST"}
    ]), encoding="utf-8")
    proc = subprocess.run([
        PY,
        str(ROOT / "compile_local_projection.py"),
        "--canonical-root", str(current),
        "--selection", str(bad_selection),
        "--output", str(tmp / "bad.md"),
        "--manifest", str(tmp / "bad.json"),
        "--current-tree", CURRENT_TREE,
        "--compiler-revision", "compiler-r1",
        "--host-profile-digest", "host-profile-A",
    ], text=True, capture_output=True)
    assert proc.returncode != 0
    print("PASS deployment HOW-D: real section compilation + missing-section refusal")


def test_native_rebind(tmp: Path) -> None:
    good = tmp / "native-rebind-good.json"
    write_result(good, {
        "source_current_tree": CURRENT_TREE,
        "bindings": [
            {
                "property_id": "mutation_pressure",
                "status": "NATIVE_REALIZATION",
                "native_organ": "wake/metabolism scan",
                "behavior_ref": "host://wake-scan-v3",
            },
            {
                "property_id": "rescue_plane",
                "status": "PARTIAL_NATIVE_REALIZATION",
                "native_organ": "recovery-root/controller",
                "behavior_ref": "host://recovery-root-v2",
            },
            {
                "property_id": "expression_axis",
                "status": "DORMANT_NOT_DECISION_CHANGING",
                "material": False,
            },
        ],
    })
    out = run([
        PY,
        str(ROOT / "validate_native_host_rebind.py"),
        "--mapping", str(good),
        "--runtime-current-tree", CURRENT_TREE,
    ])
    assert "how=HOW-E-NATIVE-HOST-REBIND" in out
    assert "mapping_posture=NATIVE_REBIND_ACCEPTABLE" in out
    assert "behavioral_application=UNPROVEN" in out

    stale = tmp / "native-rebind-stale.json"
    write_result(stale, {
        "source_current_tree": "old-tree",
        "bindings": [
            {
                "property_id": "mutation_pressure",
                "status": "NATIVE_REALIZATION",
                "native_organ": "wake/metabolism scan",
                "behavior_ref": "host://wake-scan-v3",
            }
        ],
    })
    out = run([
        PY,
        str(ROOT / "validate_native_host_rebind.py"),
        "--mapping", str(stale),
        "--runtime-current-tree", CURRENT_TREE,
    ], expect=1)
    assert "mapping_posture=STALE_REBIND_REQUIRED" in out

    unsupported = tmp / "native-rebind-unsupported.json"
    write_result(unsupported, {
        "source_current_tree": CURRENT_TREE,
        "bindings": [
            {
                "property_id": "local_selection",
                "status": "NATIVE_REALIZATION",
                "native_organ": "evidence ceiling",
            }
        ],
    })
    out = run([
        PY,
        str(ROOT / "validate_native_host_rebind.py"),
        "--mapping", str(unsupported),
        "--runtime-current-tree", CURRENT_TREE,
    ], expect=1)
    assert "mapping_posture=MAPPING_EVIDENCE_INSUFFICIENT" in out

    gap = tmp / "native-rebind-gap.json"
    write_result(gap, {
        "source_current_tree": CURRENT_TREE,
        "bindings": [
            {
                "property_id": "effect_commitment",
                "status": "GAP",
                "material": True,
            }
        ],
    })
    out = run([
        PY,
        str(ROOT / "validate_native_host_rebind.py"),
        "--mapping", str(gap),
        "--runtime-current-tree", CURRENT_TREE,
    ], expect=1)
    assert "mapping_posture=MATERIAL_GAP_REQUIRES_ORGAN_OR_ADAPTER" in out
    print("PASS deployment HOW-E: native rebind mapping + stale/evidence/gap honesty")


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="ena-fca-deploy-") as raw:
        tmp = Path(raw)
        current = tmp / "current"
        build_fake_current(current)
        test_file_git(tmp, current)
        test_tool_native(tmp, current)
        test_monolithic_hot(tmp)
        test_compiled_projection(tmp, current)
        test_native_rebind(tmp)

    print("PASS: plural finite-context deployment recipes")
    print("verification_scope=DEPLOYMENT_RECIPE_BEHAVIOR_ONLY")
    print("currently_implemented_how_count_is_not_ontology=true")
    print("how_cardinality=OPEN")
    print("shared_adapter_framework=NOT_CREATED")
    print("universal_winner=NOT_SELECTED")
    print("current_change=NO")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
