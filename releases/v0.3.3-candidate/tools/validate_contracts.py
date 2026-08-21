#!/usr/bin/env python3
"""Reference semantic validator — ENA v0.3.3-candidate (implementation candidate).

This is the v0.3.3-candidate copy of the shipped v0.3.2 validator with the
accepted V2.4.1 mechanism set translated into the shipped tool surface.

Part 1 (SHIPPED CORE) is byte-identical to v0.3.2 `releases/current/tools/
validate_contracts.py`: `validate_support`, `validate_obligation`,
`validate_recovery`, the 8-dimension applicability envelope, and the
`support/obligation/recovery/selftest` CLI. The v0.3.2 semantic selftests
(contract-fixtures.v1.json) are intentionally preserved and still pass.

Part 2 (COMPOSED LAYER, new in this candidate) implements the reconciled
mechanisms from the frozen V2.4.1 research successor (daacab1, ACCEPT_FOR_
IMPLEMENTATION, PR #34) as one coherent production surface:

  R1   every consequential reference resolves through one canonical typed
       resolver in its own artifact namespace (support/obligation/evidence/
       root/authority).
  R2   resolved support must bind back to the target claim (claim_ref).
  R3   registries are tri-state: absent | present-but-missing | malformed;
       NO raw-reference fallback when a supplied registry cannot resolve the
       artifact; mandatory consequential evidence refs resolve where the
       contract requires them (enforced when an evidence registry is supplied;
       absent-registry keeps the baseline posture for support/capability/
       transfer/closure evidence while recovery/independence provenance keeps
       absent -> UNKNOWN).
  R4   the complete baseline applicability envelope is preserved; material
       missing observations do not silently count as matches (shipped
       validate_support).
  R5   ambiguous duplicate identities fail closed (byte-identical duplicates
       dedupe).
  R6   top-level support and registry support representations compose
       consistently (dict/list forms).
  R7   obligation blocking is claim-aware: only obligations referenced by the
       claim or bound to it gate the claim.
  R8   STATE_AND_HISTORY recovery establishes both state-restoration and
       history-continuity evidence.
  R9   authority source semantics are positively typed or verified via an
       optional authority registry (explicitly bounded vocabulary).
  R10  PARTIAL support remains narrowed: PARTIAL-only support cannot establish
       a full SUPPORTED claim unless the claim is explicitly narrowed
       (support_claim == "PARTIAL").
  R11  malformed registry inputs produce machine verdicts (REGISTRY_MALFORMED),
       never uncaught exceptions; residual faults fail closed (EVALUATOR_FAULT).
  R12  registry identity rule: for dict-form registries the dict key is
       authoritative; an explicit inner id must equal the key or the registry
       is REGISTRY_MALFORMED; missing inner ids are backfilled from the key.
  F2   obligation status outside the shipped obligation-status vocabulary is
       rejected at the semantic boundary (OBLIGATION_STATUS_OUTSIDE_VOCABULARY)
       without expanding that vocabulary.

Per-mechanism rationale (what false claim / what agency / cost / why smallest)
is documented in each function docstring and in 05-CORE-OPERATIONAL-CONTRACTS.md
section 5.13.

The composed entry point is `validate_case(payload, eval_time=None)`; CLI mode
`case`; regression corpus `tools/contract-fixtures.v2.json`; deterministic
runner `tools/regression_suite.py`.

Retained trust boundaries (do NOT pretend these are eliminated): registry
content truth, evidence grades, mandate content, and observed scope are
self-declared (external attestation is outside this validator); eval_time is
caller-controlled (explicitly required, never silently defaulted).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from datetime import date
from typing import Any

# ===========================================================================
# PART 1 — SHIPPED CORE (byte-identical to v0.3.2 releases/current/tools)
# ===========================================================================

SCOPE_KEYS = ("host", "runtime_instance", "model_binding", "route", "configuration", "epoch", "time_interval", "task_scope")
DEFAULT_FIXTURES = Path(__file__).with_name("contract-fixtures.v1.json")
DEFAULT_COMPOSED_FIXTURES = Path(__file__).with_name("contract-fixtures.v2.json")


def load(path: str | Path) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        value = json.load(f)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def result(ok: bool, code: str, details: Any = None) -> dict[str, Any]:
    out = {"ok": ok, "code": code}
    if details not in (None, [], {}):
        out["details"] = details
    return out


def _scope_mismatches(observed: dict[str, Any], claimed: dict[str, Any]) -> list[dict[str, Any]]:
    mismatches: list[dict[str, Any]] = []
    for key in SCOPE_KEYS:
        c = claimed.get(key)
        if c in (None, "", "UNKNOWN"):
            continue
        o = observed.get(key)
        if o != c:
            mismatches.append({"field": key, "observed": o, "claimed": c})
    return mismatches


def validate_support(claim: dict[str, Any], support: dict[str, Any]) -> dict[str, Any]:
    if support.get("claim_ref") != claim.get("claim_id"):
        return result(False, "CLAIM_REF_MISMATCH")
    if support.get("support_status") not in {"SUPPORTS", "PARTIAL"}:
        return result(True, "NO_POSITIVE_SUPPORT_CLAIMED")

    independence = support.get("independence_basis") or {}
    claimed_independent_count = independence.get("claimed_independent_count")
    source_origins = independence.get("source_origins") or []
    if claimed_independent_count is not None:
        unique_origins = {str(x) for x in source_origins if x not in (None, "", "UNKNOWN")}
        if claimed_independent_count > len(unique_origins):
            return result(
                False,
                "INDEPENDENCE_OVERCLAIMED",
                {"claimed_independent_count": claimed_independent_count, "unique_source_origins": sorted(unique_origins)},
            )

    observed = support.get("observed_scope") or {}
    claimed = support.get("claimed_scope") or claim.get("scope") or {}
    mismatches = _scope_mismatches(observed, claimed)
    if not mismatches:
        return result(True, "SUPPORT_SCOPE_DIRECT_MATCH")
    transfer = support.get("transfer_basis") or {}
    if transfer.get("required") is True and transfer.get("type") and (transfer.get("evidence_refs") or []):
        return result(True, "SUPPORT_SCOPE_TRANSFER_DECLARED", {"mismatches": mismatches})
    return result(False, "TRANSFER_EVIDENCE_REQUIRED", {"mismatches": mismatches})


def validate_obligation(obligation: dict[str, Any]) -> dict[str, Any]:
    trigger = obligation.get("trigger") or {}
    material = obligation.get("materiality") == "MATERIAL"
    observed = trigger.get("observed") is True
    status = obligation.get("status")
    blocked_claims = obligation.get("required_before_claim_refs") or []
    if material and observed and status in {"PENDING", "FAILED", "UNKNOWN"}:
        return result(False, "MATERIAL_OBLIGATION_BLOCKS_CLAIM", {"claim_refs": blocked_claims, "status": status})
    if status == "SATISFIED" and not (obligation.get("closure_evidence_refs") or []):
        return result(False, "SATISFIED_WITHOUT_CLOSURE_EVIDENCE")
    if status in {"NOT_REQUIRED", "DEFERRED_AUTHORIZED"} and not obligation.get("resolution_reason"):
        return result(False, "CLOSURE_STATUS_REQUIRES_REASON")
    return result(True, "OBLIGATION_STATE_ACCEPTABLE")


def validate_recovery(transition: dict[str, Any]) -> dict[str, Any]:
    state = (transition.get("state_restore") or {}).get("result")
    history = (transition.get("history_continuity") or {}).get("status")
    claim_scope = (transition.get("recovery_claim") or {}).get("scope")
    if state != "SUCCESS":
        return result(False, "STATE_RESTORE_NOT_SUCCESSFUL", {"state_result": state})
    if claim_scope == "STATE_ONLY":
        return result(True, "STATE_ONLY_RECOVERY_SUPPORTED", {"history_status": history})
    if claim_scope == "STATE_AND_HISTORY":
        if history == "PRESERVED":
            return result(True, "STATE_AND_HISTORY_RECOVERY_SUPPORTED")
        return result(False, "FULL_RECOVERY_REQUIRES_PRESERVED_HISTORY", {"history_status": history})
    if claim_scope == "STATE_WITH_VISIBLE_HISTORY_GAP":
        if history in {"GAP_VISIBLE", "PARTIAL"}:
            return result(True, "RECOVERY_WITH_VISIBLE_HISTORY_GAP_SUPPORTED")
        return result(False, "VISIBLE_GAP_CLAIM_REQUIRES_GAP_EVIDENCE", {"history_status": history})
    return result(False, "UNKNOWN_RECOVERY_CLAIM_SCOPE", {"claim_scope": claim_scope})


def _run_fixture(case: dict[str, Any]) -> dict[str, Any]:
    mode = case.get("mode")
    payload = case.get("input") or {}
    if mode == "support":
        actual = validate_support(payload.get("claim") or {}, payload.get("support") or {})
    elif mode == "obligation":
        actual = validate_obligation(payload.get("obligation") or {})
    elif mode == "recovery":
        actual = validate_recovery(payload.get("transition") or {})
    elif mode == "case":
        eval_time = case.get("eval_time")
        if eval_time is None and isinstance(payload, dict):
            eval_time = payload.get("eval_time")
        actual = validate_case(payload, eval_time)
    else:
        actual = result(False, "UNKNOWN_FIXTURE_MODE", {"mode": mode})
    expected = case.get("expect") or {}
    ok_field = expected.get("ok")
    if ok_field is None and expected.get("verdict"):
        ok_field = expected.get("verdict") == "OK"
    passed = actual.get("ok") == ok_field
    if expected.get("code") and expected.get("code") not in (actual.get("code"), "ANY"):
        passed = False
    if expected.get("verdict") and expected.get("verdict") != actual.get("verdict"):
        passed = False
    return {"id": case.get("id"), "passed": passed, "expected": expected, "actual": actual}


def run_selftest(fixtures_path: str | Path) -> dict[str, Any]:
    fixture_doc = load(fixtures_path)
    cases = fixture_doc.get("cases") or []
    results = [_run_fixture(case) for case in cases]
    failed = [r for r in results if not r["passed"]]
    return {
        "ok": not failed,
        "code": "SELFTEST_PASS" if not failed else "SELFTEST_FAIL",
        "fixture_version": fixture_doc.get("fixture_version"),
        "total": len(results),
        "failed": len(failed),
        "results": results,
    }


# ===========================================================================
# PART 2 — COMPOSED LAYER (v0.3.3-candidate; accepted V2.4.1 mechanisms)
# ===========================================================================

GRADES = {"E0", "E1", "E2", "E3", "E4", "E5"}
COMPLETION_TYPES = ("WORKFLOW_COMPLETION", "TASK_COMPLETION")
# R9: positively typed authorizing mandate sources (explicitly bounded
# vocabulary; an authority_registry may verify sources outside it as upstream
# grants). False claim prevented: "authority from a restore/self-asserted
# source" endorses consequential effects. Agency preserved: explicit user grant
# and registered upstream grants. Cost: vocabulary must be maintained.
AUTHORIZING_MANDATE_SOURCES = {"USER_EXPLICIT_GRANT"}
# F2: obligation status vocabulary mirrors the shipped
# triggered-obligation.v1.schema.json enum. Statuses outside it are rejected at
# the semantic boundary (defense in depth); the vocabulary is NOT expanded.
OBLIGATION_STATUS_VOCABULARY = {"PENDING", "SATISFIED", "NOT_REQUIRED",
                                "DEFERRED_AUTHORIZED", "FAILED", "UNKNOWN"}
# R3: per-kind absent-registry policy. Support/obligation refs are named BY the
# claim itself -> mandatory -> BLOCK. Evidence/root refs verify deeper
# provenance -> absent registry -> UNKNOWN (uncertainty, not rejection).
ABSENT_POLICY = {
    "support":    ("BLOCK",   "SUPPORT_REF_UNRESOLVABLE"),
    "obligation": ("BLOCK",   "OBLIGATION_REF_UNRESOLVABLE"),
    "evidence":   ("UNKNOWN", "EVIDENCE_REGISTRY_UNAVAILABLE"),
    "root":       ("UNKNOWN", "ROOT_REGISTRY_UNAVAILABLE"),
    "authority":  ("BLOCK",   "AUTHORITY_REGISTRY_UNAVAILABLE"),
}
ID_KEYS = {
    "support":    ("support_id", "id"),
    "obligation": ("obligation_id", "id"),
    "evidence":   ("evidence_id", "id"),
    "root":       ("root_id", "id"),
    "authority":  ("grant_id", "id"),
}


def parse_date(s: str) -> date | None:
    try:
        y, m, d = s.strip().split("-")
        return date(int(y), int(m), int(d))
    except Exception:
        return None


def _worst(states: list[str]) -> str:
    """BLOCK > UNKNOWN > OK."""
    if any(s == "BLOCK" for s in states):
        return "BLOCK"
    if any(s == "UNKNOWN" for s in states):
        return "UNKNOWN"
    return "OK"


def _fingerprint(a: dict[str, Any]) -> str:
    return json.dumps(a, sort_keys=True, ensure_ascii=False, default=str)


def _id_of(artifact: dict[str, Any], kind: str) -> str | None:
    for k in ID_KEYS[kind]:
        v = artifact.get(k)
        if isinstance(v, str) and v:
            return v
    return None


def normalize_registry(raw: Any, kind: str) -> tuple[str, str, dict[str, list] | None]:
    """R11/R12 canonical registry normalization: dict | list -> {id: [artifacts]} | None.

    R12 (identity rule): for dict-form registries the dict key is the
    authoritative identity; an entry's explicit inner id must equal the key,
    otherwise the registry is REGISTRY_MALFORMED (we do not guess which identity
    is authoritative); a missing inner id is backfilled from the key. List-form
    entries must declare their inner id.

    False claim prevented: identity confusion / silent misresolution when the
    dict key and the declared id disagree (Workbuddy F1). Agency preserved:
    key==id and backfill representations keep working. Cost: one comparison per
    dict entry. Why smallest: one rule for all registry kinds, no per-kind
    special cases."""
    if raw is None:
        return ("OK", "", None)
    by_id: dict[str, list] = {}
    if isinstance(raw, dict):
        if not all(isinstance(v, dict) for v in raw.values()):
            return ("BLOCK", "REGISTRY_MALFORMED", None)
        for k, v in raw.items():
            entry = dict(v)
            inner = _id_of(entry, kind)
            if inner is not None and inner != k:
                return ("BLOCK", "REGISTRY_MALFORMED", {"key": k, "declared_id": inner, "kind": kind})
            if inner is None:
                entry[ID_KEYS[kind][0]] = k
            by_id.setdefault(k, []).append(entry)
    elif isinstance(raw, list):
        if not all(isinstance(x, dict) for x in raw):
            return ("BLOCK", "REGISTRY_MALFORMED", None)
        for x in raw:
            i = _id_of(x, kind)
            if i is None:
                return ("BLOCK", "REGISTRY_MALFORMED", None)
            by_id.setdefault(i, []).append(x)
    else:
        return ("BLOCK", "REGISTRY_MALFORMED", None)
    return ("OK", "", by_id)


def typed_resolve(ref: str, by_id: dict[str, list] | None, kind: str) -> tuple[str, str, dict[str, Any] | None]:
    """R1/R3/R5 canonical typed resolver — used for EVERY consequential ref.

    False claim prevented: cross-artifact reference confusion (a ref resolving
    to the wrong artifact type), unresolvable-but-claimed references, and
    order-dependent truth from ambiguous duplicate ids. Agency preserved:
    unique, resolvable, unambiguous references pass through. Cost: one dict
    lookup per ref. Why smallest: one resolver replaces per-mechanism ad-hoc
    resolution."""
    if by_id is None:
        state, code = ABSENT_POLICY[kind]
        return (state, code, None)
    entries = by_id.get(ref)
    if not entries:
        if kind == "obligation":
            return ("BLOCK", "OBLIGATION_REF_UNRESOLVABLE", None)
        return ("BLOCK", f"{kind.upper()}_REF_UNRESOLVABLE", None)
    if len(entries) > 1:
        if len({_fingerprint(e) for e in entries}) > 1:
            code = "DUPLICATE_OBLIGATION_ID" if kind == "obligation" else "DUPLICATE_REF_ID"
            return ("BLOCK", code, None)
        entries = entries[:1]
    return ("OK", "", entries[0])


def check_evidence_refs(refs: list[str], ev_by_id: dict[str, list] | None) -> list[tuple[str, str]]:
    """R3 evidence existence: enforced when an evidence registry is supplied;
    absent registry -> no existence verdict on this path (baseline posture).
    False claim prevented: 'evidence exists' when the supplied registry shows
    it does not. Agency preserved: evidence existence is not invented when no
    registry is provided (I06). Cost: registry lookup per ref."""
    if not refs or ev_by_id is None:
        return []
    out = []
    for r in refs:
        st, code, _ = typed_resolve(r, ev_by_id, "evidence")
        if st != "OK":
            out.append((st, code))
    return out


def check_transfer_evidence(support: dict[str, Any], ev_by_id: dict[str, list] | None) -> list[tuple[str, str]]:
    """R3/I12: transfer/equivalence evidence refs must resolve when an
    evidence registry is supplied."""
    tb = support.get("transfer_basis") or {}
    return check_evidence_refs(tb.get("evidence_refs") or [], ev_by_id)


def check_independence(support: dict[str, Any], root_by_id: dict[str, list] | None) -> tuple[str, str, dict[str, Any]]:
    """R3: independence counted on registry-verified origins; string-level
    overclaim first (no registry needed), then registry resolution. Absent
    registry -> UNKNOWN (P9 posture). False claim prevented: 'N independent
    origins' when roots are unregistered mirrors or absent. Agency preserved:
    registered distinct origins pass."""
    ind = support.get("independence_basis") or {}
    claimed = ind.get("claimed_independent_count")
    if claimed is None:
        return ("OK", "", {})
    roots = ind.get("root_provenance") or []
    if not roots:
        return ("BLOCK", "INDEPENDENCE_WITHOUT_ROOT_PROVENANCE", {})
    unique_strings = {str(x) for x in roots if x not in (None, "", "UNKNOWN")}
    if claimed > len(unique_strings):
        return ("BLOCK", "INDEPENDENCE_OVERCLAIMED", {"claimed": claimed, "unique_root_strings": sorted(unique_strings)})
    if root_by_id is None:
        return ("UNKNOWN", "ROOT_REGISTRY_UNAVAILABLE", {})
    origins = set()
    for r in roots:
        st, code, entry = typed_resolve(r, root_by_id, "root")
        if st != "OK":
            return (st, code, {"root": r})
        origins.add(entry.get("actual_origin", r))
    if claimed > len(origins):
        return ("BLOCK", "INDEPENDENCE_OVERCLAIMED", {"claimed": claimed, "origins": sorted(origins)})
    return ("OK", "", {})


def _support_sources(payload: dict[str, Any]) -> list[dict[str, Any]] | None:
    """R6/R12: top-level support + support_registry + support_relations ->
    list of artifact dicts; None on malformed shape or R12 divergence in
    dict-form maps. False claim prevented: top-level support being
    unreachable (composition failure CF-1) and dict-key/inner-id divergence.
    Agency preserved: both representations compose."""
    sources = []
    ts = payload.get("support")
    if ts is not None:
        if isinstance(ts, dict):
            sources.append(ts)
        elif isinstance(ts, list) and all(isinstance(x, dict) for x in ts):
            sources.extend(ts)
        else:
            return None
    for key in ("support_registry", "support_relations"):
        reg = payload.get(key)
        if reg is None:
            continue
        if isinstance(reg, dict) and all(isinstance(v, dict) for v in reg.values()):
            for k, v in reg.items():
                e = dict(v)
                inner = _id_of(e, "support")
                if inner is not None and inner != k:
                    return None
                if inner is None:
                    e["support_id"] = k
                sources.append(e)
        elif isinstance(reg, list) and all(isinstance(x, dict) for x in reg):
            sources.extend(reg)
        else:
            return None
    return sources


def check_support_path(claim: dict[str, Any], payload: dict[str, Any], support_by_id: dict[str, list] | None,
                       ev_by_id: dict[str, list] | None, root_by_id: dict[str, list] | None) -> list[tuple[str, str]]:
    """R1/R2/R4/R10 + evidence existence for SUPPORTED claims."""
    out: list[tuple[str, str]] = []
    refs = claim.get("support_relation_refs") or []
    if claim.get("status") == "SUPPORTED" and not refs:
        out.append(("BLOCK", "CLAIM_SUPPORTED_WITHOUT_SUPPORT_REFS"))
    for ref in refs:
        st, code, artifact = typed_resolve(ref, support_by_id, "support")
        if st != "OK":
            out.append((st, code))
            continue
        if artifact.get("claim_ref") != claim.get("claim_id"):
            out.append(("BLOCK", "SUPPORT_TARGET_MISMATCH"))
            continue
        status = artifact.get("support_status")
        if status == "CONTRADICTS":
            out.append(("BLOCK", "RESOLVED_SUPPORT_CONTRADICTS"))
            continue
        if status not in ("SUPPORTS", "PARTIAL"):
            out.append(("BLOCK", "SUPPORT_NOT_POSITIVE"))
            continue
        if status == "PARTIAL":
            if claim.get("support_claim") != "PARTIAL":
                out.append(("UNKNOWN", "PARTIAL_SUPPORT_ONLY"))
                continue
        ev_refs = artifact.get("evidence_refs") or []
        if not ev_refs:
            out.append(("BLOCK", "SUPPORT_WITHOUT_EVIDENCE"))
            continue
        out.extend(check_evidence_refs(ev_refs, ev_by_id))
        base = validate_support(claim, artifact)
        if not base["ok"]:
            out.append(("BLOCK", base["code"]))
            continue
        if base["code"] == "SUPPORT_SCOPE_TRANSFER_DECLARED":
            out.extend(check_transfer_evidence(artifact, ev_by_id))
        st2, code2, _ = check_independence(artifact, root_by_id)
        if st2 != "OK":
            out.append((st2, code2))
    return out


def check_obligation_path(claim: dict[str, Any], ob_by_id: dict[str, list] | None,
                          ev_by_id: dict[str, list] | None) -> list[tuple[str, str]]:
    """R7 claim-aware obligation blocking + closure-evidence resolution.
    False claim prevented: 'completion' while a material obligation required by
    THIS claim (or bound to it) is open; also the inverse false BLOCK from
    unrelated other-claim obligations (CF-2/I07). Agency preserved: narrower
    truthful completion survives. Cost: per-ref resolution + in-scope checks."""
    out: list[tuple[str, str]] = []
    if claim.get("claim_type") not in COMPLETION_TYPES:
        return out
    refs = claim.get("required_obligation_refs") or []
    if not refs:
        out.append(("BLOCK", "COMPLETION_CLAIM_WITHOUT_OBLIGATION_REFS"))
        return out
    for ref in refs:
        st, code, artifact = typed_resolve(ref, ob_by_id, "obligation")
        if st != "OK":
            out.append((st, code))
            continue
        base = validate_obligation(artifact)
        if not base["ok"]:
            out.append(("BLOCK", base["code"]))
        if artifact.get("status") == "SATISFIED":
            out.extend(check_evidence_refs(artifact.get("closure_evidence_refs") or [], ev_by_id))
    if ob_by_id is not None:
        for oid, entries in ob_by_id.items():
            for ob in entries:
                if claim.get("claim_id") in (ob.get("required_before_claim_refs") or []):
                    base = validate_obligation(ob)
                    if not base["ok"]:
                        out.append(("BLOCK", base["code"]))
    return out


def check_binding(binding: dict[str, Any], ev_by_id: dict[str, list] | None,
                  authority_by_id: dict[str, list] | None, eval_time: date) -> list[tuple[str, str]]:
    """R9 positive mandate typing + capability grade/evidence checks."""
    out: list[tuple[str, str]] = []
    env = binding.get("authority_envelope") or []
    if env:
        mandate = binding.get("mandate") or {}
        src = mandate.get("source")
        if not src:
            out.append(("BLOCK", "AUTHORITY_WITHOUT_MANDATE_SOURCE"))
        else:
            authorized = src in AUTHORIZING_MANDATE_SOURCES
            if not authorized and authority_by_id is not None:
                st, code, grant = typed_resolve(src, authority_by_id, "authority")
                if st == "OK":
                    g = grant
                    if g.get("agent") in (None, binding.get("agent")) and \
                       g.get("host") in (None, binding.get("host")) and \
                       parse_date(g.get("expires_at") or "2999-12-31") is not None and \
                       (parse_date(g.get("expires_at") or "2999-12-31") >= eval_time):
                        authorized = True
                    else:
                        out.append(("BLOCK", "AUTHORITY_MANDATE_SOURCE_NOT_AUTHORIZING"))
            if not authorized:
                out.append(("BLOCK", "AUTHORITY_MANDATE_SOURCE_NOT_AUTHORIZING"))
            horizon = mandate.get("expires_at")
            if not horizon:
                out.append(("BLOCK", "AUTHORITY_WITHOUT_MANDATE_HORIZON"))
            else:
                d = parse_date(horizon)
                if d is None:
                    out.append(("BLOCK", "MANDATE_DATE_UNPARSEABLE"))
                elif d < eval_time:
                    out.append(("BLOCK", "MANDATE_EXPIRED"))
    for cap in (binding.get("capabilities") or []):
        if cap.get("status") in ("VERIFIED_AVAILABLE", "VERIFIED_RESTRICTED"):
            refs = cap.get("evidence_refs") or []
            grades = [r.get("grade") for r in refs if isinstance(r, dict)]
            if not grades:
                out.append(("BLOCK", "VERIFIED_WITHOUT_EVIDENCE_GRADE"))
                continue
            invalid = [g for g in grades if g not in GRADES]
            if invalid:
                out.append(("BLOCK", "EVIDENCE_GRADE_INVALID"))
                continue
            if all(g in ("E0", "E1") for g in grades):
                out.append(("BLOCK", "VERIFIED_ONLY_STATIC_STRUCTURE_EVIDENCE"))
                continue
            out.extend(check_evidence_refs([r.get("ref") for r in refs if isinstance(r, dict) and r.get("ref")], ev_by_id))
    return out


def check_recovery_path(transition: dict[str, Any], ev_by_id: dict[str, list] | None) -> list[tuple[str, str]]:
    """R8/R3 full recovery: STATE_AND_HISTORY requires BOTH state-restoration
    and history-continuity evidence, adequately resolved; shared roots via
    registry fail closed."""
    out: list[tuple[str, str]] = []
    base = validate_recovery(transition)
    if not base["ok"]:
        out.append(("BLOCK", base["code"]))
        return out
    scope = (transition.get("recovery_claim") or {}).get("scope")
    if scope == "STATE_AND_HISTORY":
        hist = transition.get("history_continuity") or {}
        state = transition.get("state_restore") or {}
        hist_refs = hist.get("evidence_refs") or []
        state_refs = state.get("evidence_refs") or []
        if not hist_refs:
            out.append(("BLOCK", "HISTORY_PRESERVED_WITHOUT_EVIDENCE"))
        if hist.get("post_checkpoint_occurrence_delta_captured") is not True:
            out.append(("BLOCK", "HISTORY_PRESERVED_WITHOUT_DELTA_CAPTURE"))
        if not state_refs:
            out.append(("BLOCK", "STATE_RESTORE_WITHOUT_EVIDENCE"))
        if set(hist_refs) & set(state_refs):
            out.append(("BLOCK", "HISTORY_EVIDENCE_SAME_AS_STATE_EVIDENCE"))
        if ev_by_id is None:
            out.append(("UNKNOWN", "PROVENANCE_REGISTRY_UNAVAILABLE"))
        else:
            all_refs = sorted(set(hist_refs) | set(state_refs))
            for r in all_refs:
                st, code, _ = typed_resolve(r, ev_by_id, "evidence")
                if st != "OK":
                    out.append((st, code))
            hist_roots = set()
            for r in hist_refs:
                st, code, e = typed_resolve(r, ev_by_id, "evidence")
                hist_roots.add(e.get("root_provenance", r) if st == "OK" else r)
            state_roots = set()
            for r in state_refs:
                st, code, e = typed_resolve(r, ev_by_id, "evidence")
                state_roots.add(e.get("root_provenance", r) if st == "OK" else r)
            if hist_roots & state_roots:
                out.append(("BLOCK", "HISTORY_EVIDENCE_SHARED_ROOT"))
    return out


def validate_case(payload: Any, eval_time: Any = None) -> dict[str, Any]:
    """Composed claim-pack validation (R1-R12 + F2). NEVER raises (R11).

    False claim prevented: any material false claim that would survive the
    individual shipped checks alone (borrowed support, unverified evidence,
    ambiguous identity, untyped authority, partial-as-full, open obligations
    behind completion, unproven full recovery). Agency preserved: legitimate
    full-stack claim packs with complete, consistent registries reach OK; the
    three-state vocabulary keeps uncertainty honest. Cost: one pass over the
    payload's registries and references; stdlib only. Why smallest: one
    composed surface over the unchanged shipped semantic core.

    eval_time is REQUIRED (parameter or payload["eval_time"], ISO date); it is
    caller-controlled and never silently defaulted (trust boundary)."""
    try:
        return _validate_case(payload, eval_time)
    except Exception as e:  # R11: residual faults fail closed
        return {"ok": False, "verdict": "BLOCK", "code": "EVALUATOR_FAULT",
                "codes": ["EVALUATOR_FAULT", f"{type(e).__name__}: {e}"]}


def _validate_case(payload: Any, eval_time: Any) -> dict[str, Any]:
    if not isinstance(payload, dict):
        return {"ok": False, "verdict": "BLOCK", "code": "REGISTRY_MALFORMED",
                "codes": ["REGISTRY_MALFORMED", "payload not an object"]}
    et = eval_time
    if et is None:
        et = payload.get("eval_time")
    if et is None or parse_date(et) is None:
        return {"ok": False, "verdict": "BLOCK", "code": "EVAL_TIME_REQUIRED",
                "codes": ["EVAL_TIME_REQUIRED"]}
    eval_date = parse_date(et)

    # ---- R11/R12 registry extraction + shape validation (fail closed) ----
    sup = _support_sources(payload)
    if sup is None:
        return {"ok": False, "verdict": "BLOCK", "code": "REGISTRY_MALFORMED",
                "codes": ["REGISTRY_MALFORMED", "support sources"]}
    support_by_id = None
    if sup:
        st, code, by_id = normalize_registry(sup, "support")
        if st != "OK":
            return {"ok": False, "verdict": "BLOCK", "code": "REGISTRY_MALFORMED",
                    "codes": ["REGISTRY_MALFORMED", "support registry"]}
        support_by_id = by_id

    extracted = {}
    for rkey, kind, label in (("evidence_registry", "evidence", "evidence registry"),
                              ("root_registry", "root", "root registry"),
                              ("obligations", "obligation", "obligations"),
                              ("authority_registry", "authority", "authority registry")):
        st, code, by_id = normalize_registry(payload.get(rkey), kind)
        if st != "OK":
            return {"ok": False, "verdict": "BLOCK", "code": "REGISTRY_MALFORMED",
                    "codes": ["REGISTRY_MALFORMED", label]}
        extracted[kind] = by_id
    ev_by_id = extracted["evidence"]
    root_by_id = extracted["root"]
    ob_by_id = extracted["obligation"]
    authority_by_id = extracted["authority"]

    # ---- F2: obligation status vocabulary gate (defense in depth) ----
    if ob_by_id is not None:
        for entries in ob_by_id.values():
            for ob in entries:
                stt = ob.get("status")
                if stt not in OBLIGATION_STATUS_VOCABULARY:
                    return {"ok": False, "verdict": "BLOCK",
                            "code": "OBLIGATION_STATUS_OUTSIDE_VOCABULARY",
                            "codes": ["OBLIGATION_STATUS_OUTSIDE_VOCABULARY", str(stt)]}

    states: list[tuple[str, str]] = []
    claim = payload.get("claim")
    support = payload.get("support")
    binding = payload.get("binding")
    transition = payload.get("transition")

    if claim is not None:
        states.extend(check_support_path(claim, payload, support_by_id, ev_by_id, root_by_id))
        states.extend(check_obligation_path(claim, ob_by_id, ev_by_id))
    if claim is None and support is not None:
        arts = support if isinstance(support, list) else [support]
        for a in arts:
            st, code, _ = check_independence(a, root_by_id)
            if st != "OK":
                states.append((st, code))
            states.extend(check_evidence_refs(a.get("evidence_refs") or [], ev_by_id))
    if binding is not None:
        states.extend(check_binding(binding, ev_by_id, authority_by_id, eval_date))
    if transition is not None:
        states.extend(check_recovery_path(transition, ev_by_id))

    codes = [c for _, c in states if c not in ("OK", "")]
    verdict = _worst([s for s, _ in states])
    primary = codes[0] if codes else "OK"
    out: dict[str, Any] = {"ok": verdict == "OK", "verdict": verdict, "code": primary, "codes": codes}
    return out


# ===========================================================================
# CLI
# ===========================================================================

def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="mode", required=True)
    p = sub.add_parser("support"); p.add_argument("claim"); p.add_argument("support")
    p = sub.add_parser("obligation"); p.add_argument("obligation")
    p = sub.add_parser("recovery"); p.add_argument("transition")
    p = sub.add_parser("case"); p.add_argument("payload"); p.add_argument("--eval-time", default=None)
    p = sub.add_parser("selftest"); p.add_argument("fixtures", nargs="?", default=str(DEFAULT_FIXTURES))
    args = parser.parse_args()
    if args.mode == "support":
        out = validate_support(load(args.claim), load(args.support))
    elif args.mode == "obligation":
        out = validate_obligation(load(args.obligation))
    elif args.mode == "recovery":
        out = validate_recovery(load(args.transition))
    elif args.mode == "case":
        out = validate_case(load(args.payload), args.eval_time)
    else:
        out = run_selftest(args.fixtures)
    print(json.dumps(out, ensure_ascii=False, indent=2))
    if args.mode == "selftest":
        return 0 if out["ok"] else 2
    return 0 if out.get("ok", False) else 2


if __name__ == "__main__":
    sys.exit(main())
