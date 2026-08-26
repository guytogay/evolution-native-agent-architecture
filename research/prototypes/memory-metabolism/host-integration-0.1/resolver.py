#!/usr/bin/env python3
"""Reference cold scope resolver for ENA Memory Metabolism research.

This is a Host organ example, not normative ENA architecture.
The hot side supplies only a bounded intent/query. The scope catalog stays cold.
"""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path
from collections import Counter

ROOT=Path(__file__).resolve().parent
REGISTRY=ROOT/'scope-registry.json'
STOP={'the','a','an','and','or','of','to','for','in','on','is','are','be','with','from','after','before','current','agent'}

def tokens(text):
    return [x for x in re.findall(r'[a-z0-9_-]+', text.lower()) if x not in STOP and len(x)>1]

def snapshot_hash(reg):
    raw=json.dumps(reg,sort_keys=True,separators=(',',':')).encode()
    return hashlib.sha256(raw).hexdigest()

def score(query,scope):
    q=Counter(tokens(query)); s=Counter(tokens(scope.get('scope_id','')+' '+scope.get('summary','')))
    overlap=sum(min(q[t],s[t]) for t in q)
    rare=sum(1 for t in q if t in s and ('-' in t or '_' in t))
    return overlap + 0.5*rare

def discover(query,max_initial=2):
    reg=json.loads(REGISTRY.read_text(encoding='utf-8'))
    ranked=sorted(((score(query,s),s['scope_id']) for s in reg['scopes']), key=lambda x:(-x[0],x[1]))
    positive=[x for x in ranked if x[0]>0]
    selected=[sid for _,sid in (positive[:max_initial] if positive else ranked[:1])]
    return reg,ranked,selected

def expand(reg,selected,already=None,max_new=2):
    already=set(already or [])|set(selected); byid={s['scope_id']:s for s in reg['scopes']}; out=[]
    for sid in selected:
        for n in byid.get(sid,{}).get('neighbors',[]):
            if n not in already and n not in out:
                out.append(n)
                if len(out)>=max_new: return out
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('query'); ap.add_argument('--max-initial',type=int,default=2); ap.add_argument('--expand-after-no-hit',action='store_true'); a=ap.parse_args()
    reg,ranked,selected=discover(a.query,a.max_initial); byid={s['scope_id']:s for s in reg['scopes']}
    result={
      'registry_snapshot_ref':'sha256:'+snapshot_hash(reg),
      'selected_scope_refs':selected,
      'selected_paths':{sid:byid[sid]['paths'] for sid in selected},
      'ranking':[{'scope_id':sid,'score':scorev} for scorev,sid in ranked],
      'coverage':'PARTIAL',
      'note':'Reference organ only; lexical score does not prove scope relevance or discovery completeness.'
    }
    if a.expand_after_no_hit:
        ex=expand(reg,selected,max_new=2); result['bounded_expansion_scope_refs']=ex; result['bounded_expansion_paths']={sid:byid[sid]['paths'] for sid in ex}
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
