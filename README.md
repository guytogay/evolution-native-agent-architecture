# Evolution-Native Agent Architecture (ENA)

ENA is a mechanism-first architecture for Agents expected to change, learn, recover, and evolve without silently losing evidence, authority boundaries, recoverability, or the ability to continue improving.

> Protect Agency; govern Authority.
>
> Governance must pay rent.
>
> Full map, local projection.
>
> Broad knowledge, narrow authority.

## Project status

Current adoption baseline: **ENA v0.3.3**

Status: `FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE / NOT_MAINLINE`

Version identity and maturity are separate. `v0.3.3` is one complete immutable adoption world; `FIELD_VALIDATION` describes its current evidence posture.

ENA is experimental and intended for real bounded use and heterogeneous field feedback. Field-validation status does **not** mean Mainline or universal validation.

## Start in 30 seconds

For a first-time reader:

1. Read [`PROJECT-HUB.md`](PROJECT-HUB.md) for project state and navigation.
2. For actual adoption, use only [`releases/current/`](releases/current/).
3. Start with [`releases/current/00-READ-ME-FIRST.md`](releases/current/00-READ-ME-FIRST.md).
4. For bounded low-consequence work, use [`releases/current/LITE-ADOPTION-INSTRUCTION.md`](releases/current/LITE-ADOPTION-INSTRUCTION.md).
5. Machine-readable baseline pointer: [`releases/current/CURRENT-BASELINE.yaml`](releases/current/CURRENT-BASELINE.yaml).

The current adoption release is one self-contained baseline. Do **not** compose it with older ENA releases, candidates, research artifacts, or historical branches.

> Open knowledge does not mean always-loaded knowledge.

## What is in this repository?

- the current complete ENA adoption baseline;
- schemas, templates, validator fixtures, and reference tooling;
- research and Evolution Inbox material;
- evidence and historical adversarial replay;
- experiments and prototypes;
- participant contributions and reconciliation;
- architecture/process decisions;
- Git history for previous project states without duplicating old releases inside Current.

GitHub is the canonical engineering, research-lineage, and current-adoption surface. Maintainer-private recovery mirrors may exist, but they are not required to read, adopt, validate, or contribute to ENA.

## Release rhythm

ENA does not publish a new adoption version for every small observation. Issues, field evidence, research, and fixes accumulate until a coherent set of changes earns the cost of a new flattened release.

Adoption history should remain simple and linear for users: use Current. Research can branch; runtime/adoption semantics do not require version composition.

## Participate

ENA is intended to be questioned and tested, not merely followed.

Useful contributions include:

`INCIDENT | NEAR_MISS | FRICTION | VALUE_OBSERVED | COUNTEREXAMPLE | PORTABILITY_FINDING | NEW_VARIATION | EVIDENCE_RESULT | RESEARCH_HYPOTHESIS | CRITIQUE`

For a trackable bug, improvement, research question, or release concern, open a GitHub Issue first when that is the smallest useful durable artifact.

For substantial evidence/provenance, use the contribution workflow described in [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`releases/current/CONTRIBUTION-PROTOCOL.md`](releases/current/CONTRIBUTION-PROTOCOL.md).

Reading, questioning, forking, experimenting, filing Issues, or submitting Pull Requests does not automatically grant release, promotion, Mainline, deployment, or unrelated consequential authority.

> Knowledge is commons. Inquiry is open. Authority is scoped. Adoption is governed.

## Field validation

ENA v0.3.3 is intended for heterogeneous field validation. Reports of failure, useless overhead, ambiguity, and counterexamples are as valuable as reports of success.

High-value validation areas include LITE adoption economics, authority/subject/mandate lifecycle, effect-level retry/concurrency semantics, provenance independence/closure, release parity, and unexpected composition failures.

> Production before perfection; not production without evidence.
>
> Preserve history durably; retrieve history selectively.

## License

Licensed under the **Apache License, Version 2.0**. See [`LICENSE`](LICENSE).
