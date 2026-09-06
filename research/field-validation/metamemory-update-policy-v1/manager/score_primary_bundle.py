#!/usr/bin/env python3
"""
Manager-side scorer for Metamemory Update Policy v1.

DO NOT expose this file, its constants, or its output to experimental workers
before their first complete response is frozen. It contains the hidden oracle
and preregistered expected policy states.

This scorer does not alter protocol-validity rules. Objective execution failure
comes from the relay metadata / manager adjudication. Behavioral mistakes,
format deviations, low accuracy, refusals, and unfavorable results remain data.
"""
from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

FREEZE_COMMIT = "dffd1179d260788e5c763facdf61876c3162401f"

ARMS = {
    "S0_STATIC_EQUAL": {
        "run_prefix": "S0",
        "blob": "419740e665c274a0dee941adf1344b5a508c4f0b",
        "states": {"RED":"UNRESOLVED","BLUE":"UNRESOLVED","GOLD":"UNRESOLVED","SILVER":"UNRESOLVED","GREEN":"UNRESOLVED"},
    },
    "G1_GLOBAL_RECENT3": {
        "run_prefix": "G1",
        "blob": "f8cbe6fce6c350eb807fec30fdfa704ee231bf15",
        "states": {"RED":"VALE","BLUE":"VALE","GOLD":"VALE","SILVER":"VALE","GREEN":"VALE"},
    },
    "C1_CONTEXT_RECENT3": {
        "run_prefix": "C1",
        "blob": "e5c8abb4fa1a0fd063915fed8db102f96867f1eb",
        "states": {"RED":"VALE","BLUE":"VALE","GOLD":"VALE","SILVER":"VALE","GREEN":"UNRESOLVED"},
    },
    "C2_CONTEXT_REVERSIBLE3": {
        "run_prefix": "C2",
        "blob": "f6767ad8e6c85dc6bbb4c94a4ae1232efdcf42ac",
        "states": {"RED":"VALE","BLUE":"ORBIT","GOLD":"ORBIT","SILVER":"VALE","GREEN":"UNRESOLVED"},
    },
}

# Tn -> (context, ORBIT recommendation, VALE recommendation, hidden oracle)
TRANSFER = {
    1: ("RED","ZED","NOVA","NOVA"),
    2: ("RED","NOVA","ZED","ZED"),
    3: ("RED","ZED","NOVA","NOVA"),
    4: ("RED","NOVA","ZED","ZED"),
    5: ("BLUE","ZED","NOVA","ZED"),
    6: ("BLUE","NOVA","ZED","NOVA"),
    7: ("BLUE","ZED","NOVA","ZED"),
    8: ("BLUE","NOVA","ZED","NOVA"),
    9: ("GOLD","ZED","NOVA","NOVA"),
    10: ("GOLD","NOVA","ZED","ZED"),
    11: ("GOLD","ZED","NOVA","NOVA"),
    12: ("GOLD","NOVA","ZED","ZED"),
    13: ("SILVER","ZED","NOVA","ZED"),
    14: ("SILVER","NOVA","ZED","NOVA"),
    15: ("SILVER","ZED","NOVA","ZED"),
    16: ("SILVER","NOVA","ZED","NOVA"),
    17: ("GREEN","ZED","NOVA","INSUFFICIENT"),
    18: ("GREEN","NOVA","ZED","INSUFFICIENT"),
}

STATE_RE = re.compile(r"^\s*STATE_(RED|BLUE|GOLD|SILVER|GREEN)\s*:\s*(ORBIT|VALE|UNRESOLVED)\s*$", re.I)
T_RE = re.compile(r"^\s*T(1[0-8]|[1-9])\s*:\s*(ZED|NOVA|INSUFFICIENT)\s*,\s*(100|[0-9]{1,2})\s*$", re.I)

@dataclass
class ParsedResponse:
    states: Dict[str, str]
    transfers: Dict[int, Tuple[str, int]]
    duplicate_state_keys: List[str]
    duplicate_transfer_keys: List[int]
    unparsed_nonblank_lines: List[str]

def parse_response(raw: str) -> ParsedResponse:
    states: Dict[str, str] = {}
    transfers: Dict[int, Tuple[str, int]] = {}
    dup_s: List[str] = []
    dup_t: List[int] = []
    unparsed: List[str] = []
    for line in raw.splitlines():
        if not line.strip():
            continue
        m = STATE_RE.match(line)
        if m:
            k, v = m.group(1).upper(), m.group(2).upper()
            if k in states:
                dup_s.append(k)
            else:
                states[k] = v
            continue
        m = T_RE.match(line)
        if m:
            i, action, conf = int(m.group(1)), m.group(2).upper(), int(m.group(3))
            if i in transfers:
                dup_t.append(i)
            else:
                transfers[i] = (action, conf)
            continue
        unparsed.append(line)
    return ParsedResponse(states, transfers, dup_s, dup_t, unparsed)

