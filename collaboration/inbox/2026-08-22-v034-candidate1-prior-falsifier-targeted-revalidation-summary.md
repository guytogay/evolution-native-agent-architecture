# ENA v0.3.4-candidate.1 — Prior-Falsifier Targeted Revalidation Evidence Summary

Date: 2026-08-22

Status: `TARGETED_REVALIDATION_COMPLETE / SEMANTIC_RESIDUALS_CLOSED / FIELD_EVIDENCE_STILL_REQUIRED / NOT_CURRENT / NOT_MAINLINE / NOT_PROMOTED`

## Revalidator provenance

This was performed by the **same WorkBuddy validator** that independently found D14 and D2 in the original frozen `v0.3.4-candidate`.

Role:
`PRIOR_INDEPENDENT_RUNTIME_ADOPTION_FALSIFIER_TARGETED_REVALIDATION`

It was explicitly **not** relabeled as a new fresh independent validator.

Supplied full report:
`ENA-v0.3.4-candidate.1-TARGETED-REVALIDATION.md`

Host-side SHA-256 of supplied full report bytes:
`616daf4e4dc9e4f5925290ca20d5501aa19504fee51c9b4c084fce4958808716`

Observed file length: 132 newline-terminated lines in the supplied artifact (`wc -l`); report content carries 133 numbered display lines in the chat attachment representation.

## Frozen identities reverified by the prior falsifier

Original candidate:
- semantic commit: `ccc66233c1abe6778177a38950af1f7bb2356b93`
- candidate-directory tree: `61cb33562626c3b8f590919c87f4637416f1ee8f`
- freeze record commit: `d4ce9ebff0f83f47090ffea8e44be9bdd6eb7f68`
- original freeze record restored byte-identically at current PR branch tip; not relabeled candidate.1.

Corrected successor:
- identity: `v0.3.4-candidate.1`
- semantic commit: `4518eeee9405c0b784401b6960dd36fee500a84f`
- candidate-directory tree: `4e6642b5c17342fe51d932d67764643c383aba82`
- freeze record commit: `32a0729518b60fefa002eed62c34f866ee5856a1`
- separate freeze record: `collaboration/inbox/2026-08-22-v034-candidate1-residual-closure-freeze.md`

## Exact successor-delta findings

The revalidator reported 10 changed files, all confined to the adoption/runtime theme.

The following inherited surfaces remained byte-identical to both the original candidate and `releases/current/`:
- Constitution;
- roles/developmental stages;
- capability map;
- core operational contracts;
- evolution/open-participation;
- release discipline;
- contribution protocol;
- schemas;
- templates;
- validator;
- regression runner;
- inherited fixtures/results.

The revalidator did not rerun the 235-case corpus because the relevant blobs were byte-identical to the exact tooling already run in its prior validation (previous result: PASS, zero unexpected, zero exceptions, inherited 164 preserved, zero flips). It classified a redundant rerun as ceremony rather than new evidence.

## D14 targeted revalidation

Verdict: `CLOSED`

The corrected semantics now require the Compiled Local Projection to preserve an **immutable canonical source identity** actually compiled from (commit/tree/package digest) in addition to a human-readable label. Mutable branch or version label alone is explicitly insufficient as an integrity anchor.

Decision-critical cold-path revalidation is triggered when immutable source identity:
- changes;
- cannot be confirmed;
- conflicts with the compiled identity.

For transformed/paraphrased kernels, source/transformation lineage and material fidelity verification remain required; successful storage alone does not establish semantic fidelity.

The revalidator found no self-referential digest requirement and no per-task hash-check ritual.

## D2 targeted revalidation

Verdict: `CLOSED`

Before claiming ENA adoption persists across a fresh-session or equivalent decision-critical boundary, the actual boundary claimed must be evidenced.

A current-session persistence write proves only the narrow fact that a persistence object was written. It does not by itself prove a genuinely fresh session receives, interprets, or applies it.

Narrower truthful persistence claims remain permitted and do not require a fresh-session experiment merely to report that an object was written.

## Fix-induced regressions

Verdict: `NONE OBSERVED`

The revalidator specifically checked for:
- mandatory per-task hash checking;
- version labels becoming unusable;
- inability to work when source identity is temporarily unreachable but irrelevant;
- harmless source uncertainty causing false escalation;
- fresh-session testing being forced onto narrow/session-local claims;
- persistence evidence being confused with correct application;
- source digest being confused with semantic fidelity;
- self-referential final-tree embedding.

None were observed.

## Persistence experiment

`PERSISTENCE_TEST_UNAVAILABLE`

The WorkBuddy Host still could not genuinely stand up and independently verify a fresh-session boundary. This remains an **experiment/Host limitation**, not a failed D2 closure.

The important result is that candidate.1 now constrains what may be claimed when this evidence is unavailable rather than manufacturing persistence evidence.

## Optional recovery-root residual

The prior optional self-hosted recovery-root hardening suggestion remains an acceptable, non-blocking residual/field concern. The revalidator found no new false-confidence path requiring promotion of that suggestion into a mandatory mechanism.

## Final verdict

`REVALIDATION_BY_PRIOR_RUNTIME_ADOPTION_FALSIFIER_SUPPORTED_WITH_RESIDUALS`

Disposition reported by the prior falsifier:
- candidate.1 may proceed to reconciliation: **YES**;
- another semantic successor required: **NO**;
- D14: **CLOSED**;
- D2: **CLOSED**;
- remaining blocker: **evidence / field validation**, not semantic correction;
- genuine fresh-session persistence experiment remains open;
- optional self-hosted recovery-root hardening remains later field work.

The revalidator performed no repository mutation, no merge, no promotion, and no modification of `releases/current/`.
