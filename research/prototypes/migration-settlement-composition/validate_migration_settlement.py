#!/usr/bin/env python3
"""Research-only source-aware migration × commitment/settlement composition harness.

The point of this harness is not to define a new packet schema. It tests whether
decision-material obligation lineage survives projection/export honestly.

Verification boundary:
- source record and carrier inputs are represented data, not authenticated truth;
- packet/capsule digests are not external authenticity;
- transferability and authority remain Host/counterparty questions;
- import-only validation cannot discover omitted lineage that source projection
  never declared.
"""
from __future__ import annotations

import hashlib
import json
from typing import Any


def digest(value: Any) -> str:
    return hashlib.sha256(json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")).hexdigest()


def source_obligation_refs(source_record: dict[str, Any]) -> list[str]:
    refs = source_record.get("triggered_obligation_refs") or []
    return [r for r in refs if isinstance(r, str) and r]


def validate_package(
    source_record: dict[str, Any],
    package: dict[str, Any],
    commitment_by_id: dict[str, dict[str, Any]] | None = None,
) -> tuple[list[str], str]:
    """Validate lineage survival with access to the source record."""
    errors: list[str] = []
    commitment_by_id = commitment_by_id or {}

    source_id = source_record.get("candidate_id")
    packet = package.get("adaptation_packet")
    manifest = package.get("projection_manifest")
    if not isinstance(packet, dict):
        return ["adaptation_packet required"], "REJECT_PACKAGE"
    if not isinstance(manifest, dict):
        return ["projection_manifest required"], "REJECT_PACKAGE"

    if packet.get("source_candidate_id") != source_id:
        errors.append("packet source_candidate_id differs from source record")
    if manifest.get("source_candidate_id") != source_id:
        errors.append("manifest source_candidate_id differs from source record")

    if manifest.get("source_record_digest") != digest(source_record):
        errors.append("source_record_digest mismatch")
    if manifest.get("portable_packet_digest") != digest(packet):
        errors.append("portable_packet_digest mismatch")

    refs = source_obligation_refs(source_record)
    declared_classes = set(manifest.get("decision_material_lineage_classes") or [])
    carriers = manifest.get("lineage_carriers") or []
    if not isinstance(carriers, list):
        errors.append("lineage_carriers must be array")
        carriers = []

    obligation_carriers = [
        c for c in carriers
        if isinstance(c, dict) and c.get("lineage_class") == "UNRESOLVED_OBLIGATION"
    ]

    if refs:
        if "UNRESOLVED_OBLIGATION" not in declared_classes:
            errors.append("source has obligation refs but manifest omits UNRESOLVED_OBLIGATION class")
        carrier_refs = {c.get("source_ref") for c in obligation_carriers}
        missing = sorted(set(refs) - carrier_refs)
        if missing:
            errors.append(f"obligation refs omitted from lineage carriers: {missing}")

    local_ready = True
    unresolved = False
    for c in obligation_carriers:
        mode = c.get("mode")
        source_ref = c.get("source_ref")
        if mode == "RAW_SOURCE_REF":
            unresolved = True
            local_ready = False
            if c.get("receiver_resolution") == "RESOLVED":
                errors.append("RAW_SOURCE_REF cannot self-assert receiver resolution")
        elif mode == "SOURCE_SHADOW":
            unresolved = True
            local_ready = False
            if c.get("local_authority_granted") is True:
                errors.append("SOURCE_SHADOW cannot mint local authority")
            if c.get("local_executor_assigned") is True:
                errors.append("SOURCE_SHADOW cannot mint local executor ownership")
        elif mode == "TYPED_COMMITMENT_CARRIER":
            cid = c.get("commitment_id")
            if not isinstance(cid, str) or cid not in commitment_by_id:
                errors.append(f"typed commitment carrier unresolved: {cid!r}")
                local_ready = False
                unresolved = True
                continue
            commitment = commitment_by_id[cid]
            expected = c.get("expected_commitment_ref") or source_ref
            if expected != f"commitment:{cid}" and source_ref != f"commitment:{cid}":
                errors.append(f"typed commitment carrier/source ref mismatch for {cid}")
            status = commitment.get("status")
            if status in {"SETTLED", "CANCELLED"}:
                pass
            elif status == "TRANSFERRED":
                unresolved = True
                local_ready = False
            else:
                unresolved = True
                local_ready = False
        else:
            errors.append(f"unknown obligation carrier mode: {mode!r}")
            local_ready = False
            unresolved = True

    if errors:
        return errors, "REJECT_PACKAGE"
    if refs and unresolved:
        return [], "WAIT_NARROW_OR_LOCAL_REBIND"
    if refs and not local_ready:
        return [], "WAIT_NARROW_OR_LOCAL_REBIND"
    return [], "IMPORT_WITHOUT_OBLIGATION_BLOCKER"


def packet_only_false_ok(package: dict[str, Any]) -> bool:
    """Demonstrate the receiver epistemic limit.

    This intentionally checks only the portable packet structure, not the source
    record. If obligation lineage was silently omitted, this function can return
    True. That false-OK is the property under test.
    """
    packet = package.get("adaptation_packet")
    return isinstance(packet, dict) and bool(packet.get("source_candidate_id"))


def build_manifest(source_record: dict[str, Any], packet: dict[str, Any], carriers: list[dict]) -> dict:
    classes: list[str] = []
    if source_obligation_refs(source_record):
        classes.append("UNRESOLVED_OBLIGATION")
    return {
        "source_candidate_id": source_record.get("candidate_id"),
        "source_record_digest": digest(source_record),
        "portable_packet_digest": digest(packet),
        "decision_material_lineage_classes": classes,
        "lineage_carriers": carriers,
    }
