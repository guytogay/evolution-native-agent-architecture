# ENA Research Session Inheritance Gap — 2026-08-26

Status: `RESEARCH_PROCESS_INCIDENT / CONTINUITY_GAP / CURRENT_UNCHANGED / NOT_RELEASE_AUTHORITY`

## Incident

A successor ChatGPT session was asked to inherit ongoing ENA research. The previous session had already discussed, and GitHub had already preserved, key anti-dissolution methodology including:

- explanatory coverage is not operational solution;
- `Core semantic trunk` should remain thin without making the whole ENA thin;
- concrete reference organs and Host adapters remain research work even when no new Core semantic is needed;
- `Build enough organs to demonstrate that the property is actually inhabitable`;
- WHAT/WHY must lead to concrete HOW and EVIDENCE;
- plural HOW families were already represented in PR #82.

The successor session nevertheless moved into a "choose the highest-value next organ and deepen it" workflow and nearly reintroduced selection-induced ablation.

The user caught the regression before it became a new architecture assumption.

## Evidence from prior session

The prior conversation explicitly distinguished two product layers:

```text
ENA Semantic Core
-> WHAT / WHY
-> stable, simple, universal

ENA Operational Architecture
-> HOW
-> Reference Organs
-> Host Adapters
-> State Machines
-> Decision Procedures
-> Schemas
-> Playbooks
-> Examples
-> Failure Handling
-> Validation Fixtures
-> Field Evidence
```

It also explicitly stated that the operational layer may have multiple implementations, e.g. one Memory property branching into Hermes, OpenClaw, Codex, and generic reference organs.

The prior session ended by instructing the next work to recover all surviving and previously dissolved topics and reconstruct them through `WHAT -> WHY -> HOW -> EVIDENCE`, recording intermediate state in GitHub.

## Evidence from GitHub before the regression

Issue #88 already contained:

- `#80 remains useful ... for the Core semantic trunk`;
- `Build enough organs to demonstrate that the property is actually inhabitable`;
- `Abstract only after the concrete mechanism has survived meaningful reality contact`;
- explicit restored engineering families for Memory, Recovery, Settlement, Identity, Authorship, WAIT/STOP, Reputation, Ecology, language, adoption, tooling, and other concrete organs.

PR #82 already contained plural HOW families such as:

- Finite-Context / LITE Adoption plural HOW family;
- Distributed History Merge plural HOW family;
- explicit open-cardinality / anti-distortion language.

Therefore this was **not primarily a persistence failure**. Relevant durable state existed.

## Failure decomposition

### A. Prior-chat retrieval gap

The successor inherited a compressed session summary but did not first read the latest methodology-bearing tail of the prior exported conversation.

```text
PRIOR_CHAT_WRITTEN = YES
PRIOR_CHAT_RETRIEVED_AT_START = PARTIAL
```

The summary preserved anti-dissolution and WHAT/WHY/HOW/EVIDENCE, but not with enough salience as the active branching/selection-control rule.

### B. GitHub activation gap

The successor did inspect PR #82 and current reconstruction Issues, so durable GitHub information was retrieved.

However it was interpreted mainly as **project content** rather than as **research-control logic**.

```text
GITHUB_WRITTEN = YES
GITHUB_RETRIEVED = YES
GITHUB_INTERPRETED = PARTIAL
METHODOLOGY_SALIENT = INSUFFICIENT
METHODOLOGY_APPLIED = FAIL
```

This is a direct research-process instance of:

```text
WRITTEN != RETRIEVED != INTERPRETED != SALIENT != APPLIED
```

### C. Discoverability / canonical-entrypoint gap

The methodology was distributed across:

- Issue #88;
- Issue #89;
- PR #82;
- historical research Issues/comments;
- the prior conversation export;
- older collaboration-process documents.

There was no single small current research bootstrap saying:

> read this methodology first; treat it as an execution constraint before selecting new work.

Therefore:

```text
DURABLE != DISCOVERABLE
```

### D. Stale continuity-organ gap

`research/COLLABORATION-PROTOCOL.md` was intended to guide parallel sessions, but at incident review time it still hard-coded an old `v0.3.2` Current baseline and carried pre-anti-dissolution contribution questions such as "Is the problem already covered by current ENA semantics?" without the later correction that semantic coverage does not close organ engineering.

The artifact intended to preserve continuity had itself become stale.

### E. Action-selection bias

The successor treated "continue ENA" as a request to select the most valuable unresolved concrete problem and make progress immediately.

That produced:

```text
CURRENT_VISIBLE_GAP
-> PRIORITIZE
-> PROTOTYPE
-> NEXT_GAP
```

before sufficiently completing reconstruction of historical variation.

This creates a visibility feedback loop:

```text
already visible/prototyped HOW
-> receives more engineering
-> becomes more visible
-> appears more fundamental

unrecovered HOW
-> receives no engineering
-> remains less visible
-> risks silent disappearance
```

## Root cause

The root cause was not simply "context window too small".

It was a missing research-runtime bootstrap that binds durable project knowledge into future-session behavior.

The project had persistence, but insufficient **retrieval routing + salience + activation** for the research methodology itself.

In ENA terms, the project suffered the same class of gap it studies:

```text
KNOWN / WRITTEN
!=
RETRIEVED
!=
SALIENT
!=
APPLIED
```

## Corrective actions

1. Added `research/RESEARCH-START-HERE.md` as a small hot research bootstrap.
2. Keep the full open-cardinality methodology in `research/methodology/ENA-RESEARCH-DISCIPLINE.md` as the cold canonical working source.
3. Update `research/COLLABORATION-PROTOCOL.md` so it no longer hard-codes stale Current version state and so anti-dissolution/plural-HOW methodology is part of cross-session continuation.
4. Make PR #82 visibly point to the research bootstrap before substantive continuation.
5. Preserve the rule that prior-session handoff summaries are pointers, not substitutes for the latest methodology-bearing durable sources.
6. When a prior conversation export exists and recent methodology changed near session end, inspect the tail before selecting work.
7. Treat methodology inheritance as successful only when the successor **acts consistently with it**, not when it can merely paraphrase it.

## No-overcorrection rule

Do not solve this incident by forcing every future session to load all ENA history.

The desired architecture is Hot Cue + Cold Capability:

```text
small research bootstrap
-> exact methodology / ledger / workstream routing
-> relevant cold retrieval
-> current action
```

not:

```text
load entire repository and every prior chat into context
```

The continuity mechanism must itself pay context/complexity rent.

## General lesson

> **Recording knowledge prevents erasure; it does not guarantee inheritance.**

> **A research methodology needs its own runtime adoption path.**

> **Do not merely inherit conclusions. Inherit the method that governs how new conclusions may be produced.**
