#!/usr/bin/env python3
"""Reference behavior for HOW-E native Host organ rebind.

This module intentionally models only the decision boundary for mapping ENA
properties onto existing Host organs. It does not define a universal Host
schema and does not claim that a written mapping proves behavioral adoption.
"""

from __future__ import annotations

from dataclasses import dataclass


NATIVE_REALIZATION = "NATIVE_REALIZATION"
PARTIAL_NATIVE_REALIZATION = "PARTIAL_NATIVE_REALIZATION"
GAP = "GAP"
DORMANT_NOT_DECISION_CHANGING = "DORMANT_NOT_DECISION_CHANGING"

ALLOWED_STATUSES = {
    NATIVE_REALIZATION,
    PARTIAL_NATIVE_REALIZATION,
    GAP,
    DORMANT_NOT_DECISION_CHANGING,
}


@dataclass(frozen=True)
class NativeBinding:
    property_id: str
    status: str
    native_organ: str | None = None
    behavior_ref: str | None = None
    material: bool = True
    duplicate_ena_organ: bool = False


def binding_posture(binding: NativeBinding) -> str:
    if binding.status not in ALLOWED_STATUSES:
        return "INVALID_STATUS"

    if binding.status in {NATIVE_REALIZATION, PARTIAL_NATIVE_REALIZATION}:
        if not binding.native_organ:
            return "INVALID_NATIVE_CLAIM_NO_ORGAN"
        if not binding.behavior_ref:
            return "NATIVE_CLAIM_NEEDS_BEHAVIOR_EVIDENCE"
        if binding.duplicate_ena_organ and binding.status == NATIVE_REALIZATION:
            return "REJECT_REDUNDANT_MIGRATION_UNLESS_NEW_DECISION_VALUE"
        if binding.status == PARTIAL_NATIVE_REALIZATION:
            return "USE_NATIVE_ORGAN_PLUS_MINIMAL_GAP_ADAPTER"
        return "USE_NATIVE_ORGAN"

    if binding.status == GAP:
        if binding.material:
            return "MATERIAL_GAP_REQUIRES_ORGAN_OR_ADAPTER"
        return "NONMATERIAL_GAP_MAY_REMAIN_OPEN"

    return "DORMANT_WITHOUT_COMPLIANCE_PENALTY"


def mapping_posture(
    declared_current_tree: str,
    runtime_current_tree: str,
    bindings: list[NativeBinding],
) -> str:
    if declared_current_tree != runtime_current_tree:
        return "STALE_REBIND_REQUIRED"

    if not bindings:
        return "NO_BINDINGS_NO_ADOPTION_CLAIM"

    postures = [binding_posture(binding) for binding in bindings]

    if any(posture.startswith("INVALID_") for posture in postures):
        return "INVALID_MAPPING"
    if "NATIVE_CLAIM_NEEDS_BEHAVIOR_EVIDENCE" in postures:
        return "MAPPING_EVIDENCE_INSUFFICIENT"
    if "REJECT_REDUNDANT_MIGRATION_UNLESS_NEW_DECISION_VALUE" in postures:
        return "REDUNDANT_MIGRATION_REVIEW"
    if "MATERIAL_GAP_REQUIRES_ORGAN_OR_ADAPTER" in postures:
        return "MATERIAL_GAP_REQUIRES_ORGAN_OR_ADAPTER"

    return "NATIVE_REBIND_ACCEPTABLE"
