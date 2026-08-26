#!/usr/bin/env python3
"""Compile a bounded Local Projection from explicitly selected canonical sections.

This is a concrete HOW-D recipe. Selection remains Host-local and is not
normative ENA. The output carries source/compiler/Host identity and declared
selection; canonical Current remains the source of truth.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def extract_section(text: str, heading: str) -> str:
    lines = text.splitlines()
    try:
        start = next(i for i, line in enumerate(lines) if line.strip() == heading.strip())
    except StopIteration as exc:
        raise ValueError(f"heading not found: {heading}") from exc

    level = len(heading) - len(heading.lstrip("#"))
    end = len(lines)
    for i in range(start + 1, len(lines)):
        line = lines[i]
        stripped = line.lstrip()
        if not stripped.startswith("#"):
            continue
        next_level = len(stripped) - len(stripped.lstrip("#"))
        if next_level <= level:
            end = i
            break
    return "\n".join(lines[start:end]).rstrip() + "\n"


def digest_json(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--canonical-root", type=Path, required=True)
    parser.add_argument("--selection", type=Path, required=True, help="JSON array of {path, section}")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--current-tree", required=True)
    parser.add_argument("--compiler-revision", required=True)
    parser.add_argument("--host-profile-digest", required=True)
    args = parser.parse_args()

    selection = json.loads(args.selection.read_text(encoding="utf-8"))
    if not isinstance(selection, list) or not selection:
        raise SystemExit("selection must be a non-empty JSON array")

    chunks: list[str] = []
    normalized: list[dict[str, str]] = []
    for item in selection:
        if not isinstance(item, dict):
            raise SystemExit("each selection item must be an object")
        rel = item.get("path")
        heading = item.get("section")
        if not isinstance(rel, str) or not rel or not isinstance(heading, str) or not heading:
            raise SystemExit("selection item requires non-empty path and section")
        source = args.canonical_root / rel
        if not source.is_file():
            raise SystemExit(f"canonical file not found: {source}")
        try:
            section = extract_section(source.read_text(encoding="utf-8"), heading)
        except ValueError as exc:
            raise SystemExit(f"{rel}: {exc}") from exc
        chunks.append(f"<!-- source: {rel} :: {heading} -->\n{section}")
        normalized.append({"path": rel, "section": heading})

    projection_body = "\n".join(chunks).rstrip() + "\n"
    projection_revision = "sha256:" + hashlib.sha256(projection_body.encode("utf-8")).hexdigest()

    header = (
        "# Compiled ENA Local Projection — research-only\n\n"
        f"Source Current tree: `{args.current_tree}`\n\n"
        f"Compiler revision: `{args.compiler_revision}`\n\n"
        f"Host profile digest: `{args.host_profile_digest}`\n\n"
        f"Projection revision: `{projection_revision}`\n\n"
        "> This is a bounded Host-local projection, not canonical ENA and not a completeness claim.\n\n"
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(header + projection_body, encoding="utf-8")

    manifest = {
        "implementation_how": "HOW-D-HYBRID-COMPILED-PROJECTION",
        "source_current_tree": args.current_tree,
        "compiler_revision": args.compiler_revision,
        "host_profile_digest": args.host_profile_digest,
        "projection_revision": projection_revision,
        "selection": normalized,
        "selection_digest": digest_json(normalized),
        "limitations": [
            "selection is Host-local and not a completeness claim",
            "omitted Current semantics remain canonical even when not resident",
            "source/compiler/Host changes can invalidate this projection",
        ],
    }
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(f"projection={args.output}")
    print(f"manifest={args.manifest}")
    print(f"projection_revision={projection_revision}")
    print("how=HOW-D-HYBRID-COMPILED-PROJECTION")
    print("canonical_status=LOCAL_PROJECTION_NOT_CURRENT")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
