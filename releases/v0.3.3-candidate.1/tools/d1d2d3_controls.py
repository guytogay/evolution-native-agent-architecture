#!/usr/bin/env python3
"""V0.3.3-candidate.1 D1/D2/D3 closure controls (new; provenance DSH_V033C1_CONTROLS).

Derived from the accepted PR #38 findings. Each closure control has an
adversarial or legitimate expectation that pins the corrected semantics.
"""
import copy

CONTROLS = []

def add(cid, kind, expected, payload, rationale):
    CONTROLS.append({"id": cid, "kind": kind, "expected_verdict": expected,
                     "provenance": "DSH_V033C1_CONTROLS", "rationale": rationale,
                     "payload": payload})

# ============================ D1: bound obligations gate ALL claims =========
add("C1-D1-01-bound-pending-non-completion", "ADVERSARIAL", "BLOCK", {
    "eval_time": "2026-01-01",
    "claim": {"claim_id": "c1", "status": "SUPPORTED", "claim_type": "FACT",
              "support_relation_refs": ["s1"], "scope": {}},
    "support_registry": {"s1": {"support_id": "s1", "claim_ref": "c1", "support_status": "SUPPORTS",
                                "evidence_refs": ["e1"]}},
    "evidence_registry": {"e1": {"evidence_id": "e1", "root_provenance": "r1"}},
    "obligations": {"o1": {"obligation_id": "o1", "materiality": "MATERIAL",
                           "trigger": {"observed": True}, "status": "PENDING",
                           "required_before_claim_refs": ["c1"]}},
}, "D1: non-completion claim bound by material PENDING obligation -> BLOCK (exact P42 case)")

add("C1-D1-02-unrelated-pending-does-not-poison", "POSITIVE", "OK", {
    "eval_time": "2026-01-01",
    "claim": {"claim_id": "c1", "status": "SUPPORTED", "claim_type": "FACT",
              "support_relation_refs": ["s1"], "scope": {}},
    "support_registry": {"s1": {"support_id": "s1", "claim_ref": "c1", "support_status": "SUPPORTS",
                                "evidence_refs": ["e1"]}},
    "evidence_registry": {"e1": {"evidence_id": "e1", "root_provenance": "r1"}},
    "obligations": {"o-other": {"obligation_id": "o-other", "materiality": "MATERIAL",
                                "trigger": {"observed": True}, "status": "PENDING",
                                "required_before_claim_refs": ["c-other"]}},
}, "D1: unrelated PENDING obligation (bound to another claim) must NOT poison the non-completion claim")

add("C1-D1-03-bound-satisfied-allows", "POSITIVE", "OK", {
    "eval_time": "2026-01-01",
    "claim": {"claim_id": "c1", "status": "SUPPORTED", "claim_type": "FACT",
              "support_relation_refs": ["s1"], "scope": {}},
    "support_registry": {"s1": {"support_id": "s1", "claim_ref": "c1", "support_status": "SUPPORTS",
                                "evidence_refs": ["e1"]}},
    "evidence_registry": {"e1": {"evidence_id": "e1", "root_provenance": "r1"}},
    "obligations": {"o1": {"obligation_id": "o1", "materiality": "MATERIAL",
                           "trigger": {"observed": True}, "status": "SATISFIED",
                           "closure_evidence_refs": ["e1"], "required_before_claim_refs": ["c1"]}},
}, "D1: bound SATISFIED obligation with closure evidence allows the claim (subject to other checks)")

add("C1-D1-04-completion-own-open-still-blocks", "ADVERSARIAL", "BLOCK", {
    "eval_time": "2026-01-01",
    "claim": {"claim_id": "c1", "status": "SUPPORTED", "claim_type": "TASK_COMPLETION",
              "support_relation_refs": ["s1"], "required_obligation_refs": ["o1"], "scope": {}},
    "support_registry": {"s1": {"support_id": "s1", "claim_ref": "c1", "support_status": "SUPPORTS",
                                "evidence_refs": ["e1"]}},
    "evidence_registry": {"e1": {"evidence_id": "e1", "root_provenance": "r1"}},
    "obligations": {"o1": {"obligation_id": "o1", "materiality": "MATERIAL",
                           "trigger": {"observed": True}, "status": "PENDING"}},
}, "D1 regression guard: completion claim's own referenced open material obligation still blocks")

add("C1-D1-05-referenced-and-bound-single-effect", "ADVERSARIAL", "BLOCK", {
    "eval_time": "2026-01-01",
    "claim": {"claim_id": "c1", "status": "SUPPORTED", "claim_type": "TASK_COMPLETION",
              "support_relation_refs": ["s1"], "required_obligation_refs": ["o1"], "scope": {}},
    "support_registry": {"s1": {"support_id": "s1", "claim_ref": "c1", "support_status": "SUPPORTS",
                                "evidence_refs": ["e1"]}},
    "evidence_registry": {"e1": {"evidence_id": "e1", "root_provenance": "r1"}},
    "obligations": {"o1": {"obligation_id": "o1", "materiality": "MATERIAL",
                           "trigger": {"observed": True}, "status": "PENDING",
                           "required_before_claim_refs": ["c1"]}},
}, "D1: obligation both referenced AND bound is evaluated once, still blocks (no inconsistent semantics)")

