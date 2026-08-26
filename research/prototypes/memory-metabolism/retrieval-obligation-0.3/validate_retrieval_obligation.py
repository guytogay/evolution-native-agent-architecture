#!/usr/bin/env python3
"""Research validator for Triggered Retrieval Obligation 0.3.

0.3 falsification/reconciliation:
- closure must bind the latest represented scope discovery for an obligation;
- discovery/attempt sequence numbers are unique within their local lifecycle;
- a HIT is not by itself evidence that retrieval was sufficient;
- READY may rely only on NO_HIT_BOUNDED or externally resolved retrieval sufficiency.

PASS proves represented lifecycle consistency only. It does not prove trigger recall,
scope-discovery adequacy, registry freshness, resolver recall, or semantic sufficiency.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parent
SCHEMA=ROOT/'retrieval-obligation.schema.json'

def load(p): return json.loads(Path(p).read_text(encoding='utf-8'))

def index(items,key,errors,label):
    out={}
    for i,x in enumerate(items or []):
        k=x.get(key)
        if not k: errors.append(f'{label}[{i}] missing {key}')
        elif k in out: errors.append(f'duplicate {key} {k}')
        else: out[k]=x
    return out

def validate_document(doc):
    errors=[]
    schema=load(SCHEMA)
    errors += [f'schema: {e.message}' for e in Draft202012Validator(schema).iter_errors(doc)]
    decisions=index(doc.get('decisions'),'decision_id',errors,'decision')
    triggers=index(doc.get('trigger_events'),'trigger_id',errors,'trigger')
    intents=index(doc.get('retrieval_intents'),'intent_id',errors,'intent')
    obligations=index(doc.get('obligations'),'obligation_id',errors,'obligation')
    discoveries=index(doc.get('scope_discoveries'),'discovery_id',errors,'discovery')
    attempts=index(doc.get('attempts'),'attempt_id',errors,'attempt')
    trigger_owners={k:[] for k in triggers}; intent_owners={k:[] for k in intents}
    for tid,t in triggers.items():
        if t.get('decision_id') not in decisions: errors.append(f'{tid}: unknown decision')
    for iid,i in intents.items():
        did=i.get('decision_id'); resolver=i.get('resolver_ref')
        if did not in decisions: errors.append(f'{iid}: unknown decision')
        for tid in i.get('trigger_ids',[]) or []:
            t=triggers.get(tid)
            if not t: errors.append(f'{iid}: unknown trigger {tid}'); continue
            trigger_owners.setdefault(tid,[]).append(iid)
            if t.get('decision_id')!=did: errors.append(f'{iid}: trigger {tid} decision mismatch')
            if t.get('resolver_ref')!=resolver: errors.append(f'{iid}: trigger {tid} resolver mismatch')
    for tid,owners in trigger_owners.items():
        if len(owners)!=1: errors.append(f'{tid}: represented trigger must externalize through exactly one retrieval intent; owners={owners}')
    for oid,o in obligations.items():
        iid=o.get('intent_id'); intent=intents.get(iid)
        if not intent: errors.append(f'{oid}: unknown intent {iid}')
        else:
            intent_owners.setdefault(iid,[]).append(oid)
            if o.get('decision_id')!=intent.get('decision_id'): errors.append(f'{oid}: decision mismatch with intent')
            if o.get('resolver_ref')!=intent.get('resolver_ref'): errors.append(f'{oid}: resolver mismatch with intent')
        if o.get('state')=='CLOSED' and not o.get('closure'): errors.append(f'{oid}: CLOSED requires closure')
        if o.get('state')!='CLOSED' and o.get('closure'): errors.append(f'{oid}: non-CLOSED must not carry closure')
    for iid,owners in intent_owners.items():
        if len(owners)!=1: errors.append(f'{iid}: retrieval intent must externalize exactly one obligation; owners={owners}')
    discoveries_by_obligation={k:[] for k in obligations}; discovery_sequences={k:{} for k in obligations}
    for did,d in discoveries.items():
        oid=d.get('obligation_id'); o=obligations.get(oid)
        if not o: errors.append(f'{did}: unknown obligation {oid}'); continue
        discoveries_by_obligation.setdefault(oid,[]).append(did)
        seq=d.get('sequence'); seqmap=discovery_sequences.setdefault(oid,{})
        if seq in seqmap: errors.append(f'{oid}: duplicate discovery sequence {seq} for {seqmap[seq]} and {did}')
        else: seqmap[seq]=did
        if d.get('resolver_ref')!=o.get('resolver_ref'): errors.append(f'{did}: resolver mismatch with obligation')
        scopes=d.get('selected_scope_refs',[]) or []; outcome=d.get('outcome')
        if outcome=='SCOPES_SELECTED' and not scopes: errors.append(f'{did}: SCOPES_SELECTED requires >=1 selected scope')
        if outcome in {'NO_RELEVANT_SCOPE','FAILED','UNKNOWN'} and scopes: errors.append(f'{did}: {outcome} must not claim selected scopes')
    attempts_by_obligation={k:[] for k in obligations}; attempts_by_discovery={k:[] for k in discoveries}; attempt_sequences={k:{} for k in discoveries}
    for aid,a in attempts.items():
        oid=a.get('obligation_id'); o=obligations.get(oid); d=discoveries.get(a.get('discovery_id'))
        if not o: errors.append(f'{aid}: unknown obligation {oid}'); continue
        attempts_by_obligation.setdefault(oid,[]).append(aid)
        if not d: errors.append(f'{aid}: unknown discovery {a.get("discovery_id")}'); continue
        attempts_by_discovery.setdefault(d.get('discovery_id'),[]).append(aid)
        seq=a.get('sequence'); seqmap=attempt_sequences.setdefault(d.get('discovery_id'),{})
        if seq in seqmap: errors.append(f'{d.get("discovery_id")}: duplicate attempt sequence {seq} for {seqmap[seq]} and {aid}')
        else: seqmap[seq]=aid
        if d.get('obligation_id')!=oid: errors.append(f'{aid}: discovery belongs to another obligation')
        if a.get('resolver_ref')!=o.get('resolver_ref') or a.get('resolver_ref')!=d.get('resolver_ref'): errors.append(f'{aid}: resolver mismatch')
        if d.get('outcome')!='SCOPES_SELECTED': errors.append(f'{aid}: attempts require SCOPES_SELECTED discovery')
        if a.get('scope_ref') not in (d.get('selected_scope_refs',[]) or []): errors.append(f'{aid}: scope not selected by discovery')
        outcome=a.get('outcome'); returned=a.get('returned_record_ids',[]) or []
        if outcome=='HIT' and not returned: errors.append(f'{aid}: HIT requires returned records')
        if outcome=='NO_HIT' and returned: errors.append(f'{aid}: NO_HIT cannot return records')
    satisfying={'RETRIEVAL_SUFFICIENCY_RESOLVED','NO_HIT_BOUNDED'}
    for oid,o in obligations.items():
        state=o.get('state')
        if state=='PENDING' and (discoveries_by_obligation.get(oid) or attempts_by_obligation.get(oid)): errors.append(f'{oid}: PENDING cannot already have discovery/attempt activity')
        if state=='ATTEMPTED' and not discoveries_by_obligation.get(oid): errors.append(f'{oid}: ATTEMPTED requires at least one scope discovery')
        if state!='CLOSED': continue
        c=o.get('closure') or {}; cd=discoveries.get(c.get('basis_discovery_id'))
        if not cd or cd.get('obligation_id')!=oid: errors.append(f'{oid}: closure basis_discovery_id must reference this obligation'); continue
        seqs=[discoveries[x].get('sequence') for x in discoveries_by_obligation.get(oid,[]) if x in discoveries]
        if seqs and cd.get('sequence')!=max(seqs): errors.append(f'{oid}: closure must bind latest represented discovery sequence {max(seqs)}, got {cd.get("sequence")}')
        basis_attempt_ids=c.get('basis_attempt_ids',[]) or []; basis_attempts=[]
        for aid in basis_attempt_ids:
            a=attempts.get(aid)
            if not a or a.get('obligation_id')!=oid: errors.append(f'{oid}: closure basis attempt {aid} invalid'); continue
            if a.get('discovery_id')!=cd.get('discovery_id'): errors.append(f'{oid}: closure attempt {aid} is from another scope discovery')
            basis_attempts.append(a)
        disp=c.get('disposition')
        if disp=='RETRIEVAL_SUFFICIENCY_RESOLVED':
            if not c.get('sufficiency_resolution_ref'): errors.append(f'{oid}: RETRIEVAL_SUFFICIENCY_RESOLVED requires external sufficiency_resolution_ref')
            if not any(a.get('outcome')=='HIT' and a.get('returned_record_ids') for a in basis_attempts): errors.append(f'{oid}: RETRIEVAL_SUFFICIENCY_RESOLVED requires a HIT basis attempt')
        elif c.get('sufficiency_resolution_ref'):
            errors.append(f'{oid}: sufficiency_resolution_ref is only valid for RETRIEVAL_SUFFICIENCY_RESOLVED')
        if disp=='NO_HIT_BOUNDED':
            if cd.get('coverage')!='DECLARED_DISCOVERY_COMPLETE': errors.append(f'{oid}: NO_HIT_BOUNDED requires declared-complete scope discovery')
            if cd.get('outcome')=='NO_RELEVANT_SCOPE':
                if basis_attempts: errors.append(f'{oid}: NO_RELEVANT_SCOPE closure should not cite retrieval attempts')
            elif cd.get('outcome')=='SCOPES_SELECTED':
                selected=set(cd.get('selected_scope_refs',[]) or []); all_discovery_attempts=[attempts[x] for x in attempts_by_discovery.get(cd.get('discovery_id'),[]) if x in attempts]
                if any(a.get('outcome')=='HIT' for a in all_discovery_attempts): errors.append(f'{oid}: NO_HIT_BOUNDED cannot ignore HIT from basis discovery')
                covered={a.get('scope_ref') for a in basis_attempts if a.get('outcome')=='NO_HIT' and a.get('coverage')=='DECLARED_SCOPE_COMPLETE'}
                if covered!=selected: errors.append(f'{oid}: NO_HIT_BOUNDED must cover every selected scope with complete NO_HIT; missing={sorted(selected-covered)} extra={sorted(covered-selected)}')
                if set(basis_attempt_ids)!=set(attempts_by_discovery.get(cd.get('discovery_id'),[]) or []): errors.append(f'{oid}: NO_HIT_BOUNDED must account for all represented attempts from basis discovery')
            else: errors.append(f'{oid}: NO_HIT_BOUNDED requires SCOPES_SELECTED or NO_RELEVANT_SCOPE discovery')
    obligations_by_decision={k:[] for k in decisions}
    for o in obligations.values(): obligations_by_decision.setdefault(o.get('decision_id'),[]).append(o)
    for did,d in decisions.items():
        obs=obligations_by_decision.get(did,[]); unresolved=[o for o in obs if o.get('state')!='CLOSED']; nonsatisfying=[o for o in obs if o.get('state')=='CLOSED' and (o.get('closure') or {}).get('disposition') not in satisfying]; disp=d.get('disposition')
        if disp=='READY' and (unresolved or nonsatisfying): errors.append(f'{did}: READY requires every represented retrieval obligation closed by bounded-no-hit or externally resolved sufficiency')
        if disp=='PROCEED_UNCERTAIN':
            if d.get('uncertainty_declared') is not True: errors.append(f'{did}: PROCEED_UNCERTAIN requires uncertainty_declared=true')
            if d.get('consequence')=='MATERIAL': errors.append(f'{did}: MATERIAL decision cannot PROCEED_UNCERTAIN; narrow or abstain')
        if disp in {'NARROWED','ABSTAINED'} and d.get('uncertainty_declared') is not True: errors.append(f'{did}: {disp} requires uncertainty_declared=true')
    return errors

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('path'); a=ap.parse_args(); doc=load(a.path); e=validate_document(doc)
    print(json.dumps({'valid':not e,'scope':'retrieval-obligation-0.3 represented lifecycle; trigger recall, registry freshness, scope discovery adequacy, and semantic sufficiency remain external/behavioral','errors':e},indent=2))
    raise SystemExit(0 if not e else 1)

if __name__=='__main__': main()
