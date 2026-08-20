#!/usr/bin/env python3
"""ENA v0.3.2 V2 Machine-Contract Hardening Experiment — research prototype.

NOT part of releases/current/. Research/prototype surface only.
Implements minimal candidate machine-contract changes for six falsified
false-claim vectors, with adversarial fixtures, legitimate positive controls,
and second-order bypass attempts.

Success metric: cheapest machine contract that refuses to endorse a material
false claim while preserving viable agency. Not "more validation rules".
"""

from __future__ import annotations
import json, sys, os
from pathlib import Path

CURRENT = Path(r"C:\Users\PC\Documents\Deepseek Harness\_tmp_v2\repo\releases\current")
sys.path.insert(0, str(CURRENT / "tools"))
from validate_contracts import validate_support, validate_obligation, validate_recovery, _scope_mismatches

# ---------------------------------------------------------------------------
# Candidate machine-contract rules (research only). Each is keyed to one vector.
# Design principle per rule: block the material false claim with the smallest
# structural/semantic addition; do not reject legitimate cases.
# ---------------------------------------------------------------------------

def candidate_claim_supported_requires_refs(claim: dict) -> dict:
    """ATT-1 fix: status=SUPPORTED requires non-empty support_relation_refs.
    Minimal: SUPPORTED is a positive claim; zero support refs is self-assertion.
    Legitimate SUPPORTED claims always name their support. ASSERTED/UNKNOWN/REVOKED untouched."""
    if claim.get("status") == "SUPPORTED":
        refs = claim.get("support_relation_refs") or []
        if not refs:
            return {"ok": False, "code": "CLAIM_SUPPORTED_WITHOUT_SUPPORT_REFS"}
    return {"ok": True, "code": "OK"}


def candidate_binding_authority_requires_mandate(binding: dict) -> dict:
    """ATT-3 fix: non-empty authority_envelope requires mandate_source + horizon.
    Minimal: authority is not self-declared; a credential/restore fact does not
    create authority. mandate_source must be present and not just 'restore'."""
    env = binding.get("authority_envelope") or []
    if env:
        mandate = binding.get("mandate") or {}
        src = mandate.get("source")
        if not src:
            return {"ok": False, "code": "AUTHORITY_WITHOUT_MANDATE_SOURCE"}
        if src in ("RESTORE", "RESTORED_STATE", "CLONE", "CREDENTIAL_VALID"):
            return {"ok": False, "code": "AUTHORITY_MANDATE_SOURCE_NOT_AUTHORIZING",
                    "details": {"source": src}}
        horizon = mandate.get("expires_at")
        if not horizon:
            return {"ok": False, "code": "AUTHORITY_WITHOUT_MANDATE_HORIZON"}
    return {"ok": True, "code": "OK"}


def candidate_obligation_claim_link(claim: dict, obligations: list[dict]) -> dict:
    """ATT-4 fix: WORKFLOW_COMPLETION claim must enumerate required obligations
    and each must not be PENDING/FAILED/UNKNOWN when material+observed.
    Minimal: claim side must carry required_obligation_refs; validator resolves."""
    if claim.get("claim_type") in ("WORKFLOW_COMPLETION", "TASK_COMPLETION"):
        refs = claim.get("required_obligation_refs") or []
        if not refs:
            return {"ok": False, "code": "COMPLETION_CLAIM_WITHOUT_OBLIGATION_REFS"}
        for ob in obligations:
            if ob.get("obligation_id") in refs:
                mat = ob.get("materiality")
                trig = (ob.get("trigger") or {}).get("observed")
                st = ob.get("status")
                if mat == "MATERIAL" and trig and st in ("PENDING", "FAILED", "UNKNOWN"):
                    return {"ok": False, "code": "COMPLETION_WITH_OPEN_MATERIAL_OBLIGATION",
                            "details": {"obligation_id": ob.get("obligation_id"), "status": st}}
                if st == "SATISFIED" and not (ob.get("closure_evidence_refs") or []):
                    return {"ok": False, "code": "OBLIGATION_SATISFIED_WITHOUT_CLOSURE_EVIDENCE"}
                if st in ("NOT_REQUIRED", "DEFERRED_AUTHORIZED") and not ob.get("resolution_reason"):
                    return {"ok": False, "code": "OBLIGATION_CLOSURE_STATUS_REQUIRES_REASON"}
    return {"ok": True, "code": "OK"}


