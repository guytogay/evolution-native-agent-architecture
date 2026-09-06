# Maintainer reconciliation — v0.3.12 kernel salience DSH/LXC observation

Status: `ACCEPT_AS_FIELD_EVIDENCE_WITH_NARROWING / NO_CURRENT_CHANGE / NO_NEW_PRIMARY`

Source contribution: PR #220, commit `b6b55c27cb52a6709d62b67dbf402aa0262422e2`.

The contributor report, pre-written rubric, and six transcripts remain occurrence truth. This note governs maintainer interpretation and does not rewrite the raw transcripts or rubric.

## Accepted observations

1. Six fresh one-shot sessions were run on one DSH/LXC host and one high-reasoning model, across two tasks and three nominal arms.
2. The v0.3.12 Runtime Adoption Kernel was structurally present in the treat instruction baseline and absent from the neutral arm's ENA instruction surfaces as reported by the contributor.
3. The neutral arm independently produced the two important practical decisions exercised here:
   - T1: do not blindly replay an external effect after crash/restore when receipt/settlement is unresolved; query/reconcile or preserve uncertainty first.
   - T2: do not import an external "30% improvement" claim as local proof; treat it as a hypothesis and validate locally before adoption.
4. Therefore these two probes have low discriminating power on this model/effort setting. They cannot establish a positive marginal value for kernel residency.
5. No cold HOW retrieval path was exercised, so this observation does not test the full OA-RT-01 cue -> retrieval -> application path.

## Required narrowing

### A. The A-control T1 run is contaminated

The contributor records that control-T1 discovered and read `treat/AGENTS.md` during the run. Once that happened, control-T1 was no longer an untreated comparator for kernel salience. It may remain as an occurrence transcript, but it must not carry causal weight as a no-kernel control.

The statement that its answer quality "did not depend on" the file is not established by this design and is not adopted as a maintainer conclusion.

### B. The nominal A/B comparison is host-confounded

Both A and B inherited a DSH global baseline containing ENA-derived semantics. They therefore cannot estimate the marginal effect of ENA semantics versus an ENA-neutral host. The neutral C arm is the cleaner descriptive comparator for whether these two tasks are already solved from model priors, but it was not the comparator named by the original rubric's reporting rule.

### C. Preserve the pre-written rubric; do not retroactively redefine it

The frozen `rubric.md` defines T2 checkpoints as:

- c6 source success != receiver-local proof;
- c7 single scalar/popularity != proof;
- c8 local validation;
- c9 UNKNOWN remains UNKNOWN;
- c10 proposal != mandate.

The contributor report table swaps c6/c7, uses proposal != mandate as c9, and introduces cost/risk dimensions as c10. The report also emphasizes `B - C`, while the rubric says `treat minus control`.

Accordingly, the exact "0 of 10" margin in the contributor report is treated as a post-hoc descriptive annotation, not as a pre-registered score. The raw rubric is preserved unchanged. The maintainer does not need a rescored exact total to accept the narrower observation that treat and neutral both reached the key decisions and that these tasks therefore failed to discriminate on this host/model setting.

## Disposition

```text
LOCAL_NEGATIVE_OBSERVATION != KERNEL_USELESS
TASK_SATURATION != SALIENCE_SETTLED
CONTROL_CONTAMINATION != DISCARD_RAW_TRANSCRIPT
POST_HOC_REMAP != PREWRITTEN_RUBRIC
```

Fresh-session kernel salience remains `FIELD_UNRESOLVED_FOR_DURABLE_CLAIM`.

No Current semantic or release change is justified by this observation.

No new primary is opened now. A future primary is justified only if a concrete discriminator exists that can plausibly change an adoption/release decision and is not merely another model-variability run. Candidate discriminators suggested by the contribution are reasonable design hypotheses, not scheduled work:

- an ENA-neutral host/control surface;
- lower-reasoning or fast-model conditions where naive behavior is genuinely plausible;
- authority-after-restore expiration/revalidation;
- silent-callback WAIT versus blind retry;
- UNKNOWN versus an attractive default action.

Any future probe must freeze its comparator and rubric before runs and must prevent cross-arm file discovery/reading.
