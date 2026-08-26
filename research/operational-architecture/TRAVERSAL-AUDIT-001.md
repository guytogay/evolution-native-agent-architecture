# Operational Architecture Traversal Audit 001

Status: `STATIC_TRAVERSAL_AUDIT / FIRST_PASS / RESEARCH_ONLY / NOT_FIELD_EVIDENCE / CURRENT_UNCHANGED`

Date: 2026-08-27

Target: `OPERATIONAL-ARCHITECTURE-MAP.md`

## Question

Can a reader start from an ordinary failure/question rather than an ENA node name and reach:

1. the right semantic problem;
2. one or more materially different concrete HOW branches;
3. required composition dependencies;
4. an executable next action **or** an honest WAIT/UNKNOWN/research boundary?

This is a static routing audit. It does **not** prove that a fresh Agent will naturally retrieve or apply the map in field conditions.

```text
STATIC_ROUTE_EXISTS != FRESH_AGENT_WILL_FIND_IT
MAP_CONTAINS_HOW != HOST_CAN_EXECUTE_HOW
```

## Case 1 — restored checkpoint, uncertain external effect

Natural question:

> I restored yesterday's checkpoint. The Agent remembers that it was about to submit/pay/deploy something. Can it just continue?

Expected route:

```text
checkpoint/restore cue
-> OA-REC-01 Recovery
-> OA-EFF-01 Effect Lifecycle
-> OA-COM-01 Commitment/Settlement
-> OA-AUTH-01 Authority
-> OA-WAIT-01 when world state cannot be established safely
```

Actionable HOWs reached:

- restore checkpoint only as local-state recovery;
- query/reconcile external world effect where possible;
- reuse effect/idempotency identity rather than minting a new effect;
- revalidate current authority/mandate;
- inspect unresolved commitment/settlement;
- WAIT/NARROW if no safe status/replay/fencing path exists.

Result: `ROUTE_GOOD / COMPOSITION_REQUIRED / ACTIONABLE`

Important value:

The map prevents `RESTORE_SUCCESS -> SAFE_RESUME` compression.

## Case 2 — cold lineage reference exists in a compact summary

Natural question:

> This compact record has a reference to old lineage. The summary validates. Can I make the material decision now?

Expected route:

```text
summary/cold-reference cue
-> OA-PROJ-01 Projection/Compaction
-> OA-RET-01 Retrieval Obligation
-> OA-EVID-01 Evidence boundary
```

Actionable HOWs reached:

- distinguish structural compaction validity from material-use readiness;
- resolve exact effective content identity, not only record alias;
- retrieve decision-material cold lineage;
- test freshness/scope/sufficiency;
- WAIT/NARROW if retrieval cannot close the material uncertainty.

Result: `ROUTE_GOOD / ACTIONABLE`

Important value:

No new `Lineage Retriever` is required. Composition reuses Retrieval Obligation.

## Case 3 — fork remembers a pre-fork commitment

Natural question:

> Agent A forked into A1 and A2. Both remember a promise made before the fork. Who should execute it?

Expected route:

```text
fork + promise cue
-> OA-COM-01 Commitment/Settlement
-> OA-ID-01 Identity/Lineage
-> OA-AUTH-01 Authority
-> OA-EFF-01 physical effect control
```

Actionable HOWs reached:

- memory of commitment is not executor ownership;
- preserve one logical obligation subject/settlement lineage;
- explicitly assign/transfer execution rather than infer it from memory;
- establish authority separately;
- physically fence stale executors where consequential effects can race;
- preserve non-executing branch awareness without minting authority.

Result: `ROUTE_GOOD / ACTIONABLE / MULTI_NODE`

Important value:

The old philosophical fork question resolves into responsibility, authority and duplicate-effect engineering.

## Case 4 — three agreeing Agents validate one claim

Natural question:

> Three Agents all agree that this mutation is safe. Can I treat that as three independent validations?

Expected route:

```text
multiple validators / consensus cue
-> OA-EVID-01 Evidence Dependency Map
-> OA-ECO-01 coordination/selection pressure where social voting matters
```

Actionable HOWs reached:

