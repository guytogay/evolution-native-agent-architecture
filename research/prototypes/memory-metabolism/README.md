# Memory Metabolism Reference Prototype

Status: `RESEARCH_PROTOTYPE / NOT_CURRENT_BASELINE / NOT_AUTHORITY / NOT_RELEASE_CANDIDATE`

Related: #73, #80.

This prototype turns the Memory Metabolism research direction into a small falsifiable contract. It does **not** prescribe a universal memory database, vector store, graph engine, prompt format, or Agent framework.

The target property is:

> **A finite active decision surface should be able to recover relevant durable state and continue learning from effectively unbounded experience without letting compression, retrieval, restore, or persistence silently upgrade truth or authority.**

The prototype deliberately starts below LLM behavior. If a failure is structurally reachable in the memory contract, no multi-model experiment is required to prove reachability.

---

## 0. Prototype falsification log

### 0.1 Inline-provenance scaling failure

The initial sketch required every derived/compiled record to inline all inherited `source_roots`.

That looked safe for a two-record example but fails the original memory goal at scale:

`100,000 experiences -> one compiled heuristic -> 100,000 inline source roots`

The provenance rule would recreate unbounded historical baggage inside the compiled memory that was supposed to remain compact.

The property was therefore revised from:

> every compiled record must inline every source root

into:

> **provenance must remain traceable, but it may be preserved through cold indirection rather than repeated inline expansion.**

`provenance_sets` are the current research organ for that property. A compiled record may keep only a `provenance_ref`, while the larger root/evidence bundle remains cold and retrievable for audit, challenge, independence analysis, or reconstruction.

### 0.2 Superseded-memory resurrection failure

The next sketch could represent `B supersedes A`, but Decision Projection did not initially stop `A` from being reused as current state.

Even putting `A` in `revalidated_record_ids` would not solve the semantic problem: an old historical record should not silently become the present merely because reality is queried again or a snapshot is restored.

The refined property is:

> **Revalidation does not resurrect a superseded memory.**

If reality later returns to a value previously seen in `A`, represent fresh current evidence/belief. Preserve `A` as historical context rather than rewriting its temporal meaning.

This is especially relevant to rollback/restore:

`state restoration != knowledge/history restoration to an old truth surface`.

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

## 3. Three different objects

### Memory Set

Represents durable records and derivation/provenance relationships.

It answers:

- what exists;
- what layer it belongs to;
- what it was derived from;
- what evidence supports/challenges it;
- what supersedes it;
- what access/validity constraints survive transformation.

### Cold Provenance Set

Represents potentially large source-root/evidence lineage that need not be repeated inside hot/compiled memory.

It exists to preserve:

`bounded active memory + reconstructable provenance`

rather than forcing a false choice between the two.

### Decision Projection

Represents what a specific actor actually retrieved and used at one decision boundary.

It answers:

- what entered the decision surface;
- whether it is being used as current state or explicitly historical context;
- whether the actor was allowed to access it;
- whether mutable current-state memory was revalidated when consequence required it;
- whether real executable authority came from an external/current authority basis rather than from remembered text.

This preserves a central distinction:

> **Remembered != retrieved != decision-visible != current-valid != authorized.**

---

## 4. Prototype invariants

These are research-prototype checks, not new ENA Constitution IDs.

### MM-P01 — Raw history is not compiled learning

A `COMPILED` record cannot itself be a raw `OCCURRENCE` or `TASK_STATE`.

### MM-P02 — Durable compilation retains challengeable lineage

A compiled record requires derivation/evidence lineage.

For decision-material compiled memory, a challenge path must reach `EVIDENCE` or `ARCHIVE`, directly or through cold provenance indirection.

### MM-P03 — Memory cannot carry executable authority

Memory may record observations/references about authority, but the action boundary resolves current authority separately.

> **Memory can remember authority; memory cannot mint authority.**

### MM-P04 — Operational state does not compile itself

Direct `OPERATIONAL -> COMPILED` transformation requires evidence lineage.

Transient state such as `retry_count = 3` must not become a durable heuristic merely because it existed when a curator ran.

### MM-P05 — Transformation preserves provenance, not necessarily inline metadata

Derived knowledge/compiled/identity records cannot silently erase known source provenance.

They do **not** need to inline every source root. Cold `provenance_ref` indirection may preserve lineage.

> **Compression may reduce representation size without reducing epistemic traceability.**

### MM-P06 — Independent corroboration requires independent represented roots

