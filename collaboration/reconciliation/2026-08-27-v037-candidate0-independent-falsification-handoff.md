# ENA v0.3.7 candidate.0 — Fresh independent falsification handoff

Status: `VALIDATOR_HANDOFF / FRESH_INDEPENDENT_REQUIRED / DO_NOT_MERGE / NOT_AUTHOR_ORACLE / NOT_RELEASE_AUTHORITY`

Date: 2026-08-27

## Role requirement

The next validator must be **fresh and independent** of candidate.0 design, authoring, reference selection, author adversarial fixture creation, acceptance-semantics decisions, and pre-freeze reconciliation.

The candidate author's summaries, expected interpretations, green workflows, and author attack results are evidence inputs only. They are **not** the validator's oracle.

The validator should independently inspect the exact frozen bytes and reason about failure shapes **before** relying on author-side expected behavior.

## Frozen target — do not substitute branch head

Candidate identity:

`v0.3.7-candidate.0`

Exact frozen source commit:

`d0e793593184740d9732902e948afd48ed96ae2f`

Exact frozen candidate subtree:

`cffbf76fe1448b020b637c78d1f7ae46e4c0115b`

Candidate subtree:

`releases/v0.3.7-candidate/`

Freeze record:

`collaboration/reconciliation/2026-08-27-v037-candidate0-freeze.md`

Current remains v0.3.6 under `releases/current/`.

Do not treat the mutable branch ref as the candidate identity. The review target is the exact source/subtree above.

## Validation ordering

### Phase A — independent inspection before accepting author-side test oracles

Inspect the frozen implementation and package directly.

Before relying on:

- the author attack harness;
- Assembly / Identity / Pre-Freeze workflow assertions;
- reference selftest expected verdicts;
- bilingual fixture expected routes;
- candidate README/CHANGELOG narrative;

independently ask what false claims, false confidence, false BLOCKs, wrong routing, broken compositions, or unusable HOWs the package may still permit.

The purpose is to prevent author and validator from sharing the same blind spot merely because the same oracle was reused.

### Phase B — compare independent findings with author-side evidence

Only after Phase A, inspect author-side machine evidence and adversarial tests.

For each material independent finding, decide whether existing tests:

- actually catch it;
- appear to catch it but use the wrong oracle;
- miss it;
- false-BLOCK a legitimate behavior;
- validate representation only while candidate prose overclaims more;
- depend on a Host/environment condition not represented by the package.

## Candidate thesis to falsify, not assume

The candidate claims it can preserve the v0.3.6 semantic trunk while adding a practical Operational Architecture:

```text
ordinary cue / failure / decision
-> CUE-INDEX
-> HOW-MAP
-> REFERENCE-INDEX
-> bounded procedure / optional reference / Host-native HOW
-> ACT / WAIT / UNKNOWN / REFUSE / NOT_APPLICABLE
```

The validator should try to falsify whether this is actually an **inhabitable** architecture rather than a well-organized document set.

## High-value independent attack surfaces

The list below is a starting surface, not a completeness claim. The validator should add new attacks when the implementation suggests them.

### 1. Navigation / operational reachability

Ask whether a fresh adopter can move from ordinary problem language to the right concrete mechanism without hidden research-session knowledge.

Look for:

- missing or ambiguous routes;
- cycles or dead ends;
- one cue mapping to a mechanism that cannot actually resolve the decision;
- HOWs that remain abstract advice rather than executable procedures/mechanisms;
- practical mechanisms present in the package but unreachable from the hot/cold routing surface;
- route metadata that can become stale independently of the underlying mechanism.

### 2. False-BLOCK pressure from bundled references

The package says bundled references are optional/default-off and Host-native equivalents are valid.

Try to find places where prose, routing, examples, validators, or adoption instructions nevertheless make a bundled reference effectively mandatory.

Attack especially:

- Authority machinery on harmless local work;
- Contested Authorship on ordinary task/cache state;
- formal Standing on normal feedback;
- evidence envelopes/dependency graphs on trivial claims;
- recovery ceremony on cheap/disposable state;
- identity/continuity machinery when continuity cannot change the decision.

### 3. False confidence from representation

Try to make a schema/validator PASS coexist with an unjustified external claim.

Examples to probe independently:

- represented authority vs actual mandate;
- represented receipt/settlement vs external effect truth;
- evidence metadata vs evidence truth;
- checkpoint/restore vs world rollback;
- source digest vs source authentication;
- `EXPRESSED` record vs actual runtime salience/application;
- translated fixture parity vs behavioral language equivalence.

A valid representation boundary is acceptable if candidate prose remains equally narrow. A packaging overclaim is still a candidate defect even when the validator itself is honest.

### 4. Cross-organ composition seams

Attack compositions rather than only organs in isolation:

```text
Authority -> Effect Lifecycle
Effect Lifecycle -> Recovery
Authority + Effect + settlement guidance -> commitment handoff/closure
Evidence Envelope -> Dependency Map
Evolution record -> packet v2 -> receiver import
Runtime cue -> HOW -> Host adapter
```

Look for one organ silently inheriting another organ's evidence strength, scope, authority, completion, or applicability.

### 5. WAIT / UNKNOWN / REFUSE / NOT_APPLICABLE survival

