#!/usr/bin/env python3
"""Validate ENA handoff framework/record/mode separation.

This checks structural invariants, not project semantic truth.

The validator intentionally follows the current role-scoped continuation model:
- normal continuation is lightweight by default;
- deep succession carries a structured record when continuity risk warrants it;
- fresh independent validation must not inherit project-manager context before its first response.
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

require(current.get("status") == "CURRENT_DEEP_SUCCESSION_POINTER",
        "CURRENT-HANDOFF must be the current deep-succession router")

normal = current.get("normal_continuation", {})
require(normal.get("default_entry") == "NOW.md",
        "normal continuation must enter through NOW.md")
require(normal.get("full_handoff_required_by_default") is False,
        "full handoff must not be required for normal continuation")

framework = current.get("handoff_framework", {})
require(framework.get("protocol") == "research/handoffs/HANDOFF-PROTOCOL.md",
        "CURRENT-HANDOFF must point directly to canonical handoff protocol")
require(framework.get("required_takeover_context") == "research/handoffs/REQUIRED-TAKEOVER-CONTEXT.yaml",
        "CURRENT-HANDOFF must expose required takeover context")
require(framework.get("project_management_discipline") == "research/handoffs/PROJECT-MANAGEMENT-DISCIPLINE.md",
        "CURRENT-HANDOFF must expose project-management discipline")

contract = current.get("receiver_contract", {})
require(contract.get("ask_user_to_repeat_persisted_background") == "FORBIDDEN",
        "deep successor must not ask the user to repeat persisted background")
require(contract.get("reverify_live_mutable_facts_before_writes") == "REQUIRED",
        "deep successor must reverify mutable live facts before writes")
require(contract.get("preserve_negative_and_null_results") == "REQUIRED",
        "deep successor must preserve negative/null results")
require(contract.get("use_full_handoff_for_fresh_validator") == "FORBIDDEN",
        "fresh validator must not inherit full project-manager handoff")

record = current.get("current_handoff_record", {})
record_root = record.get("record_root", "")
require(record_root.startswith("research/handoffs/records/"),
        "current handoff record must live under research/handoffs/records/")
require(record.get("state") == "DEEP_PROJECT_SESSION_SUCCESSION_COMPLETE",
        "current deep handoff record must be marked complete")
require(record.get("readback_state") == "PASS",
        "current deep handoff must have successful postmerge readback")

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

# Reusable method must not be trapped inside one occurrence record.
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

require(required_ctx.get("status") == "CANONICAL_ROLE_SCOPED_TAKEOVER_CONTEXT",
        "REQUIRED-TAKEOVER-CONTEXT must use the role-scoped continuation model")

modes = required_ctx.get("modes", {})
normal_mode = modes.get("normal_continuation", {})
deep_mode = modes.get("deep_project_session_succession", {})
fresh_mode = modes.get("fresh_independent_validation", {})

require(normal_mode.get("default") is True,
        "normal continuation must be the default mode")
require("NOW.md" in normal_mode.get("required", []),
        "normal continuation must require NOW.md")
require(normal_mode.get("full_repository_audit") is False,
        "normal continuation must not require a full repository audit")
require(normal_mode.get("branch_census") is False,
        "normal continuation must not require a branch census")

require(deep_mode.get("default") is False,
        "deep succession must be exceptional rather than default")
deep_required = deep_mode.get("required", [])
for item in [
    "NOW.md",
    "research/handoffs/CURRENT-HANDOFF.yaml",
    "CURRENT_HANDOFF_RECORD_START_HERE",
    "CURRENT_HANDOFF_RECORD_MANIFEST",
    "CURRENT_HANDOFF_RECORD_PROJECT_STATE",
    "CURRENT_HANDOFF_RECORD_RECENT_ROUNDS",
    "CURRENT_HANDOFF_RECORD_FILE_CATALOG",
]:
    require(item in deep_required, f"deep succession must require {item}")

deep_receiver = deep_mode.get("receiver_requirements", [])
for item in [
    "LIVE_REVERIFY_MUTABLE_FACTS_BEFORE_WRITES",
    "DO_NOT_ASK_USER_TO_REPEAT_DURABLY_AVAILABLE_CONTEXT",
    "PRESERVE_NEGATIVE_NULL_AND_UNRESOLVED_RESULTS",
]:
    require(item in deep_receiver, f"deep succession receiver must require {item}")

require(fresh_mode.get("project_manager_handoff_before_first_response") is False,
        "fresh validation must not receive project-manager handoff before first response")
fresh_required = fresh_mode.get("required", [])
require("STRUCTURALLY_ISOLATED_TARGET_AND_TASK" in fresh_required,
        "fresh validation must require structural isolation")
fresh_forbidden = fresh_mode.get("forbidden_before_first_response", [])
for item in [
    "AUTHOR_EXPECTED_VERDICT",
    "OTHER_ARM_RESPONSES",
    "INSTRUCTIONS_TO_IGNORE_SURFACES_THAT_SHOULD_SIMPLY_BE_ABSENT",
]:
    require(item in fresh_forbidden, f"fresh validation must forbid {item}")

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
print("normal_continuation_default=YES")
print("deep_succession_exceptional=YES")
print("fresh_validation_structurally_isolated=YES")
print("record_method_separation=PASS")
