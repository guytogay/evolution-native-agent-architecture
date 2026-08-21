#!/usr/bin/env python3
"""Targeted revalidation harness — PRIOR IMPLEMENTATION FALSIFIER (same session, PR #38).

Loads BOTH the falsified old candidate (f7dc620) and the successor candidate.1
(034b789) implementations, and re-runs THIS validator's original D1/D2/D3
falsifiers plus the directly-affected extended controls. Does NOT use author's
DSH controls as the oracle.
"""
import importlib.util, json, sys, traceback

OLD = r"C:/Users/PC/WorkBuddy/ena-validation/harness/old/validate_contracts.py"
NEW = r"C:/Users/PC/WorkBuddy/ena-validation/harness/new/validate_contracts.py"

def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

old = load(OLD, "old_vc")
new = load(NEW, "new_vc")

# ---- payload builders (verbatim from PR #38 probe_harness) ----
def base_claim(cid="c1", status="SUPPORTED", ctype="FACT", refs=None, extra=None):
    c = {"claim_id": cid, "status": status, "claim_type": ctype,
         "support_relation_refs": refs if refs is not None else ["s1"], "scope": {}}
    if extra: c.update(extra)
    return c

def sup_s1(status="SUPPORTS", ev=None, extra=None):
    s = {"support_id": "s1", "claim_ref": "c1", "support_status": status,
         "evidence_refs": ev if ev is not None else ["e1"]}
    if extra: s.update(extra)
    return s

def ev_reg(entries=None):
    return entries if entries is not None else {"e1": {"evidence_id": "e1", "root_provenance": "r1"}}

# ---------------------------------------------------------------------------
# Run helpers
# ---------------------------------------------------------------------------
def run(mod, payload):
    et = payload.get("eval_time")
    try:
        out = mod.validate_case(payload, et)
        return {"verdict": out.get("verdict"), "code": out.get("code"), "codes": out.get("codes"),
                "exc": None}
    except Exception as e:
        return {"verdict": "EXCEPTION", "code": f"EXC:{type(e).__name__}", "codes": None,
                "exc": "".join(traceback.format_exception_only(type(e), e)).strip()}

def show(res):
    return f'{res["verdict"]}/{res["code"]}'

results = []  # each: id, category, expected, old, new, note

def rec(pid, cat, expected, old_r, new_r, note=""):
    results.append({"id": pid, "category": cat, "expected": expected,
                    "old": show(old_r), "new": show(new_r), "note": note,
                    "old_exc": old_r.get("exc"), "new_exc": new_r.get("exc")})

# ===========================================================================
# PHASE B — reproduce D1/D2/D3 on OLD candidate (f7dc620)
# ===========================================================================
# D1 — P42
p42 = {"eval_time":"2026-01-01",
       "claim": base_claim(ctype="FACT"),
       "support_registry":{"s1":sup_s1()},
       "evidence_registry":ev_reg(),
       "obligations":{"o1":{"obligation_id":"o1","materiality":"MATERIAL",
                           "trigger":{"observed":True},"status":"PENDING",
                           "required_before_claim_refs":["c1"]}}}
rec("P42","D1-repro-on-OLD (expect BLOCK, old was OK)", "BLOCK", run(old,p42), run(new,p42),
    "non-completion claim + bound MATERIAL PENDING obligation")

# D2 — P10
p10 = {"eval_time":"2026-01-01",
       "support":{"support_status":"SUPPORTS","claim_ref":"c1","evidence_refs":["e1"]}}
rec("P10","D2-repro-on-OLD (expect OK, old was BLOCK)", "OK", run(old,p10), run(new,p10),
    "top-level support dict WITHOUT id")

# D3 — P16 (root registry absent -> UNKNOWN)
p16 = {"eval_time":"2026-01-01",
       "claim": base_claim(),
       "support_registry":{"s1":sup_s1(extra={"independence_basis":{"claimed_independent_count":2,
                                                                     "root_provenance":["r1","r2"]}})},
       "evidence_registry":ev_reg()}
rec("P16","D3-repro-on-OLD (root registry absent)", "UNKNOWN/ROOT_REGISTRY_UNAVAILABLE",
    run(old,p16), run(new,p16), "coherent root_provenance, root registry absent")

