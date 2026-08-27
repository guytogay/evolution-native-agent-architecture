# ENA Handoff — Project State

Status: `HANDOFF_PROJECT_STATE_PROJECTION / VERIFY_AGAINST_LIVE_REFS`

Handoff ID: `2026-08-27-v037-candidate0-frozen`

Observed date: 2026-08-27

## 1. Canonical Current

Authoritative source:

`releases/current/CURRENT-BASELINE.yaml`

Observed state:

```text
version = v0.3.6
adoption_status = CURRENT
maturity = FIELD_VALIDATION
```

No work in the v0.3.7 research/candidate line has promoted or replaced Current.

`CURRENT_CHANGE = NO`

## 2. Project-control / research refs at handoff preparation

Observed `main` head after canonicalizing the convergence/divergence method:

`e42f9838294716b2ad34e6a2a0150e5d1cb89027`

Observed active research integration branch:

`research/ena-reconstruction`

Observed active research head at handoff preparation:

`e42f9838294716b2ad34e6a2a0150e5d1cb89027`

At preparation time:

```text
main == research/ena-reconstruction
```

The active research branch remains general continuation authority. Candidate branches are release-lifecycle surfaces, not replacements for the research pointer.

Reverify these refs live before writing; the handoff intentionally does not treat cached head SHAs as permanent branch identity.

## 3. v0.3.7 release line

Next assigned version:

`v0.3.7`

Release thesis:

> Make ENA operationally inhabitable while keeping the semantic trunk stable: expose concrete plural HOWs, bundle optional references without making them mandatory, provide a practical v2 evolution path, and improve zh-CN operational usability.

Demonstrated new Constitution IDs required:

`0`

Demonstrated mandatory Core semantic delta required merely to create candidate.0:

`0`

This does not imply release value is zero.

## 4. Candidate.0 state

Candidate branch:

`candidate/v0.3.7-candidate.0`

Observed branch head at handoff preparation:

`9f4ceb0e6c3b03cb6f30c3628bed800ebbf9493d`

Important: the branch head is **not** the frozen identity.

Frozen candidate identity:

```text
candidate = v0.3.7-candidate.0
frozen source commit = d0e793593184740d9732902e948afd48ed96ae2f
frozen candidate subtree = cffbf76fe1448b020b637c78d1f7ae46e4c0115b
candidate subtree path = releases/v0.3.7-candidate/
```

External freeze record:

`collaboration/reconciliation/2026-08-27-v037-candidate0-freeze.md`

Freeze-record commit:

`a3b5c16fa7af1559c84be5f9ee47351db5d0387e`

Fresh independent falsification handoff:

`collaboration/reconciliation/2026-08-27-v037-candidate0-independent-falsification-handoff.md`

Candidate branch head containing tree-external review/handoff records:

`9f4ceb0e6c3b03cb6f30c3628bed800ebbf9493d`

Tree-external records after the frozen source do not change the frozen candidate subtree identity.

## 5. Candidate contents / selected release cargo

Candidate.0 contains a release-local Operational Architecture with:

```text
HOT CUE
-> CUE-INDEX
-> HOW-MAP
-> REFERENCE-INDEX
-> bounded procedure / optional reference / Host-native HOW
-> ACT / WAIT / UNKNOWN / REFUSE / NOT_APPLICABLE
```

Selected bounded procedures/patterns include:

- Purpose-Relative Continuity;
- Standing Input;
- Control Retirement;
- Evolution Commons pattern;
- Host mapping guidance.

Bundled general optional references:

- Retrieval Obligation 0.5;
- WAIT;
- Authority Lease;
- Effect Lifecycle;
- Recovery Adapter.

Bundled advanced/specialized optional references:

- Evidence Envelope;
- Evidence Dependency Map;
- Contested Authorship.

Important packaging invariants:

```text
BUNDLED_REFERENCE != REQUIRED_FOR_COMPLETE_ADOPTION
BUNDLED_REFERENCE != DEFAULT_ACTIVE
REFERENCE_SCHEMA != NORMATIVE_ONTOLOGY
HOST_NATIVE_IMPLEMENTATION != NONCOMPLIANT
HOT_KERNEL != HOW_LIBRARY
```

