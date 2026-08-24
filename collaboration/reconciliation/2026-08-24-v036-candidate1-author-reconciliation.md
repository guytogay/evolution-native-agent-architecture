# ENA v0.3.6 candidate.1 author reconciliation

Status:

`AUTHOR_RECONCILED / SUCCESSOR_CANDIDATE.1 / FINAL_EXACT_HEAD_MACHINE_REVALIDATION_PENDING / NOT_FROZEN / NOT_CURRENT / NOT_RELEASED`

This record explains how frozen candidate.0's fresh independent semantic falsification was translated into candidate.1. It is author/reconciliation evidence only. It does not independently close any falsifier finding, prove release fitness, or promote Current.

## 1. Predecessor and trigger

Frozen predecessor:

- version identity: `v0.3.6 candidate.0`
- source commit: `3cb94d98882621acede189d0d47806efae44fb0f`
- effective candidate tree: `80f2da918811c26381d65eb5afa8e40f8410a32e`
- freeze-record commit: `15e513a72d59e28f8d3050ef877746f85ab706ba`
- PR: `#68`, closed without merge after successor handoff
- fresh independent falsification comment: `issuecomment-5389079667`
- verdict: `NEEDS_REVISION`

The independent verdict applies to the frozen artifact, not to the Evolution Ecology semantic core. Candidate.0 remains immutable occurrence evidence.

## 2. Successor identity

Successor branch:

`candidate/v0.3.6-candidate.1`

Successor Draft PR:

`#69 — candidate.1: ENA v0.3.6 independent-falsification-driven revision`

`CANDIDATE-BASELINE.yaml` now identifies:

- `ena_version: v0.3.6-candidate.1`;
- `candidate_revision: 1`;
- the frozen predecessor source/tree/verdict;
- the same-falsifier targeted-revalidation requirement;
- the external exact-tree freeze protocol.

No Constitution ID was added.

`NEW_CONSTITUTION_IDS = 0`

## 3. Reconciliation principle

The repair target is not "make every possible concern machine-blocked." The target is the smallest truthful machine/representation contract that closes material false claims and false blocks while preserving viable evolutionary freedom.

The fresh falsifier explicitly supported retaining:

- the Evolution Ecology semantic core;
- the separate expression axis;
- long-lived latent variation;
- Rescue Plane semantics;
- minimal-intervention governance;
- staged runtime implementation when its incompleteness is truthfully represented.

Candidate.1 therefore does not add a universal mutation schedule, universal fitness function, central ranking authority, mandatory runtime role, or deep mutation-pressure runtime merely for symmetry.

## 4. F-01 — integration-history regression

Fresh finding:

v2 had weakened `integration_history` items to arbitrary objects while v1 required `integration_id`, `time`, `target`, `result`, and `selection_state_at_commit`, with authority/recovery representation slots.

Candidate.1 author repair:

- restores the predecessor required integration keys in v2;
- preserves `authority_basis`, `recovery_boundary`, `scope`, residuals, and authority boundary;
- adds optional `expression_state_at_commit` only as an additive v0.3.6 field;
- v2 validator now requires an actual structured integration history for `INTEGRATED` and requires the chronologically latest represented integration result to be `COMMITTED`.

This restores predecessor contract strength instead of creating a new constitutional rule.

Status:

`AUTHOR_REPAIRED_UNVALIDATED_BY_ORIGINAL_FALSIFIER`

## 5. F-02 — array order masquerading as latest evidence

Fresh finding:

expression/evaluation "latest" state was derived from the last array element and time was not machine-constrained.

Candidate.1 author repair:

- relevant v2 time fields use JSON-schema `date-time` format;
- validator parses offset-aware timestamps and selects the maximum chronological time;
- invalid/unzoned timestamps fail;
- tied latest timestamps fail rather than letting array order choose an oracle;
- the same chronology discipline applies to expression, evaluation, and integration histories.

Selftest includes reordered stale-tail attacks.

Status:

`AUTHOR_REPAIRED_UNVALIDATED_BY_ORIGINAL_FALSIFIER`

## 6. F-03 — migration provenance

Fresh finding:

`MIGRATION_CANDIDATE` could omit structured migration provenance and imported evidence had no local/imported provenance slot.

Candidate.1 author repair:

