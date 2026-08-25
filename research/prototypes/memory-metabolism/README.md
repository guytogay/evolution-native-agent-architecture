# Memory Metabolism Reference Prototype

Status: `RESEARCH_PROTOTYPE / NOT_CURRENT_BASELINE / NOT_AUTHORITY / NOT_RELEASE_CANDIDATE`

Related: #73, #80.

This prototype turns the Memory Metabolism research direction into a small falsifiable contract. It does **not** prescribe a universal memory database, vector store, graph engine, prompt format, or Agent framework.

The target property is:

> **A finite active decision surface should be able to recover relevant durable state and continue learning from effectively unbounded experience without letting compression, retrieval, or persistence silently upgrade truth or authority.**

The prototype deliberately starts below LLM behavior. If a failure is structurally reachable in the memory contract, no multi-model experiment is required to prove reachability.

---

## 1. Core reframing

Do not optimize for:

`more remembered episodes -> larger active memory`

Prefer:

`more experience -> denser durable structure -> bounded active decision surface`

Working thesis from #73:

> **Memory is not preservation of experience. Memory is persistent change caused by experience.**

A useful architecture therefore separates what happened, what is currently true, what has been learned, and what may actually authorize action.

---

## 2. Reference layers

The prototype uses six semantic layers. They are reference categories, not required storage products.

### `OPERATIONAL`

Short-lived current task/runtime state.

Examples: retry count, current branch, temporary workaround, in-flight task state.

Operational state must not silently harden into long-term learning merely because it survived a session boundary.

### `EVIDENCE`

Provenance-bearing occurrence/observation records used to justify, challenge, or reconstruct durable conclusions.

Evidence is not the same as archive volume. A high-value evidence anchor may be cold but still decision-material.

### `KNOWLEDGE`

Retrievable beliefs, references, procedures, project facts, or organized knowledge.

Knowledge may be mutable or stale. Retrieval does not imply current truth.

### `COMPILED`

Experience that has changed future behavior: heuristics, risk models, preferences, policies, reusable decision structure.

Compiled memory is not a raw event log.

### `IDENTITY`

Durable identity/continuity-critical state when an implementation chooses to represent it in the same substrate.

This prototype does not define personhood or metaphysical identity. It only prevents an identity mutation from being treated as an ordinary ungoverned compaction side effect.

### `ARCHIVE`

Cold historical material, including evidence that has been lawfully redacted/minimized into a residual/tombstone form where appropriate.

Archive is a retrieval-priority/lifecycle concept, not permission to rewrite occurrence truth.

---

## 3. Two different objects: Memory Set and Decision Projection

### Memory Set

Represents durable records and derivation/provenance relationships.

It answers:

- what exists;
- what layer it belongs to;
- what it was derived from;
- what evidence supports/challenges it;
- what independent source roots exist;
- what access/validity constraints survive transformation.

### Decision Projection

Represents what a specific actor actually retrieved and used at one decision boundary.

It answers:

- what entered the decision surface;
- whether the actor was allowed to access it;
- whether mutable current-state memory was revalidated when consequence required it;
- whether real executable authority came from an external/current authority basis rather than from remembered text.

This preserves a central distinction:

> **Remembered != decision-visible != current-valid != authorized.**

---

## 4. Prototype invariants

These are research-prototype checks, not new ENA Constitution IDs.

### MM-P01 — Raw history is not compiled learning

A `COMPILED` record cannot itself be a raw `OCCURRENCE` or `TASK_STATE`.

If the durable change is merely “the event happened,” that belongs in evidence/history, not compiled behavioral structure.

### MM-P02 — Durable compilation retains lineage

A compiled record requires derivation/evidence lineage.

For decision-material compiled memory, a challenge path must reach `EVIDENCE` or `ARCHIVE`.

### MM-P03 — Memory cannot carry executable authority

The memory-record contract intentionally has no executable authority grant.

Memory may record observations/references about authority, but the action boundary must resolve current authority separately.

Short form:

> **Memory can remember authority; memory cannot mint authority.**

### MM-P04 — Operational state does not compile itself

Direct `OPERATIONAL -> COMPILED` transformation requires an evidence anchor.

This prevents transient state such as `retry_count = 3` from becoming a durable heuristic merely because it was present when a curator ran.

### MM-P05 — Transformation preserves source roots

Derived knowledge/compiled/identity records cannot silently drop known source roots.

Representation may compress; provenance independence may not be manufactured by compression.

### MM-P06 — Independent corroboration requires independent roots

Three summaries derived from one log are still one source family.

