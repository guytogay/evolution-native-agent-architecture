#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parent
RUNTIME_SCHEMA=ROOT/"routing-runtime.schema.json"
EVAL_SCHEMA=ROOT/"routing-evaluation.schema.json"

def load(path): return json.loads(Path(path).read_text(encoding="utf-8"))

def schema_errors(doc,schema_path):
    schema=load(schema_path)
    return [f"schema: {e.message}" for e in Draft202012Validator(schema).iter_errors(doc)]

def validate_runtime(doc):
    err=schema_errors(doc,RUNTIME_SCHEMA)
    requests={}
    attempts={}
    for i,r in enumerate(doc.get("requests",[]) or []):
        rid=r.get("request_id")
        if rid in requests: err.append(f"duplicate request_id {rid}")
        elif rid: requests[rid]=r
    for i,a in enumerate(doc.get("attempts",[]) or []):
        aid=a.get("attempt_id")
        if aid in attempts: err.append(f"duplicate attempt_id {aid}")
        elif aid: attempts[aid]=a
        req=a.get("request_id")
        if req and req not in requests: err.append(f"{aid}: unknown request_id {req}")
        scopes=a.get("searched_scope_refs",[]) or []
        returned=a.get("returned_record_ids",[]) or []
        result=a.get("result")
        coverage=a.get("coverage")
        if result=="HIT":
            if not scopes: err.append(f"{aid}: HIT requires represented searched_scope_refs")
            if not returned: err.append(f"{aid}: HIT requires returned_record_ids")
        elif result=="NO_HIT":
            if not scopes: err.append(f"{aid}: NO_HIT requires represented searched_scope_refs")
            if returned: err.append(f"{aid}: NO_HIT cannot return records")
        elif result=="FAILED":
            if returned: err.append(f"{aid}: FAILED cannot return records")
            if coverage=="DECLARED_ROUTE_COMPLETE":
                err.append(f"{aid}: FAILED cannot claim DECLARED_ROUTE_COMPLETE")
        if coverage=="DECLARED_ROUTE_COMPLETE" and not scopes:
            err.append(f"{aid}: DECLARED_ROUTE_COMPLETE requires non-empty searched_scope_refs")
    return err

def route_stage(oracle_required_scope_groups,searched_scope_refs,attempted=True,coverage="DECLARED_ROUTE_COMPLETE"):
    if not attempted: return "ROUTING_NOT_ATTEMPTED"
    searched=set(searched_scope_refs or [])
    if coverage=="UNKNOWN": return "QUERY_SCOPE_UNKNOWN"
    for group in oracle_required_scope_groups or []:
        if not searched.intersection(group):
            return "QUERY_SCOPE_MISS"
    return "ROUTING_SUCCESS"

def validate_evaluation(doc):
    err=schema_errors(doc,EVAL_SCHEMA)
    expected=route_stage(
        doc.get("oracle_required_scope_groups",[]),
        doc.get("searched_scope_refs",[]),
        attempted=doc.get("stage")!="ROUTING_NOT_ATTEMPTED",
        coverage="UNKNOWN" if doc.get("stage")=="QUERY_SCOPE_UNKNOWN" else "DECLARED_ROUTE_COMPLETE",
    )
    if doc.get("stage") not in {"ROUTING_NOT_ATTEMPTED","QUERY_SCOPE_UNKNOWN"} and doc.get("stage")!=expected:
        err.append(f"stage {doc.get('stage')} inconsistent with oracle scope groups; expected {expected}")
    return err

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--evaluation",action="store_true")
    a=ap.parse_args()
    doc=load(a.path)
    err=validate_evaluation(doc) if a.evaluation else validate_runtime(doc)
    print(json.dumps({"valid":not err,"scope":"resolver-routing-0.1 represented consistency only","errors":err},indent=2))
    raise SystemExit(0 if not err else 1)

if __name__=="__main__": main()
