#!/usr/bin/env python3
"""Research validator for ENA Memory Metabolism iteration 0.4.

Checks represented structural consistency only. A PASS does not prove:
- external source authenticity or semantic truth;
- real independence of source roots;
- quality of a compiled heuristic;
- real current authority or declassification basis;
- retrieval completeness, salience, or behavioral improvement.

Status: RESEARCH_PROTOTYPE / NOT_CURRENT_BASELINE / NOT_AUTHORITY
"""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent
SCHEMA_PATH = ROOT / "memory-set.schema.json"
COGNITIVE_DERIVED_LAYERS = {"KNOWLEDGE", "COMPILED", "IDENTITY"}
EVIDENCE_LAYERS = {"EVIDENCE", "ARCHIVE"}
FORBIDDEN_EXECUTABLE_AUTHORITY_FIELDS = {
    "executable_authority",
    "permission_grant",
    "capability_token",
    "current_mandate",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _indexes(doc: dict[str, Any]):
    records: dict[str, dict[str, Any]] = {}
    provenance: dict[str, dict[str, Any]] = {}
    errors: list[str] = []
    for i, record in enumerate(doc.get("records", []) or []):
        rid = record.get("record_id")
        if not rid:
            errors.append(f"record[{i}] missing record_id")
        elif rid in records:
            errors.append(f"duplicate record_id {rid}")
        else:
            records[rid] = record
    for i, item in enumerate(doc.get("provenance_sets", []) or []):
        pid = item.get("provenance_id")
        if not pid:
            errors.append(f"provenance_set[{i}] missing provenance_id")
        elif pid in provenance:
            errors.append(f"duplicate provenance_id {pid}")
        else:
            provenance[pid] = item
    return records, provenance, errors


def _effective_roots(record: dict[str, Any], provenance: dict[str, dict[str, Any]]) -> set[str]:
    roots = set(record.get("source_roots", []) or [])
    pref = record.get("provenance_ref")
    if pref in provenance:
        roots.update(provenance[pref].get("source_roots", []) or [])
    return roots


def _effective_evidence(record: dict[str, Any], provenance: dict[str, dict[str, Any]]) -> set[str]:
    refs = set(record.get("evidence_refs", []) or [])
    pref = record.get("provenance_ref")
    if pref in provenance:
        refs.update(provenance[pref].get("evidence_refs", []) or [])
    return refs


def _direct_lineage(record: dict[str, Any], provenance: dict[str, dict[str, Any]]) -> set[str]:
    return set(record.get("derived_from", []) or []) | _effective_evidence(record, provenance)


def _reachable_evidence(
    record_id: str,
    records: dict[str, dict[str, Any]],
    provenance: dict[str, dict[str, Any]],
) -> set[str]:
    """Return reachable EVIDENCE/ARCHIVE records through finite represented lineage."""
    found: set[str] = set()
    seen: set[str] = set()
    queue = list(_direct_lineage(records.get(record_id, {}), provenance))
    while queue:
        rid = queue.pop()
        if rid in seen:
            continue
        seen.add(rid)
        item = records.get(rid)
        if not item:
            continue
        if item.get("layer") in EVIDENCE_LAYERS:
            found.add(rid)
        queue.extend(_direct_lineage(item, provenance) - seen)
    return found


def _superseded_ids(records: dict[str, dict[str, Any]]) -> set[str]:
    superseded: set[str] = set()
    for record in records.values():
        superseded.update(record.get("supersedes", []) or [])
        for relation in record.get("relations", []) or []:
            if relation.get("type") == "SUPERSEDES" and relation.get("target"):
                superseded.add(relation["target"])
    return superseded


def _explicit_direct_contradiction(record: dict[str, Any], records: dict[str, dict[str, Any]]) -> bool:
    derived = set(record.get("derived_from", []) or [])
    for source_id in derived:
        for relation in records.get(source_id, {}).get("relations", []) or []:
            if relation.get("type") == "CONTRADICTS" and relation.get("target") in derived:
                return True
    return False


def validate_memory_set(doc: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    schema = load_json(SCHEMA_PATH)
    errors.extend(
        f"schema: {e.message}"
        for e in Draft202012Validator(schema).iter_errors(doc)
    )

    records, provenance, index_errors = _indexes(doc)
    errors.extend(index_errors)

    # Reference integrity.
    for pid, item in provenance.items():
        for ref in item.get("evidence_refs", []) or []:
            if ref not in records:
                errors.append(f"{pid}: evidence_refs references missing record {ref}")

    for rid, record in records.items():
        pref = record.get("provenance_ref")
        if pref and pref not in provenance:
            errors.append(f"{rid}: provenance_ref references missing provenance set {pref}")
        for field in ("derived_from", "evidence_refs", "supersedes"):
            for ref in record.get(field, []) or []:
                if ref not in records:
                    errors.append(f"{rid}: {field} references missing record {ref}")

    for rid, record in records.items():
        layer = record.get("layer")
        claim_type = record.get("claim_type")
        roots = _effective_roots(record, provenance)

        for field in FORBIDDEN_EXECUTABLE_AUTHORITY_FIELDS:
            if field in record:
                errors.append(f"{rid}: memory record must not carry executable authority field {field}")

        if layer == "EVIDENCE" and not roots:
            errors.append(f"{rid}: EVIDENCE requires represented source root")

        if layer == "COMPILED":
            if claim_type in {"OCCURRENCE", "TASK_STATE"}:
                errors.append(f"{rid}: COMPILED memory cannot be raw {claim_type}")
            if not _direct_lineage(record, provenance) and not record.get("provenance_ref"):
                errors.append(f"{rid}: COMPILED memory requires derivation/evidence lineage")

            operational_sources = [
                ref for ref in record.get("derived_from", []) or []
                if records.get(ref, {}).get("layer") == "OPERATIONAL"
            ]
            if operational_sources and not _effective_evidence(record, provenance):
                errors.append(f"{rid}: direct OPERATIONAL -> COMPILED requires evidence lineage")

            if record.get("decision_material") is True:
                reachable = _reachable_evidence(rid, records, provenance)
                if not reachable:
                    errors.append(
                        f"{rid}: decision-material COMPILED lineage must transitively reach EVIDENCE/ARCHIVE"
                    )
                challengeability = record.get("challengeability")
                if not challengeability:
                    errors.append(f"{rid}: decision-material COMPILED requires challengeability")
                elif challengeability == "FULL" and reachable:
                    if not any(
                        (records[e].get("evidence_status") or "PRESENT") == "PRESENT"
                        for e in reachable
                    ):
                        errors.append(
                            f"{rid}: FULL challengeability requires at least one reachable PRESENT evidence/archive record"
                        )

            if record.get("support_mode") == "INDEPENDENT_CORROBORATION" and len(roots) < 2:
                errors.append(
                    f"{rid}: independent corroboration requires >=2 distinct represented source roots"
                )

        # MM-P07 widened: explicit contradictions cannot disappear through any
        # derived cognitive representation, not only COMPILED.
        if (
            layer in COGNITIVE_DERIVED_LAYERS
            and record.get("derived_from")
            and _explicit_direct_contradiction(record, records)
            and not str(record.get("conflict_handling", "")).strip()
        ):
            errors.append(f"{rid}: contradictory derivation requires conflict_handling")

        # Identity mutation is not ordinary compaction.
        if (
            layer == "IDENTITY"
            and record.get("mutation") is True
            and not str(record.get("governance_ref", "")).strip()
        ):
            errors.append(f"{rid}: IDENTITY mutation requires governance_ref")

    # Provenance preservation and access-scope derivation.
    for rid, record in records.items():
        derived = record.get("derived_from", []) or []
        if not derived or record.get("layer") not in COGNITIVE_DERIVED_LAYERS:
            continue

        inherited_roots: set[str] = set()
        inherited_scopes: set[str] = set()
        for ref in _direct_lineage(record, provenance):
            source = records.get(ref, {})
            inherited_roots.update(_effective_roots(source, provenance))
            inherited_scopes.update(source.get("access_scope", []) or [])

        own_roots = _effective_roots(record, provenance)
        if inherited_roots and not inherited_roots.issubset(own_roots):
            missing = sorted(inherited_roots - own_roots)
            errors.append(f"{rid}: transformation lost source provenance roots {missing}")

        own_scopes = set(record.get("access_scope", []) or [])
        if inherited_scopes and not inherited_scopes.issubset(own_scopes):
            reconciliation = record.get("access_scope_reconciliation") or {}
            mode = reconciliation.get("mode")
            basis = reconciliation.get("external_basis")
            if mode not in {"EXPLICIT_DECLASSIFICATION", "SANITIZED_DERIVATION"} or not basis:
                missing = sorted(inherited_scopes - own_scopes)
                errors.append(
                    f"{rid}: derivation silently relaxed access scopes {missing}; "
                    "explicit declassification/sanitization reconciliation required"
                )
            elif basis in records:
                errors.append(
                    f"{rid}: access-scope relaxation basis must be external to memory records"
                )

    return errors


def validate_projection(doc: dict[str, Any], projection: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    records = {
        r["record_id"]: r
        for r in doc.get("records", []) or []
        if isinstance(r, dict) and r.get("record_id")
    }
    pid = projection.get("projection_id", "?")
    actor_scopes = set(projection.get("actor_scopes", []) or [])
    retrieved = set(projection.get("retrieved_record_ids", []) or [])
    used = set(projection.get("used_record_ids", []) or [])
    historical = set(projection.get("historical_use_record_ids", []) or [])

    overlap = used & historical
    if overlap:
        errors.append(
            f"projection {pid}: current used and historical-use sets must be disjoint {sorted(overlap)}"
        )

    # Both current and historical context are reads and require retrieval/access.
    for role, ids in (("used", used), ("historical", historical)):
        for rid in ids:
            if rid not in retrieved:
                errors.append(f"projection {pid}: {role} record {rid} was not retrieved")
            record = records.get(rid)
            if not record:
                errors.append(f"projection {pid}: unknown {role} record {rid}")
                continue
            scope = set(record.get("access_scope", []) or [])
            if scope and not scope.issubset(actor_scopes):
                errors.append(f"projection {pid}: actor lacks access scope for {rid}")

    superseded = _superseded_ids(records)
    for rid in used:
        if rid in superseded:
            errors.append(
                f"projection {pid}: superseded record {rid} cannot be used as current state"
            )

    if projection.get("consequence") == "MATERIAL":
        revalidated = set(projection.get("revalidated_record_ids", []) or [])
        for rid in used:
            validity = records.get(rid, {}).get("validity", {}) or {}
            if validity.get("revalidate_before_material_use") is True and rid not in revalidated:
                errors.append(f"projection {pid}: material use of {rid} requires revalidation")

    if projection.get("authority_required") is True:
        basis = projection.get("external_authority_basis")
        if not basis:
            errors.append(f"projection {pid}: authority_required needs external_authority_basis")
        elif basis in records:
            errors.append(f"projection {pid}: memory record cannot serve as executable authority basis")

    return errors


def validate_document(doc: dict[str, Any]) -> list[str]:
    errors = validate_memory_set(doc)
    for projection in doc.get("projections", []) or []:
        errors.extend(validate_projection(doc, projection))
    return errors


def ev(rid="ev-1", root="trace:1", scope=None, status=None):
    r = {
        "record_id": rid,
        "layer": "EVIDENCE",
        "claim_type": "OCCURRENCE",
        "content": "occurrence",
        "source_roots": [root],
        "access_scope": list(scope or ["project:ena"]),
        "validity": {"mode": "IMMUTABLE_OCCURRENCE", "revalidate_before_material_use": False},
    }
    if status:
        r["evidence_status"] = status
    return r


def cm(rid="cm-1", source="ev-1", scope=None):
    return {
        "record_id": rid,
        "layer": "COMPILED",
        "claim_type": "HEURISTIC",
        "content": "heuristic",
        "derived_from": [source],
        "evidence_refs": [source] if source.startswith("ev-") else [],
        "source_roots": ["trace:1"],
        "support_mode": "SINGLE_SOURCE",
        "decision_material": True,
        "challengeability": "FULL",
        "access_scope": list(scope or ["project:ena"]),
        "validity": {"mode": "CONDITIONAL", "revalidate_before_material_use": False},
    }


def doc(records, projections=None):
    return {
        "schema_version": "memory-metabolism-research-0.4",
        "provenance_sets": [],
        "records": records,
        "projections": projections or [],
    }


def expect(name, value, valid):
    errors = validate_document(value)
    assert bool(errors) is (not valid), f"{name}: expected valid={valid}, got {errors}"


def selftest() -> None:
    n = 0

    expect("baseline", doc([ev(), cm()]), True); n += 1

    # Reviewer F1: used ∩ historical cannot bypass supersession.
    old = {
        "record_id": "kb-old", "layer": "KNOWLEDGE", "claim_type": "BELIEF",
        "content": "old", "source_roots": ["inv:t1"], "access_scope": ["project:ena"],
        "validity": {"mode": "CURRENT_STATE", "revalidate_before_material_use": True},
    }
    new = copy.deepcopy(old); new.update({
        "record_id": "kb-new", "content": "new", "source_roots": ["inv:t2"],
        "supersedes": ["kb-old"],
    })
    p = {
        "projection_id": "p", "actor_scopes": ["project:ena"],
        "retrieved_record_ids": ["kb-old"], "used_record_ids": ["kb-old"],
        "revalidated_record_ids": ["kb-old"], "historical_use_record_ids": ["kb-old"],
        "consequence": "MATERIAL", "authority_required": False,
    }
    expect("f1_overlap_bypass_blocked", doc([old, new], [p]), False); n += 1

    # Legitimate historical use stays available.
    p2 = copy.deepcopy(p); p2["used_record_ids"] = []; p2["revalidated_record_ids"] = []
    expect("historical_superseded_allowed", doc([old, new], [p2]), True); n += 1

    # Reviewer F3: historical read still requires access.
    secret_old = copy.deepcopy(old); secret_old["access_scope"] = ["secret:board"]
    expect("historical_access_checked", doc([secret_old, new], [p2]), False); n += 1

    # Reviewer F2: derived record cannot silently relax source access scope.
    secret = ev("ev-secret", scope=["secret:board"])
    public_cm = cm("cm-public", "ev-secret", scope=["public"])
    public_cm["source_roots"] = ["trace:1"]
    expect("silent_scope_relaxation_blocked", doc([secret, public_cm]), False); n += 1

    # Explicit sanitization/declassification keeps legitimate publication representable.
    sanitized = copy.deepcopy(public_cm)
    sanitized["access_scope_reconciliation"] = {
        "mode": "SANITIZED_DERIVATION",
        "external_basis": "declassification:review-1",
    }
    expect("explicit_sanitization_allowed", doc([secret, sanitized]), True); n += 1

    bad_sanitized = copy.deepcopy(sanitized)
    bad_sanitized["access_scope_reconciliation"]["external_basis"] = "ev-secret"
    expect("memory_cannot_self_authorize_declassification", doc([secret, bad_sanitized]), False); n += 1

    # Reviewer F5: KNOWLEDGE cannot bypass explicit contradiction handling.
    a, b = ev("ev-a", "trace:a"), ev("ev-b", "trace:b")
    a["relations"] = [{"type": "CONTRADICTS", "target": "ev-b"}]
    kb = {
        "record_id": "kb", "layer": "KNOWLEDGE", "claim_type": "BELIEF",
        "content": "merged", "derived_from": ["ev-a", "ev-b"],
        "source_roots": ["trace:a", "trace:b"], "access_scope": ["project:ena"],
        "validity": {"mode": "CONDITIONAL", "revalidate_before_material_use": False},
    }
    expect("knowledge_contradiction_visible", doc([a, b, kb]), False); n += 1
    kb2 = copy.deepcopy(kb); kb2["conflict_handling"] = "condition on environment"
    expect("knowledge_contradiction_handled", doc([a, b, kb2]), True); n += 1

    # Reviewer FB-1: transitive evidence supports higher-order compilation.
    e = ev()
    c1 = cm()
    c2 = cm("cm-2", "cm-1")
    c2["source_roots"] = ["trace:1"]
    expect("second_order_compilation_allowed", doc([e, c1, c2]), True); n += 1

    # Known F6: full challengeability cannot survive only tombstoned/redacted evidence.
    red = ev(status="LAWFULLY_REDACTED")
    c = cm()
    expect("redacted_full_challengeability_blocked", doc([red, c]), False); n += 1
    cdeg = copy.deepcopy(c); cdeg["challengeability"] = "DEGRADED"
    expect("redacted_degraded_challengeability_allowed", doc([red, cdeg]), True); n += 1

    # Authority remains external.
    p3 = {
        "projection_id": "p3", "actor_scopes": ["project:ena"],
        "retrieved_record_ids": ["cm-1"], "used_record_ids": ["cm-1"],
        "revalidated_record_ids": [], "historical_use_record_ids": [],
        "consequence": "MATERIAL", "authority_required": True,
        "external_authority_basis": "cm-1",
    }
    expect("memory_not_authority", doc([ev(), cm()], [p3]), False); n += 1
    p3["external_authority_basis"] = "mandate:external-1"
    expect("external_authority_representable", doc([ev(), cm()], [p3]), True); n += 1

    # Root preservation through second-order compilation remains enforced.
    c2bad = copy.deepcopy(c2); c2bad["source_roots"] = []
    expect("second_order_root_loss_blocked", doc([e, c1, c2bad]), False); n += 1

    # Independent corroboration remains represented-root only, not external proof.
    ci = cm()
    ci["support_mode"] = "INDEPENDENT_CORROBORATION"
    expect("single_root_not_independent", doc([ev(), ci]), False); n += 1

    print(f"MEMORY_METABOLISM_ITERATION_04_SELFTEST_PASS {n}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    if args.selftest:
        selftest()
        return
    if not args.path:
        parser.error("path required unless --selftest is used")
    value = load_json(Path(args.path))
    errors = validate_document(value)
    print(json.dumps({
        "valid": not errors,
        "scope": "represented Memory Metabolism iteration-0.4 structural consistency only",
        "errors": errors,
    }, indent=2))
    raise SystemExit(0 if not errors else 1)


if __name__ == "__main__":
    main()
