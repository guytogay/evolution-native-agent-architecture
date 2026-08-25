#!/usr/bin/env python3
from validate_routing import validate_runtime, route_stage

def req():
    return {"request_id":"rq1","decision_id":"d1","obligation_id":"o1","resolver_ref":"memory-resolver","decision_context_ref":"ctx1","retrieval_purpose":"recover decision-material durable context","material_dimensions":["DECISION_CORRECTNESS"]}

def attempt():
    return {"attempt_id":"a1","request_id":"rq1","searched_scope_refs":["scope:recovery"],"coverage":"DECLARED_ROUTE_COMPLETE","result":"HIT","returned_record_ids":["m1"]}

def doc(a=None):
    return {"schema_version":"resolver-routing-research-0.1","requests":[req()],"attempts":[a or attempt()]}

def expect(name,d,valid):
    e=validate_runtime(d)
    assert (not e)==valid, f"{name}: {e}"

def main():
    n=0
    expect("valid hit",doc(),True); n+=1
    a=attempt(); a["searched_scope_refs"]=[]; expect("hit without scope",doc(a),False); n+=1
    a=attempt(); a["returned_record_ids"]=[]; expect("hit without records",doc(a),False); n+=1
    a=attempt(); a["result"]="NO_HIT"; a["returned_record_ids"]=[]; expect("bounded no hit",doc(a),True); n+=1
    a=attempt(); a["result"]="NO_HIT"; a["returned_record_ids"]=[]; a["searched_scope_refs"]=[]; expect("no hit without scope",doc(a),False); n+=1
    a=attempt(); a["result"]="FAILED"; a["returned_record_ids"]=[]; a["coverage"]="UNKNOWN"; a["searched_scope_refs"]=[]; expect("failed unknown route",doc(a),True); n+=1
    a=attempt(); a["result"]="FAILED"; a["returned_record_ids"]=[]; a["coverage"]="DECLARED_ROUTE_COMPLETE"; expect("failed complete contradiction",doc(a),False); n+=1
    a=attempt(); a["request_id"]="missing"; expect("unknown request",doc(a),False); n+=1
    assert route_stage([["scope:recovery"]],["scope:recovery"])=="ROUTING_SUCCESS"; n+=1
    assert route_stage([["scope:recovery"]],["scope:other"])=="QUERY_SCOPE_MISS"; n+=1
    assert route_stage([["scope:a","scope:b"]],["scope:b"])=="ROUTING_SUCCESS"; n+=1
    assert route_stage([["scope:a"],["scope:b"]],["scope:a"])=="QUERY_SCOPE_MISS"; n+=1
    assert route_stage([["scope:a"]],[],attempted=False)=="ROUTING_NOT_ATTEMPTED"; n+=1
    assert route_stage([["scope:a"]],["scope:a"],coverage="UNKNOWN")=="QUERY_SCOPE_UNKNOWN"; n+=1
    a=attempt(); a["searched_scope_refs"]=["scope:wrong"]; a["result"]="NO_HIT"; a["returned_record_ids"]=[]
    expect("wrong route structurally honest",doc(a),True); n+=1
    print(f"RESOLVER_ROUTING_01_SELFTEST_PASS {n}")

if __name__=="__main__": main()
