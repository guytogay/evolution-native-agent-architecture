#!/usr/bin/env python3
"""V2.4 freeze tooling: authoritative SHA-256 of committed blobs at a ref.
Usage: python freeze_hashes_v24.py <ref>   (run from repo root)
Hashes the BLOB content (git show <ref>:<path>) so digests are
autocrlf-independent. Mirrors the V2.3 freeze_hashes.py tool.
"""
import subprocess, sys, hashlib
from pathlib import Path

REF = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
ROOT = Path(__file__).resolve().parents[1]

FILES = [
    "research/prototypes/v2-machine-contract-hardening/v2.4/successor_contract.py",
    "research/prototypes/v2-machine-contract-hardening/v2.4/acceptance_semantics_v24.py",
    "research/prototypes/v2-machine-contract-hardening/v2.4/independent_fixtures.py",
    "research/prototypes/v2-machine-contract-hardening/v2.4/successor_controls.py",
    "research/prototypes/v2-machine-contract-hardening/v2.4/run_v24.py",
    "research/prototypes/v2-machine-contract-hardening/v2.4/reproduce_v23.py",
    "research/prototypes/v2-machine-contract-hardening/v2.4/RECONCILIATION.md",
    "research/prototypes/v2-machine-contract-hardening/v2.4/reproduction-v23.json",
    "research/prototypes/v2-machine-contract-hardening/v2.4/results-v24.json",
]

for f in FILES:
    out = subprocess.run(["git", "show", f"{REF}:{f}"], capture_output=True, cwd=ROOT)
    if out.returncode != 0:
        print(f"ERROR {f}: {out.stderr.decode(errors='replace').strip()}")
        continue
    print(f"{hashlib.sha256(out.stdout).hexdigest()}  {f}")
