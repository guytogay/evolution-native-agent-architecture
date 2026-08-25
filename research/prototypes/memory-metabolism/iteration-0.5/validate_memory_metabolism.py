#!/usr/bin/env python3
"""Research validator for ENA Memory Metabolism iteration 0.5.

Checks represented structural consistency only. A PASS does NOT prove semantic truth,
source authenticity, real independence, real authority, sanitization safety, actor
entitlement authenticity, policy correctness, retrieval completeness, or behavioral
improvement.

Security boundary:
- content_access_ref is an opaque Host policy-boundary reference, not a universal
  RBAC/ABAC/IFC label.
- boundary-change claims in memory are not effective merely because they are written;
  a trusted Host projection input must resolve them for actor-visible disclosure.
- candidate retrieval is distinct from disclosure.
- provenance dereference has a separate access boundary.

Status: RESEARCH_PROTOTYPE / NOT_CURRENT_BASELINE / NOT_AUTHORITY
"""
from __future__ import annotations
import argparse, copy, json
from pathlib import Path
from typing import Any
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parent
SCHEMA_PATH=ROOT/'memory-set.schema.json'
EVIDENCE_LAYERS={'EVIDENCE','ARCHIVE'}
COGNITIVE_LAYERS={'KNOWLEDGE','COMPILED','IDENTITY'}
FORBIDDEN_EXECUTABLE_AUTHORITY_FIELDS={'executable_authority','permission_grant','capability_token','current_mandate'}

def load_json(path:Path)->dict[str,Any]: return json.loads(path.read_text(encoding='utf-8'))

def _indexes(doc):
    records,provenance,errors={},{},[]
    for i,r in enumerate(doc.get('records',[]) or []):
        rid=r.get('record_id')
        if not rid: errors.append(f'record[{i}] missing record_id')
        elif rid in records: errors.append(f'duplicate record_id {rid}')
        else: records[rid]=r
    for i,p in enumerate(doc.get('provenance_sets',[]) or []):
        pid=p.get('provenance_id')
        if not pid: errors.append(f'provenance_set[{i}] missing provenance_id')
        elif pid in provenance: errors.append(f'duplicate provenance_id {pid}')
        else: provenance[pid]=p
    return records,provenance,errors

def _effective_roots(record,provenance):
    roots=set(record.get('source_roots',[]) or [])
    pref=record.get('provenance_ref')
    if pref in provenance: roots.update(provenance[pref].get('source_roots',[]) or [])
    return roots

def _effective_evidence(record,provenance):
    refs=set(record.get('evidence_refs',[]) or [])
    pref=record.get('provenance_ref')
    if pref in provenance: refs.update(provenance[pref].get('evidence_refs',[]) or [])
    return refs

def _direct_lineage(record,provenance): return set(record.get('derived_from',[]) or [])|_effective_evidence(record,provenance)

def _reachable_evidence(record_id,records,provenance):
    found,seen=set(),set(); queue=list(_direct_lineage(records.get(record_id,{}),provenance))
    while queue:
        rid=queue.pop()
        if rid in seen: continue
        seen.add(rid); r=records.get(rid)
        if not r: continue
        if r.get('layer') in EVIDENCE_LAYERS: found.add(rid)
        queue.extend(_direct_lineage(r,provenance)-seen)
    return found

def _superseded_ids(records):
    out=set()
    for r in records.values():
        out.update(r.get('supersedes',[]) or [])
        for rel in r.get('relations',[]) or []:
            if rel.get('type')=='SUPERSEDES' and rel.get('target'): out.add(rel['target'])
    return out

def _has_explicit_contradiction(record,records,provenance):
    lineage=_direct_lineage(record,provenance)
    for sid in lineage:
        for rel in records.get(sid,{}).get('relations',[]) or []:
            if rel.get('type')=='CONTRADICTS' and rel.get('target') in lineage: return True
    return False

def _boundary_transition_needed(record,records,provenance):
    lineage=_direct_lineage(record,provenance)
    refs={records[s].get('content_access_ref') for s in lineage if s in records and records[s].get('content_access_ref')}
    target=record.get('content_access_ref')
    if not refs: return None,refs
    if len(refs)==1 and target in refs: return None,refs
    if len(refs)==1: return 'HOST_RESOLVED_CHANGE',refs
    return 'HOST_RESOLVED_COMPOSITION',refs

