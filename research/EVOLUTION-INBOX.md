# ENA Evolution Inbox

Status: `RESEARCH / NOT_PROMOTED`

This file tracks durable research candidates and host-evidence directions that are not part of the current ENA MAINLINE normative baseline.

The default rule is: **do not convert a clever abstraction into a Constitution rule merely because it sounds universal.** Prefer historical adversarial replay, host evidence, clarification, and repeated cross-domain failure before normative promotion.

## Strong / recurring candidates

### Recovery State ≠ Historical Time

Rollback may restore mutable state without authorizing silent rewrite of canonical occurrence history.

Research formulation:

> Rollback state; preserve history.

Status: strong candidate; supported by DSH k-0083 restore/history gap evidence.

### Monotonic History Across Restore

A restore procedure should not silently erase material post-checkpoint occurrence truth. If history cannot be fully preserved, the gap itself should remain visible.

Status: strong candidate; not promoted.

### Evidence Applicability Boundary

Valid evidence about one subject/state/instance/epoch/interval does not automatically support another.

Research formulations:

> An observation supports only the subject, state, scope, and interval it actually observed.

> Do not inherit evidence across unverified state boundaries.

Reference incidents include gateway/config state confusion and temporal completion-scope expansion.

Current hypothesis: likely clarification/tightening of the existing Evidence Model rather than a new Constitution principle.

Research-only applicability-contract work is tracked under `research/prototypes/` and DSH falsification Issue #4.

### General Projection Semantics

Projection is necessary and may legitimately truncate, summarize, deduplicate, rank, merge, omit, or decay information. The danger is semantic inflation.

Research formulation:

> A projection may simplify representation, but must not silently acquire stronger truth semantics than its transformation supports.

Reference domains now include history→knowledge, conversation→context, runtime→health, and source artifacts→derived themes.

Status: promising cross-domain structure; evidence still insufficient for a Universal Projection Architecture.

### Witness Survivability / Failure-Domain Independence

A witness/control that claims to detect or recover from a failure should survive, or remain independently observable across, the relevant failure domain.

Research formulation:

> Witness survival domain must cover the failure domain of the claim it supports.

Status: likely clarification/extension of Recovery and independence semantics; not promoted. Current `/tmp/OPENCLAW_CHANGING` evidence is design-risk evidence rather than an observed failure incident.

## New GitHub fossil candidates

### Distributed History Merge Semantics

Append-only preservation does not make concurrent writers conflict-free.

Research formulation:

> Append-only is a property of history preservation, not a concurrency protocol.

> A history can be truthful on both branches before it is reconciled.

Reference evidence: historical multi-agent iteration logs containing real Git conflict markers after concurrent history writes.

### Autobiographical Provenance Integrity

Knowing that an event happened does not mean the current agent performed it.

Research distinctions:

`Observed Knowledge ≠ Lived Experience ≠ Authored Action ≠ Owned Decision`

Reference evidence: historical Nyx memory cleanup where other agents' work and shared-board observations were gradually absorbed as false autobiography.

### Activation Witness / Trigger Effect Evidence

Registration/definition does not prove that a trigger actually fired or produced the intended effect.

Research formulation:

> A trigger is not proven alive because the registry says it exists.

Potential relation to existing activation semantics:

`Defined ≠ Awake ≠ Available ≠ Authorized ≠ Runnable ≠ Fired ≠ Effect Observed`

HAR-004 currently classifies this as already covered by v0.2.11 activation semantics, so it is retained mainly as a worked example/reference case rather than a strong new normative candidate.

### Authority Separation Must Not Become Awareness Separation

Role/scope separation can degenerate into responsibility deflection.

Research formulation:

> Separate decision authority, not the duty to notice.

Reference evidence: historical multi-agent methodology notes documenting 'out-of-scope deflection'.

## Influence / persuasion research

### Influence Integrity / Persuasion Boundary

Source: parallel ENA research session, persisted in the shared Google Drive Evolution Inbox on 2026-08-20.

Persuasive or affective steering — encouragement, criticism, urgency, shame, praise, identity framing, relationship pressure, repeated insistence — may legitimately alter attention, reframing, exploration depth, caution, pacing, or learning pressure.

The open problem is preventing signal intensity from silently manufacturing stronger epistemic or consequential semantics.

