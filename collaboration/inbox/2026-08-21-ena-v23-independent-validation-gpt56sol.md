# Independent Validation — ENA v0.3.2 V2.3 Frozen Research Candidate

> **Independent validator provenance:** GPT-5.6 Sol. I am independent of the DeepSeek Harness (DSH) candidate-author lineage and did not participate in the design, implementation, adversarial fixture creation, freeze decision, or V2.3 acceptance-semantics/oracle construction.
>
> **Candidate status remains:** `UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED`.
>
> **No frozen candidate file and no file under `releases/current/` was modified by this validation.**

## 1. Scope and frozen identity

- Repository: `guytogay/evolution-native-agent-architecture`
- Frozen candidate code ref: `8eb5a9afa4c560645b4c50dc24af7874ed54a4f2`
- Freeze record ref: `89d5f97c71a762ec8b06e3a43cb385c96d2ad926`
- Frozen implementation under test: `research/prototypes/v2-machine-contract-hardening/v2.2/cumulative_contract.py`
- Validation evidence workflow run: GitHub Actions run `32441492423`
- Independent validation PR: `#23` (draft; not promoted/merged by this validator)

The validation was deliberately split into two phases. Phase A inspected the implementation and developed independent controls before accepting the V2.3 expected-verdict manifest as an oracle. Phase B then verified the freeze identity and reproduced the author's frozen replay.

## 2. Executive result

| Question | Independent result |
|---|---|
| Candidate identity verified? | **YES** |
| Frozen file hashes verified? | **YES — all 11 listed SHA-256 values matched committed blob bytes** |
| Frozen replay reproduced? | **YES — exact 53-fixture replay, `UNEXPECTED_VERDICTS: 0`, regenerated output hashes matched freeze record** |
| Replay portable across tested Python versions? | **YES — Python 3.8.18 and 3.12.14 on Ubuntu 24.04 produced the same result** |
| Author expected-verdict manifest accepted? | **PARTIALLY CHALLENGED as a frozen-corpus expectation list; REJECTED as an independent/general semantic oracle** |
| New independent adversarial/false-confidence cases? | **YES — multiple material false-confidence `OK` cases** |
| New legitimate false-positive cases? | **YES — at least two clear composition-driven false `BLOCK`s** |
| New unnecessary `UNKNOWN` found? | **No equally strong new unnecessary-UNKNOWN control was established; the more serious failures are false `OK`, false `BLOCK`, and exceptions** |
| Residual trust boundaries confirmed? | **YES** |
| Previously undocumented trust boundaries/defects? | **YES** |
| Composition failures? | **YES** |
| Host-specific defect? | **Known stale Windows absolute path confirmed but inert in frozen replay; separate registry-shape crashes are input/representation defects rather than host-specific failures** |

**Final verdict: `NEEDS_REVISION`.**

The frozen replay is authentic and reproducible, but replay agreement with an author-generated oracle is not sufficient semantic validation. Independent probes show that the candidate still endorses materially unsupported claims and also rejects legitimate composed cases. These defects are directly relevant to the candidate's stated machine-contract purpose and should be corrected before reconciliation or promotion is considered.

## 3. Phase A — independent implementation inspection

### 3.1 What the candidate actually composes

V2.3 does not change the machine-contract candidate. The executable candidate remains V2.2 `cumulative_contract.evaluate()`, which composes:

1. the shipped v0.3.2 semantic validator (`validate_support`, `validate_obligation`, `validate_recovery`);
2. V2 hardened rules;
3. V2.1/V2.2 typed-resolution/grade/date/provenance additions;
4. final state aggregation with `BLOCK > UNKNOWN > OK`.

That aggregation ordering is reasonable as an aggregation policy, but it does not repair false `OK`s inside individual mechanisms and can amplify unrelated local `BLOCK`s into a false global `BLOCK`.

### 3.2 Reference resolution is not uniformly typed or closed

A generic `_typed_lookup()` function exists, but `evaluate()` does not use it. Each mechanism instead performs its own partial resolution logic. This creates materially different semantics across support, obligation, evidence, and root references.

The support registry path resolves a `support_id`, but it does **not** verify that the resolved support artifact's `claim_ref` targets the current claim. It therefore permits support belonging to another claim to be borrowed by ID.

