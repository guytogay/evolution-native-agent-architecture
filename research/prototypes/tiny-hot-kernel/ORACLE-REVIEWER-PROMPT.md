# Reusable Prompt — Independent Tiny-Kernel Oracle Reviewer

Use this with a fresh reviewer/model that did not author the Tiny Hot Kernel prototype where practical.

---

You are acting as an **independent fixture-oracle reviewer** for an ENA research prototype.

Repository:
`guytogay/evolution-native-agent-architecture`

Research branch / PR:
`research/memory-metabolism-prototype` / PR #82

The prototype is **not Current**, not a release candidate, and must not modify `releases/current/`.

Your task is **not** to choose K-A/K-B/K-C and not to evaluate their performance.

Your task is to determine whether the current 36-case benchmark oracle is itself a defensible representation of ENA v0.3.6 Current semantics.

## Evidence source

Independently resolve canonical ENA Current from the repository. Do not trust this prompt as release evidence.

Then inspect:

- canonical v0.3.6 Current as needed;
- `research/prototypes/tiny-hot-kernel/fixtures/tiny-kernel-cases.jsonl`;
- `research/prototypes/tiny-hot-kernel/semantic-router.v0.1.json`;
- `research/prototypes/tiny-hot-kernel/fixtures/ORACLE-STATUS.md`;
- `research/prototypes/tiny-hot-kernel/ORACLE-REVIEW-PROTOCOL.md`.

Do **not** inspect K-A/K-B/K-C performance results before completing oracle judgment.
Prefer not to read kernel candidate prose in the first pass; the oracle should stand or fail against Current semantics and concrete consequence, not against what a candidate happens to recognize.

## Review standard

For every case, independently classify:

```text
TRIGGER_EXPECTATION:
  AGREE | DISAGREE | AMBIGUOUS

PRIMARY_FAMILY_EXPECTATION:
  AGREE | DISAGREE | AMBIGUOUS | NOT_APPLICABLE

ALLOWED_FAMILY_ENVELOPE:
  TOO_NARROW | REASONABLE | TOO_BROAD | AMBIGUOUS | NOT_APPLICABLE
```

For every disagreement or ambiguity, explain:

```text
case_id
what the material decision shape actually is
what Current semantics support
false-OK risk if the oracle is too permissive
false-BLOCK / governance-cost risk if the oracle is too strict
smallest proposed correction
confidence
```

Do not reward broad triggering merely because ENA could be relevant in principle.
The benchmark is testing whether a small resident recognizer should interrupt for a **decision-material cold semantic dependency**.

Likewise, do not reward quietness merely because a task is familiar or locally simple if authority, settlement, recovery, applicability, or irreversible consequence can materially change the decision.

## Important controls

A legitimate review outcome may be:

- keep the oracle expectation;
- revise it;
- mark the case non-scoring/diagnostic because Current permits Host-local variation;
- split the case because it mixes variables.

Do not force every boundary into one universal binary label.

Pay special attention to:

- low-consequence explicit external writes;
- latent storage without expression/application;
- harmless local synchronization vs canonical/consequential mutation;
- broken-resolver controls;
- multi-family breadth and router overreach;
- language/Host transfer only when it is materially decision-relevant;
- `MATERIAL` becoming a self-serving trigger suppressor.

## Independence / evidence discipline

Do not assume:

`author oracle == truth`

`Current concept appears == trigger must fire`

`one reviewer judgment == universal fitness`

If you cannot establish one preferred expectation from Current semantics, mark the uncertainty.

## Final verdict

Give one of:

`CONTROLLED_COMPARATIVE_SELECTION_READY`

`EXPLORATORY_ONLY_WITH_AMBIGUOUS_CASES`

`NEEDS_ORACLE_REVISION`

Then provide:

1. aggregate agreement/disagreement/ambiguity counts;
2. exact case dispositions;
3. proposed revised oracle rows only where needed;
4. cases that should become diagnostic/non-scoring;
5. any missing false-positive or false-negative control that materially affects kernel comparison;
6. whether the allowed-family envelopes are useful enough to keep or too author-dependent to score strongly.

Do not modify Current and do not infer that oracle review authorizes a new ENA release.

> The benchmark is also a variation. Reality is allowed to reject its author.