def validate_memory_set(doc):
    errors=[]; schema=load_json(SCHEMA_PATH)
    errors.extend(f'schema: {e.message}' for e in Draft202012Validator(schema).iter_errors(doc))
    records,provenance,idx=_indexes(doc); errors.extend(idx)
    for pid,p in provenance.items():
        cited_roots=set()
        for ref in p.get('evidence_refs',[]) or []:
            if ref not in records: errors.append(f'{pid}: evidence_refs references missing record {ref}')
            else: cited_roots.update(_effective_roots(records[ref],provenance))
        represented=set(p.get('source_roots',[]) or [])
        if cited_roots and not cited_roots.issubset(represented):
            errors.append(f'{pid}: provenance set lost roots from cited evidence {sorted(cited_roots-represented)}')
    for rid,r in records.items():
        pref=r.get('provenance_ref')
        if pref and pref not in provenance: errors.append(f'{rid}: provenance_ref references missing provenance set {pref}')
        for field in ('derived_from','evidence_refs','supersedes'):
            for ref in r.get(field,[]) or []:
                if ref not in records: errors.append(f'{rid}: {field} references missing record {ref}')
        for field in FORBIDDEN_EXECUTABLE_AUTHORITY_FIELDS:
            if field in r: errors.append(f'{rid}: memory record must not carry executable authority field {field}')
        layer=r.get('layer'); lineage=_direct_lineage(r,provenance); roots=_effective_roots(r,provenance)
        if layer in EVIDENCE_LAYERS and 'evidence_status' not in r: errors.append(f'{rid}: EVIDENCE/ARCHIVE requires explicit evidence_status')
        if layer=='EVIDENCE' and not roots: errors.append(f'{rid}: EVIDENCE requires represented source root')
        if lineage:
            inherited_roots=set()
            for ref in lineage: inherited_roots.update(_effective_roots(records.get(ref,{}),provenance))
            if inherited_roots and not inherited_roots.issubset(roots):
                errors.append(f'{rid}: transformation lost source provenance roots {sorted(inherited_roots-roots)}')
            needed,source_refs=_boundary_transition_needed(r,records,provenance); claim=r.get('boundary_transition_claim')
            if needed:
                if not claim:
                    errors.append(f'{rid}: information boundary changed/composed from {sorted(source_refs)} without represented Host-resolved transition claim')
                else:
                    if claim.get('mode')!=needed: errors.append(f"{rid}: boundary transition needs mode {needed}, got {claim.get('mode')}")
                    if claim.get('resolution_ref') in records: errors.append(f'{rid}: boundary transition resolution_ref must be external to memory records')
            elif claim:
                errors.append(f'{rid}: boundary transition claim adds governance where represented source/target boundary is unchanged')
        if layer=='COMPILED':
            if r.get('claim_type') in {'OCCURRENCE','TASK_STATE'}: errors.append(f"{rid}: COMPILED memory cannot be raw {r.get('claim_type')}")
            if not lineage and not r.get('provenance_ref'): errors.append(f'{rid}: COMPILED memory requires derivation/evidence lineage')
            operational=[ref for ref in r.get('derived_from',[]) or [] if records.get(ref,{}).get('layer')=='OPERATIONAL']
            if operational and not _effective_evidence(r,provenance): errors.append(f'{rid}: direct OPERATIONAL -> COMPILED requires evidence lineage')
            if r.get('decision_material') is True:
                reachable=_reachable_evidence(rid,records,provenance)
                if not reachable: errors.append(f'{rid}: decision-material COMPILED lineage must transitively reach EVIDENCE/ARCHIVE')
                availability=r.get('evidence_availability')
                if not availability: errors.append(f'{rid}: decision-material COMPILED requires evidence_availability')
                elif reachable:
                    statuses=[records[e].get('evidence_status') or 'UNKNOWN' for e in reachable]
                    if availability=='FULL' and any(s!='PRESENT' for s in statuses): errors.append(f'{rid}: FULL evidence_availability requires all reachable represented evidence PRESENT')
                    if availability=='UNAVAILABLE' and any(s=='PRESENT' for s in statuses): errors.append(f'{rid}: UNAVAILABLE evidence_availability conflicts with reachable PRESENT evidence')
            if r.get('support_mode')=='INDEPENDENT_CORROBORATION' and len(roots)<2: errors.append(f'{rid}: independent corroboration requires >=2 distinct represented source roots')
        if layer in COGNITIVE_LAYERS and lineage and _has_explicit_contradiction(r,records,provenance) and not str(r.get('conflict_handling','')).strip():
            errors.append(f'{rid}: contradictory lineage requires conflict_handling')
        if layer=='IDENTITY' and r.get('mutation') is True and not str(r.get('governance_ref','')).strip(): errors.append(f'{rid}: IDENTITY mutation requires governance_ref')
    return errors

