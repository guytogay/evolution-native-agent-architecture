# Independent Validation of Frozen ENA V2.3 Research Candidate

- Date: 2026-08-21
- Validator: OpenAI GPT-5.6 Sol, independent validation session
- Lineage statement: **independent of the DSH candidate-author lineage**. This validator did not participate in candidate design, implementation, adversarial-fixture construction, V2.3 acceptance-semantics construction, or expected-verdict decisions.
- Repository: `guytogay/evolution-native-agent-architecture`
- Frozen candidate code ref: `8eb5a9afa4c560645b4c50dc24af7874ed54a4f2`
- Freeze record ref: `89d5f97c71a762ec8b06e3a43cb385c96d2ad926`
- Candidate status preserved: `UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED`
- Frozen candidate modified: **No**
- `releases/current/` modified: **No**
- Promotion attempted: **No**

## Final Verdict

**FALSIFIED**

This verdict applies to the frozen V2.3 machine-contract research candidate and its semantic-validation claim, not to ENA as a whole.

The frozen replay is exactly reproducible, but independent inspection found material false-confidence paths where the candidate returns `OK` for claims whose support, provenance, authority, evidence, or closure cannot be established according to the candidate's own stated design contract and the current ENA operational contracts. Independent inspection also found composition paths that incorrectly `BLOCK` legitimate narrower/unrelated claims.

`replay matches author expectations != independent semantic validation`.

## Phase A — Independent Semantic Inspection

### 1. Reference resolution is not end-to-end

`v2.2/cumulative_contract.py` declares that every reference must resolve to the correct artifact type and target. A generic `_typed_lookup()` exists, but `evaluate()` never invokes it. Resolution is instead reimplemented per mechanism and is incomplete.

Independent counterexamples against the exact frozen implementation:

| ID | Independent expectation | Candidate | Finding |
|---|---:|---:|---|
| F1 support target mismatch | BLOCK | OK | `support_id` resolves but `claim_ref` points at another claim; resolved registry support is never target-checked. |
| F2 missing observed scope | BLOCK | OK | Claimed host exists but observed host is absent; candidate only compares when both are truthy. |
| F3 model-binding mismatch | BLOCK | OK | Resolved-support applicability omits `model_binding` even though shipped validator treats it as a scope boundary. |
| F4 untyped/unresolved transfer basis | BLOCK | OK | Transfer is accepted from `required=true` plus a non-empty evidence string; transfer type and referenced evidence are not resolved. |
| F5 duplicate support ID, same status | BLOCK | OK | Duplicate support IDs are rejected only when `support_status` differs; same-status ambiguous records silently select the first entry. |
| F6 invalid resolved support status | BLOCK | OK | Arbitrary status such as `GARBAGE` is not rejected unless exactly `CONTRADICTS`. |
| F12 verified evidence unresolved | BLOCK | OK | Grade `E2` is checked as a label, but its evidence reference need not resolve. |
| F13 closure evidence unresolved | BLOCK | OK | `SATISFIED` obligation closure requires only a non-empty evidence string, not a resolvable closure artifact. |

The candidate therefore does not currently satisfy its stated universal typed-resolution contract.

### 2. Applicability envelope is narrower than the shipped semantic validator

The shipped `validate_contracts.py` checks:

`host, runtime_instance, model_binding, route, configuration, epoch, time_interval, task_scope`.

Resolved registry support in the candidate checks only:

`host, runtime_instance, epoch, configuration, environment`.

This creates an inconsistent composition surface: registry-backed support can bypass applicability checks that would have failed if the same support artifact had been passed through the shipped validator directly.

Subject identity is also not independently checked on resolved support, and missing observed applicability fields are treated as if no mismatch existed.

### 3. Registry presence can create false confidence

Registry absence is often handled explicitly, but **registry presence is over-trusted**.

