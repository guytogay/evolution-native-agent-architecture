# ENA Research Methodology Changelog

Status: `PROJECT_CONTROL_PLANE / METHOD_LINEAGE / OPEN_ENDED`

This file records **why the research method changed**, not every wording edit.

## 2026-08-26 — Anti-dissolution reconstruction discipline

Trigger:

A post-v0.3.6 review showed that ENA research had repeatedly treated a higher-level semantic property as if it solved the concrete engineering problem underneath it.

Correction:

```text
PROPERTY != ORGAN != HOST_BINDING != EVIDENCE != ADOPTION
WHAT -> WHY -> HOW -> EVIDENCE
```

Practical effect:

- parent-property coverage no longer closes organ engineering;
- `Host-specific`, `not Core`, `reference organ`, and `no release delta` are not automatic stopping operators;
- anti-ablation archaeology became a reconstruction phase.

## 2026-08-26 — HOW growth / tree discipline

Trigger:

Applying narrow-waist/semantic-compression pressure to the HOW layer caused implementation dissolution.

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

A successor session had access to prior-session summaries and GitHub records containing anti-dissolution/plural-HOW ideas, but still resumed work by selecting one visible organ and deepening it. The method had been written/retrieved but was not salient/applied.

Correction:

```text
WRITTEN -> RETRIEVED -> INTERPRETED -> SALIENT -> APPLIED
DURABLE != DISCOVERABLE != RETRIEVED != SALIENT != APPLIED
```

Practical effect:

- project-control/bootstrap surfaces became explicit;
- a handoff summary is a pointer, not canonical project state;
- successful method inheritance is behavioral, not merely verbal.

## 2026-08-26 — Branch-governance / research-control-plane correction

Trigger:

The active research methodology, plan, and reconstruction state were stored only on a research branch while `main` contained many historical branches and no canonical active-research pointer. A new session starting from the default branch could not know which branch to inherit without doing a branch census.

Correction:

- `main` carries the project/research control plane;
- `research/ACTIVE-RESEARCH.yaml` defines exactly one active research integration branch;
- temporary branches never become continuation authority by existence/recency;
- branch roles/lifecycle are standardized in `research/BRANCH-GOVERNANCE.md`;
- historical cleanup preserves commit/PR/freeze lineage rather than preserving every branch name forever.

Practical effect:

A successor begins at `main`, reads one stable pointer, then follows the active workspace.

## 2026-08-26 — Branch-centric continuation identity

Trigger:

The control plane bound continuation state to a specific PR number and cached active-branch head SHA. Both proved unstable.

Correction:

```text
ACTIVE_RESEARCH_AUTHORITY = MAIN_VISIBLE_BRANCH_POINTER
OPEN_PR = TRANSIENT_DISCOVERABLE_INTEGRATION_ARTIFACT
HEAD_SHA = LIVE_REVERIFY_BEFORE_WRITE
```

Practical effect:

- the stable active research branch may span multiple PR generations;
- opening/merging/closing a PR on that branch no longer requires another branch handoff;
- exact head is observed from GitHub before writes instead of embedded as a self-referential lock.

## 2026-08-26 — Project State Alignment Gate

Trigger:

After branch cleanup/checkpoints/successor activation, several individually reasonable documents still described different generations of the project. The repo was durable, but routing, method, plan, Progress, and historical references could drift apart after a material transition.

Correction:

```text
INDIVIDUAL_FILE_CORRECT != PROJECT_STATE_COHERENT
MATERIAL_TRANSITION -> ALIGN -> RESUME
HISTORY_PRESERVED != HISTORY_USED_AS_CURRENT_POINTER
```

Canonical procedure:

`research/methodology/PROJECT-STATE-ALIGNMENT-GATE.md`

Practical effect:

- after material branch/control-plane, directory, methodology, plan, release-state, or checkpoint transitions, align live repository state, routing, methodology, plan, Progress, and next actions before substantive work resumes;
- old branches/PRs remain lineage without masquerading as current pointers;
- the gate is not required after every ordinary commit.

## 2026-08-27 — Convergence/divergence discipline

Trigger:

During v0.3.7 candidate author-falsification work, an adversarial harness was refactored from an observed 1080 pass conditions to 188 more structured pass conditions. The project-manager initially described the smaller harness as an improvement before proving that materially distinct predecessor attack/failure shapes had not been lost.

The user flagged this as a characteristic LLM success-narration bias: summarization/convergence can look like progress while silently ablating the HOW/failure possibility space.

Correction:

```text
COMPRESS REPRESENTATION != COMPRESS POSSIBILITY SPACE
PROVEN_BEHAVIORAL_EQUIVALENCE -> MAY_COMPRESS
UNPROVEN_EQUIVALENCE -> DO_NOT_COLLAPSE
UNKNOWN_SPACE -> EXPAND
```