# D3 — P17 (root registry present, distinct origins -> OK)
p17 = {"eval_time":"2026-01-01",
       "claim": base_claim(),
       "support_registry":{"s1":sup_s1(extra={"independence_basis":{"claimed_independent_count":2,
                                                                     "root_provenance":["r1","r2"]}})},
       "evidence_registry":ev_reg(),
       "root_registry":{"r1":{"root_id":"r1","actual_origin":"O1"},
                        "r2":{"root_id":"r2","actual_origin":"O2"}}}
rec("P17","D3-repro-on-OLD (root registry present, distinct) -> old falsely BLOCK?", "OK",
    run(old,p17), run(new,p17), "root_provenance-backed independence, distinct origins")

# ===========================================================================
# PHASE C — D1 closure + extended controls on NEW (034b789)
# ===========================================================================
# D1-A bound MATERIAL PENDING -> BLOCK
d1a = dict(p42)
rec("D1-A","D1 closure: non-completion + bound MATERIAL PENDING", "BLOCK",
    run(new,d1a), run(new,d1a))

# D1-B bound MATERIAL FAILED -> BLOCK (observed)
d1b = {"eval_time":"2026-01-01","claim":base_claim(ctype="FACT"),
       "support_registry":{"s1":sup_s1()},"evidence_registry":ev_reg(),
       "obligations":{"o1":{"obligation_id":"o1","materiality":"MATERIAL","status":"FAILED",
                           "trigger":{"observed":True},"required_before_claim_refs":["c1"]}}}
rec("D1-B","D1 closure: non-completion + bound MATERIAL FAILED", "BLOCK",
    run(new,d1b), run(new,d1b))

# D1-C bound MATERIAL UNKNOWN -> BLOCK (observed)
d1c = {"eval_time":"2026-01-01","claim":base_claim(ctype="FACT"),
       "support_registry":{"s1":sup_s1()},"evidence_registry":ev_reg(),
       "obligations":{"o1":{"obligation_id":"o1","materiality":"MATERIAL","status":"UNKNOWN",
                           "trigger":{"observed":True},"required_before_claim_refs":["c1"]}}}
rec("D1-C","D1 closure: non-completion + bound MATERIAL UNKNOWN", "BLOCK",
    run(new,d1c), run(new,d1c))

# D1-D UNRELATED MATERIAL PENDING (binds c2, not c1) -> must NOT block c1
d1d = {"eval_time":"2026-01-01","claim":base_claim(ctype="FACT"),
       "support_registry":{"s1":sup_s1()},"evidence_registry":ev_reg(),
       "obligations":{"o1":{"obligation_id":"o1","materiality":"MATERIAL","status":"PENDING",
                           "required_before_claim_refs":["c2"]}}}
rec("D1-D","D1 positive: unrelated MATERIAL PENDING (binds c2) must NOT block c1", "OK",
    run(new,d1d), run(new,d1d))

# D1-E bound SATISFIED with closure evidence -> OK
d1e = {"eval_time":"2026-01-01","claim":base_claim(ctype="FACT"),
       "support_registry":{"s1":sup_s1()},"evidence_registry":{"e1":{"evidence_id":"e1","root_provenance":"r1"},
                                                              "ce1":{"evidence_id":"ce1","root_provenance":"rc"}},
       "obligations":{"o1":{"obligation_id":"o1","materiality":"MATERIAL","status":"SATISFIED",
                           "closure_evidence_refs":["ce1"],"required_before_claim_refs":["c1"]}}}
rec("D1-E","D1 positive: bound SATISFIED w/ closure evidence", "OK",
    run(new,d1e), run(new,d1e))

# D1-F completion claim still requires required_obligation_refs behavior
# F1: completion w/ PENDING bound obligation -> BLOCK (consistent)
d1f1 = {"eval_time":"2026-01-01","claim":base_claim(ctype="TASK_COMPLETION"),
        "support_registry":{"s1":sup_s1()},"evidence_registry":ev_reg(),
        "obligations":{"o1":{"obligation_id":"o1","materiality":"MATERIAL","status":"PENDING",
                            "required_before_claim_refs":["c1"]}}}
rec("D1-F1","D1: completion + PENDING bound obligation still BLOCK", "BLOCK",
    run(new,d1f1), run(new,d1f1))