def validate_projection(doc,p):
    errors=[]
    records={r['record_id']:r for r in doc.get('records',[]) or [] if r.get('record_id')}
    provenance={x['provenance_id']:x for x in doc.get('provenance_sets',[]) or [] if x.get('provenance_id')}
    pid=p.get('projection_id','?'); access=set(p.get('resolved_actor_access_refs',[]) or [])
    candidates=set(p.get('candidate_record_ids',[]) or []); disclosed=set(p.get('disclosed_record_ids',[]) or [])
    current=set(p.get('used_current_record_ids',[]) or []); historical=set(p.get('used_historical_record_ids',[]) or [])
    revalidated=set(p.get('revalidated_record_ids',[]) or []); inspected=set(p.get('inspected_provenance_ids',[]) or [])
    host_resolved=set(p.get('host_resolved_boundary_record_ids',[]) or [])
    overlap=current&historical
    if overlap: errors.append(f'projection {pid}: current and historical use must be disjoint {sorted(overlap)}')
    for rid in candidates|disclosed|current|historical|revalidated|host_resolved:
        if rid not in records: errors.append(f'projection {pid}: unknown record {rid}')
    for rid in disclosed:
        r=records.get(rid)
        if r and r.get('content_access_ref') not in access: errors.append(f'projection {pid}: actor lacks resolved access for disclosed record {rid}')
    for rid in current|historical:
        if rid not in disclosed: errors.append(f'projection {pid}: used record {rid} was not disclosed')
    for prov_id in inspected:
        prov=provenance.get(prov_id)
        if not prov: errors.append(f'projection {pid}: unknown provenance set {prov_id}')
        elif prov.get('content_access_ref') not in access: errors.append(f'projection {pid}: actor lacks resolved access for provenance {prov_id}')
    for rid in disclosed:
        r=records.get(rid,{})
        if r.get('boundary_transition_claim') and rid not in host_resolved: errors.append(f'projection {pid}: disclosed boundary-changed record {rid} lacks trusted Host resolution')
    superseded=_superseded_ids(records)
    for rid in current:
        if rid in superseded: errors.append(f'projection {pid}: superseded record {rid} cannot be used as current state')
    if p.get('consequence')=='MATERIAL':
        for rid in current:
            validity=records.get(rid,{}).get('validity',{}) or {}
            if validity.get('revalidate_before_material_use') is True and rid not in revalidated: errors.append(f'projection {pid}: material use of {rid} requires revalidation')
    if p.get('authority_required') is True:
        basis=p.get('external_authority_basis')
        if not basis: errors.append(f'projection {pid}: authority_required needs external_authority_basis')
        elif basis in records: errors.append(f'projection {pid}: memory record cannot serve as executable authority basis')
    return errors

def validate_document(doc):
    errors=validate_memory_set(doc)
    for p in doc.get('projections',[]) or []: errors.extend(validate_projection(doc,p))
    return errors

def evidence(rid='ev-1',root='trace:1',access='policy:internal',status='PRESENT'):
    return {'record_id':rid,'layer':'EVIDENCE','claim_type':'OCCURRENCE','content':'occurrence','source_roots':[root],'content_access_ref':access,'evidence_status':status,'validity':{'mode':'IMMUTABLE_OCCURRENCE','revalidate_before_material_use':False}}

