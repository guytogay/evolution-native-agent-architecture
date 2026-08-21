#!/usr/bin/env python3
"""V0.3.3-candidate freeze tooling: authoritative SHA-256 of committed blobs at
a ref. Usage: python freeze_hashes_v033candidate.py <ref>   (run from repo root)
Hashes BLOB content (git show <ref>:<path>) so digests are autocrlf-independent.
"""
import subprocess, sys, hashlib
from pathlib import Path

REF = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
HERE = Path(__file__).resolve()

def _find_repo(start):
    cur = start
    for _ in range(8):
        if (cur / ".git").exists():
            return cur
        cur = cur.parent
    return start.parents[3]

ROOT = _find_repo(HERE)

FILES = [
    "releases/v0.3.3-candidate/CANDIDATE-BASELINE.yaml",
    "releases/v0.3.3-candidate/README.md",
    "releases/v0.3.3-candidate/CHANGELOG.md",
    "releases/v0.3.3-candidate/05-CORE-OPERATIONAL-CONTRACTS.md",
    "releases/v0.3.3-candidate/schemas/composed-case.v1.schema.json",
    "releases/v0.3.3-candidate/tools/validate_contracts.py",
    "releases/v0.3.3-candidate/tools/contract-fixtures.v2.json",
    "releases/v0.3.3-candidate/tools/regression_suite.py",
    "releases/v0.3.3-candidate/tools/regression-results-v033candidate.json",
    "releases/v0.3.3-candidate/tools/build_regression_corpus.py",
    ".github/workflows/candidate-gate.yml",
]

for f in FILES:
    out = subprocess.run(["git", "show", f"{REF}:{f}"], capture_output=True, cwd=ROOT)
    if out.returncode != 0:
        print(f"ERROR {f}: {out.stderr.decode(errors='replace').strip()}")
        continue
    print(f"{hashlib.sha256(out.stdout).hexdigest()}  {f}")
