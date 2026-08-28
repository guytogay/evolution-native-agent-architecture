# ENA v0.3.7-candidate.2 — Independent A-P Report (primary r3)

## 1. Review identity and boundary

- Review mode: independent A-P package/history/oracle/self-description audit.
- Clean-room repository stage commit: `aea2ed25107145a557b3fe46ca0e4b90e2b90fa9`.
- Target identity: `v0.3.7-candidate.2`.
- Frozen source declared by A-P intake/manifest: `bda470e0a6b170cec61225a905957a501454a2fe`.
- Frozen candidate subtree declared by A-P intake/manifest: `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`.
- Package path: `releases/v0.3.7-candidate/`.
- Attack cardinality: `OPEN`.
- Prior A-S seal SHA-256: `0e6bb214cc3398b34c13fc6a3bebd1f548ae00ea067b4c338e8ce88f42ad955f`.
- Phase B: NOT PERFORMED.
- Candidate repair: NOT PERFORMED.

I started from the pinned clean-room root `README.md` and `INTAKE-A-P.md`, then inspected only material exposed by this clean-room repository state plus the already sealed A-S artifact from the immediately preceding review stage. I did not seek the ENA source-project repository, external project history, or project-manager Phase-B context.

The sealed A-S report was treated as read-only occurrence truth. I did not revise, replace, renumber, weaken, or expand its findings. I independently re-hashed the persisted A-S report bytes available in this review session and obtained the same SHA-256 recorded by `MANIFEST-A-P.json`: `0e6bb214cc3398b34c13fc6a3bebd1f548ae00ea067b4c338e8ce88f42ad955f`.

The repository browser exposed the pinned A-P commit and exact raw files. Direct archive/clone transfer into the local execution container was unavailable in this environment, so I do not claim to have rerun the complete bundled test suite from a local checkout. Findings below rely on exact source/fixture/result inspection from the pinned clean-room state, comparison against the sealed A-S artifact where permitted by the intake, and bounded independent consistency checks. No package test is reported as executed unless it actually was.

## 2. Overall A-P verdict

**NOT CLEARED.**

I found four material package/history/oracle/self-description defects:

1. **A-P-01 — HIGH:** A-P metadata attributes the already sealed A-S artifact to a different clean-room wrapper commit than the commit recorded in that sealed A-S report.
2. **A-P-02 — HIGH:** the shipped composed-validator regression harness executes the candidate-local validator but labels its run/result as a `V0.3.5 CURRENT` / `releases/current/` implementation surface.
3. **A-P-03 — HIGH:** candidate.2 lineage/history surfaces are mutually stale or contradictory: the root README mislabels the release-scope checkpoint as the candidate.2 birth base, `LINEAGE.md` stops at candidate.1, `CHANGELOG.md` has no candidate.2 entry, and the candidate.2 release-discipline document still describes candidate.0 as unfrozen mutable workspace.
4. **A-P-04 — MEDIUM/HIGH:** the package simultaneously claims adopter-facing identity/status reconciliation is complete and that inherited top-level zh-CN semantic files still require candidate identity/status reconciliation before freeze.

These findings are additive package-level findings. They do not rewrite the sealed A-S attack tree.

## 3. A-P-01 — Sealed A-S content hash is stable, but its clean-room wrapper-commit attribution conflicts

**Severity:** HIGH

### Evidence

`MANIFEST-A-P.json` records:

- `actual_prior_a_s_cleanroom_commit` = `28dde50c9caaeee3b5c269e28a7be5f07ac29ae5`;
- `a_s_seal_sha256` = `0e6bb214cc3398b34c13fc6a3bebd1f548ae00ea067b4c338e8ce88f42ad955f`;
- `a_s_seal_persisted_before_a_p_exposure` = `true`.

The already sealed A-S report whose exact bytes hash to that same digest records its requested clean-room repository commit as:

`28dde50c9caaeee3b5cfabf51410083dbbb05a93`

Those two 40-hex commit identifiers are different.

The content seal itself is not in dispute: the persisted A-S report re-hashes to exactly the digest recorded in `MANIFEST-A-P.json`. The discrepancy is specifically the provenance claim about which clean-room wrapper commit hosted that sealed A-S review surface.

### Why this matters

