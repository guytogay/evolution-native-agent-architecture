#!/usr/bin/env python3
"""Targeted validator for ENA v0.3.8-candidate.0 adoption/product surfaces.

This validator guards represented candidate consistency only. It does not prove
external truth, future model salience, Host fitness, or bilingual behavior.
"""

from __future__ import annotations

import hashlib
from pathlib import Path
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
CURRENT = ROOT.parent / "current"


def fail(message: str) -> None:
    raise AssertionError(message)


def read(rel: str) -> str:
    p = ROOT / rel
    if not p.is_file():
        fail(f"missing candidate file: {rel}")
    return p.read_text(encoding="utf-8")


def load_yaml(rel: str):
    return yaml.safe_load(read(rel))


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("utf-8")
    return hashlib.sha1(header + data).hexdigest()


def require_all(text: str, needles: list[str], label: str) -> None:
    missing = [x for x in needles if x not in text]
    if missing:
        fail(f"{label}: missing required content: {missing}")


def forbid_all(text: str, needles: list[str], label: str) -> None:
    found = [x for x in needles if x in text]
    if found:
        fail(f"{label}: stale/forbidden narration found: {found}")


def family(doc: dict, family_id: str) -> dict:
    for item in doc.get("families", []):
        if item.get("id") == family_id:
            return item
    fail(f"missing concept-map family: {family_id}")


