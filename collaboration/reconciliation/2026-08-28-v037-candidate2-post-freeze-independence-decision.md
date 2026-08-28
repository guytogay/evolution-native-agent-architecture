# ENA v0.3.7 candidate.2 post-freeze independence decision

Date: 2026-08-28

## Decision

`FRESH_BLIND_SUCCESSOR_REVIEW_WARRANTED / ONE_FINAL_SEARCH_SPACE_INDEPENDENCE_CYCLE / NOT_RELEASE_AUTHORITY`

Frozen target:

- identity: `v0.3.7-candidate.2`
- exact frozen source: `bda470e0a6b170cec61225a905957a501454a2fe`
- exact frozen candidate subtree: `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`
- exact pre-freeze gate: workflow run `33095987843` — SUCCESS
- freeze record: `collaboration/reconciliation/2026-08-28-v037-candidate2-freeze.md`

Current remains `v0.3.6 / CURRENT / FIELD_VALIDATION` and is not changed by this decision.

## Why one more fresh blind cycle pays epistemic rent

This is not an automatic rule that every successor receives another validator forever.

Candidate.2 warrants one fresh blind search-space cycle because the evidence line contains a specific information-gain signal:

1. frozen candidate.1 received a genuinely fresh blind semantic review and that review found four material semantic defects plus one active-package drift that author-side evidence had not exposed;
2. after candidate.2 repaired those known findings, an author-side **nearby open-branch probe** still found two additional homologous decision-changing shapes — shallow durable source-history representation and same-sequence conflicting attempt chronology;
3. candidate.2 therefore changes executable/validator behavior on several sensitive boundaries: migration provenance/history, integration chronology, Authority applicability ordering, and Effect Lifecycle ordering;
4. author-side exact regression proves the known shapes are closed, but those tests were written with the findings already known and therefore cannot restore search-space independence;
5. the candidate is now frozen to one immutable tree, so a fresh reviewer can explore it without moving-target ambiguity.

The key observation is:

```text
FRESH_PREDECESSOR_FINDINGS
  -> SUCCESSOR_REPAIR
  -> AUTHOR_NEARBY_PROBE_FINDS_NEW_HOMOLOGOUS_GAPS
  -> SEARCH_SPACE_INDEPENDENCE_STILL_HAS_MEASURED_VALUE
```

That is enough epistemic rent for one more fresh cycle.

## Why this is narrower than candidate.1 review

Candidate.2 is not a new architectural expansion. Its semantic radius is bounded around repairs and active projection.

Therefore the fresh review should not be framed as “prove all ENA semantics again.” It should independently inspect the frozen candidate's actual contracts and executable/reference semantics, grow its own attack tree, and pay particular attention to false confidence and false blocking **without being told the author's known attack map or repair list**.

The reviewer may discover distant shapes; the project manager must not constrain it to the known repairs. But the task itself remains one frozen-successor review cycle, not a demand for universal completeness.

## Stopping discipline

This decision authorizes exactly **one fresh blind A-S -> A-P cycle** for frozen candidate.2 before release reconciliation.

After it is sealed:

- if a material candidate-byte defect is found, candidate.2 remains frozen occurrence truth and any correction requires a new successor identity;
- if findings are oracle defects, evidence-boundary issues, intentional residuals, Host-specific possibilities, or non-contract possibilities, reconcile them without inventing new universal rules;
- if no material blocker is found, proceed to Phase B/release reconciliation;
- attack cardinality remains `OPEN` regardless of outcome.

This is a stopping rule for the current evidence question, not a promise that no future research can ever reopen the architecture.

A later successor, if required, does **not** automatically inherit another fresh-review requirement. Its post-freeze independence decision must again depend on semantic radius and expected information gain.

## Information boundary

The current project-manager session is ineligible to perform this fresh A-S because it has already seen:

- candidate.1 independent findings;
- candidate.2 repair design;
- author nearby probes;
- regression expectations;
- exact gate construction and results.

A fresh reviewer must not receive those materials before A-S is sealed.

The blind semantic view must prevent candidate-local self-priming by withholding pre-seal history/oracle roles while retaining executable semantic bytes unchanged. Candidate.1's repaired blind-view method is the precedent; candidate.2 requires a new manifest bound to its own exact frozen source/blob identities.

Sequence:

```text
FROZEN CANDIDATE.2
-> DECLARED BLIND SEMANTIC VIEW
-> FRESH A-S
-> SEAL A-S ARTIFACT
-> A-P FULL-PACKAGE/ORACLE INSPECTION
-> PERSIST A-P
-> STOP BEFORE PHASE B
```

## Next governed action

`PREPARE_CANDIDATE2_BLIND_SEMANTIC_VIEW_AND_FRESH_INTAKE`

The project manager may prepare the view, manifest, neutral entry, validation branch, and intake issue. The project manager must not perform or simulate the fresh A-S itself.
