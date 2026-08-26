#!/usr/bin/env python3
from __future__ import annotations
import copy
from validate_retrieval_obligation import validate_document

def base_doc():
    return {
      "schema_version":"memory-retrieval-obligation-research-0.3",
      "decisions":[{"decision_id":"d1","consequence":"MATERIAL","disposition":"READY","uncertainty_declared":False}],
      "trigger_events":[{"trigger_id":"t1","decision_id":"d1","basis":"GENERIC_REFLEX","resolver_ref":"resolver"}],
      "retrieval_intents":[{"intent_id":"i1","decision_id":"d1","trigger_ids":["t1"],"resolver_ref":"resolver","decision_context_ref":"ctx:d1","need_basis":"DURABLE_STATE_MAY_CHANGE_DECISION"}],
      "obligations":[{"obligation_id":"o1","decision_id":"d1","intent_id":"i1","resolver_ref":"resolver","state":"CLOSED","closure":{"disposition":"RETRIEVAL_SUFFICIENCY_RESOLVED","basis_discovery_id":"sd1","basis_attempt_ids":["a1"],"sufficiency_resolution_ref":"external:suff:d1"}}],
      "scope_discoveries":[{"discovery_id":"sd1","obligation_id":"o1","sequence":1,"resolver_ref":"resolver","registry_snapshot_ref":"registry:v1","selected_scope_refs":["scope:A"],"outcome":"SCOPES_SELECTED","coverage":"PARTIAL","receipt_ref":"disc:1"}],
      "attempts":[{"attempt_id":"a1","obligation_id":"o1","discovery_id":"sd1","scope_ref":"scope:A","sequence":1,"resolver_ref":"resolver","outcome":"HIT","coverage":"PARTIAL","returned_record_ids":["m1"],"receipt_ref":"ret:1"}]
    }

def expect(name,doc,valid):
    errors=validate_document(doc); got=not errors
    if got != valid: raise AssertionError(f"{name}: expected valid={valid}, got errors={errors}")

