# Reconciliation — V2.4.1 Targeted Revalidation and V2.x Closure

```yaml
project: ena
artifact_type: RECONCILIATION
status: ACCEPTED
created_at: "2026-08-21T16:53:00+08:00"
contribution_refs:
  - "PR #30 — V2.4 independent validation / INDEPENDENT_VALIDATION_SUPPORTED_WITH_RESIDUALS"
  - "PR #31 — V2.4.1 residual-closure successor / daacab1f042c38f3856ef4d0366febd1b5e47600"
  - "freeze b3d16988b65ea189b7ee82fd4b665bdb8bbb1f84"
  - "PR #33 — REVALIDATION_BY_PRIOR_FALSIFIER_SUPPORTED"
reviewer:
  kind: "ChatGPT"
  session_or_run_ref: "project-continuation reconciliation session"
current_baseline: "ENA v0.3.2 FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE / NOT_MAINLINE"
outcome: ACCEPT_FOR_IMPLEMENTATION
authority_note: "implementation authorized for a successor release candidate only; promotion/release-current mutation is NOT authorized by this reconciliation"
```

## Contribution summary

The V2.4 independent validator found one new residual in the V2.4 successor: dict-key versus inner-id registry identity ambiguity (F1), plus a lower-level obligation-status vocabulary gap (F2). DSH produced the narrowly scoped V2.4.1 research successor at `daacab1f042c38f3856ef4d0366febd1b5e47600`, froze it at `b3d16988b65ea189b7ee82fd4b665bdb8bbb1f84`, and stopped implementation work pending targeted revalidation.

The same WorkBuddy session that originally falsified F1 then performed `REVALIDATION_BY_PRIOR_FALSIFIER`, submitted as PR #33, and returned `REVALIDATION_BY_PRIOR_FALSIFIER_SUPPORTED`.

## Evidence verified

- V2.4.1 frozen implementation uses one explicit dict-form identity rule across support, evidence, root, obligation, and authority registries: dict key is authoritative; a contradictory explicit inner id is `REGISTRY_MALFORMED`; missing inner ids may be backfilled where supported.
- F2 is enforced as defense-in-depth against the existing shipped obligation-status vocabulary; the vocabulary itself was not expanded.
- Author-side accumulated replay: 148 fixtures, `UNEXPECTED_VERDICTS: 0`, 98/98 frozen V2.4 verdicts preserved, 25/25 prior WorkBuddy probes matched, 25/25 closure controls matched, zero exceptions.
- Prior falsifier revalidation independently re-executed the F1 family and confirmed the old V2.4 failure reproduces while V2.4.1 closes it across all six registry surfaces without rejecting the tested legitimate representations.
- Prior falsifier revalidation independently re-executed the F2 checks and confirmed outside-vocabulary statuses are rejected while in-vocabulary semantics remain governed by the existing baseline.
- Prior falsifier independently reproduced the 148-fixture replay with zero unexpected verdicts and no directly caused regression.
- PR #33 evidence was accepted and merged as evidence only; this does not itself constitute promotion.

## Current ENA / project mapping

This work is no longer an open research-hardening question. The independently discovered residual was reproduced, minimally corrected, frozen, and revalidated by the same falsifier that found it.

The research evidence now supports carrying the V2.4.1 mechanism set forward into an implementation candidate. It does not establish production truth for self-declared external registries, grades, mandate content, caller-controlled time, or other explicitly retained trust boundaries.

## Conflicts / overlap

- The WorkBuddy revalidation report contained one local-clone observation stating that current `origin/main` did not contain V2.4.1. GitHub's current `main` does contain `research/prototypes/v2-machine-contract-hardening/v2.4.1/`. This is treated as a validator-environment bookkeeping error and does not affect the revalidation verdict.
- `FREEZE-MANIFEST-V241.md` contains stale `(private)` repository metadata; the repository is public. Non-semantic.
- `freeze_hashes_v241.py` is not covered by the freeze digest table. It is a helper, not the frozen semantic implementation set.
- `run_v241.py` contains stale 149/26 prose while the executable corpus is 148/25. Executed counts and results are authoritative for this reconciliation.

## Outcome

`ACCEPT_FOR_IMPLEMENTATION`

The V2.4.1 research successor is accepted as the evidence-backed mechanism source for the next implementation candidate.

This is not `PROMOTED`, not `MAINLINE`, and not a release decision.

## Rationale

- The main false-confidence defects discovered in V2/V2.1/V2.2/V2.3 were cumulatively closed in V2.4.
- The fresh V2.4 independent validator found a new residual rather than merely replaying the author's corpus.
- V2.4.1 made the smallest coherent correction to that residual and preserved all 98 frozen V2.4 verdicts.
- The original falsifier independently confirmed closure and regression behavior in a closed-scope revalidation.
- Further open-ended V2.x hardening would now have declining evidentiary value relative to the governance and complexity cost. The next useful falsification surface is the actual implementation candidate.

## Authority boundary

Authorized by this reconciliation:

- use the frozen V2.4.1 mechanisms as input to a new implementation/release candidate;
- translate the research mechanism into the shipped schema/tool/package surfaces;
- preserve the accumulated regression corpus as implementation tests;
- close the V2.x research-hardening loop.

Not authorized by this reconciliation:

- modifying or replacing `releases/current/`;
- declaring the implementation candidate Mainline;
- production deployment;
- claiming that retained external trust boundaries have been eliminated;
- self-validation or self-promotion by the implementation author.

## Next action

1. **Next actor: DSH, role = IMPLEMENTATION AUTHOR.** Build the next ENA implementation candidate from the frozen V2.4.1 mechanism set. Do not reopen the V2.x research loop and do not modify `releases/current/` during candidate authoring.
2. Map the accepted mechanisms into the actual shipped contract/schema/tool surfaces rather than copying the research prototype blindly.
3. Carry forward the accumulated adversarial and positive corpus, including the external WorkBuddy probes, as regression tests.
4. Freeze the implementation candidate separately and return its immutable refs plus an implementation-delta report.
5. **Then** use a fresh independent validator for the implementation candidate. The prior WorkBuddy revalidation counts as prior-falsifier closure evidence, not fresh blind validation of the implementation.
6. Promotion remains a later Host decision after implementation-candidate validation.

## Normative / canonical status after reconciliation

- V2.4.1 research successor: `RECONCILED / ACCEPTED_FOR_IMPLEMENTATION / NOT_MAINLINE / NOT_PROMOTED`.
- V2.x research-hardening loop: `CLOSED`.
- `releases/current/`: unchanged at v0.3.2.
- Next phase: implementation candidate authoring and fresh validation.

Do not rewrite or delete the source contributions. Reconciliation != promotion.