# F2: completion referencing obligation but obligation satisfied+closure -> OK
d1f2 = {"eval_time":"2026-01-01","claim":base_claim(ctype="TASK_COMPLETION",extra={"required_obligation_refs":["o1"]}),
        "support_registry":{"s1":sup_s1()},"evidence_registry":{"e1":{"evidence_id":"e1","root_provenance":"r1"},
                                                               "ce1":{"evidence_id":"ce1","root_provenance":"rc"}},
        "obligations":{"o1":{"obligation_id":"o1","materiality":"MATERIAL","status":"SATISFIED",
                            "closure_evidence_refs":["ce1"],"required_before_claim_refs":["c1"]}}}
rec("D1-F2","D1: completion w/ required_obligation_refs satisfied -> OK", "OK",
    run(new,d1f2), run(new,d1f2))

# D1-G obligation both referenced and bound -> single coherent semantics (no dup)
d1g = {"eval_time":"2026-01-01","claim":base_claim(ctype="FACT"),
       "support_registry":{"s1":sup_s1()},"evidence_registry":ev_reg(),
       "obligations":{"o1":{"obligation_id":"o1","materiality":"MATERIAL","status":"PENDING",
                           "trigger":{"observed":True},"required_before_claim_refs":["c1"]}}}
r_g = run(new,d1g)
rec("D1-G","D1: obligation referenced+bound yields single code (no duplicate semantics)", "BLOCK",
    r_g, r_g)

# ===========================================================================
# PHASE D — D2 closure + extended controls on NEW
# ===========================================================================
# D2-A id-less direct support -> OK
rec("D2-A","D2 closure: standalone top-level support w/o ID (direct, legitimate)", "OK",
    run(new,p10), run(new,p10))
# D2-B top-level support WITH id -> OK
p11 = {"eval_time":"2026-01-01",
       "support":{"support_id":"s1","support_status":"SUPPORTS","evidence_refs":["e1"]}}
rec("D2-B","D2: top-level support WITH id (standalone)", "OK", run(new,p11), run(new,p11))
# D2-C claim refs an ID; id-less DIRECT support must NOT satisfy ref -> BLOCK
d2c = {"eval_time":"2026-01-01","claim":base_claim(),
       "support":{"support_status":"SUPPORTS","claim_ref":"c1","evidence_refs":["e1"]},
       "evidence_registry":ev_reg()}
rec("D2-C","D2: claim refs s1 but only id-less direct support -> cannot resolve -> BLOCK", "BLOCK",
    run(new,d2c), run(new,d2c))
# D2-D list-form registry entry without ID -> REGISTRY_MALFORMED
d2d = {"eval_time":"2026-01-01","obligations":[{"status":"SATISFIED"}]}
rec("D2-D","D2: list-form registry entry without id -> REGISTRY_MALFORMED", "BLOCK/REGISTRY_MALFORMED",
    run(new,d2d), run(new,d2d))
# D2-E dict registry key != inner id -> REGISTRY_MALFORMED
d2e = {"eval_time":"2026-01-01","claim":base_claim(),
       "support_registry":{"s1":{"support_id":"sX","claim_ref":"c1","support_status":"SUPPORTS","evidence_refs":["e1"]}},
       "evidence_registry":ev_reg()}
rec("D2-E","D2: dict registry key != inner id -> REGISTRY_MALFORMED", "BLOCK/REGISTRY_MALFORMED",
    run(new,d2e), run(new,d2e))
# D2-F dict registry missing inner ID but key present -> R12 backfill OK
d2f = {"eval_time":"2026-01-01","claim":base_claim(),
       "support_registry":{"s1":{"claim_ref":"c1","support_status":"SUPPORTS","evidence_refs":["e1"]}},
       "evidence_registry":ev_reg()}
rec("D2-F","D2: dict registry missing inner id w/ key -> R12 backfill OK", "OK",
    run(new,d2f), run(new,d2f))
# D2-G malformed top-level support shape -> fail-closed
d2g = {"eval_time":"2026-01-01","support":"notadict"}
rec("D2-G","D2: malformed top-level support shape -> fail-closed BLOCK", "BLOCK",
    run(new,d2g), run(new,d2g))

