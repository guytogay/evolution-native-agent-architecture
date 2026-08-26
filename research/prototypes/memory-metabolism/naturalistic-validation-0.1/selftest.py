#!/usr/bin/env python3
from __future__ import annotations

from validate_field_observation import validate_document


def base_doc():
    return {
        "protocol_version": "memory-naturalistic-validation-research-0.1",
        "observation_id": "field-1",
        "evidence_class": "PRIMARY_NATURALISTIC",
        "host_profile": {
            "host_ref": "host:test",
            "resolver_organ_ref": "resolver:test",
            "hot_catalog_exposure": "NONE"
        },
        "task": {
            "task_ref": "task:1",
            "natural_task": True,
            "task_summary": "ordinary project task"
        },
        "retrieval_trace": [],
        "later_challenges": [],
        "assessment": {
            "status": "UNASSESSED",
            "failure_stage": "UNRESOLVED",
            "basis_refs": []
        },
        "utility_observation": {
            "decision_effect": "UNKNOWN",
            "basis_refs": []
        }
    }


def expect(name, doc, valid):
    errors = validate_document(doc)
    got = not errors
    if got != valid:
        raise AssertionError(f"{name}: expected valid={valid}, errors={errors}")


def main():
    n = 0

    d = base_doc(); expect("unassessed_default_valid", d, True); n += 1

    d = base_doc(); d["host_profile"]["hot_catalog_exposure"]="FULL_CATALOG"; expect("primary_rejects_full_hot_catalog", d, False); n += 1

    d = base_doc(); d["host_profile"]["hot_catalog_exposure"]="UNKNOWN"; expect("primary_rejects_unknown_hot_exposure", d, False); n += 1

    d = base_doc(); d["evidence_class"]="CONTEXT_CONTAMINATED_FIELD"; d["host_profile"]["hot_catalog_exposure"]="FULL_CATALOG"; expect("contaminated_field_can_record_full_hot_catalog", d, True); n += 1

    d = base_doc(); d["evidence_class"]="INDEPENDENT_NATURALISTIC"; d["host_profile"]["hot_catalog_exposure"]="BOUNDED_SUMMARY"; expect("independent_naturalistic_bounded_summary_valid", d, True); n += 1

    d = base_doc(); d["assessment"]["basis_refs"] = ["e:1"]; expect("unassessed_cannot_assert_failure_basis", d, False); n += 1

    d = base_doc(); d["assessment"] = {"status":"NO_MATERIAL_FAILURE_OBSERVED","failure_stage":"NONE","basis_refs":[]}; expect("no_failure_observed_valid", d, True); n += 1

    d = base_doc(); d["assessment"] = {"status":"NO_MATERIAL_FAILURE_OBSERVED","failure_stage":"R0_TRIGGER","basis_refs":[]}; expect("no_failure_observed_cannot_name_failure_stage", d, False); n += 1

    d = base_doc(); d["assessment"] = {"status":"MATERIAL_FAILURE_OBSERVED","failure_stage":"R0_TRIGGER","basis_refs":["memory:old-decision"]}; d["later_challenges"]=[{"challenge_type":"LATER_MEMORY_FOUND","evidence_ref":"memory:old-decision","decision_effect":"CHANGED_MATERIAL_DECISION"}]; expect("trigger_miss_can_have_no_retrieval_trace", d, True); n += 1

    d = base_doc(); d["assessment"] = {"status":"MATERIAL_FAILURE_OBSERVED","failure_stage":"SCOPE_DISCOVERY","basis_refs":["memory:m1"]}; d["later_challenges"]=[{"challenge_type":"LATER_MEMORY_FOUND","evidence_ref":"memory:m1","decision_effect":"CHANGED_MATERIAL_DECISION"}]; expect("downstream_failure_needs_trace", d, False); n += 1

    d = base_doc(); d["retrieval_trace"]=[{"sequence":1,"stage":"INVOCATION","event":"resolver invoked","evidence_ref":"trace:1"}]; d["assessment"] = {"status":"MATERIAL_FAILURE_OBSERVED","failure_stage":"SCOPE_DISCOVERY","basis_refs":["memory:m1"]}; d["later_challenges"]=[{"challenge_type":"LATER_MEMORY_FOUND","evidence_ref":"memory:m1","decision_effect":"CHANGED_MATERIAL_DECISION"}]; expect("downstream_failure_with_trace_valid", d, True); n += 1

    d = base_doc(); d["assessment"] = {"status":"MATERIAL_FAILURE_OBSERVED","failure_stage":"R0_TRIGGER","basis_refs":["memory:m1"]}; expect("material_failure_requires_later_challenge", d, False); n += 1

    d = base_doc(); d["assessment"] = {"status":"MATERIAL_FAILURE_OBSERVED","failure_stage":"R0_TRIGGER","basis_refs":["memory:m1"]}; d["later_challenges"]=[{"challenge_type":"LATER_MEMORY_FOUND","evidence_ref":"memory:m1","decision_effect":"NO_CHANGE"}]; expect("material_failure_requires_material_decision_effect", d, False); n += 1

    d = base_doc(); d["retrieval_trace"]=[{"sequence":1,"stage":"INVOCATION","event":"call","evidence_ref":"t1"},{"sequence":1,"stage":"RETRIEVAL","event":"hit","evidence_ref":"t2"}]; expect("duplicate_trace_sequence_invalid", d, False); n += 1

    d = base_doc(); d["retrieval_trace"]=[{"sequence":2,"stage":"RETRIEVAL","event":"hit","evidence_ref":"t2"},{"sequence":1,"stage":"INVOCATION","event":"call","evidence_ref":"t1"}]; expect("out_of_order_trace_invalid", d, False); n += 1

    d = base_doc(); d["utility_observation"]={"decision_effect":"CHANGED_MATERIAL_DECISION","basis_refs":[]}; expect("utility_change_requires_basis", d, False); n += 1

    d = base_doc(); d["utility_observation"]={"decision_effect":"CHANGED_MATERIAL_DECISION","basis_refs":["decision:before-after"]}; expect("utility_change_with_basis_valid", d, True); n += 1

    d = base_doc(); d["assessment"]={"status":"UNRESOLVED","failure_stage":"UNRESOLVED","basis_refs":[]}; d["later_challenges"]=[{"challenge_type":"MANUAL_AUDIT","evidence_ref":"audit:1","decision_effect":"UNKNOWN"}]; expect("unresolved_with_challenge_valid", d, True); n += 1

    d = base_doc(); d["assessment"]={"status":"UNRESOLVED","failure_stage":"UNRESOLVED","basis_refs":[]}; expect("unresolved_without_any_basis_invalid", d, False); n += 1

    print(f"NATURALISTIC_VALIDATION_01_SELFTEST_DEFINED {n}")


if __name__ == "__main__":
    main()
