# ENA Research Methodology

Status: `CANONICAL_PROJECT_RESEARCH_METHOD_SURFACE / MAIN_VISIBLE / OPEN_CARDINALITY / NON_NORMATIVE_TO_CURRENT`

This directory is the stable home for **how ENA itself is researched**.

It is project process, not adopter-facing ENA Constitution semantics and not the canonical session-handoff framework.

Session succession lives under:

`research/handoffs/`

Canonical succession method:

`research/handoffs/HANDOFF-PROTOCOL.md`

Mandatory takeover context:

`research/handoffs/REQUIRED-TAKEOVER-CONTEXT.yaml`

This separation is intentional:

```text
HANDOFF FRAMEWORK = how operators exchange project responsibility
PROJECT METHODOLOGY = how ENA research itself is performed
HANDOFF RECORD = one time-bounded succession occurrence
```

A successor project manager must inherit both framework and methodology.

A **fresh independent validator** is a different epistemic role. Before its blind semantic work is sealed, it should receive a deliberately priming-reduced target view rather than project-manager continuity context or candidate-local author history/oracles. See `INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md` and, when repository/UI navigation cannot enforce the boundary, `PHYSICALLY-ISOLATED-INDEPENDENT-REVIEW-CARRIER.md`.

## Canonical rule

The main-visible methodology is the research-control reference for session inheritance.

Fast-moving active research may contain newer observations, but a material method change that should govern future work must be reconciled to canonical methodology on `main` and recorded in the method changelog.

```text
CHAT_INSIGHT != DURABLE_METHOD
ACTIVE_BRANCH_NOTE != CANONICAL_METHOD
METHOD_WRITTEN != METHOD_APPLIED
```

## Read order

1. `ENA-RESEARCH-DISCIPLINE.md` — open-cardinality master method ledger.
2. `CONVERGENCE-DIVERGENCE-DISCIPLINE.md` — when abstraction/compression is valid and when HOW/failure/Host variation must remain open or grow.
3. `PROJECT-STATE-ALIGNMENT-GATE.md` — realign routing, method, plan, progress, candidate/release state, and next actions after material transitions.
4. `INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md` — role/search-space/oracle information boundaries, including A-S blind semantic falsification and post-seal A-P package audit for self-describing candidates.
5. `PHYSICALLY-ISOLATED-INDEPENDENT-REVIEW-CARRIER.md` — enforce A-S boundaries at the carrier layer when same-repository navigation/search/auto-render can expose withheld context.
6. `METHOD-CHANGELOG.md` — why significant method corrections were introduced.
7. `incidents/` — concrete method failures that changed future behavior.
8. `../BRANCH-GOVERNANCE.md` — research/candidate topology across sessions.
9. `../ACTIVE-RESEARCH.yaml` — active research routing.
10. `../handoffs/CURRENT-HANDOFF.yaml` — current succession pointer.
11. `../handoffs/HANDOFF-PROTOCOL.md` — outgoing/incoming succession rules.
12. `../handoffs/REQUIRED-TAKEOVER-CONTEXT.yaml` — explicit mandatory inheritance context for project-manager succession.

Focused methodology files may be added when a distinction changes behavior; file count is not a completeness claim.

## Core shape

```text
TELOS / PURPOSE
      |
      v
WHAT / WHY
semantic trunk; abstraction/compression may help
      |
      +--> HOW-A
      +--> HOW-B
      +--> HOW-C
      +--> ...
             |
             +--> Host binding / tool / process / protocol
             +--> failure / fallback behavior
             +--> evidence
```

> **Compress the semantic trunk; let concrete HOWs branch.**

And:

```text
COMPRESS REPRESENTATION != COMPRESS POSSIBILITY SPACE
PROVEN_BEHAVIORAL_EQUIVALENCE -> MAY_COMPRESS
UNPROVEN_EQUIVALENCE -> DO_NOT_COLLAPSE
UNKNOWN_SPACE -> EXPAND
```

For fresh independent validation, preserve two further distinctions:

```text
PROJECT_MANAGER_TAKEOVER_CONTEXT
!=
FRESH_VALIDATOR_PRE_A-S_CONTEXT

FULL_PACKAGE_INDEPENDENCE
!=
FULL_PACKAGE_SEARCH_SPACE_BLINDNESS
```

