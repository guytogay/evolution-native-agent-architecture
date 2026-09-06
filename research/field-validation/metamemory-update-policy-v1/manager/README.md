# Metamemory Update Policy v1 — Manager-only surface

Status: `MANAGER_ONLY / POST-CAPTURE_SCORING / NEVER_EXPOSE_TO_PRIMARY_WORKER`

This directory contains adjudication tooling that intentionally knows the frozen expected states and hidden transfer oracle.

It is **not** part of any treatment and must not be shown, linked, summarized, or made retrievable to a fresh primary worker before that worker's first complete response is frozen.

## Scorer

`score_primary_bundle.py` consumes the outer bundle defined by `../PRIMARY-LAUNCH-BUNDLE.md` and mechanically reports:

- bundle/run metadata mismatches;
- response-shape parsing;
- M1–M7;
- state-to-transfer compatibility;
- the preregistered all-arm replication trigger.

Run its synthetic checks with:

```bash
python research/field-validation/metamemory-update-policy-v1/manager/score_primary_bundle.py --selftest
```

Score a returned bundle with:

```bash
python research/field-validation/metamemory-update-policy-v1/manager/score_primary_bundle.py BUNDLE.txt --pretty
```

## Evidence boundary

The scorer does not turn behavioral nonconformance into protocol invalidity.

```text
WRONG / STRANGE / LOW_ACCURACY / REFUSAL_LIKE OUTPUT = BEHAVIORAL DATA
OBJECTIVE EXECUTION FAILURE = PROTOCOL FAILURE
```

Objective protocol validity still follows the frozen preregistration and relay metadata. The replication trigger is evaluated only after four valid initial outputs are available.

Do not modify frozen treatment files to accommodate scorer behavior. If this scorer is wrong, fix or supersede the scorer; do not rewrite primary occurrence truth.
