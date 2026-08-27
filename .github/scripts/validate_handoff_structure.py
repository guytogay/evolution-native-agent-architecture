#!/usr/bin/env python3
"""Validate ENA handoff framework/record/methodology separation.

This checks structural invariants, not project semantic truth.
"""

from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[2]
HANDOFF = ROOT / "research" / "handoffs"

errors = []

def require(cond, msg):
    if not cond:
        errors.append(msg)

framework_files = [
    "README.md",
    "CURRENT-HANDOFF.yaml",
    "HANDOFF-PROTOCOL.md",
    "REQUIRED-TAKEOVER-CONTEXT.yaml",
    "PROJECT-MANAGEMENT-DISCIPLINE.md",
    "records/README.md",
]
for rel in framework_files:
    require((HANDOFF / rel).is_file(), f"missing framework file: research/handoffs/{rel}")

# Dated/session-specific records belong below records/, not at framework root.
for child in HANDOFF.iterdir():
    if child.is_dir() and child.name != "records":
        if re.match(r"^20\d\d-", child.name):
            errors.append(f"dated handoff record at framework root: {child}")

with (HANDOFF / "CURRENT-HANDOFF.yaml").open(encoding="utf-8") as f:
    current = yaml.safe_load(f)

require(current.get("status") == "CURRENT_HANDOFF_POINTER_AND_TAKEOVER_CONTRACT",
        "CURRENT-HANDOFF must be pointer + takeover contract")
framework = current.get("handoff_framework", {})
require(framework.get("protocol") == "research/handoffs/HANDOFF-PROTOCOL.md",
        "CURRENT-HANDOFF must point directly to canonical handoff protocol")
require(framework.get("required_takeover_context") == "research/handoffs/REQUIRED-TAKEOVER-CONTEXT.yaml",
        "CURRENT-HANDOFF must expose required takeover context")
require(framework.get("project_management_discipline") == "research/handoffs/PROJECT-MANAGEMENT-DISCIPLINE.md",
        "CURRENT-HANDOFF must expose project-management discipline")

pm = current.get("project_methodology_required", {})
require(pm.get("required") is True, "project methodology must be explicitly required")

contract = current.get("receiver_contract", {})
for key in [
    "inherit_project_state",
    "inherit_handoff_protocol",
    "inherit_project_management_discipline",
    "inherit_project_methodology",
    "read_current_record",
    "live_reverify_refs_and_exact_identities",
]:
    require(contract.get(key) == "REQUIRED", f"receiver contract must require {key}")

record = current.get("current_handoff_record", {})
record_root = record.get("record_root", "")
require(record_root.startswith("research/handoffs/records/"),
        "current handoff record must live under research/handoffs/records/")

record_dir = ROOT / record_root
require(record_dir.is_dir(), f"current handoff record directory missing: {record_root}")

required_record_files = [
    "HANDOFF-START-HERE.md",
    "HANDOFF-MANIFEST.yaml",
    "PROJECT-STATE.md",
    "RECENT-THREE-ROUNDS.md",
    "FILE-CATALOG.md",
    "HANDOFF-READBACK.md",
]
for name in required_record_files:
    require((record_dir / name).is_file(), f"current record missing {name}")

# Reusable method must not be trapped inside one record.
for forbidden in [
    "PROJECT-MANAGEMENT-LESSONS.md",
    "PROJECT-MANAGEMENT-DISCIPLINE.md",
    "HANDOFF-PROTOCOL.md",
    "REQUIRED-TAKEOVER-CONTEXT.yaml",
]:
    require(not (record_dir / forbidden).exists(),
            f"reusable method incorrectly stored in current record: {forbidden}")

with (HANDOFF / "REQUIRED-TAKEOVER-CONTEXT.yaml").open(encoding="utf-8") as f:
    required_ctx = yaml.safe_load(f)
require(required_ctx.get("project_methodology", {}).get("required") is True,
        "REQUIRED-TAKEOVER-CONTEXT must require project methodology")
require(required_ctx.get("handoff_framework", {}).get("required") is True,
        "REQUIRED-TAKEOVER-CONTEXT must require handoff framework")

# Compatibility pointer may exist, but it must not claim canonical authority.
compat = ROOT / "research" / "methodology" / "SESSION-HANDOFF-DISCIPLINE.md"
if compat.exists():
    text = compat.read_text(encoding="utf-8")
    require("COMPATIBILITY_POINTER / NOT_CANONICAL_METHOD" in text,
            "legacy methodology handoff path must be a non-canonical compatibility pointer")
    require("research/handoffs/HANDOFF-PROTOCOL.md" in text,
            "legacy handoff pointer must route to canonical root protocol")

if errors:
    print("HANDOFF_STRUCTURE_VERDICT=FAIL")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print("HANDOFF_STRUCTURE_VERDICT=PASS")
print(f"current_record={record_root}")
print("project_methodology_required=YES")
print("handoff_protocol_required=YES")
print("project_management_discipline_required=YES")
print("record_method_separation=PASS")
