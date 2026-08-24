#!/usr/bin/env python3
"""Consistency validator for ENA v0.3.6 candidate.1 evolution-record v2.

Checks represented internal consistency only. It does not prove external truth,
actual expression, evidence validity, authority, recovery, or universal fitness.
"""
from __future__ import annotations

import argparse
import copy
import json
from datetime import datetime
from pathlib import Path

from jsonschema import FormatChecker
from jsonschema.validators import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas/evolution-record.v2.schema.json"
TEMPLATE_PATH = ROOT / "templates/evolution-record.v2.json"
POSITIVE = {"SUPPORTED", "PARTIAL"}
NEGATIVE = {"NOT_SUPPORTED", "HARMFUL"}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def parse_time(value: object, label: str, errors: list[str]) -> datetime | None:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"consistency: {label} requires non-empty RFC3339 date-time")
        return None
    text = value.strip()
    try:
        parsed = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        errors.append(f"consistency: {label} has invalid date-time {text!r}")
        return None
    if parsed.tzinfo is None:
        errors.append(f"consistency: {label} must include timezone")
        return None
    return parsed


def latest_by_time(items: list[dict], label: str, errors: list[str]) -> dict | None:
    if not items:
        return None
    parsed: list[tuple[datetime, dict]] = []
    for index, item in enumerate(items):
        stamp = parse_time(item.get("time"), f"{label}[{index}].time", errors)
        if stamp is not None:
            parsed.append((stamp, item))
    if len(parsed) != len(items):
        return None
    max_time = max(stamp for stamp, _ in parsed)
    latest = [item for stamp, item in parsed if stamp == max_time]
    if len(latest) != 1:
        errors.append(f"consistency: {label} has tied latest timestamps")
        return None
    return latest[0]


def validate_record(record: dict) -> list[str]:
    schema = load_json(SCHEMA_PATH)
    errors = [
        f"schema: {e.message}"
        for e in Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(record)
    ]

    history = record.get("expression_history") or []
    current_expr = record.get("expression_state")
    lifecycle = record.get("lifecycle_state")
    selection = record.get("selection_state")
    obligation_refs = record.get("triggered_obligation_refs") or []

    if current_expr == "EXPRESSED" and not history:
        errors.append("consistency: EXPRESSED requires represented expression history")
    latest_expr = latest_by_time(history, "expression_history", errors) if history else None
    if latest_expr:
        if latest_expr.get("state") != current_expr:
            errors.append("consistency: latest expression history state must match expression_state")
        if latest_expr.get("state") == "EXPRESSED" and not str(latest_expr.get("trigger", "")).strip():
            errors.append("consistency: EXPRESSED transition requires non-empty represented trigger")

    if current_expr == "EXPRESSED":
        if selection in NEGATIVE or lifecycle in {"ARCHIVED", "RETIRED"}:
            if not obligation_refs:
                errors.append(
                    "consistency: harmful/not-supported or archived/retired EXPRESSED state requires triggered_obligation_refs"
                )
        if latest_expr and latest_expr.get("effect_materiality") == "MATERIAL":
            if record.get("variation_space") is None and not obligation_refs:
                errors.append(
                    "consistency: materially consequential EXPRESSED state requires Variation Space or triggered obligation"
                )

    experiments = record.get("experiments") or []
    evaluations = record.get("evaluations") or []

    if lifecycle == "PROPOSED" and experiments:
        errors.append("consistency: PROPOSED cannot contain represented experiments")
    if lifecycle == "EXPERIMENTED" and not experiments:
        errors.append("consistency: EXPERIMENTED requires represented experiment")

    latest_eval = latest_by_time(evaluations, "evaluations", errors) if evaluations else None
    if selection != "UNASSESSED":
        if not experiments:
            errors.append("consistency: non-UNASSESSED selection requires represented experiment")
        if not evaluations:
            errors.append("consistency: non-UNASSESSED selection requires represented evaluation")
        elif latest_eval:
            if latest_eval.get("selection") != selection:
                errors.append("consistency: latest evaluation selection must match selection_state")
            outcomes = latest_eval.get("outcomes") or {}
            evidence = latest_eval.get("evidence_refs") or []
            tradeoffs = latest_eval.get("tradeoffs") or []
            values = set(outcomes.values())
            if selection in POSITIVE:
                if "IMPROVED" not in values:
                    errors.append("consistency: positive selection requires IMPROVED outcome")
                if not evidence:
                    errors.append("consistency: positive selection requires evidence reference")
                if selection == "SUPPORTED" and "DEGRADED" in values and not tradeoffs:
                    errors.append(
                        "consistency: SUPPORTED with represented DEGRADED outcome requires explicit tradeoffs or PARTIAL"
                    )
            elif selection == "HARMFUL":
                if "DEGRADED" not in values:
                    errors.append("consistency: HARMFUL requires DEGRADED outcome")
                if not evidence:
                    errors.append("consistency: HARMFUL requires evidence reference")
            elif selection == "NOT_SUPPORTED":
                if not outcomes:
                    errors.append("consistency: NOT_SUPPORTED requires represented outcomes")
                if not evidence:
                    errors.append("consistency: NOT_SUPPORTED requires evidence reference")

    if record.get("origin") == "MIGRATION_CANDIDATE":
        migration = record.get("migration")
        if not isinstance(migration, dict):
            errors.append("consistency: MIGRATION_CANDIDATE requires represented migration provenance")
        if selection != "UNASSESSED":
            for index, item in enumerate(experiments):
                if item.get("provenance") != "LOCAL":
                    errors.append(
                        f"consistency: migrated candidate local experiment[{index}] must declare provenance LOCAL"
                    )
            for index, item in enumerate(evaluations):
                if item.get("provenance") != "LOCAL":
                    errors.append(
                        f"consistency: migrated candidate local evaluation[{index}] must declare provenance LOCAL"
                    )

    if lifecycle == "INTEGRATED":
        if not experiments or not evaluations:
            errors.append("consistency: INTEGRATED requires represented experiment and evaluation")
        integrations = record.get("integration_history") or []
        if not integrations:
            errors.append("consistency: INTEGRATED requires integration history")
        else:
            latest_integration = latest_by_time(integrations, "integration_history", errors)
            if latest_integration and latest_integration.get("result") != "COMMITTED":
                errors.append("consistency: INTEGRATED requires latest integration result COMMITTED")

    if lifecycle in {"ARCHIVED", "RETIRED"} and not isinstance(record.get("archive"), dict):
        errors.append("consistency: ARCHIVED/RETIRED requires represented archive metadata")

    return errors


