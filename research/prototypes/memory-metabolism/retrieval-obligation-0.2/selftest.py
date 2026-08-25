#!/usr/bin/env python3
import copy
from validate_retrieval_obligation import validate_document

def base():
    return {
      'schema_version':'memory-retrieval-obligation-research-0.2',
      'decisions':[{'decision_id':'d','consequence':'MATERIAL','disposition':'READY','uncertainty_declared':False}],
      'trigger_events':[{'trigger_id':'t','decision_id':'d','basis':'GENERIC_REFLEX','resolver_ref':'memory-resolver'}],
      'retrieval_intents':[{'intent_id':'i','decision_id':'d','trigger_ids':['t'],'resolver_ref':'memory-resolver','decision_context_ref':'ctx:d','need_basis':'DURABLE_STATE_MAY_CHANGE_DECISION'}],
      'obligations':[{'obligation_id':'o','decision_id':'d','intent_id':'i','resolver_ref':'memory-resolver','state':'CLOSED','closure':{'disposition':'RETRIEVAL_USED','basis_discovery_id':'sd','basis_attempt_ids':['a']}}],
      'scope_discoveries':[{'discovery_id':'sd','obligation_id':'o','sequence':1,'resolver_ref':'memory-resolver','registry_snapshot_ref':'registry:v1','selected_scope_refs':['scope:recovery'],'outcome':'SCOPES_SELECTED','coverage':'PARTIAL','receipt_ref':'scope-receipt:1'}],
      'attempts':[{'attempt_id':'a','obligation_id':'o','discovery_id':'sd','scope_ref':'scope:recovery','sequence':1,'resolver_ref':'memory-resolver','outcome':'HIT','coverage':'PARTIAL','returned_record_ids':['m1'],'receipt_ref':'retrieval-receipt:1'}]
    }

def check(name,doc,valid):
    e=validate_document(doc)
    assert (not e)==valid, f'{name}: expected {valid}, got {e}'
    return 1