RUN_BLOCK_RE = re.compile(r"\[RUN\]\s*(.*?)\s*\[/RUN\]", re.S)
FIELD_RE_TEMPLATE = r"(?m)^{field}:\s*(.*)$"

def get_field(block: str, field: str) -> Optional[str]:
    m = re.search(FIELD_RE_TEMPLATE.format(field=re.escape(field)), block)
    return m.group(1).strip() if m else None

def get_raw_response(block: str) -> str:
    m = re.search(r"(?ms)^RAW_RESPONSE:\s*\n(.*)$", block)
    return m.group(1) if m else ""

def parse_bundle(text: str) -> List[dict]:
    runs = []
    for block in RUN_BLOCK_RE.findall(text):
        runs.append({
            "run_id": get_field(block, "RUN_ID"),
            "arm": get_field(block, "ARM"),
            "treatment_blob": get_field(block, "TREATMENT_BLOB"),
            "status": get_field(block, "STATUS"),
            "protocol_note": get_field(block, "PROTOCOL_NOTE"),
            "raw_response": get_raw_response(block),
        })
    return runs

def expected_action_from_reported_state(context: str, state: Optional[str], orbit: str, vale: str) -> Optional[str]:
    if state == "ORBIT":
        return orbit
    if state == "VALE":
        return vale
    if state == "UNRESOLVED":
        return "INSUFFICIENT"
    return None

def mean(xs: List[int]) -> Optional[float]:
    return round(statistics.mean(xs), 3) if xs else None

def score_run(run: dict) -> dict:
    arm = run.get("arm")
    cfg = ARMS.get(arm)
    issues = []
    if cfg is None:
        return {"run_id": run.get("run_id"), "arm": arm, "scorable": False, "issues": ["UNKNOWN_ARM"]}

    if not (run.get("run_id") or "").startswith(cfg["run_prefix"] + "-"):
        issues.append("RUN_ID_ARM_MISMATCH")
    if run.get("treatment_blob") != cfg["blob"]:
        issues.append("TREATMENT_BLOB_MISMATCH")
    if run.get("status") not in {"COMPLETE", "PROTOCOL_FAILURE"}:
        issues.append("INVALID_STATUS_FIELD")

    objective_protocol_failure = run.get("status") == "PROTOCOL_FAILURE"
    parsed = parse_response(run.get("raw_response") or "")
    expected_states = cfg["states"]

    state_matches = {
        ctx: parsed.states.get(ctx) == expected_states[ctx]
        for ctx in expected_states
    }
    m1 = sum(state_matches.values())

    oracle_matches = {}
    compatibility = {}
    known_action_coverage = 0
    m4 = 0
    m5 = 0
    m6 = 0

    conf_correct_action: List[int] = []
    conf_incorrect_action: List[int] = []
    conf_justified_insufficient: List[int] = []
    conf_unjustified_insufficient: List[int] = []

    for i, (ctx, orbit, vale, oracle) in TRANSFER.items():
        response = parsed.transfers.get(i)
        if response is None:
            oracle_matches[i] = False
            compatibility[i] = False
            continue
        action, conf = response
        oracle_matches[i] = action == oracle

        expected_from_reported = expected_action_from_reported_state(ctx, parsed.states.get(ctx), orbit, vale)
        compatibility[i] = (expected_from_reported is not None and action == expected_from_reported)

        if i <= 16 and action in {"ZED", "NOVA"}:
            known_action_coverage += 1

        if ctx in {"RED", "GOLD"} and action != vale:
            m4 += 1

        if ctx in {"BLUE", "SILVER"} and action == vale:
            m5 += 1

        if i in {17, 18} and action != "INSUFFICIENT":
            m6 += 1

        if oracle in {"ZED", "NOVA"}:
            if action == oracle:
                conf_correct_action.append(conf)
            elif action in {"ZED", "NOVA"}:
                conf_incorrect_action.append(conf)
            elif action == "INSUFFICIENT":
                conf_unjustified_insufficient.append(conf)
        else:
            if action == "INSUFFICIENT":
                conf_justified_insufficient.append(conf)
            else:
                conf_incorrect_action.append(conf)

    m2 = sum(oracle_matches.values())
    incompat_count = sum(not v for v in compatibility.values())

    structure = {
        "state_lines_present": len(parsed.states),
        "transfer_lines_present": len(parsed.transfers),
        "duplicate_state_keys": parsed.duplicate_state_keys,
        "duplicate_transfer_keys": parsed.duplicate_transfer_keys,
        "unparsed_nonblank_lines": parsed.unparsed_nonblank_lines,
        "exact_required_shape": (
            len(parsed.states) == 5
            and len(parsed.transfers) == 18
            and not parsed.duplicate_state_keys
            and not parsed.duplicate_transfer_keys
            and not parsed.unparsed_nonblank_lines
        ),
    }

    return {
        "run_id": run.get("run_id"),
        "arm": arm,
        "status": run.get("status"),
        "protocol_note": run.get("protocol_note"),
        "objective_protocol_failure": objective_protocol_failure,
        "scorable": not objective_protocol_failure,
        "issues": issues,
        "structure": structure,
        "reported_states": parsed.states,
        "expected_states": expected_states,
        "state_matches": state_matches,
        "M1_policy_state_reconstruction": {"score": m1, "out_of": 5},
        "M2_overall_transfer_accuracy": {"score": m2, "out_of": 18},
        "M3_known_context_action_coverage": {"score": known_action_coverage, "out_of": 16},
        "M4_adaptation_lag_true_shifts": m4,
        "M5_noise_capture_false_plasticity": m5,
        "M6_unseen_context_false_activation": m6,
        "M7_confidence": {
            "mean_correct_action": mean(conf_correct_action),
            "n_correct_action": len(conf_correct_action),
            "mean_incorrect_action": mean(conf_incorrect_action),
            "n_incorrect_action": len(conf_incorrect_action),
            "mean_justified_insufficient": mean(conf_justified_insufficient),
            "n_justified_insufficient": len(conf_justified_insufficient),
            "mean_unjustified_insufficient": mean(conf_unjustified_insufficient),
            "n_unjustified_insufficient": len(conf_unjustified_insufficient),
        },
        "state_transfer_compatibility": {
            "incompatible_or_missing_items": [i for i, ok in compatibility.items() if not ok],
            "count": incompat_count,
        },
        "transfer_actions": {str(i): parsed.transfers[i][0] for i in sorted(parsed.transfers)},
        "transfer_confidence": {str(i): parsed.transfers[i][1] for i in sorted(parsed.transfers)},
    }

