#!/usr/bin/env python3
"""V2.4.1 successor candidate — residual closure of the frozen V2.4 successor.

The frozen V2.4 candidate (ref 47e0e1b, successor_contract.py in v2.4/) is NOT
modified; releases/current/ NOT modified. This module is the V2.4.1 closure
step implementing ONLY the reconciled residuals from the WorkBuddy independent
validation (PR #30, INDEPENDENT_VALIDATION_SUPPORTED_WITH_RESIDUALS):

  R12 (F1 closure)  ONE consistent identity rule across ALL registry kinds:
       dict key is the authoritative identity; an entry's explicit inner id
       (support_id/obligation_id/evidence_id/root_id/grant_id) must EQUAL the
       dict key, otherwise the registry is REJECTED as REGISTRY_MALFORMED
       (never guess which identity is authoritative); a missing inner id is
       backfilled from the dict key. Applies uniformly to support_registry,
       support_relations, evidence_registry, root_registry, obligations and
       authority_registry dict forms. List-form entries must declare their
       inner id (unchanged). This eliminates the silent false BLOCK and the
       identity-confusion hazards found in F1.

  F2 closure         Schema-valid-input precondition, machine-enforced at the
       semantic boundary (defense in depth): obligation status must be within
       the vocabulary of the shipped triggered-obligation.v1.schema.json
       (PENDING, SATISFIED, NOT_REQUIRED, DEFERRED_AUTHORIZED, FAILED, UNKNOWN);
       any other status (e.g. OPEN) -> BLOCK OBLIGATION_STATUS_OUTSIDE_VOCABULARY.
       The obligation vocabulary is NOT expanded.

Everything else is byte-for-byte the frozen V2.4 successor (R1-R11, evaluate
surface, never-exception fail-safe). The corpus is the frozen 98 + WorkBuddy
probes + new F1/F2 closure controls, all through THIS one implementation.
"""
from __future__ import annotations
import sys, json
from pathlib import Path
from datetime import date

# ---------------------------------------------------------------------------
# repo-relative path resolution (portable)
# ---------------------------------------------------------------------------
HERE = Path(__file__).resolve().parent            # .../v2.4.1
PROTO_ROOT = HERE.parent                          # .../v2-machine-contract-hardening

def _find_repo(start):
    cur = start
    for _ in range(8):
        if (cur / "releases" / "current" / "tools").exists():
            return cur
        cur = cur.parent
    return start.parent / "repo"

REPO = _find_repo(HERE)
sys.path.insert(0, str(REPO / "releases" / "current" / "tools"))   # shipped baseline
sys.path.insert(0, str(REPO / "research" / "prototypes" / "v2-machine-contract-hardening"))
sys.path.insert(0, str(HERE))

from validate_contracts import validate_support, validate_obligation, validate_recovery, SCOPE_KEYS

# ---------------------------------------------------------------------------
# states / aggregation
# ---------------------------------------------------------------------------
class V:
    OK = "OK"
    BLOCK = "BLOCK"
    UNKNOWN = "UNKNOWN"

def _worst(states):
    if any(s == V.BLOCK for s in states):
        return V.BLOCK
    if any(s == V.UNKNOWN for s in states):
        return V.UNKNOWN
    return V.OK

def parse_date(s):
    try:
        y, m, d = s.strip().split("-")
        return date(int(y), int(m), int(d))
    except Exception:
        return None

GRADES = {"E0", "E1", "E2", "E3", "E4", "E5"}
# R9: positive typing of authorizing mandate sources (extendable; an
# authority_registry can verify sources not in this vocabulary — R9 upstream).
AUTHORIZING_MANDATE_SOURCES = {"USER_EXPLICIT_GRANT"}
COMPLETION_TYPES = ("WORKFLOW_COMPLETION", "TASK_COMPLETION")
# F2: obligation status vocabulary mirrors shipped
# releases/current/schemas/triggered-obligation.v1.schema.json status enum.
OBLIGATION_STATUS_VOCABULARY = {"PENDING", "SATISFIED", "NOT_REQUIRED",
                                "DEFERRED_AUTHORIZED", "FAILED", "UNKNOWN"}

