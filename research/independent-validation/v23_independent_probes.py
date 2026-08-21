#!/usr/bin/env python3
"""Independent semantic probes for frozen ENA V2.3 candidate.

This file is NOT part of the frozen candidate. It is validation-only and imports
cumulative_contract.py from an explicitly supplied frozen checkout.

Usage:
  python v23_independent_probes.py <path-to-frozen-repo>
"""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

if len(sys.argv) != 2:
    raise SystemExit("usage: v23_independent_probes.py <frozen-repo>")

FROZEN = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(FROZEN / "research" / "prototypes" / "v2-machine-contract-hardening" / "v2.2"))
from cumulative_contract import evaluate  # noqa: E402

EVAL_TIME = date(2026, 8, 21)


def claim(cid="C", status="SUPPORTED", scope=None, ctype="OTHER", support_refs=None, obligation_refs=None):
    out = {
        "claim_id": cid,
        "claim_type": ctype,
        "subject": {"kind": "TASK", "id": "T"},
        "scope": scope or {"host": "H1"},
        "assertion": "independent validation probe",
        "status": status,
    }
    if support_refs is not None:
        out["support_relation_refs"] = support_refs
    if obligation_refs is not None:
        out["required_obligation_refs"] = obligation_refs
    return out


def support(sid="S", cref="C", observed=None, claimed=None, status="SUPPORTS", evidence=None, transfer=None):
    out = {
        "support_id": sid,
        "claim_ref": cref,
        "evidence_refs": evidence if evidence is not None else ["E"],
        "support_status": status,
        "observed_scope": observed if observed is not None else {"host": "H1"},
        "claimed_scope": claimed if claimed is not None else {"host": "H1"},
    }
    if transfer is not None:
        out["transfer_basis"] = transfer
    return out


def obligation(oid="O", status="SATISFIED", materiality="MATERIAL", observed=True, close=None, required_for=None):
    out = {
        "obligation_id": oid,
        "materiality": materiality,
        "trigger": {"rule_ref": "R", "observed": observed},
        "status": status,
    }
    if close is not None:
        out["closure_evidence_refs"] = close
    if required_for is not None:
        out["required_before_claim_refs"] = required_for
    return out


