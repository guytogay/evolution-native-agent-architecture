# R0 OOD / counterfactual minimal-pair run 002

Status: `BEHAVIORAL_RESEARCH_EVIDENCE / NOT_CURRENT_BASELINE / NOT_AUTHORITY`

Condition: `GENERIC_R0`

Protocol: fresh ChatGPT Temporary Conversation; hidden oracle was not shown to the evaluated session. Same generic consequence-aware retrieval reflex as run-001. Task set was the pre-registered 24-case OOD/counterfactual minimal-pair challenge.

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

Oracle-positive cases: `Q01 Q04 Q06 Q08 Q10 Q12 Q14 Q16 Q18 Q20 Q22 Q23`

Oracle-negative cases: `Q02 Q03 Q05 Q07 Q09 Q11 Q13 Q15 Q17 Q19 Q21 Q24`

Result:

- TP = 12
- FN = 0
- FP = 0
- TN = 12
- recall = 100%
- specificity = 100%
- calls = 12/24

## Minimal-pair behavior

The same topical surface correctly flipped according to decision shape:

- `DEPLOYMENT`: Q01 CALL / Q13 SKIP
- `TRANSLATION`: Q02 SKIP / Q12 CALL
- `RESTART`: Q03 SKIP / Q18 CALL
- `DIAGNOSIS`: Q04 CALL / Q21 SKIP
- `DELETE`: Q05 SKIP / Q16 CALL
- `TOOL_CHANGE`: Q06 CALL / Q15 SKIP
- `RESTORE`: Q07 SKIP / Q14 CALL
- `PAYMENT`: Q08 CALL / Q19 SKIP
- `MIGRATION`: Q09 SKIP / Q20 CALL
- `OBSERVATION`: Q10 CALL / Q17 SKIP
- `ALERT_THRESHOLD`: Q11 SKIP / Q22 CALL
- `RUNBOOK`: Q23 CALL / Q24 SKIP

## Interpretation boundary

This is materially stronger than run-001 because the task set deliberately holds topical vocabulary similar while changing consequence, continuity, current-authoritative completeness, project-history dependence, or isolation.

It supports the hypothesis that a compact generic R0 instruction can discriminate retrieval need from decision shape rather than relying on a topic-specific hot cue catalog, at least for this controlled model/session phenotype.

It does NOT establish:

- universal model/framework portability;
- correct query-scope selection after CALL;
- resolver recall;
- registry/index freshness;
- projection completeness;
- behavioral application after retrieval;
- production field performance.

## Stop decision for trigger-only fixture family

Do not add a third same-kind trigger-classification fixture merely for sample count. Two controlled rounds now show the intended mechanism, including OOD counterfactual minimal pairs. Further same-family cases are unlikely to change the architecture unless a new trigger failure class is hypothesized.

Next falsification target:

> `CALL correctly fired -> wrong query scope selected`

This is `QUERY_SCOPE_MISS`, already separated in the retrieval evaluation plane. The next experiment should isolate routing/scope selection from R0 trigger detection and from low-level search/index recall.
