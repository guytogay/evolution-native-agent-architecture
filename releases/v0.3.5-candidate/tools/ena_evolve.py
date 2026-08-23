#!/usr/bin/env python3
"""ENA v0.3.5 candidate reference evolution-metabolism tool.

This is a small state/evidence tool, not a self-modification engine or an
authority oracle. It records signals, variations, experiments, observed
outcomes, selection, integration, pruning, migration, and governance closure.

It deliberately does NOT:
- execute arbitrary Host self-mutations;
- mint external authority;
- infer that omitted blockers do not exist;
- call a variation beneficial before outcome/evidence is represented;
- turn a failed source variation into a positive migration candidate;
- require this implementation as the only valid ENA organ.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

STATE_VERSION = "1.1"
DEFAULT_STATE = Path(".ena") / "evolution" / "state.json"
OUTCOME_STATES = {"IMPROVED", "DEGRADED", "UNCHANGED", "UNKNOWN"}
SELECTION_STATES = {"SUPPORTED", "PARTIAL", "NOT_SUPPORTED", "HARMFUL", "UNKNOWN"}
NEGATIVE_SELECTION = {"NOT_SUPPORTED", "HARMFUL"}
POSITIVE_SELECTION = {"SUPPORTED", "PARTIAL"}


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def new_id(prefix: str) -> str:
    return f"{prefix}-{uuid.uuid4().hex[:12]}"


def empty_state() -> dict[str, Any]:
    t = now()
    return {
        "schema_version": STATE_VERSION,
        "created_at": t,
        "updated_at": t,
        "signals": [],
        "reviews": [],
        "candidates": [],
        "migration_imports": [],
        "events": [],
    }


def state_path(args: argparse.Namespace) -> Path:
    return Path(getattr(args, "state", DEFAULT_STATE))


def load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
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
    payload = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as fh:
        tmp = Path(fh.name)
        fh.write(payload)
        fh.flush()
        os.fsync(fh.fileno())
    tmp.replace(path)


def print_json(obj: Any) -> None:
    print(json.dumps(obj, ensure_ascii=False, indent=2))


def add_event(state: dict[str, Any], kind: str, ref: str, detail: str = "") -> None:
    state["events"].append(
        {"event_id": new_id("evt"), "time": now(), "kind": kind, "ref": ref, "detail": detail}
    )


def find_candidate(state: dict[str, Any], cid: str) -> dict[str, Any]:
    for candidate in state["candidates"]:
        if candidate["candidate_id"] == cid:
            return candidate
    raise SystemExit(f"Candidate not found: {cid}")


def parse_kv(items: list[str] | None) -> dict[str, str]:
    out: dict[str, str] = {}
    for item in items or []:
        if "=" not in item:
            raise SystemExit(f"Expected KEY=VALUE, got: {item}")
        key, value = item.split("=", 1)
        if not key:
            raise SystemExit(f"Empty key in: {item}")
        out[key] = value
    return out


def canonical_digest(obj: dict[str, Any]) -> str:
    payload = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def validate_evaluation(selection: str, outcomes: dict[str, str], evidence: list[str]) -> None:
    """Prevent the reference state tool from manufacturing unsupported selection labels."""
    if selection == "UNKNOWN":
        return
    if not outcomes:
        raise SystemExit(f"{selection} requires at least one observed outcome dimension")
    if not evidence:
        raise SystemExit(f"{selection} requires at least one evidence reference")
    vals = set(outcomes.values())
    if selection in POSITIVE_SELECTION and "IMPROVED" not in vals:
        raise SystemExit(f"{selection} requires at least one represented IMPROVED outcome")
    if selection == "HARMFUL" and "DEGRADED" not in vals:
        raise SystemExit("HARMFUL requires at least one represented DEGRADED outcome")


def cmd_init(args: argparse.Namespace) -> None:
    path = state_path(args)
    if path.exists() and not args.force:
        raise SystemExit(f"State already exists: {path}; use --force to replace")
    state = empty_state()
    add_event(state, "INIT", "state", "Evolution metabolism initialized")
    atomic_write(path, state)
    print_json({"state": str(path), "result": "INITIALIZED", "schema_version": STATE_VERSION})


def cmd_observe(args: argparse.Namespace) -> None:
    path = state_path(args)
    state = load_state(path)
    signal = {
        "signal_id": new_id("sig"),
        "time": now(),
        "kind": args.kind,
        "summary": args.summary,
        "source": args.source,
        "context": parse_kv(args.context),
        "reviewed": False,
    }
    state["signals"].append(signal)
    add_event(state, "OBSERVE", signal["signal_id"], signal["summary"])
    atomic_write(path, state)
    print_json(signal)


def cmd_review(args: argparse.Namespace) -> None:
    path = state_path(args)
    state = load_state(path)
    pending = [s for s in state["signals"] if not s.get("reviewed")]
    selected = pending if args.all else pending[: args.limit]
    rid = new_id("rev")
    for signal in selected:
        signal["reviewed"] = True
        signal["review_id"] = rid
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
    source_signals = args.signal or []
    known_signals = {s["signal_id"] for s in state["signals"]}
    missing = [ref for ref in source_signals if ref not in known_signals]
    if missing:
        raise SystemExit(f"Unknown signal refs: {', '.join(missing)}")
    candidate = {
        "candidate_id": new_id("var"),
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
        "dependencies": args.dependency or [],
        "unknowns": args.unknown or [],
        "observation_plan": args.observe,
        "experiments": [],
        "evaluations": [],
        "integration": None,
        "archive": None,
        "migration": None,
    }
    state["candidates"].append(candidate)
    add_event(state, "PROPOSE", candidate["candidate_id"], candidate["hypothesis"])
    atomic_write(path, state)
    print_json(candidate)


def cmd_experiment(args: argparse.Namespace) -> None:
    path = state_path(args)
    state = load_state(path)
    candidate = find_candidate(state, args.candidate)
    if candidate.get("status") in NEGATIVE_SELECTION:
        raise SystemExit("Negatively selected candidate must be revised into a new variation before re-experiment")
    experiment = {
        "experiment_id": new_id("exp"),
        "time": now(),
        "variation_space": args.variation_space or candidate.get("variation_space"),
        "actual_change": args.actual_change,
        "effect_boundary": args.effect_boundary,
        "recovery": args.recovery,
        "external_authority_basis": args.authority_basis,
        "notes": args.note or "",
    }
    candidate["experiments"].append(experiment)
    candidate["status"] = "EXPERIMENTED"
    add_event(state, "EXPERIMENT", candidate["candidate_id"], experiment["experiment_id"])
    atomic_write(path, state)
    print_json(experiment)


def cmd_evaluate(args: argparse.Namespace) -> None:
    path = state_path(args)
    state = load_state(path)
    candidate = find_candidate(state, args.candidate)
    outcomes: dict[str, str] = {}
    for item in args.outcome or []:
        if "=" not in item:
            raise SystemExit(f"Expected DIMENSION=STATE, got: {item}")
        dim, value = item.split("=", 1)
        value = value.upper()
        if value not in OUTCOME_STATES:
            raise SystemExit(f"Invalid outcome state {value}; choose {sorted(OUTCOME_STATES)}")
        outcomes[dim] = value
    selection = args.selection.upper()
    if selection not in SELECTION_STATES:
        raise SystemExit(f"Invalid selection: {selection}; choose {sorted(SELECTION_STATES)}")
    evidence = args.evidence or []
    validate_evaluation(selection, outcomes, evidence)
    evaluation = {
        "evaluation_id": new_id("eval"),
        "time": now(),
        "outcomes": outcomes,
        "selection": selection,
        "evidence_refs": evidence,
        "negative_evidence": args.negative_evidence or [],
        "tradeoffs": args.tradeoff or [],
        "unknowns": args.unknown or [],
        "notes": args.note or "",
        "evidence_boundary": "REFERENCED_NOT_EXTERNALLY_VERIFIED_BY_THIS_TOOL",
    }
    candidate["evaluations"].append(evaluation)
    candidate["status"] = selection
    add_event(state, "EVALUATE", candidate["candidate_id"], selection)
    atomic_write(path, state)
    print_json(evaluation)


def cmd_integrate(args: argparse.Namespace) -> None:
    path = state_path(args)
    state = load_state(path)
    candidate = find_candidate(state, args.candidate)
    current = candidate.get("status")
    if current in NEGATIVE_SELECTION:
        raise SystemExit(f"Candidate status is {current}; create a revised variation instead of overriding selection")
    if current not in POSITIVE_SELECTION:
        if not args.allow_unknown or current != "UNKNOWN":
            raise SystemExit(
                f"Candidate status is {current}; integration normally requires SUPPORTED/PARTIAL. "
                "--allow-unknown is only valid after an explicit UNKNOWN evaluation."
            )
        if not candidate.get("experiments") or not candidate.get("evaluations"):
            raise SystemExit("Unknown integration requires at least one experiment and one explicit UNKNOWN evaluation")
    integration = {
        "time": now(),
        "target": args.target,
        "authority_basis": args.authority_basis,
        "recovery_boundary": args.recovery_boundary,
        "scope": args.scope,
        "result": args.result,
        "residuals": args.residual or [],
        "evidence_state_at_commit": current,
        "authority_boundary": "RECORDED_NOT_VERIFIED_BY_THIS_TOOL",
    }
    candidate["integration"] = integration
    candidate["status"] = "INTEGRATED" if args.result == "COMMITTED" else f"INTEGRATION_{args.result}"
    add_event(state, "INTEGRATE", candidate["candidate_id"], args.result)
    atomic_write(path, state)
    print_json(integration)


def cmd_archive(args: argparse.Namespace) -> None:
    path = state_path(args)
    state = load_state(path)
    candidate = find_candidate(state, args.candidate)
    candidate["archive"] = {
        "time": now(),
        "reason": args.reason,
        "record_retention": "RETAIN" if not args.retire_record else "RETIRE_RECORD_IF_POLICY_ALLOWS",
        "retention_note": args.retention_note,
    }
    candidate["status"] = "RETIRED" if args.retire_record else "ARCHIVED"
    add_event(state, "ARCHIVE", candidate["candidate_id"], args.reason)
    atomic_write(path, state)
    print_json(candidate["archive"])


def migration_packet(candidate: dict[str, Any]) -> dict[str, Any]:
    source_status = candidate.get("status", "UNKNOWN")
    if source_status in POSITIVE_SELECTION or source_status == "INTEGRATED":
        purpose = "ADAPTATION_CANDIDATE"
    elif source_status in NEGATIVE_SELECTION:
        purpose = "NEGATIVE_EVIDENCE"
    else:
        purpose = "UNRESOLVED_VARIATION"
    packet = {
        "packet_schema": "ena-adaptation-packet.v1",
        "exported_at": now(),
        "packet_purpose": purpose,
        "source_candidate_id": candidate["candidate_id"],
        "source_origin": candidate.get("origin"),
        "source_status": source_status,
        "hypothesis": candidate.get("hypothesis"),
        "change": candidate.get("change"),
        "expected_outcomes": candidate.get("expected_outcomes", []),
        "source_variation_space": candidate.get("variation_space"),
        "evolutionary_subject": candidate.get("evolutionary_subject"),
        "protected_subjects": candidate.get("protected_subjects", []),
        "source_environment": candidate.get("environment", {}),
        "dependencies": candidate.get("dependencies", []),
        "source_evaluations": candidate.get("evaluations", []),
        "source_integration": candidate.get("integration"),
        "unknowns": candidate.get("unknowns", []),
        "transfer_status": "TRANSFERRED_SOURCE_EVIDENCE_NOT_LOCAL_PROOF",
    }
    packet["content_sha256"] = canonical_digest(packet)
    return packet


def validate_packet(packet: dict[str, Any]) -> None:
    if packet.get("packet_schema") != "ena-adaptation-packet.v1":
        raise SystemExit("Unsupported migration packet schema")
    claimed = packet.get("content_sha256")
    if not claimed:
        raise SystemExit("Migration packet missing content_sha256")
    base = dict(packet)
    base.pop("content_sha256", None)
    actual = canonical_digest(base)
    if claimed != actual:
        raise SystemExit("Migration packet content digest mismatch")
    required = {"packet_purpose", "source_candidate_id", "source_status", "transfer_status"}
    missing = sorted(k for k in required if not packet.get(k))
    if missing:
        raise SystemExit(f"Migration packet missing required fields: {', '.join(missing)}")


def cmd_export(args: argparse.Namespace) -> None:
    state = load_state(state_path(args))
    candidate = find_candidate(state, args.candidate)
    packet = migration_packet(candidate)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print_json(
        {
            "output": str(out),
            "packet_purpose": packet["packet_purpose"],
            "source_status": packet["source_status"],
            "content_sha256": packet["content_sha256"],
            "transfer_status": packet["transfer_status"],
        }
    )


def cmd_import(args: argparse.Namespace) -> None:
    path = state_path(args)
    state = load_state(path)
    packet = json.loads(Path(args.packet).read_text(encoding="utf-8"))
    validate_packet(packet)
    purpose = packet["packet_purpose"]
    if purpose == "ADAPTATION_CANDIDATE":
        local_status = "PROPOSED"
    elif purpose == "NEGATIVE_EVIDENCE":
        local_status = "MIGRATION_NEGATIVE_EVIDENCE"
    else:
        local_status = "MIGRATION_UNRESOLVED"
    candidate = {
        "candidate_id": new_id("mig"),
        "created_at": now(),
        "origin": "MIGRATION_CANDIDATE",
        "status": local_status,
        "source_packet": str(args.packet),
        "source_packet_sha256": packet["content_sha256"],
        "source_candidate_id": packet["source_candidate_id"],
        "signal_refs": [],
        "hypothesis": packet.get("hypothesis"),
        "change": packet.get("change"),
        "expected_outcomes": packet.get("expected_outcomes", []),
        "variation_space": args.variation_space,
        "evolutionary_subject": args.evolutionary_subject,
        "protected_subjects": args.protected_subject or [],
        "environment": parse_kv(args.environment),
        "dependencies": packet.get("dependencies", []),
        "source_environment": packet.get("source_environment", {}),
        "source_evaluations": packet.get("source_evaluations", []),
        "unknowns": list(packet.get("unknowns", [])) + (args.unknown or []),
        "observation_plan": args.observe,
        "experiments": [],
        "evaluations": [],
        "integration": None,
        "archive": None,
        "migration": {
            "source_status": packet["source_status"],
            "packet_purpose": purpose,
            "transfer_status": "TRANSFERRED_NOT_LOCALLY_VALIDATED",
            "material_differences": args.difference or [],
        },
    }
    state["candidates"].append(candidate)
    state["migration_imports"].append(
        {
            "time": now(),
            "packet": str(args.packet),
            "packet_sha256": packet["content_sha256"],
            "candidate_id": candidate["candidate_id"],
            "packet_purpose": purpose,
        }
    )
    add_event(state, "IMPORT", candidate["candidate_id"], purpose)
    atomic_write(path, state)
    print_json(candidate)


def cmd_closure(args: argparse.Namespace) -> None:
    blockers = args.blocker or []
    evidence = args.evidence_needed or []
    narrow = args.narrow or []
    if blockers:
        outcome = "STOP_OR_ESCALATE"
    elif evidence:
        outcome = "EVIDENCE_NEEDED"
    elif narrow:
        outcome = "NARROW_AND_PROCEED"
    else:
        outcome = "READY"
    print_json(
        {
            "semantic_outcome": outcome,
            "evidence_scope": "REPRESENTED_INPUTS_ONLY",
            "unrepresented_material_blockers": "UNKNOWN",
            "blockers": blockers,
            "evidence_needed": evidence,
            "narrowing": narrow,
            "claim_boundary": (
                "This tool does not prove that omitted blockers/evidence needs do not exist. "
                "READY means ready on the caller's represented material decision inputs only."
            ),
        }
    )


def cmd_status(args: argparse.Namespace) -> None:
    state = load_state(state_path(args))
    counts: dict[str, int] = {}
    for candidate in state["candidates"]:
        status = candidate.get("status", "UNKNOWN")
        counts[status] = counts.get(status, 0) + 1
    print_json(
        {
            "state_schema": state["schema_version"],
            "signals": len(state["signals"]),
            "signals_pending_review": sum(1 for s in state["signals"] if not s.get("reviewed")),
            "reviews": len(state["reviews"]),
            "candidates": len(state["candidates"]),
            "candidate_status_counts": counts,
            "migration_imports": len(state["migration_imports"]),
            "updated_at": state.get("updated_at"),
        }
    )


def cmd_selftest(_args: argparse.Namespace) -> None:
    root = Path(tempfile.mkdtemp(prefix="ena-evolve-selftest-"))
    try:
        path = root / "state.json"
        state = empty_state()
        atomic_write(path, state)
        assert load_state(path)["schema_version"] == STATE_VERSION

        # Positive packet keeps source status and is content-bound.
        candidate = {
            "candidate_id": "var-selftest",
            "origin": "LOCAL_VARIATION",
            "status": "SUPPORTED",
            "hypothesis": "test",
            "change": "test change",
            "expected_outcomes": ["quality"],
            "variation_space": "selftest",
            "evolutionary_subject": "tool-state",
            "protected_subjects": [],
            "environment": {"host": "selftest"},
            "dependencies": [],
            "unknowns": [],
            "evaluations": [
                {
                    "outcomes": {"quality": "IMPROVED"},
                    "selection": "SUPPORTED",
                    "evidence_refs": ["selftest-observation"],
                }
            ],
            "integration": None,
        }
        packet = migration_packet(candidate)
        validate_packet(packet)
        assert packet["packet_purpose"] == "ADAPTATION_CANDIDATE"
        assert packet["source_status"] == "SUPPORTED"

        # Negative source must stay visibly negative, not become an adaptation claim.
        bad = dict(candidate)
        bad["candidate_id"] = "var-bad"
        bad["status"] = "HARMFUL"
        bad_packet = migration_packet(bad)
        assert bad_packet["packet_purpose"] == "NEGATIVE_EVIDENCE"
        assert bad_packet["source_status"] == "HARMFUL"

        # False-confidence guard: SUPPORTED without evidence must fail.
        failed = False
        try:
            validate_evaluation("SUPPORTED", {"quality": "IMPROVED"}, [])
        except SystemExit:
            failed = True
        assert failed

        # UNKNOWN may remain unknown without invented evidence.
        validate_evaluation("UNKNOWN", {}, [])
        print_json({"selftest": "PASS", "schema_version": STATE_VERSION})
    finally:
        shutil.rmtree(root, ignore_errors=True)


def parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ena_evolve.py",
        description="ENA v0.3.5 candidate evolution-metabolism state/evidence reference tool",
    )
    parser.add_argument("--state", default=str(DEFAULT_STATE), help="Evolution state JSON path")
    sub = parser.add_subparsers(dest="command", required=True)

    cmd = sub.add_parser("init")
    cmd.add_argument("--force", action="store_true")
    cmd.set_defaults(func=cmd_init)

    cmd = sub.add_parser("observe")
    cmd.add_argument("--kind", required=True)
    cmd.add_argument("--summary", required=True)
    cmd.add_argument("--source", default="agent")
    cmd.add_argument("--context", action="append", default=[])
    cmd.set_defaults(func=cmd_observe)

    cmd = sub.add_parser("review")
    cmd.add_argument("--trigger", default="MANUAL")
    cmd.add_argument("--limit", type=int, default=20)
    cmd.add_argument("--all", action="store_true")
    cmd.add_argument("--finding", default="")
    cmd.add_argument("--mutation-required", action="store_true")
    cmd.set_defaults(func=cmd_review)

    cmd = sub.add_parser("propose")
    cmd.add_argument("--signal", action="append", default=[])
    cmd.add_argument("--hypothesis", required=True)
    cmd.add_argument("--change", required=True)
    cmd.add_argument("--expected", action="append", default=[])
    cmd.add_argument("--variation-space", required=True)
    cmd.add_argument("--evolutionary-subject", default="")
    cmd.add_argument("--protected-subject", action="append", default=[])
    cmd.add_argument("--environment", action="append", default=[])
    cmd.add_argument("--dependency", action="append", default=[])
    cmd.add_argument("--unknown", action="append", default=[])
    cmd.add_argument("--observe", default="")
    cmd.set_defaults(func=cmd_propose)

    cmd = sub.add_parser("experiment")
    cmd.add_argument("candidate")
    cmd.add_argument("--variation-space")
    cmd.add_argument("--actual-change", required=True)
    cmd.add_argument("--effect-boundary", default="")
    cmd.add_argument("--recovery", default="")
    cmd.add_argument("--authority-basis", default="")
    cmd.add_argument("--note", default="")
    cmd.set_defaults(func=cmd_experiment)

    cmd = sub.add_parser("evaluate")
    cmd.add_argument("candidate")
    cmd.add_argument("--outcome", action="append", default=[])
    cmd.add_argument("--selection", required=True)
    cmd.add_argument("--evidence", action="append", default=[])
    cmd.add_argument("--negative-evidence", action="append", default=[])
    cmd.add_argument("--tradeoff", action="append", default=[])
    cmd.add_argument("--unknown", action="append", default=[])
    cmd.add_argument("--note", default="")
    cmd.set_defaults(func=cmd_evaluate)

    cmd = sub.add_parser("integrate")
    cmd.add_argument("candidate")
    cmd.add_argument("--target", required=True)
    cmd.add_argument("--authority-basis", required=True, help="Real mandate/local authority basis; not verified by this tool")
    cmd.add_argument("--recovery-boundary", required=True, help="Real recovery/irreversibility statement; not verified by this tool")
    cmd.add_argument("--scope", default="")
    cmd.add_argument("--result", choices=["COMMITTED", "DEFERRED", "REJECTED", "UNKNOWN"], default="COMMITTED")
    cmd.add_argument("--residual", action="append", default=[])
    cmd.add_argument("--allow-unknown", action="store_true")
    cmd.set_defaults(func=cmd_integrate)

    cmd = sub.add_parser("archive")
    cmd.add_argument("candidate")
    cmd.add_argument("--reason", required=True)
    cmd.add_argument("--retire-record", action="store_true")
    cmd.add_argument("--retention-note", default="")
    cmd.set_defaults(func=cmd_archive)

    cmd = sub.add_parser("export")
    cmd.add_argument("candidate")
    cmd.add_argument("--output", required=True)
    cmd.set_defaults(func=cmd_export)

    cmd = sub.add_parser("import")
    cmd.add_argument("packet")
    cmd.add_argument("--variation-space", required=True)
    cmd.add_argument("--evolutionary-subject", default="")
    cmd.add_argument("--protected-subject", action="append", default=[])
    cmd.add_argument("--environment", action="append", default=[])
    cmd.add_argument("--difference", action="append", default=[])
    cmd.add_argument("--unknown", action="append", default=[])
    cmd.add_argument("--observe", default="")
    cmd.set_defaults(func=cmd_import)

    cmd = sub.add_parser("closure")
    cmd.add_argument("--blocker", action="append", default=[])
    cmd.add_argument("--evidence-needed", action="append", default=[])
    cmd.add_argument("--narrow", action="append", default=[])
    cmd.set_defaults(func=cmd_closure)

    cmd = sub.add_parser("status")
    cmd.set_defaults(func=cmd_status)

    cmd = sub.add_parser("selftest")
    cmd.set_defaults(func=cmd_selftest)
    return parser


def main() -> None:
    args = parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
