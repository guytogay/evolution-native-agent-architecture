# FIELD_VALIDATION process decision

Status: `RECONCILED_PROCESS_DECISION / NEXT_RELEASE_INPUT / CURRENT_UNCHANGED / NO_MATURITY_LADDER`

Related: #83, #8, #61, #70, #72 S2/S14/S15/S16, #89, #94.

## Decision

For ENA release/process semantics:

> **`FIELD_VALIDATION` is an evidence-seeking posture associated with an admitted immutable release, not a prestige rung that must graduate to `MATURE`, `STABLE`, `PROVEN`, or a revived `MAINLINE`.**

The following subjects remain separate:

```text
canonical release admission
!= post-release evidence campaign/posture
!= project lifecycle
!= Host-local adoption/conformance evidence
```

`CURRENT` answers canonical adopter-facing admission.

`FIELD_VALIDATION` says that real-world applicability/failure/economics evidence remains actively relevant and that universal proof is not claimed. It does not imply an eventual same-version maturity promotion.

## No mandatory same-version maturity carrier

The earlier representation concern was real:

```text
maturity field inside immutable release bytes
+
version identity separate from maturity
-> apparent need for mutable same-version status carrier
```

The reconciliation result is to remove the unsupported assumption that every Current release must undergo a same-version maturity transition.

Until a real project decision requires such a transition:

```text
DO_NOT_BUILD_MATURITY_LADDER
DO_NOT_BUILD_EXTERNAL_MATURITY_CARRIER
DO_NOT_MUTATE_IMMUTABLE_RELEASE_BYTES_FOR_STATUS
```

This is not a deferred design choice. It is the selected minimal architecture boundary.

A future materially new case may create new release pressure, but it does not make the present architecture incomplete.

## Field tracker lifecycle

A field tracker may:

- remain active while another bounded observation can plausibly change a material claim/adoption/applicability decision enough to pay its cost;
- close with evidence/residuals preserved when its intended evidence campaign is complete;
- be superseded by a newer release's tracker before active validation closure;
- narrow or reopen a specific claim if new evidence changes the represented failure/applicability envelope.

None of these administrative/process events silently upgrades the immutable release.

```text
ISSUE_CLOSED != VALIDATION_PROVEN
NEW_CURRENT != PREDECESSOR_MATURE
MORE_RUNS != MORE_INDEPENDENT_EVIDENCE
LOW_INCIDENT_COUNT != MATURITY
KNOWN_BOUNDED_FAILURES != IMMATURE
```

## Closure without perfection

A field campaign may stop without universal proof when:

- the release claim is explicitly scoped;
- known material counterexamples have a disposition;
- residuals and UNKNOWNs are visible and bounded for the claim being made;
- no currently identified bounded evidence step can plausibly change the material adoption/applicability/claim-strength decision enough to pay its cost.

If an unbounded material counterexample remains necessary to the claim, either continue work or narrow/withdraw the claim. Do not manufacture maturity by closing the tracker.

This is a project/process application of existing Governance Closure rather than a new Constitution invariant.

## Uneven evidence

Evidence strength can differ by property and environment. A single scalar release grade must not hide this.

Use scoped evidence/residuals where a decision requires them. Do not create a mandatory giant maturity vector merely to represent uneven evidence.

## Host-local evidence

Host success or failure remains scoped to the Host/model/runtime/language/consequence dimensions that matter.

```text
LOCAL_FITNESS != RELEASE-WIDE MATURITY
HOST_COUNT != INDEPENDENT FAILURE-DOMAIN COUNT
```

## Late evidence

A later counterexample does not rewrite an earlier truthful assessment. It creates a new evidence occurrence and may narrow/revise the current claim.

```text
past assessment occurrence truth
!= permanent infallibility
```

## Next-release packaging implication

The next release should avoid wording that makes `FIELD_VALIDATION` sound like a quality badge or unfinished ladder stage. Adopter-facing release material should make the separation between release admission and evidence posture explicit.

No separate mutable maturity attestation subsystem is required by this decision.

## Closed question boundary

The project is **not** leaving open:

> What maturity tier comes after FIELD_VALIDATION?

Selected answer:

> **No tier is required.**

The project is also **not** leaving open:

> Where is the same-version mutable maturity carrier?

Selected answer:

> **There is no justified requirement for one under the current process model.**

A future real decision that cannot be expressed using immutable release identity + scoped evidence/residual records may justify a new research problem. That would be new evidence, not hidden debt in this decision.

`PROCESS_GAP = CLOSED_BY_SIMPLIFICATION`

`CURRENT_CHANGE = NO`

`NEXT_RELEASE_DOC_ABSORPTION = REQUIRED`

> **Do not invent a ladder when the real need is truthful evidence scope.**
