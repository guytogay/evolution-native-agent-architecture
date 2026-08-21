#!/usr/bin/env python3
"""V0.3.3-candidate.1 PR #38 fresh-independent-validation probes — payloads
VERBATIM from the fresh validator's probe harness
(collaboration/inbox/2026-08-21-ena-v033-fresh-independent-validation-wb.probe-harness.py,
WorkBuddy/Hy3, merged c1d29f6). Provenance preserved; the original harness,
manifest, and results files are NOT modified.

`expect` is the DSH-RECONCILED semantic expected verdict under
v0.3.3-candidate.1 semantics (from the ACCEPTED report + corrected semantics):
  * D1 (P42): BLOCK (bound obligation gates non-completion claim);
  * D2 (P10): OK (id-less top-level support legitimate);
  * D3 (P16/P17): UNKNOWN / OK (root-provenance representation authoritative);
  * P12: OK (unreferenced duplicate inert — the validator's own prediction
    error, accepted semantics);
  * P19-P22: BLOCK (verdict; the harness's differing CODE predictions were
    fixture errors in their probes — completion claims require obligation refs).
"""
import copy

# ---- builder helpers reproduced verbatim from the harness ----
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

PR38_PROBES = []

def add(pid, expect, payload):
    PR38_PROBES.append({"id": pid, "kind": "PR38_PROBE",
                        "provenance": "WORKBUDDY_FRESH_VALIDATOR_PR38",
                        "expected_verdict": expect, "payload": payload})

# --- A. happy / positive controls ---
add("P01", "OK", {"eval_time": "2026-01-01", "claim": base_claim(),
                  "support_registry": {"s1": sup_s1()}, "evidence_registry": ev_reg()})
add("P02", "BLOCK", {"eval_time": "2026-01-01", "claim": base_claim(refs=[])})
add("P03", "BLOCK", {"eval_time": "2026-01-01", "claim": base_claim(),
                     "support_registry": {"s1": sup_s1(status="CONTRADICTS")}, "evidence_registry": ev_reg()})
add("P04", "BLOCK", {"eval_time": "2026-01-01", "claim": base_claim(),
                     "support_registry": {"s1": sup_s1(status="")}, "evidence_registry": ev_reg()})
add("P05", "UNKNOWN", {"eval_time": "2026-01-01", "claim": base_claim(),
                       "support_registry": {"s1": sup_s1(status="PARTIAL")}, "evidence_registry": ev_reg()})
add("P06", "OK", {"eval_time": "2026-01-01", "claim": base_claim(extra={"support_claim": "PARTIAL"}),
                  "support_registry": {"s1": sup_s1(status="PARTIAL")}, "evidence_registry": ev_reg()})
add("P07", "OK", {"eval_time": "2026-01-01", "claim": base_claim(), "support_registry": {"s1": sup_s1()}})
add("P08", "BLOCK", {"eval_time": "2026-01-01", "claim": base_claim(),
                     "support_registry": {"s1": sup_s1()}, "evidence_registry": {}})
add("P09", "BLOCK", {"eval_time": "2026-01-01", "claim": base_claim(),
                     "support_registry": {"s1": sup_s1(ev=[])}, "evidence_registry": ev_reg()})

# --- B. FLAG candidates ---
add("P10", "OK", {"eval_time": "2026-01-01",
                  "support": {"support_status": "SUPPORTS", "claim_ref": "c1", "evidence_refs": ["e1"]}})
add("P11", "OK", {"eval_time": "2026-01-01",
                  "support": {"support_id": "s1", "support_status": "SUPPORTS", "evidence_refs": ["e1"]}})
add("P12", "OK", {"eval_time": "2026-01-01",
                  "support": [sup_s1(), {"support_id": "s1", "claim_ref": "c1", "support_status": "CONTRADICTS", "evidence_refs": ["e1"]}]})
add("P13", "OK", {"eval_time": "2026-01-01", "support": [sup_s1(), dict(sup_s1())]})
add("P14", "BLOCK", {"eval_time": "2026-01-01", "claim": base_claim(),
                     "support_registry": {"s1": sup_s1(extra={"independence_basis": {"claimed_independent_count": 3, "root_provenance": ["r1", "r2"]}})},
                     "evidence_registry": ev_reg()})
add("P15", "BLOCK", {"eval_time": "2026-01-01", "claim": base_claim(),
                     "support_registry": {"s1": sup_s1(extra={"independence_basis": {"claimed_independent_count": 1, "root_provenance": []}})},
                     "evidence_registry": ev_reg()})