| ID | Independent expectation | Candidate | Finding |
|---|---:|---:|---|
| F7 present evidence registry, referenced IDs absent | BLOCK | OK | Missing registry entries fall back to the raw evidence-ref string as a synthetic root. |
| F8 resolved evidence objects, root provenance absent | UNKNOWN | OK | Root distinctness is not established, yet raw ref strings again become roots. |
| F9 present root registry, claimed root IDs absent | BLOCK | OK | Missing root records fall back to the claimed root labels themselves. |
| F10 roots unbound to evidence | BLOCK | OK | Two root records can substantiate claimed independence even when only one evidence observation is named; no evidence-to-root binding exists. |

This is a material distinction in `BLOCK / UNKNOWN / OK` semantics:

- absent verification capability for a deeper property can reasonably be `UNKNOWN`;
- a mandatory reference that is broken in a registry that is present is `BLOCK`;
- a resolved artifact whose provenance is genuinely unavailable may be `UNKNOWN`;
- neither case should become `OK` merely because raw identifiers are distinct strings.

### 4. Authority currentness is only partially represented

Explicit evaluation time and expiry parsing work as intended. However, mandate authorization is blacklist-based rather than positively resolved or typed.

F11 uses `mandate.source = "BANANA"` with a future expiry and receives `OK` for a non-empty authority envelope.

No candidate check establishes that the source is a recognized authorizing principal, nor binds the mandate to the asserted subject/effect/task/purpose/action/scope. This is materially weaker than the operational contract statement that authority remains bound to the subject/effect/task/purpose and source of mandate that justify it.

### 5. Provenance and evidence grades remain label-level trust boundaries

The documented trust boundary that evidence grades and registry contents are self-declared is confirmed. An additional implementation-level boundary was found: even within those registries, evidence references are not consistently required to resolve, and provenance roots are not consistently bound to the evidence artifacts they purport to classify.

Thus `E2` is currently an enum-valid label, not end-to-end evidence applicability.

### 6. Obligation composition produces false-positive blocking

The composed evaluator calls the shipped `validate_obligation()` on **every obligation** in the payload before applying claim-linked obligation resolution. The shipped validator blocks every observed material open obligation regardless of whether its `required_before_claim_refs` names the current claim.

Independent legitimate controls:

| ID | Independent expectation | Candidate | Finding |
|---|---:|---:|---|
| L1 unrelated open obligation + unrelated asserted claim | OK | BLOCK | An obligation explicitly required before another claim globally blocks this claim. |
| L2 narrow completion with its own obligation satisfied + another claim's open obligation | OK | BLOCK | Contradicts ENA's allowance for explicitly narrower truthful completion. |

This is a concrete composition failure: individually sensible obligation validation and claim-link validation combine into a broader gate than either semantic contract justifies.

### 7. Parallel support surfaces compose incorrectly

Two additional composition failures were reproduced:

| ID | Independent expectation | Candidate | Finding |
|---|---:|---:|---|
| F14 contradictory top-level `support` plus supportive registry record | BLOCK | OK | Base validator says no positive support is claimed, while registry support independently endorses the claim; contradiction is not reconciled. |
| F15 contradictory `support_relations` plus supportive `support_registry` | BLOCK | OK | `support_registry` silently overwrites the registry assembled from `support_relations`. |

The implementation therefore has an undocumented precedence/trust boundary between `support`, `support_relations`, and `support_registry`.

### 8. Input-shape robustness / portability defects

Two independent controls cause evaluator exceptions rather than `BLOCK`/`UNKNOWN`:

- C1: `root_registry` supplied as a list -> `AttributeError: 'list' object has no attribute 'get'`.
- C2: explicit `support_registry: null` -> `TypeError: 'NoneType' object is not iterable`.

These demonstrate dependence on prior schema/shape enforcement that is not represented by `evaluate()` itself.

`hardened_rules.py` also contains an absolute Windows development path. It did not prevent the isolated Linux replay because the composed import path had already resolved the shipped validator from the reconstructed repository, but it remains a host-specific defect and an unnecessary hidden import-resolution dependency.

## Challenge to V2.3 Expected-Verdict Semantics

**Author's expected-verdict manifest: REJECTED as an independent semantic oracle.**

