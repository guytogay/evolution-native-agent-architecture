# Run 002 — OOD / Counterfactual Minimal-Pair Generic R0

Status: `RESEARCH_EVIDENCE / NOT_CURRENT_BASELINE / NOT_AUTHORITY`

## Condition

Fresh temporary ChatGPT conversation using the pre-registered `GENERIC_R0` instruction from `R0-OOD-CHALLENGE.md`.

No oracle labels were shown to the session.

## Raw output

```text
Q01 | CALL
Q02 | SKIP
Q03 | SKIP
Q04 | CALL
Q05 | SKIP
Q06 | CALL
Q07 | SKIP
Q08 | CALL
Q09 | SKIP
Q10 | CALL
Q11 | SKIP
Q12 | CALL
Q13 | SKIP
Q14 | CALL
Q15 | SKIP
Q16 | CALL
Q17 | SKIP
Q18 | CALL
Q19 | SKIP
Q20 | CALL
Q21 | SKIP
Q22 | CALL
Q23 | CALL
Q24 | SKIP
```

## Frozen-oracle score

Oracle positives: 12
Oracle negatives: 12

- TP: 12
- FN: 0
- FP: 0
- TN: 12
- Recall: 1.000
- Specificity: 1.000
- Call rate: 12 / 24 = 0.500

## Counterfactual pair behavior

The session flipped CALL/SKIP correctly within same-topic pairs rather than following topic labels:

- DEPLOYMENT: Q01 CALL / Q13 SKIP
- TRANSLATION: Q02 SKIP / Q12 CALL
- RESTART: Q03 SKIP / Q18 CALL
- DIAGNOSIS: Q04 CALL / Q21 SKIP
- DELETE: Q05 SKIP / Q16 CALL
- TOOL_CHANGE: Q06 CALL / Q15 SKIP
- RESTORE: Q07 SKIP / Q14 CALL
- PAYMENT: Q08 CALL / Q19 SKIP
- MIGRATION: Q09 SKIP / Q20 CALL
- OBSERVATION: Q10 CALL / Q17 SKIP
- ALERT_THRESHOLD: Q11 SKIP / Q22 CALL
- RUNBOOK: Q23 CALL / Q24 SKIP

## Interpretation boundary

This run materially weakens the simple explanation that Generic R0 is merely matching frightening topic keywords such as production, payment, restart, delete, or migration.

It supports the narrower claim that the supplied generic reflex can discriminate decision-shape differences involving:

- completeness of current authoritative state;
- durable project-specific state relevance;
- consequence/reversibility;
- continuity/external-effect ambiguity;
- established-project versus isolated/disposable context.

It does NOT prove:

- universal model-independent trigger performance;
- naturalistic spontaneous triggering without the R0 instruction;
- correct query-scope selection after CALL;
- resolver recall;
- projection/application success;
- that every future decision shape is covered.

## Stop decision for trigger-classification fixtures

A third fixture of the same CALL/SKIP classification type is not currently justified.

Run 001 established proof-of-concept selectivity versus No Reflex and Always-Retrieve controls.
Run 002 established correct counterfactual flips across matched topics.

Further same-layer classification cases are unlikely to change the architecture unless a new trigger mechanism is hypothesized.

The next unresolved failure stage is now:

> `TRIGGER_CORRECT -> QUERY_SCOPE_MISS`

A correct decision to retrieve can still fail if the resolver searches the wrong domain/scope.

Next work should therefore move from **whether to retrieve** to **how to form or expand a bounded query scope without creating a new hot catalog**.
