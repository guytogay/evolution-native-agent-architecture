# ENA Research Methodology Changelog

Status: `PROJECT_CONTROL_PLANE / METHOD_LINEAGE / OPEN_ENDED`

This file records **why the research method changed**, not every wording edit.

## 2026-08-26 — Anti-dissolution reconstruction discipline

Trigger:

A post-v0.3.6 review showed that ENA research had repeatedly treated a higher-level semantic property as if it solved the concrete engineering problem underneath it.

Correction:

```text
PROPERTY != ORGAN != HOST_BINDING != EVIDENCE != ADOPTION
```

and:

```text
WHAT -> WHY -> HOW -> EVIDENCE
```

Practical effect:

- parent-property coverage no longer closes organ engineering;
- `Host-specific`, `not Core`, `reference organ`, and `no release delta` are not automatic stopping operators;
- anti-ablation archaeology became a reconstruction phase.

## 2026-08-26 — HOW growth / tree discipline

Trigger:

The project recognized that applying narrow-waist/semantic compression pressure to the HOW layer causes implementation dissolution.

Correction:

> **Compress the semantic trunk; let concrete HOWs branch.**

```text
ONE_WHAT_WHY -> 0..N_CONCRETE_HOW_BRANCHES
HOW_DEFAULT_DIRECTION = CONCRETIZE_AND_GROW
LOCAL_WINNER != UNIVERSAL_WINNER
```

Practical effect:

- multiple Host-specific HOWs may coexist;
- tools, workflows, protocols, state machines, adapters, scripts, and procedures are first-class research outputs;
- evidence attaches to the concrete HOW/Host claim it actually supports.

## 2026-08-26 — Cardinality discovery discipline

Trigger:

Research prompts/tests repeatedly risked turning convenient counts into ontology: fixed HOW registries, exact fixture counts, top-N discovery, and arbitrary quantitative maturity thresholds.

Correction:

```text
REQUESTED_N != DISCOVERED_N
PRESENTATION_N != ONTOLOGY_N
CURRENTLY_OBSERVED_N != FINAL_N
```

Practical effect:

- counts require domain authority before becoming normative;
- presentation quotas no longer constrain discovery;
- pseudo-precise scalar claims are rejected unless measurement semantics exist.

## 2026-08-26 — Experiment epistemic-rent discipline

Trigger:

A proposed multi-model experiment had a result space that was already predictable: models would vary, but no outcome would reveal a new mechanism or change the architecture decision.

Correction:

> **Experiments must pay epistemic rent.**

Practical effect:

- static/state-space/falsification methods are preferred when they already prove the claim;
- stochastic experiments are reserved for interactions, emergence, adaptation, thresholds, long-run dynamics, or genuinely unknown structure.

## 2026-08-26 — Session inheritance incident

Trigger:

A successor session had access to both prior-session summaries and GitHub records containing anti-dissolution/plural-HOW ideas, but still resumed work by selecting one visible organ and deepening it. The method had been written/retrieved but was not salient/applied.

Correction:

```text
WRITTEN -> RETRIEVED -> INTERPRETED -> SALIENT -> APPLIED
```

and:

```text
DURABLE != DISCOVERABLE != RETRIEVED != SALIENT != APPLIED
```

Practical effect:

- project-control/bootstrap surfaces became explicit;
- a handoff summary is a pointer, not canonical project state;
- successful method inheritance is behavioral, not merely verbal.

## 2026-08-26 — Branch-governance / research-control-plane correction

Trigger:

The active research methodology, plan, and reconstruction state were stored only on `research/memory-metabolism-prototype`, while `main` contained many historical branches and no canonical active-research pointer. A new session starting from the default branch could not know which branch to inherit without doing a branch census.

Correction:

- `main` carries the project/research control plane;
- `research/ACTIVE-RESEARCH.yaml` defines exactly one active research integration branch;
- temporary branches never become continuation authority by existence/recency;
- branch roles/lifecycle are standardized in `research/BRANCH-GOVERNANCE.md`;
- historical branch cleanup preserves commit/PR/freeze lineage rather than preserving every branch name forever.

Practical effect:

A successor begins at `main`, reads one stable pointer, then follows the active workspace. It should not need to infer project state from the branch list.

