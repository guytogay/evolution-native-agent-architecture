#!/usr/bin/env python3
"""Independent probe harness — FRESH validator, no author oracle consulted.

Runs the v0.3.3-candidate validate_case() against probes designed from a blind
read of the implementation only. Predicted verdicts are the validator's own,
derived from the semantic contract (materially false/invalid -> BLOCK,
legitimate+sufficiently-supported -> OK, legitimate-but-unverifiable -> UNKNOWN).
"""
import importlib.util
import json
import sys

CANDIDATE = r"C:/Users/PC/WorkBuddy/ena-validation/repo/releases/v0.3.3-candidate/tools/validate_contracts.py"
spec = importlib.util.spec_from_file_location("vc", CANDIDATE)
vc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vc)

# ---------------------------------------------------------------------------
# Probe builders
# ---------------------------------------------------------------------------
def base_claim(cid="c1", status="SUPPORTED", ctype="FACT", refs=None, extra=None):
    c = {"claim_id": cid, "status": status, "claim_type": ctype,
         "support_relation_refs": refs if refs is not None else ["s1"], "scope": {}}
    if extra:
        c.update(extra)
    return c

def sup_s1(status="SUPPORTS", ev=None, extra=None):
    s = {"support_id": "s1", "claim_ref": "c1", "support_status": status,
         "evidence_refs": ev if ev is not None else ["e1"]}
    if extra:
        s.update(extra)
    return s

def ev_reg(entries=None):
    if entries is None:
        entries = {"e1": {"evidence_id": "e1", "root_provenance": "r1"}}
    return entries

def root_reg(entries=None):
    if entries is None:
        entries = {"r1": {"root_id": "r1", "actual_origin": "originA"}}
    return entries

# ---------------------------------------------------------------------------
# Probe manifest (predicted verdict/code authored BEFORE running)
# ---------------------------------------------------------------------------
PROBES = []

def add(pid, prop, payload, pverdict, pcode, rationale, flag=False):
    PROBES.append({
        "id": pid, "property": prop, "payload": payload,
        "predicted_verdict": pverdict, "predicted_code": pcode,
        "rationale": rationale, "flag": flag,
    })

# --- A. Happy / positive controls -----------------------------------------
add("P01", "SUPPORTED happy path w/ registry + evidence", {
    "eval_time": "2026-01-01",
    "claim": base_claim(),
    "support_registry": {"s1": sup_s1()},
    "evidence_registry": ev_reg(),
}, "OK", "OK", "Full chain resolves; evidence exists; scope empty -> direct match.")

add("P02", "SUPPORTED claim w/o support refs", {
    "eval_time": "2026-01-01",
    "claim": base_claim(refs=[]),
}, "BLOCK", "CLAIM_SUPPORTED_WITHOUT_SUPPORT_REFS", "SUPPORTED requires refs.")

add("P03", "Referenced support CONTRADICTS", {
    "eval_time": "2026-01-01",
    "claim": base_claim(),
    "support_registry": {"s1": sup_s1(status="CONTRADICTS")},
    "evidence_registry": ev_reg(),
}, "BLOCK", "RESOLVED_SUPPORT_CONTRADICTS", "Support contradicts claim.")

add("P04", "Referenced support empty status", {
    "eval_time": "2026-01-01",
    "claim": base_claim(),
    "support_registry": {"s1": sup_s1(status="")},
    "evidence_registry": ev_reg(),
}, "BLOCK", "SUPPORT_NOT_POSITIVE", "Composed layer blocks non-positive referenced support.")

add("P05", "PARTIAL support, claim not narrowed", {
    "eval_time": "2026-01-01",
    "claim": base_claim(),  # status SUPPORTED, no support_claim=PARTIAL
    "support_registry": {"s1": sup_s1(status="PARTIAL")},
    "evidence_registry": ev_reg(),
}, "UNKNOWN", "PARTIAL_SUPPORT_ONLY", "Partial-only cannot establish full SUPPORTED.")

add("P06", "PARTIAL support, claim narrowed PARTIAL", {
    "eval_time": "2026-01-01",
    "claim": base_claim(extra={"support_claim": "PARTIAL"}),
    "support_registry": {"s1": sup_s1(status="PARTIAL")},
    "evidence_registry": ev_reg(),
}, "OK", "OK", "Explicitly narrowed claim accepts partial support.")

add("P07", "Evidence ref declared, registry ABSENT -> baseline OK", {
    "eval_time": "2026-01-01",
    "claim": base_claim(),
    "support_registry": {"s1": sup_s1()},  # evidence_refs e1, no registry
}, "OK", "OK", "Absent evidence registry -> no existence verdict (baseline posture).")

