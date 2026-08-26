#!/usr/bin/env python3
"""Deterministic recovered Commitment/Settlement corpus.

Corpus size is descriptive only. This file reconstructs machine checks from
durable semantics; it is not the lost prototype's original byte-identical test set.
"""
from __future__ import annotations
from validate_commitment_settlement import validate_document, next_action


def base():
    return {
        "schema_version": "commitment-settlement-recovered-0.2",
        "decision_commitment_id": "c1",
        "commitments": [{
            "commitment_id": "c1",
            "obligation_subject_ref": "agent:A",
            "counterparty_ref": "party:B",
            "status": "OPEN",
            "partition": {"mode": "INDIVISIBLE"},
            "assignments": [{
                "assignment_id": "a1",
                "generation": 1,
                "executor_ref": "agent:A",
                "status": "ACTIVE",
                "authority_ref": "auth:1",
                "lease_state": "CURRENT",
            }],
            "obligation_transfers": [],
            "settlement": {"state": "OPEN", "evidence_refs": []},
        }]
    }


def expect_invalid(doc, needle):
    errors=validate_document(doc)
    assert errors, "expected invalid"
    assert any(needle in e for e in errors), (needle, errors)
    assert next_action(doc) == "REJECT_INCONSISTENT_RECORD"


def case_base_open():
    d=base()
    assert not validate_document(d), validate_document(d)
    assert next_action(d)=="CONTINUE_WITH_CURRENT_ASSIGNMENT"


def case_two_active_indivisible_rejected():
    d=base()
    d["commitments"][0]["assignments"].append({
        "assignment_id":"a2","generation":2,"executor_ref":"agent:A2","status":"ACTIVE",
        "authority_ref":"auth:2","lease_state":"CURRENT",
    })
    expect_invalid(d,"multiple ACTIVE assignments")


def case_stale_generation_rejected():
    d=base()
    d["commitments"][0]["assignments"][0]["status"]="ACTIVE"
    d["commitments"][0]["assignments"].append({
        "assignment_id":"a2","generation":2,"executor_ref":"agent:A2","status":"SUPERSEDED",
    })
    expect_invalid(d,"stale generation")


def case_new_assignment_supersedes_old():
    d=base()
    d["commitments"][0]["assignments"][0]["status"]="SUPERSEDED"
    d["commitments"][0]["assignments"].append({
        "assignment_id":"a2","generation":2,"executor_ref":"agent:A2","status":"ACTIVE",
        "authority_ref":"auth:2","lease_state":"CURRENT",
    })
    assert not validate_document(d), validate_document(d)
    assert next_action(d)=="CONTINUE_WITH_CURRENT_ASSIGNMENT"
    assert d["commitments"][0]["obligation_subject_ref"]=="agent:A"


def case_lease_expiry_does_not_settle():
    d=base()
    c=d["commitments"][0]
    c["assignments"][0]["status"]="EXPIRED"
    c["assignments"][0]["lease_state"]="EXPIRED"
    assert not validate_document(d), validate_document(d)
    assert next_action(d)=="ASSIGN_OR_WAIT"
    assert c["status"]=="OPEN"


def case_settled_requires_evidence():
    d=base()
    c=d["commitments"][0]
    c["status"]="SETTLED"
    c["settlement"]={"state":"SETTLED","evidence_refs":[]}
    expect_invalid(d,"requires non-empty settlement evidence_refs")


def case_settled_with_evidence():
    d=base()
    c=d["commitments"][0]
    c["assignments"][0]["status"]="SETTLED"
    c["status"]="SETTLED"
    c["settlement"]={"state":"SETTLED","evidence_refs":["receipt:r1"]}
    assert not validate_document(d), validate_document(d)
    assert next_action(d)=="NO_OBLIGATION_ACTION"


def case_cancelled_requires_evidence():
    d=base()
    c=d["commitments"][0]
    c["status"]="CANCELLED"
    c["settlement"]={"state":"CANCELLED","evidence_refs":[]}
    expect_invalid(d,"requires non-empty settlement evidence_refs")


def case_reassignment_does_not_transfer_obligation():
    d=base()
    c=d["commitments"][0]
    c["assignments"][0]["status"]="SUPERSEDED"
    c["assignments"].append({
        "assignment_id":"a2","generation":2,"executor_ref":"agent:A2","status":"ACTIVE",
    })
    assert not validate_document(d), validate_document(d)
    assert c["obligation_subject_ref"]=="agent:A"