The project manager needs continuity. The fresh validator needs enough exact target identity and behavior-bearing material to inspect safely without receiving the author's prior search map before independent semantic findings are sealed.

For a self-describing candidate:

```text
CANDIDATE_LOCAL
!=
AUTOMATICALLY_BLIND_SAFE

FROZEN_CANDIDATE
-> ROLE-AWARE A-S CARRIER
-> A-S BLIND SEMANTIC FALSIFICATION
-> A-S SEAL
-> A-P INDEPENDENT PACKAGE/HISTORY AUDIT
-> PHASE B AUTHOR RECONCILIATION
```

When a repository/UI surface cannot enforce withholding:

```text
PROCEDURAL_RANGED_READ != INFORMATION_BOUNDARY
PROCEDURAL_PATH_AVOIDANCE != INFORMATION_BOUNDARY

FROZEN_TARGET
-> PHYSICALLY_ISOLATED A-S CARRIER
-> A-S CONTENT SEAL
-> ONLY THEN A-P SUPPLEMENT
```

A blind validation projection or isolated carrier is not a successor candidate and its exclusions are not release ablation.

Generic semantic failure vocabulary must not itself be removed merely because it resembles an attack term:

```text
SEMANTIC_FAILURE_VOCABULARY != AUTHOR_ATTACK_MAP
```

## Project-state alignment rule

Durable files can all be locally reasonable yet collectively stale after a material transition.

```text
INDIVIDUAL_FILE_CORRECT != PROJECT_STATE_COHERENT
MATERIAL_TRANSITION -> ALIGN -> RESUME
```

Use `PROJECT-STATE-ALIGNMENT-GATE.md` when a handoff, branch transition, directory/method change, candidate/release-state change, or plan change can make current-state surfaces disagree.

The gate is not ceremony after every ordinary content commit.

## Update discipline

When research reveals a new method defect or stronger discipline:

1. capture triggering evidence/incident durably;
2. determine whether the lesson changes research behavior rather than wording;
3. update the master ledger or add a focused method;
4. record why in `METHOD-CHANGELOG.md`;
5. update project-control pointers only when routing/phase changes;
6. run alignment when the change materially affects current-state coherence;
7. do not force the method into an existing category merely to keep the list short;
8. do not split methods merely to make the directory look comprehensive.

```text
CURRENT_METHOD_SET != COMPLETE_METHOD_SPACE
METHOD_FILE_COUNT != METHODOLOGY_COMPLETENESS
```

## Inheritance test

A successor has not inherited the method merely because it can quote it.

```text
WRITTEN -> RETRIEVED -> INTERPRETED -> SALIENT -> APPLIED
```

If it reads anti-dissolution/plural-HOW discipline and then immediately compresses the work into one abstract mechanism or selects before recovery, inheritance failed.

If it treats a smaller assertion/file/category count as success without proving behavioral equivalence, inheritance failed.

If a project-manager successor reads project state but skips the handoff framework or project methodology, takeover failed.

If a fresh independent validator is given the author's detailed attack map before A-S, information hygiene failed.

If a self-describing candidate exposes predecessor findings, repair history, expected fixtures, or regression/selftest answers and the project calls the resulting search "blind" without an explicit boundary, information hygiene failed.

If a declared blind view still lets ordinary UI navigation, auto-render, repository search, or branch traversal expose withheld material before A-S seal, the validation interface failed even if the written instructions said not to read it.

If A-P opens candidate-local history before A-S is durably sealed, the search-space independence claim for A-S failed.

If an A-S carrier removes ordinary semantic failure vocabulary merely to make a priming scan quiet, the carrier compressed the object under review rather than preserving independence.

If a manifest claims a stable hash of its own final bytes by recording a pre-final self-hash, carrier integrity representation failed; manifest self-hash must be excluded by definition and the outer carrier hash should bind the final manifest bytes.

If a validation projection is treated as a releasable candidate or its excluded files are silently treated as release deletions, validation-interface separation failed.

If it reads a new branch/control-plane state but continues from stale routing or superseded plan, project-state inheritance failed.

> **Do not merely inherit conclusions. Inherit the method that governs how new conclusions may be produced — and give each role only the context its epistemic job requires.**
