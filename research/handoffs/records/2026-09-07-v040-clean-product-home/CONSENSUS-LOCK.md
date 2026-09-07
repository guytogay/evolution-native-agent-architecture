# ENA v0.4 Owner Consensus Lock

Status: `MANDATORY_SUCCESSION_CONTEXT / PROJECT_MAINTAINER_DIRECTION / NOT_ENA_PRODUCT`
Date: 2026-09-07

This record preserves the owner's direction so later sessions do not drift back toward the legacy ENA shape. It is maintainer/succession context. **Do not copy these instructions into the ENA product merely because they are important to the maintainer.**

## 1. Product instructions are not product content

A recurring failure in prior sessions was copying instructions about how to build, maintain, research, or hand off ENA into ENA itself.

Owner analogy: if a teacher tells a student to keep the exam paper clean and think before writing, the student should not write "keep the paper clean" as part of the exam answer. The instruction should be visible in the quality of the work, not copied into the answer.

Therefore owner feedback such as "make the new ENA simple, clear, practical, grounded, and avoid unnecessary jargon" is primarily an instruction to the maintainer. The product should **be** clear and practical. It does not need to tell adopters that its authors were instructed to write clearly unless that statement independently changes adopter action.

## 2. Legacy ENA contains embedded contamination

The problem is deeper than misplaced project-management files.

Owner analogy: a coin inserted into a tree trunk can become wrapped by layer after layer of growth until it appears to be part of the tree. Likewise, session handoff, continuity, research orchestration, maintainer workflow, and project-management problems may have shaped legacy ENA terminology, distinctions, modules, and architecture.

Deep embedding is not evidence that a legacy concept intrinsically belongs to ENA.

Legacy ENA is therefore evidence/history/regression material, not the design skeleton of v0.4.

## 3. Clean derivation order

For the new product:

1. start from ENA's actual purpose;
2. start from real Agent problems and opportunities;
3. derive the useful behavior/capability needed for those problems;
4. build the smallest coherent product that delivers those capabilities;
5. only afterward compare with legacy ENA to detect meaningful omissions/regressions.

Do not begin by enumerating old terminology, old distinction families, old modules, or old Action Card candidates and deciding where to move them.

All genuinely useful capabilities should survive. Legacy representation, taxonomy, vocabulary, and file structure do not have to survive.

## 4. New repository boundary

`guytogay/ENA` now exists and is the clean product home for the next ENA.

It was intentionally started from an empty repository rather than copied from the legacy tree. Its first commit is only a minimal product/status README.

State:
- product home: `guytogay/ENA`
- next ENA: active development, not Current, not promoted
- legacy Current remains `v0.3.14 / FIELD_VALIDATION`
- legacy Current/history/research/evidence home remains `guytogay/evolution-native-agent-architecture`

Do not copy the old repository tree, handoffs, project-management files, research organization, or rebuild branch wholesale into `guytogay/ENA`.

## 5. Field Guide decision

`guytogay/ena-field-guide` no longer has a justified independent long-term product role.

The old split — ENA contains theory while Field Guide contains practical HOW — conflicts with the new product direction. A usable ENA should include the practical HOW necessary to use its capabilities rather than force the adopter into another repository.

Disposition:
- stop independent Field Guide evolution;
- preserve useful occurrences and evidence, including PR #6;
- re-evaluate useful HOW by real capability/value before bringing it into the new ENA;
- do not migrate Field Guide README/NOW/project-management structure into the new ENA;
- archive the Field Guide repository after unique useful material is safely preserved/referenced.

## 6. Other repository ownership

`guytogay/human-ai-workbench` owns reusable human-AI project-working method: continuation, handoff, coordination reduction, experiment-working practice, and related general methods.

Those methods may support ENA development without becoming ENA product doctrine.

Cleanroom repositories remain disposable experimental surfaces, not canonical ENA product or knowledge stores.

## 7. Cleanup directive

For the legacy architecture repository and related old surfaces:

- archive what has historical/evidence value but should not remain live/prominent;
- delete what no longer earns a live place and is safely recoverable from Git history;
- transfer reusable general methods to the repository that actually owns them;
- do not make the owner manually enumerate and clean every contaminated item.

Cleanup is semantic as well as structural. Moving files alone is not enough if old project/session concerns continue to determine the new ENA's concepts.

## 8. Non-negotiable successor behavior

A successor must not soften this into "make v0.4 shorter" or "rename legacy concepts more clearly."

The correction is stronger:

- build the product cleanly from real Agent needs;
- let simplicity/clarity/practicality show in the resulting product rather than writing maintainer reminders into it;
- do not invent ENA vocabulary unless an independently necessary concept truly earns it;
- do not recreate a separate HOW product if the HOW belongs naturally inside ENA;
- do not let handoff/project-management machinery become ENA again;
- use legacy material after derivation as evidence/regression checking, not before derivation as a blueprint.

If later work starts drifting back toward legacy taxonomy, jargon, multi-hop routing, project-management doctrine, or separate practical-product fragmentation merely because those structures already exist, stop and re-derive from the real Agent problem.

The owner explicitly requested that this consensus be **thoroughly carried forward in future work and future handoffs** so succession cannot silently reset the project direction.