A-P is explicitly a package/history/provenance audit. A content hash can prove which report bytes were sealed, but it does not by itself prove which repository-wrapper commit those bytes reviewed. Recording a different prior clean-room commit under the field name `actual_prior_a_s_cleanroom_commit` creates an avoidable ambiguity in the independent-review chain.

This does **not** revise the A-S findings. The sealed report, frozen source identity, frozen candidate subtree identity, and report digest remain fixed occurrence facts. The finding is that the A-P provenance metadata does not agree with the sealed report's own wrapper-commit record.

### Disposition impact

The A-S report remains sealed and unchanged. The package/review provenance chain is not fully self-consistent as presented.

## 4. A-P-02 — Regression PASS is attributed to the wrong implementation surface and Current identity

**Severity:** HIGH

### Evidence

`releases/v0.3.7-candidate/tools/regression_suite.py` resolves its validator by:

- setting `HERE = Path(__file__).resolve().parent`;
- inserting `HERE` at the front of `sys.path`;
- executing `import validate_contracts as vc`;
- calling `vc.run_selftest(...)`.

Therefore the harness executes:

`releases/v0.3.7-candidate/tools/validate_contracts.py`

from the candidate package.

However the same harness:

- prints `V0.3.5 CURRENT INHERITED COMPOSED-VALIDATOR REGRESSION SUITE`;
- emits `"implementation_surface": "releases/current/tools/validate_contracts.py"`;
- emits lineage text tied to the older v0.3.5 candidate.2 lineage.

The checked-in `regression-results-v033.json` repeats the `releases/current/tools/validate_contracts.py` implementation-surface claim and reports all three corpora passing: 10/10, 164/164, and 61/61.

Elsewhere in the same candidate package, the active Current is explicitly identified as **v0.3.6**, while v0.3.7 candidate.2 is explicitly `NOT_CURRENT`.

### Why this matters

The numerical regression result may still describe behavior of the candidate-local inherited composed validator, but its provenance metadata says it describes a different path and an obsolete Current identity.

That makes a PASS easy to overread as evidence about `releases/current/` when the code actually imported and exercised the candidate-local file. A-P is specifically responsible for whether package-local oracles and expected outcomes truthfully describe what they tested.

The harness's own caveat that it covers only inherited composed-validator regression is useful, but it does not cure the false implementation-surface attribution.

### Relation to sealed A-S

This materially contextualizes sealed A-S-01 without changing it. A-S-01 concerns the candidate-local composed validator. The package regression PASS cannot rebut that finding merely by presenting itself as a Current regression result, because the harness actually executes the candidate-local validator and its fixture coverage does not establish the missing composed Authority Lease semantics.

## 5. A-P-03 — Candidate.2 lineage/history surfaces are stale and internally contradictory

**Severity:** HIGH

### Evidence A — root README mislabels the candidate.2 birth base

The candidate root `README.md` states:

- candidate branch: `candidate/v0.3.7-candidate.2`;
- `Correct candidate birth base:` `0ad263178ab8b7c21c150012b3c06a5c41a4f41c`;
- candidate.2 was created from the exact frozen candidate.1 source.

`CANDIDATE-BASELINE.yaml` distinguishes those identities:

- `release_scope_checkpoint_merge` = `0ad263178ab8b7c21c150012b3c06a5c41a4f41c`;
- `candidate_birth_base_commit` = `ae6903464133cb5bcf3cd8909ecae1215fe0b9ba`;
- `predecessor_frozen_source` = `ae6903464133cb5bcf3cd8909ecae1215fe0b9ba`.

The baseline is internally coherent with “candidate.2 was created from the exact frozen candidate.1 source.” The README's label `Correct candidate birth base` points instead to the older release-scope checkpoint.

### Evidence B — `LINEAGE.md` stops at candidate.1

The frozen candidate.2 package contains a `LINEAGE.md` whose title is:

`# ENA v0.3.7 candidate.1 Lineage`

It records candidate.1 succession from candidate.0 and preserved candidate.0 history, but contains no candidate.2 succession section.

This is not merely old history retained below a current section: the file's top-level active identity is candidate.1.

### Evidence C — `CHANGELOG.md` has no candidate.2 entry

The top entry in `CHANGELOG.md` is:

`v0.3.7 candidate.1 — WORKING_CANDIDATE / NOT_CURRENT / NOT_FROZEN`

