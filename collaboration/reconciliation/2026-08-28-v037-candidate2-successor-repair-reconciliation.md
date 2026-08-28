# ENA v0.3.7 candidate.2 successor repair reconciliation

Date: 2026-08-28

## Status

`SUCCESSOR_REPAIR_RECONCILED / EXACT_PREFREEZE_PASS / READY_FOR_EXTERNAL_FREEZE / NOT_CURRENT / NOT_RELEASED / ATTACK_CARDINALITY_OPEN`

This record reconciles the candidate.2 successor work required by the frozen candidate.1 fresh blind semantic A-S/A-P review and Phase B. It distinguishes candidate-byte defects, nearby homologous branches, test-harness defects, and historical/self-description projection.

It does **not** claim fresh independent review of candidate.2 and does not promote anything to Current.

## Predecessor frozen occurrence truth

Candidate.1 remains frozen and immutable:

- identity: `v0.3.7-candidate.1`
- frozen source: `ae6903464133cb5bcf3cd8909ecae1215fe0b9ba`
- frozen candidate subtree: `c0458e0d7ea417b841cbf4c8bf6e64e4aff37319`
- fresh blind A-S seal: `2e6b46aeedc1945a03aac93620ad36aa1ccbd70f`
- A-P completion commit: `b970148fe9596ea9cad0a2817a3b399a1d2b75f5`
- Phase-B verdict: `NEEDS_REVISION / CANDIDATE_2_REQUIRED`

Candidate.1 was not mutated to absorb these repairs.

## Sealed candidate.1 findings inherited by candidate.2

The fresh A-S/A-P review established five candidate.1 defects relevant to the successor:

1. **A-S-01 — integration chronology:** a committed integration could precede represented reality contact when `selection_state_at_commit=UNKNOWN`.
2. **A-S-02 — durable migration provenance:** top-level and nested source identity/digest/purpose claims were not bound after import.
3. **A-S-03 — Authority false-BLOCK:** a valid `authority_required=false` query could be poisoned by an unrelated malformed grant.
4. **A-S-04 — Effect Lifecycle chronology:** equal-sequence contradictory receipts could let input order influence next action.
5. **A-P-05 — active self-description drift:** adopter-facing candidate.1 surfaces retained stale predecessor/status projection.

Phase B classified these as material candidate-byte/shared-blind-spot defects rather than oracle errors.

## Candidate.2 focused repair round 1

Focused repair workflow:

`ENA v0.3.7 Candidate.2 Focused Repair Gate`

Run:

`33090294820`

Result:

`SUCCESS`

Candidate cargo repair commit:

`613c1e8be898865ce674199118618c0f9389da97`

Observed behavior included:

- record selftest: 30 observed cases;
- helper selftest: 13 observed cases;
- Authority fixtures: 18, all matched;
- Effect Lifecycle fixtures: 20 at that stage, all matched;
- inherited composed-validator regression: zero flips;
- Current isolation: PASS;
- `ATTACK_CARDINALITY=OPEN`;
- `FRESH_A_S_REPEATED=NO`.

Round 1 repaired the four sealed semantic findings and the first active self-description slice without rewriting historical occurrence truth.

## Nearby open-branch expansion

Read-only observation workflow:

`ENA v0.3.7 Candidate.2 Open Branch Probes`

Run:

`33090585653`

Result:

`SUCCESS / OBSERVATION_ONLY`

Two homologous decision-changing branches remained open:

1. a durable migration record could claim `source_selection_state=SUPPORTED` and `source_lifecycle_state=INTEGRATED` while retaining empty represented source experiment/evaluation/integration history;
2. same-effect, same-sequence attempts with conflicting represented outcomes could remain valid while array order changed `next_action` between retry and wait.

The same probe also showed many predecessor labels. Those were separated into:

- legitimate historical/predecessor occurrence truth; and
- active candidate-facing projection that still needed repair.

This expansion paid epistemic rent because it followed the structure of the sealed findings rather than adding arbitrary test volume.

## Candidate.2 focused repair round 2

The first round-2 workflow attempt stopped safely in an exact-anchor transform before candidate bytes were committed. The failure was a transformation-anchor ambiguity, not candidate evidence.

Successful round-2 workflow:

`ENA v0.3.7 Candidate.2 Open Branch Repair Gate`

Run:

`33091573678`

Result:

`SUCCESS`

Candidate cargo repair commit:

`34458c2ba0b94b82d182afe2606efe48e741bcda`

Round 2:

- reused the existing represented source-history validation boundary for durable migration provenance without authenticating source truth or upgrading receiver-local selection;
- rejected same-effect/same-sequence conflicting attempt state;
- rejected same-effect/same-sequence conflicting receipt status;
- preserved same-sequence duplicate observations when their represented state/status is the same, preventing a new blanket false-BLOCK rule;
- completed active candidate.2 identity/status projection across adopter-facing Operational, Reference, and zh-CN surfaces while preserving explicit historical lineage.

Observed final round-2 evidence:

