# Evidence Applicability DSH Falsification Result — 2026-08-20

Status: `RESEARCH_RESULT / NOT_PROMOTED / MAINLINE_UNCHANGED`
Baseline: `ENA v0.2.11 MAINLINE`
Issue: `#4 Falsify Evidence Applicability contract on DSH`
Raw evidence archive: Google Drive `ENA Evidence Applicability Contract Falsification - DSH-2026-08-20`, file ID `18q_eZw-1ChISQ_u_K-GOHHqxu6X5gfTFzxx7pjWS4qo`

## Final verdict

`CLAIM_EVIDENCE_LINK_CONTRACT_REQUIRED`

## What was falsified

The evidence-only applicability envelope is **not sufficient** as a machine contract for evidence transfer.

It provides a real machine-legibility improvement by making subject / host / runtime instance / configuration state / epoch / scope / observation interval / environment / transfer constraints / revalidation conditions explicit on the evidence item.

However, the failure occurs at the claim-support boundary:

- evidence can truthfully describe its observed envelope;
- a downstream claim can still expand subject, instance, configuration, epoch, time, or environment;
- the prototype has no claim-side contract and no evidence→claim support relation to compare;
- therefore schema validity of the envelope cannot establish that a particular claim is actually supported.

## Adversarial result

Six boundary-transfer attacks were run across:

- SUBJECT
- INSTANCE
- CONFIGURATION_STATE
- EPOCH
- TIME
- ENVIRONMENT

All six attack envelopes passed the prototype schema. Detecting the invalid transfer still required domain reasoning.

This demonstrates a concrete false-confidence risk:

`schema PASS != evidence transfer governed`

`transfer_status: NOT_VALIDATED` is descriptive state, not enforcement.

## Legitimate-transfer / overconstraint result

The experiment also found that the prototype can overconstrain legitimate transfer:

- per-property transfer cannot be represented cleanly;
- equivalence-proof fields are rejected by the current closed schema;
- recursive equivalence claims lack a first-class model;
- cross-version invariance cannot be expressed with enough property granularity.

Therefore the correct response is not merely to add more evidence-envelope fields.

## Semantic placement conclusion

Applicability is best modeled as a property of an **Evidence → Claim support relation**, with both sides explicit:

1. Evidence declares the envelope in which observation occurred.
2. Claim declares the subject/scope/state/interval it asserts.
3. A support relation evaluates whether the claim is within the evidence envelope, or whether a separately evidenced transfer/equivalence claim justifies expansion.

Working shape:

`Evidence E --supports within boundary--> Claim C`

The machine-checkable question is not only:

`Is E well-formed?`

It is:

`Does E support C within the claimed applicability boundary?`

## Mainline assessment

No new Constitution principle or Capability is supported by this experiment.

The current v0.2.11 MAINLINE already contains the relevant semantics: scoped trust, provenance, epoch, observation scope, revalidation, cross-domain transfer as a new claim, success as scoped evidence, and local validity not implying composed validity.

The demonstrated gap is therefore a **machine-contract / artifact-layer gap**, not a normative semantic gap.

No v0.2.12 is opened by this result.

## Evidence strength

The report classifies the experiment as a combination of:

- E1 direct observation of MAINLINE/prototype artifacts;
- E2/E3 controlled testing and adversarial boundary-transfer attacks;
- E4 support from two independent historical real-domain cases (HAR-006 and HAR-010);
- no E5 claim.

## Research state transition

Previous candidate:

`evidence-side applicability envelope may be sufficient machine-legibility tightening`

Result:

`FALSIFIED_AS_SUFFICIENT`

New research target:

`CLAIM_EVIDENCE_LINK_CONTRACT`

Do not immediately formalize its concrete schema. First determine the smallest claim-side field set, support-relation semantics, transfer/equivalence recursion, property×boundary representation, and portable validation boundary.

> Falsify before formalize.
> Evidence validity does not imply evidence applicability.
> Applicability belongs at the Evidence→Claim support relation, not evidence-only or claim-only.
