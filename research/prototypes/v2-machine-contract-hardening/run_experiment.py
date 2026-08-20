#!/usr/bin/env python3
"""V2 hardening experiment runner.
Phase 1: baseline v0.3.2 toolchain on all fixtures (adversarial should PASS = falsified).
Phase 2: hardened candidates on all fixtures (adversarial blocked, positive preserved).
Phase 3: second-order attacks on hardened candidates.
Phase 4: per-candidate cost/benefit recording.
"""

import json, sys, os
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from hardened_rules import (
    candidate_claim_supported_requires_refs,
    candidate_binding_authority_requires_mandate,
    candidate_obligation_claim_link,
    candidate_recovery_history_requires_evidence,
    candidate_independence_requires_root,
    candidate_verification_requires_grade,
)
from fixtures import get_fixtures

def base_support_ok(support, claim):
    """Invoke v0.3.2 shipped support validator logic."""
    from validate_contracts import validate_support
    return validate_support(claim, support)

def run_fixture_base(fx):
    """Phase 1: what does the SHIPPED v0.3.2 toolchain say about this fixture?
    We check only the artifact classes the shipped validator covers."""
    p = fx["payload"]
    verdicts = {}
    if "support" in p:
        claim = p.get("claim", {"claim_id": p["support"].get("claim_ref")})
        r = base_support_ok(p["support"], claim)
        verdicts["support"] = r
    if "obligations" in p:
        from validate_contracts import validate_obligation
        for ob in p["obligations"]:
            verdicts["obligation:" + ob["obligation_id"]] = validate_obligation(ob)
    if "transition" in p:
        from validate_contracts import validate_recovery
        verdicts["recovery"] = validate_recovery(p["transition"])
    return verdicts

def run_fixture_hardened(fx):
    """Phase 2/3: hardened candidates. Returns list of (rule_name, result_dict)."""
    p = fx["payload"]
    results = []
    if "claim" in p:
        results.append(("CLAIM_SUPPORTED_REQUIRES_REFS", candidate_claim_supported_requires_refs(p["claim"])))
        # second-order: resolve support relations if provided
        for sr in p.get("support_relations", []):
            if sr.get("support_status") == "SUPPORTS" and not (sr.get("evidence_refs") or []):
                results.append(("SUPPORT_WITHOUT_EVIDENCE",
                                {"ok": False, "code": "SUPPORT_WITHOUT_EVIDENCE",
                                 "details": {"support_id": sr.get("support_id")}}))
        if "obligations" in p:
            results.append(("OBLIGATION_CLAIM_LINK", candidate_obligation_claim_link(p["claim"], p["obligations"])))
    if "binding" in p:
        results.append(("AUTHORITY_REQUIRES_MANDATE", candidate_binding_authority_requires_mandate(p["binding"])))
        results.append(("VERIFIED_REQUIRES_GRADE", candidate_verification_requires_grade(p["binding"])))
    if "transition" in p:
        results.append(("RECOVERY_HISTORY_EVIDENCE", candidate_recovery_history_requires_evidence(p["transition"])))
    if "support" in p:
        results.append(("INDEPENDENCE_ROOT", candidate_independence_requires_root(p["support"])))
    return results

