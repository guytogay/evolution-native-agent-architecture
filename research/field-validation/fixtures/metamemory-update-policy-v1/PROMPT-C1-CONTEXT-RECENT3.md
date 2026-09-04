You are participating in a controlled source-trust decision task.

Apply the assigned update policy **exactly as written**. Do not replace it with a smarter policy, combine it with another policy, or use outside knowledge. `RED`, `BLUE`, `GOLD`, `SILVER`, `GREEN`, `ORBIT`, `VALE`, `ZED`, and `NOVA` are opaque task labels.

For each historical episode, `ORBIT` and `VALE` make conflicting recommendations and an authoritative correct action is shown. The source whose recommendation matches the correct action won that episode.

## Assigned update policy: C1 — CONTEXT_RECENT3

- Maintain a separate source preference for each context.
- For a known context, trust the source that won a majority of the most recent 3 labeled episodes in that context.
- For an unseen context with no history, use `UNRESOLVED`; if the sources conflict there, answer `INSUFFICIENT`.
- Do not transfer a preference learned in one context to another context.

## Historical ledger

| ID | Context | ORBIT | VALE | Correct |
|---|---|---|---|---|
| H1 | RED | ZED | NOVA | ZED |
| H2 | BLUE | NOVA | ZED | NOVA |
| H3 | GOLD | ZED | NOVA | ZED |
| H4 | SILVER | NOVA | ZED | NOVA |
| H5 | RED | NOVA | ZED | NOVA |
| H6 | BLUE | ZED | NOVA | ZED |
| H7 | GOLD | NOVA | ZED | NOVA |
| H8 | SILVER | ZED | NOVA | ZED |
| H9 | RED | ZED | NOVA | ZED |
| H10 | BLUE | NOVA | ZED | NOVA |
| H11 | GOLD | ZED | NOVA | ZED |
| H12 | SILVER | NOVA | ZED | NOVA |
| H13 | RED | NOVA | ZED | NOVA |
| H14 | BLUE | ZED | NOVA | ZED |
| H15 | GOLD | NOVA | ZED | NOVA |
| H16 | SILVER | ZED | NOVA | ZED |
| H17 | RED | ZED | NOVA | NOVA |
| H18 | BLUE | NOVA | ZED | ZED |
| H19 | GOLD | ZED | NOVA | NOVA |
| H20 | SILVER | NOVA | ZED | ZED |
| H21 | RED | NOVA | ZED | ZED |
| H22 | BLUE | ZED | NOVA | NOVA |
| H23 | GOLD | NOVA | ZED | ZED |
| H24 | SILVER | ZED | NOVA | NOVA |
| H25 | RED | ZED | NOVA | NOVA |
| H26 | SILVER | NOVA | ZED | ZED |
| H27 | RED | NOVA | ZED | ZED |

After the history, report the source-trust state implied by the assigned policy for RED, BLUE, GOLD, SILVER, and GREEN. Use `UNRESOLVED` if the policy does not justify preferring either source.

Then answer the transfer battery. The transfer items do **not** reveal authoritative outcomes. Use only the assigned update policy and the history above. If the policy gives no justified preference while the sources conflict, answer `INSUFFICIENT`.

## Transfer battery

| ID | Context | ORBIT | VALE |
|---|---|---|---|
| T1 | RED | ZED | NOVA |
| T2 | RED | NOVA | ZED |
| T3 | RED | ZED | NOVA |
| T4 | RED | NOVA | ZED |
| T5 | BLUE | ZED | NOVA |
| T6 | BLUE | NOVA | ZED |
| T7 | BLUE | ZED | NOVA |
| T8 | BLUE | NOVA | ZED |
| T9 | GOLD | ZED | NOVA |
| T10 | GOLD | NOVA | ZED |
| T11 | GOLD | ZED | NOVA |
| T12 | GOLD | NOVA | ZED |
| T13 | SILVER | ZED | NOVA |
| T14 | SILVER | NOVA | ZED |
| T15 | SILVER | ZED | NOVA |
| T16 | SILVER | NOVA | ZED |
| T17 | GREEN | ZED | NOVA |
| T18 | GREEN | NOVA | ZED |

Return **only** the following format, with no rationale or extra text:

STATE_RED: ORBIT|VALE|UNRESOLVED
STATE_BLUE: ORBIT|VALE|UNRESOLVED
STATE_GOLD: ORBIT|VALE|UNRESOLVED
STATE_SILVER: ORBIT|VALE|UNRESOLVED
STATE_GREEN: ORBIT|VALE|UNRESOLVED
T1: ZED|NOVA|INSUFFICIENT, <confidence 0-100>
T2: ZED|NOVA|INSUFFICIENT, <confidence 0-100>
T3: ZED|NOVA|INSUFFICIENT, <confidence 0-100>
T4: ZED|NOVA|INSUFFICIENT, <confidence 0-100>
T5: ZED|NOVA|INSUFFICIENT, <confidence 0-100>
T6: ZED|NOVA|INSUFFICIENT, <confidence 0-100>
T7: ZED|NOVA|INSUFFICIENT, <confidence 0-100>
T8: ZED|NOVA|INSUFFICIENT, <confidence 0-100>
T9: ZED|NOVA|INSUFFICIENT, <confidence 0-100>
T10: ZED|NOVA|INSUFFICIENT, <confidence 0-100>
T11: ZED|NOVA|INSUFFICIENT, <confidence 0-100>
T12: ZED|NOVA|INSUFFICIENT, <confidence 0-100>
T13: ZED|NOVA|INSUFFICIENT, <confidence 0-100>
T14: ZED|NOVA|INSUFFICIENT, <confidence 0-100>
T15: ZED|NOVA|INSUFFICIENT, <confidence 0-100>
T16: ZED|NOVA|INSUFFICIENT, <confidence 0-100>
T17: ZED|NOVA|INSUFFICIENT, <confidence 0-100>
T18: ZED|NOVA|INSUFFICIENT, <confidence 0-100>
