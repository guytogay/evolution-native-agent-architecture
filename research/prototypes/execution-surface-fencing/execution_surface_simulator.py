#!/usr/bin/env python3
"""Research-only execution-surface simulator for stale-executor HOW comparison.

This simulator does not claim to model any provider exactly. It isolates materially
different enforcement locations so ENA does not collapse idempotency, fencing,
optimistic concurrency, status query, gateway serialization, and WAIT into one
"exactly once" story.
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Request:
    request_id: str
    executor_generation: int
    effect_id: str
    material_digest: str
    path: str = "CONTROLLED"
    idempotency_key: str | None = None
    fence_token: int | None = None
    expected_version: int | None = None


@dataclass
class Policy:
    provider_idempotency: bool = False
    target_fencing: bool = False
    optimistic_concurrency: bool = False
    gateway_current_generation: int | None = None
    bypass_allowed: bool = True


@dataclass
class Target:
    policy: Policy
    highest_fence: int = 0
    resource_version: int = 1
    occurrences: list[tuple[str, str, int]] = field(default_factory=list)
    idempotency_seen: dict[str, tuple[str, str]] = field(default_factory=dict)

    def observe_effect(self, effect_id: str, material_digest: str, executor_generation: int) -> None:
        self.occurrences.append((effect_id, material_digest, executor_generation))

    def status(self, effect_id: str, material_digest: str) -> str:
        for eid, digest, _ in self.occurrences:
            if eid == effect_id and digest == material_digest:
                return "COMMITTED"
        return "NOT_COMMITTED"

    def submit(self, req: Request) -> str:
        if (
            self.policy.gateway_current_generation is not None
            and req.path == "CONTROLLED"
            and req.executor_generation != self.policy.gateway_current_generation
        ):
            return "REJECT_GATEWAY_GENERATION"

        if (
            req.path == "BYPASS"
            and self.policy.gateway_current_generation is not None
            and not self.policy.bypass_allowed
        ):
            return "REJECT_BYPASS_PATH"

        if self.policy.target_fencing:
            if req.fence_token is None:
                return "REJECT_MISSING_FENCE"
            if req.fence_token < self.highest_fence:
                return "REJECT_STALE_FENCE"
            self.highest_fence = max(self.highest_fence, req.fence_token)

        if self.policy.optimistic_concurrency:
            if req.expected_version is None:
                return "REJECT_MISSING_VERSION"
            if req.expected_version != self.resource_version:
                return "REJECT_VERSION_CONFLICT"

        if self.policy.provider_idempotency:
            if not req.idempotency_key:
                return "REJECT_MISSING_IDEMPOTENCY_KEY"
            seen = self.idempotency_seen.get(req.idempotency_key)
            if seen is not None:
                seen_effect, seen_digest = seen
                if (seen_effect, seen_digest) != (req.effect_id, req.material_digest):
                    return "REJECT_IDEMPOTENCY_MISMATCH"
                return "DUPLICATE_SUPPRESSED"

        self.observe_effect(req.effect_id, req.material_digest, req.executor_generation)
        if self.policy.provider_idempotency and req.idempotency_key:
            self.idempotency_seen[req.idempotency_key] = (req.effect_id, req.material_digest)
        if self.policy.optimistic_concurrency:
            self.resource_version += 1
        return "COMMITTED"


def occurrence_count(target: Target, effect_id: str, material_digest: str) -> int:
    return sum(
        1
        for eid, digest, _ in target.occurrences
        if eid == effect_id and digest == material_digest
    )
