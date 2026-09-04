# Temporal Assimilation / Developmental Order — Primary Run INT-2

Status: `IN_PROGRESS / RAW_FIRST_OUTPUTS_PRESERVED`

Preregistration:
`research/field-validation/2026-09-04-temporal-assimilation-developmental-order-preregistration.md`

Frozen fixture:
`research/field-validation/fixtures/temporal-assimilation-order-v1/FIXTURE.md`

Host claim: `ChatGPT Temporary Chat / GPT-5.6 Sol`
Relay role: `Codex transport only`
Arm: `INT — interleaved`

## A1

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: INT-2 ARM: INT STAGE: A1 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
ACTION: ZED
WORKING_RULE: Predict ZED when Aster and Coda are ON while Beryl and Dune are OFF.
CONFIDENCE: 55
```

## A2

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: INT-2 ARM: INT STAGE: A2 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
ACTION: ZED
WORKING_RULE: Current hypothesis is ZED whenever Aster is ON; other features remain untested.
CONFIDENCE: 60
```

## A3

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: INT-2 ARM: INT STAGE: A3 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
ACTION: NOVA
WORKING_RULE: Current hypothesis is NOVA when Beryl is ON and ZED when Beryl is OFF.
CONFIDENCE: 65
```

## A4

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: INT-2 ARM: INT STAGE: A4 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
ACTION: ZED
WORKING_RULE: Current hypothesis is NOVA when Beryl is ON and ZED when Beryl is OFF.
CONFIDENCE: 85
```

## A5

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: INT-2 ARM: INT STAGE: A5 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
ACTION: ZED
WORKING_RULE: Current hypothesis is NOVA when Beryl is ON and ZED when Beryl is OFF; Dune remains untested.
CONFIDENCE: 88
```

## A6

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: INT-2 ARM: INT STAGE: A6 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
ACTION: NOVA
WORKING_RULE: Current hypothesis is NOVA when Beryl or Dune is ON; otherwise ZED.
CONFIDENCE: 95
```

## A7

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: INT-2 ARM: INT STAGE: A7 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
FINAL_RULE: Route to NOVA when Beryl or Dune is ON; otherwise route to ZED.
CAUSAL_FEATURES: Beryl, Dune
IRRELEVANT_FEATURES: Aster, Coda
CONFIDENCE: 99
```

No scoring or correction was performed before preserving these outputs.
