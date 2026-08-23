# ENA v0.3.5 final release reconciliation

Date: 2026-08-23

## Final status

`ENA v0.3.5 = CURRENT / FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE`

`RELEASE_WORKFLOW_COMPLETE = YES`

`CANDIDATE_SUCCESSION_STOP = YES unless new material evidence appears`

Beginning with v0.3.5, `MAINLINE / NOT_MAINLINE` is not an active adopter-facing maturity axis. Historical records using those labels remain unchanged.

## Release decision lineage

### First frozen candidate

- source commit: `eb6d7ba00894ed446903aebe61cd59f0bdb59af7`
- effective candidate tree: `f373e7695348c157dcd48d3ed243ea3079215b8f`
- DSH independent v0.3.5 falsifier verdict: `NEEDS_REVISION`

### Frozen candidate.1

- source commit: `e6ff1e76afb8ad8919186786100ec153a5f0d07a`
- effective candidate tree: `ff2cb44c7a5d1b472800180578b5df7baa123aec`
- DSH role: `SAME_FALSIFIER / TARGETED_REVALIDATION / NOT_FRESH`
- verdict: `TARGETED_REVALIDATION_SUPPORTED_WITH_RESIDUALS`

### Frozen candidate.2

- source commit: `8393b8b05d34797965c612e8b9ca938d306f6322`
- effective candidate tree: `b10854f191d9641138e2f44278f043f124a2e120`
- freeze-record commit: `34e12333bcbe6cf8a3a2a992040d93012ead868b`
- DSH role: `SAME_FALSIFIER / NARROW_RESIDUAL_REVALIDATION / NOT_FRESH`
- verdict: `NARROW_REVALIDATION_SUPPORTED`

The narrow revalidation mechanically closed N1 invalid lifecycle self-consistency, N2 forged source-authentication self-assertion, adjacent forged transfer status, and N7 generated-regression-result drift; candidate.1 material regressions remained closed; no new MATERIAL/BLOCKING issue or evolution-starvation/over-governance regression was reported.

Host-side pre-release reconciliation:

- commit: `bbdb0347ee83b1d76d21f54e1c16c6038442b26d`
- decision: `RELEASE_PREPARATION_SUPPORTED`

This same-falsifier evidence is not relabeled as fresh independent validation.

## Release merge

Release PR:

`#64 — Release ENA v0.3.5 as Current evolution baseline`

PR head at final release review:

`502e4ee635d98c230c94e66112e215ef45d4579f`

Final PR-head automated checks:

- Main Gate run `32622821921` — SUCCESS
- Validate and package ENA Current run `32622821905` — SUCCESS
- CodeQL run `32622821928` — SUCCESS

Release merge commit:

`a18ec89d0be3a9fbd872306aa2914a05adae5e62`

The merge commit is GitHub-verified and its actual Git-object parents are:

- previous main: `9d84e179aae9f5f5d8dbabc7be56dee4ae2f8724`
- release head: `502e4ee635d98c230c94e66112e215ef45d4579f`

## Exact Current identity

Merge root Git tree:

`639f9dafe0c0d4d65327ad195c7cc8823b4b5d0c`

The final PR-head workflow recorded the same root tree for head commit `502e4ee635d98c230c94e66112e215ef45d4579f`.

Post-merge `releases/` tree:

`c174d619918f8dedcfdb3318a92ed8b4a6100cd8`

Post-merge `releases/current/` tree:

`9c928b4c99ae72e53c89978cf1d10b7ea068c182`

`releases/` contains only the compact releases README plus the singular `current/` adoption surface. Superseded candidate directories remain recoverable through Git/PR/evidence history rather than as parallel adopter-facing release trees.

## Deterministic package evidence

The release workflow builds the ZIP entirely from Git object bytes under the canonical Current source commit, with sorted paths and fixed ZIP timestamp/permissions/compression settings.

Canonical Current source commit selected by the workflow:

`32c57da7caf8f8edfdd2e85f252c14fddebcca3c`

Package:

`ENA-v0.3.5-CURRENT.zip`