`INDEPENDENT_CORROBORATION` therefore requires at least two distinct represented source roots in this prototype.

This is intentionally structural: the prototype does not prove the roots are truly independent in the external world.

### MM-P07 — Explicit contradiction cannot disappear through consolidation

If selected source records explicitly declare a `CONTRADICTS` relation, a compiled output must represent conflict handling.

The contract does not decide the correct resolution. It prevents silent unconditionalization.

### MM-P08 — Mutable state is revalidated at consequential use

A memory record may mark `revalidate_before_material_use = true`.

If such a record is used in a `MATERIAL` decision projection, the projection must record revalidation.

This implements:

> **Retrieve -> Revalidate -> Act**

without imposing a universal TTL.

### MM-P09 — Access scope survives relevance

A relevant memory that is outside the actor's access scope must not enter legitimate use merely because retrieval similarity is high.

`relevant != authorized_to_read`.

### MM-P10 — Memory is not executable authority at the action boundary

When a decision requires authority, `external_authority_basis` must not be the ID of a memory record.

A remembered approval, policy statement, or prior mandate may trigger re-resolution; it is not the live authority object.

### MM-P11 — Identity mutation is not ordinary compaction

A represented `IDENTITY` mutation requires an explicit governance/change reference in the prototype.

This does not decide who ultimately owns purpose. It only prevents a memory curator from laundering a durable self-change through ordinary summarization.

---

## 5. What this prototype intentionally does NOT solve

It does not yet define:

- the best retrieval/ranking algorithm;
- vector versus graph versus SQL versus files;
- when one episode is sufficient for compilation;
- confidence arithmetic;
- universal freshness TTLs;
- automatic semantic contradiction detection;
- a universal ontology for identity/personhood;
- how much active memory is optimal;
- whether a particular LLM will naturally use the memory correctly;
- whether an implementation improves real task performance.

Those require different evidence.

---

## 6. Why the first tests are deterministic

The first question is not:

> “Will GPT/Claude/Hermes remember correctly?”

It is:

> “Does the proposed contract itself permit a false-confidence or authority-laundering path?”

If a path is statically reachable once, reachability is established. Repeating the same structural failure across many LLMs adds little epistemic value.

Only after the contract survives structural falsification should a real Host be used to discover unanticipated integration/behavioral failures.

---

## 7. Current selftest families

`validate_memory_metabolism.py --selftest` currently covers:

1. valid compiled memory with evidence lineage;
2. raw occurrence mislabeled as compiled memory;
3. compiled memory with no lineage;
4. executable-authority field smuggled into memory;
5. operational state compiled without evidence anchor;
6. one root falsely claimed as independent corroboration;
7. two distinct represented roots accepted structurally;
8. contradictory derivation without conflict handling;
9. contradiction with explicit handling;
10. source-root loss during compression;
11. material use of mutable state without revalidation;
12. same use after represented revalidation;
13. memory record used as executable authority basis;
14. access-scope violation;
15. identity mutation without governance/change reference;
16. identity mutation with explicit governance/change reference.

Passing these checks does **not** prove memory quality, external source authenticity, real independence, truthful semantics, or behavioral improvement. It only narrows a set of structural false-claim paths.

---

## 8. Next falsification targets

Before asking other Agents to participate, prefer deterministic work on:

- lawful evidence redaction/tombstones without destroying challengeability;
- supersession chains and stale belief resurrection;
- dependency-aware retrieval versus similarity-only retrieval;
- unknown-known representation: relevant cold material exists but the actor does not know to retrieve it;
- projection omission: all projected statements are true, but a decision-material memory is omitted;
- compiled-memory rollback: revert bad heuristic without pretending its historical evidence never existed;
- support-root independence laundering through multiple transformation generations;
- context budget pressure: selection of what to project when several valid memories compete.

Use another Agent only when independent interpretation or heterogeneous Host behavior can plausibly change the conclusion.

---

## 9. Relationship to Current

This prototype is a recomposition of properties already present across ENA v0.3.6, especially memory class isolation, canonical-history/derived-knowledge separation, scoped trust, uncertainty, pruning/archive, continuity, and Hot/Cold retrieval semantics.

It does not currently justify:

- a new Constitution invariant;
- a new universal capability ID;
- a new Current release;
- changing `releases/current/` in place.

A future ENA change should be justified only if this prototype exposes a decision-material property that Current cannot already express or if field evidence shows an existing property cannot be implemented without unacceptable ambiguity/friction.

> **Preserve experience truth. Compile behavioral value. Retrieve selectively. Revalidate mutable reality. Never let memory manufacture authority.**