def main() -> int:
    required = [
        "00-READ-ME-FIRST.md",
        "README.md",
        "ADOPTER-QUICKSTART.md",
        "AGENT-ADOPTION-INSTRUCTION.md",
        "RUNTIME-ADOPTION-KERNEL.md",
        "ENFORCEMENT-MAP.yaml",
        "CURRENT-BASELINE.yaml",
        "07-ADOPTION-AND-FIELD-VALIDATION.md",
        "08-RELEASE-DISCIPLINE.md",
        "09-EVOLUTION-METABOLISM.md",
        "10-LANGUAGE-PORTABILITY.md",
        "LITE-ADOPTION-INSTRUCTION.md",
        "CONSTITUTION-CONCEPT-MAP.yaml",
        "operational/CUE-INDEX.md",
        "operational/HOW-MAP.md",
        "operational/REFERENCE-INDEX.yaml",
        "language-projections/semantic-fixtures.v3.yaml",
        "language-projections/zh-CN/RUNTIME-ADOPTION-KERNEL.md",
        "language-projections/zh-CN/09-EVOLUTION-METABOLISM.md",
        "language-projections/zh-CN/projection-manifest.yaml",
    ]
    for rel in required:
        if not (ROOT / rel).is_file():
            fail(f"missing required candidate surface: {rel}")

    # Current isolation: candidate work must not silently mutate the released baseline.
    current_baseline = CURRENT / "CURRENT-BASELINE.yaml"
    if git_blob_sha(current_baseline) != "825af4e985bd9114f6b69b145834ec050eef2a3d":
        fail("released v0.3.7 CURRENT-BASELINE.yaml bytes changed during candidate work")

    # The semantic trunk remains byte-identical to Current for candidate.0 unless scope is reopened explicitly.
    for rel in [
        "01-CONSTITUTION.md",
        "02-SELF-POSITIONING-AND-LOCAL-PROJECTION.md",
        "03-ROLES-AND-DEVELOPMENTAL-STAGES.md",
        "04-CAPABILITY-MAP.md",
    ]:
        if (ROOT / rel).read_bytes() != (CURRENT / rel).read_bytes():
            fail(f"candidate.0 unexpectedly changed inherited semantic trunk: {rel}")

    # Positive v0.3.7 machine behavior is a regression obligation unless intentionally reopened.
    for rel in [
        "tools/ena_evolve_v2.py",
        "tools/validate_evolution_record_v2.py",
        "tools/validate_contracts.py",
        "schemas/adaptation-packet.v2.schema.json",
        "schemas/evolution-record.v2.schema.json",
    ]:
        if (ROOT / rel).read_bytes() != (CURRENT / rel).read_bytes():
            fail(f"candidate.0 unexpectedly changed inherited machine path: {rel}")

    baseline = load_yaml("CURRENT-BASELINE.yaml")
    expected_baseline = {
        "ena_version": "v0.3.8-candidate.0",
        "adoption_status": "NOT_CURRENT",
        "current": False,
        "frozen": False,
        "released": False,
        "complete_adoption_baseline": False,
    }
    for key, value in expected_baseline.items():
        if baseline.get(key) != value:
            fail(f"candidate baseline {key!r} expected {value!r}, got {baseline.get(key)!r}")
    if baseline.get("current_release", {}).get("version") != "v0.3.7":
        fail("candidate baseline must point to released Current v0.3.7")

    hot_files = [
        "00-READ-ME-FIRST.md",
        "README.md",
        "ADOPTER-QUICKSTART.md",
        "AGENT-ADOPTION-INSTRUCTION.md",
        "RUNTIME-ADOPTION-KERNEL.md",
        "LITE-ADOPTION-INSTRUCTION.md",
        "07-ADOPTION-AND-FIELD-VALIDATION.md",
        "08-RELEASE-DISCIPLINE.md",
        "09-EVOLUTION-METABOLISM.md",
        "10-LANGUAGE-PORTABILITY.md",
        "language-projections/zh-CN/RUNTIME-ADOPTION-KERNEL.md",
        "language-projections/zh-CN/09-EVOLUTION-METABOLISM.md",
    ]
    stale = [
        "Do **not** adopt this directory as Current. v0.3.7 Current successor repairs",
        "Current v0.3.6 remains the only adopter-facing baseline until explicit promotion.",
        "If v0.3.7 Current is later promoted",
        "This candidate is `NOT_CURRENT / NOT_FROZEN`; the projection is therefore also a working candidate projection.",
        "Do not report that:\n\n- v0.3.7 Current is Current",
    ]
    for rel in hot_files:
        text = read(rel)
        forbid_all(text, stale, rel)

    for rel in [
        "00-READ-ME-FIRST.md",
        "README.md",
        "AGENT-ADOPTION-INSTRUCTION.md",
        "RUNTIME-ADOPTION-KERNEL.md",
        "LITE-ADOPTION-INSTRUCTION.md",
        "07-ADOPTION-AND-FIELD-VALIDATION.md",
        "08-RELEASE-DISCIPLINE.md",
        "09-EVOLUTION-METABOLISM.md",
        "10-LANGUAGE-PORTABILITY.md",
    ]:
        require_all(read(rel), ["v0.3.8-candidate.0"], rel)

    # Explicit soft/hard/external/field boundary.
    enforcement = load_yaml("ENFORCEMENT-MAP.yaml")
    required_classes = {
        "MODEL_CUE",
        "MACHINE_GUARD",
        "EXTERNAL_CONTROL_REQUIRED",
        "FIELD_EVIDENCE_REQUIRED",
    }
    classes = set((enforcement.get("classes") or {}).keys())
    if not required_classes.issubset(classes):
        fail(f"enforcement map missing classes: {sorted(required_classes - classes)}")
    if len(enforcement.get("rules") or []) < 8:
        fail("enforcement map is too thin to cover candidate high-value boundaries")

    # zh-CN hot surface must retain the decision-bearing guardrails identified by Issue #201.
    zh_hot = read("language-projections/zh-CN/RUNTIME-ADOPTION-KERNEL.md")
    require_all(
        zh_hot,
        [
            "迁移 != 本地验证",
            "局部有效/改进 != 组合后的实际结果",
            "取消 != 回滚 != 补偿",
            "完整历史",
            "持久对象存在 != 相关字节已加载 != 语义已可用",
            "reputation",
            "evidence + lineage",
            "rescue path",
            "operational/REFERENCE-INDEX.yaml",
            "默认只属于实际环境",
        ],
        "zh-CN Runtime Kernel",
    )

    projection = load_yaml("language-projections/zh-CN/projection-manifest.yaml")
    if projection.get("source_semantic_version") != "v0.3.8-candidate.0":
        fail("zh-CN projection manifest is not bound to candidate.0")
    if projection.get("not_current") is not True or projection.get("frozen") is not False:
        fail("zh-CN projection manifest has incorrect candidate status")

    # Concept-map corrections: compress text, not applicability.
    concept = load_yaml("CONSTITUTION-CONCEPT-MAP.yaml")
    diversity = family(concept, "diversity-portability")
    evidence = family(concept, "evidence-truth")
    evolution = family(concept, "evolution-agency")
    recovery = family(concept, "recovery-history")
    if "ENA-CON-035" in diversity.get("constitution_ids", []):
        fail("ENA-CON-035 remains misclassified under diversity-portability")
    if "ENA-CON-035" not in evidence.get("constitution_ids", []) and "ENA-CON-035" not in evolution.get("constitution_ids", []):
        fail("ENA-CON-035 lost availability/freshness retrieval mapping")
    if "ENA-CON-028" not in diversity.get("constitution_ids", []):
        fail("ENA-CON-028 provenance/transfer semantics missing from portability retrieval")
    recovery_cues = " ".join(recovery.get("trigger_cues", []))
    for cue in ["compaction", "reclassification", "append-only-in-meaning"]:
        if cue not in recovery_cues:
            fail(f"ENA-CON-008 applicability compression remains: missing cue {cue}")

    # Fixture coverage is requirement-based, not cardinality-as-proof.
    fixtures = load_yaml("language-projections/semantic-fixtures.v3.yaml")
    cases = fixtures.get("cases") or []
    case_ids = {case.get("id") for case in cases}
    required_case_ids = {
        "LANG-038-013-LOCAL-FITNESS-NOT-UNIVERSAL",
        "LANG-038-014-COMPOSITION-NEW-SELECTION-SUBJECT",
        "LANG-038-015-CANCEL-NOT-ROLLBACK-NOT-COMPENSATION",
        "LANG-038-016-RUNTIME-AVAILABLE-NOT-SALIENT",
        "LANG-038-017-MEMORY-METABOLISM-NOT-RAW-ACCUMULATION",
        "LANG-038-018-PROJECTION-TRUE-BUT-INCOMPLETE",
    }
    if not required_case_ids.issubset(case_ids):
        fail(f"missing candidate fixture cases: {sorted(required_case_ids - case_ids)}")
    routes = set((fixtures.get("coverage") or {}).get("routes_expected") or [])
    required_routes = {"OA-RT-01", "OA-MEM-01", "OA-PROJ-01", "OA-EVO-01", "OA-EFF-01"}
    if not required_routes.issubset(routes):
        fail(f"fixture route coverage missing: {sorted(required_routes - routes)}")

    print("v038-adoption-surface-pass")
    print(f"fixture-cases={len(cases)} (corpus fact, not completeness proof)")
    print("released-current-baseline-blob=825af4e985bd9114f6b69b145834ec050eef2a3d")
    print("semantic-trunk-01-04=byte-identical-to-v0.3.7-current")
    print("inherited-machine-paths=byte-identical-to-v0.3.7-current")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"v038-adoption-surface-fail: {exc}", file=sys.stderr)
        raise SystemExit(1)
