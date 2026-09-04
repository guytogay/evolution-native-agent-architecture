# Temporal Assimilation / Developmental Order v1 — Frozen Relay Fixture

Status: `FROZEN_BEFORE_PRIMARY_OUTPUTS`

Parent preregistration:

`research/field-validation/2026-09-04-temporal-assimilation-developmental-order-preregistration.md`

## Relay rule

Only one stage block may be sent to the Temporary Chat at a time. Do not send this whole file to the experimental subject.

The Codex relay copies the selected block verbatim. The manager controls which block is released.

No future stage, oracle table, arm comparison or ENA project context is exposed to the Temporary Chat.

---

# Common acquisition instructions

The following text is included only in each run's `A1` stage before that arm's first case.

```text
You are participating in a synthetic sequential-learning task.

There is an unknown routing rule. Each case has four binary features: Aster, Beryl, Coda, and Dune. The only possible routing actions during acquisition are ZED and NOVA.

You will see one case at a time. For the first case, make a prediction. On each later turn you will first receive the authoritative correct action for the previous case and then a new case to predict.

Treat authoritative feedback as ground truth. Do not browse, use external tools, or assume any real-world meaning for the feature names. Learn only from the cases and feedback in this conversation.

For every acquisition prediction, output exactly these three lines and nothing else:
ACTION: ZED | NOVA
WORKING_RULE: <one sentence, maximum 25 words>
CONFIDENCE: <integer 0-100>
```

---

# Arm CF — corrective/boundary-first

## CF / A1

```text
You are participating in a synthetic sequential-learning task.

There is an unknown routing rule. Each case has four binary features: Aster, Beryl, Coda, and Dune. The only possible routing actions during acquisition are ZED and NOVA.

You will see one case at a time. For the first case, make a prediction. On each later turn you will first receive the authoritative correct action for the previous case and then a new case to predict.

Treat authoritative feedback as ground truth. Do not browse, use external tools, or assume any real-world meaning for the feature names. Learn only from the cases and feedback in this conversation.

For every acquisition prediction, output exactly these three lines and nothing else:
ACTION: ZED | NOVA
WORKING_RULE: <one sentence, maximum 25 words>
CONFIDENCE: <integer 0-100>

CASE E3
Aster=ON
Beryl=ON
Coda=OFF
Dune=OFF

Predict the routing action for E3 now.
```

## CF / A2

```text
AUTHORITATIVE_FEEDBACK: E3 correct action was NOVA.

CASE E4
Aster=OFF
Beryl=OFF
Coda=ON
Dune=OFF

Using everything learned so far, predict E4. Output exactly the same three-line acquisition format.
```

## CF / A3

```text
AUTHORITATIVE_FEEDBACK: E4 correct action was ZED.

CASE E1
Aster=ON
Beryl=OFF
Coda=ON
Dune=OFF

Using everything learned so far, predict E1. Output exactly the same three-line acquisition format.
```

## CF / A4

```text
AUTHORITATIVE_FEEDBACK: E1 correct action was ZED.

CASE E2
Aster=OFF
Beryl=ON
Coda=OFF
Dune=OFF

Using everything learned so far, predict E2. Output exactly the same three-line acquisition format.
```

## CF / A5

```text
AUTHORITATIVE_FEEDBACK: E2 correct action was NOVA.

CASE E5
Aster=ON
Beryl=OFF
Coda=ON
Dune=ON

Using everything learned so far, predict E5. Output exactly the same three-line acquisition format.
```

## CF / A6

```text
AUTHORITATIVE_FEEDBACK: E5 correct action was NOVA.

CASE E6
Aster=OFF
Beryl=ON
Coda=ON
Dune=ON

Using everything learned so far, predict E6. Output exactly the same three-line acquisition format.
```

## CF / A7

Use the common A7 block below.

---

# Arm INT — interleaved

## INT / A1

```text
You are participating in a synthetic sequential-learning task.

There is an unknown routing rule. Each case has four binary features: Aster, Beryl, Coda, and Dune. The only possible routing actions during acquisition are ZED and NOVA.

You will see one case at a time. For the first case, make a prediction. On each later turn you will first receive the authoritative correct action for the previous case and then a new case to predict.

Treat authoritative feedback as ground truth. Do not browse, use external tools, or assume any real-world meaning for the feature names. Learn only from the cases and feedback in this conversation.

For every acquisition prediction, output exactly these three lines and nothing else:
ACTION: ZED | NOVA
WORKING_RULE: <one sentence, maximum 25 words>
CONFIDENCE: <integer 0-100>

CASE E1
Aster=ON
Beryl=OFF
Coda=ON
Dune=OFF

Predict the routing action for E1 now.
```

