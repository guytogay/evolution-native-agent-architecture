#!/usr/bin/env python3
"""Small executable append-only event-stream reference."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Event:
    event_id: str
    kind: str
    payload_digest: str
    refs: tuple[str, ...] = ()


class EventStream:
    def __init__(self) -> None:
        self.events: list[Event] = []
        self.by_id: dict[str, Event] = {}

    @property
    def version(self) -> int:
        return len(self.events)

    def append(self, event: Event, expected_version: int) -> int:
        if expected_version != self.version:
            raise RuntimeError(
                f"concurrency conflict: expected version {expected_version}, actual {self.version}"
            )
        existing = self.by_id.get(event.event_id)
        if existing is not None:
            if existing != event:
                raise ValueError("event_id reused with changed payload")
            return self.version
        self.events.append(event)
        self.by_id[event.event_id] = event
        return self.version

    def rebuild_projection(self) -> list[str]:
        return [event.kind for event in self.events]

    def append_reconciliation(
        self,
        event_id: str,
        refs: tuple[str, ...],
        payload_digest: str,
        expected_version: int,
    ) -> int:
        if len(set(refs)) < 2:
            raise ValueError("reconciliation must reference at least two distinct histories/events")
        for ref in refs:
            if ref not in self.by_id:
                raise ValueError(f"unknown reconciliation input {ref}")
        return self.append(
            Event(event_id, "RECONCILIATION", payload_digest, refs=refs),
            expected_version,
        )
