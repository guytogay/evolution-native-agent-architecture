#!/usr/bin/env python3
"""TEMP: compute authoritative SHA256 of committed blobs at a given ref.
Usage: python freeze_hashes.py <ref>  (run from repo root)
Prints "<sha256>  <path>" for each candidate file, hashing the BLOB content
(git show <ref>:<path>) so digests are autocrlf-independent.
"""
import subprocess, sys, hashlib
from pathlib import Path

REF = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
ROOT = Path(__file__).resolve().parents[1]   # repo root (this script sits in v2.3/)

FILES = [
    "research/prototypes/v2-machine-contract-hardening/hardened_rules.py",
    "research/prototypes/v2-machine-contract-hardening/fixtures.py",
    "research/prototypes/v2-machine-contract-hardening/v2.1/fixtures_v21.py",
    "research/prototypes/v2-machine-contract-hardening/v2.2/cumulative_contract.py",
    "research/prototypes/v2-machine-contract-hardening/v2.2/fixtures_v22.py",
    "research/prototypes/v2-machine-contract-hardening/v2.2/run_v22.py",
    "research/prototypes/v2-machine-contract-hardening/v2.3/acceptance_semantics.py",
    "research/prototypes/v2-machine-contract-hardening/v2.3/fixtures_migrated.py",
    "research/prototypes/v2-machine-contract-hardening/v2.3/run_v23.py",
    "research/prototypes/v2-machine-contract-hardening/v2.3/expected-verdict-manifest.json",
    "research/prototypes/v2-machine-contract-hardening/v2.3/results-v23.json",
]

for f in FILES:
    out = subprocess.run(["git", "show", f"{REF}:{f}"], capture_output=True, cwd=ROOT)
    if out.returncode != 0:
        print(f"ERROR {f}: {out.stderr.decode(errors='replace').strip()}")
        continue
    digest = hashlib.sha256(out.stdout).hexdigest()
    print(f"{digest}  {f}")