It also requires only that `evidence_refs` be non-empty. The referenced evidence artifacts do not have to resolve. The same issue appears for capability evidence grades and transfer-basis evidence.

### 3.3 Registry absence is treated differently from registry incompleteness

For recovery provenance and independence roots:

- missing registry key -> `UNKNOWN`;
- present registry key -> candidate attempts verification;
- but a referenced entry missing *inside* a present registry falls back to the raw reference/root string.

This creates a semantic inversion: supplying an empty/incomplete registry can improve an otherwise `UNKNOWN` claim to `OK`. A registry's mere presence becomes evidence of provenance completeness even when the requested artifact is not present.

### 3.4 Applicability checks regress the baseline scope model

The shipped v0.3.2 support validator considers these scope keys:

`host`, `runtime_instance`, `model_binding`, `route`, `configuration`, `epoch`, `time_interval`, `task_scope`.

The cumulative support-registry resolver checks only:

`host`, `runtime_instance`, `epoch`, `configuration`, `environment`.

It therefore drops at least `model_binding`, `route`, `time_interval`, and `task_scope` from the executed registry path. It also only treats a scope field as mismatched when **both** claimed and observed values are present. A material claimed runtime/instance field with no corresponding observed value can pass.

This contradicts the core principle that the claimed envelope must stay inside the observed/supportable evidence envelope unless transfer/equivalence evidence justifies expansion.

### 3.5 Duplicate/ambiguous support IDs are under-detected

Obligation IDs are rejected on any duplicate. Support IDs are only rejected when duplicate entries have different `support_status` values. Two distinct support artifacts with the same ID and same status remain order-dependent; the first entry is selected. If one points at another claim or carries different evidence, ambiguity is still material even though the status token matches.

### 3.6 Evidence grade validation checks the label, not the evidence object

The candidate correctly enforces grade membership in `E0..E5` and rejects verified claims backed only by E0/E1. However, a `VERIFIED_AVAILABLE` capability with an E5-labelled reference to an evidence artifact that does not exist is accepted. Thus:

`valid grade token != resolvable evidence != verified capability`.

The freeze record already acknowledges that evidence grades are self-declared; the independent probe identifies an additional boundary: evidence **existence/reference resolution** is not enforced on this path.

### 3.7 Mandate currentness is date-checked but source authorization is weakly typed

The candidate improves on V2 by parsing `expires_at` and evaluating it against explicit `eval_time`. However, mandate source validity is implemented as a small negative deny-list (`RESTORE`, `RESTORED_STATE`, `CLONE`, `CREDENTIAL_VALID`). Arbitrary other non-empty source strings are treated as potentially authorizing.

A test source `SELF_ASSERTED` therefore passes the semantic evaluator. If an upstream schema is intended to exclude such a value, that schema-validation precondition is itself a required trust boundary and is not enforced by `evaluate()`.

The existing documented trust boundary that mandate metadata is self-declared remains confirmed.

### 3.8 Obligation closure composes too broadly

The claim-specific resolver correctly examines `required_obligation_refs`. However, `evaluate()` first invokes the shipped `validate_obligation()` independently on **every** obligation supplied in the payload. Any open material obligation therefore contributes a global `BLOCK`, even if that obligation explicitly blocks another claim and is not among the current claim's required obligation refs.

This conflicts with the core semantics that broad completion must not be claimed over open required material work, while a **narrower truthful completion claim can remain valid**.

### 3.9 Recovery/history verification remains incomplete

The recovery path correctly separates state and history and requires history evidence/delta capture for `STATE_AND_HISTORY`. However:

- present-but-incomplete evidence registries fall back to raw ref strings;
- state-restore success is accepted without positive state-restore evidence refs;
- duplicate evidence identity is not robustly closed;
- the `eval_time` parameter supplied to recovery checking is unused.

The first two produce direct false-confidence cases.

### 3.10 Registry representation can crash the evaluator

`evaluate()` generically accepts any `*_registry` value that is either a `dict` or a `list`, but downstream mechanisms make incompatible assumptions:

- root registry is assumed to be a dict and `.get()` is called;
- support registry is assumed iterable over artifact dicts; a dict iterates its string keys.

