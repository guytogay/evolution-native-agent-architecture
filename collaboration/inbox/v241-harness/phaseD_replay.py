#!/usr/bin/env python3
"""Phase D — independent reproduction of the frozen V2.4.1 148-fixture replay.

Extracts the COMPLETE frozen tree at REF daacab1 (via `git archive`; a blobless
clone fetches the needed blobs on demand) into a temp dir, runs run_v241.py
against the frozen V2.4.1 successor over the frozen corpus, and compares the
generated results-v241.json to the committed blob (semantic JSON equality).

This does NOT trust the committed results file: it re-executes the exact frozen
implementation (successor_contract_v241.py) over the exact frozen corpus
(fixtures from all v2.x dirs + wb_fixtures + f1_controls) and re-derives every
verdict. The only thing compared is the *output*, and only to demonstrate
reproducibility / authenticity of the frozen evidence.

Self-contained: derive repo root via `git rev-parse --show-toplevel`. Run from
anywhere inside the repo:
    python collaboration/inbox/v241-harness/phaseD_replay.py
"""
import subprocess, sys, os, tempfile, json, shutil

REPO_ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).decode().strip()
REF = "daacab1f042c38f3856ef4d0366febd1b5e47600"   # frozen V2.4.1 successor
V241_RELPATH = "research/prototypes/v2-machine-contract-hardening/v2.4.1"
RESULTS_RELPATH = f"{V241_RELPATH}/results-v241.json"

PY = sys.executable


def git(*args):
    return subprocess.run(["git", *args], cwd=REPO_ROOT, capture_output=True, text=True)


def main():
    print("=" * 78)
    print("PHASE D — independent 148-fixture replay reproduction (frozen V2.4.1)")
    print("=" * 78)
    print(f"REF            : {REF}")
    print(f"REPO_ROOT      : {REPO_ROOT}")

    # 1) extract full frozen tree into a temp dir (git-object based:
    #    ls-tree enumerates, git show emits each blob; no tar/zip used)
    tmp = tempfile.mkdtemp(prefix="ena-v241-phased-")
    try:
        print(f"\n[1] extracting full frozen tree at {REF} -> {tmp}")
        paths = subprocess.run(
            ["git", "ls-tree", "-r", "--name-only", REF],
            cwd=REPO_ROOT, capture_output=True, text=True,
        )
        if paths.returncode != 0:
            print("git ls-tree FAILED:", paths.stderr); sys.exit(2)
        file_list = [p for p in paths.stdout.splitlines() if p]
        for rel in file_list:
            blob = subprocess.run(
                ["git", "show", f"{REF}:{rel}"],
                cwd=REPO_ROOT, capture_output=True,
            )
            if blob.returncode != 0:
                print(f"git show FAILED for {rel}:", blob.stderr); sys.exit(2)
            dest = os.path.join(tmp, *rel.split("/"))
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, "wb") as f:
                f.write(blob.stdout)
        print(f"    extracted {len(file_list)} paths")
        v241_dir = os.path.join(tmp, *V241_RELPATH.split("/"))
        run_script = os.path.join(v241_dir, "run_v241.py")
        if not os.path.isfile(run_script):
            print(f"run_v241.py not found at {run_script}"); sys.exit(2)
        print(f"    extracted; run_v241.py present: {os.path.isfile(run_script)}")

        # 2) run the replay
        print("\n[2] executing run_v241.py against frozen V2.4.1 successor")
        r = subprocess.run([PY, run_script], cwd=v241_dir, capture_output=True, text=True)
        if r.returncode != 0:
            print("run_v241.py exited non-zero:", r.returncode)
            print("--- stdout ---\n" + r.stdout)
            print("--- stderr ---\n" + r.stderr)
            sys.exit(2)
        # print the summary tail
        out_lines = r.stdout.strip().splitlines()
        summary_start = next((i for i, l in enumerate(out_lines)
                              if l.startswith("TOTAL_FIXTURES")), None)
        if summary_start is not None:
            print("\n".join(out_lines[summary_start:]))
        else:
            print(r.stdout[-1500:])

        # 3) load generated results and compare to committed blob
        print("\n[3] comparing generated results-v241.json to committed blob (semantic)")
        gen_path = os.path.join(v241_dir, "results-v241.json")
        if not os.path.isfile(gen_path):
            print("generated results-v241.json missing"); sys.exit(2)
        with open(gen_path, encoding="utf-8") as f:
            generated = json.load(f)

        blob = git("cat-file", "blob", f"{REF}:{RESULTS_RELPATH}")
        if blob.returncode != 0:
            print("cannot read committed blob:", blob.stderr); sys.exit(2)
        committed = json.loads(blob.stdout)

        semantically_equal = (generated == committed)
        print(f"    generated == committed (semantic JSON): {semantically_equal}")

        # 4) assert success criteria from the regenerated summary
        s = generated.get("summary", {})
        cc = generated.get("corpus_counts", {})
        total = s.get("TOTAL")
        unexpected = s.get("UNEXPECTED_VERDICTS")
        exc = s.get("exceptions")
        fault = s.get("evaluator_fault")
        frozen_pres = s.get("frozen_v24_preserved", {})
        wb_cons = s.get("wb_oracle_consistent", {})

        print("\n[4] success criteria (regenerated)")
        print(f"    corpus total                : {total}  (expect 148)")
        print(f"    FROZEN_V24 / WB / F1        : {cc.get('frozen_v24')} / {cc.get('wb_probe')} / {cc.get('f1_control')}")
        print(f"    UNEXPECTED_VERDICTS         : {unexpected}  (must be 0)")
        print(f"    exceptions / evaluator_fault: {exc} / {fault}  (must be 0 / 0)")
        print(f"    frozen V2.4 preserved      : {frozen_pres.get('preserved')}/{frozen_pres.get('total')}")
        print(f"    WB oracle consistent        : {wb_cons.get('consistent')}/{wb_cons.get('total')}")

        ok = (semantically_equal and total == 148 and unexpected == 0
              and exc == 0 and fault == 0
              and frozen_pres.get("preserved") == frozen_pres.get("total")
              and wb_cons.get("consistent") == wb_cons.get("total"))
        print("\n" + "=" * 78)
        print(f"PHASE D RESULT: {'PASS' if ok else 'FAIL'}")
        if not semantically_equal:
            print("  (generated output diverged from committed frozen evidence — investigate)")
        sys.exit(0 if ok else 1)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()
