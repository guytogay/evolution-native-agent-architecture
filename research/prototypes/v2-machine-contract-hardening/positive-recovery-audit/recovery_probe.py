#!/usr/bin/env python3
"""Did the composed contract really sacrifice five legitimate positives?

This is a correction probe. It exists because two inbox notes asserted, as measured fact, that an
independent round classified three of the five positives v2.2 reported as sacrificed
(`CONFIRMED_MATERIAL_DEFECT`, false BLOCK). No independent round ever examined those five fixtures:
the v2.4 reconciliation adjudicated its own independently authored corpus (I01-I16, O01-O04), and a
repository-wide search finds the five ids only in the v2.2/v2.3/v2.4/v2.4.1 result files and the
shipped corpus. The assertion was a misattribution. This probe replaces it with a measurement.

Background
    V2.2 (2026-08-20) reported `TOTAL_POSITIVE_PRESERVED = 14/19` and explained the five failures as
    "the intended cost of closure, not a contract bug" (P1, P5, P6 BLOCKED; P7, P9 UNKNOWN).
    V2.3 kept `kind: POSITIVE` on those five but re-authored their `expected_verdict` to
    BLOCK/UNKNOWN and replaced the positive-preservation metric with per-category verdict
    correctness. V2.4 and V2.4.1 then report all five as `preserved: True` — measured against the
    re-authored expectation, not against the original claim that they are legitimate positives that
    should pass. The shipped corpus still carries all five as `kind: POSITIVE` with
    `provenance: DSH_HISTORICAL_V2` and no expected verdict.

Hypothesis under test
    Each of the five references an artifact its own payload never supplies (a support relation, an
    evidence registry, a root registry). Supplying exactly the artifacts the fixture's own
    references name should make it pass. If so, the "sacrificed positive" is an incompletely written
    fixture — the cost of closure is "incomplete positives now fail closed", which is the documented
    intent, not the loss of five legitimate cases.

Falsification criteria (stated before results)
    F1  The as-is control must reproduce the recorded verdicts 3x BLOCK + 2x UNKNOWN. If it does
        not, this harness is not evaluating the frozen corpus and every result below is void.
    F2  The hypothesis is FALSIFIED if any completed variant is not OK. Codes are printed so a
        refusal can be read rather than assumed.
    F3  A completed variant counts only when the sole change is the addition of artifacts named by
        references already present. No field may be edited, removed or re-typed; the structural
        check below asserts that, and the as-is payload is evaluated again in the same run.

Read-only against everything it imports: the frozen fixtures and both contract implementations are
imported, never modified. `releases/current/` is untouched.
"""
from __future__ import annotations

import copy
import json
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROTO = HERE.parent


def _find_repo(start: Path) -> Path:
    cur = start
    for _ in range(8):
        if (cur / "releases" / "current" / "tools").exists():
            return cur
        cur = cur.parent
    raise SystemExit("could not locate the repository root (releases/current/tools)")


REPO = _find_repo(HERE)

for path in (PROTO / "v2.4", PROTO, PROTO / "v2.3", PROTO / "v2.2", PROTO / "v2.1",
             REPO / "releases" / "current" / "tools"):
    sys.path.insert(0, str(path))

from fixtures import get_fixtures as get_v2_fixtures          # noqa: E402
from successor_contract import evaluate                        # noqa: E402

EVAL_TIME = date(2026, 8, 20)
TARGETS = ("P1-supported-with-refs", "P5-completion-satisfied", "P6-nonmaterial-obligation-ok",
           "P7-recovery-with-history-evidence", "P9-independence-distinct-roots")
RECORDED_AS_IS = {"BLOCK": 3, "UNKNOWN": 2}


def complete(fixture: dict) -> dict:
    """Add only the artifacts the fixture's own references name. Never edit an existing field."""
    fx = copy.deepcopy(fixture)
    p = fx["payload"]
    claim = p.get("claim")
    scope = dict(claim.get("scope", {})) if claim else {}
    support_refs = list(claim.get("support_relation_refs", [])) if claim else []

    if support_refs:
        entries = list(p.get("support_registry") or [])
        for ref in support_refs:
            entries.append({
                "support_id": ref,
                "claim_ref": claim["claim_id"],
                "evidence_refs": [f"E-{ref}"],
                "support_status": "SUPPORTS",
                "observed_scope": dict(scope),
                "claimed_scope": dict(scope),
            })
        p["support_registry"] = entries
        for ref in support_refs:
            p.setdefault("evidence_registry", {})[f"E-{ref}"] = {
                "root_provenance": f"ROOT-{ref}", "derived_from": None}

    transition = p.get("transition")
    if transition:
        refs = list(transition.get("state_restore", {}).get("evidence_refs", [])) \
            + list(transition.get("history_continuity", {}).get("evidence_refs", []))
        registry = p.setdefault("evidence_registry", {})
        for ref in refs:
            registry.setdefault(ref, {"root_provenance": f"ROOT-{ref}", "derived_from": None})

    support = p.get("support")
    if isinstance(support, dict):
        registry = p.setdefault("evidence_registry", {})
        for ref in support.get("evidence_refs", []):
            registry.setdefault(ref, {"root_provenance": f"ROOT-{ref}", "derived_from": None})
        roots = list(support.get("independence_basis", {}).get("root_provenance", []))
        if roots:
            p["root_registry"] = [{"id": root, "actual_origin": f"O-{root}"} for root in roots]

    for obligation in p.get("obligations") or []:
        registry = p.setdefault("evidence_registry", {})
        for ref in obligation.get("closure_evidence_refs", []):
            registry.setdefault(ref, {"root_provenance": f"ROOT-{ref}", "derived_from": None})

    return fx


