# Owner Direction Correction — Product vs Project Contamination

Status: `MUST_READ_FOR_V040_SUCCESSION / PROJECT_DIRECTION_NOT_ENA_PRODUCT`
Date: 2026-09-07

This file records an owner correction to how ENA v0.4 must be rebuilt. It is **project-maintainer context**, not material to copy into ENA's adopter/runtime product.

## The correction

The owner identified that prior sessions repeatedly failed to distinguish between:

1. instructions about **how the maintainer/session should work on ENA**; and
2. content that **ENA itself should teach or expose to an adopter/Agent**.

The owner gave the analogy: if a teacher tells a student to keep the exam paper clean and think before writing, the student should not write "keep the exam paper clean" as part of the answer. The instruction should be internalized in the work, not copied into the product.

A concrete example from this session: the owner said the new ENA should be simple, clear, practical, grounded, and should not invent unnecessary vocabulary. The session initially wrote those instructions directly into ENA rebuild content. The owner rejected that move. If the resulting ENA is actually clear and ordinary-language, there is no need for the ENA product to tell its user that the authors were instructed to write it clearly.

## Deeper diagnosis: boundary contamination

The problem is not limited to a few misplaced files or phrases.

The owner believes substantial material unrelated to ENA itself has accumulated inside the repository and, in some cases, has become structurally embedded in ENA's concepts and architecture.

Owner analogy:

> It is like inserting a coin into a tree trunk. As the tree grows, the trunk wraps around the coin layer by layer until the coin and trunk cannot be separated cleanly.

This means some concepts, terminology, workflows, and distinctions in legacy ENA may have been shaped by project/session-management problems rather than by the intrinsic needs of an evolution-native Agent architecture.

Known contamination sources include, but are not limited to:

- session handoff and takeover problems;
- instructions given by the owner to prior ChatGPT sessions about how to prepare handover;
- project-management and continuity practices;
- repeated attempts to preserve session context;
- research orchestration and cleanroom logistics;
- maintainer workflow rules;
- anti-complexity instructions intended for ENA authors rather than ENA adopters.

Some of these methods may be useful in their own right and may belong in `human-ai-workbench`, project-internal history, or research evidence. Their usefulness does **not** make them ENA product content.

## Mandatory product/project boundary

Default interpretation of owner feedback about how to build ENA:

> It is a maintainer instruction unless there is independent reason that an ENA adopter/Agent needs the same content to act better.

Do not promote a good project-working rule into ENA merely because it helped the ENA maintainer.

Do not turn process corrections into product doctrine.

Do not turn handoff mechanics into evolution architecture without independent justification.

Do not preserve a concept merely because ENA has already grown around it.

## Consequence for v0.4 derivation

Legacy ENA is no longer a primary design source for v0.4.

Treat v0.3.x primarily as:

- historical evidence;
- falsification/incident record;
- regression oracle;
- source of possibly valuable capabilities that must be independently re-justified.

Do **not** use legacy terminology, module boundaries, distinction lists, Action Card families, file layout, or conceptual taxonomy as the skeleton of v0.4.

Correct derivation order:

1. start from ENA's actual purpose;
2. start from real Agent problems and opportunities;
3. derive the minimum useful behavior/capability from those problems;
4. build the clean product from that derivation;
5. only afterward compare against legacy ENA to detect genuinely important omissions or regressions.

Wrong derivation order:

1. enumerate old ENA concepts;
2. decide where each old concept should go;
3. rename/compress/repackage them;
4. call the result v0.4.

The existing `LEGACY-SEMANTIC-COVERAGE.md` is therefore a **secondary regression/coverage aid**, not a v0.4 product blueprint.

Likewise, previously named families such as `EVIDENCE/SUPPORT`, `EFFECT LIFECYCLE`, `RECOVERY/RESUME`, `ADAPTATION IMPORT`, and `COMPOSITION` may point to real capabilities worth preserving, but their old names/boundaries do not automatically earn five modules, five cards, or even five separate concepts in v0.4.

All genuinely necessary capabilities should be covered. Legacy conceptual structure does not need to survive.

## Repository cleanup direction

The owner explicitly directed:

- archive what should be archive;
- delete what should be deleted;
- transfer what belongs elsewhere;
- do not expect the owner to manually identify and clean every contaminated item.

The cleanup target is not only fewer files. The target is a clear boundary between:

- ENA product;
- ENA project-maintainer machinery;
- research/evidence/history;
- reusable general human-AI work methods owned elsewhere.

A user who receives the ENA repository link should be able to see the actual ENA product and purpose without first navigating session succession, branch governance, research orchestration, cleanroom mechanics, or maintainer history.

## Clean-repository option

The owner explicitly offered to create a new repository if necessary.

A clean v0.4 product repository is therefore an allowed and likely preferable migration path if it avoids carrying structural contamination forward.

Potential architecture:

- old `evolution-native-agent-architecture` repo remains the historical/research/legacy source and v0.3.x occurrence store;
- a clean repository becomes the v0.4 product home;
- only independently justified ENA capabilities are carried into the clean product;
- provenance can point back to old evidence without copying old project-management machinery.

Do not treat creation of the new repository as completed until it actually exists.

## Immediate correction to current work

Pause mechanical continuation of the five legacy-family Action Card derivation.

First establish a clean product boundary and perform clean re-derivation from purpose + real Agent problems. Use legacy coverage only afterward as a regression check.

## Non-negotiable succession requirement

A successor session must not lose or soften this correction.

If later work starts to use old ENA terminology, handoff machinery, project-management lessons, or maintainer instructions as v0.4 product structure merely because they already exist, stop and re-derive from the real Agent problem.