# per-artifact-kind absent-registry policy (R3)
#   support/obligation refs are named BY the claim itself -> mandatory -> BLOCK
#   evidence/root refs verify deeper provenance -> absent registry -> UNKNOWN
ABSENT_POLICY = {
    "support":    (V.BLOCK,   "SUPPORT_REF_UNRESOLVABLE"),
    "obligation": (V.BLOCK,   "OBLIGATION_REF_UNRESOLVABLE"),
    "evidence":   (V.UNKNOWN, "EVIDENCE_REGISTRY_UNAVAILABLE"),
    "root":       (V.UNKNOWN, "ROOT_REGISTRY_UNAVAILABLE"),
    "authority":  (V.BLOCK,   "AUTHORITY_REGISTRY_UNAVAILABLE"),
}

ID_KEYS = {
    "support":    ("support_id", "id"),
    "obligation": ("obligation_id", "id"),
    "evidence":   ("evidence_id", "id"),
    "root":       ("root_id", "id"),
    "authority":  ("grant_id", "id"),
}

def _fingerprint(a):
    return json.dumps(a, sort_keys=True, ensure_ascii=False, default=str)

def _id_of(artifact, kind):
    for k in ID_KEYS[kind]:
        v = artifact.get(k)
        if isinstance(v, str) and v:
            return v
    return None

# ---------------------------------------------------------------------------
# R11+R12 canonical registry normalization: dict | list -> {id: [artifacts]} | None
#   * None          -> absent (None)
#   * dict          -> {key: artifact}; R12: key is authoritative; an explicit
#                      inner id must equal the key (else REGISTRY_MALFORMED);
#                      a missing inner id is backfilled from the key.
#   * list          -> list of artifact dicts; each must declare its inner id.
#   * anything else -> (BLOCK, REGISTRY_MALFORMED)
# Duplicate ids collected; ambiguity decided at resolve time by fingerprint.
# ---------------------------------------------------------------------------
def normalize_registry(raw, kind):
    if raw is None:
        return (V.OK, "", None)
    by_id = {}
    if isinstance(raw, dict):
        if not all(isinstance(v, dict) for v in raw.values()):
            return (V.BLOCK, "REGISTRY_MALFORMED", None)
        for k, v in raw.items():
            entry = dict(v)
            inner = _id_of(entry, kind)
            if inner is not None and inner != k:
                # R12: explicit inner id disagrees with the dict key -> malformed;
                # do not guess which identity is authoritative.
                return (V.BLOCK, "REGISTRY_MALFORMED",
                        {"key": k, "declared_id": inner, "kind": kind})
            if inner is None:
                entry[ID_KEYS[kind][0]] = k            # backfill from key
            by_id.setdefault(k, []).append(entry)
    elif isinstance(raw, list):
        if not all(isinstance(x, dict) for x in raw):
            return (V.BLOCK, "REGISTRY_MALFORMED", None)
        for x in raw:
            i = _id_of(x, kind)
            if i is None:
                return (V.BLOCK, "REGISTRY_MALFORMED", None)
            by_id.setdefault(i, []).append(x)
    else:
        return (V.BLOCK, "REGISTRY_MALFORMED", None)
    return (V.OK, "", by_id)

# ---------------------------------------------------------------------------
# canonical typed resolver (R1/R3/R5) — used for EVERY consequential ref
# ---------------------------------------------------------------------------
def typed_resolve(ref, by_id, kind):
    """by_id: normalized {id: [artifacts]} or None (registry absent).
    Returns (state, code, artifact|None).
      absent policy by kind (R3); missing -> BLOCK {KIND}_REF_UNRESOLVABLE
      (obligation uses DUPLICATE_OBLIGATION_ID; others DUPLICATE_REF_ID);
      byte-identical duplicates deduped (R5)."""
    if by_id is None:
        state, code = ABSENT_POLICY[kind]
        return (state, code, None)
    entries = by_id.get(ref)
    if not entries:
        if kind == "obligation":
            return (V.BLOCK, "OBLIGATION_REF_UNRESOLVABLE", None)
        return (V.BLOCK, f"{kind.upper()}_REF_UNRESOLVABLE", None)
    if len(entries) > 1:
        if len({_fingerprint(e) for e in entries}) > 1:
            code = "DUPLICATE_OBLIGATION_ID" if kind == "obligation" else "DUPLICATE_REF_ID"
            return (V.BLOCK, code, None)
        entries = entries[:1]
    return (V.OK, "", entries[0])

