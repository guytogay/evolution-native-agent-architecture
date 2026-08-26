#!/usr/bin/env python3
"""Small executable reference for Git/Merkle-DAG style history relations.

Research-only. Models ancestry and merge-parent preservation; it does not perform
semantic file merging or authenticate commits.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Node:
    node_id: str
    parents: tuple[str, ...] = ()


class Dag:
    def __init__(self, nodes: list[Node]):
        self.nodes = {n.node_id: n for n in nodes}
        if len(self.nodes) != len(nodes):
            raise ValueError("duplicate node id")
        for node in nodes:
            for parent in node.parents:
                if parent not in self.nodes:
                    raise ValueError(f"unknown parent {parent!r} for {node.node_id}")

    def ancestors_including_self(self, node_id: str) -> set[str]:
        if node_id not in self.nodes:
            raise KeyError(node_id)
        seen: set[str] = set()
        stack = [node_id]
        while stack:
            current = stack.pop()
            if current in seen:
                continue
            seen.add(current)
            stack.extend(self.nodes[current].parents)
        return seen

    def relation(self, local: str, incoming: str) -> str:
        if local == incoming:
            return "EQUIVALENT"
        local_anc = self.ancestors_including_self(local)
        incoming_anc = self.ancestors_including_self(incoming)
        if local in incoming_anc:
            return "INCOMING_DESCENDS_FROM_LOCAL"
        if incoming in local_anc:
            return "INCOMING_IS_STALE_ANCESTOR"
        if local_anc & incoming_anc:
            return "DIVERGED_WITH_COMMON_ANCESTOR"
        return "UNKNOWN_RELATION"

    def merge_node(self, node_id: str, left: str, right: str) -> Node:
        if left not in self.nodes or right not in self.nodes:
            raise KeyError("merge parent missing")
        if left == right:
            raise ValueError("merge requires distinct parent histories")
        return Node(node_id=node_id, parents=(left, right))
