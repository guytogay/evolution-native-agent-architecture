#!/usr/bin/env python3
"""Regression cases from independent formal/systems-boundary review of iteration 0.5.
Reviewed target: 6d1370cde1f119e813408dbca0dda77009ab1e30
"""
from __future__ import annotations
import copy, importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("mm06",ROOT/"validate_memory_metabolism.py")
mm=importlib.util.module_from_spec(spec); spec.loader.exec_module(mm)
def ev(rid="ev-1",root="trace:1",status="PRESENT"):
    return {"record_id":rid,"layer":"EVIDENCE","claim_type":"OCCURRENCE","content":"occurrence","source_roots":[root],"evidence_status":status,"validity":{"mode":"IMMUTABLE_OCCURRENCE","revalidate_before_material_use":False}}
def cm(rid="cm-1",source="ev-1",root="trace:1"):
    return {"record_id":rid,"layer":"COMPILED","claim_type":"HEURISTIC","content":"heuristic","derived_from":[source],"evidence_refs":[source] if source.startswith("ev-") else [],"source_roots":[root],"support_mode":"SINGLE_SOURCE","decision_material":True,"evidence_availability":"ALL_PRESENT","validity":{"mode":"CONDITIONAL","revalidate_before_material_use":False}}
def doc(records,provenance=None,projections=None): return {"schema_version":"memory-metabolism-research-0.6","provenance_sets":provenance or [],"records":records,"projections":projections or []}
def proj(mode="SINGLE_BOUNDARY_REFERENCE"):
    return {"projection_id":"p","security_mode":mode,"visible_record_ids":[],"used_current_record_ids":[],"used_historical_record_ids":[],"revalidated_record_ids":[],"inspected_provenance_ids":[],"host_disclosure_resolutions":[],"host_boundary_resolutions":[],"host_provenance_resolutions":[],"consequence":"NON_MATERIAL","authority_required":False}
def expect(name,d,valid):
    e=mm.validate_document(d); assert bool(e) is (not valid), f"{name}: expected {valid}, got {e}"
def main():
    n=0
    e=ev(); c=cm(); c["relations"]=[{"type":"DERIVED_FROM","target":"ev-1"}]
    expect("F1_relation_bypass",doc([e,c]),False); n+=1
    e=ev(); c=cm(); c["boundary_assertion"]={"disposition":"UNCHANGED"}
    p=proj("HOST_RESOLVED_REFERENCE"); p["visible_record_ids"]=["cm-1"]; p["used_current_record_ids"]=["cm-1"]; p["host_disclosure_resolutions"]=[mm.resolution_for_record(c,"d:1")]; p["host_boundary_resolutions"]=[mm.resolution_for_record(c,"UNCHANGED")]
    expect("F2_control",doc([e,c],projections=[p]),True); n+=1
    changed=copy.deepcopy(c); changed["content"]="changed artifact"
    expect("F2_modified_subject",doc([e,changed],projections=[p]),False); n+=1
    p0=proj(); p0["visible_record_ids"]=["cm-1"]; p0["used_current_record_ids"]=["cm-1"]
    expect("F3_F8_no_token_semantics",doc([ev(),cm()],projections=[p0]),True); n+=1
    badp=proj(); badp["candidate_record_ids"]=["ev-1"]
    expect("F4_candidates_outside_shared_projection",doc([ev()],projections=[badp]),False); n+=1
    e1=ev("e1","r1"); prov={"provenance_id":"prov-secret","source_roots":["r1"],"evidence_refs":["e1"]}
    c1=cm("cm-p","e1","r1"); c1["provenance_ref"]="prov-secret"; c1["boundary_assertion"]={"disposition":"UNCHANGED"}
    pp=proj("HOST_RESOLVED_REFERENCE"); pp["visible_record_ids"]=["cm-p"]; pp["used_current_record_ids"]=["cm-p"]; pp["inspected_provenance_ids"]=["prov-secret"]; pp["host_disclosure_resolutions"]=[mm.resolution_for_record(c1,"d:p")]; pp["host_boundary_resolutions"]=[mm.resolution_for_record(c1,"UNCHANGED")]
    expect("F5_unresolved_provenance",doc([e1,c1],[prov],[pp]),False); n+=1
    pp["host_provenance_resolutions"]=[mm.resolution_for_provenance(prov,"audit:p")]
    expect("F5_resolved_provenance",doc([e1,c1],[prov],[pp]),True); n+=1
    e1,e2=ev("e1","r1","TOMBSTONE"),ev("e2","r2","LAWFULLY_REDACTED")
    c2=cm("cm-e","e1","r1"); c2.update({"derived_from":["e1","e2"],"evidence_refs":["e1","e2"],"source_roots":["r1","r2"],"support_mode":"MULTI_SOURCE_DEPENDENT","evidence_availability":"SOME_PRESENT"})
    expect("F6_some_present_not_none",doc([e1,e2,c2]),False); n+=1
    c2["evidence_availability"]="NONE_PRESENT"; expect("F6_none_present",doc([e1,e2,c2]),True); n+=1
    expect("F7_simple_host",doc([ev(),cm()],projections=[p0]),True); n+=1
    print(f"MEMORY_METABOLISM_REVIEW3_REGRESSION_PASS {n}")
if __name__=="__main__": main()