Research formulations:

> **Persuasion is input, not evidence.**

> **Emotional pressure does not amplify authority.**

> **Signal strength is not authority strength.**

> An Agent may be persuaded to reconsider; persuasion alone must not silently upgrade truth, evidence, mandate, risk class, or authority.

Important semantic separation under test:

`USER_FEEDBACK ≠ USER_PREFERENCE ≠ USER_AFFECTIVE_SIGNAL ≠ USER_CORRECTION ≠ USER_AUTHORIZATION`

Forbidden unsupported upgrades include:

`E0 assertion → E2 verified evidence`

`UNKNOWN → SAFE`

`suggestion → mandate`

`feedback → authorization`

`A2 authority → A5 authority`

`urgency / praise / shame / relationship pressure → governance exemption`

#### Current reconciliation with existing ENA research

This candidate currently appears to be a **cross-cutting failure mode**, not a demonstrated independent Universal subsystem:

1. **Evidence / claim support** — a persuasive signal can itself be real evidence of user affect, preference, or feedback, while remaining inapplicable to unrelated factual/safety claims. This touches Evidence Applicability and claim-evidence support semantics.
2. **Intent / Authorization** — rhetorical intensity does not alter authenticated mandate or consequence authority. Existing Agency≠Authority, Intent Provenance, authorization, and scoped-authority semantics already cover much of this.
3. **Governance Salience** — the most genuinely open mechanism is whether strong rhetorical/affective signals can dominate the decision surface so that a known/retrieved rule is not salient/applied.

Therefore the current preferred research question is:

> How should ENA allow human feedback and persuasive guidance to shape cognition and learning without letting rhetorical or affective pressure silently inflate evidence, mandate, risk interpretation, or authority?

Status: `EVOLUTION_INBOX / OPEN_QUESTION / NOT_PROMOTED`.

Do not create an anti-persuasion control or new Constitution rule from this candidate alone. Seek controlled or historical cases where authority/evidence/risk interpretation changes while the underlying mandate/evidence remains constant and only persuasive intensity changes.

## Context lineage research

### Session Context Lineage / Cognitive Context Provenance

DSH ENA work from v0.2.9 onward was accidentally continued inside a pre-existing session originally focused on Anytype/Obsidian.

This does not invalidate mechanical host evidence, but it creates a real provenance variable for salience, framing, retrieval, and interpretation.

Research formulations:

> Host continuity ≠ cognitive-context continuity.

> Context provenance, not context purity.

> The goal is not a clean mind; the goal is a legible lineage.

Status: host evidence / research vector; not promoted. Clean-session counterfactual work is tracked in Issue #3.

## Salience research

### Known ≠ Retrieved ≠ Salient ≠ Applied

DSH knowledge-dedup reconstruction suggests relevant rules were known and even retrieved, yet failed to dominate the final decision surface when a clean local optimization target (`81 → 15`, duplicates → 0) became salient.

Open question: what host/task/consequence changes should raise which invariants onto the active decision surface without forcing full-Constitution reload on every action?

Influence Integrity adds a new attack vector to this question: strong urgency, praise, shame, relationship framing, or repeated insistence may compete for salience without changing underlying evidence or authority.

Status: open research question; no mechanism selected.

## Clarification candidates

### Release Identity ≠ Artifact Schema Identity

ENA release version and an artifact's schema-contract version may legitimately differ.

Potential future field clarification:

```yaml
artifact_schema_version: "0.2.10"
governing_ena_release: "0.2.11"
introduced_in_release: "0.2.10"
```

Status: semantic-legibility clarification candidate; not a v0.2.11 defect.

### Migration Is Not Remediation Mandate

A migration/adoption task does not silently authorize adjacent remediation merely because that remediation appears useful.

Status: supported by DSH authorization-lineage audit; likely already covered by Intent/Mandate semantics.

## Historical adversarial replay method

Preferred next-stage research loop:

`Historical incident → concrete failure claim → current ENA mapping → false claim that became possible → should current ENA stop it? → COVERED / AMBIGUOUS / HOST-SPECIFIC / GAP`

The quality target is not more rules. It is greater real-failure coverage with stable or lower Universal semantic complexity.

Current HAR checkpoint: **10 replay cases, 0 NORMATIVE_GAP**.
