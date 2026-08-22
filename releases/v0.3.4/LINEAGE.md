# LINEAGE — v0.3.4

Current release: `v0.3.4`.

Immediate released predecessor: `v0.3.3` Current (`FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE / NOT_MAINLINE`).

Historical promoted Mainline: `v0.2.11 MAINLINE`.

This release is flattened and self-contained. It does not require candidate directories or older releases at runtime.

## Why v0.3.4 exists

Field adoption exposed that:

`ADOPTION != RETRIEVAL`

and more generally:

`AVAILABLE/KNOWN != INTERNALIZED != SALIENT != APPLIED`.

v0.3.4 therefore introduces a persistent Runtime Kernel, Compiled Local Projection, canonical cold-path retrieval, and runtime governance-intensity profiles.

## Candidate lineage

Original frozen candidate:

- identity: `v0.3.4-candidate`
- semantic commit: `ccc66233c1abe6778177a38950af1f7bb2356b93`
- candidate-directory tree: `61cb33562626c3b8f590919c87f4637416f1ee8f`
- freeze record commit: `d4ce9ebff0f83f47090ffea8e44be9bdd6eb7f68`
- fresh independent verdict: `INDEPENDENT_RUNTIME_ADOPTION_VALIDATION_SUPPORTED_WITH_RESIDUALS`

The independent validator supported the overall model but identified D14 source-identity drift and D2 persistence-boundary claim-strength residuals.

Corrected successor:

- identity: `v0.3.4-candidate.1`
- semantic commit: `4518eeee9405c0b784401b6960dd36fee500a84f`
- candidate-directory tree: `4e6642b5c17342fe51d932d67764643c383aba82`
- freeze record commit: `32a0729518b60fefa002eed62c34f866ee5856a1`
- prior-falsifier verdict: `REVALIDATION_BY_PRIOR_RUNTIME_ADOPTION_FALSIFIER_SUPPORTED_WITH_RESIDUALS`
- D14: CLOSED
- D2: CLOSED
- fix-induced regressions: NONE OBSERVED

The original candidate was not rewritten in place; its residual evidence remains preserved.

## Real field evidence before Current

Hermes / MiniMax M3 was used as a persistent field adopter after candidate.1 semantic support.

A real fresh-session experiment observed that candidate.1 immutable source identity plus Runtime Kernel / Local Projection content were auto-injected before the first user message. A blind low-consequence local write then proceeded without re-reading canonical ENA or escalating merely because a side effect existed.

A later persistent user-preference write exposed a salience/application near-miss: recovery reasoning did not become explicit before the mutation even though the persistent kernel contained the relevant rule. This remains a field-validation target, not a rewritten candidate defect.

The same field run also exposed memory-budget pressure, motivating continued observation of consolidation/truncation/drift economics without inventing a new rule from one Host.

## Inherited semantic lineage

The v0.3.3 composed claim-pack validator lineage remains inherited unchanged. Constitution, roles, capability map, core contracts, schemas, tools, and the 235-case regression corpus are not reopened by this release.

Open research #11/#15 and tooling drift #45 remain separate unresolved lines, not hidden dependencies.

> Preserve history durably; retrieve history selectively.
>
> A release may improve adoption semantics without rewriting predecessor evidence.