- record selftest: 32 observed cases;
- helper selftest: 13 observed cases;
- Authority fixtures: 18;
- Effect Lifecycle fixtures: 23;
- inherited composed-validator regression: zero flips;
- shallow durable supported/integrated source history rejected;
- conflicting same-sequence attempts rejected in either input order;
- same-state duplicate attempt/receipt controls remain accepted;
- semantic trunk and inherited boundaries: PASS;
- Current isolation: PASS.

## Committed readback re-probe

The original observation probe was rerun against the committed round-2 branch:

- workflow run: `33091652046`
- result: `SUCCESS`
- purpose: verify that repaired behavior survived commit/readback rather than existing only in a transient Actions workspace.

No candidate byte change resulted from this re-probe.

## Pre-freeze self-description transition

After semantic repairs had converged, candidate-facing state still described repair as in progress. Freezing that state would have recreated the package/self-description problem identified by A-P-05.

A status-only transition was therefore constrained to exactly five self-description files:

- `CANDIDATE-BASELINE.yaml`
- `README.md`
- `00-READ-ME-FIRST.md`
- `07-ADOPTION-AND-FIELD-VALIDATION.md`
- `08-RELEASE-DISCIPLINE.md`

Successful transition workflow run:

`33095122958`

Final candidate cargo/self-description commit:

`aba6f12cabc84146c92809bd7d8293a3c907dc55`

Candidate subtree after this transition:

`d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`

The transition machine-checked that semantic validators, schemas, reference tools/fixtures, and Current bytes were unchanged from the repaired cargo.

## Exact pre-freeze validation

Workflow:

`ENA v0.3.7 Candidate.2 Exact Pre-Freeze Gate`

Two early attempts failed safely in **gate tooling**, not in candidate cargo:

- run `33095464230`: schema parity normalization used the wrong historical title string;
- run `33095677352`: successor harness called the Authority module using a nonexistent `resolve` API instead of its actual `resolve_case` API.

Neither failure changed the candidate subtree. The gate/harness was corrected outside candidate cargo.

Successful exact run:

`33095987843`

Result:

`SUCCESS`

Exact tested source commit:

`bda470e0a6b170cec61225a905957a501454a2fe`

Exact tested candidate subtree:

`d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`

Current subtree at the same source:

`7dcbb3934883ffa6cc5292a662588cafc1533cff`

Observed candidate file count:

`118`

The successful gate passed:

- exact source/candidate-tree/Current-tree binding;
- semantic-trunk byte parity and bounded identity projection;
- operational routing, optional-reference policy, Host-equivalent allowance, and deferred lineage;
- inherited composed-validator regression;
- v2 record/helper selftests and CLI export/import roundtrip;
- all bundled reference selftests;
- relocated legacy compatibility regressions;
- inherited author-side attack replay;
- inherited anti-ablation replay;
- candidate.1 successor targeted/open-branch regression replay;
- candidate.2 A-S/A-P-derived record, Authority, Effect, and active-identity regressions;
- zh-CN paired operational fixture structure;
- candidate-local self-containment;
- Python compilation, no bytecode/symlink cargo;
- exact candidate and Current tree cleanliness after validation.

Successor-specific exact observations included:

- candidate.2 state checks: 22;
- inherited author pass conditions observed: 132;
- inherited anti-ablation observations: 103;
- candidate.1 targeted pass conditions: 16;
- candidate.1 open-branch observations: 9;
- candidate.2 record regressions: 5;
- candidate.2 Authority regressions: 2;
- candidate.2 Effect regressions: 4;
- active identity files checked: 9.

These are corpus/evidence facts, not epistemic-completeness thresholds.

The gate explicitly emitted:

- `CANDIDATE2_EXACT_PREFREEZE_VERDICT=PASS`
- `attack_cardinality=OPEN`
- `fresh_independent_candidate2_review_by_this_gate=NO`
- `external_truth=NOT_ESTABLISHED`
- `freeze_authority=NOT_ASSIGNED_BY_THIS_WORKFLOW`

## Reconciled disposition

The candidate.2 repair line has no demonstrated decision-changing residual from the sealed candidate.1 findings or the focused homologous branches exercised above.

This does **not** mean the possibility space is closed.

```text
EXACT_GATE_PASS != UNIVERSAL_CORRECTNESS
KNOWN_REPAIR_BRANCHES_CLOSED != ATTACK_SPACE_EXHAUSTED
VISIBLE_UNKNOWN_SPACE -> REMAINS_OPEN
```

The existing source/receiver candidate-ID namespace collision remains visible as a non-blocking residual because no current ENA contract establishes universal cross-environment candidate-ID uniqueness:

`NO_CURRENT_CONTRACT -> DO_NOT_INVENT_UNIVERSAL_RULE`

## Next governed action

Create an external freeze record binding:

- candidate identity `v0.3.7-candidate.2`;
- exact source `bda470e0a6b170cec61225a905957a501454a2fe`;
- exact candidate subtree `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`;
- exact pre-freeze run `33095987843`;
- Current subtree `7dcbb3934883ffa6cc5292a662588cafc1533cff`.

Do not rewrite candidate cargo merely to say frozen.

After freeze, make an explicit post-freeze independence/release decision. Same-falsifier repair/exact validation remains author-side machine evidence and must not be relabeled as fresh candidate.2 independent support.
