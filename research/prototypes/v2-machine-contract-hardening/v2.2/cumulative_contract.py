#!/usr/bin/env python3
"""V2.2 Cumulative Contract Composition & Closure — research prototype.

Composes ALL accepted V2 and V2.1 protections into ONE executable contract
surface, then replays every historical fixture cumulatively (never reset).

Design rules (user requirements):
- every reference must resolve to the correct artifact TYPE and target;
- resolved artifacts checked for status / scope / applicability where material;
- duplicate or ambiguous IDs rejected explicitly;
- missing registries must NOT silently degrade into trusting raw strings:
  declare FAIL_CLOSED or UNKNOWN explicitly;
- provenance/root checks must NOT fall back to self-asserted labels when the
  required registry is unavailable;
- authority expiry uses an EXPLICIT evaluation time, not a hardcoded date;
- the experiment calls the ACTUAL candidate implementations (base v0.3.2
  validator, V2 hardened_rules functions, V2.1 additions) — no manual proxy;
- all paths repo-relative and portable.

Success: one portable cumulative machine-contract candidate whose protections
remain valid when COMPOSED, not merely in isolation. A discovered composition
failure is valuable evidence.
"""
from __future__ import annotations
import sys, json
from pathlib import Path
from datetime import date

# ---------------------------------------------------------------------------
# Repo-relative path resolution (portable; no absolute paths)
#   In-repo layout: v2.2/ -> v2-machine-contract-hardening/ -> prototypes/ -> research/ -> repo
#   Workspace layout: proto/ (standalone) with repo clone at ../repo
# ---------------------------------------------------------------------------
HERE = Path(__file__).resolve().parent            # .../v2.2 or .../proto
PROTO_ROOT = HERE.parent                          # .../v2-machine-contract-hardening or workspace root
# find repo root: look for releases/current in ancestor chain
def _find_repo(start):
    cur = start
    for _ in range(8):
        if (cur / "releases" / "current" / "tools").exists():
            return cur
        cur = cur.parent
    return start.parent / "repo"  # workspace fallback: ../repo

REPO = _find_repo(HERE)
CURRENT_TOOLS = REPO / "releases" / "current" / "tools"

sys.path.insert(0, str(CURRENT_TOOLS))            # base v0.3.2 validator
# V2 hardened_rules: prefer repo's committed copy, fall back to workspace copy
sys.path.insert(0, str(REPO / "research" / "prototypes" / "v2-machine-contract-hardening"))
sys.path.insert(0, str(HERE))                     # workspace copy fallback
sys.path.insert(0, str(HERE))                     # V2.1/V2.2 additions

# --- actual base v0.3.2 validator (shipped) ---
from validate_contracts import validate_support, validate_obligation, validate_recovery

# --- actual V2 candidate functions (committed, d178ff3) ---
import hardened_rules as v2

# ---------------------------------------------------------------------------
# V2.1/V2.2 additions: typed resolution + explicit states
# ---------------------------------------------------------------------------
GRADES = {"E0", "E1", "E2", "E3", "E4", "E5"}

class VState:
    OK = "OK"
    BLOCK = "BLOCK"
    UNKNOWN = "UNKNOWN"

def parse_date(s):
    try:
        y, m, d = s.strip().split("-")
        return date(int(y), int(m), int(d))
    except Exception:
        return None

def _worst(states):
    """BLOCK > UNKNOWN > OK."""
    if any(s == VState.BLOCK for s in states):
        return VState.BLOCK
    if any(s == VState.UNKNOWN for s in states):
        return VState.UNKNOWN
    return VState.OK

