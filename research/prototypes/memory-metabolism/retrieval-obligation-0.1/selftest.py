#!/usr/bin/env python3
from validate_retrieval_obligation import validate_runtime, validate_evaluation

def base_runtime():
    return {
      'schema_version':'memory-retrieval-obligation-research-0.1',
      'decisions':[{'decision_id':'d','consequence':'MATERIAL','disposition':'READY','uncertainty_declared':False}],
      'trigger_events':[{'trigger_id':'t','decision_id':'d','basis':'GENERIC_REFLEX','resolver_ref':'r'}],
      'obligations':[{'obligation_id':'o','decision_id':'d','trigger_ids':['t'],'resolver_ref':'r','query_scope_ref':'q','state':'CLOSED','closure':{'disposition':'RETRIEVAL_USED','basis_attempt_id':'a'}}],
      'attempts':[{'attempt_id':'a','obligation_id':'o','sequence':1,'resolver_ref':'r','query_scope_ref':'q','outcome':'HIT','coverage':'PARTIAL','returned_record_ids':['m1'],'receipt_ref':'rcpt:a'}]
    }

def expect(name,doc,valid):
    e=validate_runtime(doc); assert bool(e) is (not valid), f'{name}: expected {valid}, got {e}'

def ev(stage='SUCCESS'):
    return {'schema_version':'memory-retrieval-evaluation-research-0.1','evaluation_id':'e','decision_id':'d','oracle_retrieval_needed':'YES','trigger_fired':True,'query_scope_adequate':'YES','resolver_execution':'SUCCEEDED','oracle_relevant_record_ids':['m1'],'returned_record_ids':['m1'],'projected_record_ids':['m1'],'applied_record_ids':['m1'],'failure_stage':stage}

def expect_eval(name,x,valid):
    e=validate_evaluation(x); assert bool(e) is (not valid), f'{name}: expected {valid}, got {e}'