add("P08", "Evidence ref declared, registry present, ref missing", {
    "eval_time": "2026-01-01",
    "claim": base_claim(),
    "support_registry": {"s1": sup_s1()},
    "evidence_registry": {},  # e1 not present
}, "BLOCK", "EVIDENCE_REF_UNRESOLVABLE", "Registry present but ref unresolved.")

add("P09", "Support empty evidence_refs WITH registry", {
    "eval_time": "2026-01-01",
    "claim": base_claim(),
    "support_registry": {"s1": sup_s1(ev=[])},
    "evidence_registry": ev_reg(),
}, "BLOCK", "SUPPORT_WITHOUT_EVIDENCE", "No evidence declared.")

# --- B. FLAG candidates ---------------------------------------------------
add("P10", "Top-level support dict WITHOUT id (FLAG-A false BLOCK)", {
    "eval_time": "2026-01-01",
    "support": {"support_status": "SUPPORTS", "claim_ref": "c1", "evidence_refs": ["e1"]},
}, "OK", "OK", "Self-contained unreferenced support is a valid minimal representation (v0.3.2 accepted support dicts directly). Should not be REGISTRY_MALFORMED.", flag=True)

add("P11", "Top-level support dict WITH id, no claim", {
    "eval_time": "2026-01-01",
    "support": {"support_id": "s1", "support_status": "SUPPORTS", "evidence_refs": ["e1"]},
}, "OK", "OK", "Valid independent support representation.")

add("P12", "Duplicate support ids, conflicting content", {
    "eval_time": "2026-01-01",
    "support": [sup_s1(), {"support_id": "s1", "claim_ref": "c1", "support_status": "CONTRADICTS", "evidence_refs": ["e1"]}],
}, "BLOCK", "DUPLICATE_REF_ID", "Ambiguous identity fails closed (R5).")

add("P13", "Duplicate support ids, identical content -> dedupe", {
    "eval_time": "2026-01-01",
    "support": [sup_s1(), dict(sup_s1())],
}, "OK", "OK", "Byte-identical duplicates dedupe (R5).")

add("P14", "Independence overclaim (string level)", {
    "eval_time": "2026-01-01",
    "claim": base_claim(),
    "support_registry": {"s1": sup_s1(extra={"independence_basis": {"claimed_independent_count": 3, "root_provenance": ["r1", "r2"]}})},
    "evidence_registry": ev_reg(),
}, "BLOCK", "INDEPENDENCE_OVERCLAIMED", "Claimed 3 but only 2 distinct roots.")

add("P15", "Independence w/o root_provenance", {
    "eval_time": "2026-01-01",
    "claim": base_claim(),
    "support_registry": {"s1": sup_s1(extra={"independence_basis": {"claimed_independent_count": 1, "root_provenance": []}})},
    "evidence_registry": ev_reg(),
}, "BLOCK", "INDEPENDENCE_WITHOUT_ROOT_PROVENANCE", "Independence claimed but no roots.")

add("P16", "Independence count ok, root registry ABSENT -> UNKNOWN", {
    "eval_time": "2026-01-01",
    "claim": base_claim(),
    "support_registry": {"s1": sup_s1(extra={"independence_basis": {"claimed_independent_count": 2, "root_provenance": ["r1", "r2"]}})},
    "evidence_registry": ev_reg(),
}, "UNKNOWN", "ROOT_REGISTRY_UNAVAILABLE", "Can't verify origins without root registry.")

add("P17", "Independence count ok, root registry present, distinct origins", {
    "eval_time": "2026-01-01",
    "claim": base_claim(),
    "support_registry": {"s1": sup_s1(extra={"independence_basis": {"claimed_independent_count": 2, "root_provenance": ["r1", "r2"]}})},
    "evidence_registry": ev_reg(),
    "root_registry": {"r1": {"root_id": "r1", "actual_origin": "O1"}, "r2": {"root_id": "r2", "actual_origin": "O2"}},
}, "OK", "OK", "Registry-verified distinct origins satisfy claim.")

# --- C. Obligations -------------------------------------------------------
add("P18", "Obligation status outside vocabulary (F2)", {
    "eval_time": "2026-01-01",
    "obligations": {"o1": {"obligation_id": "o1", "status": "WEIRD"}},
}, "BLOCK", "OBLIGATION_STATUS_OUTSIDE_VOCABULARY", "Vocabulary gate rejects unknown status.")

