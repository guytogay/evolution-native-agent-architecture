# Evolution Commons — Transport and Discovery HOW Patterns

Status: `REFERENCE_PATTERN_SET / RESEARCH_ONLY / NOT_CURRENT / OPEN_CARDINALITY`

Date: 2026-08-27

Parent node: `OA-MIG-01`

Current semantic anchor:

```text
PUBLISH -> DISCOVER -> IMPORT -> EXPRESS/EXPERIMENT -> LOCALLY_SELECT
```

This note exists because those semantic actions need concrete substrates, but they do not all need to be implemented by one protocol.

```text
ADAPTATION_PACKET
!= COMMONS_REGISTRY
!= AGENT_DISCOVERY
!= TASK_PROTOCOL
!= LOCAL_ADOPTION
```

## Decision cue

Use this pattern set when the problem is one of:

- publish an adaptation/evidence/variation so others can discover it;
- discover prior material without assuming it is locally valid;
- transfer a content-addressed adaptation packet/evidence bundle;
- ask another live Agent to perform work or return an artifact;
- preserve provenance/negative lineage while separating storage from active coordination.

Do not invoke a full Commons substrate for a purely local variation that is not being published or shared.

---

## HOW-A — Git / repository Commons

### Mechanism

Publish durable material as repository files, issues, PRs, release artifacts, or append-only research records.

Useful identities:

- commit SHA;
- tree SHA;
- file/blob digest;
- immutable release/tag where governed.

Discovery may use repository search, issue labels, indexes, registries, or known paths.

### Fits when

- inspectability and review matter more than high-throughput runtime exchange;
- human and Agent contributors share one project surface;
- historical diff/review lineage is useful;
- publication authority can be mapped to repository permissions/workflow.

### Residuals

- search quality may be weak;
- repo organization can become a discoverability bottleneck;
- Git identity does not prove external truth/applicability;
- publication permission does not imply receiver adoption authority.

---

## HOW-B — OCI-style content-addressed Commons

External relative: OCI Distribution Specification.

### Mechanism

Represent an ENA packet/bundle as generic registry content with:

- immutable content digest;
- manifest/descriptor metadata;
- namespace/repository scope;
- tags as mutable discovery aliases where useful;
- subject/referrer relationships for related provenance/evidence/attestation artifacts;
- push/pull/content-discovery/content-management API surface.

The ENA semantic payload may remain an adaptation packet or another typed artifact. OCI is the substrate, not the semantic definition.

### Fits when

- many publishers/receivers need a generic durable distribution API;
- content identity and deduplication matter;
- automated clients need pull/discovery;
- related evidence/provenance artifacts need discoverable references.

### Residuals

```text
DIGEST_MATCH != APPLICABILITY
REGISTRY_DISCOVERABLE != LOCALLY_SELECTED
TAG != IMMUTABLE_IDENTITY
REFERRER_EXISTS != EVIDENCE_TRUE
```

Registry authorization, privacy, retention and discovery policy remain environmental concerns.

---

## HOW-C — A2A active Agent discovery + task/artifact exchange

External relative: Linux Foundation A2A Protocol.

### Mechanism

Use Agent Card discovery to learn a live Agent endpoint/capabilities/skills, then use A2A Task/Message/Artifact lifecycle for active work exchange.

An ENA adaptation/evidence bundle may be attached/referenced as an Artifact or structured Part where appropriate.

### Fits when

- a live counterparty Agent is known/discoverable;
- the desired operation is delegated work, negotiation, clarification, streaming, callback, or active artifact production;
- both sides benefit from a task lifecycle rather than static repository publication.

### Does not replace

- long-term Commons storage;
- content-addressed historical registry;
- Commitment/Settlement semantics;
- current authority resolution;
- receiver-local evidence qualification.

A2A messages are not assumed to be a permanent critical-history ledger.

---

## HOW-D — Simple object store + explicit index

### Mechanism

Use an immutable/content-addressed object store plus a small searchable index that carries only discovery metadata and exact object identity.

Possible index dimensions:

- contribution/adaptation class;
- source environment/Host/model/language;
- semantic IDs/capabilities involved;
- creation/publication time;
- negative-evidence presence;
- applicability hints;
- controversy/unknown flags;
- exact content digest/URI.

### Fits when

- a full OCI/Git service is unnecessary;
- Host infrastructure already provides immutable objects + metadata query;
- operators want a thin Commons layer.

### Residuals

Index completeness/currentness remains an external trust boundary. Mutable index entries must not replace immutable source identity.

---

## HOW-E — Direct peer exchange without shared Commons

A publisher may send a packet directly to one receiver through an existing secure channel.

This is legitimate when population-level discoverability is unnecessary.

```text
DIRECT_TRANSFER != COMMONS_PUBLICATION
```

The receiver still performs local import/qualification/reselection.

---

# Common publish procedure

Regardless of substrate, a useful publication path is:

```text
1. identify publishable subject/content
2. resolve publication authority/confidentiality/Protected-Subject constraints
3. bind immutable/effective content identity
4. attach decision-material source/environment/negative lineage where required
5. publish through chosen substrate
6. read back discoverability/content identity where the publication claim matters
7. do not narrate publication as receiver adoption
```

# Common discovery/import procedure

```text
1. discover candidates through registry/index/Agent Card/repository/search
2. fetch exact immutable/effective content
3. preserve publisher/source identity and known provenance
4. classify applicability/required capabilities/negative evidence
5. import as candidate, not command
6. express/test only where locally justified
7. locally select/reject/recombine/keep unknown
```

# Selection rule

Choose the substrate according to environmental economics and interoperability needs.

```text
ONE_EVOLUTION_COMMONS_PROPERTY
-> 0..N_STORAGE_DISCOVERY_HOWS
-> 0..N_ACTIVE_COORDINATION_HOWS
```

Do not create a universal ENA registry merely for symmetry.

External references observed 2026-08-27:

- A2A latest concepts/specification: https://a2a-protocol.org/latest/topics/key-concepts/
- A2A specification repository: https://github.com/a2aproject/A2A
- OCI Distribution Specification: https://github.com/opencontainers/distribution-spec/blob/main/spec.md

`CURRENT_CHANGE = NO`
