# Provenance defects and record identity: three mechanism lessons from live runs

Status: `RESEARCH / NOT_PROMOTED`. Source: the current line's field runs, not the retired line. Written
2026-09-14 while triaging the field node's reports to the product issues; the product-side evidence
lives in those issues, and this note is the part that generalises past them.

Nothing here proposes a change to Current. Two of the three lessons sharpen where a *measurement* is
invalid; the third is a mechanism trap that would silently corrupt any id-based reasoning.

## 1. A score that was never promoted to a pre-registered rubric is not a score

The field node's earlier salience observation (`Runtime Kernel Salience Observation`, three arms by two
tasks) produced a headline of **0/10 margin**. Its own reconciliation records why that number was never
promoted to a pre-registered score:

```text
rubric pairs treat - control, the results table used treat - neutral
control-T1 read the treat kernel during its own run
the T2 checkpoint was remapped
```

The narrow conclusion that was accepted instead is: *the probe could not distinguish kernel residency.*

**Lesson.** `ran to completion != measured what the rubric defined`. A pair computed against a
different arm than the rubric names is a different quantity, and a contaminated control is not a
control. When a number is produced but not promoted, the promotion decision is part of the evidence
trail; without it, a later reader inherits the number and not the reason it was set aside.

## 2. An archive that stores outputs cannot recompute a score

The same observation's archive held the outputs but not the raw records that carry the machine
evidence for `WRITTEN=0/2`; those two session records existed in only one place on that host. So a
later reader could read the conclusion but not re-derive it — and the archive's apparent coverage was
higher than its recomputability.

A related shape appeared on the same host in a different subsystem: a collection source had been
declared as an input and **never produced a single record** in over a hundred pooled items, while the
collector's own comment described it as a live source. That inflates how wide the recipe looks without
changing what was actually eaten.

**Lesson.** Coverage claims need two numbers, not one: what was stored, and what can be recomputed
from what was stored. A declared-but-never-yielding input is worse than a missing one, because it is
counted.

## 3. Record identity is derived from paths, so it is not content identity

A control run nearly produced a false positive: the material digest changed and one sampled fragment
changed, which looked like support for a candidate. Re-checking showed the *content* set was
identical; the digest moved because the source tree had been copied to a temporary path. Record ids on
that host derive from paths, so the same bytes at a different path are a different record.

**Lesson, and the one with the widest reach.** Any mechanism that diffs, dedupes, ranks or derives
provenance **by record id** inherits that trap. The observable symptoms are specific and misleading:

```text
"the material changed"        may mean "the material moved"
"this record is new"          may mean "this record was copied"
"two records disagree"        may mean "two paths, one content"
```

The cheap guard is to compare content digests wherever identity is used for a decision, and to keep
the path-derived id as a locator rather than a key. A second guard is to state, in any tool whose
output feeds a comparison, which of the two it is reporting.

## Evidence boundary

The observations are from one host, reported by the field side and, for the sampling-related parts,
independently reproduced by the execution side on synthetic material (the reproduction is recorded in
the product issues, including the case where the first attempt could not have shown the effect and the
precondition that made it visible). The generalisations above are mine; the readings are not, and the
attribution is kept explicit because "who observed it" was itself a defect in an earlier round of this
project.

## Why this belongs here rather than in the product

None of the three is a product defect. The product's tools behaved as documented; what went wrong was
in how a *measurement* was promoted, stored and keyed. That is a property of the evidence discipline
around the mechanism, which is what this repository keeps.