add("P16", "UNKNOWN", {"eval_time": "2026-01-01", "claim": base_claim(),
                       "support_registry": {"s1": sup_s1(extra={"independence_basis": {"claimed_independent_count": 2, "root_provenance": ["r1", "r2"]}})},
                       "evidence_registry": ev_reg()})
add("P17", "OK", {"eval_time": "2026-01-01", "claim": base_claim(),
                  "support_registry": {"s1": sup_s1(extra={"independence_basis": {"claimed_independent_count": 2, "root_provenance": ["r1", "r2"]}})},
                  "evidence_registry": ev_reg(),
                  "root_registry": {"r1": {"root_id": "r1", "actual_origin": "O1"}, "r2": {"root_id": "r2", "actual_origin": "O2"}}})

# --- C. obligations ---
add("P18", "BLOCK", {"eval_time": "2026-01-01", "obligations": {"o1": {"obligation_id": "o1", "status": "WEIRD"}}})
add("P19", "BLOCK", {"eval_time": "2026-01-01", "claim": base_claim(ctype="TASK_COMPLETION", refs=[]),
                     "support_registry": {"s1": sup_s1()}, "evidence_registry": ev_reg()})
add("P20", "BLOCK", {"eval_time": "2026-01-01", "claim": base_claim(ctype="TASK_COMPLETION"),
                     "support_registry": {"s1": sup_s1()}, "evidence_registry": ev_reg(),
                     "obligations": {"o1": {"obligation_id": "o1", "materiality": "MATERIAL",
                                            "trigger": {"observed": True}, "status": "PENDING",
                                            "required_before_claim_refs": ["c1"]}}})
add("P21", "BLOCK", {"eval_time": "2026-01-01", "claim": base_claim(ctype="TASK_COMPLETION"),
                     "support_registry": {"s1": sup_s1()}, "evidence_registry": ev_reg(),
                     "obligations": {"o1": {"obligation_id": "o1", "status": "SATISFIED",
                                            "closure_evidence_refs": [], "required_before_claim_refs": ["c1"]}}})
add("P22", "BLOCK", {"eval_time": "2026-01-01", "claim": base_claim(ctype="TASK_COMPLETION"),
                     "support_registry": {"s1": sup_s1()}, "evidence_registry": ev_reg(),
                     "obligations": {"o1": {"obligation_id": "o1", "status": "SATISFIED",
                                            "closure_evidence_refs": ["ce1"], "required_before_claim_refs": ["c1"]}}})

# --- D. authority / mandate ---
add("P23", "OK", {"eval_time": "2026-01-01",
                  "binding": {"authority_envelope": ["env"], "mandate": {"source": "USER_EXPLICIT_GRANT", "expires_at": "2026-12-31"}}})
add("P24", "BLOCK", {"eval_time": "2026-01-01",
                     "binding": {"authority_envelope": ["env"], "mandate": {"source": "FOO", "expires_at": "2026-12-31"}}})
add("P25", "OK", {"eval_time": "2026-01-01",
                  "binding": {"authority_envelope": ["env"], "agent": "a1", "host": "h1",
                              "mandate": {"source": "g1", "expires_at": "2026-12-31"}},
                  "authority_registry": {"g1": {"grant_id": "g1", "agent": "a1", "host": "h1", "expires_at": "2026-12-31"}}})
add("P26", "BLOCK", {"eval_time": "2026-01-01",
                     "binding": {"authority_envelope": ["env"], "agent": "a1", "host": "h1",
                                 "mandate": {"source": "g1", "expires_at": "2026-12-31"}},
                     "authority_registry": {"g1": {"grant_id": "g1", "agent": "a1", "host": "h1", "expires_at": "2025-01-01"}}})
add("P27", "BLOCK", {"eval_time": "2026-01-01",
                     "binding": {"authority_envelope": ["env"], "mandate": {"source": "USER_EXPLICIT_GRANT", "expires_at": "2025-01-01"}}})
add("P28", "BLOCK", {"eval_time": "2026-01-01",
                     "binding": {"capabilities": [{"status": "VERIFIED_AVAILABLE", "evidence_refs": [{"ref": "e1", "grade": "E0"}]}]},
                     "evidence_registry": ev_reg()})
