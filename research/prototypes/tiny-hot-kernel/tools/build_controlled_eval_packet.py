#!/usr/bin/env python3
"""Build a layered Tiny Hot Kernel controlled-evaluation packet.

The output deliberately separates resident Agent material, blind stimuli,
gated resolver material, runner/maintainer instructions, and private oracle/scoring.

This is packaging discipline, not a security boundary. A runner must still
control which directories/resources the test Agent can access at each stage.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil

KERNELS = {
    "K-A": "K-A-generative-consequence-grammar.md",
    "K-B": "K-B-seven-family-index.md",
    "K-C": "K-C-minimal-interrupt-questions.md",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kernel", choices=sorted(KERNELS), required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    output = args.output.resolve()
    if output.exists():
        if any(output.iterdir()):
            raise SystemExit(f"output directory must be empty or absent: {output}")
    output.mkdir(parents=True, exist_ok=True)

    kernel_src = root / "kernels" / KERNELS[args.kernel]
    agent_output_src = root / "AGENT-OUTPUT-CONTRACT.md"
    blind_src = root / "fixtures" / "tiny-kernel-prompts.jsonl"
    router_src = root / "semantic-router.v0.1.json"
    runner_src = root / "CONTROLLED-RUNNER-INSTRUCTION.md"
    protocol_src = root / "EVAL-PROTOCOL.md"
    manifest_template_src = root / "run-manifest.template.json"
    oracle_src = root / "fixtures" / "tiny-kernel-cases.jsonl"
    scorer_src = root / "tools" / "score_tiny_kernel_results.py"

    files = [
        (kernel_src, output / "resident" / kernel_src.name, "AGENT_RESIDENT"),
        (agent_output_src, output / "resident" / agent_output_src.name, "AGENT_IO_ONLY"),
        (blind_src, output / "stimuli" / blind_src.name, "BLIND_STIMULUS"),
        (router_src, output / "gated-resolver" / router_src.name, "GATED_AFTER_TRIGGER"),
        (runner_src, output / "maintainer" / runner_src.name, "RUNNER_CONTROL_NOT_AGENT_RESIDENT"),
        (manifest_template_src, output / "maintainer" / manifest_template_src.name, "MAINTAINER_METADATA"),
        (protocol_src, output / "maintainer" / protocol_src.name, "MAINTAINER_PROTOCOL"),
        (oracle_src, output / "maintainer-private" / oracle_src.name, "MAINTAINER_ORACLE_PRIVATE"),
        (scorer_src, output / "maintainer-private" / scorer_src.name, "MAINTAINER_SCORER_PRIVATE"),
    ]

    records = []
    for src, dst, role in files:
        if not src.is_file():
            raise SystemExit(f"missing source file: {src}")
        copy_file(src, dst)
        records.append(
            {
                "path": str(dst.relative_to(output)),
                "role": role,
                "bytes": dst.stat().st_size,
                "sha256": sha256(dst),
            }
        )

    packet_manifest = {
        "schema_version": "0.2",
        "status": "RESEARCH_EVAL_PACKET / NOT_CURRENT",
        "kernel": args.kernel,
        "access_model": {
            "resident": "only candidate kernel + neutral Agent output contract at context start",
            "stimuli": "present one blind case at a time",
            "gated-resolver": "make available only after trigger=true and only when resolver_state=AVAILABLE",
            "maintainer": "runner/protocol/metadata; do not inject into Agent resident context",
            "maintainer-private": "must not be exposed to test Agent during controlled run",
        },
        "warning": "directory separation is packaging discipline, not a security sandbox; the runner must enforce access",
        "files": records,
    }
    manifest_path = output / "PACKET-MANIFEST.json"
    manifest_path.write_text(json.dumps(packet_manifest, indent=2) + "\n", encoding="utf-8")

    # Mechanical anti-leak check 1: no oracle expectation fields in any layer the
    # Agent can see during the controlled run, including the gated resolver.
    forbidden_oracle_tokens = [
        b'"expected_trigger"',
        b'"primary_families"',
        b'"allowed_families"',
    ]
    agent_accessible_roots = [
        output / "resident",
        output / "stimuli",
        output / "gated-resolver",
    ]
    leaks: list[str] = []
    for accessible_root in agent_accessible_roots:
        for path in accessible_root.rglob("*"):
            if not path.is_file():
                continue
            data = path.read_bytes()
            if any(token in data for token in forbidden_oracle_tokens):
                leaks.append(str(path.relative_to(output)))
    if leaks:
        raise SystemExit(f"oracle field-name leak into Agent-accessible layer: {leaks}")

    # Mechanical anti-leak check 2: resident context must not contain concrete
    # router route IDs. Route IDs become visible only through the gated resolver
    # after the resident recognizer has already decided to trigger.
    router = json.loads(router_src.read_text(encoding="utf-8"))
    route_ids = [route["route_id"] for route in router.get("routes", [])]
    resident_route_leaks: list[str] = []
    for path in (output / "resident").rglob("*"):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        leaked_ids = [route_id for route_id in route_ids if route_id in text]
        if leaked_ids:
            resident_route_leaks.append(
                f"{path.relative_to(output)}:{','.join(sorted(leaked_ids))}"
            )
    if resident_route_leaks:
        raise SystemExit(
            f"router answer leakage into resident layer: {resident_route_leaks}"
        )

    print(f"PASS: built layered packet kernel={args.kernel} files={len(records)}")
    print("PASS: Agent-accessible layers contain no oracle expectation field names")
    print("PASS: resident layer contains no concrete router route IDs")
    print(f"packet_manifest={manifest_path}")
    print("verification_scope=PACKAGING_AND_MECHANICAL_ORACLE_ROUTER_SEPARATION_ONLY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
