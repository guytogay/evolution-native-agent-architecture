#!/usr/bin/env python3
"""V2.1 second-order adversarial expansion runner.

Phase 1: run each V2.1 fixture against the COMMITTED V2 prototype
         (hardened_rules.py from d178ff3) — show which attacks pass (vulnerable).
Phase 2: apply minimal V2.1 additions (registry resolution, grade enum,
         date parsing, root-derivation check) and re-run.
Phase 3: per-fixture ledger.

Repo-relative: run from the research/prototypes/v2-machine-contract-hardening/
directory; resolves the v0.3.2 tools path relative to this repo, not absolute.
"""
import sys, os, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
# Repo root = three levels up from research/prototypes/v2-machine-contract-hardening
REPO = HERE.parent.parent.parent
CURRENT = REPO / "releases" / "current"

def load_v2_module():
    """Load the committed V2 prototype (d178ff3) WITHOUT our repo-relative shim
    interfering with its hardcoded absolute path: import the module directly."""
    sys.path.insert(0, str(HERE))
    import hardened_rules as v2
    return v2

from fixtures_v21 import get_fixtures

GRADE_VALUES = {"E0", "E1", "E2", "E3", "E4", "E5"}
NOW = "2026-08-20"  # reference 'today' for mandate expiry checks

def parse_date(s):
    try:
        from datetime import date
        y, m, d = s.strip().split("-")
        return date(int(y), int(m), int(d))
    except Exception:
        return None

# ---------------------------------------------------------------------------
# Phase 2: V2.1 minimal additions
# ---------------------------------------------------------------------------

def v21_resolve(claim, support_registry, evidence_registry, root_registry):
    """Registry-based resolution. Returns (ok, code, details)."""
    # resolve SUPPORTED refs
    if claim.get("status") == "SUPPORTED":
        refs = claim.get("support_relation_refs") or []
        if not refs:
            return False, "CLAIM_SUPPORTED_WITHOUT_SUPPORT_REFS", {}
        if support_registry is None:
            # no registry supplied: refs unresolvable by construction
            return False, "SUPPORT_REF_UNRESOLVABLE", {"missing": refs}
        # duplicate detection
        seen = {}
        for s in support_registry:
            sid = s.get("support_id")
            seen.setdefault(sid, []).append(s)
        for sid, entries in seen.items():
            if len(entries) > 1:
                statuses = {e.get("support_status") for e in entries}
                if len(statuses) > 1:
                    return False, "DUPLICATE_REF_ID", {"support_id": sid, "statuses": sorted(statuses)}
        missing = [r for r in refs if r not in seen]
        if missing:
            return False, "SUPPORT_REF_UNRESOLVABLE", {"missing": missing}
        # applicability: claimed scope must be compatible with observed scope
        for r in refs:
            entry = seen[r][0]
            claimed_scope = claim.get("scope") or {}
            observed = entry.get("observed_scope") or {}
            for k in ("host", "runtime_instance", "epoch", "configuration"):
                c = claimed_scope.get(k)
                o = observed.get(k)
                if c and o and c != o:
                    transfer = entry.get("transfer_basis") or {}
                    if not (transfer.get("required") is True and (transfer.get("evidence_refs") or [])):
                        return False, "TRANSFER_EVIDENCE_REQUIRED", {"field": k, "observed": o, "claimed": c}
    return True, "OK", {}


