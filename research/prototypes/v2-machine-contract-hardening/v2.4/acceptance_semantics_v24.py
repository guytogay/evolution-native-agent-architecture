#!/usr/bin/env python3
"""V2.4 structural acceptance oracle — expected verdicts from SEMANTIC
PRECONDITIONS, never from fixture `kind` labels or hard-coded IDs.

This replaces the V2.3 oracle shortcuts rejected by the independent validator
(§6 / §10.12: kind-driven BLOCK, hard-coded MIGRATED_IDS, registry-key-absence
classification, representation disagreement, blanket fallthrough). The oracle
mirrors the successor contract's semantic preconditions; the independent
fixtures (I01-I16) carry external ground truth, and run_v24 asserts the oracle
agrees with every independent expectation (I14 refined UNKNOWN_OR_BLOCK ->
UNKNOWN, documented in RECONCILIATION.md).
"""
from __future__ import annotations
import json

SCOPE_KEYS = ("host", "runtime_instance", "model_binding", "route",
              "configuration", "epoch", "time_interval", "task_scope")
AUTHORIZING_MANDATE_SOURCES = {"USER_EXPLICIT_GRANT"}
GRADES = {"E0", "E1", "E2", "E3", "E4", "E5"}
COMPLETION_TYPES = ("WORKFLOW_COMPLETION", "TASK_COMPLETION")


def _fingerprint(a):
    return json.dumps(a, sort_keys=True, ensure_ascii=False, default=str)


def _reg_keys(reg, id_keys=("id",)):
    if reg is None:
        return None
    if isinstance(reg, dict):
        return set(reg.keys())
    if isinstance(reg, list):
        return {e.get(k) for e in reg if isinstance(e, dict) for k in id_keys if isinstance(e.get(k), str)}
    return None


def _id_of(entry):
    for k in ("support_id", "obligation_id", "evidence_id", "root_id", "grant_id", "id"):
        v = entry.get(k)
        if isinstance(v, str) and v:
            return v
    return None


def _support_sources(p):
    """Returns (ids_set, entries_list) or None on malformed shape."""
    entries = []
    ts = p.get("support")
    if ts is not None:
        if isinstance(ts, dict):
            entries.append(ts)
        elif isinstance(ts, list) and all(isinstance(x, dict) for x in ts):
            entries.extend(ts)
        else:
            return None
    for key in ("support_registry", "support_relations"):
        reg = p.get(key)
        if reg is None:
            continue
        if isinstance(reg, dict) and all(isinstance(v, dict) for v in reg.values()):
            for k, v in reg.items():
                e = dict(v)
                if _id_of(e) is None:
                    e["support_id"] = k
                entries.append(e)
        elif isinstance(reg, list) and all(isinstance(x, dict) for x in reg):
            entries.extend(reg)
        else:
            return None
    ids = {_id_of(e) for e in entries}
    return (ids, entries)


def _scope_mismatches(observed, claimed):
    out = []
    for key in SCOPE_KEYS:
        c = claimed.get(key)
        if c in (None, "", "UNKNOWN"):
            continue
        if observed.get(key) != c:
            out.append({"field": key, "observed": observed.get(key), "claimed": c})
    return out


def _evidence_missing(refs, ev_keys):
    """registry present? -> any ref missing -> BLOCK; registry absent -> no verdict."""
    if ev_keys is None:
        return []
    return [r for r in refs if r not in ev_keys]