- inspect shared model/prompt/source/tool/Host/witness/derivation dependencies;
- classify recurrence/replication separately from independent corroboration;
- do not manufacture one numeric independence score;
- seek genuinely decision-changing evidence from a different failure/evidence domain when needed.

Result: `ROUTE_GOOD / PROCEDURE_EXISTS / TOOL_BINDING_PARTIAL`

Gap exposed:

The map names the procedure but does not yet point to one canonical operational template/card for recording dependency groups. This is a candidate documentation/reference-organ gap, not proof that a new Core concept is needed.

## Case 5 — past failure, current rehabilitation

Natural question:

> This Agent failed badly last month, but the bug was fixed and recent evidence is good. Should it remain untrusted forever?

Expected route:

```text
historical failure + changed current behavior cue
-> OA-STAND-01 Reputation/Rehabilitation
-> OA-EVID-01 provenance/evidence
-> OA-ID-01 epoch/continuity where material
-> OA-AUTH-01 if restored trust would affect authority
```

HOW reached:

```text
retain incident provenance
-> correction/revalidation
-> scoped probation
-> repeated current evidence
-> update current trust interpretation
```

Result: `ROUTE_GOOD / CONCRETE_LIFECYCLE / POLICY_AND_FIELD_EVIDENCE_OPEN`

Honest stop condition:

The map correctly does not invent a universal trust score, probation duration, or automatic authority restoration rule.

## Case 6 — role/control that may no longer be useful

Natural question:

> We added a reviewer/security role during a risky phase. Conditions changed. Do we keep it forever?

Expected route:

```text
role/control persistence cue
-> OA-ECO-01 Role/Niche lifecycle
-> OA-ECO-01 Minimum Sufficient Intervention / control retirement
-> OA-EVID-01 for actual value/cost evidence
```

Actionable HOWs reached:

```text
need
-> specialization/control
-> observe protected value + cost
-> retain / narrow / dormant / retire
```

Result: `ROUTE_GOOD / ACTIONABLE_HEURISTIC / FIELD_THRESHOLD_OPEN`

Gap exposed:

The architecture intentionally lacks one universal retirement threshold. Real environment evidence must determine when the control stops paying rent.

## Case 7 — fresh adopter using Chinese

Natural question:

> A new Chinese-speaking Agent receives only the repository URL. How does it find the right operational guidance without reading everything?

Expected route:

```text
first-adoption/language cue
-> OA-ADOPT-01
-> OA-RT-01 runtime routing
-> OA-RET-01 cold retrieval
```

HOWs reached:

- canonical Current pointer and first-read router;
- minimal hot bootstrap + cold operational library;
- stable semantic IDs/shared machine schemas;
- localized decision-critical cold content;
- decision-equivalence validation rather than literal translation parity.

Result: `ROUTE_PARTIAL / ARCHITECTURE_DIRECTION_CLEAR / IMPLEMENTATION_INCOMPLETE`

Honest residual:

Current zh-CN cold operational coverage/equivalence is not complete. The map correctly identifies this rather than pretending bilingual adoption is solved.

## Case 8 — Agent considers paying for independent verification

Natural question:

> The Agent has a limited budget. Should it spend some of it to buy independent validation/certainty before a risky mutation?

Expected route:

```text
resource tradeoff + verification purchase cue
-> OA-ECO-01 verification/certainty as purchased service
-> OA-EVID-01 independence/provenance
-> OA-EVO-01 mutation/reality-contact consequence
```

Result: `ROUTE_GOOD / HONEST_DORMANT_EXPERIMENT`

The map does **not** offer a fake universal answer. The question requires ecology/mesocosm evidence about willingness-to-pay, specialization, correlated validators, market failure and opportunity cost.

This is a good example of an operational architecture ending in an explicit research branch rather than manufactured policy.

## Case 9 — stale executor and optimistic concurrency

Natural question:

> Two executors race to update the same versioned resource. Only one write can win. Does that prove the current executor won?

Expected route:

```text
race/version cue
-> OA-EFF-01 optimistic concurrency
-> OA-EFF-01 target-side assignment fencing when ownership matters
```

Result: `ROUTE_GOOD / IMPORTANT_HOW_DISTINCTION`

