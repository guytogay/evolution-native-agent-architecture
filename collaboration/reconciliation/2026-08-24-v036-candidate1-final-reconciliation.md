# ENA v0.3.6 candidate.1 — final reconciliation

Date: 2026-08-24

## Reconciler role

`HOST_SIDE_RECONCILER / RELEASE_DECISION_COLLABORATOR / NOT_INDEPENDENT_VALIDATOR`

This reconciliation does not relabel author-side work, CI, or same-falsifier targeted revalidation as fresh independent validation.

## Inputs

### Frozen candidate.0

- source: `3cb94d98882621acede189d0d47806efae44fb0f`
- effective candidate tree: `80f2da918811c26381d65eb5afa8e40f8410a32e`
- freeze-record commit: `15e513a72d59e28f8d3050ef877746f85ab706ba`
- fresh independent semantic falsifier verdict: `NEEDS_REVISION`
- PR #68, closed without merge after successor handoff
- independent report comment: `issuecomment-5389079667`

### Frozen candidate.1

- source: `4af5d17a1cedcf2850b2b4dfe5446e132023369a`
- effective candidate tree: `52a0cc260ec33fc3e332f6ac0f98f5d1e98b565d`
- freeze-record commit: `aa9a79b305d2ae8f8ff423df314af974e2e51d23`
- Draft PR #69

### Final exact-source machine evidence

On frozen source `4af5d17a1cedcf2850b2b4dfe5446e132023369a`:

- ENA v0.3.6 Candidate Validate run `32677101732` — `SUCCESS`
- Main Gate run `32677101720` — `SUCCESS`
- CodeQL run `32677101753` — `SUCCESS`
- `EVOLUTION_RECORD_V2_SELFTEST_PASS 18`
- inherited `ena_evolve.py` selftest — PASS, schema 1.2, 10 cases
- inherited composed regression — `10/10 + 164/164 + 61/61 = 235/235`
- unexpected verdicts — `0`
- uncaught exceptions — `0`
- Python compile — `7/7`
- no Python bytecode artifacts
- validation worktree clean
- Current tree preserved as `9c928b4c99ae72e53c89978cf1d10b7ea068c182`

Machine evidence is not semantic acceptance by itself.

### Same-falsifier targeted revalidation

Role:

`SAME_FALSIFIER / TARGETED_REVALIDATION / NOT_FRESH / NOT_AUTHOR`

Report comment on PR #69:

`issuecomment-5389505830`

Verdict:

`TARGETED_REVALIDATION_PASS_WITH_RESIDUALS`

The same falsifier replayed its predecessor attacks against the exact frozen candidate.1 and reported:

- F-01 `CLOSED`
- F-02 `CLOSED`
- F-03 `CLOSED_WITH_RESIDUAL`
- F-04 `CLOSED`
- F-05 `CLOSED_WITH_RESIDUAL`
- F-06 `CLOSED`
- F-07 `CLOSED`
- F-08 `CLOSED`
- F-09 `CLOSED_BY_TRUTHFUL_BOUNDARY`
- F-10 `CLOSED`

No material repair-induced regression was reported.

## Reconciliation finding

The decision-changing successor cycle has converged.

The two predecessor material release blockers, F-01 and F-02, are closed for the right reasons: the invalid attack cases are rejected while legitimate controls remain representable.

The remaining successor-repair findings are either closed or truthfully bounded without introducing a new material false-OK, false-BLOCK, false-confidence, or over-governance regression.

No new `MATERIAL_RELEASE_BLOCKER` was reported.

## Why candidate.2 is not justified

The remaining residuals do not currently justify another frozen successor:

### F-03 residual — provenance self-assertion

A dishonest record may label sourced evidence as `provenance: LOCAL`. This is a real represented-truth limitation, but the current schema cannot establish external historical truth merely by adding more self-authored fields. Treating this as a release blocker would confuse representation consistency with external attestation.

### F-05 residual — obligation-reference authenticity

`triggered_obligation_refs` can contain an unverified reference string. This is visible false-confidence risk, but the repair already makes the unresolved consequence/obligation machine-visible. A future minimal reference-integrity mechanism may strengthen this without requiring a new approval organ.

### F-09 residual — inherited tool false-BLOCK

The inherited `ena_evolve.py` remains schema/state 1.2 and still requires `--variation-space` on `propose`/`import`. Candidate.1 truthfully marks it as non-normative for the v0.3.6 latent-now/experiment-later path. The same falsifier classified this `CLOSED_BY_TRUTHFUL_BOUNDARY` and nonblocking. A later tiny adapter or optional variation-space input may improve ergonomics, but full v2 runtime symmetry is not justified merely for aesthetic completeness.