Canonical focused method:

`research/methodology/CONVERGENCE-DIVERGENCE-DISCIPLINE.md`

Incident evidence:

`research/methodology/incidents/2026-08-27-CONVERGENCE-BIAS-INCIDENT.md`

Practical effect:

- smaller assertion/file/category counts are not success evidence by themselves;
- HOW/failure/Host/evidence distinctions remain separate while behaviorally distinct or equivalence is unproven;
- representation duplication may still be compressed once it adds no distinct behavior or decision value;
- the 1080 -> 188 harness change required an anti-ablation audit before independent candidate review.

## 2026-08-27 — Standardized session/project-manager handoff discipline

Trigger:

The user intentionally replaced an unstable project-manager session and requested that future Agents/sessions know by default how to hand a project over and how to take it over.

During preparation, live-state inspection showed that main-visible project-state projections lagged actual candidate/freeze state. A chat summary alone could not provide safe continuity.

Correction:

```text
PROJECT_CONTINUITY > SESSION_CONTINUITY
HANDOFF = DURABLE_BOOTSTRAP_PROJECTION
HANDOFF != PROJECT_AUTHORITY
```

The initial canonical focused method was created as `research/methodology/SESSION-HANDOFF-DISCIPLINE.md` together with `research/handoffs/CURRENT-HANDOFF.yaml`.

Incident evidence:

`research/methodology/incidents/2026-08-27-SESSION-HANDOFF-STANDARDIZATION.md`

Practical effect:

- outgoing sessions persist material work, reverify live state, align stale control surfaces, create a classified handoff record, and publish it through a stable pointer;
- incoming sessions use the handoff for speed, then independently verify canonical Current/live refs/frozen identities/method/Progress/plan;
- next sessions should not ask the user to reconstruct project state already persisted in GitHub.

## 2026-08-27 — Handoff hierarchy correction: framework, records, and project methodology

Trigger:

The user identified that the first handoff layout mixed reusable handoff/project-management method with one dated project-state-specific handoff occurrence. The dated folder sat directly under `research/handoffs/`, reusable project-management lessons were trapped inside it, while the handoff/takeover discipline itself lived under `research/methodology/`.

The user also made explicit that **project methodology is as important as project state during takeover**, and that **rules for handing over and taking over are themselves first-class continuity method**.

Correction:

```text
HANDOFF_FRAMEWORK != HANDOFF_RECORD
HANDOFF_RECORD != PROJECT_METHODOLOGY
PROJECT_STATE_INHERITANCE_WITHOUT_METHOD_INHERITANCE = INCOMPLETE_TAKEOVER
INSTANCE_DISCOVERS_METHOD -> PROMOTE_METHOD -> KEEP_INSTANCE_AS_EVIDENCE
```

Canonical handoff framework moved to `research/handoffs/` root:

- `HANDOFF-PROTOCOL.md`;
- `REQUIRED-TAKEOVER-CONTEXT.yaml`;
- `PROJECT-MANAGEMENT-DISCIPLINE.md`;
- `CURRENT-HANDOFF.yaml`.

Dated occurrences moved under `research/handoffs/records/`.

ENA research methodology remains under `research/methodology/` and is explicitly mandatory takeover context.

Incident evidence:

`research/methodology/incidents/2026-08-27-HANDOFF-HIERARCHY-CORRECTION.md`

Practical effect:

- a successor can distinguish how to take over, what project state was handed over, and how ENA research itself must be conducted;
- outgoing and incoming protocol are equal halves of continuity;
- reusable method is promoted out of instance records;
- the current handoff pointer directly declares method inheritance rather than relying on indirect links inside a dated manifest.

## 2026-08-27 — Independent validator information-boundary correction

Trigger:

After the project correctly required fresh independent Phase A for v0.3.7 candidate.0, the first validator handoff and PR #115 still exposed a detailed author-generated attack map before Phase A. The list was open-ended and not an expected-verdict oracle, but it could prime the validator to search the author's already-imagined branches and preserve shared blind spots.

Correction:

```text
PROJECT_MANAGER_TAKEOVER_CONTEXT != FRESH_VALIDATOR_PRE_PHASE_A_CONTEXT
PROJECT_MANAGER_SUCCESSION -> MAXIMIZE_RELEVANT_CONTEXT_CONTINUITY
FRESH_VALIDATOR_PHASE_A     -> MINIMIZE_AUTHOR_SHAPED_PRIMING
PHASE_A_FINDINGS_PERSISTED  -> AUTHOR_CONTEXT_MAY_OPEN_FOR_PHASE_B
```

