#!/usr/bin/env python3
"""Recovered/reconstructed Commitment / Settlement research validator.

This is a new reconstruction from durable README + Issue #91 semantics after
the earlier local prototype was found not to be durably present in GitHub.
It is NOT a byte-for-byte recovery of the lost artifact.

Verification boundary:
- represented assignment/settlement consistency only;
- no external authority truth;
- no target-side fencing proof;
- no counterparty authenticity;
- no real-world partition-disjointness proof.
"""
from __future__ import annotations

from typing import Any

COMMITMENT_STATUS = {
    "OPEN", "WAITING", "PARTIAL", "UNKNOWN", "SETTLED", "CANCELLED", "TRANSFERRED"
}
ASSIGNMENT_STATUS = {
    "ACTIVE", "SUPERSEDED", "REVOKED", "EXPIRED", "SETTLED"
}
PARTITION_MODE = {"INDIVISIBLE", "PARTITIONED"}
TRANSFER_STATUS = {"PROPOSED", "ACCEPTED", "REJECTED"}


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_document(doc: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if not isinstance(doc, dict):
        return ["document must be object"]
    commitments = doc.get("commitments")
    if not isinstance(commitments, list) or not commitments:
        return ["commitments must be a non-empty array"]

    seen_commitments: set[str] = set()
    for ci, c in enumerate(commitments):
        prefix = f"commitments[{ci}]"
        if not isinstance(c, dict):
            errors.append(f"{prefix} must be object")
            continue
        cid = c.get("commitment_id")
        if not _nonempty(cid):
            errors.append(f"{prefix}.commitment_id required")
            continue
        if cid in seen_commitments:
            errors.append(f"duplicate commitment_id: {cid}")
            continue
        seen_commitments.add(cid)

        for field in ("obligation_subject_ref", "counterparty_ref"):
            if not _nonempty(c.get(field)):
                errors.append(f"{cid}: {field} required")

        status = c.get("status")
        if status not in COMMITMENT_STATUS:
            errors.append(f"{cid}: invalid status {status!r}")

        partition = c.get("partition") or {"mode": "INDIVISIBLE"}
        if not isinstance(partition, dict):
            errors.append(f"{cid}: partition must be object")
            partition = {"mode": "INDIVISIBLE"}
        mode = partition.get("mode", "INDIVISIBLE")
        if mode not in PARTITION_MODE:
            errors.append(f"{cid}: invalid partition mode {mode!r}")
        if mode == "PARTITIONED" and not _nonempty(partition.get("disjointness_basis")):
            errors.append(f"{cid}: PARTITIONED requires represented disjointness_basis")

        assignments = c.get("assignments")
        if not isinstance(assignments, list):
            errors.append(f"{cid}: assignments must be array")
            assignments = []

        assignment_ids: set[str] = set()
        generations: set[int] = set()
        active: list[dict[str, Any]] = []
        max_generation = None
        for ai, a in enumerate(assignments):
            ap = f"{cid}: assignment[{ai}]"
            if not isinstance(a, dict):
                errors.append(f"{ap} must be object")
                continue
            aid = a.get("assignment_id")
            if not _nonempty(aid):
                errors.append(f"{ap}.assignment_id required")
            elif aid in assignment_ids:
                errors.append(f"{cid}: duplicate assignment_id {aid}")
            else:
                assignment_ids.add(aid)

            gen = a.get("generation")
            if not isinstance(gen, int) or gen < 0:
                errors.append(f"{ap}: non-negative integer generation required")
            elif gen in generations:
                errors.append(f"{cid}: duplicate assignment generation {gen}")
            else:
                generations.add(gen)
                max_generation = gen if max_generation is None else max(max_generation, gen)

            if not _nonempty(a.get("executor_ref")):
                errors.append(f"{ap}: executor_ref required")
            ast = a.get("status")
            if ast not in ASSIGNMENT_STATUS:
                errors.append(f"{ap}: invalid status {ast!r}")
            if ast == "ACTIVE":
                active.append(a)
                if a.get("lease_state") in {"EXPIRED", "REVOKED"}:
                    errors.append(f"{ap}: ACTIVE assignment cannot have lease_state {a.get('lease_state')}")
                if a.get("counterparty_acceptance_required") is True and a.get("counterparty_acceptance") != "ACCEPTED":
                    errors.append(f"{ap}: ACTIVE assignment requires represented counterparty acceptance")

            if mode == "PARTITIONED":
                if not _nonempty(a.get("partition_id")):
                    errors.append(f"{ap}: partition_id required under PARTITIONED")
            elif a.get("partition_id") not in {None, ""}:
                errors.append(f"{ap}: partition_id not allowed under INDIVISIBLE")

        if mode == "INDIVISIBLE" and len(active) > 1:
            errors.append(f"{cid}: multiple ACTIVE assignments for indivisible commitment")
        if mode == "PARTITIONED":
            active_partitions = [a.get("partition_id") for a in active if _nonempty(a.get("partition_id"))]
            if len(active_partitions) != len(set(active_partitions)):
                errors.append(f"{cid}: multiple ACTIVE assignments for same partition")
        if max_generation is not None:
            for a in active:
                if a.get("generation") != max_generation and mode == "INDIVISIBLE":
                    errors.append(f"{cid}: stale generation cannot remain ACTIVE after newer assignment")
                if a.get("generation") != max_generation and mode == "PARTITIONED":
                    errors.append(f"{cid}: recovered model requires ACTIVE partition assignments at latest generation")

        transfers = c.get("obligation_transfers") or []
        if not isinstance(transfers, list):
            errors.append(f"{cid}: obligation_transfers must be array")
            transfers = []
        transfer_ids: set[str] = set()
        accepted_transfers: list[dict[str, Any]] = []
        for ti, t in enumerate(transfers):
            tp = f"{cid}: transfer[{ti}]"
            if not isinstance(t, dict):
                errors.append(f"{tp} must be object")
                continue
            tid = t.get("transfer_id")
            if not _nonempty(tid):
                errors.append(f"{tp}: transfer_id required")
            elif tid in transfer_ids:
                errors.append(f"{cid}: duplicate transfer_id {tid}")
            else:
                transfer_ids.add(tid)
            if not _nonempty(t.get("from_subject_ref")) or not _nonempty(t.get("to_subject_ref")):
                errors.append(f"{tp}: from/to subject refs required")
            if t.get("status") not in TRANSFER_STATUS:
                errors.append(f"{tp}: invalid transfer status")
            if t.get("status") == "ACCEPTED":
                accepted_transfers.append(t)
                if not _nonempty(t.get("basis_ref")):
                    errors.append(f"{tp}: ACCEPTED transfer requires basis_ref")
                if not isinstance(t.get("evidence_refs"), list) or not t.get("evidence_refs"):
                    errors.append(f"{tp}: ACCEPTED transfer requires evidence_refs")

        if accepted_transfers:
            latest = accepted_transfers[-1]
            if c.get("obligation_subject_ref") != latest.get("to_subject_ref"):
                errors.append(
                    f"{cid}: obligation_subject_ref must match latest accepted transfer target"
                )

        settlement = c.get("settlement") or {}
        if not isinstance(settlement, dict):
            errors.append(f"{cid}: settlement must be object")
            settlement = {}
        settlement_state = settlement.get("state", status if status in {"PARTIAL","UNKNOWN","SETTLED","CANCELLED"} else "OPEN")

        if status in {"SETTLED", "CANCELLED"}:
            if settlement_state != status:
                errors.append(f"{cid}: {status} status requires matching settlement.state")
            refs = settlement.get("evidence_refs")
            if not isinstance(refs, list) or not refs or not all(_nonempty(x) for x in refs):
                errors.append(f"{cid}: {status} requires non-empty settlement evidence_refs")

        if status == "TRANSFERRED":
            if not accepted_transfers:
                errors.append(f"{cid}: TRANSFERRED requires accepted obligation transfer")

        if status in {"SETTLED", "CANCELLED"} and not settlement.get("evidence_refs"):
            errors.append(f"{cid}: assignment/lease terminal state does not itself settle commitment")

    return errors


def next_action(doc: dict[str, Any]) -> str:
    errors = validate_document(doc)
    if errors:
        return "REJECT_INCONSISTENT_RECORD"

    cid = doc.get("decision_commitment_id")
    commitments = {c["commitment_id"]: c for c in doc["commitments"]}
    c = commitments.get(cid) if cid else next(iter(commitments.values()))
    if c is None:
        return "REJECT_INCONSISTENT_RECORD"

    status = c["status"]
    if status in {"SETTLED", "CANCELLED"}:
        return "NO_OBLIGATION_ACTION"
    if status == "TRANSFERRED":
        return "VERIFY_TRANSFER_AND_LOCAL_BINDING"
    if status in {"UNKNOWN", "PARTIAL"}:
        return "RECONCILE_SETTLEMENT"

    active = [a for a in c.get("assignments", []) if a.get("status") == "ACTIVE"]
    if not active:
        return "ASSIGN_OR_WAIT"

    return "CONTINUE_WITH_CURRENT_ASSIGNMENT"
