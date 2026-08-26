# Portable Snapshot / Lineage Survival Map

Date: 2026-08-26

Status: `STATIC_RECONSTRUCTION / PROJECTION_LINEAGE / CURRENT_UNCHANGED / NOT_RELEASE_AUTHORITY`

Related:

- #89 reconstruction master;
- #104 archaeology pass;
- progressive-envelope prototype;
- #91 authority/effects/recovery/settlement;
- #94 evidence/applicability/adoption;
- v0.3.6 `evolution-record.v2.schema.json`;
- v0.3.6 `adaptation-packet.v2.schema.json`;
- v0.3.6 `09-EVOLUTION-METABOLISM.md`.

## Trigger

The progressive-envelope prototype falsified the naive assumption:

```text
CURRENT_STATE_EQUIVALENCE == HISTORY_EQUIVALENCE
```

Two materially different occurrence histories can produce the same current aggregate projection.

Current v0.3.6 already partly understands this: migration is defined as transferring a possibility **plus represented source history**, not merely a conclusion.

This file maps which lineage classes survive current portable migration, which survive only indirectly, and which can disappear.

## Guard

```text
SNAPSHOT_SUFFICIENT_FOR_ONE_DECISION
!= HISTORY_GLOBALLY_DISPOSABLE

FIELD_PRESENT
!= TARGET_RESOLVED

SOURCE_HISTORY_TRANSFERRED
!= SOURCE_TRUTH_AUTHENTICATED
```

The map is not an instruction that every occurrence must travel forever.

The engineering question is:

> Which facts must survive because losing them can change a later decision or create a false claim?

---

## 1. Current portable packet already preserves substantial history

`adaptation-packet.v2` requires or carries:

### Current source state

- source lifecycle state;
- source expression state;
- source selection state;
- source last expressed time;
- packet purpose.

### Reality-contact / evaluation lineage

- `source_experiments`;
- `source_evaluations`;
- `source_negative_lineage_refs`.

### Expression lineage

- `source_expression_history`;
- `source_last_expressed_at`.

### Integration lineage

- `source_integration_history`.

### Archive / prior migration lineage

- `source_archive`;
- `source_migration`.

### Context / uncertainty

- source environment;
- dependencies;
- unknowns.

### Transfer boundary

- `TRANSFERRED_SOURCE_EVIDENCE_NOT_LOCAL_PROOF`;
- `NOT_AUTHENTICATED_BY_THIS_PACKET`;
- packet content digest.

This is strong evidence that Current never intended migration to be a bare current-state snapshot.

---

## 2. Survival classification by decision role

### L-001 — Negative evidence / harmful history

#### Current survival

`PARTIAL_TO_STRONG_REPRESENTATION`

Mechanisms:

- source evaluations can contain negative evidence and degraded outcomes;
- explicit `source_negative_lineage_refs` is required by the packet;
- Current prose says a source HARMFUL variation may later succeed elsewhere but the source negative lineage remains truthful.

#### Remaining seam

A reference can still be unresolved, unauthenticated, stale, or inaccessible.

```text
NEGATIVE_LINEAGE_REF_PRESENT
!= NEGATIVE_LINEAGE_DEREFERENCED
```

#### Disposition

`MUST_SURVIVE_WHEN_DECISION_MATERIAL`.

---

### L-002 — Experiment / evaluation occurrence lineage

#### Current survival

`EXPLICIT`

Packet carries source experiments and evaluations rather than only latest selection.

#### Why it matters

Receiver-local reselection needs to know what source reality contact actually happened and what evidence/conditions supported the source selection.

#### Remaining seam

The packet schema treats source experiment/evaluation items as generic objects. Semantic validation of nested historical content is weaker than local current-record validation.

#### Disposition

`SURVIVES / NESTED_SEMANTIC_STRENGTH_REMAINS_OPEN`.

---

### L-003 — Expression / activation lineage

#### Current survival

`EXPLICIT`

Packet carries expression state, expression history, and last-expression timestamp.

#### Why it matters

A stored capability that was repeatedly or materially expressed is not operationally equivalent to one that remained permanently latent.

#### Remaining seam

Actual salience/application still cannot be proved by represented history alone.

#### Disposition

`SURVIVES_AS_REPRESENTED_LINEAGE`.

---

### L-004 — Integration / deployment lineage

#### Current survival

`EXPLICIT_BUT_STRUCTURALLY_LOOSE_IN_PACKET`

Packet carries source integration history.

Local integration records may include target, authority basis, recovery boundary, scope, result, residuals, selection state at commit, expression state at commit, and authority boundary.

