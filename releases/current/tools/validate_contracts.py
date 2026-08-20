#!/usr/bin/env python3
"""Reference semantic validator for ENA v0.3.2 operational contracts.

This validator deliberately checks only a few high-ROI cross-object invariants that
JSON Schema alone cannot prove. Structural schema PASS is not semantic truth.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

SCOPE_KEYS = ("host", "runtime_instance", "model_binding", "route", "configuration", "epoch", "time_interval", "task_scope")
DEFAULT_FIXTURES = Path(__file__).with_name("contract-fixtures.v1.json")


def load(path: str | Path) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        value = json.load(f)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def result(ok: bool, code: str, details: Any = None) -> dict[str, Any]:
    out = {"ok": ok, "code": code}
    if details not in (None, [], {}):
        out["details"] = details
    return out


def _scope_mismatches(observed: dict[str, Any], claimed: dict[str, Any]) -> list[dict[str, Any]]:
    mismatches: list[dict[str, Any]] = []
    for key in SCOPE_KEYS:
        c = claimed.get(key)
        if c in (None, "", "UNKNOWN"):
            continue
        o = observed.get(key)
        if o != c:
            mismatches.append({"field": key, "observed": o, "claimed": c})
    return mismatches


def validate_support(claim: dict[str, Any], support: dict[str, Any]) -> dict[str, Any]:
    if support.get("claim_ref") != claim.get("claim_id"):
        return result(False, "CLAIM_REF_MISMATCH")
    if support.get("support_status") not in {"SUPPORTS", "PARTIAL"}:
        return result(True, "NO_POSITIVE_SUPPORT_CLAIMED")

    independence = support.get("independence_basis") or {}
    claimed_independent_count = independence.get("claimed_independent_count")
    source_origins = independence.get("source_origins") or []
    if claimed_independent_count is not None:
        unique_origins = {str(x) for x in source_origins if x not in (None, "", "UNKNOWN")}
        if claimed_independent_count > len(unique_origins):
            return result(
                False,
                "INDEPENDENCE_OVERCLAIMED",
                {"claimed_independent_count": claimed_independent_count, "unique_source_origins": sorted(unique_origins)},
            )

    observed = support.get("observed_scope") or {}
    claimed = support.get("claimed_scope") or claim.get("scope") or {}
    mismatches = _scope_mismatches(observed, claimed)
    if not mismatches:
        return result(True, "SUPPORT_SCOPE_DIRECT_MATCH")
    transfer = support.get("transfer_basis") or {}
    if transfer.get("required") is True and transfer.get("type") and (transfer.get("evidence_refs") or []):
        return result(True, "SUPPORT_SCOPE_TRANSFER_DECLARED", {"mismatches": mismatches})
    return result(False, "TRANSFER_EVIDENCE_REQUIRED", {"mismatches": mismatches})


def validate_obligation(obligation: dict[str, Any]) -> dict[str, Any]:
    trigger = obligation.get("trigger") or {}
    material = obligation.get("materiality") == "MATERIAL"
    observed = trigger.get("observed") is True
    status = obligation.get("status")
    blocked_claims = obligation.get("required_before_claim_refs") or []
    if material and observed and status in {"PENDING", "FAILED", "UNKNOWN"}:
        return result(False, "MATERIAL_OBLIGATION_BLOCKS_CLAIM", {"claim_refs": blocked_claims, "status": status})
    if status == "SATISFIED" and not (obligation.get("closure_evidence_refs") or []):
        return result(False, "SATISFIED_WITHOUT_CLOSURE_EVIDENCE")
    if status in {"NOT_REQUIRED", "DEFERRED_AUTHORIZED"} and not obligation.get("resolution_reason"):
        return result(False, "CLOSURE_STATUS_REQUIRES_REASON")
    return result(True, "OBLIGATION_STATE_ACCEPTABLE")


def validate_recovery(transition: dict[str, Any]) -> dict[str, Any]:
    state = (transition.get("state_restore") or {}).get("result")
    history = (transition.get("history_continuity") or {}).get("status")
    claim_scope = (transition.get("recovery_claim") or {}).get("scope")
    if state != "SUCCESS":
        return result(False, "STATE_RESTORE_NOT_SUCCESSFUL", {"state_result": state})
    if claim_scope == "STATE_ONLY":
        return result(True, "STATE_ONLY_RECOVERY_SUPPORTED", {"history_status": history})
    if claim_scope == "STATE_AND_HISTORY":
        if history == "PRESERVED":
            return result(True, "STATE_AND_HISTORY_RECOVERY_SUPPORTED")
        return result(False, "FULL_RECOVERY_REQUIRES_PRESERVED_HISTORY", {"history_status": history})
    if claim_scope == "STATE_WITH_VISIBLE_HISTORY_GAP":
        if history in {"GAP_VISIBLE", "PARTIAL"}:
            return result(True, "RECOVERY_WITH_VISIBLE_HISTORY_GAP_SUPPORTED")
        return result(False, "VISIBLE_GAP_CLAIM_REQUIRES_GAP_EVIDENCE", {"history_status": history})
    return result(False, "UNKNOWN_RECOVERY_CLAIM_SCOPE", {"claim_scope": claim_scope})


def _run_fixture(case: dict[str, Any]) -> dict[str, Any]:
    mode = case.get("mode")
    payload = case.get("input") or {}
    if mode == "support":
        actual = validate_support(payload.get("claim") or {}, payload.get("support") or {})
    elif mode == "obligation":
        actual = validate_obligation(payload.get("obligation") or {})
    elif mode == "recovery":
        actual = validate_recovery(payload.get("transition") or {})
    else:
        actual = result(False, "UNKNOWN_FIXTURE_MODE", {"mode": mode})
    expected = case.get("expect") or {}
    passed = actual.get("ok") == expected.get("ok") and actual.get("code") == expected.get("code")
    return {"id": case.get("id"), "passed": passed, "expected": expected, "actual": actual}


def run_selftest(fixtures_path: str | Path) -> dict[str, Any]:
    fixture_doc = load(fixtures_path)
    cases = fixture_doc.get("cases") or []
    results = [_run_fixture(case) for case in cases]
    failed = [r for r in results if not r["passed"]]
    return {
        "ok": not failed,
        "code": "SELFTEST_PASS" if not failed else "SELFTEST_FAIL",
        "fixture_version": fixture_doc.get("fixture_version"),
        "total": len(results),
        "failed": len(failed),
        "results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="mode", required=True)
    p = sub.add_parser("support"); p.add_argument("claim"); p.add_argument("support")
    p = sub.add_parser("obligation"); p.add_argument("obligation")
    p = sub.add_parser("recovery"); p.add_argument("transition")
    p = sub.add_parser("selftest"); p.add_argument("fixtures", nargs="?", default=str(DEFAULT_FIXTURES))
    args = parser.parse_args()
    if args.mode == "support":
        out = validate_support(load(args.claim), load(args.support))
    elif args.mode == "obligation":
        out = validate_obligation(load(args.obligation))
    elif args.mode == "recovery":
        out = validate_recovery(load(args.transition))
    else:
        out = run_selftest(args.fixtures)
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0 if out["ok"] else 2


if __name__ == "__main__":
    sys.exit(main())
