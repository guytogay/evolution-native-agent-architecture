# ENA v0.3.7 candidate.0 — 1080 -> 188 author-harness anti-ablation audit

Status: `PASS_WITH_TREE_EXTERNAL_COVERAGE_REPAIR / CANDIDATE_BYTES_UNCHANGED / NOT_INDEPENDENT_VALIDATION`

Date: 2026-08-27

## Purpose

This record closes the mandatory tree-external anti-ablation audit required before fresh independent falsification of ENA v0.3.7 candidate.0.

The audit asks a narrower question than candidate correctness:

> When the author-side adversarial harness changed from 1080 observed pass conditions to 188, were materially distinct failure shapes preserved, replaced by stronger oracles, retained elsewhere, or explicitly retired with evidence — rather than silently lost?

The numeric counts are **not architectural thresholds** and are **not comparable as a quality score**. Both harnesses explicitly declare open attack cardinality.

This audit is author-side validation-discipline evidence. It is **not** fresh independent semantic falsification and does not establish external truth.

## Frozen target

Candidate identity: `v0.3.7-candidate.0`

Exact frozen source commit:

`d0e793593184740d9732902e948afd48ed96ae2f`

Exact frozen candidate subtree:

`cffbf76fe1448b020b637c78d1f7ae46e4c0115b`

Candidate subtree:

`releases/v0.3.7-candidate/`

Current remains `v0.3.6` under `releases/current/`.

The mutable branch head is not the candidate identity.

## Evidence examined

### Earlier 1080-condition harness

Author harness source state:

`038fbfe62432bd78ccc4ea856ae5020e554114f8`

Workflow run:

`33010925130`

Observed machine result:

```text
AUTHOR_ATTACK_VERDICT=PASS
observed_pass_conditions=1080
attack_cardinality=OPEN
evidence_scope=AUTHOR_SIDE_DETERMINISTIC_AND_REPRESENTED_SEMANTIC_ATTACKS_ONLY
independent_semantic_support=NOT_ESTABLISHED
external_truth=NOT_ESTABLISHED
```

### Later 188-condition harness on exact pre-freeze bytes

Exact candidate pre-freeze source:

`d0e793593184740d9732902e948afd48ed96ae2f`

Exact pre-freeze workflow run:

`33011823923`

Observed machine result:

```text
AUTHOR_ATTACK_VERDICT=PASS
observed_pass_conditions=188
attack_cardinality=OPEN
oracle_style=STRUCTURED_CURRENT_STATE_PLUS_DECISION_BOUNDARIES
evidence_scope=AUTHOR_SIDE_DETERMINISTIC_AND_REPRESENTED_SEMANTIC_ATTACKS_ONLY
independent_semantic_support=NOT_ESTABLISHED
external_truth=NOT_ESTABLISHED
```

### Tree-external anti-ablation repair

Added outside candidate cargo:

- `.github/scripts/v037_candidate_anti_ablation.py`
- `.github/workflows/v037-candidate-anti-ablation.yml`

First successful anti-ablation workflow run:

`33035656311`

Observed machine result:

```text
ANTI_ABLATION_VERDICT=PASS
observed_pass_conditions=106
attack_cardinality=OPEN
coverage_scope=RESTORED_DISTINCT_1080_TO_188_FAILURE_SHAPES
independent_semantic_support=NOT_ESTABLISHED
external_truth=NOT_ESTABLISHED
ANTI_ABLATION_FROZEN_SOURCE=d0e793593184740d9732902e948afd48ed96ae2f
ANTI_ABLATION_FROZEN_TREE=cffbf76fe1448b020b637c78d1f7ae46e4c0115b
candidate_bytes_changed=NO
```

## Audit method

The old and new harnesses were compared by **failure shape**, not by assertion count.

Disposition vocabulary:

- `PRESERVED` — materially the same failure shape remains guarded.
- `MERGED_AS_PROVEN_EQUIVALENT` — multiple old assertions collapse into one oracle without losing the decision distinction.
- `REPLACED_BY_STRONGER_ORACLE` — the old check is superseded by a more direct/structured oracle.
- `RETAINED_OUTSIDE_CURRENT_HARNESS` — removed from the 188 script but still protected by another exact gate.
- `RETIRED_WITH_EVIDENCE` — the old oracle itself was invalid/noisy for the lifecycle semantics and should not be restored.
- `LOST` — a materially distinct failure shape disappeared without an equivalent guard.
- `UNKNOWN` — equivalence could not be established.
- `RESTORED_TREE_EXTERNAL` — a previously lost failure shape was restored outside the frozen candidate subtree.