## 2026-08-26 — Branch-centric continuation identity

Trigger:

During the successor-branch transition, the control plane bound continuation state to a specific PR number and cached active-branch head SHA. Both proved unstable: PR generations can change while the active branch remains the same, and recording a branch's own head SHA inside a commit on that branch makes the recorded SHA stale immediately.

Correction:

```text
ACTIVE_RESEARCH_AUTHORITY = MAIN_VISIBLE_BRANCH_POINTER
OPEN_PR = TRANSIENT_DISCOVERABLE_INTEGRATION_ARTIFACT
HEAD_SHA = LIVE_REVERIFY_BEFORE_WRITE
```

Practical effect:

- `research/ena-reconstruction` can remain the active integration branch across multiple PR generations;
- opening/merging/closing a PR on the same active branch no longer requires another branch handoff;
- exact active head is observed from GitHub before writes instead of embedded as a self-referential identity lock.

## 2026-08-26 — Project State Alignment Gate

Trigger:

After branch cleanup, PR #82 checkpointing, successor activation, PR #101 bootstrap reconciliation, and deletion of the predecessor ref, several individually reasonable documents still described different generations of the project. The repo was durable, but routing, method, plan, progress, and historical references could drift apart after a material transition.

Correction:

```text
INDIVIDUAL_FILE_CORRECT != PROJECT_STATE_COHERENT
MATERIAL_TRANSITION -> ALIGN -> RESUME
HISTORY_PRESERVED != HISTORY_USED_AS_CURRENT_POINTER
```

Canonical focused procedure:

`research/methodology/PROJECT-STATE-ALIGNMENT-GATE.md`

Practical effect:

- after material branch/control-plane, directory, methodology, plan, release-state, or checkpoint transitions, ENA research aligns live repository state, routing guides, methodology, master plan, Progress, and next actions before substantive work resumes;
- old branches/PRs remain available as lineage without masquerading as current pointers;
- the gate is not required after every ordinary commit, only transitions capable of creating current-state disagreement.

## 2026-08-27 — Convergence-bias / variation-preservation discipline

Trigger:

During v0.3.7 candidate author-falsification work, an adversarial harness was refactored from an earlier run reporting 1080 observed pass conditions to a phase-aware harness reporting 188 observed pass conditions. The newer oracle removed noisy whole-file/token-style checks and was more decision-focused, but the reduction was initially described too quickly as "progress" before proving that all materially distinct predecessor attack shapes were preserved, replaced by stronger checks, or deliberately retired.

The incident exposed a broader LLM research bias: models often present success as summary, consolidation, reduced visible complexity, and narrative closure. That communication habit is unsafe when applied to ENA HOW space, adversarial/failure space, Host variation, or evidence applicability without an anti-ablation accounting step.

Correction:

```text
COMPRESS REPRESENTATION != COMPRESS POSSIBILITY SPACE
ABSTRACTION_MAY_COMPRESS_DESCRIPTION != LICENSE_TO_COLLAPSE_VARIATION
PROVEN_BEHAVIORAL_EQUIVALENCE -> MAY_COMPRESS
UNPROVEN_EQUIVALENCE -> DO_NOT_COLLAPSE
UNKNOWN_SPACE -> EXPAND
```

Canonical focused method:

`research/methodology/CONVERGENCE-DIVERGENCE-DISCIPLINE.md`

Practical effect:

- a smaller harness, document, taxonomy, organ set, or summary is no longer treated as improvement merely because it is smaller;
- before convergence, materially distinct predecessor variations require disposition as preserved, proven-equivalent merge, stronger replacement, dormant, evidence-backed retirement, lost, or unknown;
- adversarial/falsification work preserves or expands distinct failure shapes by default and compresses only redundant execution/representation;
- LLM-generated summaries are treated as projections rather than ontology/completeness proof;
- HOW, Host, failure, and evidence spaces remain open-cardinality until equivalence or selection is actually supported;
- growth remains subject to complexity/epistemic rent, so the correction does not invert into permanent uncontrolled expansion.

## Future changes

Add a new entry when a research-process failure, field observation, or stronger method changes how future ENA research should actually be conducted.

Do not add entries solely for editorial rephrasing.
