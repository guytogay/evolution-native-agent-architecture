#!/usr/bin/env python3
from __future__ import annotations
import copy, json
from pathlib import Path
from validate_retrieval_obligation import validate_document, build_sufficiency_resolution

ROOT=Path(__file__).resolve().parent

def base_doc():
    return json.loads((ROOT/'reference-runtime.json').read_text(encoding='utf-8'))

def refresh_resolution(doc, ref='suff:1'):
    packet=build_sufficiency_resolution(doc,'o1',resolution_ref=ref,receipt_ref=f'receipt:{ref}')
    doc['sufficiency_resolutions']=[packet]
    doc['obligations'][0]['closure']['sufficiency_resolution_ref']=ref
    return doc

def expect(name,doc,valid):
    errors=validate_document(doc); got=not errors
    if got != valid:
        raise AssertionError(f'{name}: expected valid={valid}, got errors={errors}')

def main():
    n=0
    d=base_doc(); expect('baseline_subject_bound_resolution',d,True); n+=1
    d=base_doc(); d['retrieval_intents'][0]['decision_context_snapshot_ref']='ctx:d1:v2'; expect('context_change_invalidates_old_resolution',d,False); n+=1
    d=base_doc(); d['attempts'].append({'attempt_id':'a2','obligation_id':'o1','discovery_id':'sd1','scope_ref':'scope:A','sequence':2,'resolver_ref':'resolver','outcome':'HIT','coverage':'PARTIAL','returned_record_ids':['m2'],'receipt_ref':'ret:2'}); expect('later_attempt_invalidates_old_resolution',d,False); n+=1
    d=base_doc(); d['scope_discoveries'][0]['selected_scope_refs']=['scope:A','scope:B']; expect('scope_plan_change_invalidates_old_resolution',d,False); n+=1
    d=base_doc(); d['decisions'][0]['consequence']='NON_MATERIAL'; expect('consequence_change_invalidates_old_resolution',d,False); n+=1
    d=base_doc(); d['sufficiency_resolutions']=[]; expect('missing_resolution_packet_fails',d,False); n+=1
    d=base_doc(); d['sufficiency_resolutions'].append(copy.deepcopy(d['sufficiency_resolutions'][0])); expect('duplicate_resolution_ref_fails',d,False); n+=1
    d=base_doc(); d['sufficiency_resolutions'][0]['subject_fingerprint']='0'*64; expect('wrong_subject_fingerprint_fails',d,False); n+=1
    d=base_doc(); d['scope_discoveries'].append({'discovery_id':'sd2','obligation_id':'o1','sequence':2,'resolver_ref':'resolver','registry_snapshot_ref':'registry:v2','selected_scope_refs':['scope:B'],'outcome':'SCOPES_SELECTED','coverage':'PARTIAL','receipt_ref':'disc:2'}); d['attempts'].append({'attempt_id':'a2','obligation_id':'o1','discovery_id':'sd2','scope_ref':'scope:B','sequence':1,'resolver_ref':'resolver','outcome':'HIT','coverage':'PARTIAL','returned_record_ids':['m2'],'receipt_ref':'ret:2'}); expect('later_discovery_invalidates_old_closure',d,False); n+=1
    d=base_doc(); d['attempts'].append({'attempt_id':'a2','obligation_id':'o1','discovery_id':'sd1','scope_ref':'scope:A','sequence':2,'resolver_ref':'resolver','outcome':'HIT','coverage':'PARTIAL','returned_record_ids':['m2'],'receipt_ref':'ret:2'}); refresh_resolution(d,'suff:2'); expect('fresh_resolution_after_new_attempt_passes',d,True); n+=1
    d=base_doc(); d['obligations'][0]['closure']={'disposition':'NO_HIT_BOUNDED','basis_discovery_id':'sd1','basis_attempt_ids':['a1']}; d['scope_discoveries'][0]['coverage']='DECLARED_DISCOVERY_COMPLETE'; d['attempts'][0].update({'outcome':'NO_HIT','coverage':'DECLARED_SCOPE_COMPLETE','returned_record_ids':[]}); d['sufficiency_resolutions']=[]; expect('no_hit_bounded_needs_no_suff_packet',d,True); n+=1
    d=base_doc(); d['scope_discoveries'][0]['registry_snapshot_ref']='registry:stale-v0'; refresh_resolution(d); expect('stale_registry_remains_external_residual',d,True); n+=1
    d=base_doc(); d['obligations'][0]['closure']={'disposition':'NO_HIT_BOUNDED','basis_discovery_id':'sd1','basis_attempt_ids':[]}; d['scope_discoveries'][0].update({'selected_scope_refs':[],'outcome':'NO_RELEVANT_SCOPE','coverage':'DECLARED_DISCOVERY_COMPLETE'}); d['attempts']=[]; d['sufficiency_resolutions']=[]; expect('false_complete_scope_discovery_remains_external_residual',d,True); n+=1
    d=base_doc(); d['retrieval_intents'][0]['query_scope_ref']='scope:A'; expect('hot_intent_query_scope_still_rejected',d,False); n+=1
    d={'schema_version':'memory-retrieval-obligation-research-0.4','decisions':[{'decision_id':'d1','consequence':'MATERIAL','disposition':'READY','uncertainty_declared':False}],'trigger_events':[],'retrieval_intents':[],'obligations':[],'scope_discoveries':[],'attempts':[],'sufficiency_resolutions':[]}; expect('runtime_missing_trigger_boundary_retained',d,True); n+=1
    print(f'RETRIEVAL_OBLIGATION_04_SUBJECT_BINDING_SELFTEST_PASS {n}')

if __name__=='__main__': main()
