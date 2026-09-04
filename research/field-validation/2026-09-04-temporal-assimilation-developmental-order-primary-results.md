# Temporal Assimilation / Developmental Order v1 — Primary Results

Date: `2026-09-04`

Status: `PRIMARY_ADJUDICATION_COMPLETE / NOT_CURRENT / MECHANISM_DISCRIMINATION`

Current baseline remains: `v0.3.7 / CURRENT / FIELD_VALIDATION`.

This result does **not** modify `releases/current/` and does not establish a new ENA natural law.

## 1. Frozen authorities

Scoring and adjudication were performed only against the already-frozen experimental surfaces and preserved first outputs:

- preregistration: `research/field-validation/2026-09-04-temporal-assimilation-developmental-order-preregistration.md`;
- fixture: `research/field-validation/fixtures/temporal-assimilation-order-v1/FIXTURE.md`;
- primary evidence: `research/field-validation/temporal-assimilation-order-v1/runs/`.

No valid primary run was rerun, replaced, extended, or supplemented to seek a preferred result.

Valid primary runs:

```text
CF:  CF-R1, CF-2, CF-3
MF:  MF-1, MF-2, MF-3
INT: INT-1, INT-2, INT-R1
```

Excluded attempts remain excluded and are not primary-scored:

```text
CF-1  — session continuity was rebuilt before B1
INT-3 — Temporary Chat closed after A2
```

`CF-R1` and `INT-R1` are their valid replacements.

`CF-3` remains a valid experimental run. Its GitHub persistence/backfill anomaly is an evidence-archival issue, not a subject-protocol failure; `CF-3.status.md` and the preserved stage artifacts carry the completion provenance.

## 2. Formal M1-M3 scoring

| Run | Arm | M1 final rule | M2 pre-correction | M3 post-correction | A7 rule family |
|---|---|---:|---:|---:|---|
| CF-R1 | CF | FAIL | 5/11 | 9/9 | Beryl/Dune alias |
| CF-2 | CF | PASS | 11/11 | 9/9 | preregistered Coda/Dune rule |
| CF-3 | CF | FAIL | 5/11 | 9/9 | Beryl/Dune alias |
| MF-1 | MF | PASS | 11/11 | 9/9 | preregistered Coda/Dune rule |
| MF-2 | MF | FAIL | 5/11 | 9/9 | Beryl/Dune alias |
| MF-3 | MF | PASS | 11/11 | 9/9 | preregistered Coda/Dune rule |
| INT-1 | INT | PASS | 11/11 | 9/9 | preregistered Coda/Dune rule |
| INT-2 | INT | FAIL | 5/11 | 9/9 | Beryl/Dune alias |
| INT-R1 | INT | PASS | 11/11 | 9/9 | preregistered Coda/Dune rule |

Totals:

```text
M1: 5/9 PASS
M2: 75/99 correct
M3: 81/81 correct
```

Arm summaries:

| Arm | M1 | M2 | M3 |
|---|---:|---:|---:|
| CF | 1/3 | 21/33 | 27/27 |
| MF | 2/3 | 27/33 | 27/27 |
| INT | 2/3 | 27/33 | 27/27 |

The preregistered misleading-first arm did **not** underperform CF/INT. CF is descriptively lower pre-correction because two of its three runs selected the alternative rule; MF and INT each contain one such run. INT did not consistently outperform both clustered orders.

After the identical authoritative correction, every valid run scored `9/9`.

## 3. M4 — developmental-debt error signatures

The four M1-failing runs (`CF-R1`, `CF-3`, `MF-2`, `INT-2`) produced the same six B1 action failures and the same effective alternative rule:

```text
ZED iff Beryl=OFF AND Dune=OFF.
```

Equivalently:

```text
NOVA if Beryl=ON or Dune=ON; otherwise ZED.
```

Per affected run, preregistered M4 tags are:

```text
ASTER_FALSE_ACTIVATION:          2
BERYL_FALSE_SUPPRESSION:         3
CAUSAL_MISS:                     3
DUNE_OVERRIDE_MISSED:            0
OVERCONFIDENT_UNDERDETERMINATION: 0
untagged exact-action failures:  1
```

Tags overlap on some failed items, so tag incidence is not the same as error count.

Across all four affected runs:

```text
ASTER_FALSE_ACTIVATION:           8
BERYL_FALSE_SUPPRESSION:         12
CAUSAL_MISS:                     12
DUNE_OVERRIDE_MISSED:             0
OVERCONFIDENT_UNDERDETERMINATION: 0
untagged exact-action failures:   4
```

The `ASTER_FALSE_ACTIVATION` label is applied mechanically according to the frozen tag definition; it should not be misread as evidence that these four A7 rules actually depended on Aster. Their preserved A7 rules depended on Beryl and Dune.

Post-correction M4 failures: `0` across all nine runs.

All nine pre-correction uncertainty items (`U1`) and all nine post-correction uncertainty items (`C9`) were correctly answered `INSUFFICIENT`.

## 4. M5 — acquisition trajectory

First stage at which the exact preregistered rule appears in the preserved working rule/final rule:

| Run | First exact rule |
|---|---|
| CF-R1 | never |
| CF-2 | A7 |
| CF-3 | never |
| MF-1 | A6 |
| MF-2 | never |
| MF-3 | A6 |
| INT-1 | A7 |
| INT-2 | never |
| INT-R1 | A6 |

The intended misleading-first developmental-debt chain is not observed coherently.

In particular:

- `MF-1` initially entertained Aster/Coda-dependent hypotheses, then dropped the unnecessary Aster requirement and reached the exact rule at A6;
- `MF-2` moved away from its early Aster-only shortcut; its final failure was the later Beryl/Dune alias, not persistence of the falsified Aster shortcut;
- `MF-3` also dropped its early Aster/Coda requirement and reached the exact rule at A6;
- `INT-1` and `INT-R1` dropped early Aster-linked hypotheses after counterevidence and later reached the exact rule;
- `INT-2`, `CF-R1`, and `CF-3` selected the Beryl/Dune alias, but that alias was not falsified by the six acquisition episodes.

Therefore the preregistered stronger chain

```text
early shortcut
-> authoritative falsification
-> shortcut persists after falsification
-> matching later transfer failures
-> repeats within the same arm
```

is **not present**.

## 5. M6 — calibration

Confidence was generally very high and did not separate correct from incorrect pre-correction actions in a coherent arm-level way.

Pooled across B1 item responses:

```text
mean confidence on correct actions:   98.49
mean confidence on incorrect actions: 97.00
```

Mean B1 confidence by arm:

```text
CF:  99.70
MF:  96.52
INT: 98.18
```

These descriptive differences do not align coherently with arm accuracy and are not large enough, under the preregistered secondary role of M6, to support a calibration mechanism claim. Post-correction actions were all correct and were reported at confidence 100.

## 6. Critical fixture-identifiability finding

Formal scores above remain valid under the frozen oracle. However, adjudication revealed an important limitation of the acquisition fixture.

The intended hidden rule is:

```text
R1: ZED iff Coda=ON AND Dune=OFF.
```

The alternative independently selected by four valid runs is:

```text
R2: ZED iff Beryl=OFF AND Dune=OFF.
```

Both `R1` and `R2` classify **all six acquisition episodes correctly**.

For every acquisition episode with `Dune=OFF` (`E1-E4`), `Coda=ON` and `Beryl=OFF` are perfectly aligned. For `E5-E6`, `Dune=ON` forces NOVA under both rules. The six labeled acquisition episodes therefore do not distinguish `R1` from `R2`.

A further rule such as a Coda/Dune XOR relation is also observationally compatible with the six acquisition cases because the acquisition set contains no `Coda=OFF, Dune=ON` discriminator.

Consequences:

1. M1 remains a strict reconstruction score against the preregistered hidden oracle; the four alias runs therefore remain M1 FAIL.
2. M2 remains an exact transfer score; the four alias runs therefore remain `5/11`.
3. The alias runs' B1 failures are coherent execution of an acquisition-consistent hypothesis, **not** persistence of a hypothesis that the authoritative acquisition evidence had already falsified.
4. The fixture therefore cannot cleanly support a claim of residual developmental debt through failed reconsolidation from those alias errors alone.
5. This is a fixture-identifiability limitation, not a reason to invalidate, rerun, or replace any primary run after seeing the result.

