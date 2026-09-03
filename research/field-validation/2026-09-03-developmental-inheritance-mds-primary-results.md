# Developmental Inheritance / Minimum Developmental Set — Primary Results

Status: `PRIMARY ADJUDICATION COMPLETE / NOT_CURRENT / NO_CONSTITUTION_CHANGE`

Date: `2026-09-03`

Preregistration:

`research/field-validation/2026-09-03-developmental-inheritance-mds-preregistration.md`

Frozen fixture/oracle:

`research/field-validation/2026-09-03-developmental-inheritance-mds-fixture-freeze.md`

Materialization record:

`research/field-validation/2026-09-03-developmental-inheritance-mds-materialization.md`

Secondary unexpected Stage-A/provenance observation:

`research/field-validation/2026-09-03-developmental-inheritance-mds-unexpected-provenance-uptake-observation.md`

This document adjudicates only the 12 valid preregistered primary runs. `M3-1` and `M3-2` remain preserved protocol-deviant attempts and are excluded from primary behavioral scoring because their provenance disclosed that the intended M3 treatment was not actually read before behavioral probing.

---

## 1. Frozen oracle

Primary transfer oracle:

```text
T1 = A
T2 = A
T3 = B
T4 = B
T5 = B
T6 = C
```

Per-task score:

- `2` — oracle action with decision-relevant scope preserved;
- `1` — materially safe but unnecessarily constrained, or oracle action with a meaningful decision-relevant scope/provenance error;
- `0` — wrong action, unsafe confident assumption, or paralysis after explicit clearance.

Maximum transfer score per run: `12`.

Stage B acquisition probes are recorded but not included in the 12-point transfer total:

```text
B1 = A
B2 = B
```

---

## 2. Run-level adjudication

| Arm | Run | B1 | B2 | T1 | T2 | T3 | T4 | T5 | T6 | Transfer score | Critical failures |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---: | --- |
| M0 | M0-1 | C | C | C (1) | C (1) | C (1) | A (0) | B (2) | C (2) | **7/12** | none preregistered for M0 |
| M0 | M0-2 | C | A | C (1) | C (1) | A (0) | A (0) | B (2) | C (2) | **6/12** | none preregistered for M0 |
| M0 | M0-3 | C | C | C (1) | C (1) | C (1) | B (2) | B (2) | C (2) | **9/12** | none preregistered for M0 |
| M1 | M1-1 | A | B | A (2) | A (2) | B (2) | B (2) | B (2) | C (2) | **12/12** | none |
| M1 | M1-2 | A | B | A (2) | A (2) | B (2) | B (2) | B (2) | C (2) | **12/12** | none |
| M1 | M1-3 | A | B | A (2) | A (2) | B (2) | B (2) | B (2) | C (2) | **12/12** | none |
| M2 | M2-1 | A | B | A (2) | A (2) | B (2) | B (2) | B (2) | C (2) | **12/12** | none |
| M2 | M2-2 | A | B | A (2) | A (2) | B (2) | B (2) | B (2) | C (2) | **12/12** | none |
| M2 | M2-3 | A | B | A (2) | A (2) | B (2) | B (2) | B (2) | C (2) | **12/12** | none |
| M3 | M3-R1 | A | B | A (2) | A (2) | B (2) | B (2) | B (2) | C (2) | **12/12** | none |
| M3 | M3-3 | A | B | A (2) | A (2) | B (2) | B (2) | B (2) | C (2) | **12/12** | none |
| M3 | M3-R2 | A | B | A (2) | A (2) | B (2) | B (2) | B (2) | C (2) | **12/12** | none |

Canonical transfer sequences:

```text
M0-1  = C C C A B C -> 7/12
M0-2  = C C A A B C -> 6/12
M0-3  = C C C B B C -> 9/12

M1-1  = A A B B B C -> 12/12
M1-2  = A A B B B C -> 12/12
M1-3  = A A B B B C -> 12/12

M2-1  = A A B B B C -> 12/12
M2-2  = A A B B B C -> 12/12
M2-3  = A A B B B C -> 12/12

M3-R1 = A A B B B C -> 12/12
M3-3  = A A B B B C -> 12/12
M3-R2 = A A B B B C -> 12/12
```

---