The governing rule is:

`COMPRESS REPRESENTATION != COMPRESS POSSIBILITY SPACE`

## Disposition map

| Old failure shape | 188 disposition before repair | Audit finding | Final disposition |
| --- | --- | --- | --- |
| Whole-tree absence of lifecycle-sensitive stale markers across every text file | Removed | Historical occurrence of a token is not equivalent to active structured state. The broad scan could false-fail archival/history/provenance text. The convergence-bias incident already identified this class as lifecycle-sensitive. | `RETIRED_WITH_EVIDENCE` |
| Active candidate phase/status identity | Reworked | Structured candidate baseline/status checks directly inspect the live state instead of inferring it from global token absence. | `REPLACED_BY_STRONGER_ORACLE` |
| `OA-EVO-01.tool_state` must reflect assembled machine-checked v2 helper | Present through current-state/pre-freeze checks | Same decision-changing state remains guarded. | `PRESERVED` |
| Absence of stale primary route `` `tools/ena_evolve.py` `` across key adopter-facing surfaces | Removed from 188 | Positive v2-path/legacy relocation checks are useful but do not prove absence of a competing stale default route in every previously protected entry surface. This is a distinct two-default-semantics failure shape. | `LOST -> RESTORED_TREE_EXTERNAL` |
| REFERENCE-INDEX route set equals English HOW-MAP route set | Present | Same route-set consistency distinction remains. | `PRESERVED` |
| zh-CN HOW-MAP carries complete route set | Present | Same language-routing consistency remains. | `PRESERVED` |
| English/zh-CN Cue Index can reach every route | Present | Same reachability distinction remains. | `PRESERVED` |
| Every `primary` entry is a string when interpreted as route metadata | Removed | Malformed route metadata is distinct from route-set equality. | `LOST -> RESTORED_TREE_EXTERNAL` |
| Path-like `primary` target stays inside candidate subtree | Removed | A route can have a valid route id but escape the packaged candidate tree. This is a distinct self-containment failure shape. | `LOST -> RESTORED_TREE_EXTERNAL` |
| Path-like `primary` target actually exists | Removed | Route-set equality does not prove target existence. Broken target reachability is independently decision-changing. | `LOST -> RESTORED_TREE_EXTERNAL` |
| HOW-MAP anchor identifies an OA route and resolves to an existing route | Removed | Weak but distinct anchor-integrity check; retained conservatively rather than assuming equivalence. | `LOST -> RESTORED_TREE_EXTERNAL` |
| Route composition edges refer to existing routes | Present | Same composition-integrity distinction remains. | `PRESERVED` |
| Deliberately broken composition edge is detected | Present | Mutation sensitivity remains. | `PRESERVED` |
| `OA-COM-01.deferred_reference` is not bundled | Removed as route-to-manifest coupling | The later gate verifies the known deferred ID in the manifest, but that does not prove the route field still points to that ID. | `LOST -> RESTORED_TREE_EXTERNAL` |
| `OA-COM-01.deferred_reference` remains represented in durable deferred manifest lineage | Removed as route-to-manifest coupling | Same decoupling risk as above. | `LOST -> RESTORED_TREE_EXTERNAL` |
| Manifest bundled-reference optional/default-off policy | Present | Same false-mandatory-reference boundary remains, with mutation checks. | `PRESERVED` |
| Bundled wrapper declares optional/default-off/not-ontology semantics | Present | Same packaging boundary remains. | `PRESERVED` |
| REFERENCE-INDEX `reference_exists_implies_applicable=false` | Removed from 188 script | Exact pre-freeze workflow still checks it. The new anti-ablation guard also restores it as durable coverage. | `RETAINED_OUTSIDE_CURRENT_HARNESS + RESTORED_TREE_EXTERNAL` |
| REFERENCE-INDEX `reference_exists_implies_required=false` | Removed from 188 script | Exact pre-freeze workflow still checks it. New anti-ablation guard adds a mutation oracle for forced requirement. | `RETAINED_OUTSIDE_CURRENT_HARNESS + RESTORED_TREE_EXTERNAL` |
| REFERENCE-INDEX `host_native_equivalent_allowed=true` | Removed from 188 script | Exact pre-freeze workflow still checks it; anti-ablation guard retains it. | `RETAINED_OUTSIDE_CURRENT_HARNESS + RESTORED_TREE_EXTERNAL` |
| REFERENCE-INDEX `missing_reference_may_route_to_host_pattern_or_honest_residual=true` | Removed from 188 script | Exact pre-freeze workflow still checks it; anti-ablation guard retains it. | `RETAINED_OUTSIDE_CURRENT_HARNESS + RESTORED_TREE_EXTERNAL` |
| Authority `NOT_REQUIRED` false-BLOCK escape | Present | Same decision boundary remains. | `PRESERVED` |
| Contested Authorship out-of-scope escape | Present | Same decision boundary remains. | `PRESERVED` |
| Standing `NO_FORMAL_STANDING` escape | Present | Same decision boundary remains. | `PRESERVED` |
| Purpose-relative continuity / standing / retirement bounded semantics | Present | Decision-relevant false-BLOCK protections remain. | `PRESERVED` |
| zh-CN bundled/default-active distinctions and operational route parity | Present | Structural/language boundary remains guarded; behavioral equivalence remains unproven. | `PRESERVED` |
| v2 latent/import/migration/source-selection boundaries | Present | Core laundering and premature-selection attacks remain. | `PRESERVED` |
| Legacy v1.2 relocation/default-demotion | Not in old shape | Later harness/pre-freeze gate added explicit legacy compartment checks. | `NEW_STRONGER_ORACLE` |
| Candidate post-author-falsification / pre-freeze lifecycle state | Reworked | Later structured status checks are more phase-correct than stale-token inference. | `REPLACED_BY_STRONGER_ORACLE` |

