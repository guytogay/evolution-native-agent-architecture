# DSH field-execution findings — 2026-09-12

This is maintainer evidence about `guytogay/ENA`, not adopter-facing product prose.

Two independent DSH adopters executed the clean ENA reference tools rather than only reviewing the Markdown.

## Evidence obtained

One adopter ran the full reference-tool path in an isolated sandbox (`/tmp/ena-trial`) without touching live `~/.ena` state. The run covered:

- `test_control_yaml.py` and `self_test.py`;
- preset initialization and preflight ready/not-ready/stale cases;
- SAFE-CHANGE scaffold creation and state-gate rejection/acceptance behavior;
- validation FAIL -> repair -> PASS records with `repair_of` linking;
- freshness reporting;
- Sleep input preparation;
- multi-source Dream material combination;
- free and problem-guided Dream sampling;
- speculative candidate recording.

Observed gate behavior included rejection of unresolved recovery fields, illegal SAFE-CHANGE transitions, and `retained` without evidence.

A second adopter executed the suite on Windows. Initial `self_test.py` failed because the Python installation had no IANA zone database for `Etc/UTC`. Installing `tzdata` made the suite pass. This exposed a real portability dependency in the reference implementation rather than a conceptual ENA failure.

## Defects found

### Dream provenance

`dream_sample.py` used `--seed` to drive deterministic sampling but did not persist the effective seed in the output artifact. Exact replay therefore depended on external CLI history.

The same run also found a semantic ambiguity: free mode exposed its internally sampled starting fragment through `anchor_id`, the same field used for the explicit problem-guided anchor.

### Windows timezone portability

`ena_init.py` and other reference tools called `ZoneInfo(...)` directly. On Windows Python installations without system IANA data or the optional `tzdata` package, even the reference self-test could fail before exercising ENA behavior.

## Product correction

Merged ENA PR #20 at `3c92d25889f7571eebcdb60196c47c6ed9b7aaa6`:

- every Dream artifact records the effective seed;
- omitted seeds are generated and persisted so sampling can be replayed;
- Dream input reference, SHA-256 digest, and record count are recorded;
- free mode uses `sampled_anchor_id`, while `anchor_id` is reserved for the explicit problem-guided anchor;
- UTC works without an external timezone database;
- unavailable non-UTC IANA zones fail with actionable guidance to install `tzdata` or use a confirmed available zone;
- timezone handling is shared by initialization, change scaffolding, validation events, and SAFE-CHANGE timestamps;
- reference-tool CI now runs on both Ubuntu and Windows;
- self-tests verify Dream replay/provenance and anchor semantics;
- SAFE-CHANGE `failed` is reachable only from `restoring`, matching the documented meaning of failed recovery.

Both OS jobs passed before merge.

## Evidence classification

These runs are stronger than documentation review or CI-only evidence because independent adopters actually executed the tools and produced concrete failures. They are still **not** enough to close ENA Issue #14 because they did not complete the full real-Host chain with:

- a real external recovery path;
- one non-trivial live SAFE-CHANGE against production-like state;
- a genuinely new session/restart reading durable ENA state and continuing work.

The findings were recorded in ENA Issue #14 and the Dream-specific provenance result was also recorded in Issue #12.

## Product-management consequence

The most useful next evidence is now installation/use on a real Host, not another prose-only review. Preserve execution failures, friction, null results, and cross-session continuation evidence before expanding mechanisms further.
