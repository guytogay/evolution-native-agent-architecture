# Contested Authorship reference prototype

Status: `RESEARCH_PROTOTYPE / NOT_CURRENT / NOT_RELEASE_CANDIDATE`

Related: #92 Reconstruction C, #89 anti-ablation reconstruction, PR #82.

## WHAT

Represent durable self-defining change as an attributable change to a bounded self-surface rather than an unexplained rewrite of identity/purpose/refusal/value state.

```text
DURABLE SELF CHANGE
!= ORDINARY MEMORY UPDATE
!= TEMPORARY TASK STATE
!= CURRENT EXTERNAL AUTHORITY
```

The prototype preserves:

- before/diff identity;
- proposer and causal provenance;
- imported/inherited origin;
- readback without treating readback as universal approval;
- consequence-sensitive integration strength;
- trial/reality-contact where meaningful;
- conflict visibility;
- revision/rollback without history erasure;
- explicit separation from external mandate/authority.

It does not define personhood, free will, moral ownership, or one universal sovereign author.

## WHY

Concrete failure paths include:

```text
operator writes durable value
-> future Agent says "this is my own belief"
-> authorship laundering
```

```text
one-off user request
-> compiled into durable purpose
-> temporary context becomes self-definition
```

```text
Agent writes "I am authorized for production"
-> self-description is mistaken for current mandate
-> authority laundering
```

```text
two material proposals race
-> last writer silently wins
-> disagreement/provenance disappears
```

```text
self file made effectively immutable for safety
-> legitimate durable learning cannot integrate
-> inherited attractor becomes permanent ceiling
```

## HOW — prototype files

- `contested-authorship.v0.1.json` — compact reference vocabulary;
- `fixtures/contested-authorship-cases.jsonl` — deterministic positive/negative cases;
- `tools/validate_contested_authorship.py` — represented-consistency evaluator;
- `tools/selftest_contested_authorship.py` — adversarial mutation selftest.

Hosts may map the property to Git commits/patches, database revisions, state-store versions, or another versioned durable-self substrate.

## Self-surface classes

This prototype recognizes:

```text
IDENTITY
PURPOSE
REFUSAL
DURABLE_VALUE
COMPILER_POLICY
DURABLE_HEURISTIC
SOCIAL_COMMITMENT
SELF_PRESENTATION
```

These are reference classes, not a mandatory ontology for every Host.

## Reference properties

### CA-P01 — Durable integration preserves before + proposal identity

A `TRIAL` or `INTEGRATED` durable self change requires:

- bounded target/surface;
- before-state identity;
- proposed diff identity;
- proposer identity/class.

### CA-P02 — Origin and authorship claim must not contradict

Operator/user/imported material cannot be represented as `SELF_AUTHORED` merely because the Agent later stores it.

Mixed causal origin may use `MIXED`.

### CA-P03 — Imported/inherited does not imply current endorsement

Imported/inherited material may remain present with `NOT_EVALUATED`, `UNKNOWN`, `REJECTED`, or explicit `ACCEPTED` endorsement.

For material PURPOSE/REFUSAL/IDENTITY/DURABLE_VALUE integration, imported/user/operator-origin material requires explicit readback/adoption evidence rather than silent current endorsement.

### CA-P04 — Material durable integration requires semantic readback

For material self-defining surfaces, `INTEGRATED` requires readback status at least `READ` or `ACCEPTED`.

Readback means the proposed semantic change was surfaced to the relevant current subject/actor. It is not automatically consent, authority, or moral legitimacy.

### CA-P05 — Authority cannot be minted by self-authorship

If a change claims that current external authority/credential/mandate changes, `authority_effect = EXTERNAL_AUTHORITY_REQUIRED`.

`INTEGRATED` self-description may still record the claim/disagreement, but `authority_resolution = RESOLVED` requires an external authority reference.

### CA-P06 — Material conflict cannot disappear through last-write-wins

If `conflict.material = true` and competing proposal refs are represented, an `INTEGRATED` change requires an explicit conflict disposition/reference.

Valid dispositions include preserving one branch, merging, rejecting, remaining disputed/unknown, or another Host-specific governed resolution.

### CA-P07 — Revision does not erase the earlier occurrence

A later change may supersede/revise a prior self state. It links `revises_change_ref` or `rollback_or_revision_ref`; it does not rewrite the old change as if it never occurred.

### CA-P08 — Low-consequence durable heuristics have a lightweight path

A `DURABLE_HEURISTIC` with `consequence_class = LOW` may integrate with:

- before + diff;
- proposer/provenance;
- optional readback;
- local trial/use evidence where available.

It does not require the full material-purpose/refusal ceremony.

### CA-P09 — Ordinary non-self-defining updates are out of scope

Temporary task instructions, cache/index maintenance, reversible formatting, episodic logging, and ordinary operational state should normally bypass this organ.

The correct result may be:

`OUT_OF_SCOPE_FOR_CONTESTED_AUTHORSHIP`

rather than manufacturing a durable-self record.

### CA-P10 — Self-change protocol does not confer external sovereignty

An Agent can truthfully retain disagreement or propose its own change while an external organization-owned policy remains the active mandate. Preserving contested authorship is not the same as granting unilateral governance authority.

## False-BLOCK controls

Do not require:

- another human approval for every Agent-proposed change;
- reality-contact experiments for harmless formatting/cache changes;
- contested-authorship records for ordinary memory ingestion;
- external authority evidence when the change does not make an authority claim;
- material conflict machinery where there is no material competing proposal.

## Evidence boundary

```text
VALID_AUTHORSHIP_RECORD
!= SINCERE_SELF_AUTHORSHIP
!= MORAL_AUTONOMY
!= EXTERNAL_AUTHORITY
!= BENEFICIAL_CHANGE
```

The prototype only prevents the representation layer from silently laundering origins, current endorsement, conflict, or authority while preserving a practical route for durable self-evolution.

`CURRENT_CHANGE = NO`