followed by candidate.0 and v0.3.6 material. There is no candidate.2 entry.

Candidate.2 repair/succession history exists in `CANDIDATE-BASELINE.yaml`, so the package contains the information, but its designated human-readable changelog does not carry it.

### Evidence D — candidate.2 release discipline preserves a false present-tense candidate.0 state

`08-RELEASE-DISCIPLINE.md` correctly states that candidate.2 succeeds frozen candidate.1 and that candidate.1 preserves candidate.0 occurrence truth. But under `Predecessor v0.3.7 candidate.0 preserved state`, it also states in present tense that candidate.0 “is still mutable workspace” and remains `NOT_FROZEN`.

That conflicts with the package's own lineage narrative that candidate.1 was a successor to a **frozen candidate.0**.

### Why this matters

The package's machine baseline contains a relatively complete candidate.2 succession record, but the reader-facing lineage/changelog/release surfaces do not present one coherent history.

This is exactly the class of A-P defect where historical occurrence truth becomes misleading through stale active narration. A reviewer or adopter should not have to infer which of several package-local “birth base,” frozen-state, or successor narratives is authoritative.

This finding does not challenge the frozen source/subtree identifiers supplied by the A-P clean-room manifest. It concerns the candidate package's own self-description/history consistency.

## 6. A-P-04 — zh-CN identity/status reconciliation is simultaneously complete and still required

**Severity:** MEDIUM/HIGH

### Evidence

`CANDIDATE-BASELINE.yaml` says:

- `semantic_trunk.identity_reconciliation_complete: true`;
- `semantic_trunk.freeze_requires_candidate_identity_reconciliation: false`;
- assembly completed: `adopter-facing identity/status projections reconciled`;
- prior identity-gate evidence includes `candidate identity-bearing projection surfaces PASS`.

But `language-projections/zh-CN/projection-manifest.yaml` still lists this as a `known_gaps` item:

`Inherited top-level zh-CN semantic files still require candidate identity/status reconciliation before freeze.`

The actual top-level zh-CN files show a mixed state:

- `zh-CN/00-READ-ME-FIRST.md` and `zh-CN/RUNTIME-ADOPTION-KERNEL.md` identify themselves as v0.3.7 candidate.2 and correctly state that Current remains v0.3.6.
- `zh-CN/01-CONSTITUTION.md` states that “this file is the Simplified Chinese semantic projection of v0.3.6 Current's existing 38 constitutional rules.”

The unchanged Constitution semantics may legitimately be inherited from v0.3.6, but the projection manifest does not describe this as a completed intentional inheritance boundary. It explicitly says candidate identity/status reconciliation is still required before freeze.

### Why this matters

The A-P wrapper exposes the package as the exact frozen candidate package. Inside that package, the machine baseline says the relevant reconciliation is complete, while the projection manifest says a pre-freeze reconciliation obligation remains open.

At least one of those package-local status claims is stale or overbroad. The package does not provide a single self-consistent answer about whether the zh-CN top-level identity/status surface was finished before the frozen identity was bound.

### Scope

This is not a claim that the entire zh-CN projection is semantically wrong. The operational zh-CN entry and Runtime Kernel are candidate.2-scoped. The defect is the contradictory package status/reconciliation narration.

## 7. Package-local context for the fixed A-S findings

This section does not modify the sealed A-S report. It records only what the newly exposed A-P material says about those already-fixed findings.

### A-S-01 — composed authority semantics

**Package-local evidence confirms the interpretation.**

The standalone Authority Lease fixture corpus explicitly expects `NOT_AUTHORIZED` for, among other cases:

- a represented `REVOKED` grant;
- an action outside `allowed_actions`;
- a protected subject outside the grant scope;
- a task outside the grant scope;
- epoch and host mismatches.

The inherited composed-validator regression corpus does not provide equivalent cross-validator parity coverage for those richer grant semantics. Thus the package contains a stronger standalone authority oracle while still allowing the composed regression suite to PASS without proving that the composed path honors it.

This strengthens the interpretation that sealed A-S-01 is a cross-surface semantic parity defect, not merely an undocumented external-authenticity limitation.

### A-S-02 — terminal effect receipt regression

**Package-local evidence confirms the exact blind direction.**

The Effect Lifecycle fixture corpus includes:

