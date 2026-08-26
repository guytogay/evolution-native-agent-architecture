#!/usr/bin/env python3
from __future__ import annotations

import copy
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOL = HERE / "ena_evolve_v2_minimal.py"
spec = importlib.util.spec_from_file_location("ena_evolve_v2_minimal", TOOL)
if spec is None or spec.loader is None:
    raise RuntimeError("Unable to load prototype")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def expect_error(fn, label: str) -> None:
    try:
        fn()
    except ValueError:
        return
    raise AssertionError(f"{label} unexpectedly passed")


def main() -> None:
    cases = 0

    latent = mod.build_latent_record(
        "var-latent",
        "Keep an unresolved possibility without preallocating an experiment surface.",
        "Store the candidate now; decide experiment context later.",
    )
    assert latent["variation_space"] is None
    assert latent["expression_state"] == "LATENT"
    assert latent["selection_state"] == "UNASSESSED"
    assert not mod.validate_record_v2(latent)
    cases += 1

    packet = mod.export_packet_v2(latent)
    assert packet["packet_schema"] == "ena-adaptation-packet.v2"
    assert packet["packet_purpose"] == "UNRESOLVED_VARIATION"
    assert packet["source_variation_space"] is None
    assert not mod.validate_packet_v2(packet)
    cases += 1

    tampered = copy.deepcopy(packet)
    tampered["hypothesis"] = "tampered after digest"
    expect_error(lambda: mod.require_valid_packet_v2(tampered), "digest tamper")
    cases += 1

    invalid_record = copy.deepcopy(latent)
    invalid_record["expression_state"] = "EXPRESSED"
    expect_error(lambda: mod.export_packet_v2(invalid_record), "invalid source record export")
    cases += 1

    harmful = mod.build_latent_record(
        "var-harmful",
        "A tested change may degrade quality.",
        "Apply a synthetic change in a bounded sandbox.",
        variation_space="sandbox",
    )
    harmful["lifecycle_state"] = "EXPERIMENTED"
    harmful["experiments"] = [
        {
            "experiment_id": "exp-harm",
            "time": "2026-08-27T00:00:00Z",
            "provenance": "LOCAL",
            "variation_space": "sandbox",
            "actual_change": "synthetic change",
        }
    ]
    harmful["selection_state"] = "HARMFUL"
    harmful["evaluations"] = [
        {
            "evaluation_id": "eval-harm",
            "time": "2026-08-27T00:01:00Z",
            "provenance": "LOCAL",
            "outcomes": {"quality": "DEGRADED"},
            "selection": "HARMFUL",
            "evidence_refs": ["trace:harm"],
            "negative_evidence": ["neg:quality-loss"],
        }
    ]
    assert not mod.validate_record_v2(harmful), mod.validate_record_v2(harmful)
    harmful_packet = mod.export_packet_v2(harmful)
    assert harmful_packet["packet_purpose"] == "NEGATIVE_EVIDENCE"
    assert harmful_packet["source_negative_lineage_refs"] == ["neg:quality-loss"]
    cases += 1

    imported = mod.import_packet_v2(harmful_packet, "mig-harmful")
    assert imported["origin"] == "MIGRATION_CANDIDATE"
    assert imported["selection_state"] == "UNASSESSED"
    assert imported["expression_state"] == "LATENT"
    assert imported["variation_space"] is None
    assert imported["migration"]["source_selection_state"] == "HARMFUL"
    assert imported["migration"]["source_negative_lineage_refs"] == ["neg:quality-loss"]
    assert not mod.validate_record_v2(imported), mod.validate_record_v2(imported)
    cases += 1

    contradiction = copy.deepcopy(harmful_packet)
    contradiction["source_selection_state"] = "SUPPORTED"
    contradiction["content_sha256"] = mod.canonical_digest(contradiction)
    expect_error(lambda: mod.require_valid_packet_v2(contradiction), "selection/purpose contradiction")
    cases += 1

    extra = copy.deepcopy(packet)
    extra["host_private_extension"] = {"x": 1}
    extra["content_sha256"] = mod.canonical_digest(extra)
    expect_error(lambda: mod.require_valid_packet_v2(extra), "top-level packet extension")
    cases += 1

    expressed = mod.build_latent_record(
        "var-expressed",
        "Represent one non-material expression occurrence.",
        "Temporarily express the candidate.",
    )
    expressed["expression_state"] = "EXPRESSED"
    expressed["expression_history"] = [
        {
            "expression_id": "expr-1",
            "time": "2026-08-27T00:02:00Z",
            "state": "EXPRESSED",
            "trigger": "task cue",
            "effect_materiality": "NON_MATERIAL",
        }
    ]
    assert not mod.validate_record_v2(expressed), mod.validate_record_v2(expressed)
    expressed_packet = mod.export_packet_v2(expressed)
    assert expressed_packet["source_last_expressed_at"] == "2026-08-27T00:02:00Z"
    cases += 1

    bad_history = copy.deepcopy(expressed_packet)
    bad_history["source_expression_state"] = "LATENT"
    bad_history["content_sha256"] = mod.canonical_digest(bad_history)
    expect_error(lambda: mod.require_valid_packet_v2(bad_history), "expression-history mismatch")
    cases += 1

    assert cases == 10
    print({"selftest": "PASS", "cases": cases, "note": "case count is corpus size, not an architectural threshold"})


if __name__ == "__main__":
    main()
