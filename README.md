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
- **Maturity/status** is declared by the Current baseline; v0.3.5 is `FIELD_VALIDATION`.

Beginning with v0.3.5, historical `MAINLINE / NOT_MAINLINE` labels are no longer an active adopter-facing maturity axis. Historical records using them remain unchanged as occurrence truth.

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
