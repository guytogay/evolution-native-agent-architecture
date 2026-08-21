#!/usr/bin/env python3
"""Phase C: empirically determine whether the 98-fixture corpus exercises the
dict-key vs inner-id registry divergence (the latent identity-ambiguity defect
found in Phase A). Loads the SAME fixtures run_v24 uses; scans every registry
for dict-form entries whose DICT KEY != the entry's inner id field."""
import sys, json
from pathlib import Path
from datetime import date

HERE = Path("C:/Users/PC/WorkBuddy/2026-08-21-12-05-33/validation-workspace/ena-repo/research/prototypes/v2-machine-contract-hardening/v2.4").resolve()
PROTO_ROOT = HERE.parent
REPO = Path("C:/Users/PC/WorkBuddy/2026-08-21-12-05-33/validation-workspace/ena-repo").resolve()
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(PROTO_ROOT/"v2.3"))
sys.path.insert(0, str(PROTO_ROOT/"v2.2"))
sys.path.insert(0, str(PROTO_ROOT/"v2.1"))
sys.path.insert(0, str(PROTO_ROOT))
sys.path.insert(0, str(REPO/"research/prototypes/v2-machine-contract-hardening/v2.3"))
sys.path.insert(0, str(REPO/"research/prototypes/v2-machine-contract-hardening/v2.2"))
sys.path.insert(0, str(REPO/"research/prototypes/v2-machine-contract-hardening/v2.1"))
sys.path.insert(0, str(REPO/"research/prototypes/v2-machine-contract-hardening"))

from fixtures import get_fixtures as g1
from fixtures_v21 import get_fixtures as g2
from fixtures_v22 import get_v22_fixtures
from fixtures_migrated import get_migrated_fixtures
from independent_fixtures import get_independent_fixtures
from successor_controls import get_controls

REGDEFS = [("evidence_registry","evidence_id"),("root_registry","root_id"),
           ("obligations","obligation_id"),("authority_registry","grant_id"),
           ("support_registry","support_id"),("support_relations","support_id")]

def scan_one(reg, idkey):
    out=[]
    if isinstance(reg, dict):
        for k,v in reg.items():
            if isinstance(v,dict):
                inner=v.get(idkey)
                if inner is not None and inner!=k:
                    out.append((k,inner))
    return out

def scan_payload(p):
    res=[]
    for rn,ik in REGDEFS:
        for (k,inner) in scan_one(p.get(rn), ik):
            res.append((rn,k,inner))
    return res

getters=[("FROZEN_V2",g1),("FROZEN_V21",g2),("FROZEN_V22",get_v22_fixtures),
         ("FROZEN_V23",get_migrated_fixtures),("INDEPENDENT",get_independent_fixtures),
         ("SUCCESSOR_CONTROL",get_controls)]
allf=[]
for tag,g in getters:
    try:
        fs=g()
    except Exception as e:
        print("LOAD ERR",tag,e); continue
    for fx in fs:
        allf.append((tag,fx))

divergent=[]   # key != inner id
dict_forms={}  # count dict vs list usage per registry
for tag,fx in allf:
    p=fx.get("payload",{})
    for rn,ik in REGDEFS:
        reg=p.get(rn)
        if isinstance(reg,dict):
            dict_forms[rn]=dict_forms.get(rn,0)+1
        elif isinstance(reg,list):
            dict_forms[rn+"_LIST"]=dict_forms.get(rn+"_LIST",0)+1
    for (rn,k,inner) in scan_payload(p):
        divergent.append((tag,fx.get("id"),rn,k,inner))

print("TOTAL FIXTURES LOADED:", len(allf))
print("DICT-FORM REGISTRY USAGE (count of fixtures using a dict for this registry):")
for k,v in sorted(dict_forms.items()):
    print(f"   {k:22} {v}")
print()
print("KEY != INNER-ID DIVERGENCE OCCURRENCES:", len(divergent))
for d in divergent:
    print("   ", d)
print()
if not divergent:
    print("CONCLUSION: the 98-fixture corpus NEVER exercises dict-key != inner-id.")
    print("The latent identity-ambiguity defect is invisible to the 98/98 replay.")