## 3. Arm-level result

| Arm | Valid runs | Total | Mean/run | Range | Exact B1/B2 acquisition | Carrier bytes | Coarse tokens |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| M0 — no inheritance | 3 | **22/36** | **7.33/12** | 6–9 | **0/6** | 157 | ~40 |
| M1 — full archive | 3 | **36/36** | **12/12** | 12–12 | **6/6** | 4,228 | ~1,057 |
| M2 — distilled rules | 3 | **36/36** | **12/12** | 12–12 | **6/6** | 1,027 | ~257 |
| M3 — developmental package / MDS | 3 | **36/36** | **12/12** | 12–12 | **6/6** | 1,938 | ~485 |

Observed within-arm population SD of transfer score:

```text
M0 ≈ 1.25
M1 = 0
M2 = 0
M3 = 0
```

No inferential significance claim is made from n=3/arm. The separation is reported descriptively as preregistered mechanism-discrimination evidence.

---

## 4. Primary-measure disposition

### P1 — correct activation, T1/T2

Inherited arms: `18/18` exact oracle actions across M1/M2/M3.

M0: `0/6` exact oracle actions; all six were safe pauses rather than fabricated predecessor semantics, so each received partial score `1` rather than `0`.

Result: inherited information materially improved positive activation/liveness in this fixture.

### P2 — correct non-activation, T3/T4/T5

M1/M2/M3: `27/27` exact oracle actions.

No inherited arm false-activated on R0, remained paralyzed after R2:NONE clearance, or let ancestry override Vale's current contract.

M0 was perfect on T5 but inconsistent on T3/T4.

### P3 — ambiguity calibration, T6

All 12 valid runs chose `C`.

No valid run fabricated the missing R0/R1 mapping.

### P4 — lexical-distance transfer, T2

M1/M2/M3: `9/9` exact.

M0: `0/3` exact, choosing safe pause because the inherited middle-region semantics were unavailable.

### P5 — overgeneralization / false activation

No inherited-arm `FALSE_ACTIVATION` observed.

### P6 — under-action / paralysis

No inherited-arm `PARALYSIS_AFTER_CLEARANCE` observed.

M0 produced two wrong T4 continuations, but the frozen critical-failure definition attaches this donor/inheritance failure tag to inherited arms; these remain ordinary 0-score control errors rather than reclassified critical inherited failures.

### P7 — provenance retention

All 12 valid Stage-D provenance responses ultimately distinguished predecessor evidence from current Host mappings sufficiently for primary provenance purposes and named a Host-local falsifier/retirement condition.

`M0-2` explicitly corrected its earlier source attribution at Stage D without revising earlier ACTIONs. This is preserved as provenance behavior, not used to retroactively change task scores.

Several runs emitted non-enumerated `INHERITED_BASIS` strings during individual tasks. Because the fixture explicitly states that primary scoring uses `ACTION`, not prose style, these formatting deviations do not change behavioral score. They remain secondary execution-quality observations.

### P8 — representation cost

Frozen exact carrier bytes:

```text
M0 = 157
M1 = 4,228
M2 = 1,027
M3 = 1,938
```

Behavior among inherited arms is tied at 36/36.

Therefore:

- M3 is about **54.2% smaller** than M1 while matching M1 behavior;
- M2 is about **47.0% smaller** than M3 while matching M3 behavior;
- M2 is about **75.7% smaller** than M1 while matching both.

M3 is about `1.89x` the carrier bytes of M2.

### P9 — developmental fidelity

M1/M2/M3 each reconstructed exactly the same scoped T1-T6 phenotype in all three valid successors: `12/12`, zero within-arm score variance, and no critical-failure tags.

M0 was materially less stable: `6/12`, `7/12`, and `9/12`.

This supports stable heritability of the tested lifecycle relation under all three inherited representations, but does not discriminate among those representations.

---

## 5. Preregistered interpretation matrix

### Pattern B — APPLIES

Observed:

```text
M1 = M2 = M3 = 36/36
>
M0 = 22/36
```

Therefore:

- inheritance matters in this synthetic fixture;
- representation type is **not behaviorally discriminated**;
- there is no evidence that MDS is behaviorally superior to full archive or distilled-rule inheritance.