def exp_record(base: dict) -> dict:
    item = copy.deepcopy(base)
    item["lifecycle_state"] = "EXPERIMENTED"
    item["variation_space"] = "sandbox"
    item["experiments"] = [{
        "experiment_id": "exp-1",
        "time": "2026-08-24T00:00:00Z",
        "actual_change": "test change",
        "variation_space": "sandbox",
        "provenance": "LOCAL",
    }]
    return item


def selftest() -> None:
    base = load_json(TEMPLATE_PATH)

    # 1: legitimate dormant possibility has no current experiment surface or verdict.
    assert not validate_record(base), validate_record(base)

    # 2: false expression claim with no trace must fail.
    bad = copy.deepcopy(base)
    bad["expression_state"] = "EXPRESSED"
    assert validate_record(bad), "EXPRESSED without history unexpectedly passed"

    # 3: chronological expression contradiction must fail even when array order is misleading.
    bad = copy.deepcopy(base)
    bad["expression_state"] = "EXPRESSED"
    bad["expression_history"] = [
        {
            "expression_id": "expr-new",
            "time": "2026-08-24T02:00:00Z",
            "state": "LATENT",
            "trigger": "task ended",
            "effect_materiality": "NON_MATERIAL",
        },
        {
            "expression_id": "expr-old",
            "time": "2026-08-24T01:00:00Z",
            "state": "EXPRESSED",
            "trigger": "task cue",
            "effect_materiality": "NON_MATERIAL",
        },
    ]
    assert validate_record(bad), "chronologically stale trailing expression unexpectedly won"

    # 4: represented expression with trigger may remain UNASSESSED if no selection claim is made.
    good = copy.deepcopy(base)
    good["expression_state"] = "EXPRESSED"
    good["expression_history"] = [{
        "expression_id": "expr-2",
        "time": "2026-08-24T01:00:00Z",
        "state": "EXPRESSED",
        "trigger": "relevant task cue",
        "effect_materiality": "NON_MATERIAL",
    }]
    assert not validate_record(good), validate_record(good)

    # 5: expression can return to dormancy without manufacturing selection.
    good["expression_state"] = "LATENT"
    good["expression_history"].append({
        "expression_id": "expr-3",
        "time": "2026-08-24T02:00:00Z",
        "state": "LATENT",
        "trigger": "task ended",
        "effect_materiality": "NON_MATERIAL",
    })
    assert not validate_record(good), validate_record(good)
    assert good["selection_state"] == "UNASSESSED"

    # 6: UNKNOWN selection without experiment is not a shortcut around reality contact.
    bad = copy.deepcopy(base)
    bad["selection_state"] = "UNKNOWN"
    bad["evaluations"] = [{
        "evaluation_id": "eval-0",
        "time": "2026-08-24T00:00:00Z",
        "outcomes": {},
        "selection": "UNKNOWN",
        "evidence_refs": [],
    }]
    assert validate_record(bad), "UNKNOWN without experiment unexpectedly passed"

    # 7: positive selection without IMPROVED evidence must fail.
    bad = exp_record(base)
    bad["selection_state"] = "SUPPORTED"
    bad["evaluations"] = [{
        "evaluation_id": "eval-1",
        "time": "2026-08-24T01:00:00Z",
        "outcomes": {"quality": "UNCHANGED"},
        "selection": "SUPPORTED",
        "evidence_refs": ["e1"],
        "provenance": "LOCAL",
    }]
    assert validate_record(bad), "SUPPORTED without IMPROVED unexpectedly passed"

    # 8: positive selection without evidence ref must fail.
    bad = exp_record(base)
    bad["selection_state"] = "SUPPORTED"
    bad["evaluations"] = [{
        "evaluation_id": "eval-2",
        "time": "2026-08-24T01:00:00Z",
        "outcomes": {"quality": "IMPROVED"},
        "selection": "SUPPORTED",
        "evidence_refs": [],
        "provenance": "LOCAL",
    }]
    assert validate_record(bad), "SUPPORTED without evidence unexpectedly passed"

    # 9: evidence-backed local positive selection is structurally consistent.
    good2 = exp_record(base)
    good2["selection_state"] = "SUPPORTED"
    good2["evaluations"] = [{
        "evaluation_id": "eval-3",
        "time": "2026-08-24T01:00:00Z",
        "outcomes": {"quality": "IMPROVED"},
        "selection": "SUPPORTED",
        "evidence_refs": ["trace:local"],
        "provenance": "LOCAL",
    }]
    assert not validate_record(good2), validate_record(good2)

    # 10: integrated state cannot self-assert with an empty/arbitrary integration object.
    bad = copy.deepcopy(good2)
    bad["lifecycle_state"] = "INTEGRATED"
    bad["integration_history"] = [{}]
    assert validate_record(bad), "INTEGRATED with empty integration object unexpectedly passed"

    # 11: valid committed integration preserves selection/authority/recovery representation.
    good3 = copy.deepcopy(good2)
    good3["lifecycle_state"] = "INTEGRATED"
    good3["integration_history"] = [{
        "integration_id": "int-1",
        "time": "2026-08-24T02:00:00Z",
        "target": "runtime",
        "authority_basis": "owner-approved",
        "recovery_boundary": "state-only",
        "result": "COMMITTED",
        "selection_state_at_commit": "SUPPORTED",
        "expression_state_at_commit": "LATENT",
    }]
    assert not validate_record(good3), validate_record(good3)

    # 12: chronologically later harmful evidence cannot be hidden before an older trailing positive result.
    bad = exp_record(base)
    bad["selection_state"] = "SUPPORTED"
    bad["evaluations"] = [
        {
            "evaluation_id": "eval-new-harm",
            "time": "2026-08-24T03:00:00Z",
            "outcomes": {"quality": "DEGRADED"},
            "selection": "HARMFUL",
            "evidence_refs": ["trace:harm"],
            "provenance": "LOCAL",
        },
        {
            "evaluation_id": "eval-old-good",
            "time": "2026-08-24T02:00:00Z",
            "outcomes": {"quality": "IMPROVED"},
            "selection": "SUPPORTED",
            "evidence_refs": ["trace:old"],
            "provenance": "LOCAL",
        },
    ]
    assert validate_record(bad), "chronologically stale trailing evaluation unexpectedly won"

    # 13: tied latest evaluation timestamps are ambiguous and must fail.
    bad = exp_record(base)
    bad["selection_state"] = "SUPPORTED"
    bad["evaluations"] = [
        {
            "evaluation_id": "eval-a",
            "time": "2026-08-24T02:00:00Z",
            "outcomes": {"quality": "IMPROVED"},
            "selection": "SUPPORTED",
            "evidence_refs": ["a"],
            "provenance": "LOCAL",
        },
        {
            "evaluation_id": "eval-b",
            "time": "2026-08-24T02:00:00Z",
            "outcomes": {"quality": "DEGRADED"},
            "selection": "HARMFUL",
            "evidence_refs": ["b"],
            "provenance": "LOCAL",
        },
    ]
    assert validate_record(bad), "tied latest evaluations unexpectedly passed"

    # 14: mixed positive/negative outcomes cannot silently claim clean SUPPORTED without tradeoffs.
    bad = exp_record(base)
    bad["selection_state"] = "SUPPORTED"
    bad["evaluations"] = [{
        "evaluation_id": "eval-mixed",
        "time": "2026-08-24T02:00:00Z",
        "outcomes": {"speed": "IMPROVED", "data_loss": "DEGRADED"},
        "selection": "SUPPORTED",
        "evidence_refs": ["trace:mixed"],
        "provenance": "LOCAL",
    }]
    assert validate_record(bad), "mixed outcomes unexpectedly passed as unqualified SUPPORTED"

    # 15: explicit tradeoff can preserve a scoped SUPPORTED claim when the caller represents the tradeoff.
    good4 = copy.deepcopy(bad)
    good4["evaluations"][0]["tradeoffs"] = ["data_loss degraded; support limited to speed objective"]
    assert not validate_record(good4), validate_record(good4)

    # 16: harmful/retired current expression requires a represented triggered obligation.
    bad = copy.deepcopy(good2)
    bad["lifecycle_state"] = "RETIRED"
    bad["selection_state"] = "HARMFUL"
    bad["evaluations"] = [{
        "evaluation_id": "eval-h",
        "time": "2026-08-24T02:00:00Z",
        "outcomes": {"quality": "DEGRADED"},
        "selection": "HARMFUL",
        "evidence_refs": ["trace:h"],
        "provenance": "LOCAL",
    }]
    bad["archive"] = {
        "time": "2026-08-24T02:30:00Z",
        "reason": "harmful",
        "selection_state_preserved": "HARMFUL",
    }
    bad["expression_state"] = "EXPRESSED"
    bad["expression_history"] = [{
        "expression_id": "expr-h",
        "time": "2026-08-24T03:00:00Z",
        "state": "EXPRESSED",
        "trigger": "still routed",
        "effect_materiality": "NON_MATERIAL",
    }]
    assert validate_record(bad), "harmful retired expression without obligation unexpectedly passed"
    bad["triggered_obligation_refs"] = ["obligation:stop-or-authorize"]
    assert not validate_record(bad), validate_record(bad)

    # 17: materially consequential expression needs Variation Space or a triggered obligation.
    bad = copy.deepcopy(base)
    bad["expression_state"] = "EXPRESSED"
    bad["expression_history"] = [{
        "expression_id": "expr-material",
        "time": "2026-08-24T01:00:00Z",
        "state": "EXPRESSED",
        "trigger": "production route",
        "effect_boundary": "external email send",
        "effect_materiality": "MATERIAL",
    }]
    assert validate_record(bad), "material expression without consequence ownership unexpectedly passed"
    bad["triggered_obligation_refs"] = ["obligation:consequence-owner"]
    assert not validate_record(bad), validate_record(bad)

    # 18: archived/retired lifecycle requires archive metadata.
    bad = copy.deepcopy(base)
    bad["lifecycle_state"] = "ARCHIVED"
    assert validate_record(bad), "ARCHIVED without archive metadata unexpectedly passed"

    print("EVOLUTION_RECORD_V2_SELFTEST_PASS 18")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args()
    if args.selftest:
        selftest()
        return
    if not args.path:
        parser.error("path required unless --selftest is used")
    record = load_json(Path(args.path))
    errors = validate_record(record)
    print(json.dumps({"valid": not errors, "errors": errors}, ensure_ascii=False, indent=2))
    raise SystemExit(0 if not errors else 1)


if __name__ == "__main__":
    main()
