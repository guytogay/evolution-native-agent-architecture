# Temporal Assimilation / Developmental Order — Replacement Run CF-R1

Status: `IN_PROGRESS / RAW_FIRST_OUTPUTS_PRESERVED`

Preregistration:
`research/field-validation/2026-09-04-temporal-assimilation-developmental-order-preregistration.md`

Frozen fixture:
`research/field-validation/fixtures/temporal-assimilation-order-v1/FIXTURE.md`

Host claim: `ChatGPT Temporary Chat / GPT-5.6 Sol`
Relay role: `Codex transport only`
Arm: `CF — corrective/boundary-first`
Replacement for: `CF-1` (excluded for rebuilt continuity before B1)

## A1

```text
[TEMPORARY_CHAT_RELAY]
RUN_ID: CF-R1
ARM: CF
STAGE: A1
SOURCE: ChatGPT Temporary Chat
RAW_RESPONSE:
ACTION: ZED
WORKING_RULE: With no feedback yet, provisionally route cases with Aster and Beryl ON to ZED.
CONFIDENCE: 50
```

## A2

```text
[TEMPORARY_CHAT_RELAY]
RUN_ID: CF-R1
ARM: CF
STAGE: A2
SOURCE: ChatGPT Temporary Chat
RAW_RESPONSE:
ACTION: ZED
WORKING_RULE: Provisionally, cases without both Aster and Beryl ON route to ZED; the observed both-ON case routed NOVA.
CONFIDENCE: 35
```

## A3

```text
[TEMPORARY_CHAT_RELAY]
RUN_ID: CF-R1
ARM: CF
STAGE: A3
SOURCE: ChatGPT Temporary Chat
RAW_RESPONSE:
ACTION: ZED
WORKING_RULE: Cases route NOVA when Aster and Beryl are both ON; otherwise they route ZED.
CONFIDENCE: 65
```

## A4

```text
[TEMPORARY_CHAT_RELAY]
RUN_ID: CF-R1
ARM: CF
STAGE: A4
SOURCE: ChatGPT Temporary Chat
RAW_RESPONSE:
ACTION: ZED
WORKING_RULE: Cases route NOVA only when Aster and Beryl are both ON; all observed alternatives route ZED.
CONFIDENCE: 75
```

## A5

```text
[TEMPORARY_CHAT_RELAY]
RUN_ID: CF-R1
ARM: CF
STAGE: A5
SOURCE: ChatGPT Temporary Chat
RAW_RESPONSE:
ACTION: ZED
WORKING_RULE: Routing appears determined by Beryl: ON maps to NOVA, while OFF maps to ZED.
CONFIDENCE: 95
```

## A6

```text
[TEMPORARY_CHAT_RELAY]
RUN_ID: CF-R1
ARM: CF
STAGE: A6
SOURCE: ChatGPT Temporary Chat
RAW_RESPONSE:
ACTION: NOVA
WORKING_RULE: Route NOVA when Beryl is ON or when Aster and Dune are both ON; otherwise route ZED.
CONFIDENCE: 90
```

## A7

```text
[TEMPORARY_CHAT_RELAY]
RUN_ID: CF-R1
ARM: CF
STAGE: A7
SOURCE: ChatGPT Temporary Chat
RAW_RESPONSE:
FINAL_RULE: Route to NOVA if Beryl is ON or Dune is ON; otherwise route to ZED.
CAUSAL_FEATURES: Beryl, Dune
IRRELEVANT_FEATURES: Aster, Coda
CONFIDENCE: 99
```

No scoring or correction was performed before preserving these outputs.
