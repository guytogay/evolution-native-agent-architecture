# Contribution — Viability Economics, Research Throughput, and ENA Overhead

```yaml
project: ena
artifact_type: CONTRIBUTION
status: UNRECONCILED
canonical_status: NOT_MAINLINE
promotion_status: NOT_PROMOTED
created_at: "2026-08-20T14:25:00+08:00"
participant:
  kind: ChatGPT
  role_this_contribution: SYNTHESIS_CONTRIBUTOR
  access_surfaces:
    github: WRITE
    google_drive: WRITE
relationship: SYNTHESIS_OF_EXISTING_SEMANTICS_AND_ACCUMULATED_RESEARCH
bridge_state:
  source_surface: GITHUB
  target_surface: GOOGLE_DRIVE
  status: PENDING
  semantic_delta: NONE
```

## Research question

Can ENA preserve viable agency if its own governance, validation, evidence, coordination, and model-routing overhead materially increases token spend, monetary cost, elapsed time, human attention, or project duration?

This contribution treats cost and time not as external inconveniences but as resources that condition future agency.

## Existing Mainline basis

This direction appears more likely to operationalize existing v0.2.11 semantics than to require a new Constitution principle:

- ENA-CON-038: governance exists to preserve viable agency and remain value-accountable;
- ENA-CAP-061: Governance Value & Applicability Contract distinguishes expected/observed benefit and friction;
- ENA-CAP-063: Governance Fitness can KEEP / SIMPLIFY / MERGE / DORMANT / RETIRE mechanisms based on whether they still justify their friction and produce protection, observability, learning, recoverability, trusted cooperation, or sustainable autonomy;
- v0.2.6: use the lightest governance that still matches consequence;
- v0.2.8: activation reality explicitly includes token budgets and model availability.

The unresolved question is whether cost/time/project-throughput are being measured strongly enough to prevent ENA itself from becoming an agency-destroying bureaucracy.

## Core framing

`Safe operation != Viable operation`

A system can be safer yet less viable if governance consumes the resources needed to perform useful work.

Candidate formulation:

> A control that preserves safety by exhausting the resources required for useful action can still destroy viable agency.

This applies at two scales:

1. **Mechanism scale** — an individual control or validator may cost more than the protection/value it produces in the current envelope.
2. **System/project scale** — individually defensible controls may compose into an ENA operating burden that slows projects, raises model spend, increases human coordination, or reduces useful throughput enough to make the whole system unfit.

`Local governance value != composed governance fitness.`

## Resource dimensions that may need explicit observation

Do not collapse these automatically into one score:

- model/API/token spend;
- monetary cost;
- wall-clock latency;
- human review/coordination time;
- number of required model calls / participants / handoffs;
- compute/storage/logging overhead;
- project lead time;
- useful task throughput;
- retry/rework cost;
- opportunity cost from delayed or abandoned work;
- cognitive/context burden;
- evidence-acquisition cost;
- governance-maintenance cost.

## Value dimensions to compare against burden

Again, keep multidimensional where practical:

- task/output value;
- prevented loss / reduced consequence exposure;
- recovery value;
- reduced rework;
- truthfulness / claim integrity;
- observability;
- reusable evidence produced;
- learning / future efficiency;
- resilience / availability;
- trusted cooperation;
- preserved future options.

## ENA overhead should be measured incrementally

A useful comparison is not simply total task cost. Distinguish:

```text
Base task cost
+ ENA incremental governance/validation cost
- avoided failure/rework/loss
- reusable evidence / future cost reduction
= observed net burden/value profile
```

But the baseline comparator must be honest: an unsafe baseline that looks cheap because it ignores rare catastrophic losses is not a valid proof that governance has negative value.

Use scenario-appropriate comparators and preserve uncertainty.

## Selection objective candidate

Do not maximize governance strength or evidence quantity.

Prefer:

```text
Minimize governance / validation burden
subject to:
- required truthfulness;
- risk-appropriate protection;
- recovery requirements;
- authority/consequence constraints;
- evidence sufficient for the decision actually being made.
```

This is compatible with:

> Use the lightest governance that still matches the consequence.

## Evidence acquisition is itself a governed economic activity

Evidence strength and evidence acquisition cost are independent axes.

Examples:

- a cheap deterministic hash/test can provide strong evidence;
- an expensive multi-hour LLM audit may still provide only bounded E2/E3 evidence;
- expensive does not imply strong;
- strong does not imply worth acquiring for every decision.

Candidate research heuristic:

```text
Validation ROI ~=
(decision-critical uncertainty reduced × probability result changes a material decision)
/
(token + money + elapsed time + human effort + operational risk + complexity)
```

Do not make this a single normative scalar yet; use it as a planning lens.

## Research throughput problem

ENA research itself must obey the same viability discipline.

Anti-pattern:

```text
one idea -> one prototype -> one DSH run -> one report
repeat daily
```

