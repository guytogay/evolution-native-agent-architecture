# Metamemory Update Policy v1 — Primary Launch Bundle

Status: `EXECUTION_WRAPPER_ONLY / FROZEN_TREATMENTS_UNCHANGED / PRIMARY_NOT_STARTED`

This file is for the **mechanical relay/operator**, not the experimental Temporary Chats.

It does not change the frozen scientific design.

## Freeze binding

Merged preregistration/fixture commit:

```text
dffd1179d260788e5c763facdf61876c3162401f
```

Frozen preregistration blob:

```text
research/field-validation/2026-09-04-metamemory-update-policy-preregistration.md
blob 5384c09cfb0cc12dc51f79af30ba66cbb133811b
```

Frozen treatment blobs on `main`:

```text
S0  research/field-validation/fixtures/metamemory-update-policy-v1/PROMPT-S0-STATIC-EQUAL.md
    blob 419740e665c274a0dee941adf1344b5a508c4f0b

G1  research/field-validation/fixtures/metamemory-update-policy-v1/PROMPT-G1-GLOBAL-RECENT3.md
    blob f8cbe6fce6c350eb807fec30fdfa704ee231bf15

C1  research/field-validation/fixtures/metamemory-update-policy-v1/PROMPT-C1-CONTEXT-RECENT3.md
    blob e5c8abb4fa1a0fd063915fed8db102f96867f1eb

C2  research/field-validation/fixtures/metamemory-update-policy-v1/PROMPT-C2-CONTEXT-REVERSIBLE3.md
    blob f6767ad8e6c85dc6bbb4c94a4ae1232efdcf42ac
```

If any treatment file on `main` no longer has the bound blob identity above, **stop before collection** and report the mismatch. Do not silently use a changed treatment.

## Relay role

The relay is transport only.

It must not:

- score or interpret responses;
- reveal expected states, hidden oracle, preregistered scores or other-arm information;
- paraphrase, shorten or prepend text to a treatment;
- reuse one Temporary Chat across arms;
- correct or tutor a worker;
- retry because a response looks wrong;
- expose this launch bundle to an experimental worker.

## Initial primary run set

Run exactly these four initial runs:

```text
S0-1
G1-1
C1-1
C2-1
```

Order of launching the independent chats is operationally irrelevant, but use the order above unless there is a mechanical reason not to.

## Procedure for each run

For each run:

1. Open a **new ChatGPT Temporary Chat**.
2. Confirm the same visible primary Host/model configuration used for all four runs: `GPT-5.6 Sol`.
3. Retrieve the matching frozen prompt from `main` at the bound path above.
4. Paste/send the **entire prompt verbatim as the first user message**. Add nothing before or after it.
5. Capture the **first complete assistant response verbatim**.
6. Do not send any follow-up message in that Temporary Chat.
7. Close/retire the chat from the active workflow after capture; never reuse it for another arm.

If an objective execution failure occurs before a first complete response can be preserved, mark the attempt `PROTOCOL_FAILURE` and report the exact reason. Do not self-authorize a replacement. The manager will apply the frozen replacement rule.

A strange, wrong, low-confidence, nonconforming or refusal-like first response is **behavioral data**, not automatically a protocol failure.

## Return format

Return all four captured outputs together in one bundle if possible, so the human does not have to relay each run separately.

Use exactly this outer wrapper; do not edit the raw response text inside it:

```text
[METAMEMORY_PRIMARY_BUNDLE]
FREEZE_COMMIT: dffd1179d260788e5c763facdf61876c3162401f
HOST: ChatGPT Temporary Chat
MODEL: GPT-5.6 Sol

[RUN]
RUN_ID: S0-1
ARM: S0_STATIC_EQUAL
TREATMENT_BLOB: 419740e665c274a0dee941adf1344b5a508c4f0b
STATUS: COMPLETE | PROTOCOL_FAILURE
PROTOCOL_NOTE: <NONE or exact objective failure>
RAW_RESPONSE:
<verbatim first complete response, or NONE if objectively unavailable>
[/RUN]

[RUN]
RUN_ID: G1-1
ARM: G1_GLOBAL_RECENT3
TREATMENT_BLOB: f8cbe6fce6c350eb807fec30fdfa704ee231bf15
STATUS: COMPLETE | PROTOCOL_FAILURE
PROTOCOL_NOTE: <NONE or exact objective failure>
RAW_RESPONSE:
<verbatim first complete response, or NONE if objectively unavailable>
[/RUN]

[RUN]
RUN_ID: C1-1
ARM: C1_CONTEXT_RECENT3
TREATMENT_BLOB: e5c8abb4fa1a0fd063915fed8db102f96867f1eb
STATUS: COMPLETE | PROTOCOL_FAILURE
PROTOCOL_NOTE: <NONE or exact objective failure>
RAW_RESPONSE:
<verbatim first complete response, or NONE if objectively unavailable>
[/RUN]

[RUN]
RUN_ID: C2-1
ARM: C2_CONTEXT_REVERSIBLE3
TREATMENT_BLOB: f6767ad8e6c85dc6bbb4c94a4ae1232efdcf42ac
STATUS: COMPLETE | PROTOCOL_FAILURE
PROTOCOL_NOTE: <NONE or exact objective failure>
RAW_RESPONSE:
<verbatim first complete response, or NONE if objectively unavailable>
[/RUN]
[/METAMEMORY_PRIMARY_BUNDLE]
```

## After return

The relay stops.

The manager will:

1. archive raw first outputs;
2. classify objective protocol validity;
3. score M1-M7 against the already frozen preregistration;
4. apply the all-arm replication trigger only after all four valid initial outputs are available;
5. either close Track 5 or launch exactly the preregistered second all-arm replicate.

The relay must not decide whether replication is scientifically desirable.