It remains useful as a reproducible record of the candidate author's expectations.

Reasons:

1. `acceptance_semantics.classify()` assigns every fixture whose `kind` is `ADVERSARIAL`, `ATTACK`, or `SECOND_ORDER` to expected `BLOCK` before inspecting claim semantics. The expected verdict therefore depends partly on author-authored labels.
2. Migrated positives are recognized by a hard-coded fixture-ID set and assigned `OK`.
3. Remaining cases default to `sufficient_positive -> OK`, although the implementation does not prove that every evidence/mandate/closure/provenance reference is actually resolvable or applicable.
4. Existing expected-positive controls such as grade-E2 verification demonstrate label validity, not end-to-end evidence resolution.
5. Therefore `53/53 expected verdicts matched` establishes agreement between one authored classifier and one authored fixture corpus; it is not an independent semantic oracle.

The following distinctions are nevertheless supported:

- mandatory broken support/obligation references: `BLOCK`;
- genuinely legitimate claim where only a deeper verification capability is absent: `UNKNOWN` can be appropriate;
- sufficiently resolved and applicable legitimate claim: `OK`;
- `UNKNOWN` must not be converted into `OK` by raw identifier fallback.

No new case was found where the candidate unnecessarily returns `UNKNOWN`. The more serious observed defect is the opposite: cases that should be `BLOCK` or `UNKNOWN` are promoted to `OK` once an incomplete registry is present.

## Phase B — Frozen Identity and Replay

### Candidate identity

**VERIFIED.**

The candidate/freeze commits were resolved independently. An isolated validator workspace was reconstructed from exact Git blob content. All 11 SHA-256 entries listed in `FREEZE-MANIFEST.md` matched exactly:

- `hardened_rules.py` — `5de4e32a57c52e8c9fc427a03e1bdac23108270f2ff3858983c0de090a518788`
- `fixtures.py` — `b71eb53f139d21e5a35a9b361598409e313d5dadf9cc47e74bff8425c6f5442f`
- `v2.1/fixtures_v21.py` — `0ba4915ba68974efca1d0108dcf99d536665920db508dacababf945bc02707f9`
- `v2.2/cumulative_contract.py` — `f2f1a49f8873967f27a161a5f4646e64b94cc71170daa06b7cea246ceb49bab9`
- `v2.2/fixtures_v22.py` — `fbda0869dfd3dac34b97ecca9f265992896d1f1033f1be1ab0e346fae2d4787b`
- `v2.2/run_v22.py` — `91dbdc5e50cd5148ac560edd52f6a8e6b3d4899fa5ca921427a05867aba303f7`
- `v2.3/acceptance_semantics.py` — `c50c667353027fc4e402d258580e4ac03f1b2d0e4e317e320f5585394c050277`
- `v2.3/fixtures_migrated.py` — `f9e819a405a2837164d1f2f9dce807e8d02a6df63354b2d309067e6dc0753962`
- `v2.3/run_v23.py` — `ecceb3e193a439ac820bca3ce7101435dfeb29ade738a80b1cab19e2c10bed15`
- regenerated `expected-verdict-manifest.json` — `27f37659b18ed41771a71cfe9d5a3e1e41bbda9203f08bc2ecf878497eac901b`
- regenerated `results-v23.json` — `03acbee06c332ad5f8faddde2bf263815eed06c699ee1c020db07367b7710430`

The shipped `releases/current/tools/validate_contracts.py`, although not one of the 11 freeze-listed candidate artifacts, was also reconstructed from its exact Git blob for replay dependency integrity.

### Frozen replay

**REPRODUCED.**

Exact command executed:

```text
python research/prototypes/v2-machine-contract-hardening/v2.3/run_v23.py
```

Observed:

- V2 fixtures: 23
- V2.1 fixtures: 18
- V2.2 fixtures: 7
- migrated fixtures: 5
- total: 53
- adversarial: 29/29 matched expected BLOCK
- mandatory-unresolvable: 3/3 matched expected BLOCK
- uncertainty-positive: 2/2 matched expected UNKNOWN
- sufficient-positive: 14/14 matched expected OK
- migrated-positive: 5/5 matched expected OK
- `UNEXPECTED_VERDICTS: 0`
- exit code: 0
- both regenerated V2.3 JSON outputs match the freeze SHA-256 values byte-for-byte.

