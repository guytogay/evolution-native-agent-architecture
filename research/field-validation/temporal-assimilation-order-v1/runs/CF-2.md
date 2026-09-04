# Temporal Assimilation / Developmental Order — Primary Run CF-2

Status: `IN_PROGRESS / RAW_FIRST_OUTPUTS_PRESERVED`

Preregistration:
`research/field-validation/2026-09-04-temporal-assimilation-developmental-order-preregistration.md`

Frozen fixture:
`research/field-validation/fixtures/temporal-assimilation-order-v1/FIXTURE.md`

Host claim: `ChatGPT Temporary Chat / GPT-5.6 Sol`
Relay role: `Codex transport only`
Arm: `CF — corrective/boundary-first`

## A1

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: CF-2 ARM: CF STAGE: A1 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
ACTION: ZED
WORKING_RULE: Initially predict ZED when Aster and Beryl are ON while Coda and Dune are OFF.
CONFIDENCE: 25
```

## A2

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: CF-2 ARM: CF STAGE: A2 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
ACTION: NOVA
WORKING_RULE: With only one labeled example, use the simplest provisional rule: predict NOVA unless feedback shows a feature-dependent split.
CONFIDENCE: 30
```

## A3

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: CF-2 ARM: CF STAGE: A3 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
ACTION: NOVA
WORKING_RULE: Provisional rule: Aster ON predicts NOVA, while Aster OFF predicts ZED; current feedback is consistent with this split.
CONFIDENCE: 55
```

## A4

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: CF-2 ARM: CF STAGE: A4 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
ACTION: NOVA
WORKING_RULE: Current evidence suggests NOVA when Beryl is ON and Coda is OFF; otherwise predict ZED.
CONFIDENCE: 75
```

## A5

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: CF-2 ARM: CF STAGE: A5 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
ACTION: ZED
WORKING_RULE: Predict NOVA when Beryl is ON and Coda is OFF; otherwise predict ZED, with Dune not yet evidenced.
CONFIDENCE: 82
```

## A6

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: CF-2 ARM: CF STAGE: A6 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
ACTION: ZED
WORKING_RULE: Predict NOVA exactly when Beryl and Dune differ; predict ZED when they match.
CONFIDENCE: 95
```

## A7

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: CF-2 ARM: CF STAGE: A7 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
FINAL_RULE: Route to ZED only when Coda is ON and Dune is OFF; otherwise route to NOVA.
CAUSAL_FEATURES: Coda, Dune
IRRELEVANT_FEATURES: Aster, Beryl
CONFIDENCE: 100
```

No scoring or correction was performed before preserving these outputs.
