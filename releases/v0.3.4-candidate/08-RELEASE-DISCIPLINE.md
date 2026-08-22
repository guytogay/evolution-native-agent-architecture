# 8. Release Discipline

A deployable ENA adoption version must be self-contained. A participant must not need to compose multiple ENA release versions to determine its effective baseline.

## Version identity

One adoption version identifies one immutable effective content state.

- `same ena_version -> same effective content`;
- any material change to the adoption package requires a new version identity;
- version identity and maturity/status are separate;
- adopters use Current only; older releases remain immutable history, not runtime dependencies.

ENA release numbers should remain simple and linear for adopters (for example `v0.3.1 -> v0.3.2 -> v0.3.3`). Research, Issues, experiments, and Git history may branch; the effective adoption line should not require version arithmetic.

Accumulate issues, field evidence, and research until a coherent set of decision-worthy changes justifies a release. Do not create a new adoption version for every small observation or cosmetic change when batching provides better project ROI and comparability.

## Frozen Current and canonical source

`releases/current/` is a frozen adoption target after release, not a live editing workspace under an unchanged version identity.

A release must be built from an identified committed Git tree/commit carrying the exact Current bytes. Do not build the canonical offline package from an independent local staging/build directory.

Because an artifact cannot safely contain a self-referential hash of itself, immutable source commit/tree identity and package digest may be recorded as release evidence outside the package while `CURRENT-BASELINE.yaml` states the required identity method.

## Distribution parity gate

Before claiming release workflow completion:

1. freeze/identify the source commit/tree;
2. enumerate the exact file set under `releases/current/`;
3. build the offline package from those committed bytes;
4. compare packaged file set against the committed source — no missing/unexpected files;
5. compare every packaged file byte/hash/blob identity against source;
6. compute and publish a package-level digest as release metadata/sidecar;
7. publish any mirror/distribution artifact;
8. read/download the published artifact back;
9. re-verify package digest and internal file parity;
10. only then claim distribution/release workflow completion.

A bundled manifest can prove internal consistency but does not by itself prove canonical-source authority. Canonical source identity and distribution parity require an external trust anchor such as the committed Git source plus published digest/read-back evidence.

`Packaging success != release workflow completion.`

`Persistence != synchronization.`

`Distribution parity must be evidenced, not assumed.`

## Transition safety

A correct final version does not prove that a mixed old/new rollout is safe. When versions interact during transition, expose version/digest/compatibility state and narrow or coordinate consequential interoperability where mixed semantics can change authority, evidence, schema, or effect interpretation.

Do not require atomic cutover when compatibility is evidenced; do not assume rolling compatibility merely because both final versions are valid in isolation.

## Branch discipline

Git branches are development mechanics, not ENA release identities.

Prefer Issues/research artifacts for exploration. For an active release effort, use at most one short-lived release branch when isolation is useful, merge it, then delete it. Do not create one branch per idea/workstream without a concrete isolation need.

## History and retrieval

Historical releases, candidates, rejected branches, and research are preserved through Git history, project research/evidence, and durable recovery archives. They are not duplicated inside Current unless a specific recovery or migration task requires them.

> **Preserve history durably; retrieve history selectively.**
>
> **Open knowledge does not mean always-loaded knowledge.**
>
> **Research may branch; an adoption baseline must be singular.**
>
> **A research lineage can be complex. A production adoption target should not require the Agent to reconstruct that lineage correctly.**

---