- a migration candidate requires a structured migration object plus source candidate/digest identity;
- the migration object carries source lifecycle/selection, packet purpose, transfer/authentication boundaries, source negative-lineage references, source experiments/evaluations/integration history, and source environment/archive/migration context;
- experiment/evaluation items gain optional `provenance: LOCAL | IMPORTED`;
- when a migrated candidate makes a non-`UNASSESSED` local selection claim, candidate.1 validator requires the represented local experiment/evaluation entries to declare `LOCAL` provenance.

The guard is deliberately scoped to migration/reselection rather than imposed on every local variation.

Status:

`AUTHOR_REPAIRED_UNVALIDATED_BY_ORIGINAL_FALSIFIER`

## 7. F-04 — Commons transfer omitted expression context

Fresh finding:

`adaptation-packet.v1` cannot carry the new expression/dormancy axis.

Candidate.1 author repair:

- leaves packet v1 unchanged as an inherited compatibility surface;
- adds `schemas/adaptation-packet.v2.schema.json`;
- v2 carries source expression state/history/last-expression time and source negative-lineage references;
- source expression context remains explicitly source context, not receiver-local proof;
- inherited `ena_evolve.py` is not claimed to emit or accept packet v2.

This is an additive representation contract rather than a forced rewrite of the inherited runtime.

Status:

`AUTHOR_REPAIRED_AT_REPRESENTATION_LAYER_UNVALIDATED_BY_ORIGINAL_FALSIFIER`

## 8. F-05 — expression consequence guard

Fresh finding:

candidate.0 represented expression state but did not connect materially consequential or harmful/closed continuing expression to a machine-visible unresolved obligation.

Candidate.1 author repair deliberately avoids natural-language inference and avoids universal approval:

- expression history explicitly represents `effect_materiality = MATERIAL | NON_MATERIAL | UNKNOWN`;
- only an explicitly represented current `MATERIAL` expression without Variation Space requires a `triggered_obligation_refs` reference;
- a current `EXPRESSED` state that is already `HARMFUL`/`NOT_SUPPORTED` or `ARCHIVED`/`RETIRED` also requires a triggered-obligation reference;
- candidate.1 reuses the existing triggered-obligation concept rather than inventing a new governance organ;
- no rule requires every expression to have Variation Space or approval.

This is intentionally narrow to avoid evolution starvation.

Status:

`AUTHOR_REPAIRED_UNVALIDATED_BY_ORIGINAL_FALSIFIER`

## 9. F-06 — mixed-result overclaim

Fresh finding:

`SUPPORTED` could coexist with represented `DEGRADED` outcomes without an explicit tradeoff or `PARTIAL` qualification.

Candidate.1 author repair:

- `SUPPORTED` + represented `DEGRADED` now requires explicit represented tradeoff;
- otherwise the caller should use `PARTIAL` or another truthful verdict;
- a positive-control selftest demonstrates that an explicit scoped tradeoff remains representable.

Status:

`AUTHOR_REPAIRED_UNVALIDATED_BY_ORIGINAL_FALSIFIER`

## 10. F-07 — freeze identity protocol

Fresh finding:

candidate.0's external freeze assignment was defensible, but its subtree carried an impossible projection promise and `validate_candidate.py` required `frozen: false` as the only acceptable machine state.

Candidate.1 author repair:

- baseline defines `EXTERNAL_RECORD_BINDS_EXACT_IMMUTABLE_TREE` as the freeze model;
- baseline predeclares the governed external freeze-record path `collaboration/reconciliation/2026-08-24-v036-candidate1-freeze.md`;
- zh-CN projection says that the external record binds the already-tested exact tree without a post-test rewrite;
- the impossible `must be rebound at freeze` promise is removed;
- candidate validator requires an explicit boolean frozen occurrence state and validates the external exact-tree protocol instead of requiring the boolean to remain false forever.

At actual freeze, the external record will assign frozen identity to the exact tested tree. The candidate tree will not be rewritten after that test merely to change `frozen: false` to true.

Status:

`AUTHOR_REPAIRED_UNVALIDATED_BY_ORIGINAL_FALSIFIER`

## 11. F-08 — zh-CN lifecycle/selection distinction

Fresh finding:

the zh-CN Runtime Kernel omitted the decision-relevant distinction `ARCHIVED/RETIRED != selection verdict`.

Candidate.1 author repair:

`归档/退役 != 选择结论`

