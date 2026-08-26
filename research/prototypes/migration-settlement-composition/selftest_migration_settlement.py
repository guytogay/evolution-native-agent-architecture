#!/usr/bin/env python3
"""Deterministic source-aware migration × settlement composition cases.

Case count is descriptive only.
"""
from __future__ import annotations
import copy
import sys
from pathlib import Path

HERE=Path(__file__).resolve().parent
CS=HERE.parent/"commitment-settlement-recovered"/"tools"
sys.path.insert(0,str(CS))
from validate_commitment_settlement import validate_document as validate_commitment
from validate_migration_settlement import (
    build_manifest, packet_only_false_ok, validate_package
)


def source(with_obligation=True):
    d={
        "candidate_id":"var-1",
        "origin":"LOCAL_VARIATION",
        "lifecycle_state":"ARCHIVED",
        "expression_state":"LATENT",
        "selection_state":"UNKNOWN",
        "triggered_obligation_refs":[],
    }
    if with_obligation:
        d["triggered_obligation_refs"]=["commitment:c1"]
    return d


def packet():
    return {
        "packet_schema":"ena-adaptation-packet.v2",
        "source_candidate_id":"var-1",
        "source_lifecycle_state":"ARCHIVED",
        "source_expression_state":"LATENT",
        "source_selection_state":"UNKNOWN",
        "source_experiments":[],
        "source_evaluations":[],
        "source_expression_history":[],
        "source_integration_history":[],
        "source_negative_lineage_refs":[],
        "transfer_status":"TRANSFERRED_SOURCE_EVIDENCE_NOT_LOCAL_PROOF",
        "source_authentication":"NOT_AUTHENTICATED_BY_THIS_PACKET",
    }


def open_commitment():
    return {
        "commitment_id":"c1",
        "obligation_subject_ref":"agent:A",
        "counterparty_ref":"party:B",
        "status":"OPEN",
        "partition":{"mode":"INDIVISIBLE"},
        "assignments":[{
            "assignment_id":"a1","generation":1,"executor_ref":"agent:A",
            "status":"ACTIVE","lease_state":"CURRENT",
        }],
        "obligation_transfers":[],
        "settlement":{"state":"OPEN","evidence_refs":[]},
    }


def settled_commitment():
    c=open_commitment()
    c["assignments"][0]["status"]="SETTLED"
    c["status"]="SETTLED"
    c["settlement"]={"state":"SETTLED","evidence_refs":["receipt:r1"]}
    return c


def package(src, carriers):
    pkt=packet()
    return {
        "adaptation_packet":pkt,
        "projection_manifest":build_manifest(src,pkt,carriers),
    }


def case_packet_only_cannot_detect_omission():
    pkg={"adaptation_packet":packet()}
    assert packet_only_false_ok(pkg) is True


def case_source_aware_manifest_rejects_omission():
    src=source(True)
    pkg=package(src,[])
    errors,action=validate_package(src,pkg,{})
    assert errors and any("omitted from lineage carriers" in e for e in errors),errors
    assert action=="REJECT_PACKAGE"


def case_raw_ref_preserves_fact_but_not_resolution():
    src=source(True)
    carriers=[{
        "lineage_class":"UNRESOLVED_OBLIGATION",
        "source_ref":"commitment:c1",
        "mode":"RAW_SOURCE_REF",
        "receiver_resolution":"UNRESOLVED",
    }]
    pkg=package(src,carriers)
    errors,action=validate_package(src,pkg,{})
    assert not errors,errors
    assert action=="WAIT_NARROW_OR_LOCAL_REBIND"


def case_raw_ref_cannot_self_assert_resolution():
    src=source(True)
    carriers=[{
        "lineage_class":"UNRESOLVED_OBLIGATION",
        "source_ref":"commitment:c1",
        "mode":"RAW_SOURCE_REF",
        "receiver_resolution":"RESOLVED",
    }]
    pkg=package(src,carriers)
    errors,action=validate_package(src,pkg,{})
    assert any("cannot self-assert receiver resolution" in e for e in errors),errors
    assert action=="REJECT_PACKAGE"