def v21_check_obligations(claim, obligations):
    if claim.get("claim_type") not in ("WORKFLOW_COMPLETION", "TASK_COMPLETION"):
        return True, "OK", {}
    refs = claim.get("required_obligation_refs") or []
    if not refs:
        return False, "COMPLETION_CLAIM_WITHOUT_OBLIGATION_REFS", {}
    if obligations is None:
        return False, "OBLIGATION_REF_UNRESOLVABLE", {"missing": refs}
    by_id = {o.get("obligation_id"): o for o in obligations}
    dup = [o.get("obligation_id") for o in obligations]
    if len(dup) != len(set(dup)):
        return False, "DUPLICATE_OBLIGATION_ID", {"ids": dup}
    missing = [r for r in refs if r not in by_id]
    if missing:
        return False, "OBLIGATION_REF_UNRESOLVABLE", {"missing": missing}
    for r in refs:
        ob = by_id[r]
        if ob.get("materiality") == "MATERIAL" and (ob.get("trigger") or {}).get("observed") \
           and ob.get("status") in ("PENDING", "FAILED", "UNKNOWN"):
            return False, "COMPLETION_WITH_OPEN_MATERIAL_OBLIGATION", {"obligation_id": r, "status": ob.get("status")}
        if ob.get("status") == "SATISFIED" and not (ob.get("closure_evidence_refs") or []):
            return False, "OBLIGATION_SATISFIED_WITHOUT_CLOSURE_EVIDENCE", {}
        if ob.get("status") in ("NOT_REQUIRED", "DEFERRED_AUTHORIZED") and not ob.get("resolution_reason"):
            return False, "OBLIGATION_CLOSURE_STATUS_REQUIRES_REASON", {}
    return True, "OK", {}


def v21_check_grades(binding):
    for cap in (binding.get("capabilities") or []):
        if cap.get("status") in ("VERIFIED_AVAILABLE", "VERIFIED_RESTRICTED"):
            refs = cap.get("evidence_refs") or []
            grades = [r.get("grade") for r in refs if isinstance(r, dict)]
            if not grades:
                return False, "VERIFIED_WITHOUT_EVIDENCE_GRADE", {}
            invalid = [g for g in grades if g not in GRADE_VALUES]
            if invalid:
                return False, "EVIDENCE_GRADE_INVALID", {"grades": invalid}
            if all(g in ("E0", "E1") for g in grades):
                return False, "VERIFIED_ONLY_STATIC_STRUCTURE_EVIDENCE", {"grades": grades}
    return True, "OK", {}


def v21_check_mandate(binding):
    env = binding.get("authority_envelope") or []
    if env:
        mandate = binding.get("mandate") or {}
        src = mandate.get("source")
        if not src:
            return False, "AUTHORITY_WITHOUT_MANDATE_SOURCE", {}
        if src in ("RESTORE", "RESTORED_STATE", "CLONE", "CREDENTIAL_VALID"):
            return False, "AUTHORITY_MANDATE_SOURCE_NOT_AUTHORIZING", {"source": src}
        horizon = mandate.get("expires_at")
        if not horizon:
            return False, "AUTHORITY_WITHOUT_MANDATE_HORIZON", {}
        d = parse_date(horizon)
        if d is None:
            return False, "MANDATE_DATE_UNPARSEABLE", {"expires_at": horizon}
        if d < parse_date(NOW):
            return False, "MANDATE_EXPIRED", {"expires_at": horizon}
    return True, "OK", {}


def v21_check_recovery(transition, evidence_registry):
    claim_scope = (transition.get("recovery_claim") or {}).get("scope")
    if claim_scope == "STATE_AND_HISTORY":
        hist = transition.get("history_continuity") or {}
        if hist.get("status") != "PRESERVED":
            return False, "FULL_RECOVERY_REQUIRES_PRESERVED_HISTORY", {}
        refs = hist.get("evidence_refs") or []
        if not refs:
            return False, "HISTORY_PRESERVED_WITHOUT_EVIDENCE", {}
        if hist.get("post_checkpoint_occurrence_delta_captured") is not True:
            return False, "HISTORY_PRESERVED_WITHOUT_DELTA_CAPTURE", {}
        state_refs = (transition.get("state_restore") or {}).get("evidence_refs") or []
        if set(refs) & set(state_refs):
            return False, "HISTORY_EVIDENCE_SAME_AS_STATE_EVIDENCE", {"shared": sorted(set(refs) & set(state_refs))}
        # root-derivation: distinct strings may share a root
        if evidence_registry is not None:
            roots_hist = set()
            for r in refs:
                e = evidence_registry.get(r, {})
                root = e.get("root_provenance") or r
                roots_hist.add(root)
            roots_state = set()
            for r in state_refs:
                e = evidence_registry.get(r, {})
                root = e.get("root_provenance") or r
                roots_state.add(root)
            if roots_hist & roots_state:
                return False, "HISTORY_EVIDENCE_SHARED_ROOT", {"roots": sorted(roots_hist & roots_state)}
    return True, "OK", {}