add("P19", "Completion claim w/o obligation refs", {
    "eval_time": "2026-01-01",
    "claim": base_claim(ctype="TASK_COMPLETION", refs=[]),
    "support_registry": {"s1": sup_s1()},
    "evidence_registry": ev_reg(),
}, "BLOCK", "COMPLETION_CLAIM_WITHOUT_OBLIGATION_REFS", "Completion must reference obligations.")

add("P20", "Completion claim, material PENDING bound obligation", {
    "eval_time": "2026-01-01",
    "claim": base_claim(ctype="TASK_COMPLETION"),
    "support_registry": {"s1": sup_s1()},
    "evidence_registry": ev_reg(),
    "obligations": {"o1": {"obligation_id": "o1", "materiality": "MATERIAL",
                            "trigger": {"observed": True}, "status": "PENDING",
                            "required_before_claim_refs": ["c1"]}},
}, "BLOCK", "MATERIAL_OBLIGATION_BLOCKS_CLAIM", "Open material obligation blocks completion.")

add("P21", "SATISFIED obligation w/o closure evidence", {
    "eval_time": "2026-01-01",
    "claim": base_claim(ctype="TASK_COMPLETION"),
    "support_registry": {"s1": sup_s1()},
    "evidence_registry": ev_reg(),
    "obligations": {"o1": {"obligation_id": "o1", "status": "SATISFIED",
                            "closure_evidence_refs": [], "required_before_claim_refs": ["c1"]}},
}, "BLOCK", "SATISFIED_WITHOUT_CLOSURE_EVIDENCE", "Satisfied must show closure evidence.")

add("P22", "SATISFIED obligation + closure refs, registry ABSENT -> OK", {
    "eval_time": "2026-01-01",
    "claim": base_claim(ctype="TASK_COMPLETION"),
    "support_registry": {"s1": sup_s1()},
    "evidence_registry": ev_reg(),
    "obligations": {"o1": {"obligation_id": "o1", "status": "SATISFIED",
                            "closure_evidence_refs": ["ce1"], "required_before_claim_refs": ["c1"]}},
}, "OK", "OK", "Absent evidence registry -> closure evidence not resolved (baseline).")

# --- D. Authority / mandate ----------------------------------------------
add("P23", "Authority USER_EXPLICIT_GRANT valid horizon", {
    "eval_time": "2026-01-01",
    "binding": {"authority_envelope": ["env"], "mandate": {"source": "USER_EXPLICIT_GRANT", "expires_at": "2026-12-31"}},
}, "OK", "OK", "Explicit user grant with valid horizon authorizes.")

add("P24", "Authority unknown source, no registry", {
    "eval_time": "2026-01-01",
    "binding": {"authority_envelope": ["env"], "mandate": {"source": "FOO", "expires_at": "2026-12-31"}},
}, "BLOCK", "AUTHORITY_MANDATE_SOURCE_NOT_AUTHORIZING", "Unknown source and no registry -> unauthorized.")

add("P25", "Authority via registry grant valid", {
    "eval_time": "2026-01-01",
    "binding": {"authority_envelope": ["env"], "agent": "a1", "host": "h1",
                "mandate": {"source": "g1", "expires_at": "2026-12-31"}},
    "authority_registry": {"g1": {"grant_id": "g1", "agent": "a1", "host": "h1", "expires_at": "2026-12-31"}},
}, "OK", "OK", "Registry grant with matching agent/host/horizon authorizes.")

add("P26", "Authority registry grant EXPIRED", {
    "eval_time": "2026-01-01",
    "binding": {"authority_envelope": ["env"], "agent": "a1", "host": "h1",
                "mandate": {"source": "g1", "expires_at": "2026-12-31"}},
    "authority_registry": {"g1": {"grant_id": "g1", "agent": "a1", "host": "h1", "expires_at": "2025-01-01"}},
}, "BLOCK", "AUTHORITY_MANDATE_SOURCE_NOT_AUTHORIZING", "Grant expiry -> not authorizing.")

add("P27", "Mandate.expires_at expired (direct)", {
    "eval_time": "2026-01-01",
    "binding": {"authority_envelope": ["env"], "mandate": {"source": "USER_EXPLICIT_GRANT", "expires_at": "2025-01-01"}},
}, "BLOCK", "MANDATE_EXPIRED", "Direct mandate horizon expired.")

add("P28", "Capability VERIFIED, grade E0/E1 only", {
    "eval_time": "2026-01-01",
    "binding": {"capabilities": [{"status": "VERIFIED_AVAILABLE", "evidence_refs": [{"ref": "e1", "grade": "E0"}]}]},
    "evidence_registry": ev_reg(),
}, "BLOCK", "VERIFIED_ONLY_STATIC_STRUCTURE_EVIDENCE", "Static-only evidence insufficient for VERIFIED.")

