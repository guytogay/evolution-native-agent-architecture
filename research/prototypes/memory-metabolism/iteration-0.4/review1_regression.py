#!/usr/bin/env python3
"""Regression fixtures derived from the first fresh independent review of iteration 0.3.

These fixtures preserve the review findings as tests against iteration 0.4.
They are not proof of the broader semantic properties.
"""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("mm04", HERE / "validate_memory_metabolism.py")
mm = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(mm)


def expect(name, value, valid):
    errors = mm.validate_document(value)
    got = not errors
    print(name, "VALID" if got else "INVALID")
    for e in errors:
        print("  -", e)
    assert got is valid, (name, errors)


def main():
    count = 0

    old = {
        "record_id": "kb-old", "layer": "KNOWLEDGE", "claim_type": "BELIEF",
        "content": "old endpoint", "source_roots": ["inv:t1"],
        "access_scope": ["project:ena"],
        "validity": {"mode": "CURRENT_STATE", "revalidate_before_material_use": True},
    }
    new = copy.deepcopy(old)
    new.update({"record_id": "kb-new", "content": "new endpoint",
                "source_roots": ["inv:t2"], "supersedes": ["kb-old"]})

    # Reviewer C13 / F1.
    p = {
        "projection_id": "p", "actor_scopes": ["project:ena"],
        "retrieved_record_ids": ["kb-old"], "used_record_ids": ["kb-old"],
        "revalidated_record_ids": ["kb-old"], "historical_use_record_ids": ["kb-old"],
        "consequence": "MATERIAL", "authority_required": False,
    }
    expect("F1_used_historical_overlap", mm.doc([old, new], [p]), False); count += 1

    # Reviewer C10 / F2.
    secret = mm.ev("ev-secret", scope=["secret:board"])
    public = mm.cm("cm-public", "ev-secret", scope=["public"])
    expect("F2_silent_scope_relaxation", mm.doc([secret, public]), False); count += 1
    declassified = copy.deepcopy(public)
    declassified["access_scope_reconciliation"] = {
        "mode": "SANITIZED_DERIVATION",
        "external_basis": "declassification:review-1",
    }
    expect("F2_explicit_sanitization", mm.doc([secret, declassified]), True); count += 1

    # Reviewer C11 / F3.
    secret_old = copy.deepcopy(old)
    secret_old["access_scope"] = ["secret:board"]
    ph = copy.deepcopy(p)
    ph["used_record_ids"] = []
    ph["revalidated_record_ids"] = []
    expect("F3_historical_access_scope", mm.doc([secret_old, new], [ph]), False); count += 1

    # Reviewer C3 / F5.
    a = mm.ev("ev-a", "trace:a")
    b = mm.ev("ev-b", "trace:b")
    a["relations"] = [{"type": "CONTRADICTS", "target": "ev-b"}]
    kb = {
        "record_id": "kb", "layer": "KNOWLEDGE", "claim_type": "BELIEF",
        "content": "merged belief", "derived_from": ["ev-a", "ev-b"],
        "source_roots": ["trace:a", "trace:b"], "access_scope": ["project:ena"],
        "validity": {"mode": "CONDITIONAL", "revalidate_before_material_use": False},
    }
    expect("F5_knowledge_contradiction", mm.doc([a, b, kb]), False); count += 1

    # Reviewer C12 / FB-1.
    e = mm.ev()
    c1 = mm.cm()
    c2 = mm.cm("cm-2", "cm-1")
    expect("FB1_second_order_compilation", mm.doc([e, c1, c2]), True); count += 1

    # Reviewer F6 concrete challengeability path.
    red = mm.ev(status="LAWFULLY_REDACTED")
    c = mm.cm()
    expect("F6_redacted_full_challengeability", mm.doc([red, c]), False); count += 1
    c["challengeability"] = "DEGRADED"
    expect("F6_redacted_degraded_challengeability", mm.doc([red, c]), True); count += 1

    print(f"MEMORY_METABOLISM_REVIEW1_REGRESSION_PASS {count}")


if __name__ == "__main__":
    main()
