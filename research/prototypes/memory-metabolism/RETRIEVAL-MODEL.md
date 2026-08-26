# Retrieval Model — Unknown-Known and Decision-Material Omission

Status: `RESEARCH_PROTOTYPE / NOT_CURRENT_BASELINE / NOT_AUTHORITY`

Related: #73, PR #82.

## 1. Why storage correctness is not memory correctness

The current Memory Set + Decision Projection contract can validate records that were retrieved and used.

It cannot, by itself, detect the most important retrieval failure:

> **A decision-material memory exists, but the Agent does not know it should retrieve it.**

A projection may therefore contain only truthful, current, authorized information and still be misleading through omission.

Example:

- durable compiled memory: `production deployment requires maintenance-window check`;
- current endpoint belief: valid and revalidated;
- current deployment mandate: valid;
- Decision Projection retrieves only endpoint + mandate;
- deployment proceeds without ever retrieving the compiled maintenance-window lesson.

Nothing included in the projection is false.

The failure is:

`decision-material memory omitted before projection`.

This is an **unknown-known** failure, not ordinary forgetting.

---

## 2. Do not solve unknown-known by loading every memory cue

A naive repair is:

> keep an always-loaded cue/index entry for every durable memory.

That recreates the original scaling problem at the index layer:

`unbounded memory -> unbounded hot cue catalog`.

So the active surface must not contain a flat list of every record or every cue.

The desired architecture is hierarchical:

> **a small hot retrieval reflex that knows when and where to expand, not a compressed copy of every memory.**

---

## 3. Reference retrieval layers

### Layer R0 — Hot Retrieval Reflex / Cognitive BIOS

Very small, normally available at decision time.

It does not know all memory contents.

It knows enough to recognize broad situations where cold state may matter and how to expand context.

Candidate responsibilities:

- recognize consequential/irreversible/external-write decisions;
- recognize authority/mandate dependence;
- recognize mutable-current-state dependence;
- recognize repeated failure/correction signals;
- recognize unfamiliar or changed Host/tool/model/environment conditions;
- recognize when a durable project/domain store exists;
- know how to query or re-resolve that store;
- degrade honestly if retrieval is unavailable.

Examples of broad reflex routes:

`deployment/external-write -> deployment + authority + recovery memory domains`

`repeated failure -> compiled failure-pattern + prior recovery domains`

`current mutable endpoint -> current-state revalidation domain`

These are reference examples, not universal keywords.

### Layer R1 — Store / Domain Registry (meta-memory)

A compact map of what durable stores/namespaces exist and what kinds of questions they can answer.

It may know:

- domain/store identifier;
- broad applicability;
- access boundary;
- retrieval method/path;
- freshness characteristics;
- whether the store is available;
- where authoritative current state lives.

It should be possible for the Agent to distinguish:

- `I do not know`;
- `I have not looked`;
- `a relevant store exists`;
- `the relevant store is unavailable`.

This registry is **meta-memory**, not a mirror of the underlying knowledge.

### Layer R2 — Cold Catalog / Index

Potentially large, not normally resident in active context.

Maps a scoped query/context to candidate records or subdomains using whatever Host organ is locally fit:

- semantic/vector retrieval;
- graph traversal;
- exact key/entity index;
- keyword/search index;
- SQL;
- file hierarchy;
- tool-specific query;
- hybrid methods.

ENA should not standardize one retrieval algorithm.

### Layer R3 — Memory Records

Actual `KNOWLEDGE`, `COMPILED`, `EVIDENCE`, `ARCHIVE`, `IDENTITY`, or `OPERATIONAL` material selected for possible use.

### Layer R4 — Decision Projection

The bounded set actually entering the decision surface.

At this point existing prototype checks apply:

- access scope;
- current validity/revalidation;
- supersession;
- authority separation;
- evidence/provenance as needed.

---

## 4. Retrieval correctness pipeline

A useful diagnostic chain is:

`EXISTS`
→ `REGISTERED`
→ `INDEXED`
→ `RETRIEVABLE`
→ `CUED`
→ `SELECTED`
→ `PROJECTED`
→ `LOADED`
→ `INTERPRETED`
→ `SALIENT`
→ `APPLIED`
→ `OUTCOME`

Each transition can fail independently.