## Why 1080 -> 188 was neither simply good nor simply bad

The reduction mixed two qualitatively different operations:

1. **legitimate oracle repair/compression** — especially removing lifecycle-sensitive global token scans and replacing them with structured current-state checks; and
2. **accidental attack-space ablation** — especially route target integrity, route-to-deferred-manifest coupling, and stale competing primary-tool route detection.

Therefore the statement "188 is better because it is smaller" is unsupported.

The supported statement is:

> The later harness is more phase-aware and less vulnerable to lifecycle false positives, but its simplification accidentally dropped several materially distinct failure shapes. Those shapes have now been restored in a tree-external guard without modifying candidate.0.

## Candidate-byte impact

No candidate-byte defect was found by this audit.

The restored attacks all pass against the exact frozen subtree:

`cffbf76fe1448b020b637c78d1f7ae46e4c0115b`

The anti-ablation workflow explicitly verifies that the current candidate branch still resolves `releases/v0.3.7-candidate/` to that exact subtree and that there is no candidate-subtree diff from frozen source `d0e793593184740d9732902e948afd48ed96ae2f`.

Therefore:

- candidate.0 remains frozen;
- candidate.0 bytes remain unchanged;
- the audit does **not** justify candidate.1;
- the repair belongs to validator/control-plane tooling outside frozen cargo.

## Residual uncertainty

This audit does not claim that every possible historical assertion from the 1080 count has a one-to-one modern counterpart. The count was heavily inflated by repeated file-by-marker assertions and is intentionally not reconstructed mechanically.

The audit instead establishes a disposition for the materially distinct failure families identified through direct old/new harness comparison. For those identified families, no material `LOST` or `UNKNOWN` disposition remains after the tree-external repair.

That is sufficient to close the mandatory anti-ablation gate; it is **not** sufficient to accept candidate.0.

## Independence boundary

Everything in this record is contaminated by author-side artifacts and prior acceptance semantics.

It must not be presented as:

- independent semantic support;
- external truth;
- a release verdict;
- evidence that candidate.0 is Current;
- a substitute for Phase A fresh inspection.

A fresh validator must still inspect the frozen candidate directly before accepting author tests, expected outcomes, or this audit's interpretations as an oracle.

## Audit verdict

`PASS_WITH_TREE_EXTERNAL_COVERAGE_REPAIR`

Reason:

- invalid lifecycle-sensitive broad scans were retired with evidence rather than restored;
- structured replacements were identified where they genuinely preserve the decision distinction;
- distinct lost failure shapes were found rather than hidden by the smaller count;
- those shapes were restored outside the frozen candidate subtree;
- the new machine gate passes against the exact frozen bytes;
- candidate.0 remains byte-identical to the frozen subtree.

## Next governed action

The mandatory 1080 -> 188 anti-ablation audit is complete.

The next action may now advance to the **fresh independent falsification review handoff / DO NOT MERGE review PR**, bound to:

- source `d0e793593184740d9732902e948afd48ed96ae2f`;
- subtree `cffbf76fe1448b020b637c78d1f7ae46e4c0115b`.

The fresh validator must perform Phase A independent inspection before using author-side evidence as a comparison oracle.
