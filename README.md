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

Current is **v0.3.13 / FIELD_VALIDATION**.

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

If the live question is **“how do I improve/evolve myself over time?”**, retrieve:

[`releases/current/operational/procedures/EVOLUTION-LOOP.md`](releases/current/operational/procedures/EVOLUTION-LOOP.md)

The loop is Host-neutral: signal/inbox -> latent candidate -> bounded trial -> before/after evidence -> local selection -> integrate/retain/dormant/reject/archive -> relevant wake.

After adoption, and after a material Host/runtime change, Current also asks for one bounded local operationalization pass: identify which applicable ENA boundaries are already covered by Host-native controls; where a real gap exists, propose the smallest cheap/reversible local mechanism that could materially change or protect a decision. This is not a request to install every ENA mechanism.

```text
SEMANTIC_ADOPTION != LOCAL_OPERATIONALIZATION
LOCAL_OPERATIONALIZATION != INSTALL_EVERY_CONTROL
EVOLUTION_VOCABULARY != EXECUTABLE_EVOLUTION_LOOP
PROTECTION_OF_EVOLVABILITY != EVOLUTION_ITSELF
```

ENA is not one giant prompt and does not require every bundled reference or private implementation name.

## Current product direction

v0.3.13 is an R1 operational successor to v0.3.12, driven by adopter reality contact rather than a new Constitution law.

It closes two related field gaps:

- `F-208-07`: the owner first questioned whether ENA lacked support for helping the Agent itself evolve. That question caused a DSH Agent to inspect its real LXC Host; the Agent then proposed rescue/canary + durable variation ledger + lightweight baseline organs and implemented them after owner authorization. This shows that semantic adoption had not made local operationalization sufficiently salient; it does **not** mean the owner designed the organs or that every Host needs the same kit.
- `F-208-08`: multiple Agent/adopter feedback, confirmed by Current inspection, showed that ENA named evolution capabilities and lifecycle semantics more strongly than it explained **how an Agent should actually keep evolving**. Capability names such as Evolution Inbox / signal capture / Variation Space / outcome-based selection existed, while the English Current HOW surface compressed `OA-EVO-01` to a short summary and `ena_evolve_v2.py` remained a narrow latent-record/migration helper rather than a full lifecycle engine.

The correction adds:

- an adoption-time / material-Host-change operationalization cue;
- a first-class runtime cue for “how do I evolve?”;
- a Host-neutral `Minimum Evolution Loop` cold HOW;
- explicit routing from Cue Index / HOW Map / Reference Index to that procedure;
- English + zh-CN evolution-loop projection;
- explicit honesty that the bundled `ena_evolve_v2.py` is narrow and does not itself constitute a complete self-evolution runtime.

No Constitution IDs or core machine/evolution schemas are changed. Host-native implementations remain plural; continuous self-editing, one universal metric, one scheduler, and install-every-control behavior are explicitly not required.

## Project work

Live project state: [`NOW.md`](NOW.md)

Current field stream: GitHub Issue **#208**.

The evolutionary-memory mechanism-discrimination campaign is closed. No mechanism experiment is active by default; new research must earn its own discriminator.

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
