# Sleep input provenance follow-up — 2026-09-12

## Source

Two independent DSH adopters re-ran the corrected `guytogay/ENA` reference toolchain after product PR #20 and reported all reference tests passing. One execution review then identified a remaining provenance asymmetry: Dream artifacts carried replay metadata, while `tools/sleep_prepare.py` did not identify the exact source state and bounded slice used to prepare a Sleep run.

## Finding

Before correction, the Sleep bundle contained only:

- `task`;
- `instructions`;
- bounded `experience` records;
- bounded `memory` records.

It did not persist source references, source digests, original/selected record counts, or the selection window. A later Agent could inspect the embedded records but could not directly prove which source-file state the bundle came from if the source had changed.

## Product correction

ENA PR #21 merged as:

`bac14d3bc84093a48b914d13b4955c15720fc960`

`tools/sleep_prepare.py` now records:

- UTC preparation time;
- each source role;
- source reference;
- SHA-256 digest of the source text;
- total source record count;
- selected record count;
- explicit bounded tail-selection policy and max-record parameter.

`tools/self_test.py` verifies the recorded digests and selected counts against the included source files. Linux and Windows reference-tool CI both passed before merge.

## Evidence boundary

This closes a provenance/auditability defect. It does **not** prove that Sleep improves later retrieval, memory quality, or Agent behavior. ENA Issue #12 remains the evidence stream for useful, harmful, null and noisy Sleep/Dream outcomes.

The independent DSH executions remain partial field-execution evidence rather than closure of Issue #14. Real external recovery, one non-trivial live SAFE-CHANGE, and genuine new-session/restart continuation are still required.

## Product-management implication

Continue to prefer execution findings over additional prose review. Fix concrete inconsistencies in already-promised mechanisms, but do not add new Sleep/Dream mechanisms without outcome evidence.