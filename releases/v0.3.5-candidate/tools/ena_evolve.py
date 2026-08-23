#!/usr/bin/env python3
"""
ENA v0.3.5 candidate reference evolution-metabolism tool.

This tool records evolutionary signals, candidates, experiments, evidence,
selection, integration, pruning, migration, and governance-closure state.

It deliberately does NOT:
- execute arbitrary Host self-mutations;
- grant or mint external authority;
- claim that a variation is beneficial before observed evidence supports it;
- require this implementation as the only valid ENA organ.

Standard library only.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

STATE_VERSION = "1.0"
DEFAULT_DIR = Path(".ena") / "evolution"
DEFAULT_STATE = DEFAULT_DIR / "state.json"
OUTCOME_STATES = {"IMPROVED", "DEGRADED", "UNCHANGED", "UNKNOWN"}
SELECTION_STATES = {"SUPPORTED", "PARTIAL", "NOT_SUPPORTED", "HARMFUL", "UNKNOWN"}
CLOSURE_STATES = {"READY", "NARROW_AND_PROCEED", "EVIDENCE_NEEDED", "STOP_OR_ESCALATE"}


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def new_id(prefix: str) -> str:
    return f"{prefix}-{uuid.uuid4().hex[:12]}"


def empty_state() -> dict[str, Any]:
    return {
        "schema_version": STATE_VERSION,
        "created_at": now(),
        "updated_at": now(),
        "signals": [],
        "reviews": [],
        "candidates": [],
        "migration_imports": [],
        "events": [],
    }


def state_path(args: argparse.Namespace) -> Path:
    return Path(getattr(args, "state", DEFAULT_STATE))


def load_state(path: Path, create: bool = False) -> dict[str, Any]:
    if not path.exists():
        if create:
            return empty_state()
        raise SystemExit(f"State not found: {path}. Run `init` first.")
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != STATE_VERSION:
        raise SystemExit(
            f"Unsupported state schema: {data.get('schema_version')!r}; expected {STATE_VERSION!r}"
        )
    return data


def atomic_write(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data["updated_at"] = now()
    payload = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=False) + "\n"
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, delete=False
    ) as fh:
        tmp = Path(fh.name)
        fh.write(payload)
        fh.flush()
        os.fsync(fh.fileno())
    tmp.replace(path)


def add_event(state: dict[str, Any], kind: str, ref: str, detail: str = "") -> None:
    state["events"].append(
        {"event_id": new_id("evt"), "time": now(), "kind": kind, "ref": ref, "detail": detail}
    )


def find_candidate(state: dict[str, Any], cid: str) -> dict[str, Any]:
    for c in state["candidates"]:
        if c["candidate_id"] == cid:
            return c
    raise SystemExit(f"Candidate not found: {cid}")


def parse_kv(items: list[str] | None) -> dict[str, str]:
    out: dict[str, str] = {}
    for item in items or []:
        if "=" not in item:
            raise SystemExit(f"Expected KEY=VALUE, got: {item}")
        k, v = item.split("=", 1)
        if not k:
            raise SystemExit(f"Empty key in: {item}")
        out[k] = v
    return out


def print_json(obj: Any) -> None:
    print(json.dumps(obj, ensure_ascii=False, indent=2))


def cmd_init(args: argparse.Namespace) -> None:
    path = state_path(args)
    if path.exists() and not args.force:
        raise SystemExit(f"State already exists: {path}; use --force to replace.")
    state = empty_state()
    add_event(state, "INIT", "state", "Evolution metabolism initialized")
    atomic_write(path, state)
    print_json({"state": str(path), "result": "INITIALIZED"})


def cmd_observe(args: argparse.Namespace) -> None:
    path = state_path(args)
    state = load_state(path)
    sid = new_id("sig")
    signal = {
        "signal_id": sid,
        "time": now(),
        "kind": args.kind,
        "summary": args.summary,
        "source": args.source,
        "context": parse_kv(args.context),
        "reviewed": False,
    }
    state["signals"].append(signal)
    add_event(state, "OBSERVE", sid, args.summary)
    atomic_write(path, state)
    print_json(signal)


def cmd_review(args: argparse.Namespace) -> None:
    path = state_path(args)
    state = load_state(path)
    pending = [s for s in state["signals"] if not s.get("reviewed")]
    selected = pending if args.all else pending[: args.limit]
    rid = new_id("rev")
    for sig in selected:
        sig["reviewed"] = True
        sig["review_id"] = rid
    review = {
        "review_id": rid,
        "time": now(),
        "trigger": args.trigger,
        "signal_refs": [s["signal_id"] for s in selected],
        "finding": args.finding,
        "mutation_required": bool(args.mutation_required),
    }
    state["reviews"].append(review)
    add_event(state, "REVIEW", rid, args.finding or "review complete")
    atomic_write(path, state)
    print_json(review)


def cmd_propose(args: argparse.Namespace) -> None:
    path = state_path(args)
    state = load_state(path)
    cid = new_id("var")
    source_signals = args.signal or []
    known_signals = {s["signal_id"] for s in state["signals"]}
    missing = [s for s in source_signals if s not in known_signals]
    if missing:
        raise SystemExit(f"Unknown signal refs: {', '.join(missing)}")
    candidate = {
        "candidate_id": cid,
        "created_at": now(),
        "origin": "LOCAL_VARIATION",
        "status": "PROPOSED",
        "signal_refs": source_signals,
        "hypothesis": args.hypothesis,
        "change": args.change,
        "expected_outcomes": args.expected or [],
        "variation_space": args.variation_space,
        "evolutionary_subject": args.evolutionary_subject,
        "protected_subjects": args.protected_subject or [],
        "environment": parse_kv(args.environment),
        "unknowns": args.unknown or [],
        "observation_plan": args.observe,
        "experiments": [],
        "evaluations": [],
        "integration": None,
        "archive": None,
        "migration": None,
    }
    state["candidates"].append(candidate)
    add_event(state, "PROPOSE", cid, args.hypothesis)
    atomic_write(path, state)
    print_json(candidate)


def cmd_experiment(args: argparse.Namespace) -> None:
    path = state_path(args)
    state = load_state(path)
    c = find_candidate(state, args.candidate)
    eid = new_id("exp")
    exp = {
        "experiment_id": eid,
        "time": now(),
        "variation_space": args.variation_space or c.get("variation_space"),
        "actual_change": args.actual_change,
        "effect_boundary": args.effect_boundary,
        "recovery": args.recovery,
        "external_authority_basis": args.authority_basis,
        "notes": args.note or "",
    }
    c["experiments"].append(exp)
    c["status"] = "EXPERIMENTED"
    add_event(state, "EXPERIMENT", c["candidate_id"], eid)
    atomic_write(path, state)
    print_json(exp)


def cmd_evaluate(args: argparse.Namespace) -> None:
    path = state_path(args)
    state = load_state(path)
    c = find_candidate(state, args.candidate)
    outcomes: dict[str, str] = {}
    for item in args.outcome or []:
        if "=" not in item:
            raise SystemExit(f"Expected DIMENSION=STATE, got: {item}")
        dim, val = item.split("=", 1)
        val = val.upper()
        if val not in OUTCOME_STATES:
            raise SystemExit(f"Invalid outcome state {val}; choose {sorted(OUTCOME_STATES)}")
        outcomes[dim] = val
    selection = args.selection.upper()
    if selection not in SELECTION_STATES:
        raise SystemExit(f"Invalid selection: {selection}; choose {sorted(SELECTION_STATES)}")
    ev = {
        "evaluation_id": new_id("eval"),
        "time": now(),
        "outcomes": outcomes,
        "selection": selection,
        "evidence_refs": args.evidence or [],
        "negative_evidence": args.negative_evidence or [],
        "tradeoffs": args.tradeoff or [],
        "unknowns": args.unknown or [],
        "notes": args.note or "",
    }
    c["evaluations"].append(ev)
    c["status"] = selection
    add_event(state, "EVALUATE", c["candidate_id"], selection)
    atomic_write(path, state)
    print_json(ev)


def cmd_integrate(args: argparse.Namespace) -> None:
    path = state_path(args)
    state = load_state(path)
    c = find_candidate(state, args.candidate)
    current = c.get("status")
    if current not in {"SUPPORTED", "PARTIAL"} and not args.allow_unknown:
        raise SystemExit(
            f"Candidate status is {current}; integration recording normally requires SUPPORTED/PARTIAL. "
            "Use --allow-unknown only to record a deliberately bounded exception, not to relabel evidence."
        )
    integ = {
        "time": now(),
        "target": args.target,
        "authority_basis": args.authority_basis,
        "recovery_boundary": args.recovery_boundary,
        "scope": args.scope,
        "result": args.result,
        "residuals": args.residual or [],
        "evidence_state_at_commit": current,
    }
    c["integration"] = integ
    c["status"] = "INTEGRATED" if args.result == "COMMITTED" else f"INTEGRATION_{args.result}"
    add_event(state, "INTEGRATE", c["candidate_id"], args.result)
    atomic_write(path, state)
    print_json(integ)


def cmd_archive(args: argparse.Namespace) -> None:
    path = state_path(args)
    state = load_state(path)
    c = find_candidate(state, args.candidate)
    c["archive"] = {
        "time": now(),
        "reason": args.reason,
        "reversible": not args.irreversible,
        "retention_note": args.retention_note,
    }
    c["status"] = "RETIRED" if args.irreversible else "ARCHIVED"
    add_event(state, "ARCHIVE", c["candidate_id"], args.reason)
    atomic_write(path, state)
    print_json(c["archive"])


def migration_packet(candidate: dict[str, Any]) -> dict[str, Any]:
    return {
        "packet_schema": "ena-adaptation-packet.v1",
        "exported_at": now(),
        "source_candidate_id": candidate["candidate_id"],
        "source_origin": candidate.get("origin"),
        "hypothesis": candidate.get("hypothesis"),
        "change": candidate.get("change"),
        "expected_outcomes": candidate.get("expected_outcomes", []),
        "source_variation_space": candidate.get("variation_space"),
        "evolutionary_subject": candidate.get("evolutionary_subject"),
        "protected_subjects": candidate.get("protected_subjects", []),
        "source_environment": candidate.get("environment", {}),
        "evaluations": candidate.get("evaluations", []),
        "integration": candidate.get("integration"),
        "unknowns": candidate.get("unknowns", []),
        "transfer_status": "MIGRATION_CANDIDATE_NOT_LOCAL_PROOF",
    }


def cmd_export(args: argparse.Namespace) -> None:
    state = load_state(state_path(args))
    c = find_candidate(state, args.candidate)
    packet = migration_packet(c)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print_json({"output": str(out), "transfer_status": packet["transfer_status"]})


def cmd_import(args: argparse.Namespace) -> None:
    path = state_path(args)
    state = load_state(path)
    packet = json.loads(Path(args.packet).read_text(encoding="utf-8"))
    if packet.get("packet_schema") != "ena-adaptation-packet.v1":
        raise SystemExit("Unsupported migration packet schema")
    cid = new_id("mig")
    candidate = {
        "candidate_id": cid,
        "created_at": now(),
        "origin": "MIGRATION_CANDIDATE",
        "status": "PROPOSED",
        "source_packet": str(args.packet),
        "source_candidate_id": packet.get("source_candidate_id"),
        "signal_refs": [],
        "hypothesis": packet.get("hypothesis"),
        "change": packet.get("change"),
        "expected_outcomes": packet.get("expected_outcomes", []),
        "variation_space": args.variation_space,
        "evolutionary_subject": args.evolutionary_subject,
        "protected_subjects": args.protected_subject or [],
        "environment": parse_kv(args.environment),
        "source_environment": packet.get("source_environment", {}),
        "source_evaluations": packet.get("evaluations", []),
        "unknowns": list(packet.get("unknowns", [])) + (args.unknown or []),
        "observation_plan": args.observe,
        "experiments": [],
        "evaluations": [],
        "integration": None,
        "archive": None,
        "migration": {
            "transfer_status": "TRANSFERRED_NOT_LOCALLY_VALIDATED",
            "material_differences": args.difference or [],
        },
    }
    state["candidates"].append(candidate)
    state["migration_imports"].append(
        {"time": now(), "packet": str(args.packet), "candidate_id": cid}
    )
    add_event(state, "IMPORT", cid, "migration candidate imported")
    atomic_write(path, state)
    print_json(candidate)


def cmd_closure(args: argparse.Namespace) -> None:
    blockers = args.blocker or []
    evidence = args.evidence_needed or []
    narrow = args.narrow or []
    if blockers:
        verdict = "STOP_OR_ESCALATE"
    elif evidence:
        verdict = "EVIDENCE_NEEDED"
    elif narrow:
        verdict = "NARROW_AND_PROCEED"
    else:
        verdict = "READY"
    result = {
        "verdict": verdict,
        "blockers": blockers,
        "evidence_needed": evidence,
        "narrowing": narrow,
        "basis": (
            "Continue governance only while a represented bounded next check "
            "can plausibly change a material decision."
        ),
    }
    print_json(result)


def cmd_status(args: argparse.Namespace) -> None:
    state = load_state(state_path(args))
    counts: dict[str, int] = {}
    for c in state["candidates"]:
        status = c.get("status", "UNKNOWN")
        counts[status] = counts.get(status, 0) + 1
    pending = sum(1 for s in state["signals"] if not s.get("reviewed"))
    print_json(
        {
            "state_schema": state["schema_version"],
            "signals": len(state["signals"]),
            "signals_pending_review": pending,
            "reviews": len(state["reviews"]),
            "candidates": len(state["candidates"]),
            "candidate_status_counts": counts,
            "migration_imports": len(state["migration_imports"]),
            "updated_at": state.get("updated_at"),
        }
    )


def cmd_selftest(args: argparse.Namespace) -> None:
    root = Path(tempfile.mkdtemp(prefix="ena-evolve-selftest-"))
    try:
        sp = root / "state.json"
        state = empty_state()
        atomic_write(sp, state)
        loaded = load_state(sp)
        assert loaded["schema_version"] == STATE_VERSION
        sid = new_id("sig")
        loaded["signals"].append(
            {
                "signal_id": sid,
                "time": now(),
                "kind": "USER_CORRECTION",
                "summary": "test",
                "source": "selftest",
                "context": {},
                "reviewed": False,
            }
        )
        cid = new_id("var")
        loaded["candidates"].append(
            {
                "candidate_id": cid,
                "created_at": now(),
                "origin": "LOCAL_VARIATION",
                "status": "SUPPORTED",
                "signal_refs": [sid],
                "hypothesis": "test hypothesis",
                "change": "test change",
                "expected_outcomes": ["quality"],
                "variation_space": "temporary-selftest",
                "evolutionary_subject": "tool-state",
                "protected_subjects": [],
                "environment": {},
                "unknowns": [],
                "observation_plan": "selftest",
                "experiments": [],
                "evaluations": [
                    {
                        "evaluation_id": new_id("eval"),
                        "time": now(),
                        "outcomes": {"quality": "IMPROVED"},
                        "selection": "SUPPORTED",
                        "evidence_refs": ["selftest"],
                        "negative_evidence": [],
                        "tradeoffs": [],
                        "unknowns": [],
                        "notes": "",
                    }
                ],
                "integration": None,
                "archive": None,
                "migration": None,
            }
        )
        atomic_write(sp, loaded)
        packet = migration_packet(find_candidate(load_state(sp), cid))
        assert packet["transfer_status"] == "MIGRATION_CANDIDATE_NOT_LOCAL_PROOF"
        assert packet["source_candidate_id"] == cid
        assert "IMPROVED" in OUTCOME_STATES
        assert "READY" in CLOSURE_STATES
        print_json({"selftest": "PASS"})
    finally:
        shutil.rmtree(root, ignore_errors=True)


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="ena_evolve.py",
        description="ENA v0.3.5 candidate reference evolution-metabolism state tool",
    )
    p.add_argument("--state", default=str(DEFAULT_STATE), help="Evolution state JSON path")
    sub = p.add_subparsers(dest="command", required=True)

    s = sub.add_parser("init")
    s.add_argument("--force", action="store_true")
    s.set_defaults(func=cmd_init)

    s = sub.add_parser("observe")
    s.add_argument("--kind", required=True)
    s.add_argument("--summary", required=True)
    s.add_argument("--source", default="agent")
    s.add_argument("--context", action="append", default=[])
    s.set_defaults(func=cmd_observe)

    s = sub.add_parser("review")
    s.add_argument("--trigger", default="MANUAL")
    s.add_argument("--limit", type=int, default=20)
    s.add_argument("--all", action="store_true")
    s.add_argument("--finding", default="")
    s.add_argument("--mutation-required", action="store_true")
    s.set_defaults(func=cmd_review)

    s = sub.add_parser("propose")
    s.add_argument("--signal", action="append", default=[])
    s.add_argument("--hypothesis", required=True)
    s.add_argument("--change", required=True)
    s.add_argument("--expected", action="append", default=[])
    s.add_argument("--variation-space", required=True)
    s.add_argument("--evolutionary-subject", default="")
    s.add_argument("--protected-subject", action="append", default=[])
    s.add_argument("--environment", action="append", default=[])
    s.add_argument("--unknown", action="append", default=[])
    s.add_argument("--observe", default="")
    s.set_defaults(func=cmd_propose)

    s = sub.add_parser("experiment")
    s.add_argument("candidate")
    s.add_argument("--variation-space")
    s.add_argument("--actual-change", required=True)
    s.add_argument("--effect-boundary", default="")
    s.add_argument("--recovery", default="")
    s.add_argument("--authority-basis", default="")
    s.add_argument("--note", default="")
    s.set_defaults(func=cmd_experiment)

    s = sub.add_parser("evaluate")
    s.add_argument("candidate")
    s.add_argument("--outcome", action="append", default=[])
    s.add_argument("--selection", required=True)
    s.add_argument("--evidence", action="append", default=[])
    s.add_argument("--negative-evidence", action="append", default=[])
    s.add_argument("--tradeoff", action="append", default=[])
    s.add_argument("--unknown", action="append", default=[])
    s.add_argument("--note", default="")
    s.set_defaults(func=cmd_evaluate)

    s = sub.add_parser("integrate")
    s.add_argument("candidate")
    s.add_argument("--target", required=True)
    s.add_argument("--authority-basis", default="")
    s.add_argument("--recovery-boundary", default="")
    s.add_argument("--scope", default="")
    s.add_argument(
        "--result",
        choices=["COMMITTED", "DEFERRED", "REJECTED", "UNKNOWN"],
        default="COMMITTED",
    )
    s.add_argument("--residual", action="append", default=[])
    s.add_argument("--allow-unknown", action="store_true")
    s.set_defaults(func=cmd_integrate)

    s = sub.add_parser("archive")
    s.add_argument("candidate")
    s.add_argument("--reason", required=True)
    s.add_argument("--irreversible", action="store_true")
    s.add_argument("--retention-note", default="")
    s.set_defaults(func=cmd_archive)

    s = sub.add_parser("export")
    s.add_argument("candidate")
    s.add_argument("--output", required=True)
    s.set_defaults(func=cmd_export)

    s = sub.add_parser("import")
    s.add_argument("packet")
    s.add_argument("--variation-space", required=True)
    s.add_argument("--evolutionary-subject", default="")
    s.add_argument("--protected-subject", action="append", default=[])
    s.add_argument("--environment", action="append", default=[])
    s.add_argument("--difference", action="append", default=[])
    s.add_argument("--unknown", action="append", default=[])
    s.add_argument("--observe", default="")
    s.set_defaults(func=cmd_import)

    s = sub.add_parser("closure")
    s.add_argument("--blocker", action="append", default=[])
    s.add_argument("--evidence-needed", action="append", default=[])
    s.add_argument("--narrow", action="append", default=[])
    s.set_defaults(func=cmd_closure)

    s = sub.add_parser("status")
    s.set_defaults(func=cmd_status)

    s = sub.add_parser("selftest")
    s.set_defaults(func=cmd_selftest)
    return p


def main() -> None:
    args = parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