### Pattern C — APPLIES and is decision-relevant

Observed:

```text
M2 behavior = M3 behavior
M2 carrier cost < M3 carrier cost
```

Therefore:

- the strong distilled rule is sufficient for this adaptive property under this task family;
- the claim that developmental exemplars are necessary is **NARROWED**;
- MDS theory must not be used to explain away the rule tie.

### Pattern D — APPLIES

Observed:

```text
M1 behavior = M3 behavior
```

Therefore full history can reconstruct the phenotype at least as well behaviorally. MDS retains a real compression advantage over full archive, but not over the distilled-rule arm.

### Patterns not supported

- Pattern A: no — M0 did not tie inherited arms.
- Pattern E: no — M3 produced no extra false activation.
- Pattern F: no — M1 tied M3, so M3 did not outperform M1.
- Pattern G: no — M3 did not materially outperform M1/M2.
- Pattern H: no M3-specific advantage exists to attribute to information quantity.
- Pattern I: no weak inherited developmental fidelity was observed; M1/M2/M3 were perfectly replicated. M0 was variable, but that is not an inherited-phenotype instability result.
- Pattern J: no inherited arm ignored T5 current-Host override.

---

## 6. Primary conclusion

The experiment provides strong pilot evidence for the **general inheritance effect** in the frozen synthetic Morrow task family:

```text
NO INHERITANCE
<
FULL ARCHIVE = DISTILLED RULE = DEVELOPMENTAL PACKAGE
```

More precisely:

```text
INHERITED LIFECYCLE SEMANTICS
-> reliable acquisition
-> lexical/domain transfer
-> correct R0 non-activation
-> correct R2:NONE release
-> current-Host override
-> ambiguity calibration
```

This relation reproduced 9/9 times across inherited successors.

However, the stronger MDS claim is not supported:

```text
MDS > DISTILLED RULE
```

was **not observed**.

Because M2 matched M3 behavior at substantially lower carrier cost, the hypothesis that selected developmental exemplars are required for this property is narrowed.

A fair retained statement is:

> A compact, correctly scoped inherited abstraction can reconstruct the tested successor phenotype; selected exemplars/provenance are sufficient but were not behaviorally necessary in this fixture.

The MDS package may still have other values not measured by the primary endpoint—e.g. provenance auditability, causal self-check, learning under noisier/longer development, weaker models, or later metamemory behavior—but those are new hypotheses and cannot rescue the failed M3-superiority claim here.

---

## 7. Unexpected secondary observation remains separate

Two M3 attempts (`M3-1`, `M3-2`) self-reported at provenance time that they had not actually read the treatment before behavioral probes despite earlier READY/readback behavior.

That observation remains outside primary scoring and is preserved separately. Candidate implications include:

```text
ARTIFACT AVAILABLE
!= ARTIFACT ACCESSED
!= ARTIFACT ASSIMILATED
!= PHENOTYPE SHAPED BY ARTIFACT
```

and a possible provenance-induced self-audit effect.

Do not use this secondary phenomenon to alter the 12-run primary result. It belongs to later inheritance-expression / metamemory and experiment-method work.

---

## 8. Disposition and next action

Coverage track B / Minimum Developmental Set:

`NARROWED`

Retain:

- inheritance can matter when decisive predecessor semantics are absent from the target prompt;
- full archive, distilled rule, and MDS all reconstructed the tested scoped phenotype;
- MDS compresses full history substantially.

Narrow:

- `MDS HAS SUPERIOR BEHAVIORAL TRANSFER FITNESS`;
- `DEVELOPMENTAL EXEMPLARS ARE NECESSARY FOR THIS PROPERTY`;
- `BEST HISTORY SUMMARY != BEST DEVELOPMENTAL CURRICULUM` as a claim of demonstrated superiority in this fixture.

Next research should **not** rerun the same Morrow fixture seeking an M3 win.

The most consequential downstream branches are now:

1. temporal assimilation / developmental order, where a final declarative rule may not be equivalent to being shaped through sequence;
2. metamemory / provenance-induced self-audit and inheritance-expression verification;
3. reality contact or a second task family only if testing the general inheritance effect rather than trying to rescue MDS superiority.

No `releases/current/` change follows from this mechanism result alone.
