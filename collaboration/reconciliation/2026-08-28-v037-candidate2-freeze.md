# ENA v0.3.7 candidate.2 freeze record

Date: 2026-08-28

## Status

`FROZEN_CANDIDATE.2 / EXACT_PREFREEZE_PASS / SUCCESSOR_REPAIR_RECONCILED / NOT_CURRENT / NOT_RELEASED / POST_FREEZE_INDEPENDENCE_RELEASE_DECISION_NEXT / ATTACK_CARDINALITY_OPEN`

This record freezes ENA v0.3.7 candidate.2 after the frozen candidate.1 received a fresh blind semantic A-S/A-P review, Phase B required a successor, candidate.2 repaired the demonstrated defects plus focused homologous branches, committed readback re-probing passed, candidate-facing state was reconciled, and one exact-source pre-freeze gate passed.

The freeze is an **external exact-tree binding**. The tested candidate subtree is not rewritten merely to set an internal `frozen: true` flag.

This freeze does not promote candidate.2 to Current, does not constitute fresh independent acceptance of candidate.2, and does not close attack cardinality.

## Frozen candidate.2 identity

Candidate identity:

`v0.3.7-candidate.2`

Frozen source commit:

`bda470e0a6b170cec61225a905957a501454a2fe`

Effective candidate path:

`releases/v0.3.7-candidate/`

Frozen candidate Git tree:

`d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`

Observed candidate file count at exact gate:

`118`

Current at the same source commit remains:

`releases/current/`

Current Git tree:

`7dcbb3934883ffa6cc5292a662588cafc1533cff`

No `releases/current/**` change is part of candidate.2.

## Candidate cargo boundary

The final candidate cargo/self-description commit before exact validation was:

`aba6f12cabc84146c92809bd7d8293a3c907dc55`

Its `releases/v0.3.7-candidate/` subtree is exactly:

`d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`

Subsequent commits on the candidate branch before the successful exact run changed only GitHub validation tooling/trigger surfaces outside the candidate subtree. The exact run source `bda470e0...` retained the same candidate tree.

Therefore the freeze binds the exact tree actually tested, not a mutable branch label or an inferred cargo state.

## Predecessor occurrence truth

Frozen predecessor candidate.1 remains immutable:

- identity: `v0.3.7-candidate.1`
- frozen source: `ae6903464133cb5bcf3cd8909ecae1215fe0b9ba`
- frozen candidate subtree: `c0458e0d7ea417b841cbf4c8bf6e64e4aff37319`
- fresh blind A-S seal: `2e6b46aeedc1945a03aac93620ad36aa1ccbd70f`
- A-P completion: `b970148fe9596ea9cad0a2817a3b399a1d2b75f5`
- Phase-B verdict: `NEEDS_REVISION / CANDIDATE_2_REQUIRED`

Candidate.1 was not mutated after freeze to absorb candidate.2 repairs.

Frozen candidate.0 remains earlier occurrence truth:

- identity: `v0.3.7-candidate.0`
- frozen source: `d0e793593184740d9732902e948afd48ed96ae2f`
- frozen subtree: `cffbf76fe1448b020b637c78d1f7ae46e4c0115b`
- fresh blind Phase-A seal: `5ba3d241efa460fe170253860ad67045aa1d96a5`
- Phase-B verdict: `NEEDS_REVISION / CANDIDATE_1_REQUIRED`

## Candidate.2 repair lineage

Detailed reconciliation:

`collaboration/reconciliation/2026-08-28-v037-candidate2-successor-repair-reconciliation.md`

Focused repair round 1:

- workflow run: `33090294820`
- candidate cargo commit: `613c1e8be898865ce674199118618c0f9389da97`

Focused nearby open-branch probe:

- workflow run: `33090585653`
- result: observation-only SUCCESS

Focused repair round 2:

- workflow run: `33091573678`
- candidate cargo commit: `34458c2ba0b94b82d182afe2606efe48e741bcda`

Committed readback re-probe:

- workflow run: `33091652046`
- result: SUCCESS

Status-only pre-freeze transition:

- workflow run: `33095122958`
- final candidate cargo/self-description commit: `aba6f12cabc84146c92809bd7d8293a3c907dc55`

The transition was constrained to candidate self-description surfaces and machine-checked that validators, schemas, reference tools/fixtures, and Current were unchanged.