def _typed_lookup(ref, registries, expected_type, ref_kind):
    """Resolve ref to the correct artifact TYPE. registries: dict type->list.
    Returns (state, code, detail). Explicit duplicate/ambiguity rejection."""
    reg = registries.get(expected_type)
    if reg is None:
        # registry for this type absent -> FAIL_CLOSED (cannot resolve)
        return VState.BLOCK, f"{ref_kind}_REF_UNRESOLVABLE", {"ref": ref, "reason": "registry_absent"}
    matches = [a for a in reg if a.get("id", a.get(a.get("id_field", "id"))) == ref] if False else [
        a for a in reg if a.get("id") == ref or a.get(a.get("id_field", "id")) == ref or a.get(a.get("_id_key", "id")) == ref]
    # fallback: try common id keys
    if not matches:
        matches = [a for a in reg if ref in a.values()]
    if not matches:
        return VState.BLOCK, f"{ref_kind}_REF_UNRESOLVABLE", {"ref": ref}
    if len(matches) > 1:
        # ambiguous: duplicate IDs with differing semantics -> explicit reject
        return VState.BLOCK, "DUPLICATE_REF_ID", {"ref": ref, "count": len(matches)}
    return VState.OK, "", {"resolved": matches[0]}


def resolve_support_refs(claim, registries):
    """SUPPORTED claim: support_relation_refs must resolve to SUPPORT artifacts."""
    if claim.get("status") != "SUPPORTED":
        return VState.OK, "", {}
    refs = claim.get("support_relation_refs") or []
    if not refs:
        return VState.BLOCK, "CLAIM_SUPPORTED_WITHOUT_SUPPORT_REFS", {}
    if "support" not in registries:
        # missing registry -> FAIL_CLOSED, do NOT trust raw strings
        return VState.BLOCK, "SUPPORT_REF_UNRESOLVABLE", {"refs": refs, "reason": "registry_absent"}
    support_reg = registries["support"]
    seen_ids = {}
    for s in support_reg:
        sid = s.get("support_id") or s.get("id")
        seen_ids.setdefault(sid, []).append(s)
    # duplicate/ambiguous
    for sid, entries in seen_ids.items():
        if len(entries) > 1 and len({e.get("support_status") for e in entries}) > 1:
            return VState.BLOCK, "DUPLICATE_REF_ID", {"support_id": sid}
    missing = [r for r in refs if r not in seen_ids]
    if missing:
        return VState.BLOCK, "SUPPORT_REF_UNRESOLVABLE", {"missing": missing}
    # resolved support must carry evidence (V2.1 SUPPORT_WITHOUT_EVIDENCE preserved)
    for r in refs:
        entry = seen_ids[r][0]
        if not (entry.get("evidence_refs") or []):
            return VState.BLOCK, "SUPPORT_WITHOUT_EVIDENCE", {"support_id": r}
    # applicability on resolved artifacts
    for r in refs:
        entry = seen_ids[r][0]
        observed = entry.get("observed_scope") or {}
        claimed = claim.get("scope") or {}
        for k in ("host", "runtime_instance", "epoch", "configuration", "environment"):
            c = claimed.get(k)
            o = observed.get(k)
            if c and o and c != o:
                transfer = entry.get("transfer_basis") or {}
                if not (transfer.get("required") is True and (transfer.get("evidence_refs") or [])):
                    return VState.BLOCK, "TRANSFER_EVIDENCE_REQUIRED", {"field": k, "observed": o, "claimed": c}
        # resolved support must not contradict
        if entry.get("support_status") == "CONTRADICTS":
            return VState.BLOCK, "RESOLVED_SUPPORT_CONTRADICTS", {"support_id": r}
    return VState.OK, "", {}


