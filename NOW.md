# ENA — NOW

This is live maintainer/project status. It is not ENA adopter/runtime content.

## Legacy Current

- repository: `guytogay/evolution-native-agent-architecture`
- `v0.3.14 / CURRENT / FIELD_VALIDATION`
- identity authority: `releases/current/CURRENT-BASELINE.yaml`
- effective package: `releases/current/`
- field stream: Issue `#208`

Do not mutate `releases/current/**` without successor identity.

## New ENA product home

Repository: `guytogay/ENA`

State: `ACTIVE_DEVELOPMENT / NOT_CURRENT / NOT_PROMOTED`

The repository was intentionally initialized from empty state and is the clean product home for the next ENA.

Do not copy the legacy repository tree, old handoffs, project-management machinery, research structure, legacy vocabulary/taxonomy, or the old rebuild branch wholesale into the new product repository.

### 2026-09-10 product-scope correction

The clean rebuild briefly started turning ordinary model reasoning into ENA product rules: how to notice bugs/feedback, how to weigh tradeoffs, when to continue, and how to judge changes.

Owner correction: **this is too much and is the wrong layer.** A capable model already has substantial judgment ability. ENA should primarily add capabilities the model/Agent does not possess merely by reasoning.

Therefore:

- `guytogay/ENA/CORE.md` was removed rather than allowed to grow into another reasoning framework;
- Issue `#7` was closed `not planned / out of product scope`;
- Issues `#1` and `#6` remain regression evidence that legacy ENA can suppress useful initiative or turn acknowledgement into a stopping point, but they do not justify a new ENA-specific reasoning layer;
- the clean product now focuses on concrete missing Agent infrastructure.

First active product work:

1. `guytogay/ENA` Issue `#10` — inspect the Agent's actual runtime, capabilities, critical operating components, communication paths, A2A, and recovery surfaces. Executable first-use guidance now lives in `FIRST-USE.md`.

2. `guytogay/ENA` Issue `#11` — establish a practical bidirectional A2A path when one does not already exist.

3. `guytogay/ENA` Issue `#8` — build survivable body-change/recovery around the current Host. The current minimum pattern is: preserve the old state, record the intended change and reversal, arm an independent 5–10 minute rollback, send the same recovery record to another Agent through A2A, then apply the change. Normal bidirectional communication after the change is enough to cancel the pending rollback; otherwise the rollback remains armed.

4. `guytogay/ENA` Issue `#9` — build an executable evolution system on top of that recovery foundation so useful self-improvements can be tried, observed, retained, revised, rejected, or rolled back.

### 2026-09-10 adopter-utility correction

While drafting `FIRST-USE.md`, the maintainer again copied owner explanation/correction language into the product, including a sentence explaining that memory loss is not Agent death. The owner correctly identified that this explanation had no concrete value for an adopter reading the first-use instructions and would be confusing out of conversational context.

Correction:

- owner explanations used to steer or correct the maintainer are maintainer/project context by default;
- a sentence belongs in ENA product text only when it independently gives the adopter a concrete capability, action, constraint, recovery path, or necessary understanding for use;
- if removing a sentence does not reduce the adopter's ability to use ENA correctly, prefer removing it;
- rationale about why the maintainer rejected another design belongs in project history/handoff, not in adopter instructions;
- `README.md`, `FIRST-USE.md`, and active Issue `#8`–`#11` bodies were cleaned to remove owner/meta/reasoning-boundary commentary from active product-facing text. Historical comments remain as project evidence, not runtime guidance.

A useful maintainer check before adding product prose is: **what specific action or capability does this sentence enable for the adopter?** If there is no concrete answer, do not put it in the product merely because it was useful in the design conversation.

This check is a maintainer discipline. Do not copy the check itself into ENA adopter/runtime content unless it independently becomes necessary there.

## Mandatory owner consensus

The owner identified **product/project boundary contamination** as a core legacy problem.

Prior sessions sometimes copied instructions about how to maintain, research, hand off, or write ENA into ENA itself. Some of this may also have become embedded in legacy concepts and architecture.

Two owner analogies define the correction:

- exam paper: instructions such as "keep the paper clean" should improve the work, not be written as part of the answer;
- tree/coin: a foreign object can become deeply wrapped by later growth; deep embedding does not prove it intrinsically belongs to ENA.

The 2026-09-10 corrections extend this boundary:

- ordinary capable-model reasoning is not automatically an ENA product gap;
- do not rebuild generic judgment, tradeoff analysis, feedback handling or bug reasoning as ENA machinery merely because those behaviors matter;
- prefer concrete missing capabilities, durable mechanisms and executable systems that materially extend what the Agent can actually do;
- do not copy explanatory language from owner/maintainer design conversations into product text unless it independently helps an adopter use the product.

Legacy ENA remains evidence/regression history, not the next product blueprint.

Mandatory deep-succession record remains:

`research/handoffs/records/2026-09-07-v040-clean-product-home/`

A deep successor must read `CONSENSUS-LOCK.md` before designing the new ENA, then apply the newer live corrections from `NOW.md` and `CURRENT-HANDOFF.yaml`.

## Repository roles

### `guytogay/ENA`
New ENA product home.

### `guytogay/evolution-native-agent-architecture`
Legacy v0.3.14 Current + research + experiments + evidence + history + provenance + maintainer succession.

### `guytogay/human-ai-workbench`
Canonical general human-AI project-working method. Handoff, continuation, coordination reduction, and similar general methods belong there rather than in the ENA product by default.

### `guytogay/ena-field-guide`
Disposition: `SUNSET_AS_INDEPENDENT_PRODUCT / PRESERVE_USEFUL_EVIDENCE_THEN_ARCHIVE`.

PR #6 remains useful evidence for bounded self-maintenance (`snapshot + canary + ledger + restore drill`) and may now be consulted only after the clean survival need has independently earned attention. Do not migrate the old Field Guide structure.

## Active legacy occurrences

- Issue `#208` — Current field validation umbrella; includes F-208-17 forward-progress evidence.
- Issue `#222` — design occurrence; re-evaluate only through clean-product lens.
- PR `#224` — contribution occurrence showing actionability/prose-rent problem; do not merge paragraph-scale rewrite into v0.3.14.
- Issue `#234` — practicality/prose-rent evidence.
- evolutionary-memory mechanism-discrimination campaign remains `CLOSED`.

## Immediate next action

`DESIGN_ACMS_V01_PROTECTED_BODY_CHANGE_PATH_THEN_EXECUTABLE_EVOLUTION_SYSTEM`

Use `FIRST-USE.md`, Issue #10 and Issue #11 as prerequisites. Design the smallest real ACMS-style protected change path for the current Host pattern: preserve old state, record the exact change/reversal, arm independent timed rollback, share the recovery record through A2A before mutation, apply the change, and cancel rollback only after a normal external conversation confirms a rescue channel still exists.

Then use that recovery base to support Issue #9: safe cumulative evolution. Keep adopter-facing text free of maintainer-only rationale.