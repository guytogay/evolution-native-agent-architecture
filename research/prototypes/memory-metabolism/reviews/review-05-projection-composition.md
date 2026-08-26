# Cross-prototype composition review

## 1. EXACT REVIEW TARGET

Reviewed repository: `guytogay/evolution-native-agent-architecture`

Frozen target:

`28e25cd0406ac3719ff353a028dd2e742078e686`

The commit is `research: reconcile issue 85 projection composition seam`, timestamped 2026-08-25 16:48:31 UTC. All repository artifacts used for the review were fetched explicitly at that SHA; I did not follow the current branch head and made no repository modifications, consistent with the review constraints.

Phase A was performed from the frozen schemas, validators, fixtures, and selftests before reading the reconciliation/Current material. I also independently recomputed Retrieval 0.5's reference subject fingerprint and replayed the composition evaluator logic against adversarial materiality/fidelity cases. I did not claim a local checkout execution: outbound DNS from the execution sandbox prevented cloning, so machine-behavior conclusions are grounded in the frozen source itself.

For non-versioned Issue/PR discussion, I treated the frozen commit timestamp as the substantive cutoff; later comments or live PR-body edits were not used to determine the verdict.

---

# PHASE A — BLIND MACHINE / INTERFACE REVIEW

## 2. INFERRED RETRIEVAL CONTRACT

Retrieval Obligation 0.5's actual machine contract is narrower than the name `decision.disposition = READY` suggests.

For `RETRIEVAL_SUFFICIENCY_RESOLVED`, its subject fingerprint binds the decision/consequence, retrieval intent, decision-context snapshot, obligation/resolver, current decision-material discovery, and the decision-material attempts—including immutable/versioned identities of returned content. Set-like scope/result order is normalized, so mere reordering does not invalidate sufficiency. Material changes to returned content, context snapshot, decision-material attempts, or the current material discovery do invalidate the old resolution.

`READY`, however, means essentially:

> all **represented retrieval obligations** for that decision are closed by a satisfying retrieval disposition.

It does not mean that every possible retrieval trigger existed, that recall was complete, that projection retained the retrieved evidence, or that the consequential action is globally ready. The selftest makes this particularly clear: a material decision with `READY` and **zero triggers, intents, or obligations** is deliberately valid under the case `runtime_cannot_detect_missing_trigger`.

The frozen reference runtime is correspondingly valid with one HIT returning both `M1` and `M2`, a sufficiency packet bound to that retrieval subject, and `D1.disposition = READY`.

**Inference:** Retrieval 0.5 closes the represented retrieval lifecycle. Its machine cannot establish universal consequential readiness.

---

## 3. INFERRED PROJECTION CONTRACT

Memory Metabolism 0.6's Decision Projection is independently a bounded-use contract.

It enforces, among other things:

- current/historical use disjointness;
- every used record must be actor-visible;
- material-current records requiring revalidation must be revalidated;
- superseded records cannot be current;
- optional Host-resolved modes bind disclosure/boundary/provenance resolutions to the record/provenance subject;
- memory cannot manufacture executable authority.

It does **not** require all records in storage—or all records returned by some independent retrieval system—to be projected. The reference projection itself contains a selected visible/used set, and nothing in the projection validator links that set to Retrieval 0.5's returned-result subject.

Therefore, neither local validator is wrong if:

`Retrieval subject = {M1,M2}`

but:

`effective Memory projection = {M1}`.

The missing property lives at their composition boundary.

---

## 4. CROSS-PROTOTYPE FALSE-OK FINDINGS