def main():
    n=0
    d=base_doc(); expect("baseline_sufficiency_resolved",d,True); n+=1
    d=base_doc(); d["obligations"][0]["closure"].pop("sufficiency_resolution_ref"); expect("hit_without_sufficiency_ref",d,False); n+=1
    d=base_doc(); d["attempts"][0]["outcome"]="NO_HIT"; d["attempts"][0]["returned_record_ids"]=[]; expect("sufficiency_requires_hit",d,False); n+=1
    d=base_doc(); d["scope_discoveries"].append({"discovery_id":"sd2","obligation_id":"o1","sequence":2,"resolver_ref":"resolver","registry_snapshot_ref":"registry:v2","selected_scope_refs":["scope:B"],"outcome":"SCOPES_SELECTED","coverage":"PARTIAL","receipt_ref":"disc:2"}); d["attempts"].append({"attempt_id":"a2","obligation_id":"o1","discovery_id":"sd2","scope_ref":"scope:B","sequence":1,"resolver_ref":"resolver","outcome":"HIT","coverage":"PARTIAL","returned_record_ids":["m2"],"receipt_ref":"ret:2"}); expect("closure_cannot_bind_old_discovery",d,False); n+=1
    d=base_doc(); d["scope_discoveries"].append({"discovery_id":"sd2","obligation_id":"o1","sequence":1,"resolver_ref":"resolver","registry_snapshot_ref":"registry:v2","selected_scope_refs":[],"outcome":"NO_RELEVANT_SCOPE","coverage":"DECLARED_DISCOVERY_COMPLETE","receipt_ref":"disc:2"}); expect("duplicate_discovery_sequence",d,False); n+=1
    d=base_doc(); d["obligations"][0]["closure"]={"disposition":"NO_HIT_BOUNDED","basis_discovery_id":"sd1","basis_attempt_ids":["a1"]}; d["scope_discoveries"][0]["coverage"]="DECLARED_DISCOVERY_COMPLETE"; d["attempts"][0].update({"outcome":"NO_HIT","coverage":"DECLARED_SCOPE_COMPLETE","returned_record_ids":[]}); expect("no_hit_bounded_valid",d,True); n+=1
    d2=copy.deepcopy(d); d2["scope_discoveries"][0]["selected_scope_refs"]=["scope:A","scope:B"]; expect("no_hit_must_cover_all_scopes",d2,False); n+=1
    d2=copy.deepcopy(d); d2["attempts"].append({"attempt_id":"a2","obligation_id":"o1","discovery_id":"sd1","scope_ref":"scope:A","sequence":2,"resolver_ref":"resolver","outcome":"HIT","coverage":"PARTIAL","returned_record_ids":["m2"],"receipt_ref":"ret:2"}); expect("no_hit_cannot_hide_hit",d2,False); n+=1
    d=base_doc(); d["obligations"][0]["closure"]={"disposition":"NO_HIT_BOUNDED","basis_discovery_id":"sd1","basis_attempt_ids":[]}; d["scope_discoveries"][0].update({"selected_scope_refs":[],"outcome":"NO_RELEVANT_SCOPE","coverage":"DECLARED_DISCOVERY_COMPLETE"}); d["attempts"]=[]; expect("no_relevant_scope_valid_structurally",d,True); n+=1
    d2=copy.deepcopy(d); d2["scope_discoveries"][0]["coverage"]="UNKNOWN"; expect("no_relevant_scope_requires_complete_discovery",d2,False); n+=1
    d=base_doc(); d["retrieval_intents"][0]["query_scope_ref"]="scope:A"; expect("hot_intent_rejects_query_scope",d,False); n+=1
    d=base_doc(); d["decisions"][0].update({"disposition":"PROCEED_UNCERTAIN","uncertainty_declared":True}); d["obligations"][0]["state"]="ATTEMPTED"; d["obligations"][0].pop("closure"); expect("material_proceed_uncertain_invalid",d,False); n+=1
    d["decisions"][0]["consequence"]="NON_MATERIAL"; expect("nonmaterial_proceed_uncertain_valid",d,True); n+=1
    d=base_doc(); d["attempts"].append({"attempt_id":"a2","obligation_id":"o1","discovery_id":"sd1","scope_ref":"scope:A","sequence":1,"resolver_ref":"resolver","outcome":"NO_HIT","coverage":"PARTIAL","returned_record_ids":[],"receipt_ref":"ret:2"}); expect("duplicate_attempt_sequence",d,False); n+=1
    d=base_doc(); d["attempts"][0]["scope_ref"]="scope:B"; expect("attempt_scope_must_be_selected",d,False); n+=1
    d=base_doc(); d["retrieval_intents"]=[]; d["obligations"]=[]; d["scope_discoveries"]=[]; d["attempts"]=[]; expect("trigger_must_externalize",d,False); n+=1
    d=base_doc(); d["obligations"]=[]; d["scope_discoveries"]=[]; d["attempts"]=[]; expect("intent_must_externalize",d,False); n+=1
    d={"schema_version":"memory-retrieval-obligation-research-0.3","decisions":[{"decision_id":"d1","consequence":"MATERIAL","disposition":"READY","uncertainty_declared":False}],"trigger_events":[],"retrieval_intents":[],"obligations":[],"scope_discoveries":[],"attempts":[]}; expect("runtime_cannot_detect_missing_trigger",d,True); n+=1
    d=base_doc(); d["scope_discoveries"][0]["registry_snapshot_ref"]="registry:stale-v0"; expect("stale_registry_not_structurally_provable",d,True); n+=1
    d=base_doc(); d["obligations"][0]["closure"]={"disposition":"NO_HIT_BOUNDED","basis_discovery_id":"sd1","basis_attempt_ids":[]}; d["scope_discoveries"][0].update({"selected_scope_refs":[],"outcome":"NO_RELEVANT_SCOPE","coverage":"DECLARED_DISCOVERY_COMPLETE"}); d["attempts"]=[]; expect("false_complete_scope_discovery_can_still_pass",d,True); n+=1
    d=base_doc(); scopes=[f"scope:{i}" for i in range(50)]; d["scope_discoveries"][0]["selected_scope_refs"]=scopes; d["scope_discoveries"][0]["coverage"]="DECLARED_DISCOVERY_COMPLETE"; d["attempts"]=[]
    for i,s in enumerate(scopes,1): d["attempts"].append({"attempt_id":f"a{i}","obligation_id":"o1","discovery_id":"sd1","scope_ref":s,"sequence":i,"resolver_ref":"resolver","outcome":"NO_HIT","coverage":"DECLARED_SCOPE_COMPLETE","returned_record_ids":[],"receipt_ref":f"ret:{i}"})
    d["obligations"][0]["closure"]={"disposition":"NO_HIT_BOUNDED","basis_discovery_id":"sd1","basis_attempt_ids":[f"a{i}" for i in range(1,51)]}; expect("search_all_is_cost_issue_not_structural_failure",d,True); n+=1
    d=base_doc(); d["obligations"][0]["closure"]={"disposition":"NO_HIT_BOUNDED","basis_discovery_id":"sd1","basis_attempt_ids":["a1"]}; d["scope_discoveries"][0]["coverage"]="DECLARED_DISCOVERY_COMPLETE"; d["attempts"][0].update({"outcome":"NO_HIT","coverage":"DECLARED_SCOPE_COMPLETE","returned_record_ids":[]}); d["attempts"].append({"attempt_id":"a2","obligation_id":"o1","discovery_id":"sd1","scope_ref":"scope:A","sequence":2,"resolver_ref":"resolver","outcome":"PARTIAL","coverage":"PARTIAL","returned_record_ids":[],"receipt_ref":"ret:2"}); expect("no_hit_must_account_all_attempts",d,False); n+=1
    d=base_doc(); d["scope_discoveries"][0]["coverage"]="UNKNOWN"; d["attempts"][0]["coverage"]="PARTIAL"; expect("external_sufficiency_can_resolve_partial_search",d,True); n+=1
    print(f"RETRIEVAL_OBLIGATION_03_SELFTEST_PASS {n}")

if __name__=="__main__": main()