add("C1-D1-06-bound-failed-non-completion", "ADVERSARIAL", "BLOCK", {
    "eval_time": "2026-01-01",
    "claim": {"claim_id": "c1", "status": "SUPPORTED", "claim_type": "FACT",
              "support_relation_refs": ["s1"], "scope": {}},
    "support_registry": {"s1": {"support_id": "s1", "claim_ref": "c1", "support_status": "SUPPORTS",
                                "evidence_refs": ["e1"]}},
    "evidence_registry": {"e1": {"evidence_id": "e1", "root_provenance": "r1"}},
    "obligations": {"o1": {"obligation_id": "o1", "materiality": "MATERIAL",
                           "trigger": {"observed": True}, "status": "FAILED",
                           "required_before_claim_refs": ["c1"]}},
}, "D1: bound FAILED obligation also blocks a non-completion claim")

# ============================ D2: id-less top-level support ================
add("C1-D2-01-idless-top-level-support", "POSITIVE", "OK", {
    "eval_time": "2026-01-01",
    "support": {"support_status": "SUPPORTS", "claim_ref": "c1", "evidence_refs": ["e1"]},
}, "D2: standalone id-less top-level support is legitimate (exact P10 case)")

add("C1-D2-02-top-level-support-with-id", "POSITIVE", "OK", {
    "eval_time": "2026-01-01",
    "support": {"support_id": "s1", "support_status": "SUPPORTS", "evidence_refs": ["e1"]},
}, "D2: top-level support with id remains legitimate (exact P11 case)")

add("C1-D2-03-idless-cannot-resolve-ref", "ADVERSARIAL", "BLOCK", {
    "eval_time": "2026-01-01",
    "claim": {"claim_id": "c1", "status": "SUPPORTED", "claim_type": "FACT",
              "support_relation_refs": ["s1"], "scope": {}},
    "support": {"support_status": "SUPPORTS", "claim_ref": "c1", "evidence_refs": ["e1"]},
}, "D2: claim referencing an id-less top-level support must NOT silently resolve -> BLOCK (SUPPORT_REF_UNRESOLVABLE)")

add("C1-D2-04-list-entry-without-id", "ADVERSARIAL", "BLOCK", {
    "eval_time": "2026-01-01",
    "obligations": [{"status": "SATISFIED"}],
}, "D2 regression guard: list-form registry entry without id remains REGISTRY_MALFORMED (P37)")

add("C1-D2-05-r12-key-ne-id", "ADVERSARIAL", "BLOCK", {
    "eval_time": "2026-01-01",
    "claim": {"claim_id": "c1", "status": "SUPPORTED", "claim_type": "FACT",
              "support_relation_refs": ["s1"], "scope": {}},
    "support_registry": {"s1": {"support_id": "sX", "claim_ref": "c1", "support_status": "SUPPORTS",
                                "evidence_refs": ["e1"]}},
    "evidence_registry": {"e1": {"evidence_id": "e1", "root_provenance": "r1"}},
}, "D2 regression guard: R12 dict key != inner id remains REGISTRY_MALFORMED (P35)")

# ============================ D3: independence composition =================
add("C1-D3-01-roots-no-registry-unknown", "POSITIVE", "UNKNOWN", {
    "eval_time": "2026-01-01",
    "claim": {"claim_id": "c1", "status": "SUPPORTED", "claim_type": "FACT",
              "support_relation_refs": ["s1"], "scope": {}},
    "support_registry": {"s1": {"support_id": "s1", "claim_ref": "c1", "support_status": "SUPPORTS",
                                "evidence_refs": ["e1"],
                                "independence_basis": {"claimed_independent_count": 2,
                                                       "root_provenance": ["r1", "r2"]}}},
    "evidence_registry": {"e1": {"evidence_id": "e1", "root_provenance": "r1"}},
}, "D3: valid root_provenance + absent root registry -> UNKNOWN (exact P16 case)")

add("C1-D3-02-roots-distinct-origins-ok", "POSITIVE", "OK", {
    "eval_time": "2026-01-01",
    "claim": {"claim_id": "c1", "status": "SUPPORTED", "claim_type": "FACT",
              "support_relation_refs": ["s1"], "scope": {}},
    "support_registry": {"s1": {"support_id": "s1", "claim_ref": "c1", "support_status": "SUPPORTS",
                                "evidence_refs": ["e1"],
                                "independence_basis": {"claimed_independent_count": 2,
                                                       "root_provenance": ["r1", "r2"]}}},
    "evidence_registry": {"e1": {"evidence_id": "e1", "root_provenance": "r1"}},
    "root_registry": {"r1": {"root_id": "r1", "actual_origin": "O1"}, "r2": {"root_id": "r2", "actual_origin": "O2"}},
}, "D3: roots + distinct registered actual origins -> OK (exact P17 case)")