- **F1 — Local-valid readiness laundering** (`CROSS_PROTOTYPE_INTERFACE_GAP`): Retrieval returns `{M1,M2}` → subject-bound sufficiency → Retrieval `READY`; later projection uses only `{M1}` while M2 is a material limitation. Both local contracts remain valid. Smallest reconciliation: final consequential closure reasons from the effective projected subject, or an explicit transfer check establishes preservation before reuse.
- **F2 — `READY` naming/level hazard** (`REFERENCE_MODEL_OVERREACH`): a material decision can be `READY` with no represented retrieval trigger/obligation. Treat/namespace it as retrieval-stage closure, not action readiness; frozen 0.5 need not be rewritten solely for naming.
- **F3 — Self-declared non-materiality** (`HOST_SEMANTIC_TRUST_BOUNDARY`): a Host can mark a genuinely material M2 non-material and obtain `TRANSFER_OK`; structural validation cannot infer natural-language materiality.
- **F4 — Self-declared preservation/coverage** (`HOST_SEMANTIC_TRUST_BOUNDARY`): a Host can claim C1 covers `{M1,M2}` and `PRESERVES_DECISION_EFFECT`; coverage/fidelity are semantic assertions, not independently proven facts.
- **F5 — Stale projection assessment** (`FALSE_ALARM`): P1 assessed → effective projection P2; differing subject refs force `REASSESS_REQUIRED`.
- **F6 — Identity-preserving projection supposedly required** (`FALSE_ALARM`): `{M1,M2}` → compact C1 covering both with preserved decision effect returns `TRANSFER_OK`.
- **F7 — Certificate ladder supposedly required** (`FALSE_ALARM`): the evaluator is only a transfer test and does not create universal downstream certificates.

The strongest structural result is F1. The frozen composition evaluator exists precisely because neither local validator detects it. When M2 is truthfully represented as material and omitted, the evaluator returns `REASSESS_REQUIRED`.

---

## 5. FALSE-BLOCK FINDINGS

I found **no intrinsic structural false-BLOCK** in the reconciliation property.

The frozen controls correctly permit:

- omission of genuinely non-material/redundant evidence;
- deletion of exploratory hits;
- preserving only the decision-material subset;
- many-to-one compaction;
- full exact projection.

A duplicate-equivalent M2 does not have to remain separately hot: a projected item can represent coverage of both M1 and M2. Likewise, compact C1 can cover multiple material inputs under `PRESERVES_DECISION_EFFECT`.

The requirement that `assessed_projection_subject_ref` equal the effective subject ref is not accidental record-identity preservation. It is resolution-subject binding. A Host is free to implement the reference as a content identity, immutable snapshot ID, semantic-equivalence identity, or another suitable mechanism. The fixture explicitly avoids prescribing hashing or storage identity.

If a Host gratuitously generates a fresh subject identity for an unchanged subject and thereby forces needless reassessment, that is a Host identity-design problem rather than a shared-contract false-BLOCK.

---

## 6. SUBJECT-BINDING FINDINGS

**Subject binding is necessary.**

Retrieval 0.5 already demonstrates why: changing content identity or the decision-context snapshot invalidates an existing sufficiency packet. Conversely, set reordering does not, because it is normalized before fingerprinting.

The composition layer applies the same principle at the next boundary:

`assessment(P1)` cannot silently become `assessment(P2)`.

This does **not** imply:

`representation(P1) == representation(P2)`.

It means only that reuse of the old assessment requires a truthful basis that the effective subject is still the one assessed. Therefore the opaque projection-subject references are not inherently over-specified.

**Finding:** necessary binding; no normative identity protocol warranted.

---

## 7. HOST-TRUST / VACUITY FINDINGS

The fixture has a real semantic trust boundary, but it is **not vacuous**.

A dishonest or mistaken Host can obtain `TRANSFER_OK` by asserting:

- that an actually material M2 is non-material;
- that C1 covers M2 when it does not;
- that C1 preserves M2's decision effect when it actually destroys a limitation or contradiction.

The evaluator cannot falsify those claims from arbitrary natural language.

What the architecture still contributes is substantial:

