#!/usr/bin/env python3
from __future__ import annotations

import subprocess
from pathlib import Path

FROZEN = "bda470e0a6b170cec61225a905957a501454a2fe"
FROZEN_CANDIDATE_TREE = "d5fefc8c786d7e40b3e9a59211ee7045bccee5bf"
FROZEN_CURRENT_TREE = "7dcbb3934883ffa6cc5292a662588cafc1533cff"
VIEW = "9876be2e683d07a3b5bb4421618d3b2cb04dbda4"
ROOT = "releases/v0.3.7-candidate"

EXCLUDED = {
    f"{ROOT}/README.md",
    f"{ROOT}/00-READ-ME-FIRST.md",
    f"{ROOT}/CANDIDATE-BASELINE.yaml",
    f"{ROOT}/CHANGELOG.md",
    f"{ROOT}/LINEAGE.md",
    f"{ROOT}/08-RELEASE-DISCIPLINE.md",
    f"{ROOT}/language-projections/semantic-fixtures.v1.yaml",
    f"{ROOT}/language-projections/semantic-fixtures.v2.yaml",
    f"{ROOT}/language-projections/semantic-fixtures.v3.yaml",
    f"{ROOT}/tools/contract-fixtures.v1.json",
    f"{ROOT}/tools/contract-fixtures.v2.json",
    f"{ROOT}/tools/contract-fixtures.v2.1.json",
    f"{ROOT}/tools/regression-results-v033.json",
    f"{ROOT}/tools/regression_suite.py",
    f"{ROOT}/tools/selftest_ena_evolve_v2.py",
    f"{ROOT}/tools/legacy/README.md",
    f"{ROOT}/tools/legacy/candidate1_adversarial_v1_2.py",
    f"{ROOT}/tools/legacy/candidate2_adversarial_v1_2.py",
    f"{ROOT}/references/advanced/contested-authorship/fixtures/contested-authorship-cases.jsonl",
    f"{ROOT}/references/advanced/contested-authorship/tools/selftest_contested_authorship.py",
    f"{ROOT}/references/advanced/evidence-dependency-map/fixtures/evidence-dependency-map-cases.jsonl",
    f"{ROOT}/references/advanced/evidence-dependency-map/tools/selftest_evidence_dependency_map.py",
    f"{ROOT}/references/advanced/evidence-envelope/fixtures/evidence-envelope-cases.jsonl",
    f"{ROOT}/references/advanced/evidence-envelope/tools/selftest_evidence_envelope.py",
    f"{ROOT}/references/general/authority-lease/fixtures/authority-lease-cases.jsonl",
    f"{ROOT}/references/general/authority-lease/tools/selftest_authority_lease.py",
    f"{ROOT}/references/general/effect-lifecycle/fixtures/effect-lifecycle-cases.jsonl",
    f"{ROOT}/references/general/effect-lifecycle/tools/selftest_effect_lifecycle.py",
    f"{ROOT}/references/general/recovery-adapter/fixtures/recovery-adapter-cases.jsonl",
    f"{ROOT}/references/general/recovery-adapter/tools/selftest_recovery_adapter.py",
    f"{ROOT}/references/general/retrieval-obligation/selftest.py",
    f"{ROOT}/references/general/wait-state/fixtures/wait-state-cases.jsonl",
    f"{ROOT}/references/general/wait-state/tools/selftest_wait_state.py",
}

PROJECTED = {
    f"{ROOT}/RUNTIME-ADOPTION-KERNEL.md",
    f"{ROOT}/tools/validate_evolution_record_v2.py",
}


def git_bytes(spec: str) -> bytes:
    return subprocess.check_output(["git", "show", spec])


def git_text(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True).strip()


def exists(ref: str, path: str) -> bool:
    return subprocess.run(
        ["git", "cat-file", "-e", f"{ref}:{path}"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode == 0


def main() -> None:
    assert git_text("rev-parse", f"{FROZEN}:{ROOT}") == FROZEN_CANDIDATE_TREE
    assert git_text("rev-parse", f"{FROZEN}:releases/current") == FROZEN_CURRENT_TREE
    assert git_text("rev-parse", f"{VIEW}^{{commit}}") == VIEW

    diff = git_text("diff", "--name-status", FROZEN, VIEW, "--", ROOT)
    observed_deleted: set[str] = set()
    observed_modified: set[str] = set()
    unexpected: list[str] = []
    for line in diff.splitlines():
        if not line:
            continue
        status, path = line.split("\t", 1)
        if status == "D":
            observed_deleted.add(path)
        elif status == "M":
            observed_modified.add(path)
        else:
            unexpected.append(line)

    assert not unexpected, f"unexpected candidate diff statuses: {unexpected}"
    assert observed_deleted == EXCLUDED, (
        f"excluded-file mismatch; missing={sorted(EXCLUDED-observed_deleted)} "
        f"extra={sorted(observed_deleted-EXCLUDED)}"
    )
    assert observed_modified == PROJECTED, (
        f"projection mismatch; expected={sorted(PROJECTED)} observed={sorted(observed_modified)}"
    )

    for path in EXCLUDED:
        assert not exists(VIEW, path), f"excluded file still exists in A-S view: {path}"

    runtime_path = f"{ROOT}/RUNTIME-ADOPTION-KERNEL.md"
    runtime_source = git_bytes(f"{FROZEN}:{runtime_path}")
    runtime_view = git_bytes(f"{VIEW}:{runtime_path}")
    runtime_expected = b"".join(runtime_source.splitlines(keepends=True)[6:])
    assert runtime_view == runtime_expected, "runtime projection != frozen source lines 7-EOF"

    validator_path = f"{ROOT}/tools/validate_evolution_record_v2.py"
    validator_source = git_bytes(f"{FROZEN}:{validator_path}")
    validator_view = git_bytes(f"{VIEW}:{validator_path}")
    validator_expected = b"".join(validator_source.splitlines(keepends=True)[:342])
    assert validator_view == validator_expected, "validator projection != frozen source lines 1-342"
    assert b"def validate_record(" in validator_view
    assert b"def exp_record(" not in validator_view
    assert b"def selftest(" not in validator_view
    assert b"--selftest" not in validator_view

    manifest = git_bytes(
        f"{VIEW}:collaboration/reconciliation/2026-08-28-v037-candidate2-blind-semantic-view.yaml"
    ).decode("utf-8")
    entry = git_bytes(
        f"{VIEW}:collaboration/reconciliation/2026-08-28-v037-candidate2-blind-semantic-entry.md"
    ).decode("utf-8")
    assert "validation/v037-c2-blind-semantic-primary-r2" in manifest
    assert "NATURAL_NAVIGATION_SAFE" in manifest
    assert 'source_range: "7-EOF"' in manifest
    assert 'source_range: "1-342"' in manifest
    assert "ba94cf252cc259b8ba837ae555ec431dadac4d25" in manifest
    assert "validation/v037-c2-blind-semantic-primary-r2" in entry
    assert "inspect **only**" in entry
    assert "do **not** open the exact frozen source commit directly before A-S seal" in entry

    print("CANDIDATE2_BLIND_VIEW_R2_AUDIT=PASS")
    print(f"frozen_source={FROZEN}")
    print(f"frozen_candidate_tree={FROZEN_CANDIDATE_TREE}")
    print(f"view_head={VIEW}")
    print(f"whole_file_exclusions={len(EXCLUDED)}")
    print(f"derived_projections={len(PROJECTED)}")
    print("retained_unprojected_candidate_byte_drift=0")
    print("attack_cardinality=OPEN")


if __name__ == "__main__":
    main()
