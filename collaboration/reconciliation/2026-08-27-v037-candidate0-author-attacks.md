# ENA v0.3.7 candidate.0 — Author-side adversarial record

Status: `AUTHOR / PREFREEZE_FALSIFICATION / PASS_WITH_REPAIRS / NOT_INDEPENDENT / NOT_FREEZE / NOT_RELEASE_AUTHORITY`

Date: 2026-08-27

## Purpose

Record the candidate author's own adversarial inspection before exact pre-freeze validation.

This record is deliberately outside `releases/v0.3.7-candidate/`. It is validation/reconciliation evidence, not adopter cargo and not part of the future frozen candidate subtree.

```text
AUTHOR_ATTACK_PASS
!= FRESH_INDEPENDENT_FALSIFICATION
!= EXTERNAL_TRUTH
!= FREEZE
!= RELEASE_AUTHORITY
```

The attack space remains open. No count in this record is an architectural or release threshold.

## Candidate context

Candidate branch:

`candidate/v0.3.7-candidate.0`

Correct candidate birth base:

`0ad263178ab8b7c21c150012b3c06a5c41a4f41c`

Current remains:

`v0.3.6 / releases/current/ / CURRENT / FIELD_VALIDATION`

The candidate thesis remains practical Operational Architecture over a preserved v0.3.6 semantic trunk, with no demonstrated need for a new Constitution rule or gratuitous Core semantic rewrite.

## Material author-side defects found before final attack PASS

### A-01 — Top-level README did not expose the direct Cue Index hop

Observed failure:

The candidate README described the Operational Architecture but did not directly point an adopter from the package entry surface to:

`operational/CUE-INDEX.md`

Why material:

v0.3.7's release value depends on a new Agent being able to reach concrete HOWs without repository archaeology. A README that says an operational layer exists but omits the direct cue-router hop weakens the primary adopter traversal.

Repair:

`152d35fe4a7c13706e2f90eac530a7864031719e`

The README now exposes:

```text
00-READ-ME-FIRST.md
-> RUNTIME-ADOPTION-KERNEL.md
-> operational/CUE-INDEX.md
-> operational/HOW-MAP.md
-> operational/REFERENCE-INDEX.yaml
-> concrete HOW / honest residual
```

Assembly Gate run `33010099144`: `SUCCESS`.

Disposition: `CLOSED_BY_CANDIDATE_REPAIR`

### A-02 — Core Operational Contracts retained stale v0.3.6 Current identity

Observed failure:

`05-CORE-OPERATIONAL-CONTRACTS.md` was initially byte-preserved from Current, but that also preserved the false candidate-local statement that it was the single active operational-contract surface for `v0.3.6 Current`.

Why material:

This exposed a real distinction:

```text
SEMANTIC_PRESERVATION
!= IDENTITY_BYTE_PRESERVATION
```

Exact-byte preservation was over-applied. Candidate self-containment requires truthful candidate identity without silently rewriting the contract body.

Repair:

`24c60c161ce787c681b7aafcde56bb2b33ac4fc7`

Only three version/identity statements changed. The Candidate Identity Gate was then strengthened to require:

- 01–04 and the key v2 schemas remain exact-byte identical to v0.3.6 Current;
- 05 equals Current except for the three explicitly allowed identity substitutions.

Identity Gate run `33010461940`: `SUCCESS`.

Disposition: `CLOSED_BY_IDENTITY_ONLY_PROJECTION_WITH_MACHINE_SEMANTIC_BODY_PARITY`

### A-03 — OA-EVO-01 route metadata said the v2 helper was still pending

Observed failure:

`operational/REFERENCE-INDEX.yaml` contained:

`OA-EVO-01.tool_state: ASSEMBLY_PENDING_STAGE_3`

after the candidate-local v2 helper had already been assembled and machine checked.

Why material:

The Reference Index is a decision/router surface. A stale state can make an Agent reason from a world that no longer exists even when the underlying tool is correct.

Repair:

`6548c82275bf66041e141b83b7d0965ec458cd2c`

New state:

`ASSEMBLED_MACHINE_CHECKED_STAGE_3`

