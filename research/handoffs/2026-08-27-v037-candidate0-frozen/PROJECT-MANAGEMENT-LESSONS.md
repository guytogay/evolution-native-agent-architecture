# ENA Handoff — Project Management Lessons

Status: `HANDOFF_MANAGEMENT_LESSONS / METHOD_CONTINUITY / NOT_ENA_CURRENT`

Handoff ID: `2026-08-27-v037-candidate0-frozen`

This file captures project-management and research-execution lessons the next session should **apply**, not merely quote.

## 1. Session replacement must be a normal lifecycle

The project must not depend on one long-lived chat/session remaining healthy.

```text
PROJECT_CONTINUITY > SESSION_CONTINUITY
```

A healthy project-manager session assumes it will eventually be replaced and continuously leaves durable state that another session can inherit.

The new canonical method is:

`research/methodology/SESSION-HANDOFF-DISCIPLINE.md`

## 2. A handoff summary is a map, not authority

Earlier project discipline already recognized:

```text
HANDOFF_SUMMARY != PROJECT_STATE
```

The new handoff system keeps that invariant while making the map much better.

The successor reads the handoff first for speed, then verifies Current, branch refs, candidate freeze identity, methodology, and Progress from canonical sources.

## 3. Project-state alignment is part of handoff, not optional cleanup

This handoff audit found that `research/ACTIVE-RESEARCH.yaml` and `research/plans/PROGRESS.yaml` on main still described v0.3.7 candidate.0 as not yet created, even though candidate.0 had already been built, validated, and frozen.

This is a concrete example of:

```text
INDIVIDUAL_FILE_CORRECT_AT_TIME_T
!=
PROJECT_STATE_COHERENT_AT_TIME_T_PLUS_1
```

A future outgoing session must not simply write a new handoff summary over stale control-plane documents. It must align them.

## 4. LLM success narration has a convergence bias

The session initially described the author-harness reduction from an observed 1080 pass conditions to 188 structured pass conditions as an improvement.

The user correctly challenged that narrative.

Key correction:

```text
FEWER_ASSERTIONS != BETTER_ORACLE
MORE_ASSERTIONS != BROADER_EVIDENCE
```

The relevant question is whether materially distinct failure shapes were preserved.

Canonical method:

`research/methodology/CONVERGENCE-DIVERGENCE-DISCIPLINE.md`

## 5. ENA requires different directions at different layers

Default tendencies:

```text
WHAT / WHY
-> abstraction/compression may be useful

HOW
-> concretize / branch / recombine

FAILURE / ADVERSARIAL SPACE
-> actively expand while distinct failure shapes remain plausible

REPRESENTATION DUPLICATION
-> may compress after equivalence is established
```

Do not generalize “growth is good” or “compression is good” across every layer.

## 6. Growth also pays complexity rent

While documenting the convergence/divergence lesson, duplicate quick-check/checklist files were briefly created without distinct behavioral value and then removed before main integration.

That was valid compression because the removed files added no new HOW, failure shape, applicability boundary, decision, or evidence relation.

Lesson:

```text
ANTI_CONVERGENCE != MAXIMIZE_FILE_COUNT
```

## 7. Preserve occurrence truth when validation oracles are wrong

During candidate identity/pre-freeze work, multiple validation gates produced false positives because their oracle assumptions were too broad or phase-locked.

The project did not rewrite history to pretend they never happened. It preserved the failed runs and corrected the oracle.

This matters because:

```text
VALIDATOR_FAILURE != CANDIDATE_FAILURE
VALIDATOR_PASS != EXTERNAL_TRUTH
```

Always separate:

- candidate defect;
- packaging/navigation defect;
- oracle defect;
- infrastructure failure;
- external evidence gap.

## 8. Frozen identity must remain outside mutable candidate narration

Candidate.0 was frozen by an external record binding an exact source commit and candidate subtree.

The candidate bytes were not modified afterward to insert `frozen: true`.

This prevents:

```text
validate bytes
-> modify bytes to say validated/frozen
-> pretend modified bytes are the validated object
```

The branch may later contain review records; the branch head does not redefine the frozen identity.

## 9. Optional reference packaging must not become hidden adoption burden

v0.3.7 candidate.0 intentionally bundles multiple references while keeping them default-off/context-dependent.

The project must preserve:

```text
BUNDLED_REFERENCE != REQUIRED_RUNTIME_ORGAN
```

A future session should be suspicious if release packaging starts turning research/reference richness into mandatory ceremony.

## 10. Candidate correction must preserve candidate lineage

If independent review or the 1080 -> 188 audit reveals a material candidate-byte defect:

```text
candidate.0 remains frozen occurrence truth
-> create candidate.1
```

Do not edit candidate.0 and rewrite history.

But also do not create candidate.1 merely because another research question exists.

```text
RESEARCH_RESIDUAL != CANDIDATE_BYTE_DEFECT
```

## 11. Recent dialogue should preserve decisions, not recreate raw chat dependence

The new handoff standard stores at least the latest three decision-bearing rounds in structured form.

This is intended to preserve:

- user corrections;
- reversals;
- why the next action changed;
- what durable changes followed.

It is not intended to make raw conversation logs the new project database.

## 12. Exact next action should be singular even when possibility space is plural

The project may preserve many HOW/failure branches while still naming one next execution step.

Current example:

```text
plural adversarial possibility space
BUT
next project-management action = 1080 -> 188 anti-ablation audit
```

This is operational sequencing, not ontological convergence.

## 13. Incoming session behavior is the real handoff test

A successor has not inherited the project merely because it can summarize these lessons.

Successful inheritance means it actually:

- starts from main;
- reads the current handoff pointer;
- verifies live refs;
- does not mutate Current;
- respects frozen candidate identity;
- performs the anti-ablation audit before independent review;
- preserves divergent attack/HOW space where equivalence is unproven;
- does not ask the user to repeat already persisted project state.

```text
HANDOFF_WRITTEN != HANDOFF_APPLIED
```