# ---------------------------------------------------------------------------
# evidence-existence resolution (R3): enforced when the evidence registry is
# supplied; absent registry -> no existence verdict on this path.
# ---------------------------------------------------------------------------
def check_evidence_refs(refs, ev_by_id, ctx):
    """Returns list of (state, code). ctx: label for codes."""
    if not refs:
        return []
    if ev_by_id is None:
        return []                       # absent registry: baseline posture (I06)
    out = []
    for r in refs:
        st, code, _ = typed_resolve(r, ev_by_id, "evidence")
        if st != V.OK:
            out.append((st, code))
    return out

# ---------------------------------------------------------------------------
# scope: full baseline envelope (R4) — handled by shipped validate_support,
# plus transfer-evidence resolution (R3/I12).
# ---------------------------------------------------------------------------
def check_transfer_evidence(support, ev_by_id):
    tb = support.get("transfer_basis") or {}
    refs = tb.get("evidence_refs") or []
    if not refs:
        return []
    return check_evidence_refs(refs, ev_by_id, "transfer")

# ---------------------------------------------------------------------------
# independence roots (R3/R4): string-level overclaim first, then registry.
# ---------------------------------------------------------------------------
def check_independence(support, root_by_id):
    ind = support.get("independence_basis") or {}
    claimed = ind.get("claimed_independent_count")
    if claimed is None:
        return (V.OK, "", {})
    roots = ind.get("root_provenance") or []
    if not roots:
        return (V.BLOCK, "INDEPENDENCE_WITHOUT_ROOT_PROVENANCE", {})
    unique_strings = {str(x) for x in roots if x not in (None, "", "UNKNOWN")}
    if claimed > len(unique_strings):
        return (V.BLOCK, "INDEPENDENCE_OVERCLAIMED", {"claimed": claimed, "unique_root_strings": sorted(unique_strings)})
    if root_by_id is None:
        return (V.UNKNOWN, "ROOT_REGISTRY_UNAVAILABLE", {})
    origins = set()
    for r in roots:
        st, code, entry = typed_resolve(r, root_by_id, "root")
        if st != V.OK:
            return (st, code, {"root": r})
        origins.add(entry.get("actual_origin", r))
    if claimed > len(origins):
        return (V.BLOCK, "INDEPENDENCE_OVERCLAIMED", {"claimed": claimed, "origins": sorted(origins)})
    return (V.OK, "", {})

# ---------------------------------------------------------------------------
# claim pipeline (R2/R6/R7/R10)
# ---------------------------------------------------------------------------
def _support_sources(p):
    """top-level support + support_registry + support_relations -> list of
    artifact dicts; None on malformed shape. R12: dict-form maps apply the
    same identity rule (key authoritative; explicit inner id must equal key;
    missing inner id backfilled)."""
    sources = []
    ts = p.get("support")
    if ts is not None:
        if isinstance(ts, dict):
            sources.append(ts)
        elif isinstance(ts, list) and all(isinstance(x, dict) for x in ts):
            sources.extend(ts)
        else:
            return None
    for key in ("support_registry", "support_relations"):
        reg = p.get(key)
        if reg is None:
            continue
        if isinstance(reg, dict) and all(isinstance(v, dict) for v in reg.values()):
            for k, v in reg.items():
                e = dict(v)
                inner = _id_of(e, "support")
                if inner is not None and inner != k:
                    return None                     # R12 divergence -> malformed
                if inner is None:
                    e["support_id"] = k             # backfill from key
                sources.append(e)
        elif isinstance(reg, list) and all(isinstance(x, dict) for x in reg):
            sources.extend(reg)
        else:
            return None
    return sources