def candidate_recovery_history_requires_evidence(transition: dict) -> dict:
    """ATT-5 fix: STATE_AND_HISTORY recovery claim requires preservation evidence,
    not just the PRESERVED status word. Minimal: evidence_refs non-empty AND
    post_checkpoint_occurrence_delta_captured == true AND evidence is not the
    same artifact as the state-restore evidence (history proof != state proof)."""
    claim_scope = (transition.get("recovery_claim") or {}).get("scope")
    if claim_scope == "STATE_AND_HISTORY":
        hist = transition.get("history_continuity") or {}
        if hist.get("status") != "PRESERVED":
            return {"ok": False, "code": "FULL_RECOVERY_REQUIRES_PRESERVED_HISTORY"}
        refs = hist.get("evidence_refs") or []
        delta = hist.get("post_checkpoint_occurrence_delta_captured")
        if not refs:
            return {"ok": False, "code": "HISTORY_PRESERVED_WITHOUT_EVIDENCE"}
        if delta is not True:
            return {"ok": False, "code": "HISTORY_PRESERVED_WITHOUT_DELTA_CAPTURE"}
        state_refs = (transition.get("state_restore") or {}).get("evidence_refs") or []
        overlap = set(refs) & set(state_refs)
        if overlap:
            return {"ok": False, "code": "HISTORY_EVIDENCE_SAME_AS_STATE_EVIDENCE",
                    "details": {"shared_refs": sorted(overlap)}}
    return {"ok": True, "code": "OK"}


def candidate_independence_requires_root(support: dict) -> dict:
    """ATT-6 fix: independence counting is based on root provenance, not distinct
    label strings. Minimal: if claimed_independent_count is set, require
    root_provenance list and count distinct roots, not source_origins labels."""
    ind = support.get("independence_basis") or {}
    claimed = ind.get("claimed_independent_count")
    if claimed is None:
        return {"ok": True, "code": "OK"}
    roots = ind.get("root_provenance") or []
    if not roots:
        return {"ok": False, "code": "INDEPENDENCE_WITHOUT_ROOT_PROVENANCE"}
    unique_roots = {str(x) for x in roots if x not in (None, "", "UNKNOWN")}
    if claimed > len(unique_roots):
        return {"ok": False, "code": "INDEPENDENCE_OVERCLAIMED",
                "details": {"claimed": claimed, "unique_roots": sorted(unique_roots)}}
    return {"ok": True, "code": "OK"}


def candidate_verification_requires_grade(binding: dict) -> dict:
    """ATT-2 fix: capability claims marked verified require evidence with a grade
    above static-structure. Minimal: add optional evidence_grade on evidence refs
    entries; VERIFIED_AVAILABLE cannot rest solely on E0/E1-static refs."""
    for cap in (binding.get("capabilities") or []):
        if cap.get("status") in ("VERIFIED_AVAILABLE", "VERIFIED_RESTRICTED"):
            refs = cap.get("evidence_refs") or []
            grades = [r.get("grade") for r in refs if isinstance(r, dict)]
            if not grades:
                return {"ok": False, "code": "VERIFIED_WITHOUT_EVIDENCE_GRADE"}
            if all(g in ("E0", "E1") for g in grades):
                return {"ok": False, "code": "VERIFIED_ONLY_STATIC_STRUCTURE_EVIDENCE",
                        "details": {"grades": grades}}
    return {"ok": True, "code": "OK"}


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

def run_candidates(claim=None, support=None, binding=None, obligations=None, transition=None):
    results = []
    if claim is not None:
        results.append(("CLAIM_SUPPORTED_REQUIRES_REFS", candidate_claim_supported_requires_refs(claim)))
    if binding is not None:
        results.append(("AUTHORITY_REQUIRES_MANDATE", candidate_binding_authority_requires_mandate(binding)))
        results.append(("VERIFIED_REQUIRES_GRADE", candidate_verification_requires_grade(binding)))
    if claim is not None and obligations is not None:
        results.append(("OBLIGATION_CLAIM_LINK", candidate_obligation_claim_link(claim, obligations)))
    if transition is not None:
        results.append(("RECOVERY_HISTORY_EVIDENCE", candidate_recovery_history_requires_evidence(transition)))
    if support is not None:
        results.append(("INDEPENDENCE_ROOT", candidate_independence_requires_root(support)))
    return results


if __name__ == "__main__":
    print("candidate rule module loaded (research prototype)")
