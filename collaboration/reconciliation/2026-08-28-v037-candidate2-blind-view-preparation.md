# ENA v0.3.7 candidate.2 blind semantic view preparation audit

Date: 2026-08-28

Status: `BLIND_VIEW_PREPARED_AND_AUDITED / FRESH_A_S_INTAKE_READY / NOT_A_CANDIDATE / NOT_RELEASE_AUTHORITY`

## Exact frozen target

- identity: `v0.3.7-candidate.2`
- frozen source: `bda470e0a6b170cec61225a905957a501454a2fe`
- frozen candidate subtree: `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`
- candidate path: `releases/v0.3.7-candidate/`
- Current subtree at freeze: `7dcbb3934883ffa6cc5292a662588cafc1533cff`

Candidate.2 remains frozen and immutable. This preparation does not change candidate cargo or Current.

## Validation projection

Branch:

`validation/v037-c2-blind-semantic-primary`

Prepared view head:

`d020d82d442156b75c667ee9f987f2654d814561`

Neutral entry:

`collaboration/reconciliation/2026-08-28-v037-candidate2-blind-semantic-entry.md`

Blind-view manifest:

`collaboration/reconciliation/2026-08-28-v037-candidate2-blind-semantic-view.yaml`

The branch was created directly from the exact frozen source, then reduced only by declared information-role exclusions before the neutral entry and manifest were added.

## Information-role audit

The candidate.1 blind-view deletion list was not copied mechanically.

Candidate.2 introduced a new self-priming surface:

`08-RELEASE-DISCIPLINE.md`

It disclosed predecessor fresh-review findings, predecessor independent seal/A-P identities, the predecessor NEEDS_REVISION disposition, and successor repair narrative. That file is therefore withheld in candidate.2 A-S even though it had not been a whole-file exclusion in the prior blind view.

Three candidate overview files also carry status/confidence headers while retaining useful semantic content. They are kept byte-identical but require ranged reads during A-S:

- `README.md`: A-S may read `9-EOF`; lines `1-8` withheld as author status/confidence;
- `00-READ-ME-FIRST.md`: A-S may read `7-EOF`; lines `1-6` withheld as package status;
- `RUNTIME-ADOPTION-KERNEL.md`: A-S may read `7-EOF`; lines `1-6` withheld as package status.

The mixed-role evolution validator remains fully byte-identical. Its executable semantics are visible while its embedded author selftest corpus is withheld:

- `tools/validate_evolution_record_v2.py`: A-S may read `1-358` and `789-EOF`; lines `359-788` withheld; `--selftest` must not be invoked before A-S seal.

## Whole-file exclusions

The manifest declares 31 whole-file A-S exclusions covering only these information roles:

- candidate history / lineage / author confidence;
- predecessor findings and repair narrative;
- expected semantic fixtures;
- composed-regression oracles/results;
- helper/reference selftest corpora;
- prior adversarial probe corpora.

No semantic validator, schema, template, Operational Architecture HOW, Constitution/Core semantic surface, Authority implementation, Effect implementation, Recovery implementation, WAIT implementation, or evidence implementation was removed merely to make the view easier to pass.

## Mechanical source-to-view audit

Compared:

`bda470e0a6b170cec61225a905957a501454a2fe`

against:

`d020d82d442156b75c667ee9f987f2654d814561`

Observed diff:

- 31 declared candidate-file removals;
- 2 additions: neutral entry + blind-view manifest;
- 0 modified retained candidate files;
- no other file changes.

Therefore:

`RETAINED_CANDIDATE_BYTES_EQUAL_FROZEN_SOURCE = PASS`

High-value retained blob readback:

- evolution-record v2 validator: `4a98306ee8bc0685ec6706aedb782381f57071bb`
- Authority Lease validator: `9a73191b79bcdd62df9490fcc37e58cc154090c7`
- Effect Lifecycle validator: `b56340799abdf552662482809aeb40ea94309581`
- evolution-record v2 schema: `84af09cc2bc91dfe0193722c3f954ba5f266eb72`

These match the exact frozen candidate source.

## Why this is not release ablation

The projection exists only to protect A-S search-space independence.

After A-S is sealed, A-P is explicitly required to reopen the withheld candidate-local history, self-description, fixture, and oracle surfaces from the exact frozen source. Therefore the full package is still independently audited; review is temporally layered rather than permanently narrowed.

`EXCLUSION_FOR_BLINDNESS != RELEASE_ABLATION`

`BLIND_VIEW != NEW_CANDIDATE`

## Reviewer-role boundary

The current project-manager session is materially exposed to candidate.2 repair history and author-side probes and cannot perform fresh A-S.

A genuinely fresh reviewer must start from the neutral entry on this validation branch, obey the manifest through A-S seal, then perform A-P and stop before Phase B.

## Operator noise

Issues `#135` and `#136` were accidental tool-routing placeholders, closed immediately as `not_planned`. They carry no project, validation, candidate, or release authority and must not be used for continuation.

## Verdict

`PASS / FRESH_INTAKE_MAY_BE_CREATED`

Attack cardinality remains open. This audit establishes only the integrity and information-role discipline of the validation interface; it does not establish candidate correctness or release readiness.