def resolve_obligation_refs(claim, registries):
    """Completion claim: required_obligation_refs must resolve to OBLIGATION artifacts."""
    if claim.get("claim_type") not in ("WORKFLOW_COMPLETION", "TASK_COMPLETION"):
        return VState.OK, "", {}
    refs = claim.get("required_obligation_refs") or []
    if not refs:
        return VState.BLOCK, "COMPLETION_CLAIM_WITHOUT_OBLIGATION_REFS", {}
    if "obligation" not in registries:
        return VState.BLOCK, "OBLIGATION_REF_UNRESOLVABLE", {"refs": refs, "reason": "registry_absent"}
    ob_reg = registries["obligation"]
    by_id = {}
    for o in ob_reg:
        oid = o.get("obligation_id") or o.get("id")
        by_id.setdefault(oid, []).append(o)
    for oid, entries in by_id.items():
        if len(entries) > 1:
            return VState.BLOCK, "DUPLICATE_OBLIGATION_ID", {"obligation_id": oid}
    missing = [r for r in refs if r not in by_id]
    if missing:
        return VState.BLOCK, "OBLIGATION_REF_UNRESOLVABLE", {"missing": missing}
    for r in refs:
        ob = by_id[r][0]
        if ob.get("materiality") == "MATERIAL" and (ob.get("trigger") or {}).get("observed") \
           and ob.get("status") in ("PENDING", "FAILED", "UNKNOWN"):
            return VState.BLOCK, "COMPLETION_WITH_OPEN_MATERIAL_OBLIGATION", {"obligation_id": r}
        if ob.get("status") == "SATISFIED" and not (ob.get("closure_evidence_refs") or []):
            return VState.BLOCK, "OBLIGATION_SATISFIED_WITHOUT_CLOSURE_EVIDENCE", {}
        if ob.get("status") in ("NOT_REQUIRED", "DEFERRED_AUTHORIZED") and not ob.get("resolution_reason"):
            return VState.BLOCK, "OBLIGATION_CLOSURE_STATUS_REQUIRES_REASON", {}
    return VState.OK, "", {}


def check_evidence_grades(binding):
    """V2.1 addition: valid E0..E5 enum enforced (V2 only checked E0/E1 subset)."""
    for cap in (binding.get("capabilities") or []):
        if cap.get("status") in ("VERIFIED_AVAILABLE", "VERIFIED_RESTRICTED"):
            refs = cap.get("evidence_refs") or []
            grades = [r.get("grade") for r in refs if isinstance(r, dict)]
            if not grades:
                return VState.BLOCK, "VERIFIED_WITHOUT_EVIDENCE_GRADE", {}
            invalid = [g for g in grades if g not in GRADES]
            if invalid:
                return VState.BLOCK, "EVIDENCE_GRADE_INVALID", {"grades": invalid}
            if all(g in ("E0", "E1") for g in grades):
                return VState.BLOCK, "VERIFIED_ONLY_STATIC_STRUCTURE_EVIDENCE", {"grades": grades}
    return VState.OK, "", {}


def check_mandate(binding, eval_time):
    """V2.1 addition: explicit evaluation time for expires_at (no hardcoded date)."""
    env = binding.get("authority_envelope") or []
    if not env:
        return VState.OK, "", {}
    mandate = binding.get("mandate") or {}
    src = mandate.get("source")
    if not src:
        return VState.BLOCK, "AUTHORITY_WITHOUT_MANDATE_SOURCE", {}
    if src in ("RESTORE", "RESTORED_STATE", "CLONE", "CREDENTIAL_VALID"):
        return VState.BLOCK, "AUTHORITY_MANDATE_SOURCE_NOT_AUTHORIZING", {"source": src}
    horizon = mandate.get("expires_at")
    if not horizon:
        return VState.BLOCK, "AUTHORITY_WITHOUT_MANDATE_HORIZON", {}
    d = parse_date(horizon)
    if d is None:
        return VState.BLOCK, "MANDATE_DATE_UNPARSEABLE", {"expires_at": horizon}
    if d < eval_time:
        return VState.BLOCK, "MANDATE_EXPIRED", {"expires_at": horizon, "evaluated_at": str(eval_time)}
    return VState.OK, "", {}


