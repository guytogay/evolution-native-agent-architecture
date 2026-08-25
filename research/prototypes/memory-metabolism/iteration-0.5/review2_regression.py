#!/usr/bin/env python3
"""Regression cases distilled from the independent information-flow review of iteration 0.4."""
from validate_memory_metabolism import document,evidence,compiled,projection,expect
import copy

def main():
    n=0
    secret=evidence('secret',access='policy:secret')
    p=projection(); p['candidate_record_ids']=['secret']
    expect('A1_candidate_pre_disclosure',document([secret],projections=[p]),True); n+=1
    p['disclosed_record_ids']=['secret']
    expect('A1_unauthorized_disclosure',document([secret],projections=[p]),False); n+=1

    c=compiled('public-c','secret',access='policy:public'); c['derived_from']=[]
    expect('A2_evidence_ref_scope_bypass',document([secret,c]),False); n+=1

    e2=evidence('summary',access='policy:public'); e2['derived_from']=['secret']
    expect('A3_noncognitive_intermediary',document([secret,e2]),False); n+=1

    c=compiled('public-c','secret',access='policy:public')
    c['boundary_transition_claim']={'mode':'HOST_RESOLVED_CHANGE','resolution_ref':'release:7'}
    p=projection(); p['resolved_actor_access_refs']=['policy:public']; p['candidate_record_ids']=['public-c']; p['disclosed_record_ids']=['public-c']; p['used_current_record_ids']=['public-c']
    expect('A4_assertion_not_authority',document([secret,c],projections=[p]),False); n+=1
    p['host_resolved_boundary_record_ids']=['public-c']
    expect('A4_host_resolved',document([secret,c],projections=[p]),True); n+=1

    e1=evidence('e1',root='r1',status='PRESENT'); er=evidence('e2',root='r2',status='TOMBSTONE')
    c=compiled('multi','e1',root='r1'); c['derived_from']=['e1','e2']; c['evidence_refs']=['e1','e2']; c['source_roots']=['r1','r2']; c['support_mode']='MULTI_SOURCE_DEPENDENT'; c['evidence_availability']='FULL'
    expect('A5_full_overclaim',document([e1,er,c]),False); n+=1

    prov={'provenance_id':'prov','source_roots':['trace:1'],'evidence_refs':['secret'],'content_access_ref':'policy:secret'}
    c=compiled('pub','secret',root='trace:1',access='policy:public'); c['source_roots']=[]; c['evidence_refs']=[]; c['provenance_ref']='prov'; c['boundary_transition_claim']={'mode':'HOST_RESOLVED_CHANGE','resolution_ref':'release:8'}
    p=projection(); p['resolved_actor_access_refs']=['policy:public']; p['candidate_record_ids']=['pub']; p['disclosed_record_ids']=['pub']; p['used_current_record_ids']=['pub']; p['host_resolved_boundary_record_ids']=['pub']
    expect('A6_content_without_provenance',document([secret,c],[prov],[p]),True); n+=1
    p2=copy.deepcopy(p); p2['inspected_provenance_ids']=['prov']
    expect('A6_provenance_requires_separate_access',document([secret,c],[prov],[p2]),False); n+=1

    a=evidence('a',root='a',access='policy:A'); b=evidence('b',root='b',access='policy:B')
    c=compiled('agg','a',root='a',access='policy:aggregate'); c['derived_from']=['a','b']; c['evidence_refs']=['a','b']; c['source_roots']=['a','b']; c['support_mode']='MULTI_SOURCE_DEPENDENT'
    expect('B1_no_literal_union_without_resolution',document([a,b,c]),False); n+=1
    c['boundary_transition_claim']={'mode':'HOST_RESOLVED_COMPOSITION','resolution_ref':'aggregate:policy'}
    expect('B1_composition_representable',document([a,b,c]),True); n+=1

    print(f'MEMORY_METABOLISM_REVIEW2_REGRESSION_PASS {n}')

if __name__=='__main__': main()