### Conservative tied-latest timestamp rejection

Rejecting tied latest instants is conservative and can false-BLOCK some legitimate histories, but no material release failure was demonstrated. Preserve as a visible usability/research residual rather than adding an arbitrary tie-break oracle.

### F-11 / F-12

Future cue salience/application remains field evidence, and `experiments` versus broader `reality contact` terminology remains research wording. Neither is a hidden release claim.

Creating candidate.2 solely to erase these visible residuals would optimize governance cleanliness rather than decision-relevant evolvability.

`Governance must pay rent.`

Therefore:

`CANDIDATE_SUCCESSION_STOP = YES`

unless new material evidence appears.

## Accepted residuals

Carry forward visibly into release lineage / field / research tracking:

1. F-03 — self-asserted `LOCAL` provenance is not external proof;
2. F-05 — obligation references are represented but not authenticated merely by schema acceptance;
3. F-09 — inherited v0.3.5 reference tool false-BLOCKs the normative v0.3.6 latent propose/import path and remains explicitly non-normative for that path;
4. tied-latest timestamp rejection is conservative;
5. F-11 — fresh-session cue salience/application remains unproven field evidence;
6. F-12 — experiment/reality-contact terminology remains research wording.

Do not silently call these solved. Do not add Constitution rules from them without stronger evidence.

## Constitution / semantic-core outcome

The independent falsifier supported preserving the v0.3.6 Evolution Ecology semantic core, including:

- Mutation Pressure without forced mutation;
- legitimate long-lived Latent Variation;
- separate lifecycle / expression / selection axes;
- `stored != expressed != applied != selected`;
- Evolution Commons publication/discovery/import/local-reselection separation;
- environment-local selection rather than universal scalar fitness;
- Rescue Plane without sovereign approval authority;
- minimal-intervention ecological governance with externality boundaries;
- carrier-independent canonical lineage property with GitHub as current carrier;
- staged representation/runtime evolution when implementation gaps remain explicit.

All 38 inherited Constitution IDs remain unchanged.

`NEW_CONSTITUTION_IDS = 0`

## Release decision

Frozen candidate.1 is accepted as the semantic/representation source for preparing ENA v0.3.6 release packaging.

Decision:

`RELEASE_PREPARATION_SUPPORTED`

Target adopter-facing release state:

`v0.3.6 / CURRENT / FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE`

This decision does not itself merge or publish Current.

## Release packaging constraints

Release packaging may change candidate/release identity metadata needed to transform the frozen candidate into adopter-facing v0.3.6 Current, but must not silently alter the validated material semantics.

At minimum:

- transform `v0.3.6-candidate.1` identity into `v0.3.6` Current identity;
- replace `CANDIDATE-BASELINE.yaml` with an appropriate `CURRENT-BASELINE.yaml`;
- preserve all 38 Constitution IDs and material Constitution semantics;
- preserve candidate.1 v2 schema/validator behavior closing F-01/F-02;
- preserve `adaptation-packet.v1` compatibility and additive packet v2 representation contract;
- keep the inherited `ena_evolve.py` runtime boundary explicit rather than claiming v2 implementation it does not have;
- preserve English/zh-CN decision semantics and rebind supported projections to immutable release identity;
- preserve accepted residuals visibly in lineage/changelog/research/field tracking;
- publish one singular `releases/current/` adoption surface and remove the candidate directory from the final adopter-facing repository surface;
- verify exact source/tree/file-set/package identity and published readback before claiming release workflow complete.

## Next meaningful evidence after release

The highest-value next evidence is heterogeneous fresh-Host use of the v0.3.6 ecology semantics, especially:

- whether cues become salient naturally without prompt encyclopedias;
- whether long-lived latent variation remains useful rather than becoming a garbage reservoir;
- whether local reselection keeps Commons useful without importing source conclusions;
- whether expression-state representation corresponds to real behavior often enough to justify the third axis;
- whether Rescue Plane remains narrow in actual deployments;
- whether the ecology machinery costs less attention/tooling than the adaptation value it creates;
- whether EN/zh-CN hot paths remain materially decision-equivalent;
- whether the inherited reference-tool boundary causes practical confusion despite its explicit non-normative status.

Do not manufacture candidate.2 or another validator ceremony unless a decision-changing hypothesis appears.

> Variation first; selection by reality.
>
> Governance must pay rent.
>
> Evolution is the purpose; governance protects evolvability.
