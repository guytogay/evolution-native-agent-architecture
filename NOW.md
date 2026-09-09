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

### 2026-09-10 adopter-utility correction

While drafting `FIRST-USE.md`, the maintainer again copied owner explanation/correction language into the product. The owner correctly identified that explanation used to steer the maintainer is not automatically useful to an adopter.

Correction:

- owner explanations used to steer or correct the maintainer are maintainer/project context by default;
- a sentence belongs in ENA product text only when it independently gives the adopter a concrete capability, action, constraint, recovery path, or necessary understanding for use;
- if removing a sentence does not reduce the adopter's ability to use ENA correctly, prefer removing it;
- rationale about why the maintainer rejected another design belongs in project history/handoff, not in adopter instructions.

This check is a maintainer discipline. Do not copy the check itself into ENA adopter/runtime content unless it independently becomes necessary there.

### 2026-09-10 current clean-product foundation

The clean product currently has a coherent **foundation**, but the overall design is not yet complete because the evolution subsystem was initially narrowed too early.

Current adopter-facing foundation:

1. `FIRST-USE.md` — inspect the actual Agent/Host and normalize shared operating conventions.
   - user confirms canonical timezone, canonical language, and ENA home;
   - default timezone suggestion is `Asia/Shanghai`, but adopters may choose another IANA timezone;
   - Host clock synchronization is checked because timed rollback requires trustworthy time;
   - ENA-owned text records use UTF-8;
   - First Use leaves `ENA.yaml` for stable configuration/pointers and `BODY.yaml` for grounded body/recovery inspection results.

2. `A2A.md` — establish or reuse practical bidirectional Agent-to-Agent reach.
   - reuse the A2A Agent Card/discovery mechanism rather than inventing a parallel ENA identity;
   - verify a real two-way exchange;
   - retain at least one usable rescue peer;
   - ACMS rescue material must be acknowledged for the exact change package before mutation.

3. `SURVIVAL.md` — build an external survivable runtime path.
   - external start/restart mechanism;
   - simple reachability/communication check;
   - recovery ladder: probe again → restart → verify → restore relevant known-good state → verify → A2A/human escalation;
   - recovery controls should remain outside the failure surface of the Agent being protected.

4. `ACMS.md` — protected body-change path.
   - one second-precise change package per protected change, named in canonical timezone with actual UTC offset;
   - package includes `rescue.yaml`, `change.md`, `status.yaml`, known-good backup/restore material, and executable/Host-native rollback;
   - package must survive failure of the changed component;
   - lifecycle: `preparing → armed → applied → retained` or `restoring → restored/failed`, with `cancelled` before mutation;
   - independent 5–10 minute rollback is armed before mutation;
   - rescue peer receives and acknowledges executable recovery information before mutation;
   - rollback should be idempotent or protected against timer/rescue-peer races;
   - where practical, normal critical self-change should be technically routed through ACMS rather than relying on remembered checklist behavior.

5. `EVOLUTION.md` — **still under active design**.
   - the first draft captured candidate → baseline → ACMS trial → observation → `retain / revise / reject / restore`;
   - owner correction: this is only the reality-selection/execution portion and does not by itself constitute an evolution system;
   - evolution must also include memory consolidation that improves the Agent's durable memory/adaptive substrate, and dream-like recombination that creates new associations/variation from accumulated experience;
   - `EVOLUTION.md` has been expanded to the current working shape: experience/memory → consolidation → dreaming/recombination → candidate → reality contact/selection → feed result back into memory.

### Recovered legacy evolution evidence relevant to the clean design

Legacy ENA is being consulted here as evidence and prior work, not as the new product blueprint.

Relevant preserved material includes:

- `releases/current/09-EVOLUTION-METABOLISM.md` — retains the general metabolism `stimulus → variation → reality contact → local selection → retention/dormancy/loss → migration/recombination → renewed variation`;
- `research/evolution-inbox/EVOLUTIONARY-MEMORY-PRESERVED-ADAPTATION.md` — distinguishes preserved information from preserved adaptation and treats memory as what experience changes about future behavior;
- `research/evolution-inbox/MEMORY-ECOLOGY-SLEEP-DREAMING-AND-ADAPTIVE-CONSOLIDATION.md` — preserves the earlier `ai-dreaming` lineage, sleep-like offline consolidation, associative memory, dream-like recombination, and the boundary that generated dream material is variation rather than factual evidence;
- `research/evolution-inbox/EVOLUTIONARY-MEMORY-CLOSURE-DISPOSITIONS.yaml` — closed the old mechanism-discrimination campaign without rejecting these functions: sleep-like consolidation was subsumed under memory/metamemory/local selection; dream-like recombination was subsumed as a variation-generation implementation family whose invocation policy remained field-unresolved.

Do not mechanically recreate the old ontology, experiments, or research terminology in the clean product. Extract only practical capabilities that independently earn adopter utility.

Current example artifacts include:

- `ENA.example.yaml`
- `examples/BODY.example.yaml`
- `examples/acms/RESCUE.example.yaml`
- `examples/acms/STATUS.example.yaml`
- `examples/evolution/CANDIDATE.example.yaml`

Active Issues `#8`–`#11` point at the current working product needs. Project-phase/testing commentary was removed from those issue bodies because it does not belong in adopter/product requirements.

Owner phase direction belongs here in project status, not in product instructions: continue the remaining design before moving to practical failure/evolution testing.

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

PR #6 remains useful evidence for bounded self-maintenance (`snapshot + canary + ledger + restore drill`) and may be consulted only after the clean need has independently earned attention. Do not migrate the old Field Guide structure.

## Active legacy occurrences

- Issue `#208` — Current field validation umbrella; includes F-208-17 forward-progress evidence.
- Issue `#222` — design occurrence; re-evaluate only through clean-product lens.
- PR `#224` — contribution occurrence showing actionability/prose-rent problem; do not merge paragraph-scale rewrite into v0.3.14.
- Issue `#234` — practicality/prose-rent evidence.
- evolutionary-memory mechanism-discrimination campaign remains `CLOSED`; consult its preserved results without reopening it merely because the clean product now needs an evolution implementation.

## Immediate next action

`CONTINUE_CLEAN_EVOLUTION_DESIGN_FROM_MEMORY_CONSOLIDATION_DREAMING_AND_REALITY_SELECTION`

Continue the clean evolution design with the owner before practical testing. Use the recovered legacy evolution material as prior evidence/omission checking only. Work out the smallest useful mechanisms by which an Agent can:

1. consolidate/organize its own durable memory so accumulated experience improves future competence;
2. perform dream-like recombination that creates genuinely new candidate associations/variations without treating generated material as fact;
3. route selected candidates through reality contact and ACMS where body-affecting change is involved;
4. feed positive and negative outcomes back into future memory/consolidation/dreaming cycles.

Do not treat the first candidate-selection draft as a completed evolution system, and do not move to practical testing until the owner moves the phase.
