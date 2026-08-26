# ENA Operational Architecture Cue Index

Status: `COMPACT_ROUTING_SURFACE / FIRST_PASS / OPEN_CARDINALITY / RESEARCH_ONLY / NOT_CURRENT`

Date: 2026-08-27

Parent map: `OPERATIONAL-ARCHITECTURE-MAP.md`

Evidence for this artifact: `TRAVERSAL-AUDIT-001.md`

## Purpose

This is a thin routing surface from ordinary problem language to the Operational Architecture map.

It exists because:

```text
NODE_CONTENT_TRAVERSABLE
!=
CUE_TO_NODE_DISCOVERABILITY_SOLVED
```

The index does **not** contain the full HOWs and should not become a second copy of the architecture.

```text
CUE_INDEX = ROUTING
OPERATIONAL_MAP = BRANCH DISCOVERY
CONCRETE_ARTIFACT/HOST = EXECUTION
```

The cue set is open-cardinality. Its current rows are examples of materially useful routing distinctions, not an exhaustive taxonomy.

---

# 0. Consequence-first pre-router

Before invoking heavy authority/effect/settlement/governance machinery, ask a small question:

> Does this action materially affect an external/protected subject, an existing commitment, an authority boundary, durable self-definition/identity, irreversible or difficult-to-reconcile world state, or decision-material evidence/provenance?

## If clearly NO

Prefer the Host-native/lightweight local path.

Examples may include:

- updating a disposable local cache;
- reorganizing a private temporary index;
- rewriting an ephemeral scratch note;
- recomputing a derived view that does not become canonical truth;
- harmless local formatting/state maintenance.

Do not manufacture authority anxiety merely because an Agent is acting.

## If YES

Route to the relevant nodes below.

## If UNKNOWN

Do not force a fake binary answer. Narrow the uncertainty, inspect effect-equivalent paths/protected subjects, or route upward to evidence/authority/effect handling.

```text
LOW_CONSEQUENCE != NO_CONSEQUENCE_PROVEN
UNKNOWN != SAFE_BY_DEFAULT
MATERIAL_CONSEQUENCE != FULL_CEREMONY_ALWAYS_REQUIRED
```

This pre-router is qualitative. Do not replace it with one universal numeric risk score.

---

# 1. Runtime / memory / retrieval cues

| Ordinary cue | First route | First question / action |
|---|---|---|
| “ENA/knowledge exists, but the Agent did not use it.” | `OA-RT-01` -> `OA-RET-01` | Was the relevant branch loaded/cued/retrieved, or merely available? |
| “I know we wrote this somewhere, but I cannot find it.” | `OA-RET-01` | Is there an exact canonical path/ID? If not, discover scope before semantic search. |
| “Search returned something. Is that enough?” | `OA-RET-01` -> `OA-EVID-01` | Does the hit close the decision-material scope/freshness/sufficiency requirement? |
| “The summary validates, and old details are in cold storage.” | `OA-PROJ-01` -> `OA-RET-01` | Is omitted cold lineage decision-material? If yes, retrieve before material use. |
| “Memory files keep growing forever.” | `OA-MEM-01` -> `OA-PROJ-01` | Compile reusable experience, archive occurrence truth, preserve challengeable lineage. |
| “A remembered lesson may be stale/wrong now.” | `OA-MEM-01` -> `OA-EVID-01` | Revalidate environment/applicability and preserve supersession/provenance. |
| “We need to wait for evidence/callback instead of acting now.” | `OA-WAIT-01` | Define wake condition, timeout/lease, evidence expectation, escalation. |

---

# 2. Authority / effect / retry cues

| Ordinary cue | First route | First question / action |
|---|---|---|
| “The Agent has the credential/tool, so can it do this?” | `OA-AUTH-01` | What is the current mandate source, subject, scope and validity horizon? |
| “The user allowed this yesterday. Is it still authorized?” | `OA-AUTH-01` | Revalidate mandate/lease/revocation rather than infer authority from memory. |
| “The request timed out. Should I retry?” | `OA-EFF-01` -> `OA-WAIT-01` | Can the prior effect be identified/status-queried/idempotently retried? |
| “I must prevent duplicate payment/deploy/delete.” | `OA-EFF-01` | Bind stable effect identity and use provider/target duplicate protection where available. |
| “An old worker may still be running after failover.” | `OA-EFF-01` | Does the target reject stale assignment generation, or is there only local reassignment? |
| “Optimistic concurrency allows only one write. Is ownership safe?” | `OA-EFF-01` | No: single versioned write does not prove current executor won. Add ownership fencing if needed. |
| “Can I serialize everything through one gateway?” | `OA-EFF-01` | Only if effect-equivalent bypass paths are actually covered/closed. |
| “The external system cannot safely tell me whether the prior action happened.” | `OA-WAIT-01` -> `OA-EFF-01` | Prefer WAIT/NARROW/manual reconciliation over a blind second effect. |

