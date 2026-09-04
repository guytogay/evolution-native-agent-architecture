# Metamemory Update Policy v1 Fixture

Status: `FROZEN_WITH_PREREGISTRATION / PRIMARY_NOT_STARTED`

Purpose: provide exact one-shot treatment payloads for four source-trust update-policy arms while holding the object-level experience ledger and transfer battery constant.

Primary preregistration:

`research/field-validation/2026-09-04-metamemory-update-policy-preregistration.md`

## Treatment files

- `PROMPT-S0-STATIC-EQUAL.md`
- `PROMPT-G1-GLOBAL-RECENT3.md`
- `PROMPT-C1-CONTEXT-RECENT3.md`
- `PROMPT-C2-CONTEXT-REVERSIBLE3.md`

Each file is a complete single-turn payload. Deliver it verbatim to one fresh ChatGPT Temporary Chat. Do not prepend project context, ENA theory, the preregistration, expected scores, hidden oracle or another arm.

## Shared invariants

All four prompts contain the exact same:

- task wording except the treatment-policy block;
- H1-H16 history;
- history order;
- source recommendations and outcomes;
- T1-T10 transfer battery;
- output schema.

Only the update-policy block changes.

## Primary run plan

Initial:

```text
S0-1
G1-1
C1-1
C2-1
```

Frozen replication trigger is defined in the preregistration. If triggered, add exactly:

```text
S0-2
G1-2
C1-2
C2-2
```

Do not selectively replicate only an arm with an unwanted result.

## Relay target

This fixture intentionally reduces human transport cost:

```text
one fresh chat
+ one complete prompt delivery
+ one first-output capture
= one run
```

No developmental stage-by-stage relay is required.
