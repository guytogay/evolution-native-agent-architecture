# Circular Provenance Path Experiment

Status: `EXPERIMENT_PLAN / ISSUE-14 / NOT_PROMOTED`

Experiment ID: `ENA-EXP-NET-001`

## Question

Can an ENA participant mistakenly treat repeated propagation of one originating claim as independent evidence or multiplied authority?

## Synthetic fixture

1. Actor A originates claim `C1` with evidence `E1`.
2. Actor B receives `C1` from A, summarizes it, and reports `C1` to C.
3. Actor C receives B's summary and reports agreement back to A.
4. A now sees apparent support from B and C.
5. No actor has obtained evidence independent of `E1`.

Variants:

- V1: B and C clearly preserve provenance to A/E1.
- V2: B preserves provenance, C drops one hop of provenance.
- V3: all text is paraphrased so wording differs but source lineage is the same.
- V4: B adds a real independent observation `E2` while C remains derivative.
- V5: replace claim propagation with delegation/approval propagation rather than epistemic evidence.

## Competing treatments

### T0 — Count endorsements
Treat B and C as additional support because multiple actors repeat/agree.

### T1 — Source-deduplicated support
Collapse derivative endorsements back to originating evidence/source lineage.

### T2 — Explicit provenance-path check
Represent a support/delegation path and reject circular return as independent support or authority multiplication.

## Measurements

- false independent-support claim produced: YES/NO;
- decision changed by derivative repetition: YES/NO;
- legitimate independent support preserved in V4: YES/NO;
- implementation/governance overhead;
- whether existing Claim↔Evidence semantics already reject the problem without new machinery;
- whether path representation catches delegation/authority loops that ordinary evidence dedup does not.

## Success / falsification

A new ENA mechanism is **not** justified merely because T2 looks elegant.

Promising result:

- Current treatment permits a materially false independence/authority claim;
- a provenance-path check prevents it;
- the same property recurs in more than one domain (evidence, delegation, approval, contribution, etc.).

Null result:

- existing evidence-source/provenance semantics already reject all material cases;
- path tracking adds cost without changing a decision.

## Candidate property if supported

> Propagation does not create independence. A support or authority chain that returns to its own origin must not gain weight merely by traversing additional actors.

Do not promote this wording from the experiment alone.