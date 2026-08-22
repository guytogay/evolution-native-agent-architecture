# LINEAGE — v0.3.4-candidate

Candidate: `v0.3.4-candidate`.

Immediate predecessor: `v0.3.3` Current (`FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE / NOT_MAINLINE`).

Historical promoted Mainline: `v0.2.11 MAINLINE`.

This candidate is flattened and self-contained. It inherits still-effective v0.3.3 semantics by copying them into its own candidate tree; adopters/evaluators must not compose `releases/current/` or older releases with this directory at runtime.

## Why this candidate exists

Field finding issue #46 records an adoption/runtime ambiguity observed during fresh heterogeneous-host onboarding:

`AVAILABLE/KNOWN != INTERNALIZED != SALIENT != APPLIED`

and specifically:

`ADOPTION != RETRIEVAL`.

The candidate changes the adoption model so first adoption compiles a compact persistent Runtime Kernel plus material Local Projection, while LITE/STANDARD/HIGH_ASSURANCE/CUSTOM become runtime governance-intensity projections rather than different knowledge subsets.

## Inherited semantic lineage

The v0.3.3 composed claim-pack validator lineage remains inherited unchanged:

1. original v0.3.3 candidate -> fresh independent validation `NEEDS_REVISION`;
2. corrected v0.3.3-candidate.1 closing D1/D2/D3;
3. prior-falsifier targeted revalidation `SUPPORTED`;
4. v0.3.3 Current release with final published-artifact read-back completed.

This candidate does not reopen or relabel that evidence. It adds an adoption/runtime layer that now requires its own independent falsification.

Open research #11/#15 and tooling drift #45 remain separate unresolved lines, not hidden dependencies of this candidate.

> Preserve history durably; retrieve history selectively.
>
> A successor may change adoption semantics without rewriting predecessor evidence.