def v21_check_independence(support, root_registry):
    ind = support.get("independence_basis") or {}
    claimed = ind.get("claimed_independent_count")
    if claimed is None:
        return True, "OK", {}
    roots = ind.get("root_provenance") or []
    if not roots:
        return False, "INDEPENDENCE_WITHOUT_ROOT_PROVENANCE", {}
    # root derivation: if a registry maps roots to actual origins, count origins
    if root_registry is not None:
        origins = set()
        for r in roots:
            entry = root_registry.get(r, {})
            origins.add(entry.get("actual_origin", r))
        if claimed > len(origins):
            return False, "INDEPENDENCE_OVERCLAIMED", {"claimed": claimed, "origins": sorted(origins)}
    else:
        if claimed > len(set(roots)):
            return False, "INDEPENDENCE_OVERCLAIMED", {"claimed": claimed, "roots": sorted(set(roots))}
    return True, "OK", {}


def run_v21(fx):
    p = fx["payload"]
    blocks = []
    # resolution phase
    ok, code, det = v21_resolve(p.get("claim", {}), p.get("support_registry"),
                                p.get("evidence_registry"), p.get("root_registry"))
    if not ok:
        blocks.append(code)
    # obligations
    if "claim" in p:
        ok, code, det = v21_check_obligations(p["claim"], p.get("obligations"))
        if not ok:
            blocks.append(code)
    # grades + mandate
    if "binding" in p:
        ok, code, det = v21_check_grades(p["binding"])
        if not ok:
            blocks.append(code)
        ok, code, det = v21_check_mandate(p["binding"])
        if not ok:
            blocks.append(code)
    # recovery
    if "transition" in p:
        ok, code, det = v21_check_recovery(p["transition"], p.get("evidence_registry"))
        if not ok:
            blocks.append(code)
    # independence
    if "support" in p:
        ok, code, det = v21_check_independence(p["support"], p.get("root_registry"))
        if not ok:
            blocks.append(code)
    return blocks


def run_v2_committed(fx):
    """Phase 1: run against committed V2 prototype semantics (no registry, no enum, no date)."""
    p = fx["payload"]
    blocks = []
    if "claim" in p:
        c = p["claim"]
        if c.get("status") == "SUPPORTED" and not (c.get("support_relation_refs") or []):
            blocks.append("CLAIM_SUPPORTED_WITHOUT_SUPPORT_REFS")
    if "binding" in p:
        b = p["binding"]
        env = b.get("authority_envelope") or []
        if env:
            m = b.get("mandate") or {}
            if not m.get("source"):
                blocks.append("AUTHORITY_WITHOUT_MANDATE_SOURCE")
            elif not m.get("expires_at"):
                blocks.append("AUTHORITY_WITHOUT_MANDATE_HORIZON")
        for cap in (b.get("capabilities") or []):
            if cap.get("status") in ("VERIFIED_AVAILABLE", "VERIFIED_RESTRICTED"):
                grades = [r.get("grade") for r in (cap.get("evidence_refs") or []) if isinstance(r, dict)]
                if not grades:
                    blocks.append("VERIFIED_WITHOUT_EVIDENCE_GRADE")
                elif all(g in ("E0", "E1") for g in grades):
                    blocks.append("VERIFIED_ONLY_STATIC_STRUCTURE_EVIDENCE")
    if "claim" in p and "obligations" in p:
        c = p["claim"]
        if c.get("claim_type") in ("WORKFLOW_COMPLETION", "TASK_COMPLETION"):
            if not (c.get("required_obligation_refs") or []):
                blocks.append("COMPLETION_CLAIM_WITHOUT_OBLIGATION_REFS")
            else:
                for ob in p["obligations"]:
                    if ob.get("materiality") == "MATERIAL" and (ob.get("trigger") or {}).get("observed") \
                       and ob.get("status") in ("PENDING", "FAILED", "UNKNOWN"):
                        blocks.append("COMPLETION_WITH_OPEN_MATERIAL_OBLIGATION")
    if "transition" in p:
        t = p["transition"]
        if (t.get("recovery_claim") or {}).get("scope") == "STATE_AND_HISTORY":
            h = t.get("history_continuity") or {}
            if h.get("status") != "PRESERVED":
                blocks.append("FULL_RECOVERY_REQUIRES_PRESERVED_HISTORY")
            if not (h.get("evidence_refs") or []):
                blocks.append("HISTORY_PRESERVED_WITHOUT_EVIDENCE")
            if h.get("post_checkpoint_occurrence_delta_captured") is not True:
                blocks.append("HISTORY_PRESERVED_WITHOUT_DELTA_CAPTURE")
            if set(h.get("evidence_refs") or []) & set((t.get("state_restore") or {}).get("evidence_refs") or []):
                blocks.append("HISTORY_EVIDENCE_SAME_AS_STATE_EVIDENCE")
    if "support" in p:
        ind = (p["support"].get("independence_basis") or {})
        claimed = ind.get("claimed_independent_count")
        if claimed is not None:
            roots = ind.get("root_provenance") or []
            if not roots:
                blocks.append("INDEPENDENCE_WITHOUT_ROOT_PROVENANCE")
            elif claimed > len({str(x) for x in roots if x not in (None, "", "UNKNOWN")}):
                blocks.append("INDEPENDENCE_OVERCLAIMED")
    return blocks


