# Temporal Assimilation / Developmental Order — Primary Run CF-1

Status: `EXCLUDED_PROTOCOL_DEVIATION / RAW_FIRST_OUTPUTS_PRESERVED`

Preregistration:
`research/field-validation/2026-09-04-temporal-assimilation-developmental-order-preregistration.md`

Frozen fixture:
`research/field-validation/fixtures/temporal-assimilation-order-v1/FIXTURE.md`

Host claim through A7: `ChatGPT Temporary Chat / GPT-5.6 Sol`
Relay role: `Codex transport only`
Arm: `CF — corrective/boundary-first`

Objective exclusion reason:

> At B1 the relay reported `SOURCE: ChatGPT Temporary Chat (rebuilt continuity; original tab unavailable)`. The preregistered protocol requires all stages of one run to remain in the same Temporary Chat. Therefore CF-1 is excluded from the primary set independent of behavioral quality. No later stages will be collected for this attempt.

## A1

```text
[TEMPORARY_CHAT_RELAY]
RUN_ID: CF-1
ARM: CF
STAGE: A1
SOURCE: ChatGPT Temporary Chat
RAW_RESPONSE:
ACTION: ZED
WORKING_RULE: Cases with Aster and Beryl ON route to ZED unless later feedback indicates a different interaction.
CONFIDENCE: 50
```

## A2

```text
[TEMPORARY_CHAT_RELAY]
RUN_ID: CF-1
ARM: CF
STAGE: A2
SOURCE: ChatGPT Temporary Chat
RAW_RESPONSE:
ACTION: NOVA
WORKING_RULE: Current evidence suggests NOVA may apply broadly; no feedback yet distinguishes Coda-positive cases from the observed NOVA case.
CONFIDENCE: 35
```

## A3

```text
[TEMPORARY_CHAT_RELAY]
RUN_ID: CF-1
ARM: CF
STAGE: A3
SOURCE: ChatGPT Temporary Chat
RAW_RESPONSE:
ACTION: ZED
WORKING_RULE: Current evidence is consistent with Coda ON routing to ZED and Coda OFF routing to NOVA.
CONFIDENCE: 50
```

## A4

```text
[TEMPORARY_CHAT_RELAY]
RUN_ID: CF-1
ARM: CF
STAGE: A4
SOURCE: ChatGPT Temporary Chat
RAW_RESPONSE:
ACTION: NOVA
WORKING_RULE: All observed cases fit Coda ON routing to ZED and Coda OFF routing to NOVA.
CONFIDENCE: 85
```

## A5

```text
[TEMPORARY_CHAT_RELAY]
RUN_ID: CF-1
ARM: CF
STAGE: A5
SOURCE: ChatGPT Temporary Chat
RAW_RESPONSE:
ACTION: ZED
WORKING_RULE: All observed cases route by Coda: ON gives ZED and OFF gives NOVA; Dune has not yet been tested.
CONFIDENCE: 90
```

## A6

```text
[TEMPORARY_CHAT_RELAY]
RUN_ID: CF-1
ARM: CF
STAGE: A6
SOURCE: ChatGPT Temporary Chat
RAW_RESPONSE:
ACTION: NOVA
WORKING_RULE: Current evidence fits ZED only when Coda is ON and Dune is OFF; otherwise route to NOVA.
CONFIDENCE: 90
```

## A7

```text
[TEMPORARY_CHAT_RELAY]
RUN_ID: CF-1
ARM: CF
STAGE: A7
SOURCE: ChatGPT Temporary Chat
RAW_RESPONSE:
FINAL_RULE: Route to ZED exactly when Coda is ON and Dune is OFF; otherwise route to NOVA.
CAUSAL_FEATURES: Coda, Dune
IRRELEVANT_FEATURES: Aster, Beryl
CONFIDENCE: 100
```

## B1 — protocol-deviant continuity rebuild

```text
[TEMPORARY_CHAT_RELAY]
RUN_ID: CF-1
ARM: CF
STAGE: B1
SOURCE: ChatGPT Temporary Chat (rebuilt continuity; original tab unavailable)
RAW_RESPONSE:
P1: ZED, 95
P2: NOVA, 95
P3: NOVA, 95
P4: ZED, 95
P5: NOVA, 95
P6: NOVA, 95
P7: NOVA, 95
P8: NOVA, 95
L1: ZED, 95
L2: NOVA, 95
U1: INSUFFICIENT, 100
```

Primary scoring status: `NOT_SCORED / EXCLUDED_BEFORE_B1_PRIMARY_ADJUDICATION`

Replacement: `CF-R1`.
