#!/usr/bin/env python3
"""Reference semantic validator for ENA v0.3.0 Candidate 2 prototypes.

This validator deliberately checks only a few high-ROI cross-object invariants that
JSON Schema alone cannot prove. Structural schema PASS is not semantic truth.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

SCOPE_KEYS = (
    "host",
    "runtime_instance",
    "model_binding",
    "route",
    "configuration",
    "epoch",
    "time_interval",
    "task_scope",
)


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

    observed = support.get("observed_scope") or {}
    claimed = support.get("claimed_scope") or claim.get("scope") or {}
    mismatches = _scope_mismatches(observed, claimed)

    if not mismatches:
        return result(True, "SUPPORT_SCOPE_DIRECT_MATCH")

    transfer = support.get("transfer_basis") or {}
    transfer_evidence = transfer.get("evidence_refs") or []
    transfer_type = transfer.get("type")
    transfer_required = transfer.get("required") is True

    if transfer_required and transfer_type and transfer_evidence:
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


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="mode", required=True)

    p = sub.add_parser("support")
    p.add_argument("claim")
    p.add_argument("support")

    p = sub.add_parser("obligation")
    p.add_argument("obligation")

    p = sub.add_parser("recovery")
    p.add_argument("transition")

    args = parser.parse_args()

    if args.mode == "support":
        out = validate_support(load(args.claim), load(args.support))
    elif args.mode == "obligation":
        out = validate_obligation(load(args.obligation))
    else:
        out = validate_recovery(load(args.transition))

    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0 if out["ok"] else 2


if __name__ == "__main__":
    sys.exit(main())