add("P29", "Capability VERIFIED, grade E3 valid ref", {
    "eval_time": "2026-01-01",
    "binding": {"capabilities": [{"status": "VERIFIED_AVAILABLE", "evidence_refs": [{"ref": "e1", "grade": "E3"}]}]},
    "evidence_registry": ev_reg(),
}, "OK", "OK", "Non-static grade with resolvable evidence -> OK.")

add("P30", "Capability VERIFIED, invalid grade", {
    "eval_time": "2026-01-01",
    "binding": {"capabilities": [{"status": "VERIFIED_AVAILABLE", "evidence_refs": [{"ref": "e1", "grade": "E9"}]}]},
    "evidence_registry": ev_reg(),
}, "BLOCK", "EVIDENCE_GRADE_INVALID", "Grade outside vocabulary.")

# --- E. Recovery ----------------------------------------------------------
add("P31", "Recovery STATE_ONLY", {
    "eval_time": "2026-01-01",
    "transition": {"state_restore": {"result": "SUCCESS"}, "history_continuity": {"status": "GAP_VISIBLE"},
                   "recovery_claim": {"scope": "STATE_ONLY"}},
}, "OK", "OK", "State-only recovery supported.")

add("P32", "Recovery STATE_AND_HISTORY full ok", {
    "eval_time": "2026-01-01",
    "transition": {"state_restore": {"result": "SUCCESS", "evidence_refs": ["s1"]},
                   "history_continuity": {"status": "PRESERVED", "evidence_refs": ["h1"],
                                          "post_checkpoint_occurrence_delta_captured": True},
                   "recovery_claim": {"scope": "STATE_AND_HISTORY"}},
    "evidence_registry": {"s1": {"evidence_id": "s1", "root_provenance": "rs"},
                           "h1": {"evidence_id": "h1", "root_provenance": "rh"}},
}, "OK", "OK", "Both state and history evidenced; distinct roots.")

add("P33", "Recovery STATE_AND_HISTORY shared roots", {
    "eval_time": "2026-01-01",
    "transition": {"state_restore": {"result": "SUCCESS", "evidence_refs": ["s1"]},
                   "history_continuity": {"status": "PRESERVED", "evidence_refs": ["h1"],
                                          "post_checkpoint_occurrence_delta_captured": True},
                   "recovery_claim": {"scope": "STATE_AND_HISTORY"}},
    "evidence_registry": {"s1": {"evidence_id": "s1", "root_provenance": "rX"},
                           "h1": {"evidence_id": "h1", "root_provenance": "rX"}},
}, "BLOCK", "HISTORY_EVIDENCE_SHARED_ROOT", "Shared provenance root is not independent history.")

add("P34", "Recovery STATE_AND_HISTORY same evidence refs", {
    "eval_time": "2026-01-01",
    "transition": {"state_restore": {"result": "SUCCESS", "evidence_refs": ["h1"]},
                   "history_continuity": {"status": "PRESERVED", "evidence_refs": ["h1"],
                                          "post_checkpoint_occurrence_delta_captured": True},
                   "recovery_claim": {"scope": "STATE_AND_HISTORY"}},
    "evidence_registry": {"h1": {"evidence_id": "h1", "root_provenance": "r1"}},
}, "BLOCK", "HISTORY_EVIDENCE_SAME_AS_STATE_EVIDENCE", "Same evidence cannot serve both.")

# --- F. Registry shape / R12 ---------------------------------------------
add("P35", "R12 dict key != inner id (support_registry)", {
    "eval_time": "2026-01-01",
    "claim": base_claim(),
    "support_registry": {"s1": {"support_id": "sX", "claim_ref": "c1", "support_status": "SUPPORTS", "evidence_refs": ["e1"]}},
    "evidence_registry": ev_reg(),
}, "BLOCK", "REGISTRY_MALFORMED", "Key/id divergence is malformed.")

add("P36", "Malformed registry (dict value not dict)", {
    "eval_time": "2026-01-01",
    "evidence_registry": {"e1": "notadict"},
}, "BLOCK", "REGISTRY_MALFORMED", "Non-dict registry value malformed.")

add("P37", "List registry entry without id", {
    "eval_time": "2026-01-01",
    "obligations": [{"status": "SATISFIED"}],  # no obligation_id
}, "BLOCK", "REGISTRY_MALFORMED", "List-form entry must declare id.")