The package explicitly preserves non-action and non-applicability states.

Try to find compositions where they disappear and the system is pushed toward:

- blind retry;
- fabricated completion;
- unnecessary governance;
- false authority requirement;
- premature selection;
- forced identity resolution;
- automatic activation merely because a reference is bundled.

### 6. v2 evolution helper and migration

Independently inspect `tools/ena_evolve_v2.py` and its schemas.

Attack whether:

- latent-now / experiment-later is actually possible;
- source `SUPPORTED` can be laundered into receiver-local selection;
- negative lineage is lost;
- import silently expresses an adaptation;
- packet digest is described or treated as authentication;
- schema-valid migration can create a false local-proof narrative;
- legacy v1.2 compatibility surfaces can leak back into the primary v2 semantics.

### 7. Legacy compatibility compartment

Inspect `tools/legacy/` and all references to it.

Ask whether legacy preservation:

- creates two competing default semantics;
- breaks executable history;
- accidentally routes ordinary adopters toward v1.2 limitations;
- silently influences v2 conclusions;
- contains stale tooling that cannot run from its packaged location.

### 8. zh-CN semantic projection

Do not treat paired fixtures as proof of behavioral equivalence.

Independently inspect whether Chinese operational wording preserves high-risk distinctions such as:

- capability != authority;
- source evidence != receiver-local proof;
- bundled != required/default-active;
- WAIT/wake != authorized resume;
- restore != world rollback;
- being heard != sovereignty;
- continuity-for-purpose != universal sameness;
- local success != universal fitness.

A translation can be structurally aligned and still create a different model decision.

### 9. Hot/cold architecture

Try to falsify the practical claim:

`HOT_KERNEL -> KNOW_WHEN_TO_RETRIEVE_HOW`

Ask whether the Runtime Kernel has enough cues to find needed cold capability without either:

- requiring the whole HOW library to stay hot; or
- relying on unstated session/research memory.

Fresh-session natural salience remains unproven field evidence; do not mark it proven merely because paths exist.

### 10. Semantic-trunk preservation versus candidate identity

Verify independently that candidate.0 did not smuggle a Core semantic change into what is described as Operational Architecture packaging.

Also verify the opposite failure: preserving old bytes must not leave candidate-local files making false v0.3.6 Current claims.

### 11. Deferred / omitted organs

Candidate.0 deliberately does not bundle the recovered Commitment/Settlement machine prototype.

Independently ask whether the remaining Authority + Effect + explicit settlement guidance is sufficient for candidate.0's claimed operational surface, or whether omission creates a concrete release blocker.

Do **not** infer either conclusion from the fact that the prototype was deferred.

### 12. Candidate-scope economics

Ask whether the new operational surface earns its complexity:

- does it materially reduce research archaeology for adopters?;
- does it create duplicated or conflicting navigation?;
- can a Host ignore irrelevant references cheaply?;
- does the package become more inhabitable rather than merely larger?;
- are any files/axes/mechanisms present only because the author wanted the candidate to look complete?

Deletion/simplification is a valid finding.

## Evidence and methodology requirements for the validator

Keep separate:

```text
PROSE_PRESENT
STRUCTURALLY_REPRESENTED
MACHINE_GUARDED
EXECUTED
EXTERNALLY_OBSERVED
INDEPENDENTLY_SUPPORTED
```

Also preserve:

```text
DEFINED
APPLICABLE
IMPLEMENTED
ACTIVE
EVIDENCED
```

Do not upgrade one level into another.

Avoid arbitrary numeric thresholds. Test counts are corpus facts, not proof of completeness.

Do not use stochastic/model-diversity experiments to prove a bug that can already be derived statically.

If an experiment is proposed, state what decision it can change and what non-derivable structure reality may reveal.

## Required independent output

Return a durable report with:

1. role declaration: `FRESH_INDEPENDENT / NOT_AUTHOR`;
2. exact frozen source/tree inspected;
3. Phase-A findings produced before accepting author oracles;
4. each material finding classified as candidate defect, false positive, residual, field-only uncertainty, or research opportunity;
5. concrete reproduction/evidence for every release-blocking claim;
6. explicit false-BLOCK controls / legitimate behaviors that must remain allowed;
7. comparison against author-side tests only after independent inspection;
8. whether any finding requires candidate-byte modification;
9. final candidate verdict, using one of:
   - `PASS_WITH_RESIDUALS`
   - `NEEDS_REVISION`
   - `UNRESOLVED_EVIDENCE_REQUIRED`
10. recommendation:
   - `CANDIDATE_SUCCESSION_STOP_SUPPORTED`
   - `CANDIDATE_1_REQUIRED`
   - `DECISION_DEFERRED`

The validator may use different internal categories if they are more precise, but must not collapse uncertainty into PASS or every residual into a blocker.

## Release boundary

This review PR/handoff is **not** a release PR and must not be merged as a route to Current.

If independent validation finds a material candidate defect:

`frozen candidate.0 -> preserve occurrence truth -> create candidate.1`

If no candidate-byte repair is required:

`independent report -> host reconciliation -> release preparation -> explicit promotion decision`

Until that decision:

```text
FROZEN_CANDIDATE = v0.3.7-candidate.0
CURRENT = v0.3.6
CURRENT_CHANGE = NO
```
