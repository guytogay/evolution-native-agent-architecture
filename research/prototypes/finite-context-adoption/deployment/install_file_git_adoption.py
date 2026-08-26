#!/usr/bin/env python3
"""Install a research-only File/Git tiny-resident ENA adoption bundle.

This is a concrete HOW-A recipe. It copies one chosen resident kernel and writes
an exact source-identity pointer to an existing canonical Current checkout.
It does not install a semantic index or claim the kernel is universally best.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kernel", type=Path, required=True)
    parser.add_argument("--cold-current-root", type=Path, required=True)
    parser.add_argument("--install-root", type=Path, required=True)
    parser.add_argument("--ena-version", default="v0.3.6")
    parser.add_argument("--current-tree", default="7dcbb3934883ffa6cc5292a662588cafc1533cff")
    parser.add_argument("--merge-commit", default="74b790741653286e0f01a1483723cdeb065ec3df")
    args = parser.parse_args()

    if not args.kernel.is_file():
        raise SystemExit(f"kernel file not found: {args.kernel}")
    if not args.cold_current_root.is_dir():
        raise SystemExit(f"cold Current root not found: {args.cold_current_root}")

    required = [
        "02-SELF-POSITIONING-AND-LOCAL-PROJECTION.md",
        "05-CORE-OPERATIONAL-CONTRACTS.md",
        "09-EVOLUTION-METABOLISM.md",
    ]
    missing = [name for name in required if not (args.cold_current_root / name).is_file()]
    if missing:
        raise SystemExit(f"cold Current root missing expected files: {missing}")

    args.install_root.mkdir(parents=True, exist_ok=True)
    resident = args.install_root / "ENA-RESIDENT-KERNEL.md"
    shutil.copyfile(args.kernel, resident)

    source = {
        "implementation_how": "HOW-A-FILE-GIT-TINY-COLD",
        "ena_version": args.ena_version,
        "current_tree": args.current_tree,
        "release_merge_commit": args.merge_commit,
        "cold_current_root": str(args.cold_current_root.resolve()),
        "resident_kernel_file": str(resident.resolve()),
        "claim_boundary": [
            "KERNEL_INSTALLED != NATURALISTIC_SALIENCE_PROVEN",
            "COLD_SOURCE_PRESENT != RELEVANT_SECTION_RETRIEVED",
            "SOURCE_IDENTITY_REPRESENTED != EXTERNALLY_AUTHENTICATED",
        ],
    }
    (args.install_root / "ena-source.json").write_text(
        json.dumps(source, indent=2) + "\n", encoding="utf-8"
    )

    print(f"installed_resident={resident}")
    print(f"source_pointer={args.install_root / 'ena-source.json'}")
    print("how=HOW-A-FILE-GIT-TINY-COLD")
    print("current_change=NO")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