The author adversarial script now scans for stale assembly markers so this class is mechanically guarded.

Disposition: `CLOSED_BY_METADATA_RECONCILIATION`

## Oracle defects found and corrected

These were failures of author-side validation logic, not candidate semantic defects. They are preserved as occurrence truth because a broken oracle can be as misleading as broken candidate bytes.

### O-01 — Predecessor Current description misclassified as candidate self-identity

Identity Gate run `33008927401`: `FAIL`.

The oracle rejected the correct statement that the active adopter baseline remained `v0.3.6 / CURRENT / FIELD_VALIDATION` merely because the phrase appeared near the top of a candidate README.

Repair: inspect the file's own title/status identity rather than banning truthful predecessor references from surrounding prose.

### O-02 — Exact freeze slogan required instead of freeze semantics

Identity Gate run `33010099209`: `FAIL`.

`08-RELEASE-DISCIPLINE.md` already represented the external-record freeze property, but the oracle demanded one exact uppercase token.

Repair: validate the actual properties:

- candidate branch is not frozen identity;
- external-record freeze model is stated;
- authoritative freeze property is exact source/tree binding plus governed lineage.

Identity Gate run `33010204370`: `SUCCESS` after oracle correction.

## Final author adversarial suite

Harness:

`.github/scripts/v037_candidate_author_attacks.py`

Workflow:

`.github/workflows/v037-candidate-author-attacks.yml`

Exact tested repository head:

`038fbfe62432bd78ccc4ea856ae5020e554114f8`

Workflow run:

`33010925130`

Conclusion:

`SUCCESS`

Observed script output:

```text
AUTHOR_ATTACK_VERDICT=PASS
observed_pass_conditions=1080
attack_cardinality=OPEN
evidence_scope=AUTHOR_SIDE_DETERMINISTIC_AND_REPRESENTED_SEMANTIC_ATTACKS_ONLY
independent_semantic_support=NOT_ESTABLISHED
external_truth=NOT_ESTABLISHED
```

All workflow steps executed successfully, including Current isolation and confirmation that the author-attack harness remains outside candidate cargo.

`1080` is the number of pass conditions emitted by this exact script/candidate combination. It has no minimum-threshold or completeness authority.

## Attack surfaces exercised

The suite currently attacks, without claiming exhaustiveness:

- stale assembly/status metadata;
- stale default v1.2 evolution-tool references in decision-bearing entry surfaces;
- Reference Index / Cue Index / HOW Map route-set and composition integrity;
- candidate-local route/path existence and containment;
- accidental bundling of deferred Commitment/Settlement;
- optional-reference promotion into required/default-active/universal applicability;
- loss of Host-native equivalents;
- loss of `NOT_REQUIRED`, out-of-scope, no-formal-standing, KEEP/WAIT escape routes;
- EN/zh-CN route identity drift;
- projection self-promotion to Current;
- accidental second translated machine canonical surface;
- v2 source-selection laundering into receiver-local selection;
- v2 import accidentally expressing a source adaptation or forcing early Variation Space;
- packet digest tampering;
- candidate self-promotion into current/frozen/released state;
- mutation sensitivity of selected route-graph and optionality oracles.

## What this PASS does not prove

It does not prove:

- that future sessions will naturally retrieve the correct HOW;
- that a Host-native mapping is operationally fit on every Host;
- that external authority, receipts, provenance, evidence, recovery, or world state are true;
- that EN and zh-CN produce behaviorally equivalent model decisions;
- that the selected optional references are universally appropriate;
- that no adversarial semantic defect remains;
- that candidate.0 should be released.

Those boundaries remain for exact pre-freeze validation, frozen-candidate independent falsification, field evidence, and later reconciliation.

## Author-side stop decision

No additional author-side candidate mutation is justified merely to increase attack count after this exact suite passed.

The next decision-changing step is exact-source **pre-freeze validation** that recomposes all candidate machine/identity/author-attack gates and binds the exact candidate subtree identity.

```text
AUTHOR_ATTACK_PHASE = CLOSED_WITH_REPAIRS
NEXT = EXACT_PREFREEZE_VALIDATION
CURRENT_CHANGE = NO
```