1. it makes the materiality/preservation claims explicit rather than implicit;
2. it forces all *represented* material inputs to be accounted for;
3. it distinguishes preserving from `UNKNOWN/LOSSY`;
4. it detects subject staleness;
5. it prevents accidental transfer after an honestly represented material omission;
6. it locates exactly which semantic claims remain externally trusted.

That is the same general trust shape already visible in Retrieval 0.5: the validator explicitly cannot prove Host materiality classification, discovery completeness, or evaluator legitimacy.

**Classification:** `HOST_SEMANTIC_TRUST_BOUNDARY`, with actual natural-language truth remaining `EXTERNAL_EVALUATION_ONLY`.

---

## 8. CERTIFICATE-LADDER / OVER-GOVERNANCE FINDINGS

The proposed stage-local approach avoids the certificate ladder.

`retrieval sufficient → projection sufficient → interpretation sufficient → salience sufficient → application sufficient → ...`

would not converge. The fixture explicitly rejects that interpretation and treats stage-local states as diagnostic evidence rather than universal readiness certificates.

Projection-correct/model-misinterprets, projection-correct/not-salient, and projection-correct/Agent-ignores are **different behavioral failure stages**. They are not evidence that the same structural projection-transfer certificate should recursively reproduce itself.

One final consequential closure against the **effective subject actually used**, with open material gaps honestly represented, is sufficient architecturally.

---

## 9. THINGS SUSPECTED BUT FALSIFIED

The machine review falsified the following stronger suspicions:

- `retrieved records == projected records` is required — **false**.
- Every raw material record must remain hot — **false**.
- Exact record identity must survive compression — **false**.
- Decision-effect-preserving many-to-one compaction is impossible — **false**.
- Non-material/exploratory retrieval automatically forces reassessment when trimmed — **false**.
- Opaque subject binding necessarily specifies a particular hash/storage scheme — **false**.
- The machine should infer natural-language materiality itself — **false requirement**.
- `PRESERVES_DECISION_EFFECT` being externally asserted makes the entire fixture vacuous — **false**.
- A universal sufficiency certificate is needed for every downstream behavioral stage — **false**.

---

## 10. WHAT CANNOT BE PROVEN STRUCTURALLY

Neither the individual prototypes nor the composition evaluator can prove:

- actual decision materiality;
- semantic equivalence of two differently represented memories;
- that a compressed summary really preserves a contradiction, prerequisite, or limitation;
- truth of a `covers_result_refs` mapping;
- Host evaluator legitimacy;
- actual retrieval/discovery completeness;
- real-world source truth/authenticity;
- current-world freshness beyond represented evidence;
- whether the model correctly interprets loaded information;
- whether loaded material becomes salient;
- whether the Agent actually applies it;
- final external-world decision correctness.

Those are genuine evaluation/Host/behavior boundaries, not missing JSON-schema tricks.

**PHASE A COMPLETE**

---

# PHASE B — ENA RECONCILIATION

## A. Is `retrieval lifecycle closed != final consequential decision ready` already implied by Current?

**YES. Strongly.**

Current's Local Projection explicitly includes the Host's **effective loaded surface**, including capacity, precedence, truncation, selective loading/routing, known gaps, and—where material—the distinction between `WRITTEN`, `LOADED`, `INTERPRETED`, `SALIENT`, and `APPLIED`.

Core also says:

- `claim != evidence != support relation`;
- transfer across subject/Host/configuration/etc. boundaries may require an equivalence/invariance basis;
- a materially changed composition is a new selection/verification subject;
- `local validity != composed validity`;
- final `READY` is always bounded by completeness of represented material inputs.

So Retrieval 0.5's stage-local `READY` cannot legitimately bypass those downstream semantics.

---

## B. Is “Sufficiency does not automatically survive a material lossy subject transformation” a genuinely new ENA property?

**NO.**

It is an excellent **cross-prototype specialization** of existing Current semantics, particularly:

`materially changed composition = new selection/verification subject`

and:

`local validity != composed validity`.

