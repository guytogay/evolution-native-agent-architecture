# Evolution-Native Agent Architecture (ENA)

ENA explores durable properties of Agents expected to change, learn, recover, propagate adaptations, and evolve without silently losing evidence, authority boundaries, recoverability, or the ability to continue improving.

**ENA exists to make sustained self-evolution viable.**

> Evolution is the purpose. Governance protects evolvability.
>
> Governance must pay rent.
>
> Variation first; selection by reality.

ENA may contain abstract semantic work. An abstract distinction earns its place by helping explain or discriminate real evolutionary behavior; it does not need to pretend to be a turnkey framework.

## Start here

### To use the current ENA baseline

1. Read [`releases/current/CURRENT-BASELINE.yaml`](releases/current/CURRENT-BASELINE.yaml) for the machine-readable Current identity.
2. Use only [`releases/current/`](releases/current/) as the effective adoption baseline.
3. Start with [`releases/current/00-READ-ME-FIRST.md`](releases/current/00-READ-ME-FIRST.md).

Do **not** infer Current from version numbers, branch names, candidate names, commit recency, research notes, or historical evidence.

`Git main != ENA Current`

- **Git `main`** is the canonical repository branch.
- **ENA Current** is the singular adoption baseline under `releases/current/`.
- v0.3.7 remains `CURRENT / FIELD_VALIDATION` until a later release is actually justified and promoted.

### To continue ENA research/project work

Read [`NOW.md`](NOW.md), then open only the Issue/files needed for the current consequential action.

Old project hub, metadata, handoff, progress, branch-inventory, reconciliation, release, and candidate records remain available as cold history. They are not mandatory takeover reading.

## Current semantic direction

v0.3.7 Current includes a compact Runtime Adoption Kernel, consequence-first cue/HOW routing, Purpose-Relative Continuity, Standing Input, Control Retirement, Evolution Commons/Host Mapping patterns, optional references, a narrow v2 evolution helper, and explicit evidence/Host/language boundaries.

Current research is also examining two connected selection questions outside the immutable v0.3.7 package:

- **purpose-relative selection** — a change is not evolution merely because a metric/capability increased; selection must remain related to the purpose/context that made the adaptation valuable, while allowing purpose itself to evolve explicitly;
- **propagation fitness** — local fitness, heritability, portability, and population/commons propagation are distinct dimensions; more portable does not automatically mean more evolved.

See [`research/evolution-inbox/PURPOSE-RELATIVE-SELECTION-AND-PROPAGATION-FITNESS.md`](research/evolution-inbox/PURPOSE-RELATIVE-SELECTION-AND-PROPAGATION-FITNESS.md).

No new Constitution ID is implied merely because a useful new expression was found. Existing semantics should be reused or clarified before growing the universal invariant set.

## Repository shape

The live surfaces are intentionally small:

- adoption truth: `releases/current/`;
- live project/research status: `NOW.md`;
- open work and field contact: GitHub Issues;
- history/evidence: Git history plus the relevant research/evidence records.

Research, prototypes, experiments, reconciliations, handoffs, and old plans are cold-path material: retrieve them when a concrete question needs them rather than loading them by default.

## Validation and release discipline

Executable logic should keep executable tests.

- changes to `releases/current/**` receive Current semantic/regression/package validation;
- executable/Python changes receive relevant selftests and security/static checks;
- ordinary research/doc changes outside Current do not need release-style freeze/readback/package ceremony.

A release remains a higher-consequence boundary. Ordinary thinking is not a release.

## Participate

ENA is intended to be questioned, falsified, specialized, partially adopted, and improved. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

Reading, questioning, forking, experimenting, filing Issues, or submitting Pull Requests does not automatically grant release, deployment, remediation, or unrelated consequential authority.

## License

Licensed under the **Apache License, Version 2.0**. See [`LICENSE`](LICENSE).
