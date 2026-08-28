#!/usr/bin/env python3
from __future__ import annotations

import ast
import hashlib
import io
import json
import re
import shutil
import subprocess
import tempfile
import tokenize
import zipfile
from pathlib import Path

FROZEN = "bda470e0a6b170cec61225a905957a501454a2fe"
FROZEN_TREE = "d5fefc8c786d7e40b3e9a59211ee7045bccee5bf"
ROOT = Path("releases/v0.3.7-candidate")
OUT = Path("capsule-out")

WHOLE_AS_EXCLUSIONS = {
    "README.md",
    "00-READ-ME-FIRST.md",
    "CANDIDATE-BASELINE.yaml",
    "CHANGELOG.md",
    "LINEAGE.md",
    "07-ADOPTION-AND-FIELD-VALIDATION.md",
    "08-RELEASE-DISCIPLINE.md",
    "10-LANGUAGE-PORTABILITY.md",
    "references/REFERENCE-MANIFEST.yaml",
    "operational/README.md",
    "language-projections/semantic-fixtures.v1.yaml",
    "language-projections/semantic-fixtures.v2.yaml",
    "language-projections/semantic-fixtures.v3.yaml",
    "language-projections/zh-CN/00-READ-ME-FIRST.md",
    "language-projections/zh-CN/REFERENCE-GUIDE.md",
    "language-projections/zh-CN/projection-manifest.yaml",
    "tools/contract-fixtures.v1.json",
    "tools/contract-fixtures.v2.json",
    "tools/contract-fixtures.v2.1.json",
    "tools/regression-results-v033.json",
    "tools/regression_suite.py",
    "tools/selftest_ena_evolve_v2.py",
    "tools/legacy/README.md",
    "tools/legacy/candidate1_adversarial_v1_2.py",
    "tools/legacy/candidate2_adversarial_v1_2.py",
    "tools/legacy/ena_evolve_v1_2.py",
    "references/advanced/contested-authorship/fixtures/contested-authorship-cases.jsonl",
    "references/advanced/contested-authorship/tools/selftest_contested_authorship.py",
    "references/advanced/evidence-dependency-map/fixtures/evidence-dependency-map-cases.jsonl",
    "references/advanced/evidence-dependency-map/tools/selftest_evidence_dependency_map.py",
    "references/advanced/evidence-envelope/fixtures/evidence-envelope-cases.jsonl",
    "references/advanced/evidence-envelope/tools/selftest_evidence_envelope.py",
    "references/general/authority-lease/fixtures/authority-lease-cases.jsonl",
    "references/general/authority-lease/tools/selftest_authority_lease.py",
    "references/general/effect-lifecycle/fixtures/effect-lifecycle-cases.jsonl",
    "references/general/effect-lifecycle/tools/selftest_effect_lifecycle.py",
    "references/general/recovery-adapter/fixtures/recovery-adapter-cases.jsonl",
    "references/general/recovery-adapter/tools/selftest_recovery_adapter.py",
    "references/general/retrieval-obligation/selftest.py",
    "references/general/wait-state/fixtures/wait-state-cases.jsonl",
    "references/general/wait-state/tools/selftest_wait_state.py",
}

HIGH_SIGNAL = re.compile(
    r"candidate[ ._-]*1|NEEDS_REVISION|Phase[ -]*B|pre[- ]?freeze|author[- ]side|"
    r"prior[- ]falsifier|PR #[0-9]+|false claim|false block|false OK|fixes P[0-9]+|"
    r"REVALIDATION_BY|INDEPENDENT_IMPLEMENTATION_VALIDATION|workflow_run_id|330[0-9]{7,}|"
    r"independent review of [0-9]|repair reconciliation|regression-results",
    re.I,
)


def run(*args: str, text: bool = True) -> str:
    return subprocess.check_output(list(args), text=text).strip() if text else subprocess.check_output(list(args))


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def remove_docstrings(tree: ast.AST) -> ast.AST:
    for node in ast.walk(tree):
        body = getattr(node, "body", None)
        if isinstance(body, list) and body:
            first = body[0]
            if isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant) and isinstance(first.value.value, str):
                body.pop(0)
    ast.fix_missing_locations(tree)
    return tree


