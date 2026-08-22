# LINEAGE — v0.3.4-candidate.1

Candidate: `v0.3.4-candidate.1`.

Immediate predecessor candidate: frozen `v0.3.4-candidate`.

Released predecessor: `v0.3.3` Current (`FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE / NOT_MAINLINE`).

Historical promoted Mainline: `v0.2.11 MAINLINE`.

This candidate is flattened and self-contained. It does not require the original v0.3.4 candidate or `releases/current/` at runtime.

## Why candidate.1 exists

The original `v0.3.4-candidate` introduced:

`ADOPTION != RETRIEVAL`

through a persistent Runtime Kernel, Compiled Local Projection, canonical cold-path retrieval, and runtime governance-intensity profiles.

Fresh independent validation of that frozen candidate returned:

`INDEPENDENT_RUNTIME_ADOPTION_VALIDATION_SUPPORTED_WITH_RESIDUALS`

The model was supported, but two residuals were identified before promotion:

1. the persisted projection did not require an immutable canonical source identity, leaving a label/branch drift path;
2. the persistence-boundary wording could allow a current-session persistence write to be overclaimed as fresh-session adoption without actual-boundary evidence.

## Successor relationship

The original candidate remains immutable:

- semantic commit: `ccc66233c1abe6778177a38950af1f7bb2356b93`
- candidate-directory tree: `61cb33562626c3b8f590919c87f4637416f1ee8f`
- freeze record commit: `d4ce9ebff0f83f47090ffea8e44be9bdd6eb7f68`

candidate.1 preserves that negative/residual evidence and corrects it in a new identity rather than editing the frozen candidate in place.

The correction is below the constitutional layer:

- immutable source commit/tree/package identity becomes part of the Compiled Local Projection;
- mutable branch/version labels are insufficient alone as integrity anchors;
- source-identity change/conflict/unconfirmability can trigger canonical revalidation;
- transformed persisted kernels preserve source lineage;
- cross-session persistent-adoption claims require evidence across the actual boundary claimed.

The concrete source digest installed by an adopter is supplied by candidate freeze/distribution evidence and recorded at compile time; it is not self-referentially embedded into the candidate content.

## Inherited semantic lineage

The v0.3.3 composed claim-pack validator lineage remains inherited unchanged. Constitution, roles, capability map, core contracts, schemas, tools, and the 235-case regression corpus are not reopened by this successor.

Open research #11/#15 and tooling drift #45 remain separate unresolved lines, not hidden dependencies.

Next actor:
`PRIOR_INDEPENDENT_RUNTIME_ADOPTION_FALSIFIER_TARGETED_REVALIDATION`

> Preserve history durably; retrieve history selectively.
>
> Correct a frozen candidate by successor identity, not by rewriting its evidence.