def case_shadow_cannot_mint_local_authority():
    src=source(True)
    carriers=[{
        "lineage_class":"UNRESOLVED_OBLIGATION",
        "source_ref":"commitment:c1",
        "mode":"SOURCE_SHADOW",
        "summary_state":"OPEN",
        "local_authority_granted":True,
    }]
    pkg=package(src,carriers)
    errors,action=validate_package(src,pkg,{})
    assert any("cannot mint local authority" in e for e in errors),errors
    assert action=="REJECT_PACKAGE"


def case_shadow_preserves_blocker_without_transfer():
    src=source(True)
    carriers=[{
        "lineage_class":"UNRESOLVED_OBLIGATION",
        "source_ref":"commitment:c1",
        "mode":"SOURCE_SHADOW",
        "summary_state":"OPEN",
        "local_authority_granted":False,
        "local_executor_assigned":False,
    }]
    pkg=package(src,carriers)
    errors,action=validate_package(src,pkg,{})
    assert not errors,errors
    assert action=="WAIT_NARROW_OR_LOCAL_REBIND"


def case_typed_open_commitment_survives_but_requires_rebind():
    src=source(True)
    c=open_commitment()
    assert not validate_commitment({"commitments":[c]}), validate_commitment({"commitments":[c]})
    carriers=[{
        "lineage_class":"UNRESOLVED_OBLIGATION",
        "source_ref":"commitment:c1",
        "mode":"TYPED_COMMITMENT_CARRIER",
        "commitment_id":"c1",
    }]
    pkg=package(src,carriers)
    errors,action=validate_package(src,pkg,{"c1":c})
    assert not errors,errors
    assert action=="WAIT_NARROW_OR_LOCAL_REBIND"


def case_typed_settled_commitment_no_longer_blocks():
    src=source(True)
    c=settled_commitment()
    assert not validate_commitment({"commitments":[c]}), validate_commitment({"commitments":[c]})
    carriers=[{
        "lineage_class":"UNRESOLVED_OBLIGATION",
        "source_ref":"commitment:c1",
        "mode":"TYPED_COMMITMENT_CARRIER",
        "commitment_id":"c1",
    }]
    pkg=package(src,carriers)
    errors,action=validate_package(src,pkg,{"c1":c})
    assert not errors,errors
    assert action=="IMPORT_WITHOUT_OBLIGATION_BLOCKER"


def case_no_source_obligation_needs_no_carrier():
    src=source(False)
    pkg=package(src,[])
    errors,action=validate_package(src,pkg,{})
    assert not errors,errors
    assert action=="IMPORT_WITHOUT_OBLIGATION_BLOCKER"


def case_manifest_digest_detects_source_mutation_after_projection():
    src=source(True)
    pkg=package(src,[{
        "lineage_class":"UNRESOLVED_OBLIGATION",
        "source_ref":"commitment:c1","mode":"RAW_SOURCE_REF","receiver_resolution":"UNRESOLVED",
    }])
    mutated=copy.deepcopy(src)
    mutated["triggered_obligation_refs"].append("commitment:c2")
    errors,action=validate_package(mutated,pkg,{})
    assert any("source_record_digest mismatch" in e for e in errors),errors
    assert action=="REJECT_PACKAGE"


def case_manifest_digest_detects_packet_mutation():
    src=source(True)
    pkg=package(src,[{
        "lineage_class":"UNRESOLVED_OBLIGATION",
        "source_ref":"commitment:c1","mode":"RAW_SOURCE_REF","receiver_resolution":"UNRESOLVED",
    }])
    pkg["adaptation_packet"]["source_selection_state"]="SUPPORTED"
    errors,action=validate_package(src,pkg,{})
    assert any("portable_packet_digest mismatch" in e for e in errors),errors
    assert action=="REJECT_PACKAGE"


CASES=[
    case_packet_only_cannot_detect_omission,
    case_source_aware_manifest_rejects_omission,
    case_raw_ref_preserves_fact_but_not_resolution,
    case_raw_ref_cannot_self_assert_resolution,
    case_shadow_cannot_mint_local_authority,
    case_shadow_preserves_blocker_without_transfer,
    case_typed_open_commitment_survives_but_requires_rebind,
    case_typed_settled_commitment_no_longer_blocks,
    case_no_source_obligation_needs_no_carrier,
    case_manifest_digest_detects_source_mutation_after_projection,
    case_manifest_digest_detects_packet_mutation,
]


def main():
    for case in CASES:
        case()
        print("PASS",case.__name__)
    print(f"PASS composition_cases={len(CASES)} (descriptive only)")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