def structural_check(before: dict, after: dict) -> list[str]:
    """F3: every pre-existing leaf must survive unchanged in the completed payload."""
    problems: list[str] = []

    def walk(a, b, path=""):
        if isinstance(a, dict):
            if not isinstance(b, dict):
                problems.append(f"{path}: type changed")
                return
            for key, value in a.items():
                if key not in b:
                    problems.append(f"{path}.{key}: field removed")
                else:
                    walk(value, b[key], f"{path}.{key}")
        elif isinstance(a, list):
            if not isinstance(b, list) or len(b) < len(a):
                problems.append(f"{path}: list shortened or retyped")
                return
            for index, value in enumerate(a):
                walk(value, b[index], f"{path}[{index}]")
        elif a != b:
            problems.append(f"{path}: value changed {a!r} -> {b!r}")

    walk(before.get("payload", {}), after.get("payload", {}))
    return problems


def main() -> int:
    payloads = {fx["id"]: fx for fx in get_v2_fixtures()}
    missing = [name for name in TARGETS if name not in payloads]
    if missing:
        print(f"FATAL: fixtures not found: {missing}")
        return 2

    rows = []
    seen_as_is: dict[str, int] = {}
    recovery_ok = True
    print(f"{'fixture':<40} {'as-is':<30} {'completed':<22} structure")
    print("-" * 112)

    for name in TARGETS:
        fixture = payloads[name]
        completed = complete(fixture)
        problems = structural_check(fixture, completed)
        state_before, codes_before = evaluate(fixture, EVAL_TIME)
        state_after, codes_after = evaluate(completed, EVAL_TIME)
        seen_as_is[state_before] = seen_as_is.get(state_before, 0) + 1

        print(f"{name:<40} {(state_before + ' ' + str(codes_before[:1])):<30} "
              f"{state_after:<22} {'clean' if not problems else 'VIOLATION'}")
        rows.append({"id": name, "as_is": state_before, "as_is_codes": codes_before,
                     "completed": state_after, "completed_codes": codes_after,
                     "structural_problems": problems,
                     "added_keys": sorted(set(completed["payload"]) - set(fixture["payload"]))})
        if state_after != "OK" or problems:
            recovery_ok = False

    # ---- negative control: the acceptance must come from resolving the refs, not from the mere
    # presence of a registry. Point P1's supplied support at a different claim; a contract that
    # accepts that too would make this probe measure nothing about resolution.
    p1 = payloads["P1-supported-with-refs"]
    mismatched = complete(p1)
    mismatched["payload"]["support_registry"][0]["claim_ref"] = "C-NOT-P1"
    mismatch_state, mismatch_codes = evaluate(mismatched, EVAL_TIME)
    print(f"{'NEGATIVE: P1 support bound to another claim':<40} {'(registry supplied, wrong target)':<30} "
          f"{mismatch_state:<22} "
          f"{'expected BLOCK' if mismatch_state == 'BLOCK' else 'PROBE TOO WEAK'}")
    negative_ok = mismatch_state == "BLOCK"

    print("-" * 112)
    control_ok = seen_as_is == RECORDED_AS_IS
    if control_ok:
        print(f"F1 holds: as-is control reproduces the recorded verdicts {seen_as_is}")
    else:
        print(f"F1 FAILED: as-is produced {seen_as_is}, recorded is {RECORDED_AS_IS} — results void")

    if recovery_ok:
        print("F2 holds: every completed variant is accepted (OK) with only added artifacts")
        print("=> the five 'sacrificed positives' are incompletely written fixtures, not lost")
        print("   legitimate cases: the composed contract accepts the same cases once their own")
        print("   references resolve.")
    else:
        print("F2 FALSIFIED for at least one fixture: a registry-carrying positive is still")
        print("   refused; read the codes above.")

    if not negative_ok:
        print(f"F4 FAILED: a supplied registry with a wrong claim target returned "
              f"{mismatch_state} {mismatch_codes[:1]}; the probe would accept cases it should not")

    out = HERE / "recovery.json"
    out.write_text(json.dumps({
        "question": "were five legitimate positives sacrificed by the composed contract, or were "
                    "the fixtures never completed for it?",
        "eval_time": EVAL_TIME.isoformat(),
        "as_is_control": seen_as_is,
        "F1_as_is_matches_recorded": control_ok,
        "F2_all_completed_accepted": recovery_ok,
        "F4_negative_control_blocks": negative_ok,
        "negative_control": {"id": "P1 with support_registry bound to C-NOT-P1",
                             "state": mismatch_state, "codes": mismatch_codes},
        "rows": rows,
    }, indent=2) + "\n", encoding="utf-8")
    print(f"receipt: {out.relative_to(REPO)}")
    return 0 if (control_ok and recovery_ok and negative_ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
