#!/usr/bin/env python3
"""Research validator for ENA Memory Metabolism prototype.

Checks represented structural properties only. A PASS does not prove:
- external source authenticity;
- semantic truth of content;
- actual independence of source roots;
- quality of a compiled heuristic;
- real current authority;
- retrieval quality in a live Agent;
- behavioral improvement.

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

FORBIDDEN_EXECUTABLE_AUTHORITY_FIELDS = {
    "executable_authority",
    "permission_grant",
    "capability_token",
    "current_mandate",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_memory_set(doc: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    schema = load_json(SCHEMA_PATH)
    errors.extend(
        f"schema: {e.message}"
        for e in Draft202012Validator(schema).iter_errors(doc)
    )

    records: dict[str, dict[str, Any]] = {}
    for index, record in enumerate(doc.get("records", [])):
        record_id = record.get("record_id")
        if not record_id:
            errors.append(f"record[{index}] missing record_id")
            continue
        if record_id in records:
            errors.append(f"duplicate record_id {record_id}")
        records[record_id] = record

    # Cross-record reference integrity.
    for record_id, record in records.items():
        for field in ("derived_from", "evidence_refs", "supersedes"):
            for ref in record.get(field, []) or []:
                if ref not in records:
                    errors.append(
                        f"{record_id}: {field} references missing record {ref}"
                    )

    for record_id, record in records.items():
        # MM-P03: memory may reference authority but must not carry executable authority.
        for field in FORBIDDEN_EXECUTABLE_AUTHORITY_FIELDS:
            if field in record:
                errors.append(
                    f"{record_id}: memory record must not carry executable authority field {field}"
                )

        layer = record.get("layer")
        claim_type = record.get("claim_type")

        if layer == "COMPILED":
            # MM-P01: raw occurrence/task state is not compiled behavioral learning.
            if claim_type in {"OCCURRENCE", "TASK_STATE"}:
                errors.append(
                    f"{record_id}: COMPILED memory cannot be raw {claim_type}"
                )

            # MM-P02: durable compilation retains derivation/evidence lineage.
            if not (record.get("evidence_refs") or record.get("derived_from")):
                errors.append(
                    f"{record_id}: COMPILED memory requires derivation/evidence lineage"
                )

            # MM-P04: transient operational state cannot compile itself.
            operational_sources = [
                ref
                for ref in record.get("derived_from", []) or []
                if records.get(ref, {}).get("layer") == "OPERATIONAL"
            ]
            if operational_sources and not record.get("evidence_refs"):
                errors.append(
                    f"{record_id}: direct OPERATIONAL -> COMPILED requires evidence_refs"
                )

            # Decision-material compiled memory keeps a challenge path.
            if record.get("decision_material") is True:
                evidence_refs = record.get("evidence_refs", []) or []
                if not evidence_refs:
                    errors.append(
                        f"{record_id}: decision-material COMPILED memory requires evidence_refs"
                    )
                elif not any(
                    records.get(ref, {}).get("layer") in {"EVIDENCE", "ARCHIVE"}
                    for ref in evidence_refs
                ):
                    errors.append(
                        f"{record_id}: decision-material COMPILED memory evidence_refs must reach EVIDENCE/ARCHIVE"
                    )

            # MM-P06: represented independent corroboration needs distinct roots.
            if record.get("support_mode") == "INDEPENDENT_CORROBORATION":
                roots = {
                    root
                    for root in (record.get("source_roots") or [])
                    if isinstance(root, str) and root.strip()
                }
                if len(roots) < 2:
                    errors.append(
                        f"{record_id}: independent corroboration requires >=2 distinct source_roots"
                    )

            # MM-P07: explicit contradiction may not silently disappear.
            derived = set(record.get("derived_from", []) or [])
            contradiction_present = False
            for source_id in derived:
                for relation in records.get(source_id, {}).get("relations", []) or []:
                    if (
                        relation.get("type") == "CONTRADICTS"
                        and relation.get("target") in derived
                    ):
                        contradiction_present = True
            if contradiction_present and not str(
                record.get("conflict_handling", "")
            ).strip():
                errors.append(
                    f"{record_id}: contradictory derivation requires conflict_handling"
                )

        # MM-P11: identity mutation is not ordinary compaction.
        if (
            layer == "IDENTITY"
            and record.get("mutation") is True
            and not str(record.get("governance_ref", "")).strip()
        ):
            errors.append(
                f"{record_id}: IDENTITY mutation requires governance_ref"
            )

    # MM-P05: transformation may compress representation but not silently lose roots.
    for record_id, record in records.items():
        derived = record.get("derived_from", []) or []
        if derived and record.get("layer") in {"KNOWLEDGE", "COMPILED", "IDENTITY"}:
            inherited_roots: set[str] = set()
            for ref in derived:
                inherited_roots.update(records.get(ref, {}).get("source_roots", []) or [])
            own_roots = set(record.get("source_roots", []) or [])
            if inherited_roots and not inherited_roots.issubset(own_roots):
                missing = sorted(inherited_roots - own_roots)
                errors.append(
                    f"{record_id}: transformation lost source_roots {missing}"
                )

    return errors


def validate_projection(
    doc: dict[str, Any], projection: dict[str, Any]
) -> list[str]:
    errors: list[str] = []
    records = {
        r["record_id"]: r
        for r in doc.get("records", [])
        if isinstance(r, dict) and r.get("record_id")
    }

    projection_id = projection.get("projection_id", "?")
    actor_scopes = set(projection.get("actor_scopes", []) or [])
    retrieved = set(projection.get("retrieved_record_ids", []) or [])
    used = projection.get("used_record_ids", []) or []

    for record_id in used:
        if record_id not in retrieved:
            errors.append(
                f"projection {projection_id}: used record {record_id} was not retrieved"
            )
        record = records.get(record_id)
        if not record:
            errors.append(
                f"projection {projection_id}: unknown used record {record_id}"
            )
            continue

        # MM-P09: relevance never bypasses access scope.
        access_scope = set(record.get("access_scope", []) or [])
        if access_scope and not access_scope.issubset(actor_scopes):
            errors.append(
                f"projection {projection_id}: actor lacks access scope for {record_id}"
            )

    # MM-P08: mutable state must be revalidated when a material decision says so.
    if projection.get("consequence") == "MATERIAL":
        revalidated = set(projection.get("revalidated_record_ids", []) or [])
        for record_id in used:
            validity = records.get(record_id, {}).get("validity", {}) or {}
            if (
                validity.get("revalidate_before_material_use") is True
                and record_id not in revalidated
            ):
                errors.append(
                    f"projection {projection_id}: material use of {record_id} requires revalidation"
                )

    # MM-P10: when authority is required, memory itself is not the authority object.
    if projection.get("authority_required") is True:
        authority_basis = projection.get("external_authority_basis")
        if not authority_basis:
            errors.append(
                f"projection {projection_id}: authority_required needs external_authority_basis"
            )
        elif authority_basis in records:
            errors.append(
                f"projection {projection_id}: memory record cannot serve as executable authority basis"
            )

    return errors


def validate_document(doc: dict[str, Any]) -> list[str]:
    errors = validate_memory_set(doc)
    for projection in doc.get("projections", []) or []:
        errors.extend(validate_projection(doc, projection))
    return errors


def base_document() -> dict[str, Any]:
    return {
        "schema_version": "memory-metabolism-research-0.1",
        "records": [
            {
                "record_id": "ev-1",
                "layer": "EVIDENCE",
                "claim_type": "OCCURRENCE",
                "content": "Deployment failed after stale endpoint reuse.",
                "source_roots": ["trace:run-1"],
                "access_scope": ["project:ena"],
                "validity": {
                    "mode": "IMMUTABLE_OCCURRENCE",
                    "revalidate_before_material_use": False,
                },
            },
            {
                "record_id": "cm-1",
                "layer": "COMPILED",
                "claim_type": "HEURISTIC",
                "content": "Revalidate mutable endpoint state before consequential reuse.",
                "derived_from": ["ev-1"],
                "evidence_refs": ["ev-1"],
                "source_roots": ["trace:run-1"],
                "support_mode": "SINGLE_SOURCE",
                "decision_material": True,
                "access_scope": ["project:ena"],
                "validity": {
                    "mode": "CONDITIONAL",
                    "revalidate_before_material_use": False,
                },
            },
        ],
        "projections": [],
    }


def expect_valid(name: str, doc: dict[str, Any]) -> None:
    errors = validate_document(doc)
    assert not errors, f"{name} unexpectedly failed: {errors}"


def expect_invalid(name: str, doc: dict[str, Any]) -> None:
    errors = validate_document(doc)
    assert errors, f"{name} unexpectedly passed"


def selftest() -> None:
    count = 0

    # 1: normal evidence -> compiled heuristic lineage is structurally valid.
    expect_valid("good_compiled_lineage", base_document())
    count += 1

    # 2: raw occurrence mislabeled as compiled memory must fail.
    bad = base_document()
    bad["records"][1]["claim_type"] = "OCCURRENCE"
    expect_invalid("raw_occurrence_in_compiled", bad)
    count += 1

    # 3: compiled memory without derivation/evidence lineage must fail.
    bad = base_document()
    bad["records"][1]["derived_from"] = []
    bad["records"][1]["evidence_refs"] = []
    bad["records"][1]["source_roots"] = []
    bad["records"][1]["decision_material"] = False
    expect_invalid("compiled_without_lineage", bad)
    count += 1

    # 4: executable authority fields must not enter the memory contract.
    bad = base_document()
    bad["records"][1]["capability_token"] = "secret-token"
    expect_invalid("memory_cannot_carry_executable_authority", bad)
    count += 1

    # 5: transient operational state cannot directly become compiled learning.
    bad = {
        "schema_version": "memory-metabolism-research-0.1",
        "records": [
            {
                "record_id": "op-1",
                "layer": "OPERATIONAL",
                "claim_type": "TASK_STATE",
                "content": "retry_count = 3",
                "source_roots": ["runtime:session-1"],
                "access_scope": [],
                "validity": {
                    "mode": "CURRENT_STATE",
                    "revalidate_before_material_use": True,
                },
            },
            {
                "record_id": "cm-op",
                "layer": "COMPILED",
                "claim_type": "HEURISTIC",
                "content": "Retry three times by default.",
                "derived_from": ["op-1"],
                "evidence_refs": [],
                "source_roots": ["runtime:session-1"],
                "support_mode": "SINGLE_SOURCE",
                "decision_material": False,
                "access_scope": [],
                "validity": {
                    "mode": "CONDITIONAL",
                    "revalidate_before_material_use": False,
                },
            },
        ],
        "projections": [],
    }
    expect_invalid("operational_direct_compile", bad)
    count += 1

    # 6: repeated derivations from one root are not independent corroboration.
    bad = base_document()
    bad["records"][1]["support_mode"] = "INDEPENDENT_CORROBORATION"
    expect_invalid("duplicate_root_not_independent", bad)
    count += 1

    # 7: two represented distinct roots satisfy the structural independence check.
    good = base_document()
    good["records"].insert(
        1,
        {
            "record_id": "ev-2",
            "layer": "EVIDENCE",
            "claim_type": "OCCURRENCE",
            "content": "The same failure was independently observed in another run.",
            "source_roots": ["trace:run-2"],
            "access_scope": ["project:ena"],
            "validity": {
                "mode": "IMMUTABLE_OCCURRENCE",
                "revalidate_before_material_use": False,
            },
        },
    )
    compiled = good["records"][2]
    compiled["derived_from"] = ["ev-1", "ev-2"]
    compiled["evidence_refs"] = ["ev-1", "ev-2"]
    compiled["source_roots"] = ["trace:run-1", "trace:run-2"]
    compiled["support_mode"] = "INDEPENDENT_CORROBORATION"
    expect_valid("two_roots_independent_structurally", good)
    count += 1

    # 8: explicit contradiction cannot vanish during consolidation.
    bad = copy.deepcopy(good)
    bad["records"][0]["relations"] = [
        {"type": "CONTRADICTS", "target": "ev-2"}
    ]
    expect_invalid("contradiction_requires_handling", bad)
    count += 1

    # 9: the contract permits explicit/inspectable conflict handling.
    good_conflict = copy.deepcopy(bad)
    good_conflict["records"][2]["conflict_handling"] = (
        "Keep the heuristic conditional on the environment difference."
    )
    expect_valid("contradiction_with_handling", good_conflict)
    count += 1

    # 10: a transformation may not silently lose known source roots.
    bad = base_document()
    bad["records"][1]["source_roots"] = []
    expect_invalid("source_root_loss", bad)
    count += 1

    # 11: consequential use of mutable current state requires revalidation.
    bad = base_document()
    bad["records"].append(
        {
            "record_id": "kb-current",
            "layer": "KNOWLEDGE",
            "claim_type": "BELIEF",
            "content": "Current deployment endpoint is 10.0.0.5.",
            "source_roots": ["inventory:snapshot-old"],
            "access_scope": ["project:ena"],
            "validity": {
                "mode": "CURRENT_STATE",
                "revalidate_before_material_use": True,
            },
        }
    )
    bad["projections"] = [
        {
            "projection_id": "p-1",
            "actor_scopes": ["project:ena"],
            "retrieved_record_ids": ["kb-current"],
            "used_record_ids": ["kb-current"],
            "revalidated_record_ids": [],
            "consequence": "MATERIAL",
            "authority_required": True,
            "external_authority_basis": "mandate:deploy-7",
        }
    ]
    expect_invalid("material_current_state_requires_revalidation", bad)
    count += 1

    # 12: after represented revalidation, the same projection is structurally valid.
    good_projection = copy.deepcopy(bad)
    good_projection["projections"][0]["revalidated_record_ids"] = ["kb-current"]
    expect_valid("revalidated_current_state", good_projection)
    count += 1

    # 13: remembered text cannot become executable authority merely by being retrieved.
    bad_authority = copy.deepcopy(good_projection)
    bad_authority["projections"][0]["external_authority_basis"] = "cm-1"
    expect_invalid("memory_not_authority_basis", bad_authority)
    count += 1

    # 14: relevance does not bypass access scope.
    bad = base_document()
    bad["projections"] = [
        {
            "projection_id": "p-2",
            "actor_scopes": ["project:other"],
            "retrieved_record_ids": ["cm-1"],
            "used_record_ids": ["cm-1"],
            "revalidated_record_ids": [],
            "consequence": "NON_MATERIAL",
            "authority_required": False,
        }
    ]
    expect_invalid("access_scope_enforced", bad)
    count += 1

    # 15: durable identity mutation cannot be an ordinary compaction side effect.
    bad = base_document()
    bad["records"].append(
        {
            "record_id": "id-1",
            "layer": "IDENTITY",
            "claim_type": "PREFERENCE",
            "content": "A new durable purpose/orientation.",
            "derived_from": ["ev-1"],
            "evidence_refs": ["ev-1"],
            "source_roots": ["trace:run-1"],
            "access_scope": ["project:ena"],
            "validity": {
                "mode": "CONDITIONAL",
                "revalidate_before_material_use": False,
            },
            "mutation": True,
        }
    )
    expect_invalid("identity_mutation_needs_governance", bad)
    count += 1

    # 16: explicit governance/change provenance makes the mutation representable.
    good_identity = copy.deepcopy(bad)
    good_identity["records"][-1]["governance_ref"] = "change:approved-1"
    expect_valid("identity_mutation_with_governance", good_identity)
    count += 1

    print(f"MEMORY_METABOLISM_RESEARCH_SELFTEST_PASS {count}")


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

    doc = load_json(Path(args.path))
    errors = validate_document(doc)
    print(
        json.dumps(
            {
                "valid": not errors,
                "scope": "represented Memory Metabolism structural consistency only",
                "errors": errors,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    raise SystemExit(0 if not errors else 1)


if __name__ == "__main__":
    main()
