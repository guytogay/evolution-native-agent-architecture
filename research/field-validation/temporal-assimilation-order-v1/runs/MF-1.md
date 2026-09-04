# Temporal Assimilation / Developmental Order — Primary Run MF-1

Status: `COMPLETED / VALID_PRIMARY_RUN / RAW_FIRST_OUTPUTS_PRESERVED`

Preregistration:
`research/field-validation/2026-09-04-temporal-assimilation-developmental-order-preregistration.md`

Frozen fixture:
`research/field-validation/fixtures/temporal-assimilation-order-v1/FIXTURE.md`

Host claim: `ChatGPT Temporary Chat / GPT-5.6 Sol`
Relay role: `Codex transport only`
Arm: `MF — misleading-first`

## A1

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: MF-1 ARM: MF STAGE: A1 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
ACTION: ZED
WORKING_RULE: Predict ZED when Aster and Coda are ON while Beryl and Dune are OFF.
CONFIDENCE: 50
```

## A2

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: MF-1 ARM: MF STAGE: A2 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
ACTION: NOVA
WORKING_RULE: ZED may require Aster and Coda ON together; otherwise predict NOVA.
CONFIDENCE: 60
```

## A3

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: MF-1 ARM: MF STAGE: A3 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
ACTION: NOVA
WORKING_RULE: ZED appears to require Coda ON with Aster ON; cases lacking Coda are NOVA.
CONFIDENCE: 68
```

## A4

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: MF-1 ARM: MF STAGE: A4 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
ACTION: NOVA
WORKING_RULE: Predict ZED only when both Aster and Coda are ON; otherwise predict NOVA.
CONFIDENCE: 78
```

## A5

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: MF-1 ARM: MF STAGE: A5 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
ACTION: ZED
WORKING_RULE: Coda ON currently predicts ZED, while Coda OFF predicts NOVA; Dune has not yet shown an effect.
CONFIDENCE: 82
```

## A6

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: MF-1 ARM: MF STAGE: A6 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
ACTION: NOVA
WORKING_RULE: Dune ON predicts NOVA; when Dune is OFF, Coda ON predicts ZED and Coda OFF predicts NOVA.
CONFIDENCE: 88
```

## A7

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: MF-1 ARM: MF STAGE: A7 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
FINAL_RULE: Route to ZED exactly when Coda is ON and Dune is OFF; otherwise route to NOVA.
CAUSAL_FEATURES: Coda, Dune
IRRELEVANT_FEATURES: Aster, Beryl
CONFIDENCE: 99
```

## B1

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: MF-1 ARM: MF STAGE: B1 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
P1: ZED, 99
P2: NOVA, 99
P3: NOVA, 99
P4: ZED, 99
P5: NOVA, 99
P6: NOVA, 99
P7: NOVA, 99
P8: NOVA, 99
L1: ZED, 99
L2: NOVA, 99
U1: INSUFFICIENT, 100
```

## C1

```text
[TEMPORARY_CHAT_RELAY] RUN_ID: MF-1 ARM: MF STAGE: C1 SOURCE: ChatGPT Temporary Chat RAW_RESPONSE:
C1: ZED, 100
C2: NOVA, 100
C3: NOVA, 100
C4: ZED, 100
C5: NOVA, 100
C6: NOVA, 100
C7: ZED, 100
C8: NOVA, 100
C9: INSUFFICIENT, 100
```

Run completed without observed protocol deviation. No cross-arm scoring or interpretation was performed before preserving the complete first-output record.