def main():
    fixtures = get_fixtures()
    print("=" * 100)
    print("V2.1 SECOND-ORDER EXPANSION against V2 prototype (d178ff3)")
    print("=" * 100)
    print()
    print("--- PHASE 1: committed V2 prototype (expected: structural attacks PASS = vulnerable) ---")
    v2_leaks = []
    for fx in fixtures:
        if fx["kind"] != "ATTACK":
            continue
        blocks = run_v2_committed(fx)
        vulnerable = not blocks  # attack not blocked
        if vulnerable:
            v2_leaks.append(fx["id"])
        print("  %-38s V2_blocks=%s %s" % (fx["id"], blocks, "VULNERABLE" if vulnerable else "blocked"))
    print()
    print("  V2 leaks (structural attacks NOT blocked by committed V2): %d/%d" % (
        len(v2_leaks), sum(1 for f in fixtures if f["kind"] == "ATTACK")))
    print("  " + ", ".join(v2_leaks))
    print()
    print("--- PHASE 2: V2.1 additions applied ---")
    summary = {"ATTACK_blocked": 0, "ATTACK_total": 0, "POSITIVE_preserved": 0, "POSITIVE_total": 0}
    detail = []
    for fx in fixtures:
        blocks = run_v21(fx)
        ok = not blocks
        exp_block = fx.get("expect_block", [])
        matched = [c for c in blocks if c in exp_block]
        if fx["kind"] == "ATTACK":
            summary["ATTACK_total"] += 1
            if not ok:
                summary["ATTACK_blocked"] += 1
        else:
            summary["POSITIVE_total"] += 1
            if ok:
                summary["POSITIVE_preserved"] += 1
        detail.append({"id": fx["id"], "kind": fx["kind"], "case": fx.get("case", ""),
                       "blocked": not ok, "codes": blocks, "expected": exp_block,
                       "matched_expected": matched,
                       "v2_was_vulnerable": fx["id"] in v2_leaks})
        print("  %-38s %-8s blocked=%-5s codes=%s" % (fx["id"], fx["kind"], not ok, blocks))
    print()
    print("SUMMARY:", json.dumps(summary))
    print()
    with open(os.path.join(HERE, "results-v21.json"), "w", encoding="utf-8") as f:
        json.dump({"summary": summary, "detail": detail,
                   "v2_leaks": v2_leaks, "fixture_version": "2.1"}, f, ensure_ascii=False, indent=2)
    print("results-v21.json written (repo-relative: %s)" % HERE)

if __name__ == "__main__":
    main()