# ===========================================================================
# PHASE E — D3 closure + extended controls on NEW
# ===========================================================================
# D3-A claimed count > distinct roots -> BLOCK/OVERCLAIMED
d3a = {"eval_time":"2026-01-01","claim":base_claim(),
       "support_registry":{"s1":sup_s1(extra={"independence_basis":{"claimed_independent_count":3,
                                                                     "root_provenance":["r1","r2"]}})},
       "evidence_registry":ev_reg()}
rec("D3-A","D3: claimed 3 but 2 roots -> OVERCLAIMED", "BLOCK/INDEPENDENCE_OVERCLAIMED",
    run(new,d3a), run(new,d3a))
# D3-B claimed independence but no root_provenance -> BLOCK
d3b = {"eval_time":"2026-01-01","claim":base_claim(),
       "support_registry":{"s1":sup_s1(extra={"independence_basis":{"claimed_independent_count":1,
                                                                     "root_provenance":[]}})},
       "evidence_registry":ev_reg()}
rec("D3-B","D3: independence claimed, no roots -> BLOCK", "BLOCK",
    run(new,d3b), run(new,d3b))
# D3-C root registry absent, coherent roots -> UNKNOWN
rec("D3-C","D3: coherent roots, root registry absent -> UNKNOWN", "UNKNOWN/ROOT_REGISTRY_UNAVAILABLE",
    run(new,p16), run(new,p16))
# D3-D registered roots -> distinct origins -> OK
rec("D3-D","D3: registered roots resolve to distinct origins -> OK", "OK",
    run(new,p17), run(new,p17))
# D3-E roots collapse to fewer distinct origins than claimed -> BLOCK/OVERCLAIMED
d3e = {"eval_time":"2026-01-01","claim":base_claim(),
       "support_registry":{"s1":sup_s1(extra={"independence_basis":{"claimed_independent_count":3,
                                                                     "root_provenance":["r1","r2","r3"]}})},
       "evidence_registry":ev_reg(),
       "root_registry":{"r1":{"root_id":"r1","actual_origin":"O1"},
                        "r2":{"root_id":"r2","actual_origin":"O1"},
                        "r3":{"root_id":"r3","actual_origin":"O1"}}}
rec("D3-E","D3: 3 roots collapse to 1 origin -> OVERCLAIMED", "BLOCK/INDEPENDENCE_OVERCLAIMED",
    run(new,d3e), run(new,d3e))
# D3-F legacy source_origins-only representation remains coherent (not disabled)
d3f = {"eval_time":"2026-01-01","claim":base_claim(),
       "support_registry":{"s1":sup_s1(extra={"independence_basis":{"claimed_independent_count":1,
                                                                     "source_origins":["srcA"]}})},
       "evidence_registry":ev_reg()}
r_f = run(new,d3f)
rec("D3-F","D3: legacy source_origins-only still coherent (no error)", "OK-or-legacy",
    r_f, r_f)
# D3-G both source_origins AND root_provenance; collapse must not be bypassed
d3g = {"eval_time":"2026-01-01","claim":base_claim(),
       "support_registry":{"s1":sup_s1(extra={"independence_basis":{"claimed_independent_count":2,
                                                                     "source_origins":["srcA","srcB"],
                                                                     "root_provenance":["r1","r2"]}})},
       "evidence_registry":ev_reg(),
       "root_registry":{"r1":{"root_id":"r1","actual_origin":"O1"},
                        "r2":{"root_id":"r2","actual_origin":"O1"}}}
rec("D3-G","D3: dual rep, roots collapse -> composed check blocks (no bypass)", "BLOCK/INDEPENDENCE_OVERCLAIMED",
    run(new,d3g), run(new,d3g))

# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------
print("="*110)
print(f"{'ID':7}{'CATEGORY':52}{'EXPECTED':28}{'OLD':26}{'NEW':26}")
print("="*110)
for r in results:
    print(f'{r["id"]:7}{r["category"][:50]:52}{r["expected"][:26]:28}{r["old"]:26}{r["new"]:26}')
    if r["old_exc"]: print(f'     OLD EXC: {r["old_exc"]}')
    if r["new_exc"]: print(f'     NEW EXC: {r["new_exc"]}')
print("="*110)

with open(r"C:/Users/PC/WorkBuddy/ena-validation/harness/closure_results.json","w",encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print("Wrote closure_results.json")