def structural_expect(fx, eval_time) -> str:
    """Expected verdict (BLOCK/OK/UNKNOWN) derived ONLY from payload semantics."""
    p = fx.get("payload", {})
    claim = p.get("claim")
    support = p.get("support")
    binding = p.get("binding")
    transition = p.get("transition")

    ev_keys = _reg_keys(p.get("evidence_registry"), ("evidence_id", "id"))
    root_keys = _reg_keys(p.get("root_registry"), ("root_id", "id"))

    # ---------------- recovery ----------------
    if transition is not None:
        scope = (transition.get("recovery_claim") or {}).get("scope")
        state = transition.get("state_restore") or {}
        hist = transition.get("history_continuity") or {}
        if state.get("result") != "SUCCESS":
            return "BLOCK"
        if scope == "STATE_AND_HISTORY":
            if hist.get("status") != "PRESERVED":
                return "BLOCK"
            hist_refs = hist.get("evidence_refs") or []
            state_refs = state.get("evidence_refs") or []
            if not hist_refs:
                return "BLOCK"
            if hist.get("post_checkpoint_occurrence_delta_captured") is not True:
                return "BLOCK"
            if not state_refs:
                return "BLOCK"                       # I13
            if set(hist_refs) & set(state_refs):
                return "BLOCK"                       # S4
            if ev_keys is None:
                return "UNKNOWN"                     # P7 (absent registry)
            if _evidence_missing(sorted(set(hist_refs) | set(state_refs)), ev_keys):
                return "BLOCK"                       # I02/O03
            # root distinctness via registry entries
            reg = p.get("evidence_registry")
            def root_of(r):
                e = reg.get(r) if isinstance(reg, dict) else None
                return (e or {}).get("root_provenance", r)
            if {root_of(r) for r in hist_refs} & {root_of(r) for r in state_refs}:
                return "BLOCK"                       # V22-A4/A21-5
            return "OK"
        return "OK"                                   # STATE_ONLY / visible-gap (baseline)

    # ---------------- support-only artifact (no claim) ----------------
    if support is not None and claim is None:
        arts = support if isinstance(support, list) else [support]
        for a in arts:
            ind = a.get("independence_basis") or {}
            claimed = ind.get("claimed_independent_count")
            if claimed is not None:
                roots = ind.get("root_provenance") or []
                if not roots:
                    return "BLOCK"                    # A6
                if claimed > len({str(x) for x in roots if x not in (None, "", "UNKNOWN")}):
                    return "BLOCK"                    # A6b/S5
                if root_keys is None:
                    return "UNKNOWN"                  # P9
                if [r for r in roots if r not in root_keys]:
                    return "BLOCK"                    # I03
                reg = p.get("root_registry")
                origins = set()
                for r in roots:
                    e = reg.get(r) if isinstance(reg, dict) else None
                    origins.add((e or {}).get("actual_origin", r))
                if claimed > len(origins):
                    return "BLOCK"                    # V22-A5/A21-6
            if _evidence_missing(a.get("evidence_refs") or [], ev_keys):
                return "BLOCK"
        return "OK"

    # ---------------- claim ----------------
    if claim is not None:
        status = claim.get("status")
        ctype = claim.get("claim_type")
        needs_support = (status == "SUPPORTED") or (ctype in COMPLETION_TYPES)
        if needs_support:
            src = _support_sources(p)
            if src is None:
                return "BLOCK"                        # malformed registry shape
            ids, entries = src
            refs = claim.get("support_relation_refs") or []
            if status == "SUPPORTED" and not refs:
                return "BLOCK"                        # A1
            for ref in refs:
                if ref not in ids:
                    return "BLOCK"                    # A21-1/A21-7/P1/P5/P6/O02/V22-A1
                matches = [e for e in entries if _id_of(e) == ref]
                if not matches:
                    return "BLOCK"
                # R5: duplicate ids with differing content are ambiguous
                if len(matches) > 1 and len({_fingerprint(e) for e in matches}) > 1:
                    return "BLOCK"                    # I08/V24-A08
                entry = matches[0]
                if entry.get("claim_ref") != claim.get("claim_id"):
                    return "BLOCK"                    # I01
                st = entry.get("support_status")
                if st == "CONTRADICTS":
                    return "BLOCK"
                if st not in ("SUPPORTS", "PARTIAL"):
                    return "BLOCK"
                if st == "PARTIAL":
                    if claim.get("support_claim") != "PARTIAL":
                        return "UNKNOWN"              # I14 (minimal rule)
                ev = entry.get("evidence_refs") or []
                if not ev:
                    return "BLOCK"                    # S1
                if _evidence_missing(ev, ev_keys):
                    return "BLOCK"                    # I09
                # R4 full baseline applicability envelope (missing observed = mismatch)
                observed = entry.get("observed_scope") or {}
                claimed_scope = entry.get("claimed_scope") or claim.get("scope") or {}
                mismatches = _scope_mismatches(observed, claimed_scope)
                if mismatches:
                    tb = entry.get("transfer_basis") or {}
                    if not (tb.get("required") is True and tb.get("type") and (tb.get("evidence_refs") or [])):
                        return "BLOCK"                # I04/I05/A21-9
                    if _evidence_missing(tb.get("evidence_refs") or [], ev_keys):
                        return "BLOCK"                # I12
                # independence on this support
                ind = entry.get("independence_basis") or {}
                ic = ind.get("claimed_independent_count")
                if ic is not None:
                    roots = ind.get("root_provenance") or []
                    if not roots:
                        return "BLOCK"
                    if ic > len({str(x) for x in roots if x not in (None, "", "UNKNOWN")}):
                        return "BLOCK"
                    if root_keys is None:
                        return "UNKNOWN"
                    if [r for r in roots if r not in root_keys]:
                        return "BLOCK"
        # obligations (claim-aware)
        if ctype in COMPLETION_TYPES:
            ob_refs = claim.get("required_obligation_refs") or []
            if not ob_refs:
                return "BLOCK"                        # A4
            obligations = p.get("obligations")
            if obligations is None:
                return "BLOCK"
            ob_ids = {_id_of(o) for o in obligations} if isinstance(obligations, list) else set(obligations.keys())
            for ref in ob_refs:
                if ref not in ob_ids:
                    return "BLOCK"                    # A21-2
            obs = obligations.values() if isinstance(obligations, dict) else obligations
            for ob in obs:
                oid = _id_of(ob)
                bound = claim.get("claim_id") in (ob.get("required_before_claim_refs") or [])
                if oid not in ob_refs and not bound:
                    continue                          # R7: out of scope (I07)
                if ob.get("materiality") == "MATERIAL" and (ob.get("trigger") or {}).get("observed") is True \
                   and ob.get("status") in ("PENDING", "FAILED", "UNKNOWN"):
                    return "BLOCK"                    # S3 / bound-open
                if ob.get("status") == "SATISFIED" and not (ob.get("closure_evidence_refs") or []):
                    return "BLOCK"
                if _evidence_missing(ob.get("closure_evidence_refs") or [], ev_keys):
                    return "BLOCK"
        # if nothing blocked so far and claim required no support -> OK
        return "OK"

    # ---------------- binding ----------------
    if binding is not None:
        env = binding.get("authority_envelope") or []
        if env:
            mandate = binding.get("mandate") or {}
            src = mandate.get("source")
            if not src:
                return "BLOCK"                        # A3
            authorized = src in AUTHORIZING_MANDATE_SOURCES
            if not authorized:
                areg = p.get("authority_registry")
                akeys = _reg_keys(areg, ("grant_id", "id"))
                if akeys is not None and src in akeys:
                    authorized = True
            if not authorized:
                return "BLOCK"                        # I11/S2
            horizon = mandate.get("expires_at")
            if not horizon:
                return "BLOCK"
            try:
                y, m, d = horizon.strip().split("-")
                from datetime import date as _d
                if _d(int(y), int(m), int(d)) < eval_time:
                    return "BLOCK"                    # A21-4/V22-A3
            except Exception:
                return "BLOCK"                        # A21-4b
        for cap in (binding.get("capabilities") or []):
            if cap.get("status") in ("VERIFIED_AVAILABLE", "VERIFIED_RESTRICTED"):
                refs = cap.get("evidence_refs") or []
                grades = [r.get("grade") for r in refs if isinstance(r, dict)]
                if not grades:
                    return "BLOCK"
                if any(g not in GRADES for g in grades):
                    return "BLOCK"
                if all(g in ("E0", "E1") for g in grades):
                    return "BLOCK"
                if _evidence_missing([r.get("ref") for r in refs if isinstance(r, dict) and r.get("ref")], ev_keys):
                    return "BLOCK"                    # I10
        return "OK"

    # ---------------- nothing relevant ----------------
    return "OK"