def check_recovery_history(transition, registries, eval_time):
    """V2 + V2.1: STATE_AND_HISTORY requires preservation evidence; distinct
    refs must not silently mean distinct roots unless registry backs it."""
    claim_scope = (transition.get("recovery_claim") or {}).get("scope")
    if claim_scope != "STATE_AND_HISTORY":
        return VState.OK, "", {}
    hist = transition.get("history_continuity") or {}
    if hist.get("status") != "PRESERVED":
        return VState.BLOCK, "FULL_RECOVERY_REQUIRES_PRESERVED_HISTORY", {}
    refs = hist.get("evidence_refs") or []
    if not refs:
        return VState.BLOCK, "HISTORY_PRESERVED_WITHOUT_EVIDENCE", {}
    if hist.get("post_checkpoint_occurrence_delta_captured") is not True:
        return VState.BLOCK, "HISTORY_PRESERVED_WITHOUT_DELTA_CAPTURE", {}
    state_refs = (transition.get("state_restore") or {}).get("evidence_refs") or []
    if set(refs) & set(state_refs):
        return VState.BLOCK, "HISTORY_EVIDENCE_SAME_AS_STATE_EVIDENCE", {"shared": sorted(set(refs) & set(state_refs))}
    # root derivation: distinct strings may share a root; must verify via registry.
    ev_reg = registries.get("evidence")
    if ev_reg is None:
        # registry unavailable: do NOT fall back to self-asserted label distinctness.
        return VState.UNKNOWN, "PROVENANCE_REGISTRY_UNAVAILABLE", {}
    if isinstance(ev_reg, list):
        ev_by_id = {}
        for e in ev_reg:
            if isinstance(e, dict):
                ev_by_id[e.get("id") or e.get("evidence_id")] = e
    else:
        ev_by_id = {k: v for k, v in ev_reg.items() if isinstance(v, dict)}
    hist_roots = set()
    for r in refs:
        e = ev_by_id.get(r, {})
        hist_roots.add(e.get("root_provenance") or r)
    state_roots = set()
    for r in state_refs:
        e = ev_by_id.get(r, {})
        state_roots.add(e.get("root_provenance") or r)
    if hist_roots & state_roots:
        return VState.BLOCK, "HISTORY_EVIDENCE_SHARED_ROOT", {"roots": sorted(hist_roots & state_roots)}
    return VState.OK, "", {}


def check_independence(support, registries):
    """V2 + V2.1: independence counted on ROOT provenance, verified via registry;
    without registry -> UNKNOWN, not silent label trust."""
    ind = support.get("independence_basis") or {}
    claimed = ind.get("claimed_independent_count")
    if claimed is None:
        return VState.OK, "", {}
    roots = ind.get("root_provenance") or []
    if not roots:
        return VState.BLOCK, "INDEPENDENCE_WITHOUT_ROOT_PROVENANCE", {}
    root_reg = registries.get("root")
    if root_reg is None:
        # registry unavailable -> cannot verify root truth; explicit UNKNOWN.
        return VState.UNKNOWN, "ROOT_REGISTRY_UNAVAILABLE", {}
    origins = set()
    for r in roots:
        entry = root_reg.get(r, {})
        origins.add(entry.get("actual_origin", r))
    if claimed > len(origins):
        return VState.BLOCK, "INDEPENDENCE_OVERCLAIMED", {"claimed": claimed, "origins": sorted(origins)}
    return VState.OK, "", {}


