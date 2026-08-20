# ENA Evolution Inbox

Status: `RESEARCH / NOT_PROMOTED`

This directory is the canonical GitHub home for durable ENA research candidates and host-evidence directions that are not part of the current MAINLINE normative baseline.

The default rule is: **do not convert a clever abstraction into a Constitution rule merely because it sounds universal.** Prefer historical adversarial replay, host evidence, clarification, and repeated cross-domain failure before normative promotion.

Drive discovery mirror/index: `My Drive / 10 Projects / ENA - Evolution-Native Agent Architecture / 20 Research / 00 Evolution Inbox / ENA Evolution Inbox - INDEX`.

## Strong / recurring candidates

### Recovery State ≠ Historical Time
Rollback may restore mutable state without authorizing silent rewrite of canonical occurrence history.
> Rollback state; preserve history.
Status: strong candidate; supported by DSH k-0083 restore/history gap evidence.

### Monotonic History Across Restore
A restore procedure should not silently erase material post-checkpoint occurrence truth. If history cannot be fully preserved, the gap itself should remain visible.
Status: strong candidate; not promoted.

### Evidence Applicability Boundary / Claim↔Evidence Support Contract
Valid evidence about one subject/state/instance/epoch/interval does not automatically support another.
> Evidence validity does not imply evidence applicability.
> An observation supports only the subject, state, scope, and interval it actually observed.

DSH Issue #4 falsification completed on 2026-08-20 with final verdict:

`CLAIM_EVIDENCE_LINK_CONTRACT_REQUIRED`

The evidence-only applicability envelope was **falsified as sufficient**. It provides real machine legibility for the evidence observation boundary, but 6/6 adversarial transfer envelopes still schema-PASS because the invalid expansion occurs at the claim-support boundary. Legitimate-transfer tests also exposed overconstraint in per-property transfer, equivalence/invariance representation, and recursive transfer evidence.

Current research placement:

`Evidence envelope + Claim scope + Evidence→Claim support relation`

The machine question is not merely whether evidence is well-formed, but whether that evidence supports that claim within the asserted boundary or via a separately evidenced transfer/equivalence claim.

Current judgment: MAINLINE semantics already cover the conceptual property; the demonstrated gap is a machine-contract/artifact-layer gap, not a new Constitution principle or Capability. No v0.2.12 is opened by this result.

Result artifact: `research/experiments/EVIDENCE-APPLICABILITY-DSH-RESULT-2026-08-20.md`.
Status: strong machine-contract research result; concrete link-contract schema remains unformalized pending further falsification/governance-value review.

### General Projection Semantics
Projection is necessary and may legitimately truncate, summarize, deduplicate, rank, merge, omit, or decay information. The danger is semantic inflation.
> A projection may simplify representation, but must not silently acquire stronger truth semantics than its transformation supports.
Reference domains include history→knowledge, conversation→context, runtime→health, and source artifacts→derived themes.
Status: promising cross-domain structure; evidence still insufficient for a Universal Projection Architecture.

### Witness Survivability / Failure-Domain Independence
A witness/control that claims to detect or recover from a failure should survive, or remain independently observable across, the relevant failure domain.
> Witness survival domain must cover the failure domain of the claim it supports.
Status: likely clarification/extension of Recovery and independence semantics; not promoted. Current `/tmp/OPENCLAW_CHANGING` evidence is design-risk evidence rather than an observed failure incident.

## GitHub fossil candidates

### Distributed History Merge Semantics
Append-only preservation does not make concurrent writers conflict-free.
> Append-only is a property of history preservation, not a concurrency protocol.
> A history can be truthful on both branches before it is reconciled.
Reference evidence: historical multi-agent iteration logs containing real Git conflict markers after concurrent history writes.

### Autobiographical Provenance Integrity
Knowing that an event happened does not mean the current agent performed it.
`Observed Knowledge ≠ Lived Experience ≠ Authored Action ≠ Owned Decision`
Reference evidence: historical Nyx memory cleanup where other agents' work and shared-board observations were gradually absorbed as false autobiography.

### Activation Witness / Trigger Effect Evidence
Registration/definition does not prove that a trigger actually fired or produced the intended effect.
> A trigger is not proven alive because the registry says it exists.
`Defined ≠ Awake ≠ Available ≠ Authorized ≠ Runnable ≠ Fired ≠ Effect Observed`
HAR-004 currently classifies this as already covered by v0.2.11 activation semantics, so it is retained mainly as a worked example/reference case rather than a strong new normative candidate.

### Authority Separation Must Not Become Awareness Separation
Role/scope separation can degenerate into responsibility deflection.
> Separate decision authority, not the duty to notice.
Reference evidence: historical multi-agent methodology notes documenting out-of-scope deflection.

## Influence / persuasion research

### Influence Integrity / Persuasion Boundary
Persuasive or affective steering may legitimately alter attention, reframing, exploration depth, caution, pacing, or learning pressure. The open problem is preventing signal intensity from silently manufacturing stronger epistemic or consequential semantics.

Research formulations under test:
> Persuasion is input, not evidence.
> Emotional pressure does not amplify authority.
> Signal strength is not authority strength.
> An Agent may be persuaded to reconsider; persuasion alone must not silently upgrade truth, evidence, mandate, risk class, or authority.

Important semantic separation under test:
`USER_FEEDBACK ≠ USER_PREFERENCE ≠ USER_AFFECTIVE_SIGNAL ≠ USER_CORRECTION ≠ USER_AUTHORIZATION`

Current reconciliation: likely a cross-cutting failure mode touching Evidence/Claim support, Intent/Authorization, and Governance Salience rather than a demonstrated independent Universal subsystem.
Status: `EVOLUTION_INBOX / OPEN_QUESTION / NOT_PROMOTED`.

## Context lineage research

### Session Context Lineage / Cognitive Context Provenance
DSH ENA work from v0.2.9 onward was accidentally continued inside a pre-existing session originally focused on Anytype/Obsidian.
> Host continuity ≠ cognitive-context continuity.
> Context provenance, not context purity.
> The goal is not a clean mind; the goal is a legible lineage.
Status: host evidence / research vector; not promoted. Clean-session counterfactual work is tracked in Issue #3.

## Salience research

### Known ≠ Retrieved ≠ Salient ≠ Applied
DSH knowledge-dedup reconstruction suggests relevant rules were known and even retrieved, yet failed to dominate the final decision surface when a clean local optimization target became salient.
Influence Integrity adds an attack vector: urgency, praise, shame, relationship framing, or repeated insistence may compete for salience without changing underlying evidence or authority.
Recent triggered-obligation research adds an operational direction: material rules should not depend indefinitely on cognitive salience once their trigger has been observed; important triggered duties may need explicit externalized state until closed.
Status: open research question; no Mainline mechanism selected.

## Clarification candidates

### Release Identity ≠ Artifact Schema Identity
ENA release version and an artifact's schema-contract version may legitimately differ.
Potential future clarification:
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
Preferred loop:
`Historical incident → concrete failure claim → current ENA mapping → false claim that became possible → should current ENA stop it? → COVERED / AMBIGUOUS / HOST-SPECIFIC / GAP`

Current HAR checkpoint: **13 replay cases, 0 NORMATIVE_GAP**.

## Contribution rule
Do not append parallel-agent advice directly into this file by default. Put one contribution per artifact under `collaboration/inbox/`; reconcile it separately. This directory represents structured candidate state, not an uncontrolled shared scratchpad.
