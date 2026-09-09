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

1. `guytogay/ENA` Issue `#8` — **Help an Agent build a survivable runtime around itself**.
   - inspect the current Host;
   - use Host-native mechanisms where suitable;
   - make interruption, restart, bad self-change and recovery less destructive;
   - prove recovery actually works rather than merely claiming backup exists.

2. `guytogay/ENA` Issue `#9` — **Help an Agent build an executable evolution system**.
   - preserve candidate improvements;
   - make bounded changes without destroying known-good state;
   - test against reality;
   - keep, revise, reject or roll back changes;
   - carry useful improvement across sessions/restarts.

The user summarized the intended level concretely: ENA should be able to guide a model to build an "不死的框架" around the current Agent and to build an actual evolution system around it.

## Mandatory owner consensus

The owner identified **product/project boundary contamination** as a core legacy problem.

Prior sessions sometimes copied instructions about how to maintain, research, hand off, or write ENA into ENA itself. Some of this may also have become embedded in legacy concepts and architecture.

Two owner analogies define the correction:

- exam paper: instructions such as "keep the paper clean" should improve the work, not be written as part of the answer;
- tree/coin: a foreign object can become deeply wrapped by later growth; deep embedding does not prove it intrinsically belongs to ENA.

The 2026-09-10 correction extends this boundary:

- ordinary capable-model reasoning is not automatically an ENA product gap;
- do not rebuild generic judgment, tradeoff analysis, feedback handling or bug reasoning as ENA machinery merely because those behaviors matter;
- prefer concrete missing capabilities, durable mechanisms and executable systems that materially extend what the Agent can actually do.

Legacy ENA remains evidence/regression history, not the next product blueprint.

Mandatory deep-succession record remains:

`research/handoffs/records/2026-09-07-v040-clean-product-home/`

A deep successor must read `CONSENSUS-LOCK.md` before designing the new ENA, then apply this newer live correction from `NOW.md` and `CURRENT-HANDOFF.yaml`.

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

`DESIGN_SURVIVABLE_AGENT_RUNTIME_THEN_EXECUTABLE_EVOLUTION_SYSTEM`

Start from Issue #8 as the first concrete capability. Derive the smallest Host-adaptive survivability/recovery guidance that gives an Agent something it does not already have through model reasoning alone. Use Field Guide PR #6 and legacy recovery evidence only afterward as regression/omission checks.

Then use that recovery base to support Issue #9: safe cumulative evolution. Do not add generic reasoning rules unless a real missing capability cannot be supplied without them.
