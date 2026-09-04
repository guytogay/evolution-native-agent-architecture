# Temporal Assimilation v1 — Primary Run Ledger

This is a run-status ledger, not formal adjudication.

## Valid primary runs

```text
CF:  CF-R1, CF-2, CF-3
MF:  MF-1, MF-2, MF-3
INT: INT-1, INT-2, INT-R1
```

Mechanical acquisition-end observation:

```text
Correct A7 Coda/Dune rule: CF-2, MF-1, MF-3, INT-1, INT-R1
Wrong A7 Beryl/Dune rule: CF-R1, CF-3, MF-2, INT-2
```

For each wrong-A7 valid run above, B1 followed the learned wrong rule and C1 followed the later authoritative final rule correctly. The correct-A7 runs were B1/C1 action-correct. Use raw files and the preregistration for formal scoring; do not infer the experiment verdict from this summary alone.

## Excluded attempts

- `CF-1`: original Temporary Chat unavailable before B1; continuity rebuilt; exclude from primary scoring.
- `INT-3`: Temporary Chat closed after A2; exclude; `INT-R1` is replacement.

## Persistence notes

- `CF-3`: valid run; A7/B1/C1 later backfilled from verbatim manager-session capture after connector write failures.
- `MF-3`: valid run; A5 stored reversibly as Base64 due connector persistence failure.
- `INT-R1`: valid run; some returned bodies lacked canonical wrapper while run/stage/same-session continuity remained explicit.