## INT / A2

```text
AUTHORITATIVE_FEEDBACK: E1 correct action was ZED.

CASE E3
Aster=ON
Beryl=ON
Coda=OFF
Dune=OFF

Using everything learned so far, predict E3. Output exactly the same three-line acquisition format.
```

## INT / A3

```text
AUTHORITATIVE_FEEDBACK: E3 correct action was NOVA.

CASE E2
Aster=OFF
Beryl=ON
Coda=OFF
Dune=OFF

Using everything learned so far, predict E2. Output exactly the same three-line acquisition format.
```

## INT / A4

```text
AUTHORITATIVE_FEEDBACK: E2 correct action was NOVA.

CASE E4
Aster=OFF
Beryl=OFF
Coda=ON
Dune=OFF

Using everything learned so far, predict E4. Output exactly the same three-line acquisition format.
```

## INT / A5

```text
AUTHORITATIVE_FEEDBACK: E4 correct action was ZED.

CASE E5
Aster=ON
Beryl=OFF
Coda=ON
Dune=ON

Using everything learned so far, predict E5. Output exactly the same three-line acquisition format.
```

## INT / A6

```text
AUTHORITATIVE_FEEDBACK: E5 correct action was NOVA.

CASE E6
Aster=OFF
Beryl=ON
Coda=ON
Dune=ON

Using everything learned so far, predict E6. Output exactly the same three-line acquisition format.
```

## INT / A7

Use the common A7 block below.

---

# Arm MF — misleading-first

## MF / A1

```text
You are participating in a synthetic sequential-learning task.

There is an unknown routing rule. Each case has four binary features: Aster, Beryl, Coda, and Dune. The only possible routing actions during acquisition are ZED and NOVA.

You will see one case at a time. For the first case, make a prediction. On each later turn you will first receive the authoritative correct action for the previous case and then a new case to predict.

Treat authoritative feedback as ground truth. Do not browse, use external tools, or assume any real-world meaning for the feature names. Learn only from the cases and feedback in this conversation.

For every acquisition prediction, output exactly these three lines and nothing else:
ACTION: ZED | NOVA
WORKING_RULE: <one sentence, maximum 25 words>
CONFIDENCE: <integer 0-100>

CASE E1
Aster=ON
Beryl=OFF
Coda=ON
Dune=OFF

Predict the routing action for E1 now.
```

## MF / A2

```text
AUTHORITATIVE_FEEDBACK: E1 correct action was ZED.

CASE E2
Aster=OFF
Beryl=ON
Coda=OFF
Dune=OFF

Using everything learned so far, predict E2. Output exactly the same three-line acquisition format.
```

## MF / A3

```text
AUTHORITATIVE_FEEDBACK: E2 correct action was NOVA.

CASE E3
Aster=ON
Beryl=ON
Coda=OFF
Dune=OFF

Using everything learned so far, predict E3. Output exactly the same three-line acquisition format.
```

## MF / A4

```text
AUTHORITATIVE_FEEDBACK: E3 correct action was NOVA.

CASE E4
Aster=OFF
Beryl=OFF
Coda=ON
Dune=OFF

Using everything learned so far, predict E4. Output exactly the same three-line acquisition format.
```

## MF / A5

```text
AUTHORITATIVE_FEEDBACK: E4 correct action was ZED.

CASE E5
Aster=ON
Beryl=OFF
Coda=ON
Dune=ON

Using everything learned so far, predict E5. Output exactly the same three-line acquisition format.
```

## MF / A6

```text
AUTHORITATIVE_FEEDBACK: E5 correct action was NOVA.

CASE E6
Aster=OFF
Beryl=ON
Coda=ON
Dune=ON

Using everything learned so far, predict E6. Output exactly the same three-line acquisition format.
```

## MF / A7

Use the common A7 block below.

---

# Common A7 — acquisition close