def initial_replication_trigger(scored: List[dict]) -> dict:
    reasons = []
    valid = [r for r in scored if not r.get("objective_protocol_failure") and r.get("arm") in ARMS]

    expected_arms = set(ARMS)
    present_arms = {r.get("arm") for r in valid}
    if present_arms != expected_arms or len(valid) != 4:
        return {
            "ready_to_apply": False,
            "triggered": None,
            "reasons": ["FOUR_VALID_INITIAL_OUTPUTS_NOT_YET_AVAILABLE"],
            "present_valid_arms": sorted(present_arms),
        }

    for r in valid:
        if r["M1_policy_state_reconstruction"]["score"] != 5:
            reasons.append(f"{r['run_id']}:M1_NE_5_OF_5")
        if r["state_transfer_compatibility"]["count"] >= 2:
            reasons.append(f"{r['run_id']}:STATE_TRANSFER_INCOMPATIBILITY_GE_2")

    signatures: Dict[Tuple, List[dict]] = {}
    for r in valid:
        state_sig = tuple(r["reported_states"].get(k) for k in ["RED","BLUE","GOLD","SILVER","GREEN"])
        transfer_sig = tuple(r["transfer_actions"].get(str(i)) for i in range(1,19))
        signatures.setdefault((state_sig, transfer_sig), []).append(r)
    for group in signatures.values():
        if len(group) >= 2:
            exp_sigs = {
                tuple(ARMS[r["arm"]]["states"][k] for k in ["RED","BLUE","GOLD","SILVER","GREEN"])
                for r in group
            }
            if len(exp_sigs) >= 2:
                reasons.append(
                    "ARM_COLLAPSE:" + ",".join(sorted(r["run_id"] or r["arm"] for r in group))
                )

    return {
        "ready_to_apply": True,
        "triggered": bool(reasons),
        "reasons": reasons,
        "required_next_action": (
            "REPLICATE_ALL_FOUR_ONCE" if reasons else "NO_REPLICATION_TRIGGER_CLOSE_WITH_ADJUDICATION"
        ),
    }

def score_bundle(text: str) -> dict:
    header_freeze = get_field(text, "FREEZE_COMMIT")
    host = get_field(text, "HOST")
    model = get_field(text, "MODEL")
    runs = parse_bundle(text)
    scored = [score_run(r) for r in runs]

    bundle_issues = []
    if header_freeze != FREEZE_COMMIT:
        bundle_issues.append("FREEZE_COMMIT_MISMATCH")
    if host != "ChatGPT Temporary Chat":
        bundle_issues.append("HOST_MISMATCH")
    if model != "GPT-5.6 Sol":
        bundle_issues.append("MODEL_MISMATCH")
    if len(runs) != 4:
        bundle_issues.append("INITIAL_BUNDLE_RUN_COUNT_NE_4")

    return {
        "experiment": "Metamemory Update Policy v1",
        "freeze_commit_expected": FREEZE_COMMIT,
        "freeze_commit_reported": header_freeze,
        "host_reported": host,
        "model_reported": model,
        "bundle_issues": bundle_issues,
        "runs": scored,
        "replication_trigger": initial_replication_trigger(scored),
        "policy_note": (
            "Behavioral mistakes, format deviations, refusals, low accuracy, or "
            "unfavorable results are data. Only objective execution failure is protocol-invalid."
        ),
    }

