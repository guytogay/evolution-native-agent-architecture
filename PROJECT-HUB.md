# ENA Project Hub

Status: `PROJECT_ENTRYPOINT / CURRENT`

Project: **Evolution-Native Agent Architecture (ENA)**

This is the stable entrypoint for any participant asked to adopt, use, continue, review, research, experiment on, or contribute to ENA.

## Current adoption state

Current complete adoption baseline: **ENA v0.3.2**

Status: `FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE / NOT_MAINLINE`

Version identity and maturity are separate. For any new or refreshed ENA adoption, use only:

`releases/current/`

Do not compose the current baseline with older ENA releases, candidates, research artifacts, or branches. Older versions remain historical lineage through Git and maintainer recovery storage; they are not runtime dependencies.

An adopter should be able to state simply:

`ENA baseline: v0.3.2`

## First-read order

### LITE — bounded low-consequence work

1. `releases/current/00-READ-ME-FIRST.md`
2. `releases/current/01-CONSTITUTION.md`
3. `releases/current/LITE-ADOPTION-INSTRUCTION.md`
4. Retrieve only the contract sections triggered by the task.

### STANDARD / HIGH_ASSURANCE

1. `releases/current/README.md`
2. `releases/current/00-READ-ME-FIRST.md`
3. `releases/current/02-SELF-POSITIONING-AND-LOCAL-PROJECTION.md`
4. `releases/current/01-CONSTITUTION.md`
5. Only the current-version contracts/capabilities needed for the task and consequence envelope.
6. Search project research/evidence/history only when a question, failure, contribution, or deeper rationale makes it useful.

Machine-readable current-version pointer:

`releases/current/CURRENT-BASELINE.yaml`

> Open knowledge does not mean always-loaded knowledge.

## Knowledge and participation

ENA project knowledge, evidence, research, lineage, and open questions in this repository are readable to repository participants. Any participant may, within actual capability and authority, read, question, critique, research, experiment, and contribute.

Useful contribution classes include:

`INCIDENT | NEAR_MISS | FRICTION | VALUE_OBSERVED | COUNTEREXAMPLE | PORTABILITY_FINDING | NEW_VARIATION | EVIDENCE_RESULT | RESEARCH_HYPOTHESIS | CRITIQUE`

Contribution guidance:

- root `CONTRIBUTING.md`
- `releases/current/CONTRIBUTION-PROTOCOL.md`
- `releases/current/templates/field-experience.v1.yaml`
- GitHub contribution artifacts: `collaboration/inbox/`
- Reconciliation artifacts: `collaboration/reconciliation/`

For trackable bugs, enhancements, research questions, or release concerns, prefer a GitHub Issue when it is the smallest useful durable tracker.

`Contribution != Reconciliation != Promotion != Mainline Authority.`

> Knowledge is commons. Inquiry is open. Authority is scoped. Adoption is governed.

## Shared baseline, local projection

All adopters use the same v0.3.2 semantics. Different hosts may have different Active Governance Sets only because actual host reality and declared applicability differ.

Host preference does not create a different baseline. Temporary cognitive/operating mode does not create a different role or authority envelope.

> Local projection may differ; baseline semantics must not drift silently.

## ENA narrow waist

Keep universal semantics focused on the properties required for truthful, viable interoperability. Host/model/tool/cognitive/organizational implementations may differ without being translated into one universal control plane.

> Standardize the property; discover the organ.

> Universal semantics != universal implementation burden.

## Persistent project surfaces

### GitHub

Repository: `guytogay/evolution-native-agent-architecture`

GitHub is the canonical engineering, research-lineage, and current-adoption surface.

- Current adoption baseline: `releases/current/`
- Evolution Inbox: `research/evolution-inbox/`
- Historical Adversarial Replay: `research/adversarial-replay/`
- Experiments: `research/experiments/`
- Prototypes: `research/prototypes/`
- Contributions: `collaboration/inbox/`
- Reconciliation: `collaboration/reconciliation/`
- Decisions: `decisions/`

### Maintainer recovery mirror

The maintainer may keep private durable backup/recovery copies of project artifacts. Those coordinates are intentionally not part of the public project metadata.

The private recovery mirror:

- is not required to read or adopt ENA;
- is not a second canonical runtime/adoption version;
- does not silently synchronize with GitHub;
- does not grant promotion authority to anyone who can access it.

## Persistent collaboration rules

- project-first, not Agent-first;
- persistent project state is the collaboration bus;
- tool access is connectivity, not project authority;
- one substantial contribution should normally be one independent artifact;
- contribution and reconciliation are separate;
- conflicts remain visible until evidence/authorized decision resolves them;
- persistence is not synchronization;
- project continuity does not depend on one permanent owning session/Agent.

GitHub write capability does not grant promotion, Mainline, deployment, remediation, or scope-expansion authority.

## Current field-validation posture

v0.3.2 is intended for real bounded adoption and heterogeneous field validation.

Current high-value observation areas include:

- LITE adoption cost/outcome versus STANDARD;
- Claim ↔ Evidence provenance independence and closure;
- Authority/subject/mandate lifecycle;
- effect identity, retry, replay, failover, cancellation, and concurrency semantics;
- Recovery State ≠ Historical Time;
- Capability/Model/Route Binding;
- ENA friction, control-composition debt, and viability economics;
- Influence Integrity / ambient-authority misuse;
- local-projection portability;
- release/distribution parity;
- unexpected failure modes, counterexamples, or useful new mechanisms.

Current discipline:

> Falsify before formalize.

> Use the cheapest evidence that can honestly support the decision.

> Batch variation; concentrate expensive selection.

> Production before perfection; not production without evidence.

## Release rhythm

Problems and ideas are collected durably first. A new version is released when a coherent batch of changes justifies the integration/validation cost. Do not micro-release every small observation by default.

Research may branch. Adoption versions remain linear, flattened, and self-contained.

## Modification guardrails

Do not silently:

- report field-validation status as Mainline;
- compose Current with older ENA versions to create an undocumented baseline;
- weaken current baseline semantics because a host cannot implement a mechanism;
- treat schema PASS as semantic truth;
- turn field recurrence into automatic independent corroboration or Universal truth;
- promote a contribution merely because another participant proposed it;
- erase conflicting evidence for convenience;
- use a technically available write path as proof of mandate;
- treat a renewed credential as automatic renewal of the underlying mandate;
- retry/cancel/failover consequential effects without considering effect semantics.

The whole project may evolve. The currently adopted version must remain singular, legible, and evidence-backed.
