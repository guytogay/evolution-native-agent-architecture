# ENA v0.3.5 candidate.2 — DSH narrow residual revalidation summary

Date: 2026-08-23

## Validator identity

`SAME_FALSIFIER / NARROW_RESIDUAL_REVALIDATION / NOT_FRESH`

Validator: DSH / DeepSeek v4-flash, same falsifier that previously performed the candidate.1 targeted revalidation.

This evidence must not be relabeled as fresh independent validation.

## Frozen identity verified by validator

- frozen source commit: `8393b8b05d34797965c612e8b9ca938d306f6322`
- expected candidate tree: `b10854f191d9641138e2f44278f043f124a2e120`
- expected Current tree during validation: `b237802c08d608bb9be650fe213b7846d3be4bf6`
- freeze-record commit: `34e12333bcbe6cf8a3a2a992040d93012ead868b`

The validator reported all identity checks passed and did not modify canonical repository state.

## Narrow verdict

`NARROW_REVALIDATION_SUPPORTED`

## Mechanical findings

### N1 — CLOSED

Attack:
- mutate a valid packet to `source_lifecycle_state="BANANA"`;
- recompute a valid `content_sha256`;
- pass it through the real CLI import/validate path.

Observed result:
- CLI itself rejected the packet with `invalid source_lifecycle_state`;
- rejection did not depend only on JSON Schema.

### N2 — CLOSED

Attack:
- mutate `source_authentication` to `TOTALLY_TRUSTED`;
- recompute digest;
- import through CLI.

Observed result:
- CLI rejected the forged authentication value;
- normal generated packets still contain `NOT_AUTHENTICATED_BY_THIS_PACKET`;
- packet digest remained distinct from source authentication.

Supported distinction:

`packet digest != source authentication`

### Adjacent transfer_status — CLOSED

Attack:
- mutate `transfer_status` to `LOCALLY_PROVEN`;
- recompute digest;
- import through CLI.

Observed result:
- CLI rejected the forged transfer status;
- normal packet remains `TRANSFERRED_SOURCE_EVIDENCE_NOT_LOCAL_PROOF`.

### N7 — CLOSED

The validator:
- recorded the committed regression-result file hash;
- ran `python releases/v0.3.5-candidate/tools/regression_suite.py`;
- confirmed the hash remained unchanged;
- confirmed `git diff` remained empty and worktree clean;
- confirmed committed result contains the candidate implementation surface and explicit inherited-regression coverage boundary.

## candidate.1 regression preservation

Validator reported PASS for:

- `ena_evolve.py selftest` — 10 cases;
- `candidate1_adversarial.py`;
- `candidate2_adversarial.py`;
- inherited regression suite — `10/10 + 164/164 + 61/61`.

Additional CLI spot checks remained correct:

- zero-experiment `SUPPORTED` rejected;
- imported negative evidence cannot become local positive selection without local experiment;
- receiver-side real local experiment can produce a different local positive selection while source negative lineage remains preserved;
- `UNKNOWN + INTEGRATED` exports as `UNRESOLVED_VARIATION`;
- `ARCHIVED + HARMFUL` exports as `NEGATIVE_EVIDENCE`;
- closure reads represented unresolved state;
- a merely `PROPOSED` candidate does not globally freeze closure.

## Evolution-starvation / over-governance check

No evolution-starvation or over-governance regression was found.

The validator explicitly confirmed:

- legal migration remains available;
- no external signature, trust-anchor, or approval ritual became universally required;
- source `HARMFUL / NOT_SUPPORTED` variation remains eligible for receiver-side re-experiment in a different environment;
- candidate.2 fixes are narrow mechanical packet-consistency guards.

## Constitution / Current boundary

Validator reported:

- English Constitution unchanged relative to candidate.1;
- zh-CN Constitution unchanged relative to candidate.1;
- Current remained v0.3.4 during revalidation;
- no universal bilingual-conformance claim was added.

## Retained residuals

N3–N6 remain explicit research/field residuals, not silently closed:

- N3 — repeated evaluation/reinterpretation of the same represented experiment;
- N4 — source-negative lineage is nested after receiver positive reselection;
- N5 — no in-place restore/reopen transition for `ARCHIVED/RETIRED` in the reference tool;
- N6 — nested migration lineage can grow in depth.

The validator did not find evidence that these had become MATERIAL/BLOCKING.

## Validator's release-cycle judgment

The validator answered that there is **no material reason to create candidate.3** based on N1/N2/N7 and candidate.2's repair approach.

Its rationale was that the fixes are narrow mechanical consistency guards, preserve viable migration/evolution, add no new rule/gate/approval ceremony, and leave N3–N6 visible for future reality-driven research.

## Claim boundary

This evidence supports only the narrow statement:

> candidate.2 closes the release-decision residuals left by candidate.1 targeted revalidation without introducing a newly observed material regression.

It does not establish:

- fresh independent validation of candidate.2;
- Current/release status;
- universal Host/model/language behavior;
- external evidence truth;
- universal field benefit.