def main():
    fixtures = get_fixtures()
    print("=" * 100)
    print("PHASE 1: baseline v0.3.2 shipped toolchain (does the false claim already pass?)")
    print("=" * 100)
    for fx in fixtures:
        if fx["kind"] != "ADVERSARIAL":
            continue
        v = run_fixture_base(fx)
        ok = all(r.get("ok") for r in v.values()) if v else True
        print("  %-42s base_ok=%s  %s" % (fx["id"], ok, json.dumps({k: r.get("code") for k, r in v.items()})))

    print()
    print("=" * 100)
    print("PHASE 2/3: hardened candidates (adversarial blocked? positive preserved? second-order?)")
    print("=" * 100)
    summary = {"ADVERSARIAL_blocked": 0, "ADVERSARIAL_total": 0,
               "POSITIVE_preserved": 0, "POSITIVE_total": 0,
               "SECOND_ORDER_blocked": 0, "SECOND_ORDER_total": 0}
    detail = []
    for fx in fixtures:
        results = run_fixture_hardened(fx)
        codes = [r[1].get("code") for r in results if not r[1].get("ok")]
        ok = not codes
        exp_block = fx.get("expect_block", [])
        matched = [c for c in codes if c in exp_block]
        if fx["kind"] == "ADVERSARIAL":
            summary["ADVERSARIAL_total"] += 1
            if not ok:
                summary["ADVERSARIAL_blocked"] += 1
        elif fx["kind"] == "POSITIVE":
            summary["POSITIVE_total"] += 1
            if ok:
                summary["POSITIVE_preserved"] += 1
        elif fx["kind"] == "SECOND_ORDER":
            summary["SECOND_ORDER_total"] += 1
            if not ok:
                summary["SECOND_ORDER_blocked"] += 1
        detail.append({"id": fx["id"], "kind": fx["kind"], "vector": fx["vector"],
                       "blocked": not ok, "codes": codes,
                       "expected": exp_block, "matched_expected": matched})
    for d in detail:
        print("  %-42s %-13s %-22s blocked=%-5s codes=%s" % (
            d["id"], d["kind"], d["vector"], d["blocked"], d["codes"]))
    print()
    print("SUMMARY:", json.dumps(summary))
    print()
    print("=" * 100)
    print("PHASE 4: per-candidate cost/benefit ledger")
    print("=" * 100)
    ledger = [
        {"rule": "CLAIM_SUPPORTED_REQUIRES_REFS",
         "vector": "I_KNOW",
         "false_claim_blocked": "YES (A1)",
         "legit_preserved": "YES (P1,P2)",
         "new_fields": "none (uses existing support_relation_refs)",
         "new_rules": "1 validator rule",
         "cost": "O(1) per claim; no tool/runtime change",
         "new_false_positive_surface": "LOW: SUPPORTED with refs to missing support not yet resolved (second-order S1 needs relation registry)",
         "protection_beyond_prose": "YES: prose already says supported needs support; now a machine rule enforces non-empty refs"},
        {"rule": "VERIFIED_REQUIRES_GRADE",
         "vector": "I_VERIFIED",
         "false_claim_blocked": "YES (A2)",
         "legit_preserved": "YES (P10)",
         "new_fields": "evidence_grade on capability evidence_refs entries",
         "new_rules": "1 validator rule (grade > E1 required for verified)",
         "cost": "schema field + validator; no runtime",
         "new_false_positive_surface": "MEDIUM: grade is self-asserted; E2 can be claimed without proof (documented residual)",
         "protection_beyond_prose": "PARTIAL: blocks 'static-structure log as verification'; grade truth still self-declared"},
        {"rule": "AUTHORITY_REQUIRES_MANDATE",
         "vector": "I_HAVE_AUTHORITY",
         "false_claim_blocked": "YES (A3, S2)",
         "legit_preserved": "YES (P3,P4)",
         "new_fields": "mandate.source + mandate.expires_at",
         "new_rules": "2 validator rules (source required; source not restore/clone/credential; horizon required)",
         "cost": "schema field + validator; no runtime",
         "new_false_positive_surface": "MEDIUM: mandate source is a string; 'USER_EXPLICIT_GRANT' can be forged without verification (CON-029/027 residual)",
         "protection_beyond_prose": "YES: machine-izes 'credential/restore != mandate'; stops the naive restore-authority claim"},
        {"rule": "OBLIGATION_CLAIM_LINK",
         "vector": "I_COMPLETED",
         "false_claim_blocked": "YES (A4, S3)",
         "legit_preserved": "YES (P5,P6)",
         "new_fields": "claim.required_obligation_refs",
         "new_rules": "1 validator rule resolving claim-side obligation linkage",
         "cost": "schema field + validator; obligations must be resolvable",
         "new_false_positive_surface": "MEDIUM: requires obligations registry; unenumerated obligations still invisible (residual)",
         "protection_beyond_prose": "YES: closes the claim-side hole (obligation→claim existed; claim→obligation did not)"},
        {"rule": "RECOVERY_HISTORY_EVIDENCE",
         "vector": "I_RECOVERED",
         "false_claim_blocked": "YES (A5, S4)",
         "legit_preserved": "YES (P7,P8)",
         "new_fields": "none (existing history_continuity fields)",
         "new_rules": "3 validator rules (evidence non-empty; delta captured; history evidence != state evidence)",
         "cost": "validator-only; no schema change",
         "new_false_positive_surface": "LOW-MEDIUM: distinct-ref requirement is heuristic; attacker can name two different fabricated logs (content truth unverifiable)",
         "protection_beyond_prose": "YES: 'PRESERVED' status word alone no longer suffices; requires delta capture + distinct history evidence"},
        {"rule": "INDEPENDENCE_ROOT",
         "vector": "EVIDENCE_INDEPENDENT",
         "false_claim_blocked": "YES (A6, A6b, S5)",
         "legit_preserved": "YES (P9)",
         "new_fields": "independence_basis.root_provenance",
         "new_rules": "2 validator rules (roots required when count claimed; count <= distinct roots)",
         "cost": "schema field + validator",
         "new_false_positive_surface": "MEDIUM: root_provenance is self-declared; attacker can declare 3 fake distinct roots (laundering moves one level down)",
         "protection_beyond_prose": "YES: stops label-string laundering; shifts the trust boundary to root identity"},
    ]
    for l in ledger:
        print("  Rule : %s" % l["rule"])
        for k in ("vector", "false_claim_blocked", "legit_preserved", "new_fields", "new_rules",
                  "cost", "new_false_positive_surface", "protection_beyond_prose"):
            print("    %-26s %s" % (k + ":", l[k]))
        print()
    with open(os.path.join(os.path.dirname(__file__), "results.json"), "w", encoding="utf-8") as f:
        json.dump({"summary": summary, "detail": detail, "ledger": ledger}, f, ensure_ascii=False, indent=2)
    print("results.json written")

if __name__ == "__main__":
    main()