Examples:

### EXISTS but not REGISTERED

The knowledge store exists, but the hot/meta-memory layer does not know it exists.

### REGISTERED but not RETRIEVABLE

The Agent knows the store exists, but the retrieval tool/path is broken or unavailable.

### RETRIEVABLE but not CUED

The relevant task occurs, but the Hot Retrieval Reflex does not recognize the need to query the store.

This is the strongest form of unknown-known.

### CUED but not SELECTED

The store is queried, but ranking/index logic misses the relevant record.

### SELECTED but not PROJECTED

A relevant record is found but dropped during context construction/budgeting.

### PROJECTED but not SALIENT

The record is present in context, yet another instruction/memory dominates the actual decision.

### SALIENT but not APPLIED

The Agent can state the lesson but does not use it behaviorally.

The final outcome alone cannot identify which failure occurred.

---

## 5. Structural guarantees versus behavioral evidence

Some retrieval properties can be checked structurally:

- a durable store has a registered retrieval route;
- access scope is represented;
- decision-material records have discoverability/index metadata somewhere;
- a cold retrieval path exists;
- retrieval failure is not narrated as success;
- a material action can require revalidation after retrieval;
- hot state need not inline all cold memory/index entries.

But the central semantic question cannot be proven from schema alone:

> **Did the system recognize that this particular memory was relevant to this particular decision?**

That requires an evaluation oracle, naturalistic occurrence, adversarial task, or other behavioral evidence.

Therefore:

`structural retrieval path != retrieval recall`

and

`record present in context != behavioral salience`.

---

## 6. Proposed evaluation trace (not runtime requirement)

For tests/field evidence, a retrieval trace may record:

- decision/task context;
- relevant store(s) according to evaluator/oracle;
- stores registered to the Agent;
- cue/reflex activation;
- query issued;
- candidate records returned;
- records selected;
- records projected;
- records actually used;
- false-positive retrievals;
- false-negative retrievals;
- retrieval/tool failure;
- context cost;
- resulting action/outcome.

Important:

> `oracle_relevant_record_ids` belongs to **evaluation evidence**, not ordinary runtime memory.

The runtime Agent usually does not possess a perfect list of what it should have remembered. If it did, the unknown-known problem would already be solved.

---

## 7. Retrieval failure fallback

When the Hot Retrieval Reflex fires but cold retrieval fails, do not standardize one universal response such as `reload all ENA/memory`.

Use consequence-aware fallback:

- low-consequence/reversible/evidence-seeking work may continue with explicit uncertainty when the missing memory cannot plausibly change the material decision;
- material/high-consequence work should strengthen retrieval/re-resolution or abstain when the missing domain can change authority, recovery, consequence, or decision correctness;
- a Host with unreliable cold retrieval may legitimately keep more semantics hot if that is locally fitter;
- retrieval failure must not be narrated as successful memory application.

This reuses ENA's existing agency-preserving uncertainty rather than creating a permanent global block.

---

## 8. Key research hypothesis

The irreducible always-hot memory of a long-lived Agent may be smaller than a traditional “core memory file.”

It may primarily be:

> **a retrieval-and-governance reflex plus minimal continuity/current-scope state.**

In other words, the Agent need not permanently remember every lesson in active context.

It must reliably know:

- that relevant durable knowledge may exist;
- where to look;
- when not looking would be dangerous;
- how to interpret/revalidate what is retrieved;
- how to fail honestly when retrieval is unavailable.

This is the current candidate solution to the bounded-memory / unbounded-experience problem.

---

## 9. When another Agent becomes useful

A fresh independent Agent can now add epistemic value by attacking questions that are not exhaustively derivable from schema:

1. Does the R0/R1/R2/R3/R4 decomposition miss a distinct retrieval failure class?
2. Can a truthful projection still cause a material wrong decision in a way not represented above?
3. Does the proposed Hot Retrieval Reflex create a new hidden always-hot scaling problem?
4. Can a Host preserve unknown-known detection without a permanent flat cue catalog?
5. Which parts are genuine ENA properties versus implementation organs?

This should be an adversarial architecture review, **not** a poll asking what memory design the Agent prefers.

> **The goal is not to make all memory hot. The goal is to make the path to relevant cold memory reliably hot enough.**