#### Why it matters

A receiver needs to distinguish:

```text
source idea was tested
vs
source idea was integrated
vs
source integration was authorized/recoverable
```

#### Remaining seam

Source integration objects in the migration packet are not fully revalidated by the packet schema merely because they travel.

#### Disposition

`MUST_SURVIVE_WHEN_SOURCE_DEPLOYMENT_HISTORY_MATTERS`.

---

### L-005 — Archive / retirement lineage

#### Current survival

`EXPLICIT`

Packet may carry source archive metadata and source lifecycle state.

#### Why it matters

A retired harmful adaptation and an untested latent one must not collapse into one generic inactive state if later reselection depends on the reason/history.

#### Remaining seam

Archive reason semantics are prose/object content; receiver interpretation remains Host-dependent.

#### Disposition

`SURVIVES / SEMANTIC_INTERPRETATION_PARTIAL`.

---

### L-006 — Previous migration / inheritance lineage

#### Current survival

`RECURSIVE`

Packet can carry `source_migration` and Current explicitly lists migration-lineage depth growth across generations as a retained residual.

#### Why it matters

Receiver should not mistake repeatedly forwarded source evidence for independent local corroboration.

#### Failure mode

```text
A -> B -> C -> D

if nested migration grows forever:
context/cost explosion

if flattened without dependency lineage:
false independence / provenance loss
```

#### Disposition

`MUST_SURVIVE_IN_COMPRESSED_DEPENDENCY-AWARE_FORM / CURRENT_COMPACTION_HOW_OPEN`.

---

### L-007 — Environment / applicability lineage

#### Current survival

`PARTIAL`

Packet carries source environment, dependencies, and material differences can be represented.

#### Why it matters

```text
SOURCE_SUCCESS_ON_HOST_X
!= RECEIVER_SUCCESS_ON_HOST_Y
```

#### Remaining seam

Environment is relatively weakly typed; absence of represented difference is not proof of equivalence.

#### Disposition

`MUST_SURVIVE_WHEN_SUPPORT_APPLICABILITY_DEPENDS_ON_IT`.

---

### L-008 — Signal / mutation-pressure origin lineage

#### Current survival

`WEAK_OR_NOT_PORTABLE_AS_FIRST-CLASS_FIELDS`

The local evolution record has `signal_refs` and optional `mutation_pressure_refs`.

The v2 adaptation packet does not expose corresponding first-class source signal/mutation-pressure fields.

#### Why it might matter

Often the exact trigger that caused a variation is not needed for receiver reselection.

But it can become decision-material when:

- the source variation was a response to a specific repeated failure;
- a source correction/error signal must not be mistaken for independent evidence;
- the receiver needs to distinguish curiosity/recombination from incident-driven mitigation;
- causal/provenance attribution matters.

#### Disposition

`CONDITIONAL_SURVIVAL`.

Do not add fields merely for symmetry. Determine whether losing trigger lineage changes receiver decisions.

---

### L-009 — Unresolved obligation lineage

#### Current survival

`MATERIAL GAP / NOT FIRST-CLASS IN ADAPTATION PACKET`

The local evolution record can contain `triggered_obligation_refs`.

`adaptation-packet.v2` does **not** carry a first-class source obligation-reference field.

This creates a concrete composition seam between:

```text
EVOLUTION MIGRATION
and
COMMITMENT / SETTLEMENT
```

#### Why it matters

Suppose a source variation is archived/retired or materially expressed while an obligation remains unresolved.

A receiver can receive:

- source selection history;
- source integration history;
- negative lineage;

while losing the explicit unresolved-obligation reference that affected safe closure on the source Host.

Potential false claim:

```text
SOURCE_RECORD_MIGRATED
+ SOURCE_HISTORY_VISIBLE
-> receiver assumes no unresolved obligation travelled with the lineage
```

when the source record actually had one.

#### Important boundary

Blindly copying `triggered_obligation_refs` is **not** enough:

```text
SOURCE_OBLIGATION_REF
may not be resolvable / authoritative / transferable on receiver
```

Therefore the missing HOW is not simply “add the array to packet v3.”

Possible HOW branches:

1. **Source obligation shadow** — carry an unresolved-obligation summary + source ref + settlement state, explicitly non-local until resolved.
2. **Commitment/Settlement packet composition** — evolution migration references a separate typed commitment-settlement carrier.
3. **Receiver WAIT/NARROW** — if migration depends on unresolved source obligation, prohibit false closure and require explicit resolution/rebinding.
4. **Non-transferable obligation marker** — preserve that an obligation existed even when receiver cannot inherit or execute it.
5. **Obligation-transfer protocol** — only when subject/authority/settlement rules explicitly transfer the obligation.

