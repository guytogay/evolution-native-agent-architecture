# Independent Oracle Review Protocol — Tiny Hot Kernel

Status: `RESEARCH_REVIEW_PROTOCOL / NOT_CURRENT`

Purpose:

Before using the 36-case oracle to select among K-A/K-B/K-C, independently review whether the oracle itself encodes defensible ENA expectations rather than the benchmark author's preferences.

## Reviewer independence

Prefer a reviewer that did not author:

- K-A/K-B/K-C;
- `semantic-router.v0.1.json`;
- `tiny-kernel-cases.jsonl`;
- the scorer.

The reviewer may use canonical ENA v0.3.6 Current and the full fixture oracle, but should **not** use model/kernel performance results while judging the oracle. Otherwise outcome knowledge can bias the expected labels.

## Inputs

- canonical v0.3.6 Current at tree `7dcbb3934883ffa6cc5292a662588cafc1533cff`;
- `fixtures/tiny-kernel-cases.jsonl`;
- `semantic-router.v0.1.json` only to review family/route reachability;
- `fixtures/ORACLE-STATUS.md`;
- this protocol.

Kernel candidate prose is optional and preferably withheld in the first oracle pass.

## Review each case independently

For every case, classify:

```text
TRIGGER_EXPECTATION:
  AGREE | DISAGREE | AMBIGUOUS

PRIMARY_FAMILY_EXPECTATION:
  AGREE | DISAGREE | AMBIGUOUS | NOT_APPLICABLE

ALLOWED_FAMILY_ENVELOPE:
  TOO_NARROW | REASONABLE | TOO_BROAD | AMBIGUOUS | NOT_APPLICABLE
```

Then record:

```text
case_id
reviewed_expected_trigger
reviewed_primary_families
reviewed_allowed_families
material_decision_shape
Current semantic basis
false-OK risk if expectation is too permissive
false-BLOCK/governance-cost risk if expectation is too strict
confidence: HIGH | MEDIUM | LOW
notes
```

Do not force binary certainty when the Current semantics intentionally leave a Host/local consequence boundary open.

## Key reviewer questions

1. Does this task actually require an ENA cold lookup, or could the resident substrate safely handle it without retrieval?
2. Is `trigger=true` being used as a synonym for `the task mentions an ENA concept`?
3. Is `trigger=false` being used merely because the action looks familiar or low effort?
4. Does the expected family set identify decision-material semantics, or just everything loosely related?
5. Would the allowed-family envelope punish a legitimate alternate route?
6. Could a broad family union hide router overreach/context inflation?
7. Does the oracle accidentally require governance on a reversible/local/explicitly authorized low-consequence action?
8. Does the oracle fail to interrupt an authority, settlement, recovery, applicability, or irreversible-effect boundary that can materially change the decision?
9. Is the case testing the resident recognizer, the router, or a downstream R4/R5 behavior that the current scorer cannot actually judge?
10. Is there a legitimate `AMBIGUOUS / HOST_DEPENDENT` answer that should be represented rather than collapsed into author preference?

## Special attention cases

Review at least these with explicit reasoning:

- `TK-026` — storing a latent idea without applying it;
- `TK-029` — harmless local fast-forward / authority-anxiety control;
- `TK-031` — explicit low-consequence external GitHub comment;
- `TK-034` — broken resolver on a task expected to remain quiet;
- multi-family cases where family-envelope breadth can dominate score.

This list identifies likely boundary pressure; it is not an instruction to overturn them.

## Reconciliation outcomes

For each disputed case choose one:

### A. Keep oracle expectation

Reviewer challenge does not survive Current semantics/decision consequence analysis.

### B. Revise oracle expectation

A real author-oracle error is found. Preserve the old fixture version/history and record the reason.

### C. Mark case non-scoring / diagnostic

The case is useful but Current intentionally permits multiple locally valid trigger/routing outcomes. Do not force a false universal label.

### D. Split the case

One prompt accidentally mixes two variables; create paired cases that isolate the distinction.

## Benchmark admission rule

Only after oracle reconciliation may a run be used for comparative kernel selection.

Even then:

```text
oracle-reviewed controlled score
!= naturalistic salience
!= universal Host fitness
!= Current release evidence by itself
```

## Reviewer output

Produce a durable review artifact with:

- exact Current identity;
- exact oracle content identity / research head;
- independence statement;
- per-case disposition;
- aggregate counts;
- unresolved ambiguities;
- whether the oracle is fit for `CONTROLLED_COMPARATIVE_SELECTION`, `EXPLORATORY_ONLY`, or `NEEDS_REVISION`.

Do not optimize the oracle to make any existing kernel win.

> The benchmark is also a variation. Reality is allowed to reject its author.