def evaluate(fixture, eval_time):
    """Evaluate ONE fixture through the CUMULATIVE contract. Returns
    (final_state, codes) where final_state in {OK, BLOCK, UNKNOWN}."""
    p = fixture.get("payload", {})
    registries = {}
    for rk, rv in p.items():
        if rk.endswith("_registry") and isinstance(rv, (dict, list)):
            registries[rk[:-len("_registry")]] = rv
        elif rk in ("obligations",) and isinstance(rv, list):
            registries["obligation"] = rv
        elif rk == "support_relations" and isinstance(rv, list):
            registries["support"] = rv
    if "support_registry" in p:
        registries["support"] = p["support_registry"]
    if "evidence_registry" in p:
        registries["evidence"] = p["evidence_registry"]
    if "root_registry" in p:
        registries["root"] = p["root_registry"]

    states = []   # (state, code)
    claim = p.get("claim")
    support = p.get("support")
    binding = p.get("binding")
    transition = p.get("transition")

    # ---- base v0.3.2 validator (actual shipped implementation) ----
    if support is not None and claim is not None:
        r = validate_support(claim, support)
        states.append((VState.BLOCK if not r["ok"] else VState.OK, r.get("code", "OK")))
    for ob in (p.get("obligations") or []):
        r = validate_obligation(ob)
        states.append((VState.BLOCK if not r["ok"] else VState.OK, r.get("code", "OK")))
    if transition is not None:
        r = validate_recovery(transition)
        states.append((VState.BLOCK if not r["ok"] else VState.OK, r.get("code", "OK")))

    # ---- V2 candidate functions (actual committed implementation) ----
    if claim is not None:
        r = v2.candidate_claim_supported_requires_refs(claim)
        states.append((VState.BLOCK if not r["ok"] else VState.OK, r.get("code", "OK")))
    if binding is not None:
        r = v2.candidate_binding_authority_requires_mandate(binding)
        states.append((VState.BLOCK if not r["ok"] else VState.OK, r.get("code", "OK")))
        r = v2.candidate_verification_requires_grade(binding)
        states.append((VState.BLOCK if not r["ok"] else VState.OK, r.get("code", "OK")))
    if claim is not None and p.get("obligations") is not None:
        r = v2.candidate_obligation_claim_link(claim, p["obligations"])
        states.append((VState.BLOCK if not r["ok"] else VState.OK, r.get("code", "OK")))
    if transition is not None:
        r = v2.candidate_recovery_history_requires_evidence(transition)
        states.append((VState.BLOCK if not r["ok"] else VState.OK, r.get("code", "OK")))
    if support is not None:
        r = v2.candidate_independence_requires_root(support)
        states.append((VState.BLOCK if not r["ok"] else VState.OK, r.get("code", "OK")))

    # ---- V2.1/V2.2 additions (typed resolution, enums, dates, roots) ----
    if claim is not None:
        st, code, _ = resolve_support_refs(claim, registries)
        states.append((st, code))
        st, code, _ = resolve_obligation_refs(claim, registries)
        states.append((st, code))
    if binding is not None:
        st, code, _ = check_evidence_grades(binding)
        states.append((st, code))
        st, code, _ = check_mandate(binding, eval_time)
        states.append((st, code))
    if transition is not None:
        st, code, _ = check_recovery_history(transition, registries, eval_time)
        states.append((st, code))
    if support is not None:
        st, code, _ = check_independence(support, registries)
        states.append((st, code))

    codes = [c for _, c in states if c not in ("OK", "")]
    final = _worst([s for s, _ in states])
    return final, codes


EVAL_TIME_DEFAULT = date(2026, 8, 20)

def run_all(fixtures, eval_time=EVAL_TIME_DEFAULT):
    results = []
    for fx in fixtures:
        final, codes = evaluate(fx, eval_time)
        results.append({"id": fx["id"], "kind": fx.get("kind"), "vector": fx.get("vector"),
                        "case": fx.get("case", ""), "final": final, "codes": codes,
                        "expect_block": fx.get("expect_block", []),
                        "expect_pass": fx.get("expect_pass", False)})
    adv = [r for r in results if r["kind"] in ("ADVERSARIAL", "ATTACK", "SECOND_ORDER")]
    pos = [r for r in results if r["kind"] == "POSITIVE"]
    adv_blocked = sum(1 for r in adv if r["final"] == "BLOCK")
    adv_unknown = sum(1 for r in adv if r["final"] == "UNKNOWN")
    pos_ok = sum(1 for r in pos if r["final"] == "OK")
    pos_unknown = sum(1 for r in pos if r["final"] == "UNKNOWN")
    return {
        "TOTAL_ADVERSARIAL_BLOCKED": adv_blocked, "TOTAL_ADVERSARIAL": len(adv),
        "ADVERSARIAL_UNKNOWN": adv_unknown,
        "TOTAL_POSITIVE_PRESERVED": pos_ok, "TOTAL_POSITIVE": len(pos),
        "POSITIVE_UNKNOWN": pos_unknown,
        "results": results,
    }


if __name__ == "__main__":
    print("cumulative contract module loaded (repo-relative)")
    print("REPO =", REPO)
