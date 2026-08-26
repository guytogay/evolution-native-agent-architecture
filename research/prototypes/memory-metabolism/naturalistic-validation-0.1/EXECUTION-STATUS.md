# Naturalistic Validation 0.1 — Execution Status

Status: `RESEARCH_EVALUATION_PROTOCOL / NOT_CURRENT_BASELINE`

## Current machine-check status

The protocol currently contains:

- `field-observation.schema.json`
- `validate_field_observation.py`
- `observation-template.json`
- `selftest.py`

`selftest.py` currently defines 19 deterministic observation-discipline cases, including Host evidence-class eligibility.

At the time this status note was updated, those 19 cases had **not been executed in the current authoring Host** because the available execution container could not resolve `github.com` to clone/fetch the just-written branch state.

Therefore the truthful status is:

`SELFTEST_DEFINED_19 / NOT_EXECUTED_IN_CURRENT_HOST`

Do not restate this as `SELFTEST_PASS 19` until an actual execution result exists.

This is an execution-environment limitation, not evidence for or against the protocol semantics.

## What is already evidenced

GitHub writes succeeded and the research files exist on branch `research/memory-metabolism-prototype`.

That establishes persistence of the artifacts, not executable correctness.

## Next execution opportunity

Run the deterministic selftest in any Host that can access the branch and has Python + `jsonschema` available.

Record the exact commit SHA and raw output when executed.

Do not create extra infrastructure merely to turn this small protocol selftest green; use the next convenient execution-capable Host.