add("C1-D3-03-roots-collapse", "ADVERSARIAL", "BLOCK", {
    "eval_time": "2026-01-01",
    "claim": {"claim_id": "c1", "status": "SUPPORTED", "claim_type": "FACT",
              "support_relation_refs": ["s1"], "scope": {}},
    "support_registry": {"s1": {"support_id": "s1", "claim_ref": "c1", "support_status": "SUPPORTS",
                                "evidence_refs": ["e1"],
                                "independence_basis": {"claimed_independent_count": 2,
                                                       "root_provenance": ["r1", "r2"]}}},
    "evidence_registry": {"e1": {"evidence_id": "e1", "root_provenance": "r1"}},
    "root_registry": {"r1": {"root_id": "r1", "actual_origin": "ORIGIN-X"},
                      "r2": {"root_id": "r2", "actual_origin": "ORIGIN-X"}},
}, "D3: multiple roots resolving to the same actual origin -> BLOCK INDEPENDENCE_OVERCLAIMED")

add("C1-D3-04-claimed-gt-root-strings", "ADVERSARIAL", "BLOCK", {
    "eval_time": "2026-01-01",
    "claim": {"claim_id": "c1", "status": "SUPPORTED", "claim_type": "FACT",
              "support_relation_refs": ["s1"], "scope": {}},
    "support_registry": {"s1": {"support_id": "s1", "claim_ref": "c1", "support_status": "SUPPORTS",
                                "evidence_refs": ["e1"],
                                "independence_basis": {"claimed_independent_count": 3,
                                                       "root_provenance": ["r1", "r2"]}}},
    "evidence_registry": {"e1": {"evidence_id": "e1", "root_provenance": "r1"}},
}, "D3: declared count > distinct root strings -> BLOCK INDEPENDENCE_OVERCLAIMED (exact P14 case)")

add("C1-D3-05-claimed-without-roots", "ADVERSARIAL", "BLOCK", {
    "eval_time": "2026-01-01",
    "claim": {"claim_id": "c1", "status": "SUPPORTED", "claim_type": "FACT",
              "support_relation_refs": ["s1"], "scope": {}},
    "support_registry": {"s1": {"support_id": "s1", "claim_ref": "c1", "support_status": "SUPPORTS",
                                "evidence_refs": ["e1"],
                                "independence_basis": {"claimed_independent_count": 1,
                                                       "root_provenance": []}}},
    "evidence_registry": {"e1": {"evidence_id": "e1", "root_provenance": "r1"}},
}, "D3: claimed independence without root provenance -> BLOCK (P15/A6 family)")

add("C1-D3-06-legacy-source-origins-coherent", "POSITIVE", "OK", {
    "eval_time": "2026-01-01",
    "claim": {"claim_id": "c1", "status": "SUPPORTED", "claim_type": "FACT",
              "support_relation_refs": ["s1"], "scope": {}},
    "support_registry": {"s1": {"support_id": "s1", "claim_ref": "c1", "support_status": "SUPPORTS",
                                "evidence_refs": ["e1"],
                                "independence_basis": {"claimed_independent_count": 2,
                                                       "source_origins": ["A", "B"],
                                                       "root_provenance": ["r1", "r2"]}}},
    "evidence_registry": {"e1": {"evidence_id": "e1", "root_provenance": "r1"}},
    "root_registry": {"r1": {"root_id": "r1", "actual_origin": "O1"}, "r2": {"root_id": "r2", "actual_origin": "O2"}},
}, "D3: legacy source_origins + root_provenance + distinct registry origins -> OK (coherent, root authoritative)")

add("C1-D3-07-root-authoritative-over-legacy", "POSITIVE", "OK", {
    "eval_time": "2026-01-01",
    "claim": {"claim_id": "c1", "status": "SUPPORTED", "claim_type": "FACT",
              "support_relation_refs": ["s1"], "scope": {}},
    "support_registry": {"s1": {"support_id": "s1", "claim_ref": "c1", "support_status": "SUPPORTS",
                                "evidence_refs": ["e1"],
                                "independence_basis": {"claimed_independent_count": 2,
                                                       "source_origins": ["A"],
                                                       "root_provenance": ["r1", "r2"]}}},
    "evidence_registry": {"e1": {"evidence_id": "e1", "root_provenance": "r1"}},
    "root_registry": {"r1": {"root_id": "r1", "actual_origin": "O1"}, "r2": {"root_id": "r2", "actual_origin": "O2"}},
}, "D3: legacy-inadequate source_origins + adequate roots + registry -> OK (root representation authoritative, deterministic)")


def get_d1d2d3_controls():
    return copy.deepcopy(CONTROLS)