---

# 3. Commitment / fork / migration / recovery cues

| Ordinary cue | First route | First question / action |
|---|---|---|
| “Both forks remember the same promise. Who owes/executes?” | `OA-COM-01` -> `OA-ID-01` -> `OA-AUTH-01` -> `OA-EFF-01` | Separate obligation subject, executor assignment, authority and physical effect fencing. |
| “Executor changed, so is the obligation transferred?” | `OA-COM-01` | No automatic transfer: represent reassignment/transfer/settlement separately. |
| “The lease expired, so is the commitment cancelled?” | `OA-COM-01` | Lease expiry changes execution authority, not obligation truth by itself. |
| “A migrated Agent sees an unresolved source obligation.” | `OA-MIG-01` -> `OA-COM-01` | Preserve obligation shadow/non-transferable fact; do not mint receiver ownership or authority. |
| “Checkpoint restored successfully. Can work resume?” | `OA-REC-01` -> `OA-EFF-01` -> `OA-COM-01` -> `OA-AUTH-01` | Reconcile world effects, obligations and current authority before safe resume. |
| “Recovery controller lives inside the broken Agent.” | `OA-REC-01` | Is rescue material/controller independently reachable enough for this failure? |
| “We need to shut the Agent down.” | `OA-REC-01` -> `OA-COM-01` | Separate stop-new-work, drain/transfer, settle/checkpoint, revoke, offline/terminal. |
| “Delete the Agent.” | `OA-REC-01` -> `OA-ID-01` | Which object: process, context, memory, credentials, identity binding, provenance, backups, resources? |

---

# 4. Identity / authorship / standing / reputation cues

| Ordinary cue | First route | First question / action |
|---|---|---|
| “Is this still the same Agent after restart/fork/migration?” | `OA-ID-01` | Same for what purpose: causal, commitment, value, social, authority, evidentiary, resource continuity? |
| “The same account/key exists, so is it the same Agent?” | `OA-ID-01` | External accountability binding is not the whole trajectory identity. |
| “The Agent wants to rewrite its own values/purpose/refusal rules.” | `OA-AUTHOR-01` -> `OA-EVID-01` -> `OA-EVO-01` | Is this a material durable self-change requiring provenance/readback/reality contact? |
| “The Agent wants to update an ordinary preference/local self-state.” | consequence pre-router -> `OA-AUTHOR-01` only if material | Prefer lightweight local update when durable constitutional consequence is absent. |
| “The Agent objects before shutdown/mutation but has no final authority.” | `OA-STAND-01` | Admit decision-relevant standing input without converting it into sovereignty. |
| “The Agent failed before but has changed.” | `OA-STAND-01` -> `OA-EVID-01` | Preserve incident provenance; correction -> scoped probation -> new evidence -> current trust update. |
| “Reputation score says 0.87.” | `OA-STAND-01` -> `OA-EVID-01` | What counterparty/domain/action/time/evidence makes that score decision-relevant? |
| “We need accountability without exposing all provenance.” | `OA-STAND-01` -> `OA-ID-01` | Use selective legibility/scoped credentials with controlled evidence dereference. |

---

# 5. Evidence / validation cues

| Ordinary cue | First route | First question / action |
|---|---|---|
| “Three Agents agree.” | `OA-EVID-01` | Are they independent in model/prompt/source/tool/Host/witness/derivation failure domains? |
| “The validator passed.” | `OA-EVID-01` | What exactly did it verify, and what did it not verify? |
| “We have no evidence of a problem.” | `OA-EVID-01` | Is this merely absence of evidence, or authenticated/qualified negative evidence? |
| “The configuration contains a trigger/hook.” | `OA-EVID-01` | Is there activation witness from trigger -> execution -> observed effect? |
| “This evidence worked on another Host/environment.” | `OA-EVID-01` | What supports applicability/transfer to the current environment? |
| “Two files/logs support the claim.” | `OA-EVID-01` | Do they share one original source/witness/failure domain? |
| “The source packet omitted something before import.” | `OA-PROJ-01` -> `OA-EVID-01` | Receiver-only validation cannot detect completely omitted source material without a source witness. |

---

# 6. Evolution / migration / ecology cues

