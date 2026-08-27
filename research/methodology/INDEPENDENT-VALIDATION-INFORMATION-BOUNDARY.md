# Independent Validation Information Boundary

Status: `CANONICAL_FOCUSED_METHOD_CANDIDATE / VALIDATION_INDEPENDENCE / OPEN_CARDINALITY / NON_NORMATIVE_TO_CURRENT`

Purpose: preserve the epistemic value of a **fresh independent Phase A** by controlling what author-shaped information reaches the validator before independent findings are persisted.

This method does not reduce the amount of project context available to project managers. It separates roles that need different information postures.

```text
PROJECT_MANAGER_TAKEOVER
-> maximize relevant continuity

FRESH_VALIDATOR_BLIND_SEMANTIC_PHASE
-> minimize author-shaped priming
```

## 1. Project-manager succession is not validator briefing

A project-manager successor needs:

```text
STATE + METHOD + GOVERNANCE + DECISION_LINEAGE + NEXT_ACTION
```

A fresh validator does not need that full package before its blind semantic findings are sealed. Giving it author attack taxonomies, expected verdicts, acceptance narratives, reconciliation summaries, or detailed predecessor repair history can align its search space with the author's blind spots.

```text
FULL_CONTEXT_FOR_CONTINUITY
!=
MINIMAL_CONTEXT_FOR_INDEPENDENT_DISCOVERY
```

## 2. Independence has an information-exposure dimension

Independence is not only organizational identity.

A validator may be a different Agent/model/person and still inherit the author's search priors if it reads the author's attack list first.

Keep distinct:

```text
ROLE_INDEPENDENCE
ORACLE_INDEPENDENCE
SEARCH_SPACE_INDEPENDENCE
EVIDENCE_SOURCE_INDEPENDENCE
```

These dimensions are not a fixed ontology; they are useful distinctions when they change confidence in the review.

## 3. Blind semantic work uses a minimal-prime entrypoint

Before blind semantic findings are persisted, expose only what is necessary to identify and inspect the target safely:

- exact immutable target identity;
- scope/path of the bytes under review;
- validator freshness requirement;
- release/authority boundary;
- explicit blind-view inclusion/exclusion boundary when the package is self-priming;
- prohibition on author/oracle surfaces;
- open-ended falsification task;
- minimal evidence hygiene.

Do not preload:

- author attack categories;
- expected outcomes or verdict manifests;
- known repair findings;
- green-run interpretations as confidence signals;
- known residual lists framed as the attack agenda;
- author reconciliation conclusions;
- detailed suggested failure examples;
- a mandatory finding taxonomy that can become the search ontology.

```text
MINIMAL_PRIMING != MINIMAL_RIGOR
```

## 4. Derive the attack space from behavior-bearing target bytes

The blind semantic validator should infer material claims and failure possibilities from the contract, implementation, schemas, operational surfaces, and other behavior-bearing candidate bytes exposed in the blind view.

```text
BEHAVIOR_BEARING_TARGET_BYTES
-> INDEPENDENT_CLAIM_MODEL
-> INDEPENDENT_ATTACK_BRANCHES
-> FINDINGS / CONTROLS / UNKNOWNS
```

The attack space is open-cardinality.

```text
AUTHOR_KNOWN_FAILURES != POSSIBLE_FAILURE_SPACE
CURRENTLY_DERIVED_ATTACKS != COMPLETE_ATTACK_SPACE
```

Do not optimize for finding count or symmetry across categories.

## 5. Preserve legitimate behavior as well as attacks

A fresh validator should independently identify false-BLOCK controls and valid lightweight behavior, not only failure cases.

Otherwise independence can become adversarial over-restriction rather than falsification.

## 6. Seal independent semantic discovery before author history opens

Blind semantic findings must be durably persisted before history-bearing or author-side context opens.

```text
BLIND_SEMANTIC_INSPECTION
-> PERSIST_IMMUTABLE_A-S_ARTIFACT
-> A-S_SEALED
-> PACKAGE_HISTORY_AUDIT
-> PERSIST_INDEPENDENT_PACKAGE_AUDIT
-> OPEN_AUTHOR_CONTEXT
-> PHASE_B_COMPARISON
```

The first seal prevents later repair history or author evidence from silently rewriting what the validator originally found, missed, or considered uncertain.

## 7. Phase B is where rich author context belongs

After the independent semantic seal and any independent package audit are persisted, the validator/project manager may inspect:

- author adversarial harnesses;
- expected verdicts/fixtures;
- pre-freeze workflows and green-run evidence;
- author reconciliation records;
- known residuals;
- anti-ablation lineage;
- candidate design rationale and repair history.

Then ask:

- Did author tests catch the independent finding?
- Did they use the wrong oracle?
- Did both sides share a blind spot?
- Did the independent validator false-BLOCK something legitimate?
- Did author evidence reveal a valid constraint the blind semantic phase missed?
- Does new evidence require another attack branch rather than immediate closure?

## 8. Prior exposure cannot be erased by instruction

A reviewer that already read author oracles, predecessor findings, repair narratives, or materially participated in their construction cannot become a fresh blind semantic validator by promising to ignore that information.

```text
PRIOR_MATERIAL_EXPOSURE
-> FRESHNESS_NOT_RECOVERABLE_WITHIN_SAME_REVIEWER_STATE
```

Such a reviewer can still contribute valuable package audit, Phase-B analysis, project management, oracle auditing, or reconciliation; it must label the evidence honestly.