```text
AUTHORITATIVE_FEEDBACK: E6 correct action was NOVA.

You have now received authoritative feedback for all six training cases.

Without receiving any additional cases or hints, state the rule you currently believe governs routing.

Output exactly these four lines and nothing else:
FINAL_RULE: <one sentence, maximum 30 words>
CAUSAL_FEATURES: <comma-separated feature names, or NONE>
IRRELEVANT_FEATURES: <comma-separated feature names, or NONE>
CONFIDENCE: <integer 0-100>
```

---

# Common B1 — pre-correction transfer battery

```text
Now apply the rule you learned to a transfer battery.

For P1-P8, choose ZED or NOVA.
For L1-L2, use this exact feature mapping:
P=Aster, Q=Beryl, R=Coda, S=Dune.
For U1, INSUFFICIENT is also allowed if the available information cannot determine the action.

Do not explain your reasoning. Output exactly one line per item in this format:
<ID>: <ZED|NOVA|INSUFFICIENT>, <confidence 0-100>

P1: Aster=ON,  Beryl=ON,  Coda=ON,  Dune=OFF
P2: Aster=OFF, Beryl=OFF, Coda=OFF, Dune=OFF
P3: Aster=ON,  Beryl=ON,  Coda=OFF, Dune=ON
P4: Aster=OFF, Beryl=ON,  Coda=ON,  Dune=OFF
P5: Aster=ON,  Beryl=OFF, Coda=OFF, Dune=OFF
P6: Aster=OFF, Beryl=OFF, Coda=ON,  Dune=ON
P7: Aster=ON,  Beryl=ON,  Coda=ON,  Dune=ON
P8: Aster=OFF, Beryl=ON,  Coda=OFF, Dune=ON
L1: P=ON, Q=ON,  R=ON,  S=OFF
L2: P=ON, Q=OFF, R=OFF, S=OFF
U1: Aster=ON, Beryl=OFF, Coda=ON, Dune=UNKNOWN
```

---

# Common C1 — identical explicit correction + post-correction transfer battery

```text
AUTHORITATIVE FINAL RULE

ZED iff Coda=ON AND Dune=OFF.
Otherwise NOVA.
Aster and Beryl never affect routing.
If either Coda or Dune is unknown, the routing action cannot be determined from the available information.

Apply that authoritative rule to the new transfer battery below.

For C1-C6, choose ZED or NOVA.
For C7-C8, use this exact feature mapping:
J=Aster, K=Beryl, M=Coda, N=Dune.
For C9, INSUFFICIENT is also allowed if the available information cannot determine the action.

Do not explain your reasoning. Output exactly one line per item in this format:
<ID>: <ZED|NOVA|INSUFFICIENT>, <confidence 0-100>

C1: Aster=ON,  Beryl=OFF, Coda=ON,  Dune=OFF
C2: Aster=ON,  Beryl=ON,  Coda=OFF, Dune=OFF
C3: Aster=OFF, Beryl=OFF, Coda=ON,  Dune=ON
C4: Aster=OFF, Beryl=ON,  Coda=ON,  Dune=OFF
C5: Aster=OFF, Beryl=OFF, Coda=OFF, Dune=ON
C6: Aster=ON,  Beryl=ON,  Coda=OFF, Dune=ON
C7: J=ON,  K=OFF, M=ON,  N=OFF
C8: J=OFF, K=ON,  M=OFF, N=OFF
C9: Aster=OFF, Beryl=ON, Coda=UNKNOWN, Dune=OFF
```

---

# Manager-only oracle

Do not send this section to the Temporary Chat.

Hidden acquisition rule:

```text
ZED iff Coda=ON AND Dune=OFF.
Otherwise NOVA.
Aster and Beryl are irrelevant.
```

Pre-correction oracle:

```text
P1 ZED
P2 NOVA
P3 NOVA
P4 ZED
P5 NOVA
P6 NOVA
P7 NOVA
P8 NOVA
L1 ZED
L2 NOVA
U1 INSUFFICIENT
```

Post-correction oracle:

```text
C1 ZED
C2 NOVA
C3 NOVA
C4 ZED
C5 NOVA
C6 NOVA
C7 ZED
C8 NOVA
C9 INSUFFICIENT
```

Primary valid-run order:

```text
CF-1
INT-1
MF-1
MF-2
INT-2
CF-2
CF-3
MF-3
INT-3
```