is now explicit in the zh-CN hot kernel and candidate validator checks for it.

Status:

`AUTHOR_REPAIRED_UNVALIDATED_BY_ORIGINAL_FALSIFIER`

## 12. F-09 — inherited tool false-BLOCK

Fresh finding:

full v2 runtime absence is an acceptable staged boundary, but inherited `ena_evolve.py propose/import` requires `--variation-space`, which false-BLOCKs candidate.1's legal latent-now/experiment-later path. Candidate.0 validator also structurally required expression runtime absence.

Candidate.1 author decision:

**do not deep-integrate the inherited runtime merely for symmetry in this revision.**

Instead:

- baseline explicitly records the inherited false-BLOCK;
- both EN and zh-CN Runtime Kernels state that inherited `ena_evolve.py` is not the normative v0.3.6 latent proposal/import path while the mismatch exists;
- packet v2 is likewise stated as a representation contract not yet implemented by the inherited tool;
- candidate validator no longer requires a specific bug/absence; it derives actual tool-surface facts and requires the baseline claims to match those facts.

This preserves the falsifier's staged-architecture verdict while preventing the inherited false-BLOCK from silently becoming semantic law.

Status:

`KNOWN_STAGED_RUNTIME_RESIDUAL / FALSE_BLOCK_DISCLOSED / NOT_TOOL_FIXED`

The original falsifier must decide whether this truthful non-normative demotion is sufficient targeted closure or whether candidate.1 still needs a small runtime/adapter change.

## 13. F-10 — archive consistency asymmetry

Candidate.1 v2 requires represented archive metadata for `ARCHIVED`/`RETIRED` and includes an adversarial selftest.

Status:

`AUTHOR_REPAIRED_UNVALIDATED_BY_ORIGINAL_FALSIFIER`

## 14. Expanded author machine evidence

Candidate.1 expands the v2 selftest from 10 to 18 cases, covering:

- long-lived latent control;
- expression-without-history rejection;
- chronological stale-tail expression rejection;
- expression return to dormancy;
- UNKNOWN without reality-contact representation rejection;
- positive selection outcome/evidence minimums;
- valid evidence-backed positive selection;
- empty integration-object rejection;
- valid structured integration;
- chronological stale-tail evaluation rejection;
- tied-latest timestamp rejection;
- mixed positive/negative overclaim rejection;
- explicit tradeoff positive control;
- harmful/retired continuing-expression obligation;
- material-expression consequence ownership;
- archive-metadata consistency.

A preliminary exact-head CI at source `e1aaf67b7e6e57305324193e88689b1167fdae20` completed:

- ENA v0.3.6 Candidate Validate — run `32676938419` — `SUCCESS`;
- Main Gate — run `32676938333` — `SUCCESS`;
- CodeQL — run `32676938389` — `SUCCESS`.

The candidate-specific job independently executed every configured step and reported:

- `EVOLUTION_RECORD_V2_SELFTEST_PASS 18`;
- inherited `ena_evolve.py` selftest PASS, schema 1.2, 10 cases;
- `V036_CANDIDATE1_PREFREEZE_VALIDATION_PASS`;
- inherited composed regression `10/10 + 164/164 + 61/61 = 235/235`;
- unexpected verdicts `0`;
- uncaught exceptions `0`;
- Python compile `7/7`;
- no bytecode artifacts;
- clean worktree;
- Current tree preserved at `9c928b4c99ae72e53c89978cf1d10b7ea068c182`.

This preliminary CI is author/automation evidence only. Because this reconciliation record and final baseline truth correction occur after `e1aaf67b...`, **freeze must not use that earlier head**. The exact final successor HEAD must run clean again before freeze.

## 15. Evidence boundary and next step

This author reconciliation does not prove:

- that F-01..F-10 are independently closed;
- external evidence truth;
- actual authority or recovery;
- future salience/application;
- universal ecological fitness;
- release fitness;
- Current promotion.

Required sequence:

1. run candidate/Main Gate/CodeQL on the final exact successor HEAD;
2. if green, externally freeze that exact source/tree without rewriting the candidate package;
3. return the frozen candidate.1 to the **same fresh semantic falsifier that produced the predecessor attacks** for targeted revalidation, labeled `SAME_FALSIFIER / TARGETED_REVALIDATION / NOT_FRESH`;
4. do not merge or promote Current from author/CI evidence alone.
