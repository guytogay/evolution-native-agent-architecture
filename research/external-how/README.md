# ENA External HOW Research

Status: `ACTIVE_EXTERNAL_MECHANISM_HARVEST / RESEARCH_ONLY / OPEN_CARDINALITY`

Purpose: find concrete tools, workflows, protocols, runtime mechanisms, operational patterns, and implementation ideas outside ENA that may become candidate HOW branches.

ENA should not invent every organ from scratch when mature mechanisms already exist elsewhere.

At the same time:

```text
POPULAR_EXTERNAL_PATTERN != ENA_BEST_PRACTICE
VENDOR_CLAIM != INDEPENDENT_EVIDENCE
ANALOGY != ARCHITECTURAL_NECESSITY
```

External mechanisms become useful only after mapping them to an ENA failure model and Host conditions.

## Canonical files

- `SOURCE-REGISTRY.md` — durable source/mechanism registry and current ENA mapping.
- `harvests/` — dated research passes preserving what was observed at that time.

Future focused files may be added by topic when one source family becomes large enough to justify its own surface. Do not preallocate a fixed topic taxonomy.

## Source classes

Useful sources may include:

- official agent framework/runtime documentation;
- AI memory systems;
- durable workflow/orchestration systems;
- agent-to-agent protocols;
- AI lab engineering/research publications;
- peer-reviewed/preprint research;
- open-source implementations/issues;
- AI developer communities and field reports;
- adjacent distributed-systems, security, identity, database, and networking practice.

Community discussion is valuable for discovering failure modes and implementation tricks, but should normally be tagged as weaker/experience evidence unless independently verified.

## Required record shape

For a material external mechanism, record:

```text
SOURCE
DATE OBSERVED
EVIDENCE CLASS
MECHANISM
ENA WHAT/WHY OR FAILURE MAPPING
CANDIDATE HOW
HOST/APPLICABILITY CONDITIONS
LIMITATIONS / CONFLICTS
DECISION-CHANGING EVIDENCE STILL NEEDED
STATUS
```

The fields are a working template, not an ontology.

## Research workflow

```text
ENA gap / recovered WHAT-WHY
-> search external systems
-> observe concrete mechanism
-> preserve source/date
-> map to ENA failure model
-> compare with existing HOW branches
-> retain as candidate / specialization / counterexample
-> static falsification where possible
-> reality contact only when it can pay epistemic rent
-> selection / coexistence / retirement
```

Do not collapse several materially different external mechanisms into a generic phrase such as "use durable execution". Preserve the mechanism details that change behavior.

> **Search widely; map concretely; select by evidence.**