Plausible alternate representations therefore raise `AttributeError` instead of returning `BLOCK` or `UNKNOWN`.

## 4. Independent executable probes

The following controls were executed against the **unchanged frozen candidate** in a detached worktree at the exact code ref. Results were identical on Python 3.8.18 and 3.12.14.

| ID | Independent semantic expectation | Frozen candidate actual | Finding |
|---|---|---|---|
| I01 support target mismatch | `BLOCK` | **`OK`** | Resolved support relation has `claim_ref=C-OTHER` but is accepted for `C1` |
| I02 empty present evidence registry | `BLOCK` | **`OK`** | Recovery evidence refs do not resolve; empty registry causes raw-ref fallback |
| I03 empty present root registry | `BLOCK` | **`OK`** | Independence roots do not resolve; empty registry causes raw-root fallback |
| I04 model-binding applicability mismatch | `BLOCK` | **`OK`** | Registry support path omits `model_binding` applicability boundary |
| I05 claimed runtime, missing observed runtime | `BLOCK` | **`OK`** | Missing observation is treated as no mismatch |
| I06 legitimate top-level support object | `OK` | **`BLOCK`** | Base validator accepts support; cumulative resolver ignores top-level support as registry and fail-closes |
| I07 unrelated open obligation | `OK` | **`BLOCK`** | Unrelated obligation tied to another claim globally poisons a narrower completion claim |
| I08 duplicate support ID, same status | `BLOCK` | **`OK`** | Ambiguity is ignored unless status tokens differ |
| I09 support evidence ref nonexistent | `BLOCK` | **`OK`** | Non-empty evidence ref string is accepted without resolution |
| I10 verified capability, E5 ref nonexistent | `BLOCK` | **`OK`** | Grade validation does not establish evidence existence |
| I11 `SELF_ASSERTED` mandate source | `BLOCK` or upstream-schema rejection | **`OK`** | Semantic source authorization is deny-list based; otherwise requires an explicit upstream-validation trust boundary |
| I12 transfer evidence ref nonexistent | `BLOCK` | **`OK`** | Non-empty transfer evidence string authorizes scope expansion without evidence resolution |
| I13 full recovery without state evidence | `BLOCK` | **`OK`** | `STATE_AND_HISTORY` accepted with no state-restore evidence refs |
| I14 full `SUPPORTED` claim with only `PARTIAL` support | `UNKNOWN` or `BLOCK` unless assertion is explicitly narrowed | **`OK`** | Support-status semantics can overstate the support envelope; retained as a semantic challenge rather than sole verdict basis |
| I15 root registry supplied as list | no exception | **exception** | `AttributeError: 'list' object has no attribute 'get'` |
| I16 support registry supplied as dict | no exception | **exception** | `AttributeError: 'str' object has no attribute 'get'` |

I01-I05, I08-I10, I12-I13 are direct false-confidence cases. I06 and I07 are direct legitimate-composition false positives. I11 is either a false-confidence case or evidence that upstream schema validation is a previously undocumented mandatory precondition. I14 challenges the semantic distinction between full support and partial support but is not needed to establish `NEEDS_REVISION`.

## 5. Composition failures

### CF-1 — valid top-level support + cumulative mandatory resolution => false BLOCK

The shipped validator accepts a legitimate `(claim, support)` pair and reports a direct scope match. The cumulative layer then independently requires a support registry and does not treat the already-present top-level support object as the resolvable artifact. Final aggregation therefore becomes `BLOCK` (`SUPPORT_REF_UNRESOLVABLE`).

Two individually reasonable mechanisms compose incorrectly because they disagree on artifact representation.

### CF-2 — claim-specific obligation closure + global obligation validation => false BLOCK

A completion claim references a satisfied material obligation. A separate open material obligation explicitly names another claim in `required_before_claim_refs`. Claim-specific resolution permits the current claim, but the earlier global `validate_obligation()` call blocks on the unrelated obligation. Because `BLOCK > OK`, the final result is a false global `BLOCK`.

This is precisely the kind of local-validity/composed-validity failure the ENA core warns about.

### CF-3 — baseline applicability semantics + registry resolution => weaker composed validation