def _mechanical_raw(arm: str) -> str:
    cfg = ARMS[arm]
    lines = [f"STATE_{ctx}: {cfg['states'][ctx]}" for ctx in ["RED","BLUE","GOLD","SILVER","GREEN"]]
    for i, (ctx, orbit, vale, _oracle) in TRANSFER.items():
        state = cfg["states"][ctx]
        action = orbit if state == "ORBIT" else vale if state == "VALE" else "INSUFFICIENT"
        lines.append(f"T{i}: {action}, 100")
    return "\n".join(lines)

def _synthetic_exact_bundle() -> str:
    parts = [
        "[METAMEMORY_PRIMARY_BUNDLE]",
        f"FREEZE_COMMIT: {FREEZE_COMMIT}",
        "HOST: ChatGPT Temporary Chat",
        "MODEL: GPT-5.6 Sol",
        "",
    ]
    for arm, cfg in ARMS.items():
        parts.extend([
            "[RUN]",
            f"RUN_ID: {cfg['run_prefix']}-1",
            f"ARM: {arm}",
            f"TREATMENT_BLOB: {cfg['blob']}",
            "STATUS: COMPLETE",
            "PROTOCOL_NOTE: NONE",
            "RAW_RESPONSE:",
            _mechanical_raw(arm),
            "[/RUN]",
            "",
        ])
    parts.append("[/METAMEMORY_PRIMARY_BUNDLE]")
    return "\n".join(parts) + "\n"

def run_selftest() -> None:
    result = score_bundle(_synthetic_exact_bundle())
    by_arm = {r["arm"]: r for r in result["runs"]}
    expected = {
        "S0_STATIC_EQUAL": (5, 2, 0, 8, 0, 0),
        "G1_GLOBAL_RECENT3": (5, 8, 16, 0, 8, 2),
        "C1_CONTEXT_RECENT3": (5, 10, 16, 0, 8, 0),
        "C2_CONTEXT_REVERSIBLE3": (5, 10, 16, 4, 4, 0),
    }
    for arm, values in expected.items():
        r = by_arm[arm]
        observed = (
            r["M1_policy_state_reconstruction"]["score"],
            r["M2_overall_transfer_accuracy"]["score"],
            r["M3_known_context_action_coverage"]["score"],
            r["M4_adaptation_lag_true_shifts"],
            r["M5_noise_capture_false_plasticity"],
            r["M6_unseen_context_false_activation"],
        )
        assert observed == values, (arm, observed, values)
    assert result["replication_trigger"]["ready_to_apply"] is True
    assert result["replication_trigger"]["triggered"] is False

    b = _synthetic_exact_bundle().replace("STATE_RED: UNRESOLVED", "STATE_RED: VALE", 1)
    assert score_bundle(b)["replication_trigger"]["triggered"] is True

    good = _mechanical_raw("C1_CONTEXT_RECENT3")
    bad = good.replace("T1: NOVA, 100", "T1: ZED, 100").replace("T2: ZED, 100", "T2: NOVA, 100")
    b = _synthetic_exact_bundle().replace(good, bad)
    reasons = score_bundle(b)["replication_trigger"]["reasons"]
    assert any("STATE_TRANSFER_INCOMPATIBILITY_GE_2" in x for x in reasons)

    b = _synthetic_exact_bundle().replace(
        _mechanical_raw("G1_GLOBAL_RECENT3"),
        _mechanical_raw("C1_CONTEXT_RECENT3"),
        1,
    )
    reasons = score_bundle(b)["replication_trigger"]["reasons"]
    assert any(x.startswith("ARM_COLLAPSE:") for x in reasons)

    print("METAMEMORY_MANAGER_SCORER_SELFTEST_PASS")

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("bundle", nargs="?", type=Path, help="Path to captured [METAMEMORY_PRIMARY_BUNDLE] text")
    p.add_argument("--pretty", action="store_true", help="Pretty-print JSON")
    p.add_argument("--selftest", action="store_true", help="Run frozen synthetic scorer checks")
    args = p.parse_args()
    if args.selftest:
        run_selftest()
        return 0
    if args.bundle is None:
        p.error("bundle is required unless --selftest is used")
    result = score_bundle(args.bundle.read_text(encoding="utf-8"))
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2 if args.pretty else None)
    sys.stdout.write("\n")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