- same-sequence `COMMITTED` + `NOT_COMMITTED` as invalid;
- earlier `NOT_COMMITTED`, strictly later `COMMITTED` as valid and settled;
- new `REALIZE` after a known `COMMITTED` receipt as invalid.

But the exposed corpus does not include the sealed A-S counter-direction:

`earlier COMMITTED -> strictly later NOT_COMMITTED`.

The package therefore contains explicit settlement-order tests adjacent to the A-S defect while leaving that terminal-to-nonterminal downgrade branch uncovered.

### A-S-03 — transferred source-history chronology

**Package-local evidence contextualizes the missing chronology parity.**

`tools/selftest_ena_evolve_v2.py` exercises source-history retention and rejects, among other cases:

- shallow represented source experiment/evaluation objects;
- source selection/evaluation contradiction;
- tied latest expression history;
- expression-state/history mismatch.

It does not exercise the sealed A-S chronology case in which a transferred source history claims `INTEGRATED`/`COMMITTED` before its represented experiment/evaluation history.

Therefore the package's helper selftest PASS does not contradict A-S-03; it shows that migration history received targeted consistency tests without local-equivalent commit chronology coverage.

### A-S-04 — self-hash sealing procedure

**A-P uses a corrected sealing shape without revising A-S.**

`INTAKE-A-P.md` explicitly requires the report digest to be returned externally or in a sibling sidecar and says not to embed the digest in the bytes being hashed. This avoids the self-referential exact-file-hash construction identified in sealed A-S-04.

That is A-P process context only. The A-S finding remains sealed occurrence truth.

## 8. Additional observations that did not become findings

- The A-P clean-room manifest and intake agree on target identity, frozen source, and frozen candidate subtree.
- The A-P manifest's recorded A-S content digest matches the persisted sealed A-S report bytes exactly.
- Candidate-local `NOT_FROZEN` / `frozen: false` text is **not by itself** treated as a defect in this A-P review. `CANDIDATE-BASELINE.yaml` explicitly defines an external-record freeze model in which the tested candidate tree is not rewritten to insert a post-hoc frozen flag; the internal flag remains pre-freeze occurrence state.
- The package repeatedly states that machine PASS counts are corpus facts, not completeness thresholds, and that attack cardinality remains open. I did not treat an untested branch as disproven merely because an author selftest passed.
- The package explicitly limits reference applicability, external-truth claims, natural bilingual behavioral equivalence, and helper-tool scope. Those caveats are materially useful.
- I did not infer that every stale inherited version label is automatically a defect. The findings above are limited to cases where package-local status/history claims conflict with other active package claims or falsely describe what a shipped oracle executes.

## 9. Inspection summary

A-P inspection covered the pinned clean-room entry material and the package surfaces most relevant to the intake's withheld classes, including:

- root `README.md`, `INTAKE-A-P.md`, and `MANIFEST-A-P.json`;
- candidate `README.md`, `00-READ-ME-FIRST.md`, `CANDIDATE-BASELINE.yaml`, `LINEAGE.md`, `CHANGELOG.md`, `08-RELEASE-DISCIPLINE.md`, adoption instructions, Runtime Kernel, and contribution/status surfaces;
- zh-CN projection manifest and top-level decision/status-bearing documents;
- `tools/regression_suite.py`, `regression-results-v033.json`, inherited composed-validator fixtures, candidate v2 helper selftest;
- Authority Lease fixtures/selftest surface;
- Effect Lifecycle fixtures/selftest surface;
- the already sealed A-S report only as read-only occurrence/provenance context.

No source-project repository, external project history, or Phase-B material was used.

## 10. Final A-P disposition

A-P review is complete for the pinned clean-room surface.

**Disposition: NOT CLEARED.**

The sealed A-S report remains unchanged and already records substantive candidate-semantic blockers. A-P independently adds package-level reasons not to clear the frozen candidate as presented:

1. inconsistent prior-review wrapper provenance;
2. false regression implementation-surface / Current attribution;
3. stale and contradictory candidate.2 lineage/history surfaces;
4. contradictory zh-CN identity-reconciliation status.

No candidate repair was performed.

No Phase B was performed.

The SHA-256 of the exact bytes of this report is intentionally returned **outside** this file, as required by `INTAKE-A-P.md`.

STOP.
