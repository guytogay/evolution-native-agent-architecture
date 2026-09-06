# Evolution-Native Agent Architecture (ENA)

ENA is a design method, operational rule set, and conformance surface for Agents expected to learn, adapt, recover, use tools, affect external systems, and pass adaptations onward.

**ENA exists to make sustained self-evolution viable.**

> Evolution is the purpose. Governance protects evolvability.
>
> Governance must pay rent.
>
> Variation first; selection by reality.

## Use ENA

Current adoption truth is always:

- machine identity: [`releases/current/CURRENT-BASELINE.yaml`](releases/current/CURRENT-BASELINE.yaml)
- effective package: [`releases/current/`](releases/current/)

Current is **v0.3.9 / FIELD_VALIDATION**.

### Human adopter

Start with [`releases/current/ADOPTER-QUICKSTART.md`](releases/current/ADOPTER-QUICKSTART.md).

### Agent runtime

The **only default resident ENA text** is:

[`releases/current/RUNTIME-ADOPTION-KERNEL.md`](releases/current/RUNTIME-ADOPTION-KERNEL.md)

Cue routing, HOWs, enforcement classification, fixtures, references, Constitution detail, and research lineage are retrieved only when the current decision needs them.

```text
AVAILABLE_RESOURCE != DEFAULT_HOT_PAYLOAD
DEFAULT_AGENT_HOT_PAYLOAD = RUNTIME-ADOPTION-KERNEL.md
```

ENA is not one giant prompt and does not require every bundled reference or private implementation name.

## Current product direction

v0.3.9 is an R0 adoption-surface successor to v0.3.8. It does not add Constitution IDs or rewrite core machine semantics.

It closes two field findings from Issue #208:

- the v0.3.8 first-use wording still made several cold resources look like a default load list;
- root and zh-CN adopter-facing narration could still retain stale release identity even when `releases/current/` had moved.

The Current validator now checks the single hot-payload contract and release/adoption identity across root and zh-CN entry surfaces.

## Project work

Live project state: [`NOW.md`](NOW.md)

Current field stream: GitHub Issue **#208**.

The only currently planned fresh-session mechanism experiment is **Metamemory Update Policy v1**. It does not block product successors.

Old plans, handoffs, candidate records, prototype workflows, adjudications, and research artifacts remain cold lineage. Retrieve them only when a concrete question requires them.

## Repository shape

- adoption truth: `releases/current/`
- live project/research status: `NOW.md`
- open field work: GitHub Issues
- change history: Git / Pull Requests
- detailed evidence/research: relevant `research/` or `evidence/` artifact

```text
RESEARCH_LINEAGE != ADOPTION_PAYLOAD
IMMUTABLE_VERSION != IMMOBILE_CURRENT
SOFT_GUIDANCE != HARD_ENFORCEMENT
```

## Participate

ENA is intended to be questioned, falsified, specialized, partially adopted, and improved. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

Apache License 2.0. See [`LICENSE`](LICENSE).
