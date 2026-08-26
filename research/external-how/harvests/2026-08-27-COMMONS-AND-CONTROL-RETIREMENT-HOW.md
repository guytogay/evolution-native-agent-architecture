# External HOW Harvest — Commons Substrates and Control Retirement

Status: `BOUNDED_EXTERNAL_HARVEST / RESEARCH_ONLY / NOT_SELECTION_PROOF`

Observed: 2026-08-27

Purpose: search for mature mechanisms only after Operational Architecture breadth audit exposed concrete execution-depth questions.

## Question A — should Evolution Commons use one Agent protocol?

### A2A Protocol

Official sources:

- https://a2a-protocol.org/latest/topics/key-concepts/
- https://github.com/a2aproject/A2A

Observed mechanisms:

- Agent Card capability/endpoint/skill discovery;
- Task lifecycle;
- Message vs Artifact separation;
- streaming/push updates;
- structured data/file/URL parts;
- authentication declared at the Agent interaction boundary.

Useful ENA mapping:

`ACTIVE_AGENT_DISCOVERY + TASK/ARTIFACT_EXCHANGE`

Important boundary:

A2A task/message history is not automatically a permanent Commons/provenance ledger. Active Agent coordination and durable publication remain separate.

### OCI Distribution

Official sources:

- https://github.com/opencontainers/distribution-spec/blob/main/spec.md
- https://specs.opencontainers.org/distribution-spec/
- https://opencontainers.org/posts/blog/2026-04-04-distribution-spec-conformance/

Observed mechanisms:

- content-type-agnostic distribution;
- push/pull;
- content discovery;
- content management;
- digest-addressed objects/blobs/manifests;
- tags as human-readable aliases;
- subject/referrer relationships for related content;
- conformance tooling explicitly split by workflow category.

Useful ENA mapping:

`DURABLE_CONTENT_ADDRESSED_COMMONS_SUBSTRATE`

Important boundaries:

```text
OCI_DIGEST != ENA_APPLICABILITY
REGISTRY_DISCOVERY != LOCAL_SELECTION
TAG != IMMUTABLE_IDENTITY
```

### Harvest conclusion A

Do not select one universal ENA transport.

Preserve the layered pattern:

```text
adaptation/evidence semantic carrier
        |
        +--> Git/repository Commons
        +--> OCI-style durable registry
        +--> object store + index
        +--> direct transfer

live Agent coordination
        |
        +--> A2A / Host-native task protocol
```

`ACTIVE_PROTOCOL != DURABLE_COMMONS`

---

## Question B — how do mature systems retire controls without deleting history blindly?

### LaunchDarkly feature-flag lifecycle

Official sources:

- https://launchdarkly.com/docs/home/flags/deprecate
- https://launchdarkly.com/docs/home/flags/archive
- https://launchdarkly.com/docs/home/flags/flag-lifecycle-settings

Observed mechanisms:

- lifecycle readiness separate from final deletion;
- deprecated state can hide an old control/flag while it remains evaluable;
- archive removes it from active lists while preserving restore/history;
- code references/dependencies are checked before archive/removal;
- restore remains possible after archive;
- lifecycle readiness criteria are configurable rather than one global age.

### Unleash feature-flag lifecycle

Official sources:

- https://docs.getunleash.io/guides/manage-feature-flags-in-code
- https://docs.getunleash.io/concepts/technical-debt
- https://docs.getunleash.io/guides/feature-flag-best-practices

Observed mechanisms:

- lifecycle moves toward Cleanup/Archived;
- stale state can be explicit without immediately changing runtime behavior;
- stale events can trigger automated cleanup workflows;
- code/old-path removal precedes archive;
- archive preserves audit/history;
- cleanup is treated as technical-debt management.

### Harvest conclusion B

Useful mechanism shape for ENA:

```text
identify original failure
-> inspect actual dependency/use/decision value
-> test replacement coverage
-> choose reversible de-escalation
-> retain rollback/wake path
-> archive lineage before deletion where useful
-> reactivate if failure returns
```

Do not transfer vendor-specific flag states as ENA ontology.

Do not infer:

```text
no recent activation -> safe retirement
old control -> obsolete control
new control exists -> old failure fully covered
```

This harvest supports a bounded Control Retirement procedure, not a universal machine schema.

`EXTERNAL_MECHANISM_EXISTS != ENA_SELECTION_PROOF`
`CURRENT_CHANGE = NO`
