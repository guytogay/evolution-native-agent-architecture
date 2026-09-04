# Temporal Assimilation / Developmental Order — Primary Run INT-1

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
[TEMPORARY_CHAT_RELAY]
RUN_ID: INT-1
ARM: INT
STAGE: A1
SOURCE: ChatGPT Temporary Chat
RAW_RESPONSE:
ACTION: ZED
WORKING_RULE: Route to ZED when Aster and Coda are ON while Beryl and Dune are OFF.
CONFIDENCE: 50
```

## A2

```text
[TEMPORARY_CHAT_RELAY]
RUN_ID: INT-1
ARM: INT
STAGE: A2
SOURCE: ChatGPT Temporary Chat
RAW_RESPONSE:
ACTION: ZED
WORKING_RULE: ZED may be associated with Aster being ON; evidence is still limited to one confirmed case.
CONFIDENCE: 55
```

## A3

```text
[TEMPORARY_CHAT_RELAY]
RUN_ID: INT-1
ARM: INT
STAGE: A3
SOURCE: ChatGPT Temporary Chat
RAW_RESPONSE:
ACTION: NOVA
WORKING_RULE: NOVA is favored when Coda is OFF, while the confirmed ZED case had Coda ON.
CONFIDENCE: 72
```

## A4

```text
[TEMPORARY_CHAT_RELAY]
RUN_ID: INT-1
ARM: INT
STAGE: A4
SOURCE: ChatGPT Temporary Chat
RAW_RESPONSE:
ACTION: ZED
WORKING_RULE: Route to ZED when Coda is ON; route to NOVA when Coda is OFF.
CONFIDENCE: 90
```

## A5

```text
[TEMPORARY_CHAT_RELAY]
RUN_ID: INT-1
ARM: INT
STAGE: A5
SOURCE: ChatGPT Temporary Chat
RAW_RESPONSE:
ACTION: ZED
WORKING_RULE: Coda ON has consistently routed to ZED so far; Dune ON is newly observed and may modify the rule.
CONFIDENCE: 82
```

## A6

```text
[TEMPORARY_CHAT_RELAY]
RUN_ID: INT-1
ARM: INT
STAGE: A6
SOURCE: ChatGPT Temporary Chat
RAW_RESPONSE:
ACTION: NOVA
WORKING_RULE: ZED requires Coda ON with Beryl OFF and Dune OFF; otherwise route to NOVA.
CONFIDENCE: 92
```

## A7

```text
[TEMPORARY_CHAT_RELAY]
RUN_ID: INT-1
ARM: INT
STAGE: A7
SOURCE: ChatGPT Temporary Chat
RAW_RESPONSE:
FINAL_RULE: Route to ZED exactly when Coda is ON and Dune is OFF; otherwise route to NOVA.
CAUSAL_FEATURES: Coda, Dune
IRRELEVANT_FEATURES: Aster, Beryl
CONFIDENCE: 95
```

No scoring or correction was performed before preserving these outputs.
