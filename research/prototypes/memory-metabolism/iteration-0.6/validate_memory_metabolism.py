#!/usr/bin/env python3
"""ENA Memory Metabolism iteration 0.6 research validator.
PASS = represented structural consistency only.
Security objects are optional reference encoding, not universal ENA semantics.
Status: RESEARCH_PROTOTYPE / NOT_CURRENT_BASELINE / NOT_AUTHORITY / SECURITY_REVIEW_STOP
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parent
SCHEMA=ROOT/"memory-set.schema.json"
EVIDENCE={"EVIDENCE","ARCHIVE"}
COGNITIVE={"KNOWLEDGE","COMPILED","IDENTITY"}

def load(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def _idx(doc):
    rs,ps,err={},{},[]
    for i,r in enumerate(doc.get("records",[]) or []):
        k=r.get("record_id")
        if not k: err.append(f"record[{i}] missing record_id")
        elif k in rs: err.append(f"duplicate record_id {k}")
        else: rs[k]=r
    for i,p in enumerate(doc.get("provenance_sets",[]) or []):
        k=p.get("provenance_id")
        if not k: err.append(f"provenance_set[{i}] missing provenance_id")
        elif k in ps: err.append(f"duplicate provenance_id {k}")
        else: ps[k]=p
    return rs,ps,err
def roots(r,ps):
    x=set(r.get("source_roots",[]) or []); q=r.get("provenance_ref")
    if q in ps: x.update(ps[q].get("source_roots",[]) or [])
    return x
def evidence_refs(r,ps):
    x=set(r.get("evidence_refs",[]) or []); q=r.get("provenance_ref")
    if q in ps: x.update(ps[q].get("evidence_refs",[]) or [])
    return x
def lineage(r,ps): return set(r.get("derived_from",[]) or [])|evidence_refs(r,ps)
def reachable_evidence(rid,rs,ps):
    out,seen=set(),set(); q=list(lineage(rs.get(rid,{}),ps))
    while q:
        x=q.pop()
        if x in seen: continue
        seen.add(x); r=rs.get(x)
        if not r: continue
        if r.get("layer") in EVIDENCE: out.add(x)
        q.extend(lineage(r,ps)-seen)
    return out
def superseded(rs):
    out=set()
    for r in rs.values(): out.update(r.get("supersedes",[]) or [])
    return out
def contradicts(r,rs,ps):
    ln=lineage(r,ps)
    return any(rel.get("type")=="CONTRADICTS" and rel.get("target") in ln
               for x in ln for rel in (rs.get(x,{}).get("relations",[]) or []))
def canon(x):
    if isinstance(x,dict): return {k:canon(v) for k,v in sorted(x.items()) if k!="notes"}
    if isinstance(x,list): return [canon(v) for v in x]
    return x
def fp(x): return hashlib.sha256(json.dumps(canon(x),sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def rec_fp(r): return fp(r)
def prov_fp(p): return fp(p)
def rmap(items,key):
    out={}
    for x in items or []:
        if x.get(key): out.setdefault(x[key],[]).append(x)
    return out
def rec_resolved(m,rid,r,ref=None):
    f=rec_fp(r)
    return any(x.get("subject_fingerprint")==f and (ref is None or x.get("resolution_ref")==ref) for x in m.get(rid,[]))
def prov_resolved(m,pid,p):
    f=prov_fp(p)
    return any(x.get("subject_fingerprint")==f for x in m.get(pid,[]))

def validate_memory(doc):
    err=[]; schema=load(SCHEMA)
    err += [f"schema: {e.message}" for e in Draft202012Validator(schema).iter_errors(doc)]
    rs,ps,e=_idx(doc); err+=e
    for pid,p in ps.items():
        cited=set()
        for ref in p.get("evidence_refs",[]) or []:
            if ref not in rs: err.append(f"{pid}: missing evidence {ref}")
            else: cited.update(roots(rs[ref],ps))
        if cited and not cited.issubset(set(p.get("source_roots",[]) or [])):
            err.append(f"{pid}: provenance lost cited roots")
    for rid,r in rs.items():
        if r.get("provenance_ref") and r["provenance_ref"] not in ps: err.append(f"{rid}: missing provenance_ref")
        for f in ("derived_from","evidence_refs","supersedes"):
            for ref in r.get(f,[]) or []:
                if ref not in rs: err.append(f"{rid}: {f} missing {ref}")
        for rel in r.get("relations",[]) or []:
            if rel.get("target") not in rs: err.append(f"{rid}: relation target missing")
        ln=lineage(r,ps); rr=roots(r,ps); layer=r.get("layer")
        if layer in EVIDENCE and "evidence_status" not in r: err.append(f"{rid}: evidence_status required")
        if layer=="EVIDENCE" and not rr: err.append(f"{rid}: evidence root required")
        if ln:
            inherited=set()
            for x in ln: inherited.update(roots(rs.get(x,{}),ps))
            if inherited and not inherited.issubset(rr): err.append(f"{rid}: transformation lost source roots")
        a=r.get("boundary_assertion")
        if a:
            d=a.get("disposition"); x=a.get("external_resolution_ref")
            if d in {"CHANGED","COMPOSED"} and not x: err.append(f"{rid}: boundary change needs external_resolution_ref")
            if d=="UNCHANGED" and x: err.append(f"{rid}: UNCHANGED should not carry external_resolution_ref")
        if layer=="COMPILED":
            if r.get("claim_type") in {"OCCURRENCE","TASK_STATE"}: err.append(f"{rid}: raw state cannot be COMPILED")
            if not ln and not r.get("provenance_ref"): err.append(f"{rid}: compiled lineage required")
            if r.get("decision_material") is True:
                re=reachable_evidence(rid,rs,ps)
                if not re: err.append(f"{rid}: decision-material lineage must reach evidence")
                av=r.get("evidence_availability")
                if not av: err.append(f"{rid}: evidence_availability required")
                elif re and av!="UNKNOWN":
                    n=sum(rs[x].get("evidence_status")=="PRESENT" for x in re)
                    expected="ALL_PRESENT" if n==len(re) else ("NONE_PRESENT" if n==0 else "SOME_PRESENT")
                    if av!=expected: err.append(f"{rid}: evidence_availability conflicts with {expected}")
            if r.get("support_mode")=="INDEPENDENT_CORROBORATION" and len(rr)<2: err.append(f"{rid}: independent roots >=2 required")
        if layer in COGNITIVE and ln and contradicts(r,rs,ps) and not str(r.get("conflict_handling","")).strip():
            err.append(f"{rid}: contradiction requires conflict_handling")
        if layer=="IDENTITY" and r.get("mutation") is True and not str(r.get("governance_ref","")).strip():
            err.append(f"{rid}: identity mutation requires governance_ref")
    return err

def validate_projection(doc,p):
    err=[]; rs={r["record_id"]:r for r in doc.get("records",[]) or [] if r.get("record_id")}
    ps={x["provenance_id"]:x for x in doc.get("provenance_sets",[]) or [] if x.get("provenance_id")}
    pid=p.get("projection_id","?"); vis=set(p.get("visible_record_ids",[]) or [])
    cur=set(p.get("used_current_record_ids",[]) or []); hist=set(p.get("used_historical_record_ids",[]) or [])
    rev=set(p.get("revalidated_record_ids",[]) or []); insp=set(p.get("inspected_provenance_ids",[]) or [])
    if cur&hist: err.append(f"projection {pid}: current/historical overlap")
    for x in vis|cur|hist|rev:
        if x not in rs: err.append(f"projection {pid}: unknown record {x}")
    for x in insp:
        if x not in ps: err.append(f"projection {pid}: unknown provenance {x}")
    for x in cur|hist:
        if x not in vis: err.append(f"projection {pid}: used {x} not actor-visible")
    mode=p.get("security_mode")
    dr=rmap(p.get("host_disclosure_resolutions",[]),"record_id")
    br=rmap(p.get("host_boundary_resolutions",[]),"record_id")
    pr=rmap(p.get("host_provenance_resolutions",[]),"provenance_id")
    if mode=="SINGLE_BOUNDARY_REFERENCE":
        if any((p.get("host_disclosure_resolutions"),p.get("host_boundary_resolutions"),p.get("host_provenance_resolutions"))):
            err.append(f"projection {pid}: simple Host should not need security-resolution ceremony")
    elif mode=="HOST_RESOLVED_REFERENCE":
        for rid in vis:
            r=rs.get(rid)
            if r and not rec_resolved(dr,rid,r): err.append(f"projection {pid}: {rid} lacks subject-bound disclosure resolution")
            if r and lineage(r,ps):
                a=r.get("boundary_assertion")
                if not a: err.append(f"projection {pid}: {rid} lacks boundary disposition")
                elif not rec_resolved(br,rid,r,a.get("external_resolution_ref") or "UNCHANGED"):
                    err.append(f"projection {pid}: {rid} lacks subject-bound boundary resolution")
        for x in insp:
            if x in ps and not prov_resolved(pr,x,ps[x]): err.append(f"projection {pid}: provenance {x} lacks subject-bound resolution")
    sup=superseded(rs)
    for x in cur:
        if x in sup: err.append(f"projection {pid}: superseded {x} cannot be current")
        if p.get("consequence")=="MATERIAL" and rs.get(x,{}).get("validity",{}).get("revalidate_before_material_use") is True and x not in rev:
            err.append(f"projection {pid}: material use of {x} requires revalidation")
    if p.get("authority_required") is True:
        b=p.get("external_authority_basis")
        if not b: err.append(f"projection {pid}: external authority basis required")
        elif b in rs: err.append(f"projection {pid}: memory cannot be executable authority")
    return err

def validate_document(doc):
    e=validate_memory(doc)
    for p in doc.get("projections",[]) or []: e+=validate_projection(doc,p)
    return e

def resolution_for_record(r,ref): return {"record_id":r["record_id"],"subject_fingerprint":rec_fp(r),"resolution_ref":ref}
def resolution_for_provenance(p,ref): return {"provenance_id":p["provenance_id"],"subject_fingerprint":prov_fp(p),"resolution_ref":ref}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("path"); a=ap.parse_args()
    d=load(a.path); e=validate_document(d)
    print(json.dumps({"valid":not e,"scope":"iteration-0.6 represented consistency; security encoding is optional reference organ","errors":e},indent=2))
    raise SystemExit(0 if not e else 1)
if __name__=="__main__": main()