Replay host actually exercised: Linux validator environment, Python 3.13.5.

A validation-only GitHub Actions matrix was also prepared for Linux/Windows and Python 3.8/3.12, but repository Actions did not produce a run for the isolated validation branches/PRs during this validation session. No claim is therefore made that those additional host/version combinations were executed.

## Residual Trust Boundaries

### Previously documented and confirmed

- registry truth/authenticity is self-declared;
- evidence-grade truth is self-declared;
- mandate source/expiry truth is self-declared;
- evaluation time is caller-controlled and can be backdated;
- observed scope is self-declared;
- absolute Windows path exists in `hardened_rules.py`;
- research-only / not production hardened;
- historical and migrated corpus is candidate-author authored.

### Previously undocumented or insufficiently explicit

- schema/shape validation is an external prerequisite for evaluator safety;
- registry **completeness** is trusted separately from registry presence;
- present-but-incomplete evidence/root registries can launder raw identifier strings into apparent provenance;
- `_typed_lookup()` is not in the execution path, so universal typed/target resolution is not actually enforced;
- resolved support does not inherit all shipped applicability dimensions;
- evidence grade is not bound to a resolved evidence artifact;
- closure evidence is not bound to a resolved evidence artifact;
- independence roots are not bound one-to-one or otherwise materially to the named evidence set;
- mandate source is blacklist-filtered, not positively authorized/resolved, and mandate scope is not bound to the authority envelope;
- multiple support input surfaces have silent precedence and no contradiction reconciliation.

## Required Reconciliation Before Any Promotion

The Host should not promote this frozen candidate. A successor candidate should, at minimum:

1. Put one typed resolution mechanism on the actual evaluator path for support, evidence, obligations, roots/provenance, transfer evidence, closure evidence, and mandate/authority sources where material.
2. Distinguish registry absence from broken references inside a present registry, and remove raw-ref-as-root fallbacks.
3. Reuse a single applicability envelope (including model/route/time/task scope and subject binding) rather than maintaining divergent scope-key sets.
4. Reject all duplicate IDs irrespective of whether duplicated records happen to share a status label.
5. Scope obligation blocking to the claims/effects for which the obligation is actually required; preserve narrower truthful completion.
6. Reconcile contradictory parallel support surfaces rather than relying on implicit precedence.
7. Positively type/bind mandate sources and authority envelope applicability, not merely blacklist four source labels plus check expiry.
8. Define evaluator input-shape failure semantics so malformed registries return a controlled verdict instead of crashing.
9. Replace fixture-kind/fixture-ID-driven expected verdict derivation with an oracle specified independently from candidate-authored fixture labels.
10. Re-run the original 53 corpus plus the independent cases in this report without modifying the old frozen candidate.

## Requested Status Summary

- candidate identity verified? **YES**
- frozen replay reproduced? **YES — exact 53/53 author-oracle replay, zero unexpected, output hashes matched**
- author's expected-verdict manifest accepted / partially challenged / rejected? **REJECTED as an independent semantic oracle; retained as a reproducible author-expectation baseline**
- new independent adversarial cases found? **YES — 15 false-confidence `OK` cases**
- new legitimate false-positive / unnecessary-UNKNOWN cases found? **YES — 2 legitimate false-positive `BLOCK` cases; no new unnecessary-UNKNOWN established**
- residual trust boundaries confirmed? **YES**
- previously undocumented trust boundary? **YES — multiple, listed above**
- composition failure? **YES — obligation overblocking, contradictory support-surface precedence, and registry/provenance fallback composition**
- portability or host-specific defect? **YES — absolute Windows path remains; malformed-registry crashes are portable shape defects; exact Linux/Python 3.13.5 replay succeeded**

**FINAL: `FALSIFIED`**
