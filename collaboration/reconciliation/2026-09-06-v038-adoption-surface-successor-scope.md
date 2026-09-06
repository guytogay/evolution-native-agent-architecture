# v0.3.8 candidate.0 — Adoption-Surface Successor Scope

Date: `2026-09-06`

Status: `ACTIVE_CANDIDATE_SCOPE / NOT_CURRENT / NOT_FROZEN / NOT_RELEASED`

Candidate branch: `candidate/v0.3.8-candidate.0`

Candidate surface: `releases/v0.3.8-candidate/`

Current remains: `v0.3.7 / CURRENT / FIELD_VALIDATION`

## Why a successor exists

v0.3.7 established a materially better Operational Architecture without adding new Constitution IDs. Field use now shows that the remaining problem is not primarily missing Core law; it is that adopter-facing representation can still contradict release reality, lose decision-bearing meaning across projection, or force users to reconstruct too much project history.

The successor is therefore driven by **adoption/product-surface evidence**, not by a desire to manufacture new ENA theory.

Primary evidence inputs:

- GitHub Issue #201: post-release narration drift, zh-CN hot-surface fidelity omissions, concept-map misfit, semantic-fixture gaps, plus positive machine/tool verification;
- external Doubao review: useful ENA semantics were understandable locally, but the visible artifact mix made ENA appear more like nested legal/research prose than a deployable design method + rule library + test kit;
- direct follow-up inspection found an additional stale contradiction in `AGENT-ADOPTION-INSTRUCTION.md`: it is labeled CURRENT while telling the Agent not to report v0.3.7 as Current/frozen/released.

## Product thesis

```text
RESEARCH LINEAGE != ADOPTION PAYLOAD

SEMANTIC PRECISION != PRESENTATION VERBOSITY

SEMANTIC COMPLETENESS != RUNTIME CONTEXT COMPLETENESS

CORRECT ROUTING != CORRECT ADOPTION DECISION
```

v0.3.8 candidate.0 should preserve the semantic protection earned by ENA while requiring an adopter to know less project history and making implementation/conformance boundaries easier to inspect.

Desired compile path:

```text
research + evidence + adjudication
-> canonical semantic contracts
-> minimal adopter/runtime surface
-> explicit enforcement classification
-> conformance fixtures/validators
-> cold HOW/reference retrieval
```

## In scope

### 1. Adopter-state consistency

No adopter-facing file may simultaneously describe the same package as both released Current and pre-freeze/not-current candidate.

Candidate.0 itself must be unambiguous:

```text
v0.3.8-candidate.0
NOT_CURRENT
NOT_FROZEN
NOT_RELEASED
```

Historical release/candidate narration remains in lineage/history, not in the hot adopter decision path.

### 2. Minimal human entry surface

Add a short human-facing Quickstart answering:

- what ENA is for;
- what an adopter actually loads/uses;
- what remains cold/on-demand;
- what is machine-enforced vs model-guidance vs external-system responsibility;
- how to run conformance checks;
- where to inspect evidence/lineage only if needed.

Ordinary adoption must not require reading `research/`, handoffs, adjudications, or candidate history.

### 3. Explicit enforcement boundaries

Provide a compact machine-readable enforcement map distinguishing at least:

- `MODEL_CUE` — semantic/reasoning guidance that can fail under model behavior;
- `MACHINE_GUARD` — locally executable schema/validator/tool invariant;
- `EXTERNAL_CONTROL_REQUIRED` — fact/permission/effect that cannot be established by model narration or package bytes alone;
- `FIELD_EVIDENCE_REQUIRED` — salience, Host fitness, language behavior or other empirical behavior not guaranteed by static packaging.

The map must not pretend every ENA rule has a hard-code implementation.

### 4. zh-CN decision-bearing fidelity

Repair the v0.3.7 omissions identified in Issue #201 when ported into the successor:

- migration vs local validation;
- local validity/improvement vs composed outcome;
- cancel vs rollback vs compensation;
- durable object existence vs loaded bytes vs available semantics;
- restore/resume vs complete history vs restored authority;
- rescue-path narrow-authority guardrail;
- evidence-and-lineage control-retirement guardrail;
- environment-scoped selection qualifier;
- reputation not self-minting authority;
- missing Reference Index step where decision-bearing routing requires it.

Projection wording may differ; decision meaning may not silently shrink.

### 5. Retrieval/concept-map correction

Repair the Issue #201 map problems without expanding the Constitution:

- move or cross-map `ENA-CON-035` to a family where availability/freshness semantics are retrievable;
- broaden `ENA-CON-008` trigger cues so compaction/reclassification/append-only-in-meaning applicability is not reduced to secret/privacy payloads;
- surface `ENA-CON-028` imported/transformed evidence provenance in portability/migration retrieval where material.

`compress loaded text != compress applicability` remains the governing rule.

### 6. Conformance fixture expansion

Add dedicated paired semantic cases for currently uncovered high-value distinctions, including:

- local success != universal fitness / survival != moral correctness / environment-scoped selection;
- composition/emergence;
- cancel != rollback != compensation;
- runtime routing/salience, memory metabolism and projection/compaction routes where coverage claims list them.

Fixture presence remains a test definition, not behavioral proof.

### 7. Preserve v0.3.7 positive evidence

Do not rewrite working mechanisms merely because the presentation layer changes.

Issue #201 positively verified, among other things:

- v2 evolution-tool round-trip;
- invalid-record rejection;
- receiver-local selection not minted from source selection;
- digest tamper rejection;
- validator selftests;
- operational route closure;
- bundled-reference path/optionality consistency;
- stable inherited Constitution bytes.

These are regression obligations for the successor where applicable.

## Out of scope by default

- adding Constitution IDs merely to justify a new release;
- turning current evolutionary-memory research into Core law before its evidence warrants that;
- hiding or deleting research/lineage history;
- claiming prompt text alone creates safety;
- translating every canonical machine artifact into a second implementation;
- requiring adopters to use ENA-private implementation names where an equivalent Host-native mechanism preserves the property;
- silently changing `releases/current/` while candidate.0 is under development.

## Relationship to Metamemory Update Policy v1

Metamemory Update Policy v1 remains the preregistered final active mechanism experiment for the current evolutionary-memory round.

Candidate.0 may proceed in parallel because its immediate scope is already justified by field/adoption defects in v0.3.7.

A later Metamemory result may affect v0.3.8 only if it independently earns a decision-changing product/semantic implication before candidate freeze. It is not required to invent a v0.3.8 delta.

## Candidate acceptance questions

Before freeze, candidate.0 must answer:

1. Can an ordinary human identify what to use without reading research history?
2. Can an Agent distinguish candidate/release state without contradictory narration?
3. Can an adopter identify which protections are model cues, machine guards, external controls, or field claims?
4. Does zh-CN preserve decision-bearing hot semantics rather than just approximate wording?
5. Do fixtures cover the high-value semantics claimed by the hot/adoption surfaces?
6. Does the package remain useful without forcing every bundled reference or private implementation name?
7. Did product simplification preserve the v0.3.7 semantic trunk and positive machine behavior?

## Stop rule

Do not grow candidate.0 into a general rewrite.

When the identified adoption defects are repaired, the product surfaces are coherent, targeted machine checks pass, and new review no longer finds a decision-changing blocker in scope, stop adding polish and move to freeze/independent falsification.

```text
V0.3.8 SHOULD REQUIRE THE ADOPTER TO KNOW LESS
WHILE PRESERVING OR IMPROVING THE PROTECTION THEY ACTUALLY RECEIVE
```