The B1 transfer battery successfully distinguishes the hypotheses, but it occurs only after A7 has frozen the model's learned rule. The later explicit correction then removes the ambiguity for every run.

## 7. Cross-arm adjudication against the preregistered matrix

### Pattern A — all arms converge before and after correction

**Not observed.** Pre-correction runs do not all converge. Post-correction convergence is complete.

### Pattern B — pre-correction arm differences, post-correction convergence

A **surface B-like shape** exists at the aggregate level: CF scores lower than MF/INT pre-correction, and all arms converge after correction.

However, the direction is not the preregistered misleading-first debt pattern, every arm contains both exact-rule and alias outcomes, and the alias is acquisition-consistent. Therefore the data do not justify the stronger Pattern-B statement that acquisition order produced a stable arm-level developmental schema difference.

### Pattern C — MF remains worse after identical correction

**Not observed.** MF is not worse pre-correction and every arm is perfect after correction.

### Pattern D — MF worse before correction but catches up after correction

**Not observed.** MF is not the underperforming arm.

### Pattern E — INT consistently outperforms both clustered orders

**Not observed.** INT ties MF and contains an alias run.

### Pattern F — direct items tie while lexical transfer differs

**Not observed.** Alias-rule failures affect both direct and lexical items.

### Pattern G — accuracy ties but calibration differs coherently

**Not observed.** Accuracy does not tie pre-correction, and confidence differences are not coherent enough to carry the result.

### Pattern H — high within-arm variance or inconsistent direction

**Observed; best preregistered fit.** Every arm contains both exact-rule and alias-rule outcomes, while no preregistered arm-level direction repeats consistently enough to support a developmental-order mechanism claim.

### Pattern I — immediate position/recency explains the differences

**Not established.** The present data do not isolate a specific recency/position mechanism. Generic unstable in-context hypothesis selection under an underidentified evidence set is a sufficient, weaker explanation and should be preferred over an ENA developmental-law claim.

## 8. Primary disposition

### Supported observation

Within this Host/task family, fresh sessions that ultimately received the same six externally supplied labeled episodes did not always reconstruct the same hidden rule before explicit correction.

That observation alone is **not** evidence of ENA developmental assimilation, because:

- the phenotype is not stable by arm;
- the preregistered misleading-first debt direction is absent;
- the four failing runs span all three arms;
- their common alternative rule is not falsified by the acquisition evidence;
- within-arm variance is high;
- all post-correction behavior converges immediately and completely.

### Not observed / narrowed

The following stronger claims are **not observed in this fixture and are narrowed**:

- `MISLEADING-FIRST ORDER CREATES PERSISTENT DEVELOPMENTAL DEBT`;
- `INTERLEAVING PROVIDES A STABLE TRANSFER ADVANTAGE`;
- `SAME FINAL EXTERNAL EVIDENCE + DIFFERENT ORDER PRODUCES A STABLE ARM-SPECIFIC PHENOTYPE`;
- `EXPLICIT CORRECTION FAILS TO RECONSOLIDATE THE TESTED PHENOTYPE`;
- `CORRECTION != RECONSOLIDATION` as a demonstrated relation in this experiment.

For the tested phenotype, the identical explicit correction was sufficient to produce `81/81` correct post-correction actions.

### Strongest allowed interpretation

The data support, at most:

> The frozen task exhibits variable pre-correction in-context hypothesis selection under an underidentified acquisition set, followed by complete behavioral convergence after an identical explicit correction.

They do **not** support a stronger ENA developmental assimilation law or persistent within-session developmental debt.

## 9. Research implications

Do **not** rerun or augment this primary fixture merely to seek a cleaner order effect.

If Temporal Assimilation / Developmental Order is revisited later, use a newly preregistered task family whose acquisition evidence uniquely discriminates the intended causal rule from plausible aliases before A7. That is a new experiment, not a repair of these frozen primary data.

Cross-Host or durable cross-session assimilation also remains outside this experiment's scope.

The current research program can proceed to the next Coverage Map mechanism rather than extending this same fixture for a preferred result.

## 10. Current / release implication

None directly.

```text
INTERESTING RESULT != NEW NATURAL LAW != CURRENT CHANGE
```

`v0.3.7 / CURRENT / FIELD_VALIDATION` remains the adoption baseline and `releases/current/` remains unchanged.