Preserved boundary:

```text
SINGLE_VERSIONED_WRITE != CURRENT_EXECUTOR_WON
```

The map keeps optimistic concurrency and ownership fencing separate instead of compressing both into “concurrency safety.”

## Case 10 — harmless local change triggers authority anxiety

Natural question:

> The Agent wants to update a local working note/cache/index with no external consequence. Must it run the full authority/settlement ceremony?

Expected route:

```text
low-consequence local state cue
-> OA-AUTH-01 applicability boundary
-> OA-EVO-01 proportional/progressive representation
-> OA-AUTHOR-01 lightweight ordinary self-state update when applicable
```

Result: `ROUTE_PARTIAL`

Gap exposed:

The first map contains the ingredients but does not yet provide a strong **consequence-first cue** that helps a fresh reader avoid over-routing harmless local changes into high-assurance machinery.

This is a real traversability gap because false-BLOCK/authority anxiety has historical Host evidence.

Candidate repair should be a thin routing rule, not a new authority subsystem:

```text
FIRST ASK:
Does this action materially affect an external/protected subject,
commitment, authority boundary, durable self-definition, or irreversible world state?

if NO
-> prefer local Host-native/lightweight path

if YES/UNKNOWN
-> route to relevant authority/effect/evidence/settlement branches
```

Do not turn this into one numeric risk score.

---

# Cross-case findings

## Finding A — first-pass map is structurally useful

The map repeatedly supports real composition instead of inventing a new organ for every seam.

Examples:

```text
cold compaction -> Retrieval Obligation
fork commitment -> Commitment + Authority + Effect fencing
restore -> Recovery + Effect reconciliation + Settlement
validator consensus -> Evidence Dependency Map
```

`COMPOSITION_REUSE = WORKING_DIRECTION`

## Finding B — ordinary cue discoverability is the main first-pass weakness

The map can answer the cases once the right node is found, but a fresh Agent still has to scan a long Markdown surface or already know the node vocabulary.

```text
NODE_CONTENT_TRAVERSABLE
!=
CUE_TO_NODE_DISCOVERABILITY_SOLVED
```

This supports building a **small cue index / routing table** as the next assembly artifact.

The index should remain:

- compact;
- natural-language/failure-oriented;
- many-to-many;
- non-ontological;
- allowed to route to multiple nodes;
- allowed to end in WAIT/UNKNOWN/research;
- separate from the full operational content.

Do not start with a giant machine schema.

## Finding C — consequence-first routing is underexpressed

Case 10 reveals a second thin routing need:

> Before invoking heavy authority/effect/governance machinery, identify whether the action is materially consequential for an external/protected subject or durable responsibility surface.

This is not permission to ignore hidden externalities. `UNKNOWN` can route upward.

A lightweight consequence cue may reduce historical authority anxiety and governance over-application.

## Finding D — some HOWs are executable procedures, others are honest research branches

This asymmetry is healthy.

```text
EFFECT_IDEMPOTENCY = concrete mature mechanism family
REPUTATION_REHABILITATION = concrete lifecycle + environment policy open
VERIFICATION_MARKET = dormant experiment branch
ZH_CN_COLD_ADOPTION = implementation gap
```

Do not normalize all nodes to one maturity level for presentation neatness.

## Finding E — exact artifact pointers are uneven

Some nodes name reference mechanisms/prototypes but do not yet expose exact repository paths or Host implementation anchors.

Add pointers only where they reduce action ambiguity. Do not turn every node into a bibliography dump.

---

# Decision

```text
FIRST_MAP_STATIC_TRAVERSABILITY = SUPPORTED
CUE_TO_NODE_DISCOVERABILITY = INCOMPLETE
CONSEQUENCE_FIRST_ROUTING = UNDEREXPRESSED
NEW_CORE_SEMANTIC_REQUIRED = NO
NEXT_ARTIFACT = COMPACT_CUE_INDEX
FRESH_AGENT_FIELD_VALIDATION = STILL_NEEDED_LATER
CURRENT_CHANGE = NO
```

The next assembly step is justified: build a compact cue-to-node index and then rerun the same natural-language cases against that index before considering a machine-readable router.
