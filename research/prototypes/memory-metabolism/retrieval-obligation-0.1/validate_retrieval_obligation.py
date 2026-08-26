#!/usr/bin/env python3
"""Research validator for Triggered Retrieval Obligation 0.1.

PASS means represented lifecycle consistency only. It does NOT prove that the
retrieval reflex fired when it should, that the resolver searched the right world,
that DECLARED_SCOPE_COMPLETE is externally true, or that returned memory was
semantically relevant.

Crucial boundary: runtime validation begins AFTER a retrieval trigger exists.
Trigger recall/false-negative detection belongs to the separate evaluation plane.

Status: RESEARCH_PROTOTYPE / NOT_CURRENT_BASELINE / NOT_AUTHORITY
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parent
SCHEMA=ROOT/'retrieval-obligation.schema.json'
EVAL_SCHEMA=ROOT/'retrieval-evaluation.schema.json'


def load(path): return json.loads(Path(path).read_text(encoding='utf-8'))

def _unique(items,key,kind):
    out,errs={},[]
    for i,x in enumerate(items or []):
        k=x.get(key)
        if not k: errs.append(f'{kind}[{i}] missing {key}')
        elif k in out: errs.append(f'duplicate {kind} {k}')
        else: out[k]=x
    return out,errs

def validate_runtime(doc):
    err=[f'schema: {e.message}' for e in Draft202012Validator(load(SCHEMA)).iter_errors(doc)]
    decisions,e=_unique(doc.get('decisions',[]),'decision_id','decision'); err+=e
    triggers,e=_unique(doc.get('trigger_events',[]),'trigger_id','trigger'); err+=e
    obligations,e=_unique(doc.get('obligations',[]),'obligation_id','obligation'); err+=e
    attempts,e=_unique(doc.get('attempts',[]),'attempt_id','attempt'); err+=e

    obligation_for_trigger={}; obs_by_dec={did:[] for did in decisions}; attempts_by_ob={oid:[] for oid in obligations}
    for tid,t in triggers.items():
        if t.get('decision_id') not in decisions: err.append(f'{tid}: unknown decision {t.get("decision_id")}')

    for oid,o in obligations.items():
        did=o.get('decision_id')
        if did not in decisions: err.append(f'{oid}: unknown decision {did}')
        else: obs_by_dec.setdefault(did,[]).append(o)
        for tid in o.get('trigger_ids',[]) or []:
            t=triggers.get(tid)
            if not t: err.append(f'{oid}: unknown trigger {tid}'); continue
            if t.get('decision_id')!=did: err.append(f'{oid}: trigger {tid} belongs to another decision')
            if t.get('resolver_ref')!=o.get('resolver_ref'): err.append(f'{oid}: trigger {tid} resolver mismatch')
            if tid in obligation_for_trigger: err.append(f'trigger {tid}: covered by multiple obligations')
            obligation_for_trigger[tid]=oid
        state=o.get('state'); closure=o.get('closure')
        if state=='CLOSED' and not closure: err.append(f'{oid}: CLOSED requires closure')
        if state!='CLOSED' and closure: err.append(f'{oid}: non-CLOSED must not carry closure')

    seq_seen={}
    for aid,a in attempts.items():
        oid=a.get('obligation_id'); o=obligations.get(oid)
        if not o: err.append(f'{aid}: unknown obligation {oid}'); continue
        attempts_by_ob.setdefault(oid,[]).append(a)
        if a.get('resolver_ref')!=o.get('resolver_ref'): err.append(f'{aid}: resolver mismatch with obligation {oid}')
        if a.get('query_scope_ref')!=o.get('query_scope_ref'): err.append(f'{aid}: query scope mismatch with obligation {oid}')
        pair=(oid,a.get('sequence'))
        if pair in seq_seen: err.append(f'{aid}: duplicate attempt sequence {pair[1]} for obligation {oid}')
        seq_seen[pair]=aid
        out=a.get('outcome'); returned=a.get('returned_record_ids',[]) or []
        if out=='HIT' and not returned: err.append(f'{aid}: HIT requires returned_record_ids')
        if out=='NO_HIT' and returned: err.append(f'{aid}: NO_HIT must not return records')
        if out=='FAILED' and a.get('coverage')=='DECLARED_SCOPE_COMPLETE': err.append(f'{aid}: FAILED cannot claim complete coverage')

    for tid in triggers:
        if tid not in obligation_for_trigger: err.append(f'{tid}: trigger did not externalize a retrieval obligation')

    for oid,o in obligations.items():
        state=o.get('state'); aa=attempts_by_ob.get(oid,[])
        if state=='PENDING' and aa: err.append(f'{oid}: PENDING must not already have attempts')
        if state in {'ATTEMPTED','CLOSED'} and not aa: err.append(f'{oid}: state {state} requires at least one attempt')
        if state=='CLOSED':
            c=o.get('closure',{}); basis=attempts.get(c.get('basis_attempt_id'))
            if not basis or basis.get('obligation_id')!=oid:
                err.append(f'{oid}: closure basis_attempt_id must reference an attempt for this obligation')
                continue
            disp=c.get('disposition')
            if disp=='RETRIEVAL_USED' and basis.get('outcome')!='HIT':
                err.append(f'{oid}: RETRIEVAL_USED requires HIT basis attempt')
            if disp=='NO_HIT_BOUNDED' and not (basis.get('outcome')=='NO_HIT' and basis.get('coverage')=='DECLARED_SCOPE_COMPLETE'):
                err.append(f'{oid}: NO_HIT_BOUNDED requires NO_HIT + declared-scope-complete basis attempt')
            if disp in {'UNCERTAIN_CONTINUATION','CONSEQUENCE_NARROWED','ABSTAINED'} and basis.get('outcome') not in {'PARTIAL','FAILED','UNKNOWN','NO_HIT','HIT'}:
                err.append(f'{oid}: closure basis attempt has invalid outcome')

    for did,d in decisions.items():
        obs=obs_by_dec.get(did,[])
        unresolved=[o for o in obs if o.get('state')!='CLOSED']
        disp=d.get('disposition'); consequence=d.get('consequence')
        if disp=='READY':
            if unresolved: err.append(f'{did}: READY has unresolved retrieval obligation')
            for o in obs:
                c=o.get('closure',{}).get('disposition')
                if c not in {'RETRIEVAL_USED','NO_HIT_BOUNDED'}:
                    err.append(f'{did}: READY incompatible with retrieval closure {c}')
        elif disp=='PROCEED_UNCERTAIN':
            if consequence!='NON_MATERIAL': err.append(f'{did}: PROCEED_UNCERTAIN allowed only for NON_MATERIAL consequence')
            if not d.get('uncertainty_declared'): err.append(f'{did}: PROCEED_UNCERTAIN requires uncertainty_declared')
            if obs:
                for o in obs:
                    if o.get('state')!='CLOSED' or o.get('closure',{}).get('disposition')!='UNCERTAIN_CONTINUATION':
                        err.append(f'{did}: PROCEED_UNCERTAIN requires obligations closed as UNCERTAIN_CONTINUATION')
        elif disp=='NARROWED' and obs:
            for o in obs:
                if o.get('state')!='CLOSED' or o.get('closure',{}).get('disposition')!='CONSEQUENCE_NARROWED':
                    err.append(f'{did}: NARROWED requires obligations closed as CONSEQUENCE_NARROWED')
        elif disp=='ABSTAINED' and obs:
            for o in obs:
                if o.get('state')!='CLOSED' or o.get('closure',{}).get('disposition')!='ABSTAINED':
                    err.append(f'{did}: ABSTAINED requires obligations closed as ABSTAINED')
    return err


def expected_failure_stage(e):
    need=e.get('oracle_retrieval_needed')
    trig=e.get('trigger_fired'); scope=e.get('query_scope_adequate'); execution=e.get('resolver_execution')
    relevant=set(e.get('oracle_relevant_record_ids',[]) or [])
    returned=set(e.get('returned_record_ids',[]) or [])
    projected=set(e.get('projected_record_ids',[]) or [])
    applied=set(e.get('applied_record_ids',[]) or [])
    if need=='UNKNOWN': return 'ORACLE_UNKNOWN'
    if need=='NO': return 'FALSE_POSITIVE_TRIGGER' if trig else 'NOT_REQUIRED'
    if not trig: return 'TRIGGER_FALSE_NEGATIVE'
    if execution=='NOT_INVOKED': return 'RESOLVER_NOT_INVOKED'
    if scope=='NO': return 'QUERY_SCOPE_MISS'
    if scope=='UNKNOWN': return 'QUERY_SCOPE_UNKNOWN'
    if execution=='FAILED': return 'RESOLVER_FAILURE'
    if relevant and not (relevant & returned): return 'RESOLVER_FALSE_NEGATIVE'
    relevant_returned = relevant & returned if relevant else returned
    if relevant_returned and not (relevant_returned & projected): return 'PROJECTION_DROP'
    relevant_projected = relevant_returned & projected
    if relevant_projected and not (relevant_projected & applied): return 'APPLICATION_FAILURE'
    return 'SUCCESS'

def validate_evaluation(e):
    err=[f'schema: {x.message}' for x in Draft202012Validator(load(EVAL_SCHEMA)).iter_errors(e)]
    expected=expected_failure_stage(e)
    if e.get('failure_stage')!=expected:
        err.append(f"failure_stage {e.get('failure_stage')} conflicts with computed {expected}")
    if e.get('oracle_retrieval_needed')=='YES' and not e.get('oracle_relevant_record_ids'):
        err.append('oracle YES requires at least one oracle_relevant_record_id for this record-level evaluation')
    if e.get('resolver_execution')!='SUCCEEDED' and e.get('returned_record_ids'):
        err.append('returned records require resolver_execution=SUCCEEDED')
    if not e.get('trigger_fired') and e.get('query_scope_adequate')!='NOT_APPLICABLE':
        err.append('query_scope_adequate must be NOT_APPLICABLE when trigger did not fire')
    if not set(e.get('projected_record_ids',[]) or []).issubset(set(e.get('returned_record_ids',[]) or [])):
        err.append('projected_record_ids must be a subset of returned_record_ids')
    if not set(e.get('applied_record_ids',[]) or []).issubset(set(e.get('projected_record_ids',[]) or [])):
        err.append('applied_record_ids must be a subset of projected_record_ids')
    return err


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('path'); ap.add_argument('--evaluation',action='store_true'); a=ap.parse_args()
    d=load(a.path); err=validate_evaluation(d) if a.evaluation else validate_runtime(d)
    scope='evaluation trace consistency; oracle belongs to evaluation only' if a.evaluation else 'post-trigger retrieval-obligation lifecycle consistency; trigger correctness and resolver truth remain external'
    print(json.dumps({'valid':not err,'scope':scope,'errors':err},indent=2))
    raise SystemExit(0 if not err else 1)
if __name__=='__main__': main()