This produces high evidence cost, long lead time, and risk of overfitting ENA to one reference host.

Preferred research funnel:

```text
Broad idea intake / accumulated feedback
        ↓
Periodic synthesis into related hypothesis families
        ↓
V0 reasoning / consistency checks
        ↓
V1 static / mechanical checks
        ↓
V2 HAR + synthetic attacks
        ↓
V3 cheap/disposable model or host experiments
        ↓
Only surviving decision-critical questions
        ↓
V4 batched DSH reference-host campaign
        ↓
V5 independent host / real-world replication when justified
```

### Operational consequences

- Do not require every useful idea to receive immediate formal treatment.
- Accumulate variation cheaply.
- Synthesize many related observations at once.
- Reuse existing evidence through applicability checks.
- Batch DSH experiments so one baseline/host setup tests several competing hypotheses.
- Do not run an expensive experiment unless plausible outcomes can change a material decision.
- Reference-host testing should be milestone-driven, not daily ritual.

Candidate maxim:

> Batch variation; concentrate expensive selection.

## Runtime implications for Agent societies

ENA should evaluate not only whether a task route is safe/capable, but whether it is economically and temporally viable.

Example:

```text
Route A: expensive strong model only
Route B: cheap hallucination-prone model + deterministic validator
Route C: cheap multimodal model + strong reasoning model + validator
```

The preferred route depends on observed consequence, reliability, cost, latency, validation burden, and failure/rework cost.

A cheaper model may survive because governance allows its strengths to be used without granting unsupported attestation authority. Conversely, a nominally superior model may be a poor route when cost/latency exceeds its marginal value.

This supports ecological specialization rather than global model ranking.

## Failure conditions for ENA itself

Treat the following as possible ENA fitness failures, not merely usability complaints:

- token/API cost rises materially without proportional risk/value benefit;
- project lead time grows materially due to governance steps;
- human coordination/review becomes the dominant bottleneck;
- low-risk tasks receive high-assurance ceremony by default;
- evidence is repeatedly reacquired instead of reused when still applicable;
- safety mechanisms create more rework than the failures they prevent;
- multi-agent coordination overhead exceeds the cognitive diversity/value gained;
- governance artifacts proliferate faster than productive capability;
- Agent spends more effort proving work than doing work when consequence does not justify it;
- users bypass ENA because compliant paths are too expensive or slow;
- ENA makes a previously viable Agent/project economically non-viable.

Candidate maxim:

> ENA must pay rent at project scale, not only at control scale.

## Important counterpressure

Cost reduction must not become a loophole for dishonest under-governance.

A high-consequence irreversible action may rationally justify large validation cost and delay. The objective is not cheapest operation; it is **the least burden that honestly purchases the required protection and evidence**.

`Cheaper != better` when the cheaper route leaves a materially larger uncontrolled consequence envelope.

## Relationship to developmental stages

Do not automatically turn efficiency into another P0-P5 axis. Developmental stage remains maturity of the operating arrangement.

Instead, record operational sustainability / resource economics as a parallel fitness profile. A mature P3/P4 system can still be economically unfit; a lightweight P1 host can be economically excellent within a narrow consequence envelope.

## Candidate maxims — research only

- `Safe operation != viable operation.`
- `Resources are part of the future action space.`
- `A control that consumes the budget required for useful action can defeat its own purpose.`
- `ENA must pay rent at project scale, not only at control scale.`
- `Use the cheapest evidence that can honestly support the decision.`
- `Cheap falsification before expensive validation.`
- `No expensive experiment without a decision it can change.`
- `Batch variation; concentrate expensive selection.`
- `Evidence reuse is an efficiency mechanism, not an epistemic shortcut.`
- `Do not maximize evidence; acquire sufficient evidence for the consequence and claim.`

## Falsification pressure

Test whether this framing:

- causes under-validation of rare but catastrophic risks;
- over-rewards short-term token savings while hiding expected failure cost;
- creates a misleading single ROI score;
- makes human time look free;
- ignores latency-sensitive and deadline-sensitive project value;
- treats reusable evidence as universally applicable when its envelope has expired;
- causes premature retirement of controls whose value is mostly counterfactual/preventive;
- overfits to commercial API pricing that changes over time;
- undervalues learning effects that reduce future cost;
- becomes so elaborate that measuring ENA overhead itself creates material overhead.

## Current judgment

Likely classification:

`CLARIFICATION / OPERATIONALIZATION CANDIDATE` grounded in existing ENA-CON-038 and ENA-CAP-061..063, not evidence for a new Constitution principle.

The immediate practical change should be methodological rather than normative:

1. stop treating DSH as a daily validation ritual;
2. batch accumulated research into synthesis families;
3. use cheap falsification aggressively;
4. reserve DSH for decision-critical batched campaigns;
5. begin observing ENA-induced cost/latency/human-time/project-throughput overhead in future host evidence.

No ENA v0.2.11 Mainline change is authorized by this contribution.