Deferred but preserved:

- recovered Commitment/Settlement machine reconstruction;
- progressive occurrence/enrichment runtime branches;
- mesocosm/ecology/reputation/verification-market research;
- a universal Tiny Hot Kernel phenotype.

`NOT_BUNDLED != RETIRED`.

## 6. Candidate tooling

Candidate default practical evolution tool:

`releases/v0.3.7-candidate/tools/ena_evolve_v2.py`

The legacy v1.2 tool and its historical regression probes were moved together under:

`releases/v0.3.7-candidate/tools/legacy/`

The candidate-local v2 helper is intentionally narrow. It orchestrates v2 record/packet paths rather than becoming a second independent semantic engine.

## 7. Validation state

Author-side candidate assembly, identity, zh-CN, reference/tool and exact pre-freeze validation passed after repairing real defects and several validation-oracle false positives.

Exact successful pre-freeze workflow:

`ENA v0.3.7 Candidate Exact Pre-Freeze Gate`

Run:

`33011823923`

Result:

`SUCCESS`

Exact binding emitted by that run:

```text
PREFREEZE_SOURCE_COMMIT=d0e793593184740d9732902e948afd48ed96ae2f
PREFREEZE_CANDIDATE_TREE=cffbf76fe1448b020b637c78d1f7ae46e4c0115b
```

Author attack record:

`collaboration/reconciliation/2026-08-27-v037-candidate0-author-attacks.md`

## 8. Important validation-method correction after freeze

The frozen record reports a final author harness with an observed `188` pass conditions and states that reducing noisy assertions was an oracle-quality improvement.

The user challenged this as an unproven convergence claim because the earlier harness had produced an observed `1080` pass conditions.

Canonical method was subsequently updated on `main` at:

`e42f9838294716b2ad34e6a2a0150e5d1cb89027`

New focused method:

`research/methodology/CONVERGENCE-DIVERGENCE-DISCIPLINE.md`

Therefore the correct current interpretation is:

```text
188 may be a cleaner representation
BUT
188 has not yet been shown to preserve all materially distinct attack/failure shapes from the predecessor harness
```

The older freeze-record wording is historical author interpretation, not an independently established fact.

This does not by itself invalidate the frozen candidate bytes.

## 9. Immediate next action

Before independent semantic falsification, perform a **1080 -> 188 anti-ablation audit** outside the frozen candidate subtree.

Required output:

- recover materially distinct attack/failure shapes from the earlier author harness;
- map them to the newer harness;
- classify each shape as preserved/replaced/proven-equivalent/retained/retired/lost/unknown;
- reintroduce materially distinct lost attacks into the validation surface;
- determine whether any recovered attack reveals an actual frozen-candidate defect.

Do not optimize for recovering the numeric count `1080`. Recover behaviorally distinct variation.

## 10. After the anti-ablation audit

If the frozen candidate survives the restored/verified attack space:

1. create a clearly labeled `DO NOT MERGE / INDEPENDENT FALSIFICATION` review PR;
2. bind the review to the exact frozen source/tree;
3. use a fresh independent validator;
4. require Phase A independent inspection before the validator accepts author fixtures/oracles;
5. then compare Phase A findings with author evidence in Phase B;
6. reconcile the verdict.

Possible high-level outcomes:

```text
PASS_WITH_RESIDUALS
NEEDS_REVISION
UNRESOLVED_EVIDENCE_REQUIRED
```

Only material candidate-byte defects require candidate.1.

## 11. Promotion state

```text
candidate.0 frozen = YES
independent falsification = PENDING
candidate succession stop = NOT_DECIDED
release preparation = NOT_STARTED
v0.3.7 released = NO
v0.3.7 Current = NO
```

## 12. Explicit prohibitions for the incoming session

Until evidence changes the state:

- do not edit frozen candidate.0 bytes;
- do not promote v0.3.7;
- do not modify `releases/current/`;
- do not call author PASS independent validation;
- do not create candidate.1 without a material candidate-byte correction;
- do not skip the new anti-convergence discipline;
- do not treat file/assertion counts as completeness proof;
- do not collapse Host/HOW/failure branches because a summary looks cleaner.