## Exact pre-freeze gate

Workflow:

`ENA v0.3.7 Candidate.2 Exact Pre-Freeze Gate`

Successful run:

`33095987843`

Result:

`SUCCESS`

Exact run source:

`bda470e0a6b170cec61225a905957a501454a2fe`

Exact candidate subtree:

`d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`

Exact Current subtree:

`7dcbb3934883ffa6cc5292a662588cafc1533cff`

Two earlier gate attempts failed safely in validation tooling rather than candidate bytes:

- run `33095464230`: incorrect historical schema-title normalization in the gate oracle;
- run `33095677352`: successor harness called a nonexistent Authority API name.

Those harness defects were corrected outside candidate cargo. Candidate subtree identity remained unchanged.

The successful exact gate passed all composed stages, including:

- exact source/candidate-tree/Current-tree binding;
- semantic-trunk byte parity and bounded identity projection;
- routing, optionality, Host-equivalent, and deferred-lineage checks;
- inherited composed-validator regression;
- v2 record/helper selftests and CLI roundtrip;
- bundled reference selftests;
- relocated legacy compatibility regressions;
- inherited author attack replay;
- inherited anti-ablation replay;
- candidate.1 successor targeted/open-branch regression replay;
- candidate.2 A-S/A-P-derived record, Authority, Effect, and identity regressions;
- zh-CN paired operational fixture structure;
- candidate-local self-containment;
- Python compile plus bytecode/symlink hygiene;
- final exact-tree cleanliness.

The gate explicitly emitted:

```text
CANDIDATE2_EXACT_PREFREEZE_VERDICT=PASS
attack_cardinality=OPEN
fresh_independent_candidate2_review_by_this_gate=NO
external_truth=NOT_ESTABLISHED
freeze_authority=NOT_ASSIGNED_BY_THIS_WORKFLOW
```

This external governed record supplies the freeze authority after the exact gate passed.

## Freeze rule

Tree `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf` is now frozen occurrence truth for `v0.3.7-candidate.2`.

Any material correction to candidate cargo after this record requires a new successor identity such as `v0.3.7-candidate.3`. Do not silently mutate this frozen tree and continue calling it candidate.2.

Research/control-plane records and validation tooling may evolve outside the frozen subtree, but they cannot retroactively change the bytes or evidence bound here.

## Evidence boundary

The candidate.2 repair and exact pre-freeze evidence is author/project-manager-side machine validation. It is useful evidence, but it is not a fresh independent candidate.2 review.

The fresh independent evidence that triggered this successor applies directly to frozen candidate.1. Candidate.2 has been regression-checked against those sealed findings and nearby homologous branches, but freshness/independence is a separate epistemic dimension.

Therefore:

```text
SAME_FALSIFIER_REPAIR_REVALIDATION != FRESH_INDEPENDENT_REVIEW
EXACT_TREE_PASS != CLOSED_ATTACK_SPACE
FROZEN != RELEASED
FROZEN != CURRENT
```

## Visible residuals

The source/receiver `candidate_id` namespace collision remains allowed because no current ENA contract establishes universal cross-environment candidate-ID uniqueness.

Classification:

`VISIBLE_RESIDUAL / NO_CURRENT_GLOBAL_NAMESPACE_CONTRACT / NOT_AUTOMATIC_RELEASE_BLOCKER`

Rule:

`NO_CURRENT_CONTRACT -> DO_NOT_INVENT_UNIVERSAL_RULE`

Attack cardinality remains `OPEN`.

## Required next decision

Perform one explicit **post-freeze independence/release reconciliation** before any promotion decision.

The decision must evaluate epistemic rent, not apply an automatic ritual. Candidate.2 is a focused successor of a freshly reviewed predecessor, but it contains material executable/validator repairs plus nearby homologous closure. The project must explicitly decide whether:

1. a fresh blind candidate.2 inspection would still materially expand search-space independence; or
2. the predecessor fresh review + bounded successor repair evidence is sufficient for the release decision, with residual uncertainty explicitly retained.

Until that decision is recorded:

- candidate.2 is `FROZEN / NOT_CURRENT / NOT_RELEASED`;
- Current remains `v0.3.6 / FIELD_VALIDATION`;
- no promotion authority is assigned;
- attack cardinality remains open.
