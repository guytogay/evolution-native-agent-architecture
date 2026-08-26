#!/usr/bin/env python3
from __future__ import annotations

from execution_surface_simulator import Policy, Request, Target, occurrence_count


def req(
    name: str,
    generation: int,
    *,
    path: str = "CONTROLLED",
    key: str | None = None,
    fence: int | None = None,
    version: int | None = None,
    digest: str = "params:v1",
) -> Request:
    return Request(
        request_id=name,
        executor_generation=generation,
        effect_id="effect:E1",
        material_digest=digest,
        path=path,
        idempotency_key=key,
        fence_token=fence,
        expected_version=version,
    )


def main() -> None:
    n = 0

    t = Target(Policy())
    assert t.submit(req("B", 2)) == "COMMITTED"
    assert t.submit(req("A-stale", 1)) == "COMMITTED"
    assert occurrence_count(t, "effect:E1", "params:v1") == 2
    n += 1

    t = Target(Policy(provider_idempotency=True))
    assert t.submit(req("B", 2, key="effect:E1")) == "COMMITTED"
    assert t.submit(req("A-stale", 1, key="effect:E1")) == "DUPLICATE_SUPPRESSED"
    assert occurrence_count(t, "effect:E1", "params:v1") == 1
    n += 1

    t = Target(Policy(provider_idempotency=True))
    assert t.submit(req("B", 2, key="effect:E1")) == "COMMITTED"
    assert (
        t.submit(req("A-stale-mutated", 1, key="effect:E1", digest="params:v2"))
        == "REJECT_IDEMPOTENCY_MISMATCH"
    )
    n += 1

    t = Target(Policy(target_fencing=True), highest_fence=2)
    assert t.submit(req("A-stale", 1, fence=1)) == "REJECT_STALE_FENCE"
    assert t.submit(req("B", 2, fence=2)) == "COMMITTED"
    assert occurrence_count(t, "effect:E1", "params:v1") == 1
    n += 1

    t = Target(Policy(optimistic_concurrency=True), resource_version=5)
    assert t.submit(req("A-stale", 1, version=5)) == "COMMITTED"
    assert t.submit(req("B", 2, version=5)) == "REJECT_VERSION_CONFLICT"
    assert t.occurrences[0][2] == 1
    n += 1

    t = Target(Policy(gateway_current_generation=2, bypass_allowed=False))
    assert t.submit(req("A-stale", 1)) == "REJECT_GATEWAY_GENERATION"
    assert t.submit(req("B", 2)) == "COMMITTED"
    assert occurrence_count(t, "effect:E1", "params:v1") == 1
    n += 1

    t = Target(Policy(gateway_current_generation=2, bypass_allowed=True))
    assert t.submit(req("B", 2)) == "COMMITTED"
    assert t.submit(req("A-stale-bypass", 1, path="BYPASS")) == "COMMITTED"
    assert occurrence_count(t, "effect:E1", "params:v1") == 2
    n += 1

    t = Target(Policy())
    assert t.submit(req("A-unknown-to-B", 1)) == "COMMITTED"
    assert t.status("effect:E1", "params:v1") == "COMMITTED"
    assert occurrence_count(t, "effect:E1", "params:v1") == 1
    n += 1

    t = Target(Policy())
    assert t.status("effect:E1", "params:v1") == "NOT_COMMITTED"
    assert t.submit(req("B", 2)) == "COMMITTED"
    assert t.submit(req("A-delayed", 1)) == "COMMITTED"
    assert occurrence_count(t, "effect:E1", "params:v1") == 2
    n += 1

    t = Target(Policy())
    assert occurrence_count(t, "effect:E1", "params:v1") == 0
    assert t.submit(req("A-delayed", 1)) == "COMMITTED"
    assert occurrence_count(t, "effect:E1", "params:v1") == 1
    n += 1

    print(f"EXECUTION_SURFACE_FENCING_SELFTEST_PASS {n}")
    print("local_assignment_truth=NOT_PHYSICAL_FENCE")
    print("idempotency=EFFECT_IDENTITY_DUPLICATE_SUPPRESSION")
    print("fencing=STALE_ASSIGNMENT_REJECTION_AT_TARGET")
    print("optimistic_concurrency=SINGLE_VERSIONED_WRITE_NOT_ASSIGNMENT_WINNER")
    print("status_query=SETTLEMENT_AMBIGUITY_CONTROL_NOT_FUTURE_STALE_FENCE")
    print("gateway=ONLY_AS_STRONG_AS_EFFECT_SURFACE_COVERAGE")
    print("wait=SAFE_NON_RETRY_NOT_STALE_EXECUTOR_FENCE")
    print("external_exactly_once=NOT_CLAIMED")


if __name__ == "__main__":
    main()
