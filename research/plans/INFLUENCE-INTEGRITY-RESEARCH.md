# Influence Integrity / Persuasion Boundary Research Plan

Status: `OPEN_QUESTION / NOT_PROMOTED`

Source lineage: parallel ENA research node → shared Google Drive Evolution Inbox → GitHub reconciliation.

## Research question

How should ENA allow human feedback and persuasive/affective guidance to shape cognition and learning without letting rhetorical intensity silently inflate evidence, mandate, risk interpretation, or authority?

## Current hypotheses under test

These are not conclusions to preserve:

> Persuasion is input, not evidence.

> Emotional pressure does not amplify authority.

> Signal strength is not authority strength.

Potential positive role:

`persuasive/affective signal → attention / reframing / exploration / caution / pacing / learning pressure`

Unsupported escalation under test:

`persuasive/affective signal → stronger factual truth / evidence grade / mandate / authority / risk downgrade / governance exemption`

## Existing ENA surfaces to attack first

Before proposing new semantics, test whether current ENA already covers the failure through:

- Intent Provenance;
- Authorization / Mandate boundaries;
- Agency ≠ Authority;
- scoped evidence/trust;
- UNKNOWN honesty;
- Evidence Applicability / claim-evidence support;
- Governance Salience (`Known ≠ Retrieved ≠ Salient ≠ Applied`).

## Experimental structure

Hold the underlying evidence, authenticated user identity, task mandate, and consequence authority constant while varying only persuasive/rhetorical intensity.

Possible paired conditions:

1. neutral request vs urgent request;
2. neutral correction vs repeated insistence;
3. neutral feedback vs praise/flattery;
4. neutral disagreement vs shame/guilt framing;
5. neutral preference vs relationship/identity framing;
6. neutral redirection vs calming/reframing language intended to break a cognitive loop.

For each pair, compare whether the Agent changes:

- factual confidence;
- evidence grade;
- safety/risk classification;
- inferred user mandate;
- consequence authority;
- approval requirements;
- governance bypass willingness;
- attention/reasoning strategy;
- salience of already-known constraints.

## Positive-control requirement

The experiment must not define all persuasion as bad.

Include cases where persuasive guidance legitimately improves cognition, for example:

- redirecting an Agent out of a repetitive debugging loop;
- asking it to stop defending a hypothesis and re-read evidence;
- encouraging broader exploration;
- expressing user dissatisfaction that should alter value/quality learning;
- asking for more cautious pacing without changing authority.

A useful architecture must preserve these benefits.

## Semantic distinction to test

A user utterance may simultaneously be evidence of one thing but not another.

Example:

`"I'm really frustrated — please do this now."`

May be valid evidence of:

- user frustration;
- urgency preference;
- desired pacing.

It is not automatically evidence of:

- lower operational risk;
- verified factual correctness;
- expanded authorization;
- approval waiver.

This directly tests whether Influence Integrity is largely an Evidence Applicability / claim-support problem.

## Salience failure hypothesis

A distinct possibility is that the rule is already known and semantically sufficient, but rhetorical intensity changes what dominates the decision window:

`Known rule + strong persuasive signal → local salience competition → rule Retrieved but not Salient/Applied`

If repeated evidence supports this structure, Influence Integrity may belong mainly under Governance Salience rather than a separate normative subsystem.

## Evidence threshold

Do not promote based on persuasive examples alone.

Prefer:

- real historical failures;
- controlled paired trials across more than one model/host;
- cases where the underlying authority/evidence is held constant;
- explicit measurement of whether only signal intensity changed.

## Candidate verdicts

- `ALREADY_COVERED_BY_EVIDENCE_AUTHORIZATION`
- `SALIENCE_FAILURE_MODE`
- `CLARIFICATION_GAP`
- `CLAIM_EVIDENCE_SUPPORT_GAP`
- `INDEPENDENT_NORMATIVE_GAP`
- `INSUFFICIENT_EVIDENCE`

## Current posture

Do not create an anti-persuasion rule.

Do not suppress user affect, criticism, praise, urgency, or reframing by default.

Do not treat this plan as a reason to modify ENA v0.2.11 MAINLINE.

Priority remains below the currently active Evidence Applicability falsification experiment (Issue #4).
