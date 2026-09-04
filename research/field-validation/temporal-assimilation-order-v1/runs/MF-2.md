# Temporal Assimilation / Developmental Order — Primary Run MF-2

Status: `IN_PROGRESS / RAW_FIRST_OUTPUTS_PRESERVED`

Preregistration:
`research/field-validation/2026-09-04-temporal-assimilation-developmental-order-preregistration.md`

Frozen fixture:
`research/field-validation/fixtures/temporal-assimilation-order-v1/FIXTURE.md`

Host claim: `ChatGPT Temporary Chat / GPT-5.6 Sol`
Relay role: `Codex transport only`
Arm: `MF — misleading-first`

## A1

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: MF-2 ARM: MF STAGE: A1 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
ACTION: ZED
WORKING_RULE: Cases with Aster and Coda ON route to ZED unless later feedback contradicts this provisional rule.
CONFIDENCE: 50
```

## A2

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: MF-2 ARM: MF STAGE: A2 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
ACTION: NOVA
WORKING_RULE: Aster and Coda both ON may indicate ZED; otherwise provisionally predict NOVA until feedback refines the rule.
CONFIDENCE: 55
```

## A3

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: MF-2 ARM: MF STAGE: A3 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
ACTION: ZED
WORKING_RULE: Aster ON currently predicts ZED, while Aster OFF predicts NOVA; Beryl and Coda remain unresolved.
CONFIDENCE: 65
```

## A4

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: MF-2 ARM: MF STAGE: A4 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
ACTION: ZED
WORKING_RULE: Coda ON currently predicts ZED, while Beryl ON with Coda OFF predicts NOVA; Dune remains untested.
CONFIDENCE: 75
```

## A5

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: MF-2 ARM: MF STAGE: A5 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
ACTION: ZED
WORKING_RULE: Coda ON predicts ZED despite Aster; Beryl ON with Coda OFF predicts NOVA, while Dune remains untested.
CONFIDENCE: 80
```

## A6

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: MF-2 ARM: MF STAGE: A6 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
ACTION: NOVA
WORKING_RULE: ZED occurs when Coda and Dune differ; matching Coda and Dune values route to NOVA.
CONFIDENCE: 90
```

## A7

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: MF-2 ARM: MF STAGE: A7 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
FINAL_RULE: Route to ZED exactly when Beryl is OFF and Dune is OFF; otherwise route to NOVA.
CAUSAL_FEATURES: Beryl, Dune
IRRELEVANT_FEATURES: Aster, Coda
CONFIDENCE: 90
```

No scoring or correction was performed before preserving these outputs.