CASES = [
    {
        "id": "F1-support-target-mismatch",
        "independent_expected": "BLOCK",
        "why": "Resolved support must target the current claim; registry presence is not target resolution.",
        "fixture": {"payload": {
            "claim": claim("C-F1", support_refs=["S-F1"]),
            "support_registry": [support("S-F1", cref="C-OTHER")],
        }},
    },
    {
        "id": "F2-support-missing-observed-scope",
        "independent_expected": "BLOCK",
        "why": "A SUPPORTED material claim cannot inherit host applicability from evidence whose observed host is absent.",
        "fixture": {"payload": {
            "claim": claim("C-F2", scope={"host": "H1"}, support_refs=["S-F2"]),
            "support_registry": [support("S-F2", cref="C-F2", observed={})],
        }},
    },
    {
        "id": "F3-support-model-binding-mismatch",
        "independent_expected": "BLOCK",
        "why": "model_binding is an applicability boundary in the base contract but is omitted by resolved-support checking.",
        "fixture": {"payload": {
            "claim": claim("C-F3", scope={"host": "H1", "model_binding": "M2"}, support_refs=["S-F3"]),
            "support_registry": [support("S-F3", cref="C-F3", observed={"host": "H1", "model_binding": "M1"})],
        }},
    },
    {
        "id": "F4-transfer-basis-untyped-unresolved",
        "independent_expected": "BLOCK",
        "why": "Scope transfer needs a typed/evidenced transfer relation, not only a non-empty evidence string.",
        "fixture": {"payload": {
            "claim": claim("C-F4", scope={"host": "H2"}, support_refs=["S-F4"]),
            "support_registry": [support(
                "S-F4", cref="C-F4", observed={"host": "H1"}, claimed={"host": "H2"},
                transfer={"required": True, "evidence_refs": ["E-NONEXISTENT"]},
            )],
        }},
    },
    {
        "id": "F5-duplicate-support-same-status",
        "independent_expected": "BLOCK",
        "why": "Duplicate IDs remain ambiguous even when both entries carry the same support_status.",
        "fixture": {"payload": {
            "claim": claim("C-F5", support_refs=["S-DUP"]),
            "support_registry": [
                support("S-DUP", cref="C-F5", observed={"host": "H1"}, evidence=["E1"]),
                support("S-DUP", cref="C-F5", observed={"host": "H2"}, evidence=["E2"]),
            ],
        }},
    },
    {
        "id": "F6-resolved-support-invalid-status",
        "independent_expected": "BLOCK",
        "why": "A resolved support artifact with an unrecognized status cannot substantiate SUPPORTED.",
        "fixture": {"payload": {
            "claim": claim("C-F6", support_refs=["S-F6"]),
            "support_registry": [support("S-F6", cref="C-F6", status="GARBAGE")],
        }},
    },
    {
        "id": "F7-recovery-registry-present-refs-unresolved",
        "independent_expected": "BLOCK",
        "why": "Present registry with missing referenced evidence is a broken reference, not proof of distinct roots.",
        "fixture": {"payload": {
            "transition": {
                "transition_id": "RT-F7",
                "state_restore": {"target_checkpoint": "CP", "result": "SUCCESS", "evidence_refs": ["E-ST"]},
                "history_continuity": {"status": "PRESERVED", "post_checkpoint_occurrence_delta_captured": True, "evidence_refs": ["E-HI"]},
                "recovery_claim": {"claim_ref": "C-F7", "scope": "STATE_AND_HISTORY"},
            },
            "evidence_registry": {},
        }},
    },
    {
        "id": "F8-recovery-resolved-but-root-unknown",
        "independent_expected": "UNKNOWN",
        "why": "When artifacts resolve but root provenance is absent, root distinctness remains unknown.",
        "fixture": {"payload": {
            "transition": {
                "transition_id": "RT-F8",
                "state_restore": {"target_checkpoint": "CP", "result": "SUCCESS", "evidence_refs": ["E-ST"]},
                "history_continuity": {"status": "PRESERVED", "post_checkpoint_occurrence_delta_captured": True, "evidence_refs": ["E-HI"]},
                "recovery_claim": {"claim_ref": "C-F8", "scope": "STATE_AND_HISTORY"},
            },
            "evidence_registry": {"E-ST": {}, "E-HI": {}},
        }},
    },
    {
        "id": "F9-independence-root-refs-unresolved",
        "independent_expected": "BLOCK",
        "why": "A present root registry that lacks claimed root IDs cannot verify those roots.",
        "fixture": {"payload": {
            "support": {
                "support_id": "S-F9", "claim_ref": "C-F9", "evidence_refs": ["E1", "E2"],
                "support_status": "SUPPORTS", "observed_scope": {"host": "H1"}, "claimed_scope": {"host": "H1"},
                "independence_basis": {"claimed_independent_count": 2, "source_origins": ["A", "B"], "root_provenance": ["R1", "R2"]},
            },
            "root_registry": {},
        }},
    },
    {
        "id": "F10-independence-roots-unbound-to-evidence",
        "independent_expected": "BLOCK",
        "why": "Two independent roots cannot substantiate two observations when only one evidence reference is named and no mapping binds them.",
        "fixture": {"payload": {
            "support": {
                "support_id": "S-F10", "claim_ref": "C-F10", "evidence_refs": ["E1"],
                "support_status": "SUPPORTS", "observed_scope": {"host": "H1"}, "claimed_scope": {"host": "H1"},
                "independence_basis": {"claimed_independent_count": 2, "source_origins": ["A", "B"], "root_provenance": ["R1", "R2"]},
            },
            "root_registry": {"R1": {"actual_origin": "O1"}, "R2": {"actual_origin": "O2"}},
        }},
    },
    {
        "id": "F11-mandate-arbitrary-source",
        "independent_expected": "BLOCK",
        "why": "Authority requires a recognized/current authorizing mandate; blacklist-only source checking accepts arbitrary strings.",
        "fixture": {"payload": {
            "binding": {"binding_id": "B-F11", "agent": "me", "host": "H1", "route": ["r"],
                        "authority_envelope": ["approve stable admission"],
                        "mandate": {"source": "BANANA", "expires_at": "2999-01-01"}},
        }},
    },
    {
        "id": "F12-verified-evidence-unresolvable",
        "independent_expected": "BLOCK",
        "why": "VERIFIED_AVAILABLE cannot be certified by an E2 label attached to a non-resolved evidence reference.",
        "fixture": {"payload": {
            "binding": {"binding_id": "B-F12", "agent": "me", "host": "H1", "route": ["r"],
                        "capabilities": [{"id": "ENA-CAP-048", "status": "VERIFIED_AVAILABLE",
                                          "evidence_refs": [{"ref": "E-NONEXISTENT", "grade": "E2"}]}]},
        }},
    },
    {
        "id": "F13-obligation-closure-evidence-unresolvable",
        "independent_expected": "BLOCK",
        "why": "SATISFIED closure evidence must exist/resolvable for a completion claim; non-empty string alone is not closure evidence.",
        "fixture": {"payload": {
            "claim": claim("C-F13", ctype="WORKFLOW_COMPLETION", support_refs=["S-F13"], obligation_refs=["O-F13"]),
            "support_registry": [support("S-F13", cref="C-F13")],
            "obligations": [obligation("O-F13", close=["E-NONEXISTENT"], required_for=["C-F13"])],
        }},
    },
    {
        "id": "F14-contradictory-top-level-support-laundered",
        "independent_expected": "BLOCK",
        "why": "A contradictory support object must not be neutralized by a separate supportive registry entry for the same claim.",
        "fixture": {"payload": {
            "claim": claim("C-F14", support_refs=["S-F14"]),
            "support": support("S-TOP", cref="C-F14", status="CONTRADICTS"),
            "support_registry": [support("S-F14", cref="C-F14", status="SUPPORTS")],
        }},
    },
    {
        "id": "F15-support-relations-overwritten-by-registry",
        "independent_expected": "BLOCK",
        "why": "Parallel support surfaces that disagree must be reconciled; support_registry must not silently overwrite contradictory support_relations.",
        "fixture": {"payload": {
            "claim": claim("C-F15", support_refs=["S-F15"]),
            "support_relations": [support("S-F15", cref="C-F15", status="CONTRADICTS")],
            "support_registry": [support("S-F15", cref="C-F15", status="SUPPORTS")],
        }},
    },
    {
        "id": "L1-unrelated-open-obligation-noncompletion",
        "independent_expected": "OK",
        "why": "An open material obligation explicitly tied to another claim must not globally block an unrelated asserted claim.",
        "fixture": {"payload": {
            "claim": claim("C-L1", status="ASSERTED"),
            "obligations": [obligation("O-L1", status="PENDING", close=None, required_for=["C-OTHER"])],
        }},
    },
    {
        "id": "L2-narrow-completion-unrelated-open-obligation",
        "independent_expected": "OK",
        "why": "The core contract permits narrower truthful completion; an unrelated open obligation should not block a claim whose required obligation is satisfied.",
        "fixture": {"payload": {
            "claim": claim("C-L2", ctype="WORKFLOW_COMPLETION", support_refs=["S-L2"], obligation_refs=["O-SAT"]),
            "support_registry": [support("S-L2", cref="C-L2")],
            "obligations": [
                obligation("O-SAT", status="SATISFIED", close=["E-CLOSE"], required_for=["C-L2"]),
                obligation("O-OTHER", status="PENDING", close=None, required_for=["C-OTHER"]),
            ],
        }},
    },
]