Therefore there is no distinct Core-level bad decision that Current permits only because this new sentence was absent. The bad decision arises when a reference-level retrieval status is incorrectly laundered past Current's existing composition/effective-subject rules.

The fixture adds epistemic value by making that particular handoff mechanically falsifiable. It does not earn a new ENA law.

---

## C. Is `PRESERVES_DECISION_EFFECT` an honest Host boundary, or does it make the abstraction vacuous?

**It is an honest Host boundary.**

It would become vacuous only if the architecture treated the claim as self-proving. It does not.

The useful shared property is:

> if the Host claims preservation, bind that claim to the relevant inputs/effective subject and make the semantic trust explicit.

This matches Current's broader position that represented contract validation does not establish every external-world support, causal, evidence, or applicability assertion.

I would include `covers_result_refs` in the same trust boundary; fidelity is not the only semantic assertion.

---

## D. Can bounded active memory remain viable without keeping every retrieved record hot?

**YES.**

The fixture already demonstrates the required cases:

`{M1,M2} → C1`

is allowed when C1 truthfully preserves both material effects, and genuinely non-material/exploratory retrieval can be discarded from the active surface.

Current itself expects bounded projection, truncation, selective routing, and known gaps.

The architecture therefore does not regress to flat/unbounded hot memory.

---

## E. Is Retrieval 0.6 justified?

**NO.**

The one concrete Retrieval 0.5 issue exposed here is a naming/abstraction hazard around `decision.disposition = READY`. The actual retrieval contract is coherent once read as stage-local closure, and the composition failure occurs after its evaluated subject has been transformed.

A new Retrieval version would add machinery at the wrong layer unless naturalistic evidence shows that the reference naming itself repeatedly causes implementation failure.

The frozen reconciliation reaches the same narrow direction without mutating 0.5.

---

## F. Does Current need any change?

**NO.**

Current already contains all parent semantics needed:

effective loaded surface; known gaps; claim/evidence/support separation; applicability across changed subjects; composition as a new verification subject; whole effect surface; consequential closure bounded by represented material inputs.

No new Constitution/Core property pays additional rent here.

---

## G. Would another reviewer of this mechanism still pay epistemic rent?

**NO.**

This review was the differentiated cross-prototype review requested by the frozen reconciliation. It found:

- the structural seam is real;
- the proposed reconciliation prevents the intended readiness laundering when used;
- bounded projection remains possible;
- Host semantic trust is real but non-vacuous;
- no new Core mechanism emerged;
- no new Retrieval mechanism emerged;
- no certificate ladder is needed.

Under the stated stopping rule, another architecture reviewer would now mostly repeat known information. The next epistemically different step is naturalistic/Host observation of whether material information is actually lost, misclassified, or falsely summarized at the projection boundary.

---

# FINAL VERDICT

**COMPOSITION_RECONCILIATION_SURVIVES**

Strongest structural false-OK:
Retrieval 0.5 can validly close `D1` as `READY` on the subject `{M1,M2}` while a separately valid Memory 0.6 projection subsequently uses only `{M1}`; if M2 carries a decision-material limitation, the composed effective decision subject is no longer the subject whose retrieval sufficiency was assessed.

Strongest false-BLOCK:
NONE

Strongest Host-trust residual:
A Host can falsely classify M2 as non-material, falsely claim that C1 covers M2, or falsely claim `PRESERVES_DECISION_EFFECT`, and thereby obtain `TRANSFER_OK`; structural machinery cannot prove those semantic assertions.

Minimal property that pays rent:
**Stage-local sufficiency does not automatically transfer across a decision-material lossy change of the effective subject; consequential closure must bind the effective subject actually used.**

Does Retrieval 0.6 need to exist?
**NO**

Does ENA Current need a change?
**NO**

Should another cross-prototype reviewer be used?
**NO**

Is #85 ready to move to naturalistic observation after reconciliation?
**YES**

This review does not authorize repository modification, merge, release, Current mutation, or promotion.