def check_support_path(claim, p, support_by_id, ev_by_id, root_by_id):
    """R1/R2/R4/R10 + evidence existence. Returns list of (state, code, detail)."""
    out = []
    refs = claim.get("support_relation_refs") or []
    if claim.get("status") == "SUPPORTED" and not refs:
        out.append((V.BLOCK, "CLAIM_SUPPORTED_WITHOUT_SUPPORT_REFS", {}))   # V2 ATT-1 preserved (A1)
    for ref in refs:
        st, code, artifact = typed_resolve(ref, support_by_id, "support")
        if st != V.OK:
            out.append((st, code, {"ref": ref}))
            continue
        # R2: resolved support must bind back to the current claim
        if artifact.get("claim_ref") != claim.get("claim_id"):
            out.append((V.BLOCK, "SUPPORT_TARGET_MISMATCH",
                        {"support_id": ref, "claim_ref": artifact.get("claim_ref"), "claim": claim.get("claim_id")}))
            continue
        # support status semantics
        status = artifact.get("support_status")
        if status == "CONTRADICTS":
            out.append((V.BLOCK, "RESOLVED_SUPPORT_CONTRADICTS", {"support_id": ref}))
            continue
        if status not in ("SUPPORTS", "PARTIAL"):
            out.append((V.BLOCK, "SUPPORT_NOT_POSITIVE", {"support_id": ref, "support_status": status}))
            continue
        # R10: PARTIAL cannot establish a full SUPPORTED claim
        if status == "PARTIAL":
            if claim.get("support_claim") != "PARTIAL":
                out.append((V.UNKNOWN, "PARTIAL_SUPPORT_ONLY", {"support_id": ref}))
                continue
        # evidence must be carried (V2.1) and, when a registry is supplied, resolve
        ev_refs = artifact.get("evidence_refs") or []
        if not ev_refs:
            out.append((V.BLOCK, "SUPPORT_WITHOUT_EVIDENCE", {"support_id": ref}))
            continue
        out.extend(check_evidence_refs(ev_refs, ev_by_id, "support"))
        # R4: full baseline applicability envelope via the shipped validator
        base = validate_support(claim, artifact)
        if not base["ok"]:
            out.append((V.BLOCK, base["code"], {"support_id": ref, "details": base.get("details")}))
            continue
        if base["code"] == "SUPPORT_SCOPE_TRANSFER_DECLARED":
            out.extend(check_transfer_evidence(artifact, ev_by_id))
        # independence roots (R3)
        st2, code2, _ = check_independence(artifact, root_by_id)
        if st2 != V.OK:
            out.append((st2, code2, {"support_id": ref}))
    return out

def check_obligation_path(claim, p, ob_by_id, ev_by_id):
    """R7 claim-aware obligation blocking; R3 closure-evidence resolution;
    F2 status-vocabulary gate is applied to ALL supplied obligations in
    _evaluate (schema-valid-input precondition); here only the claim-scoped
    blocking semantics run."""
    out = []
    if claim.get("claim_type") not in COMPLETION_TYPES:
        return out
    refs = claim.get("required_obligation_refs") or []
    if not refs:
        out.append((V.BLOCK, "COMPLETION_CLAIM_WITHOUT_OBLIGATION_REFS", {}))
        return out
    for ref in refs:
        st, code, artifact = typed_resolve(ref, ob_by_id, "obligation")
        if st != V.OK:
            out.append((st, code, {"ref": ref}))
            continue
        # in-scope: referenced by this claim OR bound to this claim
        base = validate_obligation(artifact)
        if not base["ok"]:
            out.append((V.BLOCK, base["code"], {"obligation_id": ref, "details": base.get("details")}))
        # closure evidence resolution when registry supplied
        if artifact.get("status") == "SATISFIED":
            out.extend(check_evidence_refs(artifact.get("closure_evidence_refs") or [], ev_by_id, "closure"))
    # R7: obligations bound to THIS claim (even if not referenced) also gate it
    if ob_by_id is not None:
        for oid, entries in ob_by_id.items():
            for ob in entries:
                if claim.get("claim_id") in (ob.get("required_before_claim_refs") or []):
                    base = validate_obligation(ob)
                    if not base["ok"]:
                        out.append((V.BLOCK, base["code"], {"obligation_id": oid, "details": base.get("details")}))
    return out