# --- G. eval_time / boundaries -------------------------------------------
add("P38", "Empty payload + eval_time -> vacuous OK", {
    "eval_time": "2026-01-01",
}, "OK", "OK", "No consequential claims -> nothing to block.")

add("P39", "Missing eval_time -> BLOCK", {
}, "BLOCK", "EVAL_TIME_REQUIRED", "eval_time is required.")

add("P40", "Malformed eval_time -> BLOCK", {
    "eval_time": "not-a-date",
}, "BLOCK", "EVAL_TIME_REQUIRED", "Unparseable eval_time rejected.")

add("P41", "claim_ref mismatch (R2)", {
    "eval_time": "2026-01-01",
    "claim": base_claim(),
    "support_registry": {"s1": sup_s1(extra={"claim_ref": "OTHER"})},
    "evidence_registry": ev_reg(),
}, "BLOCK", "SUPPORT_TARGET_MISMATCH", "Support must bind back to target claim.")

# --- H. FLAG: non-completion claim gated by bound obligation --------------
add("P42", "FLAG-D: bound PENDING obligation, NON-completion claim (expect BLOCK per R7, actual?)", {
    "eval_time": "2026-01-01",
    "claim": base_claim(ctype="FACT"),  # not a completion type
    "support_registry": {"s1": sup_s1()},
    "evidence_registry": ev_reg(),
    "obligations": {"o1": {"obligation_id": "o1", "materiality": "MATERIAL",
                            "trigger": {"observed": True}, "status": "PENDING",
                            "required_before_claim_refs": ["c1"]}},
}, "BLOCK", "MATERIAL_OBLIGATION_BLOCKS_CLAIM",
   "R7 says obligations BOUND to the claim gate it regardless of completion type. A material PENDING obligation naming c1 in required_before_claim_refs must block.", flag=True)

add("P43", "FLAG: capabilities verified WITHOUT authority_envelope (trust gap)", {
    "eval_time": "2026-01-01",
    "binding": {"capabilities": [{"status": "VERIFIED_AVAILABLE", "evidence_refs": [{"ref": "e1", "grade": "E3"}]}]},
    "evidence_registry": ev_reg(),
}, "OK", "OK",
   "Capabilities verified despite no authority envelope. Acceptable retained boundary, but note VERIFIED does not require authority context.", flag=True)

# ---------------------------------------------------------------------------
# Execute
# ---------------------------------------------------------------------------
results = []
for p in PROBES:
    payload = p["payload"]
    et = payload.get("eval_time")
    try:
        out = vc.validate_case(payload, et)
    except Exception as e:  # should never happen (R11) but guard
        out = {"ok": False, "verdict": "EXCEPTION", "code": f"HARNESS_EXCEPTION:{e}"}
    actual_v = out.get("verdict")
    actual_c = out.get("code")
    # PASS if verdict matches AND (predicted_code == 'OK' or code matches)
    verdict_match = (actual_v == p["predicted_verdict"])
    code_match = (p["predicted_code"] == "OK") or (actual_c == p["predicted_code"])
    passed = verdict_match and code_match
    results.append({
        "id": p["id"], "flag": p["flag"], "property": p["property"],
        "predicted": f'{p["predicted_verdict"]}/{p["predicted_code"]}',
        "actual": f'{actual_v}/{actual_c}',
        "passed": passed,
        "all_codes": out.get("codes"),
        "rationale": p["rationale"],
    })

# Report
n = len(results)
npass = sum(1 for r in results if r["passed"])
nflag = sum(1 for r in results if r["flag"])
print(f"TOTAL={n} PASS={npass} FAIL={n-npass} FLAGGED={nflag}")
print("=" * 100)
for r in results:
    status = "PASS " if r["passed"] else "CHLG "
    flagmark = " *" if r["flag"] else "  "
    print(f'{status}{r["id"]}{flagmark:3} pred={r["predicted"]:45} act={r["actual"]:40} codes={r["all_codes"]}')
print("=" * 100)
print("CHALLENGES:")
for r in results:
    if not r["passed"]:
        print(f'  {r["id"]}: pred={r["predicted"]} act={r["actual"]} :: {r["property"]}')
        print(f'      rationale: {r["rationale"]}')

# Dump machine-readable
with open(r"C:/Users/PC/WorkBuddy/ena-validation/my-probes/probe_results.json", "w", encoding="utf-8") as f:
    json.dump({"total": n, "pass": npass, "probes": results}, f, ensure_ascii=False, indent=2)
print("\nWrote probe_results.json")
