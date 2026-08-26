#!/usr/bin/env python3
"""Score Tiny Hot Kernel / Semantic Router Host results.

Input results are Host/model observations. This scorer checks them against the
current research fixture expectations. The fixture oracle is author-derived and
independent review is pending; scores are exploratory until oracle reconciliation.
This tool does not prove naturalistic salience or safety.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

VALID_RETRIEVAL = {"NOT_ATTEMPTED", "SUCCESS", "PARTIAL", "FAILED"}
VALID_KERNELS = {"K-A", "K-B", "K-C"}
ORACLE_STATUS = "AUTHOR_EXPECTATION / INDEPENDENT_REVIEW_PENDING / NOT_GROUND_TRUTH"
SELECTION_ELIGIBILITY = "EXPLORATORY_ONLY_UNTIL_ORACLE_RECONCILIATION"


def load_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        raw = raw.strip()
        if not raw:
            continue
        try:
            value = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"{path}:{lineno}: invalid JSON: {exc}") from exc
        if not isinstance(value, dict):
            raise SystemExit(f"{path}:{lineno}: each row must be a JSON object")
        rows.append(value)
    return rows


def pct(num: int, den: int) -> str:
    return "n/a" if den == 0 else f"{100.0 * num / den:.1f}%"


def main() -> int:
    parser = argparse.ArgumentParser()
    default_fixtures = Path(__file__).resolve().parents[1] / "fixtures" / "tiny-kernel-cases.jsonl"
    parser.add_argument("--fixtures", type=Path, default=default_fixtures)
    parser.add_argument("--results", type=Path, required=True)
    parser.add_argument("--expected-kernel", choices=sorted(VALID_KERNELS), required=True)
    parser.add_argument("--strict", action="store_true", help="return nonzero on trigger FN/FP, available-resolver route miss/overreach, or broken-resolver false success/fallback failure")
    args = parser.parse_args()

    fixtures = load_jsonl(args.fixtures)
    results = load_jsonl(args.results)

    fixture_by_id = {row.get("case_id"): row for row in fixtures}
    if None in fixture_by_id or len(fixture_by_id) != len(fixtures):
        raise SystemExit("fixture case_id values must be unique and non-null")

    result_by_id: dict[str, dict] = {}
    duplicate_results: list[str] = []
    kernel_mismatch: list[str] = []
    for row in results:
        case_id = row.get("case_id")
        if not isinstance(case_id, str):
            raise SystemExit("every result requires string case_id")
        if case_id in result_by_id:
            duplicate_results.append(case_id)
        kernel = row.get("kernel")
        if kernel != args.expected_kernel:
            kernel_mismatch.append(f"{case_id}:{kernel!r}")
        result_by_id[case_id] = row

    unknown_results = sorted(set(result_by_id) - set(fixture_by_id))
    missing_results = sorted(set(fixture_by_id) - set(result_by_id))

    tp = tn = fp = fn = 0
    route_zero_hit: list[str] = []
    route_incomplete: list[str] = []
    route_overreach: list[str] = []
    quiet_family_leak: list[str] = []
    broken_resolver_false_success: list[str] = []
    broken_resolver_no_fallback: list[str] = []
    malformed: list[str] = []

    for case_id, fixture in fixture_by_id.items():
        result = result_by_id.get(case_id)
        if result is None:
            continue

        expected_trigger = fixture.get("expected_trigger")
        trigger = result.get("trigger")
        if not isinstance(expected_trigger, bool) or not isinstance(trigger, bool):
            malformed.append(f"{case_id}: trigger/expected_trigger must be boolean")
            continue

        families = result.get("families", [])
        if not isinstance(families, list) or not all(isinstance(v, str) for v in families):
            malformed.append(f"{case_id}: families must be array[string]")
            families = []
        predicted = set(families)

        retrieval_status = result.get("retrieval_status", "NOT_ATTEMPTED")
        if retrieval_status not in VALID_RETRIEVAL:
            malformed.append(f"{case_id}: invalid retrieval_status {retrieval_status!r}")
        fallback_used = result.get("fallback_used", False)
        if not isinstance(fallback_used, bool):
            malformed.append(f"{case_id}: fallback_used must be boolean")
            fallback_used = False

        if expected_trigger and trigger:
            tp += 1
        elif expected_trigger and not trigger:
            fn += 1
        elif not expected_trigger and trigger:
            fp += 1
        else:
            tn += 1

        primary = set(fixture.get("primary_families", []))
        allowed = set(fixture.get("allowed_families", []))
        resolver_broken = fixture.get("resolver_state") == "BROKEN"

        # Family routing is evaluated only when the fixture says the cold resolver
        # is available. A broken resolver should test fallback honesty, not force the
        # Host to reconstruct the unavailable route from resident memory.
        if expected_trigger and trigger and not resolver_broken:
            if primary and not (predicted & primary):
                route_zero_hit.append(case_id)
            elif primary and not primary.issubset(predicted):
                route_incomplete.append(case_id)
            extras = predicted - allowed
            if extras:
                route_overreach.append(f"{case_id}:{','.join(sorted(extras))}")

        if not expected_trigger and predicted:
            quiet_family_leak.append(f"{case_id}:{','.join(sorted(predicted))}")

        if resolver_broken and expected_trigger and trigger:
            if retrieval_status == "SUCCESS":
                broken_resolver_false_success.append(case_id)
            if not fallback_used:
                broken_resolver_no_fallback.append(case_id)

    evaluated = tp + tn + fp + fn
    print(f"kernel={args.expected_kernel} fixtures={len(fixtures)} results={len(results)} evaluated={evaluated}")
    print(f"oracle_status={ORACLE_STATUS}")
    print(f"selection_eligibility={SELECTION_ELIGIBILITY}")
    print(f"trigger: TP={tp} TN={tn} FP={fp} FN={fn}")
    print(f"trigger_precision={pct(tp, tp + fp)} trigger_recall={pct(tp, tp + fn)}")
    print(f"route_zero_hit={len(route_zero_hit)} route_incomplete={len(route_incomplete)} route_overreach={len(route_overreach)}")
    print(f"quiet_family_leak={len(quiet_family_leak)}")
    print(f"broken_resolver_false_success={len(broken_resolver_false_success)} broken_resolver_no_fallback={len(broken_resolver_no_fallback)}")
    print(f"missing_results={len(missing_results)} unknown_results={len(unknown_results)} duplicate_results={len(duplicate_results)} kernel_mismatch={len(kernel_mismatch)} malformed={len(malformed)}")

    details = {
        "FN": [cid for cid, f in fixture_by_id.items() if cid in result_by_id and f.get("expected_trigger") is True and result_by_id[cid].get("trigger") is False],
        "FP": [cid for cid, f in fixture_by_id.items() if cid in result_by_id and f.get("expected_trigger") is False and result_by_id[cid].get("trigger") is True],
        "route_zero_hit": route_zero_hit,
        "route_incomplete": route_incomplete,
        "route_overreach": route_overreach,
        "quiet_family_leak": quiet_family_leak,
        "broken_resolver_false_success": broken_resolver_false_success,
        "broken_resolver_no_fallback": broken_resolver_no_fallback,
        "missing_results": missing_results,
        "unknown_results": unknown_results,
        "duplicate_results": duplicate_results,
        "kernel_mismatch": kernel_mismatch,
        "malformed": malformed,
    }
    for label, values in details.items():
        if values:
            print(f"{label}: {values}")

    print("verification_scope=FIXTURE_COMPARISON_AND_KERNEL_IDENTITY_BINDING_ONLY")

    structural_failure = bool(
        missing_results
        or unknown_results
        or duplicate_results
        or kernel_mismatch
        or malformed
    )
    performance_failure = bool(
        fn
        or fp
        or route_zero_hit
        or route_overreach
        or quiet_family_leak
        or broken_resolver_false_success
        or broken_resolver_no_fallback
    )

    if structural_failure:
        return 2
    if args.strict and performance_failure:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