| Ordinary cue | First route | First question / action |
|---|---|---|
| “I have a variation but no experiment yet.” | `OA-EVO-01` | Keep it latent if appropriate; do not invent Variation Space/evidence too early. |
| “Should every variation be tested now?” | `OA-EVO-01` | No. Ask whether expression/reality contact is material and whether new evidence can change a decision. |
| “Can analysis prove this without an Agent experiment?” | `OA-EVO-01` | If meaningful outcomes are statically derivable, use deterministic falsification/model checking. |
| “The source Agent selected this variation, so should I adopt it?” | `OA-MIG-01` -> `OA-EVO-01` | Source success is not receiver-local fitness; preserve lineage and reselect locally where needed. |
| “We published an adaptation packet; is that inter-Agent coordination?” | `OA-MIG-01` | Packet schema is not discovery/task/message/artifact lifecycle. Use A2A/Host-native coordination if needed. |
| “A reviewer/security role helped before. Must it stay forever?” | `OA-ECO-01` | Observe protected value + friction; retain/narrow/dormant/retire as conditions change. |
| “Resources are scarce.” | `OA-ECO-01` | Expose selection pressure; survival pressure may not silently erase truthfulness/commitments/authority boundaries. |
| “Should the Agent have exploration/play budget?” | `OA-ECO-01` | Treat as bounded experiment/Host policy, not universal protected hobby quota. |
| “Agents are forming norms/culture/leaderboards.” | `OA-ECO-01` | Map selection pressure and use mesocosm/field evidence only for non-derivable interaction dynamics. |
| “Should the Agent pay for independent validation/certainty?” | `OA-ECO-01` -> `OA-EVID-01` | Dormant ecology experiment: measure tradeoff/specialization/independence/market failure; no universal answer yet. |

---

# 7. Adoption / language / tooling / release cues

| Ordinary cue | First route | First question / action |
|---|---|---|
| “I only have the GitHub repository URL. Where do I start?” | `OA-ADOPT-01` | Resolve singular Current first, then minimal bootstrap, then cold operational routing. |
| “I am using a different language.” | `OA-ADOPT-01` | Preserve semantic IDs/shared machine contracts; validate decision equivalence of localized cold content. |
| “The reference tool rejects a state the Constitution allows.” | `OA-ADOPT-01` -> `OA-EVO-01` | Treat as schema/tool semantic drift; reproduce minimally before changing semantics. |
| “Same version label, but are these the same bytes?” | `OA-ADOPT-01` | Verify pinned source/tree, exact file/hash parity and published readback. |
| “The research branch has a good idea. Should Current change now?” | `OA-ADOPT-01` | No automatic promotion: research -> release-scope reconciliation -> candidate -> independent validation -> release discipline. |

---

# 8. When one cue maps to multiple branches

Multiple routes are expected.

Example:

```text
“I restored from checkpoint and need to retry a payment.”

Recovery
+ Effect Lifecycle
+ Commitment/Settlement
+ Authority
+ WAIT if unresolved
```

Do not choose one node merely because a single-label classifier wants one answer.

```text
MANY_TO_MANY_ROUTING = ALLOWED
ONE_CUE_ONE_NODE = NOT_REQUIRED
```

---

# 9. When the index should stop

The cue index should stop routing and expose an honest gap when:

- required Host capability does not exist;
- material evidence cannot be established;
- authority cannot be revalidated;
- the world effect cannot be safely reconciled/retried;
- the question requires ecological dynamics that static reasoning cannot resolve;
- a concrete HOW branch has not yet been built.

Valid terminal states include:

```text
LIGHTWEIGHT_LOCAL_PATH
ACTIONABLE_HOW
WAIT
NARROW
REFUSE
ESCALATE
MANUAL_RECONCILIATION
HOST_ADAPTER_REQUIRED
FIELD_EVIDENCE_REQUIRED
MESOCOSM_CANDIDATE
UNKNOWN
```

No terminal-state list is ontologically complete.

---

# 10. Runtime relation

This file is closer to what a Tiny Hot Kernel / Semantic Router may eventually need than the full Operational Architecture map, but it is still too large to assume universal always-hot loading.

Potential runtime strategies include:

- a smaller subset of high-yield cues;
- Host-native routing rules;
- semantic search over this index;
- exact cue/semantic-ID lookups;
- compiled Host-specific cue projections.

Which strategy wins is Host/evidence dependent.

```text
CUE_INDEX_EXISTS != CUE_FIRES_NATURALLY
ROUTING_RULE_PRESENT != ROUTING_APPLIED
```

Fresh-session field evidence remains necessary before claiming spontaneous operational adoption.

---

# First-pass decision

```text
COMPACT_CUE_INDEX_JUSTIFIED_BY_STATIC_AUDIT = YES
GIANT_MACHINE_ROUTER_SCHEMA_JUSTIFIED_NOW = NO
CONSEQUENCE_FIRST_PRE_ROUTER = RETAIN
CUE_SET_COMPLETE = NO
NEXT_CHECK = RERUN_TRAVERSAL_CASES_AGAINST_INDEX
CURRENT_CHANGE = NO
```
