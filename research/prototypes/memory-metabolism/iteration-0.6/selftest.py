#!/usr/bin/env python3
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
    e=mm.validate_document(d); assert bool(e) is (not valid), f"{name}: {e}"
def main():
    n=0
    expect("baseline",doc([ev(),cm()]),True); n+=1
    p=proj(); p["visible_record_ids"]=["cm-1"]; p["used_current_record_ids"]=["cm-1"]
    expect("simple_host",doc([ev(),cm()],projections=[p]),True); n+=1
    b=cm(); b["relations"]=[{"type":"DERIVED_FROM","target":"ev-1"}]; expect("no_duplicate_lineage",doc([ev(),b]),False); n+=1
    e=ev(); c=cm(); c["boundary_assertion"]={"disposition":"UNCHANGED"}
    p=proj("HOST_RESOLVED_REFERENCE"); p["visible_record_ids"]=["cm-1"]; p["used_current_record_ids"]=["cm-1"]; p["host_disclosure_resolutions"]=[mm.resolution_for_record(c,"disclose:1")]; p["host_boundary_resolutions"]=[mm.resolution_for_record(c,"UNCHANGED")]
    expect("subject_bound",doc([e,c],projections=[p]),True); n+=1
    changed=copy.deepcopy(c); changed["content"]="changed"; expect("stale_resolution",doc([e,changed],projections=[p]),False); n+=1
    c2=cm(); c2["boundary_assertion"]={"disposition":"CHANGED","external_resolution_ref":"release:7"}
    p2=proj("HOST_RESOLVED_REFERENCE"); p2["visible_record_ids"]=["cm-1"]; p2["used_current_record_ids"]=["cm-1"]; p2["host_disclosure_resolutions"]=[mm.resolution_for_record(c2,"d:2")]; p2["host_boundary_resolutions"]=[mm.resolution_for_record(c2,"wrong")]
    expect("wrong_resolution_ref",doc([e,c2],projections=[p2]),False); n+=1
    p2["host_boundary_resolutions"]=[mm.resolution_for_record(c2,"release:7")]; expect("right_resolution_ref",doc([e,c2],projections=[p2]),True); n+=1
    e1,e2=ev("e1","r1","PRESENT"),ev("e2","r2","TOMBSTONE"); c3=cm("cm-x","e1","r1"); c3.update({"derived_from":["e1","e2"],"evidence_refs":["e1","e2"],"source_roots":["r1","r2"],"support_mode":"MULTI_SOURCE_DEPENDENT","evidence_availability":"NONE_PRESENT"})
    expect("availability_mismatch",doc([e1,e2,c3]),False); n+=1
    c3["evidence_availability"]="SOME_PRESENT"; expect("availability_some",doc([e1,e2,c3]),True); n+=1
    prov={"provenance_id":"prov-1","source_roots":["r1"],"evidence_refs":["e1"]}; c4=cm("cm-p","e1","r1"); c4["provenance_ref"]="prov-1"; c4["boundary_assertion"]={"disposition":"UNCHANGED"}
    p3=proj("HOST_RESOLVED_REFERENCE"); p3["visible_record_ids"]=["cm-p"]; p3["used_current_record_ids"]=["cm-p"]; p3["inspected_provenance_ids"]=["prov-1"]; p3["host_disclosure_resolutions"]=[mm.resolution_for_record(c4,"d:p")]; p3["host_boundary_resolutions"]=[mm.resolution_for_record(c4,"UNCHANGED")]
    expect("prov_requires_resolution",doc([e1,c4],[prov],[p3]),False); n+=1
    p3["host_provenance_resolutions"]=[mm.resolution_for_provenance(prov,"audit:p")]; expect("prov_resolved",doc([e1,c4],[prov],[p3]),True); n+=1
    old={"record_id":"old","layer":"KNOWLEDGE","claim_type":"BELIEF","content":"old","source_roots":["s1"],"validity":{"mode":"CURRENT_STATE","revalidate_before_material_use":True}}; new=copy.deepcopy(old); new.update({"record_id":"new","content":"new","source_roots":["s2"],"supersedes":["old"]})
    p4=proj(); p4.update({"visible_record_ids":["old"],"used_current_record_ids":["old"],"revalidated_record_ids":["old"],"consequence":"MATERIAL"})
    expect("no_resurrection",doc([old,new],projections=[p4]),False); n+=1
    print(f"MEMORY_METABOLISM_ITERATION_06_SELFTEST_PASS {n}")
if __name__=="__main__": main()
