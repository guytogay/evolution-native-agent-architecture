#!/usr/bin/env python3
"""Phase A — independent verification of V2.4.1 frozen digests.

Computes SHA-256 over `git show <REF>:<path>` blob content (LF-normalized,
autocrlf-independent) for each file declared in FREEZE-MANIFEST-V241.md and
compares to the declared digest. Also lists the full v2.4.1 file set at REF
to confirm "candidate files are exactly those frozen".

Self-contained: derive repo root via `git rev-parse --show-toplevel`. Run from
anywhere inside the repo:
    python collaboration/inbox/v241-harness/verify_digests.py
"""
import subprocess, sys, hashlib

REPO_ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).decode().strip()
REF = "daacab1f042c38f3856ef4d0366febd1b5e47600"   # frozen V2.4.1 successor
V241_DIR = "research/prototypes/v2-machine-contract-hardening/v2.4.1"

# (manifest-declared path, expected SHA-256) — copied verbatim from FREEZE-MANIFEST-V241.md
EXPECTED = [
    ("successor_contract_v241.py",
     "1390112d62bd27eecb2b6d68d7032fd6cf4d28fd977e1c600de9f0043496566a"),
    ("acceptance_semantics_v241.py",
     "b7735289a0835d44aabcf4dfb841293335fed719ceccee0eaed7d8c80bfd8689"),
    ("wb_fixtures.py",
     "71c972a6cd4694dea32b0b6ac9c61a7668b67f2819f2b591dc56ac15e0e25bf8"),
    ("f1_controls.py",
     "b821293e3308e12859fff8db34713d0d898eb1362341a997b23b637645290298"),
    ("run_v241.py",
     "1fa74a1f01e52ec010d032c977cf7271de875d2b3c5ba7394276a625ed9541f9"),
    ("reproduce_f1.py",
     "dfa4ab040afd35d3cc7b5264e49ed698b8d4e6020e0d9980f4c4e19154a57c8e"),
    ("reproduction-f1.json",
     "b73a8d744b5caf889833bc9758dda768e57eaa4ea354e8d0e299a835ff9ef699"),
    ("results-v241.json",
     "d1e83e25d541e360c03696fbdbdd59da45b19f2f92d477d7999d54ee3989e09b"),
]


def blob_sha256(ref, path):
    raw = subprocess.check_output(["git", "show", f"{ref}:{path}"])
    return hashlib.sha256(raw).hexdigest()


def main():
    all_ok = True
    for name, exp in EXPECTED:
        path = f"{V241_DIR}/{name}"
        try:
            got = blob_sha256(REF, path)
        except subprocess.CalledProcessError as e:
            print(f"[MISSING] {name}: {e}")
            all_ok = False
            continue
        ok = (got == exp)
        all_ok = all_ok and ok
        print(f"[{'OK' if ok else 'FAIL'}] {name}\n    exp {exp}\n    got {got}")

    # full v2.4.1 file set at REF
    out = subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", REF]
    ).decode().splitlines()
    v241_files = [p for p in out if p.startswith(V241_DIR + "/")]
    digested = {f"{V241_DIR}/{n}" for n, _ in EXPECTED}
    undigested = [p for p in v241_files if p not in digested]

    print("\n=== Full v2.4.1 file set at REF ===")
    for p in v241_files:
        print("  ", p)
    print("\nUndigested v2.4.1 files present in REF:", undigested or "(none)")

    print("\n=== RESULT ===")
    print("All 8 declared digests MATCH:", all_ok)
    print("Undigested v2.4.1 files present in REF:", undigested)
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