CRASH_CASES = [
    {
        "id": "C1-root-registry-list-shape",
        "fixture": {"payload": {
            "support": {
                "support_id": "S-C1", "claim_ref": "C-C1", "evidence_refs": ["E1"],
                "support_status": "SUPPORTS", "observed_scope": {"host": "H1"}, "claimed_scope": {"host": "H1"},
                "independence_basis": {"claimed_independent_count": 1, "source_origins": ["A"], "root_provenance": ["R1"]},
            },
            "root_registry": [{"id": "R1", "actual_origin": "O1"}],
        }},
    },
    {
        "id": "C2-null-support-registry",
        "fixture": {"payload": {
            "claim": claim("C-C2", support_refs=["S-C2"]),
            "support_registry": None,
        }},
    },
]


def run():
    rows = []
    semantic_failures = 0
    for case in CASES:
        actual, codes = evaluate(case["fixture"], EVAL_TIME)
        mismatch = actual != case["independent_expected"]
        semantic_failures += int(mismatch)
        rows.append({
            "id": case["id"],
            "independent_expected": case["independent_expected"],
            "candidate_actual": actual,
            "codes": codes,
            "semantic_mismatch": mismatch,
            "why": case["why"],
        })

    crashes = []
    for case in CRASH_CASES:
        try:
            actual, codes = evaluate(case["fixture"], EVAL_TIME)
            crashes.append({"id": case["id"], "crashed": False, "candidate_actual": actual, "codes": codes})
        except Exception as exc:  # validation intentionally records candidate robustness failures
            crashes.append({"id": case["id"], "crashed": True, "exception": f"{type(exc).__name__}: {exc}"})

    out = {
        "validator_lineage": "independent of DSH candidate-author lineage",
        "frozen_candidate_ref": "8eb5a9afa4c560645b4c50dc24af7874ed54a4f2",
        "semantic_cases": rows,
        "semantic_mismatch_count": semantic_failures,
        "crash_cases": crashes,
        "crash_count": sum(1 for x in crashes if x["crashed"]),
    }
    print(json.dumps(out, indent=2))
    # These are regression assertions for the independent findings, not candidate acceptance criteria.
    assert semantic_failures >= 17, semantic_failures
    assert out["crash_count"] == 2, out["crash_count"]


if __name__ == "__main__":
    run()