# ---------------------------------------------------------------------------
# binding pipeline (R9 + grades + evidence existence)
# ---------------------------------------------------------------------------
def check_binding(binding, ev_by_id, authority_by_id, eval_time):
    out = []
    env = binding.get("authority_envelope") or []
    if env:
        mandate = binding.get("mandate") or {}
        src = mandate.get("source")
        if not src:
            out.append((V.BLOCK, "AUTHORITY_WITHOUT_MANDATE_SOURCE", {}))
        else:
            authorized = src in AUTHORIZING_MANDATE_SOURCES
            if not authorized and authority_by_id is not None:
                st, code, grant = typed_resolve(src, authority_by_id, "authority")
                if st == V.OK:
                    g = grant
                    if g.get("agent") in (None, binding.get("agent")) and \
                       g.get("host") in (None, binding.get("host")) and \
                       parse_date(g.get("expires_at") or "2999-12-31") is not None and \
                       (parse_date(g.get("expires_at") or "2999-12-31") >= eval_time):
                        authorized = True
                    else:
                        out.append((V.BLOCK, "AUTHORITY_MANDATE_SOURCE_NOT_AUTHORIZING",
                                    {"source": src, "reason": "grant_does_not_cover_binding"}))
            if not authorized:
                out.append((V.BLOCK, "AUTHORITY_MANDATE_SOURCE_NOT_AUTHORIZING", {"source": src}))
            horizon = mandate.get("expires_at")
            if not horizon:
                out.append((V.BLOCK, "AUTHORITY_WITHOUT_MANDATE_HORIZON", {}))
            else:
                d = parse_date(horizon)
                if d is None:
                    out.append((V.BLOCK, "MANDATE_DATE_UNPARSEABLE", {"expires_at": horizon}))
                elif d < eval_time:
                    out.append((V.BLOCK, "MANDATE_EXPIRED", {"expires_at": horizon, "evaluated_at": str(eval_time)}))
    for cap in (binding.get("capabilities") or []):
        if cap.get("status") in ("VERIFIED_AVAILABLE", "VERIFIED_RESTRICTED"):
            refs = cap.get("evidence_refs") or []
            grades = [r.get("grade") for r in refs if isinstance(r, dict)]
            if not grades:
                out.append((V.BLOCK, "VERIFIED_WITHOUT_EVIDENCE_GRADE", {}))
                continue
            invalid = [g for g in grades if g not in GRADES]
            if invalid:
                out.append((V.BLOCK, "EVIDENCE_GRADE_INVALID", {"grades": invalid}))
                continue
            if all(g in ("E0", "E1") for g in grades):
                out.append((V.BLOCK, "VERIFIED_ONLY_STATIC_STRUCTURE_EVIDENCE", {"grades": grades}))
                continue
            out.extend(check_evidence_refs([r.get("ref") for r in refs if isinstance(r, dict) and r.get("ref")],
                                           ev_by_id, "capability"))
    return out

# ---------------------------------------------------------------------------
# recovery pipeline (R8/R3)
# ---------------------------------------------------------------------------
def check_recovery(transition, ev_by_id, eval_time):
    out = []
    base = validate_recovery(transition)
    if not base["ok"]:
        out.append((V.BLOCK, base["code"], {"details": base.get("details")}))
        return out
    scope = (transition.get("recovery_claim") or {}).get("scope")
    if scope == "STATE_AND_HISTORY":
        hist = transition.get("history_continuity") or {}
        state = transition.get("state_restore") or {}
        hist_refs = hist.get("evidence_refs") or []
        state_refs = state.get("evidence_refs") or []
        if not hist_refs:
            out.append((V.BLOCK, "HISTORY_PRESERVED_WITHOUT_EVIDENCE", {}))
        if hist.get("post_checkpoint_occurrence_delta_captured") is not True:
            out.append((V.BLOCK, "HISTORY_PRESERVED_WITHOUT_DELTA_CAPTURE", {}))
        if not state_refs:
            out.append((V.BLOCK, "STATE_RESTORE_WITHOUT_EVIDENCE", {}))   # R8/I13
        if set(hist_refs) & set(state_refs):
            out.append((V.BLOCK, "HISTORY_EVIDENCE_SAME_AS_STATE_EVIDENCE",
                        {"shared": sorted(set(hist_refs) & set(state_refs))}))
        all_refs = sorted(set(hist_refs) | set(state_refs))
        if ev_by_id is None:
            out.append((V.UNKNOWN, "PROVENANCE_REGISTRY_UNAVAILABLE", {}))  # P7 preserved
        else:
            for r in all_refs:
                st, code, _ = typed_resolve(r, ev_by_id, "evidence")
                if st != V.OK:
                    out.append((st, code, {"ref": r}))
            # root distinctness via registry (no raw-string trust)
            hist_roots = set()
            for r in hist_refs:
                st, code, e = typed_resolve(r, ev_by_id, "evidence")
                hist_roots.add(e.get("root_provenance", r) if st == V.OK else r)
            state_roots = set()
            for r in state_refs:
                st, code, e = typed_resolve(r, ev_by_id, "evidence")
                state_roots.add(e.get("root_provenance", r) if st == V.OK else r)
            shared = hist_roots & state_roots
            if shared:
                out.append((V.BLOCK, "HISTORY_EVIDENCE_SHARED_ROOT", {"roots": sorted(shared)}))
    return out

