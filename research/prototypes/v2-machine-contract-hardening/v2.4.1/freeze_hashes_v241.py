#!/usr/bin/env python3
"""V2.4.1 freeze tooling: authoritative SHA-256 of committed blobs at a ref.
Usage: python freeze_hashes_v241.py <ref>   (run from repo root)
Hashes the BLOB content (git show <ref>:<path>) so digests are
autocrlf-independent. Mirrors v2.3/v2.4 tooling.
"""
import subprocess, sys, hashlib
from pathlib import Path

REF = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
ROOT = Path(__file__).resolve().parents[1]

FILES = [
    "research/prototypes/v2-machine-contract-hardening/v2.4.1/successor_contract_v241.py",
    "research/prototypes/v2-machine-contract-hardening/v2.4.1/acceptance_semantics_v241.py",
    "research/prototypes/v2-machine-contract-hardening/v2.4.1/wb_fixtures.py",
    "research/prototypes/v2-machine-contract-hardening/v2.4.1/f1_controls.py",
    "research/prototypes/v2-machine-contract-hardening/v2.4.1/run_v241.py",
    "research/prototypes/v2-machine-contract-hardening/v2.4.1/reproduce_f1.py",
    "research/prototypes/v2-machine-contract-hardening/v2.4.1/reproduction-f1.json",
    "research/prototypes/v2-machine-contract-hardening/v2.4.1/results-v241.json",
]

for f in FILES:
    out = subprocess.run(["git", "show", f"{REF}:{f}"], capture_output=True, cwd=ROOT)
    if out.returncode != 0:
        print(f"ERROR {f}: {out.stderr.decode(errors='replace').strip()}")
        continue
    print(f"{hashlib.sha256(out.stdout).hexdigest()}  {f}")