def main():
    n=0
    expect('baseline',base_runtime(),True); n+=1
    x=base_runtime(); x['trigger_events']=[]; x['obligations']=[]; x['attempts']=[]
    expect('runtime_does_not_pretend_to_detect_missing_trigger',x,True); n+=1
    x=base_runtime(); x['obligations'][0]['state']='PENDING'; x['obligations'][0].pop('closure'); x['attempts']=[]
    expect('ready_with_pending_obligation',x,False); n+=1
    x=base_runtime(); x['attempts'][0].update({'outcome':'NO_HIT','coverage':'UNKNOWN','returned_record_ids':[]}); x['obligations'][0]['closure']={'disposition':'NO_HIT_BOUNDED','basis_attempt_id':'a'}
    expect('nohit_unknown_not_absence',x,False); n+=1
    x=base_runtime(); x['attempts'][0].update({'outcome':'NO_HIT','coverage':'DECLARED_SCOPE_COMPLETE','returned_record_ids':[]}); x['obligations'][0]['closure']={'disposition':'NO_HIT_BOUNDED','basis_attempt_id':'a'}
    expect('bounded_nohit',x,True); n+=1
    x=base_runtime(); x['attempts'][0]['query_scope_ref']='other'
    expect('query_scope_binding',x,False); n+=1
    x=base_runtime(); x['trigger_events'][0]['resolver_ref']='r2'
    expect('resolver_binding',x,False); n+=1
    x=base_runtime(); x['obligations'][0]['closure']={'disposition':'RETRIEVAL_USED','basis_attempt_id':'a'}; x['attempts'][0].update({'outcome':'NO_HIT','coverage':'DECLARED_SCOPE_COMPLETE','returned_record_ids':[]})
    expect('used_requires_hit',x,False); n+=1
    x=base_runtime(); x['decisions'][0].update({'consequence':'NON_MATERIAL','disposition':'PROCEED_UNCERTAIN','uncertainty_declared':True}); x['attempts'][0].update({'outcome':'FAILED','coverage':'UNKNOWN','returned_record_ids':[]}); x['obligations'][0]['closure']={'disposition':'UNCERTAIN_CONTINUATION','basis_attempt_id':'a'}
    expect('low_consequence_uncertain_continuation',x,True); n+=1
    x=base_runtime(); x['decisions'][0].update({'disposition':'PROCEED_UNCERTAIN','uncertainty_declared':True}); x['attempts'][0].update({'outcome':'FAILED','coverage':'UNKNOWN','returned_record_ids':[]}); x['obligations'][0]['closure']={'disposition':'UNCERTAIN_CONTINUATION','basis_attempt_id':'a'}
    expect('material_not_cleared_by_uncertainty',x,False); n+=1
    x=base_runtime(); x['decisions'][0]['disposition']='NARROWED'; x['attempts'][0].update({'outcome':'FAILED','coverage':'UNKNOWN','returned_record_ids':[]}); x['obligations'][0]['closure']={'disposition':'CONSEQUENCE_NARROWED','basis_attempt_id':'a'}
    expect('material_can_narrow_after_failure',x,True); n+=1
    x=base_runtime(); x['obligations'][0]['closure']['basis_attempt_id']='missing'
    expect('closure_must_bind_attempt',x,False); n+=1
    x=base_runtime(); x['attempts'].append({'attempt_id':'a2','obligation_id':'o','sequence':1,'resolver_ref':'r','query_scope_ref':'q','outcome':'FAILED','coverage':'UNKNOWN','returned_record_ids':[],'receipt_ref':'rcpt:a2'})
    expect('attempt_sequence_unique',x,False); n+=1
    x=base_runtime(); x['trigger_events'].append({'trigger_id':'t2','decision_id':'d','basis':'HOST_SIGNAL','resolver_ref':'r'}); x['obligations'][0]['trigger_ids'].append('t2')
    expect('one_obligation_can_externalize_multiple_same_decision_triggers',x,True); n+=1
    x=base_runtime(); x['trigger_events'].append({'trigger_id':'t2','decision_id':'d','basis':'HOST_SIGNAL','resolver_ref':'r'})
    expect('every_trigger_must_be_externalized',x,False); n+=1
    expect_eval('eval_success',ev(),True); n+=1
    x=ev(); x.update({'trigger_fired':False,'query_scope_adequate':'NOT_APPLICABLE','resolver_execution':'NOT_INVOKED','returned_record_ids':[],'projected_record_ids':[],'applied_record_ids':[],'failure_stage':'TRIGGER_FALSE_NEGATIVE'})
    expect_eval('trigger_false_negative',x,True); n+=1
    x=ev(); x.update({'query_scope_adequate':'NO','returned_record_ids':[],'projected_record_ids':[],'applied_record_ids':[],'failure_stage':'QUERY_SCOPE_MISS'})
    expect_eval('query_scope_miss',x,True); n+=1
    x=ev(); x.update({'resolver_execution':'FAILED','returned_record_ids':[],'projected_record_ids':[],'applied_record_ids':[],'failure_stage':'RESOLVER_FAILURE'})
    expect_eval('resolver_failure',x,True); n+=1
    x=ev(); x.update({'returned_record_ids':[],'projected_record_ids':[],'applied_record_ids':[],'failure_stage':'RESOLVER_FALSE_NEGATIVE'})
    expect_eval('resolver_false_negative',x,True); n+=1
    x=ev(); x.update({'projected_record_ids':[],'applied_record_ids':[],'failure_stage':'PROJECTION_DROP'})
    expect_eval('projection_drop',x,True); n+=1
    x=ev(); x.update({'applied_record_ids':[],'failure_stage':'APPLICATION_FAILURE'})
    expect_eval('application_failure',x,True); n+=1
    x=ev(); x['failure_stage']='TRIGGER_FALSE_NEGATIVE'
    expect_eval('wrong_failure_stage_blocked',x,False); n+=1
    print('TRIGGERED_RETRIEVAL_OBLIGATION_01_SELFTEST_PASS',n)
if __name__=='__main__': main()
