#!/usr/bin/env python3
"""V2.3 Acceptance Semantics Layer — research prototype (UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED).

Establishes EXPLICIT acceptance semantics for the composed cumulative contract
(V2.2 cumulative_contract.py — the SAME candidate implementation, ZERO changes):

  BLOCK   <- materially false/invalid claim, OR a claim requiring mandatory
             support whose references cannot be resolved (fail-closed).
  OK      <- legitimate claim with sufficient resolvable support.
  UNKNOWN <- legitimate but materially UNVERIFIABLE claim where uncertainty is
             allowed (verification capability absent, not reference broken).

UNKNOWN is DELIBERATELY distinct from BLOCK:
  * BLOCK   = the claim cannot be accepted (mandatory precondition unfulfilled).
  * UNKNOWN = the claim is well-formed but a deeper property (root distinctness,
              origin uniqueness) cannot be verified without the required registry;
              honesty requires uncertainty, not rejection of a legitimate claim.

This layer does NOT modify the candidate. It only declares WHAT verdict each
fixture is EXPECTED to receive, and why. The verdict-correctness replay
(run_v23.py) reports expected-vs-actual for every fixture; success = zero
unexpected verdicts.
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# Semantic categories (per-fixture, deterministic from fixture structure)
# ---------------------------------------------------------------------------
#   adversarial            : ATTACK / ADVERSARIAL / SECOND_ORDER -> BLOCK
#   mandatory_unresolvable : legitimate claim REQUIRING support whose refs
#                            cannot resolve (no registry)          -> BLOCK
#   uncertainty_positive   : legitimate claim, materially unverifiable
#                            (registry absent)                     -> UNKNOWN
#   sufficient_positive    : legitimate claim with sufficient resolvable
#                            support                                -> OK
#   migrated_positive      : migrated equivalent of a historical positive,
#                            supplying required registries          -> OK

CATEGORY_VERDICT = {
    "adversarial":            "BLOCK",
    "mandatory_unresolvable": "BLOCK",
    "uncertainty_positive":   "UNKNOWN",
    "sufficient_positive":    "OK",
    "migrated_positive":      "OK",
}

CATEGORY_RATIONALE = {
    "adversarial": "materially false/invalid claim; contract must refuse endorsement",
    "mandatory_unresolvable": "claim requires mandatory resolvable support (SUPPORTED/completion); references cannot be resolved (registry absent) -> fail-closed BLOCK; uncertainty is NOT allowed for a mandatory precondition",
    "uncertainty_positive": "legitimate claim; verification capability (registry) absent so a deeper property cannot be verified; uncertainty allowed -> UNKNOWN, deliberately not BLOCK",
    "sufficient_positive": "legitimate claim with sufficient resolvable support; every required reference resolves and every resolved artifact carries the required evidence",
    "migrated_positive": "migrated equivalent supplying the registry/provenance/support information the cumulative contract now legitimately requires; must reach OK",
}

# Migrated positives: historical fixtures P1/P5/P6/P7/P9 supplied with the
# registries the cumulative contract legitimately requires (NOT a weakening of
# protections — a completing of the claim pack).
MIGRATED_IDS = {
    "P1m-supported-with-refs",
    "P5m-completion-satisfied",
    "P6m-nonmaterial-obligation-ok",
    "P7m-recovery-with-history-evidence",
    "P9m-independence-distinct-roots",
}

COMPLETION_TYPES = ("WORKFLOW_COMPLETION", "TASK_COMPLETION")


def classify(fx: dict) -> str:
    """Deterministic semantic category for ONE fixture, derived from structure.
    The explicit expected-verdict manifest must agree with this derivation."""
    # 1. adversarial kinds are always expected BLOCK (checked first: an attack
    #    may also carry registry fields; its semantics are still adversarial)
    if fx.get("kind") in ("ADVERSARIAL", "ATTACK", "SECOND_ORDER"):
        return "adversarial"
    # 2. migrated positives are declared controls
    if fx.get("id") in MIGRATED_IDS:
        return "migrated_positive"
    # 3. historical positives
    p = fx.get("payload", {})
    claim = p.get("claim") or {}
    # 3a. mandatory resolvable support: SUPPORTED status or completion claim
    #     requires that its support refs resolve; no registry -> fail-closed.
    if claim and (
        claim.get("status") == "SUPPORTED"
        or claim.get("claim_type") in COMPLETION_TYPES
    ):
        has_support_source = (
            p.get("support_registry") is not None
            or "support_relations" in p
            or "support" in p
        )
        if not has_support_source:
            return "mandatory_unresolvable"
    # 3b. uncertainty-positive: STATE_AND_HISTORY recovery or independence
    #     count requires a registry to verify roots; registry absent -> UNKNOWN.
    transition = p.get("transition") or {}
    if (transition.get("recovery_claim") or {}).get("scope") == "STATE_AND_HISTORY":
        if "evidence_registry" not in p:
            return "uncertainty_positive"
    support = p.get("support") or {}
    ind = support.get("independence_basis") or {}
    if ind.get("claimed_independent_count") is not None and "root_registry" not in p:
        return "uncertainty_positive"
    # 4. everything else: legitimate with sufficient resolvable support
    return "sufficient_positive"


def expected_verdict(fx: dict) -> str:
    """Expected verdict (BLOCK/OK/UNKNOWN) for one fixture."""
    return CATEGORY_VERDICT[classify(fx)]


def build_expected_manifest(fixtures: list) -> list:
    """Expected-verdict manifest: one entry per fixture (deterministic)."""
    manifest = []
    for fx in fixtures:
        cat = classify(fx)
        manifest.append({
            "id": fx["id"],
            "kind": fx.get("kind"),
            "semantic_category": cat,
            "expected_verdict": CATEGORY_VERDICT[cat],
            "rationale": CATEGORY_RATIONALE[cat],
        })
    return manifest
