# Evolution-Native Agent Architecture (ENA)

ENA is a mechanism-first architecture for Agents expected to change, learn, recover, and evolve without silently losing evidence, authority boundaries, recoverability, or the ability to continue improving.

**ENA exists to make sustained self-evolution viable.**

> Evolution is the purpose. Governance protects evolvability.
>
> Governance must pay rent.
>
> Open knowledge does not mean always-loaded knowledge.

## Start here

For adoption, use the repository's canonical default branch and follow one stable pointer:

1. Read [`PROJECT-HUB.md`](PROJECT-HUB.md).
2. Treat [`releases/current/CURRENT-BASELINE.yaml`](releases/current/CURRENT-BASELINE.yaml) as the machine-readable adoption identity.
3. Use only [`releases/current/`](releases/current/) for the effective ENA baseline.
4. Start actual adoption with [`releases/current/00-READ-ME-FIRST.md`](releases/current/00-READ-ME-FIRST.md).

Do **not** infer the current ENA from version numbers, candidate names, commit recency, branch names, research artifacts, or historical evidence.

`Git main != ENA Current`

- **Git `main`** is the canonical project branch.
- **ENA Current** is the singular adoption baseline under `releases/current/`.
- **Maturity/status** is declared by the Current baseline; v0.3.7 is `FIELD_VALIDATION` in this release payload.

Beginning with v0.3.5, historical `MAINLINE / NOT_MAINLINE` labels are no longer an active adopter-facing maturity axis. Historical records using them remain unchanged as occurrence truth.

## Current direction

v0.3.7 preserves the v0.3.6 Evolution Ecology semantic trunk while making concrete HOWs substantially easier to retrieve and use:

- a compact Runtime Adoption Kernel with hot cues rather than an always-loaded HOW encyclopedia;
- consequence-first `operational/CUE-INDEX.md` and `operational/HOW-MAP.md` routing;
- Purpose-Relative Continuity, Standing Input, and Control Retirement procedures;
- Evolution Commons and Host Mapping patterns;
- bundled **optional/default-off** reference organs whose inclusion does not make them normative or universally applicable;
- a primary narrow v2 practical evolution path at `tools/ena_evolve_v2.py`;
- explicit legacy compatibility under `tools/legacy/`;
- decision-bearing zh-CN Operational Architecture projection while preserving one canonical machine surface.

All 38 inherited Constitution IDs remain unchanged. v0.3.7 does not claim that machine consistency proves external authority/receipt truth, universal Host applicability, natural future-session salience, or universal bilingual behavioral equivalence; those remain explicit evidence/field boundaries.

## Repository shape

The ordinary adoption hot path is intentionally small:

- `PROJECT-HUB.md`
- `releases/current/`

Research, evidence, reconciliation, experiments, and Git history remain available as cold-path material when a real question requires them.

Historical versions and candidates are preserved through Git history, release evidence, and [`HISTORY.md`](HISTORY.md); they are not parallel adoption choices.

> **Expose one adoption surface; preserve many historical surfaces.**
>
> **Current is the hot path; history is the cold path.**

## Participate

ENA is intended to be questioned and tested, not merely followed. For contribution guidance see [`CONTRIBUTING.md`](CONTRIBUTING.md) and the Current contribution protocol.

Reading, questioning, forking, experimenting, filing Issues, or submitting Pull Requests does not automatically grant release, deployment, remediation, or unrelated consequential authority.

## License

Licensed under the **Apache License, Version 2.0**. See [`LICENSE`](LICENSE).