def compiled(rid='cm-1',source='ev-1',root='trace:1',access='policy:internal'):
    return {'record_id':rid,'layer':'COMPILED','claim_type':'HEURISTIC','content':'heuristic','derived_from':[source],'evidence_refs':[source] if source.startswith('ev-') else [],'source_roots':[root],'support_mode':'SINGLE_SOURCE','decision_material':True,'evidence_availability':'FULL','content_access_ref':access,'validity':{'mode':'CONDITIONAL','revalidate_before_material_use':False}}

def document(records,provenance=None,projections=None): return {'schema_version':'memory-metabolism-research-0.5','provenance_sets':provenance or [],'records':records,'projections':projections or []}

def projection(): return {'projection_id':'p','resolved_actor_access_refs':['policy:internal'],'candidate_record_ids':[],'disclosed_record_ids':[],'used_current_record_ids':[],'used_historical_record_ids':[],'revalidated_record_ids':[],'inspected_provenance_ids':[],'host_resolved_boundary_record_ids':[],'consequence':'NON_MATERIAL','authority_required':False}

def expect(name,d,valid):
    errors=validate_document(d); assert bool(errors) is (not valid),f'{name}: expected valid={valid}, got {errors}'

def selftest():
    n=0
    expect('baseline',document([evidence(),compiled()]),True); n+=1
    p=projection(); p['candidate_record_ids']=['ev-secret']
    expect('candidate_not_disclosure',document([evidence('ev-secret',access='policy:secret')],projections=[p]),True); n+=1
    p2=copy.deepcopy(p); p2['disclosed_record_ids']=['ev-secret']
    expect('unauthorized_disclosure_blocked',document([evidence('ev-secret',access='policy:secret')],projections=[p2]),False); n+=1
    evs=evidence('ev-secret',access='policy:secret'); c=compiled('cm-public',source='ev-secret',access='policy:public'); c['derived_from']=[]
    expect('evidence_ref_boundary_bypass_closed',document([evs,c]),False); n+=1
    e2=evidence('ev-summary',root='trace:1',access='policy:public'); e2['derived_from']=['ev-secret']
    expect('noncognitive_boundary_bypass_closed',document([evs,e2]),False); n+=1
    c=compiled('cm-public',source='ev-secret',access='policy:public'); c['boundary_transition_claim']={'mode':'HOST_RESOLVED_CHANGE','resolution_ref':'policy-release:7'}
    expect('represented_boundary_claim_valid_memory',document([evs,c]),True); n+=1
    p=projection(); p['resolved_actor_access_refs']=['policy:public']; p['candidate_record_ids']=['cm-public']; p['disclosed_record_ids']=['cm-public']; p['used_current_record_ids']=['cm-public']
    expect('claim_alone_not_effective',document([evs,c],projections=[p]),False); n+=1
    p['host_resolved_boundary_record_ids']=['cm-public']; expect('host_resolved_boundary_effective',document([evs,c],projections=[p]),True); n+=1
    a=evidence('ev-a',root='a',access='policy:A'); b=evidence('ev-b',root='b',access='policy:B'); cm=compiled('cm-ab',source='ev-a',root='a',access='policy:aggregate')
    cm['derived_from']=['ev-a','ev-b']; cm['evidence_refs']=['ev-a','ev-b']; cm['source_roots']=['a','b']; cm['support_mode']='MULTI_SOURCE_DEPENDENT'
    expect('mixed_boundary_requires_composition_resolution',document([a,b,cm]),False); n+=1
    cm['boundary_transition_claim']={'mode':'HOST_RESOLVED_COMPOSITION','resolution_ref':'aggregate-policy:1'}; expect('mixed_boundary_claim_representable',document([a,b,cm]),True); n+=1
    prov={'provenance_id':'prov-secret','source_roots':['trace:1'],'evidence_refs':['ev-secret'],'content_access_ref':'policy:secret'}
    c2=copy.deepcopy(c); c2['source_roots']=[]; c2['evidence_refs']=[]; c2['provenance_ref']='prov-secret'
    p=projection(); p['resolved_actor_access_refs']=['policy:public']; p['candidate_record_ids']=['cm-public']; p['disclosed_record_ids']=['cm-public']; p['used_current_record_ids']=['cm-public']; p['host_resolved_boundary_record_ids']=['cm-public']
    expect('public_content_without_provenance_dereference',document([evs,c2],[prov],[p]),True); n+=1
    pb=copy.deepcopy(p); pb['inspected_provenance_ids']=['prov-secret']; expect('restricted_provenance_inspection_blocked',document([evs,c2],[prov],[pb]),False); n+=1
    pg=copy.deepcopy(pb); pg['resolved_actor_access_refs'].append('policy:secret'); expect('authorized_provenance_inspection',document([evs,c2],[prov],[pg]),True); n+=1
    e1=evidence('e1',root='r1',status='PRESENT'); er=evidence('e2',root='r2',status='LAWFULLY_REDACTED'); c3=compiled('cm-multi',source='e1',root='r1')
    c3['derived_from']=['e1','e2']; c3['evidence_refs']=['e1','e2']; c3['source_roots']=['r1','r2']; c3['support_mode']='MULTI_SOURCE_DEPENDENT'; c3['evidence_availability']='FULL'
    expect('full_not_if_partial_evidence_missing',document([e1,er,c3]),False); n+=1
    c3['evidence_availability']='DEGRADED'; expect('degraded_if_partial_evidence_missing',document([e1,er,c3]),True); n+=1
    ev0=evidence(); c1=compiled(); cc=compiled('cm-2',source='cm-1'); cc['evidence_refs']=[]; cc['source_roots']=['trace:1']; expect('second_order_compilation',document([ev0,c1,cc]),True); n+=1
    old={'record_id':'kb-old','layer':'KNOWLEDGE','claim_type':'BELIEF','content':'old','source_roots':['inv:t1'],'content_access_ref':'policy:internal','validity':{'mode':'CURRENT_STATE','revalidate_before_material_use':True}}
    new=copy.deepcopy(old); new.update({'record_id':'kb-new','content':'new','source_roots':['inv:t2'],'supersedes':['kb-old']})
    p=projection(); p['candidate_record_ids']=['kb-old']; p['disclosed_record_ids']=['kb-old']; p['used_current_record_ids']=['kb-old']; p['used_historical_record_ids']=['kb-old']
    expect('current_historical_overlap',document([old,new],projections=[p]),False); n+=1
    p['used_historical_record_ids']=[]; p['consequence']='MATERIAL'; p['revalidated_record_ids']=['kb-old']; expect('superseded_current_blocked',document([old,new],projections=[p]),False); n+=1
    p['used_current_record_ids']=[]; p['used_historical_record_ids']=['kb-old']; expect('authorized_historical_use',document([old,new],projections=[p]),True); n+=1
    ea=evidence('ea',root='a'); eb=evidence('eb',root='b'); ea['relations']=[{'type':'CONTRADICTS','target':'eb'}]
    kb={'record_id':'kb','layer':'KNOWLEDGE','claim_type':'BELIEF','content':'combined','derived_from':['ea','eb'],'source_roots':['a','b'],'content_access_ref':'policy:internal','validity':{'mode':'CONDITIONAL','revalidate_before_material_use':False}}
    expect('knowledge_contradiction_visible',document([ea,eb,kb]),False); n+=1
    print(f'MEMORY_METABOLISM_ITERATION_05_SELFTEST_PASS {n}')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('path',nargs='?'); ap.add_argument('--selftest',action='store_true'); args=ap.parse_args()
    if args.selftest: selftest(); return
    if not args.path: ap.error('path required unless --selftest')
    d=load_json(Path(args.path)); errors=validate_document(d)
    print(json.dumps({'valid':not errors,'scope':'represented Memory Metabolism iteration-0.5 structural consistency only','security_boundary':'Host-resolved access and boundary transitions are trusted inputs, not proven by this validator','errors':errors},indent=2))
    raise SystemExit(0 if not errors else 1)

if __name__=='__main__': main()