Canonical focused method:

`research/methodology/INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md`

Incident evidence:

`research/methodology/incidents/2026-08-27-INDEPENDENT-VALIDATOR-PRIMING-INCIDENT.md`

Practical effect:

- fresh validators receive a minimal-prime Phase-A entry rather than the full project-manager handoff or author attack taxonomy;
- Phase A derives its claim/failure space from exact frozen bytes and persists findings before Phase B;
- the detailed author validator handoff is retained as Phase-B context/lineage rather than erased;
- a reviewer with prior material author-oracle exposure may still contribute, but cannot relabel itself as fresh Phase A.

## 2026-08-27 — Candidate self-priming / A-S + A-P split

Trigger:

A genuinely fresh reviewer followed the candidate.1 blind intake and opened a permitted candidate-local file, `CANDIDATE-BASELINE.yaml`. The file itself disclosed predecessor findings, `NEEDS_REVISION`, required repairs, repair commits, and validation lineage. The reviewer correctly stopped rather than claiming freshness.

Further contamination audit found the same information-role problem in changelog/lineage, expected fixtures, regression/selftest corpora, and prior adversarial probes.

Correction:

```text
CANDIDATE_LOCAL != AUTOMATICALLY_BLIND_SAFE
FULL_PACKAGE_INDEPENDENCE != FULL_PACKAGE_SEARCH_SPACE_BLINDNESS
VALIDATION_INTERFACE_DEFECT != CANDIDATE_BYTE_DEFECT

FROZEN_CANDIDATE
-> EXACT_BYTE_PRESERVING_BLIND_SEMANTIC_VIEW
-> A-S BLIND SEMANTIC FALSIFICATION
-> A-S SEAL
-> A-P INDEPENDENT PACKAGE/HISTORY/ORACLE AUDIT
-> PHASE B AUTHOR RECONCILIATION
```

Canonical focused method:

`research/methodology/INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md`

Incident evidence:

`research/methodology/incidents/2026-08-27-CANDIDATE-SELF-PRIMING-INCIDENT.md`

Practical effect:

- the invalidated candidate.1 Issue #128 remains occurrence truth but carries no Phase-A seal;
- a validation projection may withhold explicitly declared history/oracle/selftest surfaces while retaining behavior-bearing candidate bytes exactly;
- the projection is not a successor candidate and the withheld files are not release ablation;
- A-S must be durably sealed before withheld candidate-local history/oracles open;
- A-P remains independent but is not mislabeled search-space blind;
- candidate.2 is not manufactured for a validation-interface defect alone; a material candidate/package correction basis is still required.

## 2026-08-28 — Physically isolated independent-review carrier

Trigger:

Candidate.2 fresh intake Issue #137 was correctly aborted before A-S seal because GitHub's normal candidate-directory view auto-rendered a README range that the blind-view manifest had explicitly withheld. Broader surface audit showed that same-repository navigation/search and candidate-local implementation comments could also expose author-shaped priors even when the reviewer followed the declared path.

Correction:

```text
PROCEDURAL_RANGED_READ != INFORMATION_BOUNDARY
PROCEDURAL_PATH_AVOIDANCE != INFORMATION_BOUNDARY
SEMANTIC_FAILURE_VOCABULARY != AUTHOR_ATTACK_MAP
```

Canonical focused method:

`research/methodology/PHYSICALLY-ISOLATED-INDEPENDENT-REVIEW-CARRIER.md`

Incident evidence:

`research/methodology/incidents/2026-08-28-CANDIDATE2-BLIND-CARRIER-LEAK-INCIDENT.md`

Practical effect:

- when a repository/UI cannot enforce withholding, fresh A-S uses a physically isolated deterministic semantic capsule rather than a same-repository branch UI;
- A-P uses a separate exact frozen-package supplement that is not supplied until A-S is content-sealed;
- an A-S SHA-256 of exact report bytes may serve as the pre-A-P seal when the fresh environment lacks authenticated GitHub write access;
- mechanically justified projections may remove history-bearing comments/docstrings while preserving executable AST semantics;
- priming scans distinguish the contract's own failure vocabulary from author attack/probe history;
- manifest self-hash is excluded by definition while non-self payload hashes and outer capsule hashes are verified;
- authoritative candidate.2 r3 carrier audit run `33131773164` passed deterministic build, physical isolation, exact A-P frozen-package equality and payload inventory checks;
- no frozen candidate or Current bytes changed.

## Future changes

Add a new entry when a research-process failure, field observation, handoff incident, or stronger method changes how future ENA research should actually be conducted.

Do not add entries solely for editorial rephrasing.