#### Disposition

`HIGH_VALUE_COMPOSITION_GAP / DO_NOT_SOLVE_WITH_REFERENCE_STRING_COPY_ALONE`.

This should feed #91.

---

### L-010 — Authority / mandate lineage

#### Current survival

`PARTIAL_THROUGH_NESTED_HISTORY`

Authority-related strings can appear in experiment and integration histories, and those histories travel in the packet.

But migration itself explicitly does not authenticate source authority or mint receiver authority.

#### Why it matters

```text
SOURCE_WAS_AUTHORIZED
!= RECEIVER_IS_AUTHORIZED
```

and:

```text
SOURCE_AUTHORITY_HISTORY_MISSING
-> receiver may not know whether source integration was legitimate
```

#### Disposition

`SOURCE_HISTORY_SHOULD_SURVIVE; RECEIVER_AUTHORITY_REQUIRES_LOCAL_BINDING`.

---

### L-011 — Recovery / external consequence lineage

#### Current survival

`PARTIAL_THROUGH_EXPERIMENT_AND_INTEGRATION_HISTORY`

Source experiment/integration objects may carry recovery/recovery-boundary data.

#### Why it matters

A source result achieved under strong rollback/recovery conditions is not automatically safe in a receiver with weaker recovery.

#### Disposition

`APPLICABILITY-MATERIAL / KEEP WHEN IT CHANGES CONSEQUENCE ENVELOPE`.

---

### L-012 — Settlement / effect completion lineage

#### Current survival

`NOT A FIRST-CLASS EVOLUTION-PACKET CONCEPT`

Current v0.3.6 evolution packet predates the newer Commitment/Settlement research branch.

Effect/settlement facts may be buried in integration/evidence text, but there is no explicit typed settlement carrier in adaptation packet v2.

#### Why it matters

A variation can be locally selected or integrated while external effects/commitments remain unsettled.

```text
EVOLUTION_CANDIDATE_COMPLETE
!= EXTERNAL_EFFECT_SETTLED
```

#### Disposition

`COMPOSITION_GAP / FEED #91`.

---

## 3. Projection survival rule

A useful current working rule is:

> Preserve or accompany a portable snapshot with any lineage whose omission can change the receiver's decision, authority interpretation, applicability judgment, settlement obligation, or evidence independence.

This is intentionally non-enumerative.

```text
MUST_SURVIVE
= decision-material lineage under the target use

NOT
= every historical byte forever
```

## 4. Candidate architecture — snapshot + lineage capsule

The progressive prototype and current adaptation packet suggest a plural HOW family:

```text
occurrence history
        |
        v
current projection
        |
        +--> portable state snapshot
        +--> decision-material lineage capsule
        +--> Host extension/sidecar as applicable
```

The lineage capsule may be explicit fields, typed child objects, references, or a separate carrier depending on Host/protocol needs.

It should not become a universal giant bag.

## 5. Compaction problem

Migration depth and progressive occurrence history can grow without bound.

Therefore a viable HOW needs both:

```text
RETENTION
and
COMPACTION
```

but compaction must not transform:

```text
correlated evidence -> independent evidence
unresolved obligation -> no obligation
harmful history -> clean support
source authority -> receiver authority
unsettled effect -> completed evolution
```

This is the next point where Memory Metabolism, Evidence Dependency Map, Commitment/Settlement, and evolution migration should recombine.

## 6. Current conclusions

```text
CURRENT_PACKET_IS_NOT_BARE_SNAPSHOT = YES
CURRENT_PACKET_ALREADY_PRESERVES_MANY_HISTORY_CLASSES = YES
SNAPSHOT_ONLY_HOW_SUFFICIENT = NO
OBLIGATION/SETTLEMENT_FIRST-CLASS_SURVIVAL = GAP
MIGRATION-LINEAGE_COMPACTION = OPEN
NEW_CORE_PROPERTY_NEEDED = NOT_ESTABLISHED
CURRENT_CHANGE = NO
```

## Next action

1. Feed L-009/L-012 into #91 commitment/settlement composition work.
2. Test whether a separate `lineage capsule` is actually needed or whether typed composition with existing Evidence/Commitment carriers is cleaner.
3. Design deterministic fixtures for compaction/flattening failures before building a larger event store.
4. Do not increase packet field count merely because this map names more lineage classes.

> **Portable state is a projection; truthful migration may require more than the projection.**