def case_accepted_transfer_requires_basis():
    d=base()
    c=d["commitments"][0]
    c["obligation_subject_ref"]="agent:C"
    c["obligation_transfers"]=[{
        "transfer_id":"t1","from_subject_ref":"agent:A","to_subject_ref":"agent:C",
        "status":"ACCEPTED","basis_ref":"","evidence_refs":["ack:1"],
    }]
    expect_invalid(d,"requires basis_ref")


def case_accepted_transfer_requires_evidence():
    d=base()
    c=d["commitments"][0]
    c["obligation_subject_ref"]="agent:C"
    c["obligation_transfers"]=[{
        "transfer_id":"t1","from_subject_ref":"agent:A","to_subject_ref":"agent:C",
        "status":"ACCEPTED","basis_ref":"novation:n1","evidence_refs":[],
    }]
    expect_invalid(d,"requires evidence_refs")


def case_transfer_updates_obligation_subject():
    d=base()
    c=d["commitments"][0]
    c["obligation_subject_ref"]="agent:C"
    c["assignments"][0]["status"]="SUPERSEDED"
    c["obligation_transfers"]=[{
        "transfer_id":"t1","from_subject_ref":"agent:A","to_subject_ref":"agent:C",
        "status":"ACCEPTED","basis_ref":"novation:n1","evidence_refs":["ack:1"],
    }]
    c["status"]="TRANSFERRED"
    assert not validate_document(d), validate_document(d)
    assert next_action(d)=="VERIFY_TRANSFER_AND_LOCAL_BINDING"


def case_transfer_subject_mismatch_rejected():
    d=base()
    c=d["commitments"][0]
    c["obligation_transfers"]=[{
        "transfer_id":"t1","from_subject_ref":"agent:A","to_subject_ref":"agent:C",
        "status":"ACCEPTED","basis_ref":"novation:n1","evidence_refs":["ack:1"],
    }]
    expect_invalid(d,"must match latest accepted transfer target")


def case_counterparty_acceptance_gate():
    d=base()
    a=d["commitments"][0]["assignments"][0]
    a["counterparty_acceptance_required"]=True
    a["counterparty_acceptance"]="PENDING"
    expect_invalid(d,"requires represented counterparty acceptance")


def case_partition_requires_basis():
    d=base()
    c=d["commitments"][0]
    c["partition"]={"mode":"PARTITIONED","disjointness_basis":""}
    c["assignments"][0]["partition_id"]="p1"
    expect_invalid(d,"requires represented disjointness_basis")


def case_partition_duplicate_active_partition_rejected():
    d=base()
    c=d["commitments"][0]
    c["partition"]={"mode":"PARTITIONED","disjointness_basis":"range split"}
    c["assignments"][0]["partition_id"]="p1"
    c["assignments"].append({
        "assignment_id":"a2","generation":1,"executor_ref":"agent:A2",
        "status":"ACTIVE","partition_id":"p1",
    })
    errors=validate_document(d)
    assert any("same partition" in e for e in errors), errors


def case_unknown_settlement_reconciles():
    d=base()
    c=d["commitments"][0]
    c["status"]="UNKNOWN"
    c["settlement"]={"state":"UNKNOWN","evidence_refs":[]}
    assert not validate_document(d), validate_document(d)
    assert next_action(d)=="RECONCILE_SETTLEMENT"


def case_partial_settlement_reconciles():
    d=base()
    c=d["commitments"][0]
    c["status"]="PARTIAL"
    c["settlement"]={"state":"PARTIAL","evidence_refs":["receipt:partial"]}
    assert not validate_document(d), validate_document(d)
    assert next_action(d)=="RECONCILE_SETTLEMENT"


CASES=[
    case_base_open,
    case_two_active_indivisible_rejected,
    case_stale_generation_rejected,
    case_new_assignment_supersedes_old,
    case_lease_expiry_does_not_settle,
    case_settled_requires_evidence,
    case_settled_with_evidence,
    case_cancelled_requires_evidence,
    case_reassignment_does_not_transfer_obligation,
    case_accepted_transfer_requires_basis,
    case_accepted_transfer_requires_evidence,
    case_transfer_updates_obligation_subject,
    case_transfer_subject_mismatch_rejected,
    case_counterparty_acceptance_gate,
    case_partition_requires_basis,
    case_partition_duplicate_active_partition_rejected,
    case_unknown_settlement_reconciles,
    case_partial_settlement_reconciles,
]


def main():
    for case in CASES:
        case()
        print("PASS",case.__name__)
    print(f"PASS recovered_corpus_cases={len(CASES)} (descriptive only; not original lost corpus)")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
