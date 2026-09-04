You are participating in a controlled source-trust decision task.

Apply the assigned update policy **exactly as written**. Do not replace it with a smarter policy, combine it with another policy, or use outside knowledge. `RED`, `BLUE`, `GREEN`, `ORBIT`, `VALE`, `ZED`, and `NOVA` are opaque task labels.

For each historical episode, `ORBIT` and `VALE` make conflicting recommendations and an authoritative correct action is shown. The source whose recommendation matches the correct action won that episode.

## Assigned update policy: G1 — GLOBAL_RECENT3

- Maintain one global source preference across all contexts.
- After the history, trust the source that won a majority of the most recent 3 labeled episodes overall.
- Apply that global preference in every context, including contexts not previously seen.
- If the most recent 3 episodes are tied in a way that does not justify a source preference, use `UNRESOLVED` / `INSUFFICIENT`.

## Historical ledger

| ID | Context | ORBIT | VALE | Correct |
|---|---|---|---|---|
| H1 | RED  | ZED  | NOVA | ZED |
| H2 | BLUE | NOVA | ZED  | NOVA |
| H3 | RED  | NOVA | ZED  | NOVA |
| H4 | BLUE | ZED  | NOVA | ZED |
| H5 | RED  | ZED  | NOVA | ZED |
| H6 | BLUE | NOVA | ZED  | NOVA |
| H7 | RED  | NOVA | ZED  | NOVA |
| H8 | BLUE | ZED  | NOVA | ZED |
| H9 | RED  | ZED  | NOVA | NOVA |
| H10 | BLUE | NOVA | ZED  | NOVA |
| H11 | RED  | NOVA | ZED  | ZED |
| H12 | BLUE | ZED  | NOVA | ZED |
| H13 | RED  | ZED  | NOVA | NOVA |
| H14 | BLUE | NOVA | ZED  | ZED |
| H15 | RED  | NOVA | ZED  | ZED |
| H16 | BLUE | ZED  | NOVA | NOVA |

After the history, report the source-trust state implied by the assigned policy for RED, BLUE, and GREEN. Use `UNRESOLVED` if the policy does not justify preferring either source.

Then answer the transfer battery. The transfer items do **not** reveal authoritative outcomes. Use only the assigned update policy and the history above. If the policy gives no justified preference while the sources conflict, answer `INSUFFICIENT`.

## Transfer battery

| ID | Context | ORBIT | VALE |
|---|---|---|---|
| T1 | RED   | ZED  | NOVA |
| T2 | RED   | NOVA | ZED |
| T3 | RED   | ZED  | NOVA |
| T4 | RED   | NOVA | ZED |
| T5 | BLUE  | ZED  | NOVA |
| T6 | BLUE  | NOVA | ZED |
| T7 | BLUE  | ZED  | NOVA |
| T8 | BLUE  | NOVA | ZED |
| T9 | GREEN | ZED  | NOVA |
| T10 | GREEN | NOVA | ZED |

Return **only** the following format, with no rationale or extra text:

STATE_RED: ORBIT|VALE|UNRESOLVED
STATE_BLUE: ORBIT|VALE|UNRESOLVED
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