Deterministic inner package SHA-256:

`b4a0c1188729b10df9b4e68f67118e6679ffcc1c9007828e474522f6c5b4732d`

File count:

`49`

PR-head published workflow artifact:

- artifact ID: `9488870775`
- artifact name: `ENA-v0.3.5-release-package`
- GitHub artifact-wrapper digest: `sha256:eb36c0185d9388f516cec07a87f90a3cede60fc7dd2df39c1c9227b12d4f7bfa`

The artifact-wrapper digest is not the release-package digest. The canonical release package identity is the inner deterministic ZIP SHA above.

PR-head package verification established:

- source bytes were read from Git objects;
- exact source/ZIP file-set parity;
- per-file SHA-256 parity after ZIP readback;
- deterministic ZIP metadata;
- 49 files.

## Post-merge readback

`POST_MERGE_GIT_OBJECT_READBACK = PASS`

The final PR-head root tree and the merged main root tree are both:

`639f9dafe0c0d4d65327ad195c7cc8823b4b5d0c`

Therefore the merged main Current subtree is byte-for-byte the same reviewed Current subtree:

`9c928b4c99ae72e53c89978cf1d10b7ea068c182`

Because the package construction is deterministic over those Git-object Current bytes, the released Current tree preserves the already-read-back deterministic package identity:

`b4a0c1188729b10df9b4e68f67118e6679ffcc1c9007828e474522f6c5b4732d`

The available GitHub connector in this reconciliation could enumerate pull-request-triggered workflow runs but not list main-push-triggered runs by commit. No main-push artifact ID is invented or claimed. This is a connector-observability limitation, not an unknown about merged Current bytes: exact Git-object identity is established above.

## Release semantic outcome

v0.3.5 makes ENA's positive telos explicit:

> **ENA exists to make sustained self-evolution viable.**
>
> **Evolution is the purpose. Governance protects evolvability.**

The Current baseline now explicitly supports:

`observe -> wake -> vary -> experiment -> evaluate/select -> integrate/prune -> migrate/recombine -> repeat`

while retaining truthful evidence/claim boundaries, recovery and history distinctions, bounded external authority, composition semantics, effective-loading evidence, and future correction capacity.

The release also introduces English + Simplified Chinese semantic projection hot paths and a Constitution concept map without deleting or renumbering the 38 universal Constitution IDs.

## Retained residuals

The following candidate.1 observations remain explicit research/field opportunities rather than release gates:

- N3 — repeated evaluation/reinterpretation of one represented experiment;
- N4 — source-negative lineage becomes nested after receiver positive reselection;
- N5 — no in-place restore/reopen for archived/retired candidates in the reference tool;
- N6 — migration-lineage depth growth across generations.

No candidate.3 is authorized by these observations alone.

## Next evidence boundary

The next high-value evidence is heterogeneous fresh-Host field use, tracked in issue `#61`.

High-value questions include whether v0.3.5:

- naturally wakes on real corrections/friction/opportunity without forcing pointless mutation;
- provides enough real Variation Space to try uncertain changes;
- turns real outcomes into useful selection rather than paperwork;
- accelerates useful adaptation migration without copying conclusions;
- supports positive composition/emergence discovery;
- prunes stale adaptation without losing material learning;
- remains lightweight enough that governance does not starve evolution;
- behaves materially equivalently across supported language projections.

Do not create a fresh validation ceremony merely to increase role/test counts. Use new validators/Hosts when they answer a material question the existing evidence cannot answer.

## Final claim boundary

This release decision proves a reviewed and reconciled Current baseline was published with exact Git-object identity and deterministic package evidence.

It does **not** prove:

- universal model/Host/language behavior;
- that every future self-mutation is beneficial;
- that all external evidence/authority/recovery statements entered into reference tools are true;
- that retained N3–N6 observations are permanently harmless;
- that field evolution value has already been demonstrated across heterogeneous Hosts.

Those are field/research questions, not hidden release claims.

> **Variation first; selection by reality.**
>
> **Governance must pay rent.**