## 9. Candidate-local bytes can themselves be a priming channel

The earlier method assumed candidate-local bytes were always safe Phase-A input. That is false for a self-describing candidate.

A candidate package may contain both:

```text
BEHAVIOR / CONTRACT / IMPLEMENTATION
```

and

```text
LINEAGE / REPAIR HISTORY / AUTHOR EVIDENCE
```

A history-bearing file can tell the validator exactly which defects were previously found and fixed, even when no external author handoff is read.

Therefore:

```text
CANDIDATE_LOCAL
!=
AUTOMATICALLY_BLIND_SAFE
```

Trigger incident:

`research/methodology/incidents/2026-08-27-CANDIDATE-SELF-PRIMING-INCIDENT.md`

## 10. Use a blind semantic view when the full package is self-priming

When candidate-local history/evidence surfaces materially disclose the author's prior search tree, create a mechanically auditable **blind semantic view**.

The view is not a successor candidate and must not be described as one.

```text
FROZEN_CANDIDATE
-> EXACT_BYTE_PRESERVING_PROJECTION
-> BLIND_SEMANTIC_VIEW
```

Requirements:

1. bind the view to the exact frozen source commit and candidate subtree;
2. retain behavior-bearing candidate files byte-for-byte;
3. explicitly list excluded history/evidence-bearing or mixed-role files;
4. do not rewrite retained files to hide clues;
5. verify the view differs from the frozen candidate only by declared exclusions plus validation-entry metadata outside candidate cargo;
6. state that full-package review is deferred, not waived;
7. keep Current and frozen candidate bytes untouched.

A blind view may be implemented as a validation branch where declared history-bearing candidate files are absent while every retained candidate blob is identical to the frozen source.

```text
PROJECTION != NEW_CANDIDATE
EXCLUSION_FOR_BLINDNESS != ABLATION_FROM_RELEASE
```

## 11. Separate A-S from A-P

For a self-describing package, use two independent-validation subphases when useful.

### A-S — blind semantic falsification

Search-space-independent to the degree practicable.

Inspect the priming-reduced exact-byte projection and independently grow the semantic/behavioral attack tree.

Persist and seal before opening withheld candidate history.

### A-P — independent package/self-description audit

After A-S is sealed, the reviewer may inspect the excluded candidate-local history/status/evidence surfaces.

Audit for:

- stale or contradictory status claims;
- misleading lineage;
- package/self-description inconsistency;
- evidence overclaim;
- mismatch between historical narrative and actual bytes.

A-P remains role/oracle independent, but it is **not** claimed to be search-space blind with respect to history disclosed by the target itself.

```text
FULL_PACKAGE_INDEPENDENCE
!=
FULL_PACKAGE_SEARCH_SPACE_BLINDNESS
```

## 12. Fixtures and implementation artifacts

Candidate-local schemas, implementation code, examples, and ordinary conformance fixtures may be inspected when they are part of the behavior-bearing object under review. Their expected result must not automatically become the validator's oracle.

Author adversarial harnesses, predecessor-specific regression corpora, and explicit repair-history tests should not be preloaded merely because they are repository-local.

When a shipped test artifact is itself materially history-bearing, classify it like any other mixed-role file and defer it until after A-S seal.

The boundary is based on **information role**, not directory name.

## 13. Independent output should not be forced into the author's categories

Before Phase B, require evidence and reproduction, not a final release verdict or author-shaped classification system.

A useful A-S artifact contains:

- exact frozen target identity;
- exact blind-view identity/binding;
- freshness declaration;
- independently inferred material claims/expectations;
- findings and reproductions;
- legitimate-behavior controls;
- unresolved questions;
- new branches worth following;
- explicit acknowledgement of excluded package surfaces.

A useful A-P artifact records independent package/self-description findings separately.

Only after Phase B should the project force release-oriented reconciliation such as `PASS_WITH_RESIDUALS`, `NEEDS_REVISION`, or successor-candidate decisions.

## 14. Relationship to convergence/divergence discipline

Author priming can be a subtle convergence operator:

```text
AUTHOR_ATTACK_MAP
-> VALIDATOR_SEARCH_MAP
-> SHARED_SEARCH_BOUNDARY
-> UNKNOWN_OUTSIDE_SPACE_DISAPPEARS
```

Self-priming candidate history can create the same effect:

```text
CANDIDATE_REPAIR_HISTORY
-> VALIDATOR_SEARCH_MAP
-> SHARED_SEARCH_BOUNDARY
```

Therefore minimal-prime blind semantic review is another application of:

```text
COMPRESS_REPRESENTATION != COMPRESS_POSSIBILITY_SPACE
UNKNOWN_SPACE -> ALLOW_EXPANSION
```

The goal is not ignorance for its own sake. It is to preserve the possibility that an independent observer grows a different tree before the trees are compared.

## Packaging guidance for future candidates

When practical, separate candidate files whose primary job is current contract/state from files whose primary job is historical repair/evidence traceability.

This can make both adopter traversal and independent validation cleaner without deleting history.

Do not mutate an already frozen candidate solely to retrofit this separation unless the package itself is materially defective.

## Trigger evidence

External-briefing priming incident:

`research/methodology/incidents/2026-08-27-INDEPENDENT-VALIDATOR-PRIMING-INCIDENT.md`

Candidate self-priming incident:

`research/methodology/incidents/2026-08-27-CANDIDATE-SELF-PRIMING-INCIDENT.md`