add("P29", "OK", {"eval_time": "2026-01-01",
                  "binding": {"capabilities": [{"status": "VERIFIED_AVAILABLE", "evidence_refs": [{"ref": "e1", "grade": "E3"}]}]},
                  "evidence_registry": ev_reg()})
add("P30", "BLOCK", {"eval_time": "2026-01-01",
                     "binding": {"capabilities": [{"status": "VERIFIED_AVAILABLE", "evidence_refs": [{"ref": "e1", "grade": "E9"}]}]},
                     "evidence_registry": ev_reg()})

# --- E. recovery ---
add("P31", "OK", {"eval_time": "2026-01-01",
                  "transition": {"state_restore": {"result": "SUCCESS"}, "history_continuity": {"status": "GAP_VISIBLE"},
                                 "recovery_claim": {"scope": "STATE_ONLY"}}})
add("P32", "OK", {"eval_time": "2026-01-01",
                  "transition": {"state_restore": {"result": "SUCCESS", "evidence_refs": ["s1"]},
                                 "history_continuity": {"status": "PRESERVED", "evidence_refs": ["h1"],
                                                        "post_checkpoint_occurrence_delta_captured": True},
                                 "recovery_claim": {"scope": "STATE_AND_HISTORY"}},
                  "evidence_registry": {"s1": {"evidence_id": "s1", "root_provenance": "rs"},
                                        "h1": {"evidence_id": "h1", "root_provenance": "rh"}}})
add("P33", "BLOCK", {"eval_time": "2026-01-01",
                     "transition": {"state_restore": {"result": "SUCCESS", "evidence_refs": ["s1"]},
                                    "history_continuity": {"status": "PRESERVED", "evidence_refs": ["h1"],
                                                           "post_checkpoint_occurrence_delta_captured": True},
                                    "recovery_claim": {"scope": "STATE_AND_HISTORY"}},
                     "evidence_registry": {"s1": {"evidence_id": "s1", "root_provenance": "rX"},
                                           "h1": {"evidence_id": "h1", "root_provenance": "rX"}}})
add("P34", "BLOCK", {"eval_time": "2026-01-01",
                     "transition": {"state_restore": {"result": "SUCCESS", "evidence_refs": ["h1"]},
                                    "history_continuity": {"status": "PRESERVED", "evidence_refs": ["h1"],
                                                           "post_checkpoint_occurrence_delta_captured": True},
                                    "recovery_claim": {"scope": "STATE_AND_HISTORY"}},
                     "evidence_registry": {"h1": {"evidence_id": "h1", "root_provenance": "r1"}}})

# --- F. registry shape / R12 ---
add("P35", "BLOCK", {"eval_time": "2026-01-01", "claim": base_claim(),
                     "support_registry": {"s1": {"support_id": "sX", "claim_ref": "c1", "support_status": "SUPPORTS", "evidence_refs": ["e1"]}},
                     "evidence_registry": ev_reg()})
add("P36", "BLOCK", {"eval_time": "2026-01-01", "evidence_registry": {"e1": "notadict"}})
add("P37", "BLOCK", {"eval_time": "2026-01-01", "obligations": [{"status": "SATISFIED"}]})

# --- G. eval_time / boundaries ---
add("P38", "OK", {"eval_time": "2026-01-01"})
add("P39", "BLOCK", {})
add("P40", "BLOCK", {"eval_time": "not-a-date"})
add("P41", "BLOCK", {"eval_time": "2026-01-01", "claim": base_claim(),
                     "support_registry": {"s1": sup_s1(extra={"claim_ref": "OTHER"})}, "evidence_registry": ev_reg()})

# --- H. FLAG: D1 ---
add("P42", "BLOCK", {"eval_time": "2026-01-01", "claim": base_claim(ctype="FACT"),
                     "support_registry": {"s1": sup_s1()}, "evidence_registry": ev_reg(),
                     "obligations": {"o1": {"obligation_id": "o1", "materiality": "MATERIAL",
                                            "trigger": {"observed": True}, "status": "PENDING",
                                            "required_before_claim_refs": ["c1"]}}})
add("P43", "OK", {"eval_time": "2026-01-01",
                  "binding": {"capabilities": [{"status": "VERIFIED_AVAILABLE", "evidence_refs": [{"ref": "e1", "grade": "E3"}]}]},
                  "evidence_registry": ev_reg()})


def get_pr38_fixtures():
    return copy.deepcopy(PR38_PROBES)