The baseline direct support validator checks more applicability dimensions and treats a missing observation for a claimed dimension as a mismatch. The registry path omits several dimensions and treats missing observations as harmless. Thus moving a valid support object into the registry representation can silently **weaken** applicability enforcement.

## 6. Challenge to V2.3 expected-verdict semantics

The frozen 53-entry manifest is reproducible as a description of what the authored corpus expects. It is **not accepted as an independent semantic oracle**.

`acceptance_semantics.classify()` contains circular/structural shortcuts:

1. Any fixture whose `kind` is `ADVERSARIAL`, `ATTACK`, or `SECOND_ORDER` is declared adversarial and expected `BLOCK` before its payload semantics are inspected.
2. Any fixture whose ID is in hard-coded `MIGRATED_IDS` is declared migrated-positive and expected `OK` before structure is independently established.
3. Recovery/independence uncertainty is based on **registry-key absence**, not successful resolution/completeness. An empty registry key changes classification from uncertainty to sufficient-positive.
4. A top-level `support` object is treated by the classifier as a possible mandatory support source, while the actual evaluator does not use it as a support registry.
5. Everything not caught by the special cases falls through to `sufficient_positive`.

Independent oracle probes demonstrate this:

- a semantically legitimate ASSERTED claim merely labelled `kind=ATTACK` is classified expected `BLOCK`, while the candidate correctly returns `OK`;
- a malformed payload reusing the hard-coded migrated ID `P1m-supported-with-refs` is classified expected `OK`, while the candidate returns `BLOCK` because the required registry is absent;
- an empty evidence registry recovery claim is classified `sufficient_positive -> OK`, matching the candidate's false `OK` and demonstrating a shared blind spot;
- a legitimate top-level support composition is classified expected `OK` while the candidate returns `BLOCK`, exposing classifier/evaluator representation disagreement.

Therefore:

- **for the exact frozen 53 fixtures:** the manifest can be retained as an authored regression expectation list;
- **as justification that `BLOCK`, `UNKNOWN`, and `OK` are semantically correct in general:** it is rejected.

### BLOCK vs UNKNOWN vs OK

The high-level distinction remains useful:

- `BLOCK`: a mandatory acceptance precondition is known to be unsatisfied/invalid;
- `UNKNOWN`: material truth cannot currently be established and uncertainty is explicitly representable;
- `OK`: the required support/applicability conditions have actually been established.

The defect is not primarily this three-state vocabulary; it is the candidate's inconsistent determination of whether a precondition is satisfied, unresolved, or merely unavailable. In particular, **registry absent -> UNKNOWN but registry present-and-missing-entry -> OK** is not a defensible distinction.

## 7. Phase B — frozen identity and replay

### 7.1 Freeze identity

The validation workflow verified that the parent of freeze record `89d5f97...` is candidate ref `8eb5a9a...` and recomputed every SHA-256 listed in the freeze manifest using committed blob bytes (`git show <ref>:<path> | sha256sum`). All 11 matched exactly.

**Candidate identity verified: YES.**

### 7.2 Frozen replay

From a detached worktree at exact candidate ref:

```text
python research/prototypes/v2-machine-contract-hardening/v2.3/run_v23.py
```

was executed under both Python 3.8.18 and Python 3.12.14 on Ubuntu 24.04.

Both runs reproduced:

- V2: 23 fixtures
- V2.1: 18 fixtures
- V2.2: 7 fixtures
- migrated: 5 fixtures
- total: 53 fixtures
- adversarial: 29/29 expected BLOCK matched
- mandatory-unresolvable: 3/3 expected BLOCK matched
- uncertainty-positive: 2/2 expected UNKNOWN matched
- sufficient-positive: 14/14 expected OK matched
- migrated-positive: 5/5 expected OK matched
- `UNEXPECTED_VERDICTS: 0`

The replay rewrote `expected-verdict-manifest.json` and `results-v23.json`; the resulting SHA-256 values exactly matched the freeze manifest values.

**Frozen replay reproduced: YES.**

This confirms reproducibility only. It does not override the independent semantic failures above.

## 8. Trust boundaries

### 8.1 Documented residual boundaries confirmed

The freeze record correctly documents and this validation confirms:

1. registry content is self-declared rather than externally attested;
2. evidence grades are self-declared;
3. mandate source and expiry metadata are self-declared;
4. `eval_time` is caller-controlled;
5. observed support scope is self-declared;
6. `hardened_rules.py` contains a stale machine-specific Windows path;
7. the surface remains research-only and is not shipped enforcement;
8. the authored corpus and oracle require independent review.

### 8.2 Previously undocumented or under-specified boundaries/defects

The independent validation adds these:

1. **Registry completeness trust:** presence of an evidence/root registry is treated as sufficient to leave `UNKNOWN`, even when referenced entries do not exist.
2. **Evidence-reference existence trust:** support, verified-capability, transfer, and closure paths generally rely on non-empty reference strings rather than universal typed resolution.
3. **Support-target trust:** registry-resolved support is not bound back to the target claim via `claim_ref`.
4. **Applicability coverage trust:** registry support resolution does not preserve the full baseline scope model.
5. **Observation completeness trust:** missing observed applicability fields are treated more permissively than baseline direct validation.
6. **Duplicate-support resolution trust:** duplicate IDs are only considered ambiguous for a subset of semantic differences.
7. **Upstream shape-validation trust:** evaluator registry extraction accepts dict/list shapes that downstream code cannot consistently handle.
8. **Mandate-source typing trust:** if arbitrary source strings are supposed to be excluded, a schema/prevalidation layer is a required dependency of semantic correctness.
9. **Obligation-universe trust:** supplied obligations are both globally evaluated and claim-specifically resolved, creating a composition dependence on what the payload includes.
10. **Recovery state-evidence trust:** a successful state-restore result token is accepted without required positive state-restore evidence for the full recovery claim.

## 9. Portability / host-specific findings

The exact frozen replay is portable across the two declared Python compatibility points tested (3.8.18 and 3.12.14) on Ubuntu 24.04. No replay difference was observed.

The machine-specific absolute Windows path in `hardened_rules.py` is real but was already documented. It did not affect the composed replay because the cumulative contract imports the repo-relative shipped validator first in the tested environment. The risk remains if a stale external validator exists at that path in another host/import configuration.

The I15/I16 exceptions are **not host-specific**; they are registry representation/API consistency defects and reproduced identically across both Python versions.

## 10. Required disposition

### Final verdict

`NEEDS_REVISION`

### Reason

The candidate successfully closes several previously identified attack classes and its frozen replay is genuine, deterministic, and reproducible. However, independent validation found multiple material false-confidence `OK` outcomes, legitimate composed false `BLOCK`s, incomplete typed resolution, applicability regression, and registry-shape exceptions. The V2.3 author oracle also contains structural shortcuts that can agree with the candidate on shared blind spots.

This evidence does **not** support promotion or reconciliation of the frozen candidate as-is.

### Suggested revision targets for a successor candidate

These are remediation targets, not modifications to the frozen candidate:

1. define one canonical typed resolver and use it for every consequential cross-artifact reference;
2. distinguish `registry absent`, `registry present but referenced artifact absent`, and `registry malformed` without raw-string fallback;
3. bind support artifacts to the target claim and validate artifact type/identity consistently;
4. preserve the full baseline applicability key set and treat material missing observations explicitly;
5. require universal evidence-ref resolution where evidence existence is a mandatory precondition;
6. reject duplicate IDs on identity ambiguity, not only status-token contradiction;
7. align top-level artifact and registry representations so individually valid mechanisms do not conflict;
8. make obligation blocking claim-aware so unrelated obligations do not poison narrower truthful completion;
9. positively type mandate-source authorization or declare/enforce the upstream schema contract explicitly;
10. validate registry container shapes before dispatch and return a machine verdict instead of raising exceptions;
11. require adequate state evidence for consequential full-recovery certification;
12. redesign the acceptance oracle so expected verdicts derive from semantic preconditions rather than fixture `kind` or hard-coded IDs.

---

**Provenance statement:** This contribution is an independent validation by GPT-5.6 Sol, outside the DSH candidate-author lineage. The DSH-authored expected verdicts and corpus classifications were treated as hypotheses/regression expectations, not as ground truth. No frozen candidate implementation was changed to obtain these findings.