def run():
    n=0
    d=base(); n+=check('baseline-hit',d,True)
    d=base(); d['retrieval_intents'][0]['query_scope_ref']='scope:x'; n+=check('hot-intent-cannot-carry-domain',d,False)
    d=base(); d['scope_discoveries'][0]['selected_scope_refs']=[]; n+=check('selected-needs-scope',d,False)
    d=base(); sd=d['scope_discoveries'][0]; sd['outcome']='NO_RELEVANT_SCOPE'; sd['selected_scope_refs']=['scope:x']; n+=check('no-relevant-scope-cannot-select',d,False)
    d=base(); d['attempts'][0]['scope_ref']='scope:other'; n+=check('attempt-must-use-selected-scope',d,False)
    d=base(); sd=d['scope_discoveries'][0]; sd['coverage']='DECLARED_DISCOVERY_COMPLETE'; a=d['attempts'][0]; a['outcome']='NO_HIT'; a['coverage']='DECLARED_SCOPE_COMPLETE'; a['returned_record_ids']=[]; d['obligations'][0]['closure']['disposition']='NO_HIT_BOUNDED'; n+=check('bounded-no-hit-valid',d,True)
    d=base(); sd=d['scope_discoveries'][0]; a=d['attempts'][0]; a['outcome']='NO_HIT'; a['coverage']='DECLARED_SCOPE_COMPLETE'; a['returned_record_ids']=[]; d['obligations'][0]['closure']['disposition']='NO_HIT_BOUNDED'; n+=check('bounded-no-hit-needs-discovery-complete',d,False)
    d=base(); sd=d['scope_discoveries'][0]; sd['coverage']='DECLARED_DISCOVERY_COMPLETE'; sd['selected_scope_refs']=['scope:a','scope:b']; a=d['attempts'][0]; a['scope_ref']='scope:a'; a['outcome']='NO_HIT'; a['coverage']='DECLARED_SCOPE_COMPLETE'; a['returned_record_ids']=[]; d['obligations'][0]['closure']['disposition']='NO_HIT_BOUNDED'; n+=check('bounded-no-hit-must-cover-all-scopes',d,False)
    d=base(); sd=d['scope_discoveries'][0]; sd['coverage']='DECLARED_DISCOVERY_COMPLETE'; a=d['attempts'][0]; a['outcome']='NO_HIT'; a['coverage']='PARTIAL'; a['returned_record_ids']=[]; d['obligations'][0]['closure']['disposition']='NO_HIT_BOUNDED'; n+=check('bounded-no-hit-needs-inscope-complete',d,False)
    d=base(); old=copy.deepcopy(d['scope_discoveries'][0]); old['discovery_id']='sd-old'; old['sequence']=1; old['selected_scope_refs']=['scope:wrong']; old['registry_snapshot_ref']='registry:v0'; d['scope_discoveries'][0]['sequence']=2; d['scope_discoveries'].insert(0,old); n+=check('newer-discovery-may-supersede-by-closure-basis',d,True)
    d=base(); old=copy.deepcopy(d['scope_discoveries'][0]); old['discovery_id']='sd-old'; old['selected_scope_refs']=['scope:wrong']; d['scope_discoveries'].insert(0,old); d['obligations'][0]['closure']['basis_discovery_id']='sd'; d['obligations'][0]['closure']['basis_attempt_ids']=['a-old']; ao=copy.deepcopy(d['attempts'][0]); ao['attempt_id']='a-old'; ao['discovery_id']='sd-old'; ao['scope_ref']='scope:wrong'; d['attempts'].append(ao); n+=check('closure-attempt-must-match-basis-discovery',d,False)
    d=base(); d['decisions'][0]['disposition']='READY'; d['obligations'][0]['closure']['disposition']='UNCERTAIN_CONTINUATION'; n+=check('ready-cannot-hide-uncertain-closure',d,False)
    d=base(); d['decisions'][0]['disposition']='PROCEED_UNCERTAIN'; d['decisions'][0]['uncertainty_declared']=True; d['obligations'][0]['closure']['disposition']='UNCERTAIN_CONTINUATION'; n+=check('material-cannot-proceed-uncertain',d,False)
    d=base(); d['decisions'][0]['consequence']='NON_MATERIAL'; d['decisions'][0]['disposition']='PROCEED_UNCERTAIN'; d['decisions'][0]['uncertainty_declared']=True; d['obligations'][0]['closure']['disposition']='UNCERTAIN_CONTINUATION'; n+=check('nonmaterial-may-proceed-uncertain',d,True)
    d=base(); d['retrieval_intents']=[]; d['obligations']=[]; d['scope_discoveries']=[]; d['attempts']=[]; n+=check('trigger-must-externalize-intent',d,False)
    d=base(); d['obligations']=[]; d['scope_discoveries']=[]; d['attempts']=[]; n+=check('intent-must-externalize-obligation',d,False)
    d=base(); d['retrieval_intents'].append(copy.deepcopy(d['retrieval_intents'][0])); d['retrieval_intents'][1]['intent_id']='i2'; n+=check('trigger-cannot-feed-two-intents',d,False)
    d=base(); sd=d['scope_discoveries'][0]; sd['outcome']='FAILED'; sd['selected_scope_refs']=[]; sd['coverage']='UNKNOWN'; d['attempts']=[]; d['obligations'][0]['closure']={'disposition':'ABSTAINED','basis_discovery_id':'sd','basis_attempt_ids':[]}; d['decisions'][0]['disposition']='ABSTAINED'; d['decisions'][0]['uncertainty_declared']=True; n+=check('failed-discovery-may-abstain',d,True)
    d=base(); sd=d['scope_discoveries'][0]; sd['outcome']='NO_RELEVANT_SCOPE'; sd['selected_scope_refs']=[]; sd['coverage']='DECLARED_DISCOVERY_COMPLETE'; d['attempts']=[]; d['obligations'][0]['closure']={'disposition':'NO_HIT_BOUNDED','basis_discovery_id':'sd','basis_attempt_ids':[]}; n+=check('complete-no-relevant-scope-can-close-bounded',d,True)
    d=base(); sd=d['scope_discoveries'][0]; sd['outcome']='NO_RELEVANT_SCOPE'; sd['selected_scope_refs']=[]; sd['coverage']='UNKNOWN'; d['attempts']=[]; d['obligations'][0]['closure']={'disposition':'NO_HIT_BOUNDED','basis_discovery_id':'sd','basis_attempt_ids':[]}; n+=check('unknown-scope-discovery-cannot-close-bounded',d,False)
    d=base(); d['attempts'][0]['outcome']='NO_HIT'; d['attempts'][0]['returned_record_ids']=[]; n+=check('retrieval-used-needs-hit',d,False)
    d=base(); d['attempts'][0]['returned_record_ids']=[]; n+=check('hit-needs-record',d,False)
    d=base(); d['attempts'][0]['outcome']='NO_HIT'; n+=check('nohit-cannot-return-records',d,False)
    d=base(); d['scope_discoveries'][0]['resolver_ref']='other'; n+=check('discovery-resolver-binding',d,False)
    print(f'RETRIEVAL_OBLIGATION_02_SELFTEST_PASS {n}')

if __name__=='__main__': run()
