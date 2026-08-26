# ENA Research Methodology

Status: `CANONICAL_RESEARCH_METHOD_SURFACE / OPEN_CARDINALITY / NON_NORMATIVE_TO_CURRENT`

This directory is the durable home for **how ENA itself is researched**.

It is intentionally separate from:

- ENA adopter-facing Current semantics in `releases/current/`;
- reconstruction findings in `research/reconstruction/`;
- implementation prototypes in `research/prototypes/`;
- external HOW harvesting in `research/external-how/`;
- release/project execution planning in `research/plans/`.

A future session should not have to reconstruct the research method from old chat, Issues, comments, or implementation files.

## Read order

1. `ENA-RESEARCH-DISCIPLINE.md` — open-cardinality master methodology ledger.
2. `HOW-GROWTH-DISCIPLINE.md` — compression boundary: WHAT/WHY may abstract; HOW should concretize, branch, and remain plural where reality supports it.
3. `CARDINALITY-DISCOVERY-GUARD.md` — counts/categories are discovered unless the domain makes them normative.
4. `SESSION-CONTINUITY-AND-COLLABORATION.md` — cross-session inheritance and collaboration protocol.
5. `METHOD-CHANGELOG.md` — durable record of significant methodology changes and the evidence/incidents that caused them.

`research/RESEARCH-START-HERE.md` remains the small hot bootstrap that points here.

## Methodology status model

A methodology item may be:

```text
OBSERVED_FAILURE
CANDIDATE_METHOD
ACTIVE_WORKING_METHOD
REVISED
SUPERSEDED
RETIRED_WITH_LINEAGE
UNKNOWN
```

These states are descriptive research-process states, not ENA Constitution authority.

## Update discipline

When research reveals a new method defect or a better research discipline:

1. capture the triggering incident/evidence;
2. update the relevant methodology file or add a new focused method file if the distinction changes behavior;
3. record the change in `METHOD-CHANGELOG.md`;
4. update `research/RESEARCH-START-HERE.md` only when future-session routing must change;
5. do not compress a newly discovered method into an existing rule merely to keep the directory small;
6. do not split methods merely to make the directory look comprehensive.

```text
METHOD_COUNT = OPEN_CARDINALITY
METHOD_FILE_COUNT != METHODOLOGY_COMPLETENESS
```

## Core methodological shape

```text
TELOS / PURPOSE
      |
      v
WHAT / WHY
semantic trunk; abstraction may help
      |
      +--> HOW-A
      +--> HOW-B
      +--> HOW-C
      +--> ...
             |
             +--> Host bindings / tools / procedures / protocols
             +--> failures / fallbacks
             +--> evidence
```

> **Compress the semantic trunk; let concrete HOWs branch.**

> **Do not merely inherit conclusions. Inherit the method that governs how new conclusions may be produced.**