def strip_python_to_ast_equivalent(source: str, label: str) -> str:
    original = ast.parse(source, filename=label)
    expected = remove_docstrings(original)
    if any(isinstance(n, ast.Name) and n.id == "__doc__" for n in ast.walk(expected)):
        raise SystemExit(f"{label}: __doc__ is referenced; cannot safely strip docstrings")
    rendered = ast.unparse(expected) + "\n"
    observed = ast.parse(rendered, filename=label + ":projection")
    if ast.dump(expected, include_attributes=False) != ast.dump(observed, include_attributes=False):
        raise SystemExit(f"{label}: AST-equivalent projection failed")
    return rendered


def deterministic_zip(root: Path, output: Path) -> None:
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted(p for p in root.rglob("*") if p.is_file()):
            rel = path.relative_to(root).as_posix()
            info = zipfile.ZipInfo(rel, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            zf.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def inventory(root: Path) -> list[dict[str, str]]:
    result = []
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        result.append({"path": path.relative_to(root).as_posix(), "sha256": sha256(path)})
    return result


def main() -> None:
    if run("git", "rev-parse", f"{FROZEN}:{ROOT.as_posix()}") != FROZEN_TREE:
        raise SystemExit("frozen candidate tree binding mismatch")
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    with tempfile.TemporaryDirectory(prefix="ena-c2-r3-") as td:
        td = Path(td)
        archive = td / "candidate.tar"
        archive.write_bytes(subprocess.check_output(["git", "archive", FROZEN, ROOT.as_posix()]))
        subprocess.check_call(["tar", "-xf", str(archive), "-C", str(td)])
        frozen_candidate = td / ROOT

        as_root = OUT / "candidate2-as-capsule-r3"
        as_candidate = as_root / ROOT
        as_candidate.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(frozen_candidate, as_candidate)

        # Physically remove history/oracle/status-heavy surfaces from A-S.
        for rel in sorted(WHOLE_AS_EXCLUSIONS):
            target = as_candidate / rel
            if not target.exists():
                raise SystemExit(f"declared A-S exclusion missing from frozen candidate: {rel}")
            target.unlink()
        for d in sorted((p for p in as_candidate.rglob("*") if p.is_dir()), reverse=True):
            try:
                d.rmdir()
            except OSError:
                pass

        transformations: list[dict[str, str]] = []

        # Runtime kernel: exact source lines 7-EOF.
        runtime = as_candidate / "RUNTIME-ADOPTION-KERNEL.md"
        src = (frozen_candidate / "RUNTIME-ADOPTION-KERNEL.md").read_text(encoding="utf-8")
        runtime_text = "".join(src.splitlines(keepends=True)[6:])
        runtime.write_text(runtime_text, encoding="utf-8", newline="")
        transformations.append({"path": str(runtime.relative_to(as_root)), "kind": "EXACT_SOURCE_SLICE", "source_range": "7-EOF"})

        # Core contracts: remove one author-history paragraph while preserving surrounding semantic contract.
        core = as_candidate / "05-CORE-OPERATIONAL-CONTRACTS.md"
        core_src = (frozen_candidate / "05-CORE-OPERATIONAL-CONTRACTS.md").read_text(encoding="utf-8")
        history_para = (
            "v0.3.7 candidate.2 retains the accepted composed-validator implementation released through v0.3.6 Current "
            "(originating in the v0.3.3 falsification/repair lineage) under `tools/validate_contracts.py`, together with its inherited "
            "fixture/regression corpus. This preserved implementation surface protects previously falsified semantics while the broader architecture evolves.\n\n"
        )
        if core_src.count(history_para) != 1:
            raise SystemExit("core-contract author-history paragraph anchor mismatch")
        core.write_text(core_src.replace(history_para, "", 1), encoding="utf-8", newline="")
        transformations.append({"path": str(core.relative_to(as_root)), "kind": "EXACT_AUTHOR_HISTORY_PARAGRAPH_REMOVAL"})

        # Adaptation schema: redact predecessor identity in annotation-only title.
        schema = as_candidate / "schemas/adaptation-packet.v2.schema.json"
        schema_src = (frozen_candidate / "schemas/adaptation-packet.v2.schema.json").read_text(encoding="utf-8")
        old_title = '"title": "ENA Adaptation Migration Packet v2 (v0.3.6 candidate.1)"'
        new_title = '"title": "ENA Adaptation Migration Packet v2"'
        if schema_src.count(old_title) != 1:
            raise SystemExit("adaptation schema title anchor mismatch")
        schema_text = schema_src.replace(old_title, new_title, 1)
        schema.write_text(schema_text, encoding="utf-8", newline="")
        old_obj, new_obj = json.loads(schema_src), json.loads(schema_text)
        old_obj.pop("title", None); new_obj.pop("title", None)
        if old_obj != new_obj:
            raise SystemExit("adaptation schema projection changed validation-bearing JSON")
        transformations.append({"path": str(schema.relative_to(as_root)), "kind": "ANNOTATION_ONLY_TITLE_REDACTION"})

        # Evolution validator: first 342 frozen lines are the executable semantic core; then strip docstrings/comments via AST unparse.
        evo = as_candidate / "tools/validate_evolution_record_v2.py"
        evo_src_full = (frozen_candidate / "tools/validate_evolution_record_v2.py").read_text(encoding="utf-8")
        evo_prefix = "".join(evo_src_full.splitlines(keepends=True)[:342])
        evo.write_text(strip_python_to_ast_equivalent(evo_prefix, "validate_evolution_record_v2.py"), encoding="utf-8", newline="")
        transformations.append({"path": str(evo.relative_to(as_root)), "kind": "AST_EQUIVALENT_SOURCE_PREFIX", "source_range": "1-342"})

        # All other retained Python: remove comments/docstrings by AST round-trip to avoid author search-map prose while preserving executable AST.
        for py in sorted(as_candidate.rglob("*.py")):
            if py == evo:
                continue
            rel = py.relative_to(as_candidate)
            frozen_py = frozen_candidate / rel
            source = frozen_py.read_text(encoding="utf-8")
            projected = strip_python_to_ast_equivalent(source, rel.as_posix())
            py.write_text(projected, encoding="utf-8", newline="")
            transformations.append({"path": str(py.relative_to(as_root)), "kind": "AST_EQUIVALENT_COMMENTS_AND_DOCSTRINGS_REMOVED"})

        # Tight priming sweep over the actual A-S carrier.
        hits = []
        for path in sorted(p for p in as_candidate.rglob("*") if p.is_file()):
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for n, line in enumerate(text.splitlines(), 1):
                if HIGH_SIGNAL.search(line):
                    hits.append(f"{path.relative_to(as_root)}:{n}:{line}")
        if hits:
            raise SystemExit("high-signal priming remained in A-S capsule:\n" + "\n".join(hits))

        intake_as = f"""# ENA v0.3.7 candidate.2 — fresh independent A-S intake (capsule r3)\n\nStatus: `PHYSICALLY_ISOLATED_A_S_CAPSULE / NOT_RELEASE_AUTHORITY`\n\nExact frozen target:\n- identity: `v0.3.7-candidate.2`\n- source commit: `{FROZEN}`\n- candidate subtree: `{FROZEN_TREE}`\n\nThis archive is the complete A-S review surface. Do not browse the project repository or seek external project history during A-S. The archive physically omits author history, expected fixtures/oracles, prior findings, project-manager context, Current, and historical releases. Some executable files are declared AST-equivalent comment/docstring-free projections so prior attack maps are not embedded in implementation comments.\n\nIndependently falsify the represented semantics and executable behavior. Search for false claims/false confidence, false blocks, chronology/order ambiguity, duplicated-fact contradictions, evidence-scope inflation, migration/provenance errors, authority/effect/recovery/wait composition seams, accidental universalization, prose/schema/tool disagreement, and legitimate unresolved possibilities. This is not a finite checklist. `ATTACK_CARDINALITY = OPEN`.\n\nWrite the A-S report to `candidate2-independent-a-s-primary-r3.md`. Before opening any A-P material, compute SHA-256 of that exact report file and record the digest in the report and in your response. That digest is the A-S content seal for this isolated-review workflow. Then STOP and request the separate A-P supplement.\n\nDo not perform A-P or Phase B while only this capsule is available.\n"""
        (as_root / "INTAKE-A-S.md").write_text(intake_as, encoding="utf-8")

        as_manifest = {
            "schema_version": "1.0",
            "status": "PHYSICALLY_ISOLATED_A_S_CAPSULE_R3",
            "frozen_target": {"identity": "v0.3.7-candidate.2", "source_commit": FROZEN, "candidate_subtree": FROZEN_TREE},
            "whole_file_exclusions_from_a_s": sorted(WHOLE_AS_EXCLUSIONS),
            "transformations": transformations,
            "invariants": [
                "A_S_REVIEW_SURFACE_NE_PROJECT_REPOSITORY_UI",
                "PROCEDURAL_PATH_AVOIDANCE_NE_INFORMATION_BOUNDARY",
                "PROJECT_MANAGER_CONTEXT_PHYSICALLY_ABSENT",
                "AUTHOR_ORACLES_PHYSICALLY_ABSENT",
                "PYTHON_PROJECTIONS_EXECUTABLE_AST_EQUIVALENT_EXCEPT_DOCSTRINGS",
                "ATTACK_CARDINALITY_OPEN",
            ],
        }
        (as_root / "MANIFEST-A-S.json").write_text(json.dumps(as_manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        as_manifest["files"] = inventory(as_root)
        (as_root / "MANIFEST-A-S.json").write_text(json.dumps(as_manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        # A-P supplement contains exact frozen candidate package only; no research/project-manager context.
        ap_root = OUT / "candidate2-ap-supplement-r3"
        ap_candidate = ap_root / ROOT
        ap_candidate.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(frozen_candidate, ap_candidate)
        intake_ap = f"""# ENA v0.3.7 candidate.2 — independent A-P supplement (r3)\n\nOpen this archive only after the A-S report has been content-sealed with SHA-256.\n\nExact frozen target:\n- identity: `v0.3.7-candidate.2`\n- source commit: `{FROZEN}`\n- candidate subtree: `{FROZEN_TREE}`\n\nAudit the full frozen candidate package: self-description, lineage consistency, fixtures, selftests, regression oracles, packaging claims, and any package-level defects. Compare against the already sealed A-S attack tree; do not rewrite A-S. This supplement intentionally contains the exact frozen candidate package but no external project-manager repair maps/reconciliation context.\n\nWrite `candidate2-independent-a-p-primary-r3.md`, record the A-S SHA-256 you received, then STOP. Do not perform Phase B.\n"""
        (ap_root / "INTAKE-A-P.md").write_text(intake_ap, encoding="utf-8")
        ap_manifest = {
            "schema_version": "1.0",
            "status": "A_P_SUPPLEMENT_EXACT_FROZEN_CANDIDATE_R3",
            "frozen_target": {"identity": "v0.3.7-candidate.2", "source_commit": FROZEN, "candidate_subtree": FROZEN_TREE},
            "candidate_package_bytes": "EXACT_FROZEN_SOURCE_TREE",
            "external_project_manager_context_included": False,
        }
        (ap_root / "MANIFEST-A-P.json").write_text(json.dumps(ap_manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        ap_manifest["files"] = inventory(ap_root)
        (ap_root / "MANIFEST-A-P.json").write_text(json.dumps(ap_manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    as_zip = OUT / "candidate2-as-capsule-r3.zip"
    ap_zip = OUT / "candidate2-ap-supplement-r3.zip"
    deterministic_zip(OUT / "candidate2-as-capsule-r3", as_zip)
    deterministic_zip(OUT / "candidate2-ap-supplement-r3", ap_zip)
    hashes = {
        "candidate2-as-capsule-r3.zip": sha256(as_zip),
        "candidate2-ap-supplement-r3.zip": sha256(ap_zip),
    }
    (OUT / "CAPSULE-HASHES.json").write_text(json.dumps(hashes, indent=2) + "\n", encoding="utf-8")
    print("CANDIDATE2_REVIEW_CAPSULE_R3_BUILD=PASS")
    print(json.dumps(hashes, indent=2))
    print("attack_cardinality=OPEN")


if __name__ == "__main__":
    main()