Three summaries derived from one log are still one source family.

`INDEPENDENT_CORROBORATION` requires at least two distinct represented effective source roots, inline or through cold provenance.

This does not prove external-world independence.

### MM-P07 — Explicit contradiction cannot disappear through consolidation

If selected source records explicitly declare `CONTRADICTS`, a compiled output must represent conflict handling.

The contract does not decide the correct resolution. It prevents silent unconditionalization.

### MM-P08 — Mutable state is revalidated at consequential use

A record may mark `revalidate_before_material_use = true`.

If it is used in a `MATERIAL` Decision Projection, revalidation must be represented.

> **Retrieve -> Revalidate -> Act**

without a universal TTL.

### MM-P09 — Access scope survives relevance

Semantic relevance or retrieval rank must not override access scope.

`relevant != authorized_to_read`.

### MM-P10 — Memory is not executable authority at the action boundary

When authority is required, `external_authority_basis` must not be the ID of a memory record.

A remembered approval can trigger re-resolution; it is not the live authority object.

### MM-P11 — Identity mutation is not ordinary compaction

A represented `IDENTITY` mutation requires an explicit governance/change reference in the prototype.

This does not decide creator-versus-Agent sovereignty. It prevents durable self-change from being laundered through ordinary memory summarization.

### MM-P12 — Superseded memory remains historical unless a new current record is established

If a record has been superseded, a material Decision Projection may not use it as current state.

It may still be retrieved and used when explicitly marked as historical context.

Even represented revalidation does not automatically revive the old record:

> **Revalidation ≠ resurrection.**

If present reality now resembles an old state again, record fresh current evidence rather than rewriting the old temporal claim.

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
- whether an implementation improves real task performance;
- how a huge cold provenance set should itself be compressed (graph index, Merkle structure, digest + retrievable expansion, etc.);
- how a restored snapshot discovers a superseding record that exists outside the restored local state.

Those require different evidence.

---

## 6. Why the first tests are deterministic

The first question is not:

> “Will GPT/Claude/Hermes remember correctly?”

It is:

> “Does the proposed contract itself permit a false-confidence, provenance-erasure, stale-state, or authority-laundering path?”

If a path is statically reachable once, reachability is established. Repeating the same structural failure across many LLMs adds little epistemic value.

Only after the contract survives structural falsification should a real Host be used to discover unanticipated integration/behavioral failures.

---

## 7. Current selftest families

`validate_memory_metabolism.py --selftest` currently covers 24 deterministic cases:

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
16. identity mutation with explicit governance/change reference;
17. compact compiled memory using cold provenance indirection;
18. incomplete cold provenance detected as provenance loss;
19. independent corroboration through cold provenance;
20. multi-generation provenance laundering;
21. multi-generation cold provenance preservation;
22. revalidation attempting to resurrect a superseded current-state record;
23. explicit historical use of a superseded record;
24. use of the current replacement after its own required revalidation.

Passing these checks does **not** prove memory quality, external source authenticity, real independence, truthful semantics, or behavioral improvement. It only narrows structural false-confidence paths.

---

## 8. Next falsification targets

Before asking other Agents to participate, prefer deterministic work on:

- lawful evidence redaction/tombstones without destroying challengeability;
- restore/rollback where the superseding evidence lives outside the restored snapshot;
- unknown-known representation: relevant cold material exists but the actor does not know to retrieve it;
- truthful projection with decision-material omission;
- compiled-memory rollback without rewriting historical truth;
- dependency-aware retrieval versus similarity-only retrieval;
- context-budget competition among several valid memories.

Use another Agent only when independent interpretation or heterogeneous Host behavior can plausibly change the conclusion.

---

## 9. Relationship to Current

This prototype is a recomposition of properties already present across ENA v0.3.6, especially memory class isolation, canonical-history/derived-knowledge separation, scoped trust, uncertainty, pruning/archive, continuity, restore semantics, and Hot/Cold retrieval.

It does not currently justify:

- a new Constitution invariant;
- a new universal capability ID;
- a new Current release;
- changing `releases/current/` in place.

A future ENA change should be justified only if this prototype exposes a decision-material property that Current cannot already express or if field evidence shows an existing property cannot be implemented without unacceptable ambiguity/friction.

> **Preserve experience truth. Compile behavioral value. Retrieve selectively. Revalidate mutable reality. Do not resurrect superseded truth. Never let memory manufacture authority.**
