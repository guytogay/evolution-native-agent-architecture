# 5A. v0.3.5 Operational Extensions and Clarifications

This file extends `05-CORE-OPERATIONAL-CONTRACTS.md` for the v0.3.5 candidate without changing the accepted v0.3.3 composed-validator implementation in section 5.13.

Where older wording can be read more broadly than the v0.3.5 Constitution, the v0.3.5 Constitution and this extension define the candidate semantics.

## 5A.1 History truth vs lawful payload retention

`occurrence truth preservation != permanent retention of every payload`

A recovery/history system must not use rollback, compaction, or redaction to falsely claim an event did not occur.

But secrets, personal data, regulated content, or legally expirable data may require minimization/redaction/deletion.

When lawful and useful, retain only a non-sensitive tombstone/provenance such as:

- an event occurred;
- sensitive payload was removed;
- removal authority/reason;
- references that remain lawful.

If law/policy prohibits even that residual, do not retain it merely for ENA.

## 5A.2 Variation Space and permission mutation

A consequential self-mutation enters a represented mutation boundary, but that does not imply a universal prior-approval step.

Inside a legitimate Variation Space, the Agent may be allowed to mutate:

- prompts/instructions;
- memory policy;
- skills/workflows;
- model/route;
- internal capability/permission topology;
- recovery/evaluation mechanisms where the space itself has adequate alternate recovery.

However:

`internal permission change != external mandate change`

Changing an internal ACL/configuration cannot create legitimate authority over an external Protected Subject that did not already follow from a real mandate.

## 5A.3 Outcome-based selection

A mutation is not an improvement claim at creation time.

Represent:

`variation -> experiment -> observed outcome -> selection`

Material outcome dimensions may include:

- task quality;
- reliability;
- latency;
- cost/resource use;
- user/project value;
- autonomy/agency;
- recovery quality;
- error modes;
- external side effects;
- maintenance burden;
- unknown/novel effects.

Do not require a universal scalar.

## 5A.4 Governance closure

Additional governance is justified when a bounded next action/check can plausibly change a material decision.

If all represented decision-changing questions are resolved/bounded and further review would only repeat already-known information, stop.

Reference outcomes:

- `READY`
- `NARROW_AND_PROCEED`
- `EVIDENCE_NEEDED`
- `STOP_OR_ESCALATE`

This vocabulary is an operational aid, not a global risk score.

## 5A.5 Composition and positive emergence

Composition-level revalidation is also composition-level exploration.

A new composition may cause:

`DEGRADE | NEUTRAL | ADDITIVE | SUPER_ADDITIVE | EMERGENT | MIXED | UNKNOWN`

Evidence of positive emergence is legitimate selection evidence.

Do not infer a positive emergent outcome merely because components were individually selected.

## 5A.6 Adaptation migration

A source adaptation may be transferred before universal equivalence is established.

Transfer should preserve source applicability and evidence.

At the receiver:

`TRANSFERRED != LOCALLY_APPLICABLE != LOCALLY_SELECTED`

Prefer differential validation of material source/receiver differences over mandatory full rediscovery.

## 5A.7 Continuity rather than metaphysical identity

For cross-session/model/Host/restore/clone decisions, track a Continuity Vector rather than forcing a binary same-Agent claim.

Use the dimensions needed to decide whether:

- knowledge/evidence still applies;
- authority remains current;
- adaptive state persisted;
- recovery lineage remains usable;
- language/Host/model changes require revalidation.

## 5A.8 Effective loaded surface

Persistence evidence must account for what the Host actually loads.

`DURABLE_OBJECT_EXISTS != RELEVANT_BYTES_LOADED != SEMANTICS_AVAILABLE`

Material factors may include:

- instruction-chain byte/token limits;
- precedence/order;
- truncation;
- selective skill loading;
- memory retrieval/index failure;
- routing/activation rules.

A globally persistent ENA bootstrap should be compact enough not to starve more specific project/task instructions.

## 5A.9 Language projection applicability

A translation/projection carries source lineage.

If language/model interaction can change a material decision, language is part of the evidence applicability envelope.

Cross-language semantic conformance is demonstrated by equivalent decisions/behavior on material fixtures, not by literal text similarity alone.
