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

### 2026-09-10 clean working product shape

The first coherent working product shape is now present in `guytogay/ENA`. It remains a working draft and has **not** been live-tested, promoted, or made Current.

Current adopter path:

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

5. `EVOLUTION.md` — executable cumulative improvement.
   - preserve a candidate;
   - capture the smallest relevant real baseline before changing anything;
   - use ACMS for body-affecting trials;
   - distinguish survival of the mutation from evidence that the change actually improved anything;
   - compare post-change reality with baseline and `retain / revise / reject / restore`;
   - preserve successful and failed outcomes so later cycles inherit reality rather than rediscovering it.

Current example artifacts include:

- `ENA.example.yaml`
- `examples/BODY.example.yaml`
- `examples/acms/RESCUE.example.yaml`
- `examples/acms/STATUS.example.yaml`
- `examples/evolution/CANDIDATE.example.yaml`

Active Issues `#8`–`#11` have been updated to point at the current working design.

Owner direction for this point in the work: **finish the remaining working design first; do not start practical failure/evolution tests yet.**

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
- evolutionary-memory mechanism-discrimination campaign remains `CLOSED`.

## Immediate next action

`PRE_TEST_COMPLETENESS_AND_OMISSION_REVIEW_ONLY`

The working product path is now drafted end-to-end. Before any live failure, rescue, interoperability, or evolution test, perform a bounded completeness/consistency review of the new `guytogay/ENA` files and examples only. Look for missing practical dependencies, contradictions between First Use/A2A/Survival/ACMS/Evolution, and any remaining prose that does not directly help an adopter.

Do **not** start practical tests until the owner explicitly moves the project into that phase. Do not use the review as an excuse to reopen closed legacy research or re-import legacy architecture.