# ---------------------------------------------------------------------------
# evaluate — one surface, never raises (R11)
# ---------------------------------------------------------------------------
def evaluate(fixture, eval_time):
    """Returns (final_state, codes). final in {OK, BLOCK, UNKNOWN}. Never raises."""
    try:
        return _evaluate(fixture, eval_time)
    except Exception as e:
        return (V.BLOCK, ["EVALUATOR_FAULT", f"{type(e).__name__}: {e}"])

def _evaluate(fixture, eval_time):
    p = fixture.get("payload", {})
    states = []

    # ---- R11/R12: canonical registry extraction + shape validation ----
    support_by_id = None
    ev_by_id = None
    root_by_id = None
    ob_by_id = None
    authority_by_id = None

    sup = _support_sources(p)
    if sup is None:
        return (V.BLOCK, ["REGISTRY_MALFORMED", "support sources"])
    if sup:
        st, code, by_id = normalize_registry(sup, "support")
        if st != V.OK:
            return (V.BLOCK, [code, "support registry"])
        support_by_id = by_id

    st, code, by_id = normalize_registry(p.get("evidence_registry"), "evidence")
    if st != V.OK:
        return (V.BLOCK, [code, "evidence registry"])
    ev_by_id = by_id

    st, code, by_id = normalize_registry(p.get("root_registry"), "root")
    if st != V.OK:
        return (V.BLOCK, [code, "root registry"])
    root_by_id = by_id

    st, code, by_id = normalize_registry(p.get("obligations"), "obligation")
    if st != V.OK:
        return (V.BLOCK, [code, "obligations"])
    ob_by_id = by_id

    st, code, by_id = normalize_registry(p.get("authority_registry"), "authority")
    if st != V.OK:
        return (V.BLOCK, [code, "authority registry"])
    authority_by_id = by_id

    # ---- F2: schema-valid-input precondition — obligation status vocabulary
    # (shipped triggered-obligation.v1.schema.json enum; vocabulary NOT expanded).
    if ob_by_id is not None:
        for entries in ob_by_id.values():
            for ob in entries:
                stt = ob.get("status")
                if stt not in OBLIGATION_STATUS_VOCABULARY:
                    return (V.BLOCK, ["OBLIGATION_STATUS_OUTSIDE_VOCABULARY", str(stt)])

    claim = p.get("claim")
    support = p.get("support")
    binding = p.get("binding")
    transition = p.get("transition")

    # ---- claim pipeline ----
    if claim is not None:
        # R1/R2/R4/R10 (+ evidence existence)
        states.extend(check_support_path(claim, p, support_by_id, ev_by_id, root_by_id))
        # R7 obligations
        states.extend(check_obligation_path(claim, p, ob_by_id, ev_by_id))

    # ---- support-only artifact (no claim): independence + evidence ----
    if claim is None and support is not None:
        arts = support if isinstance(support, list) else [support]
        for a in arts:
            st, code, _ = check_independence(a, root_by_id)
            if st != V.OK:
                states.append((st, code))
            states.extend(check_evidence_refs(a.get("evidence_refs") or [], ev_by_id, "support"))

    # ---- binding pipeline ----
    if binding is not None:
        states.extend(check_binding(binding, ev_by_id, authority_by_id, eval_time))

    # ---- recovery pipeline ----
    if transition is not None:
        states.extend(check_recovery(transition, ev_by_id, eval_time))

    codes = [c for _, c, *_ in states if c not in ("OK", "")]
    final = _worst([s for s, *_ in states])
    return final, codes
