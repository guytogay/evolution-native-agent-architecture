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

The repository now exists, is public, and was intentionally initialized from empty state with only a minimal README. It is the clean product home for the next ENA.

Do not copy the legacy repository tree, old handoffs, project-management machinery, research structure, legacy vocabulary/taxonomy, or the old rebuild branch wholesale into the new product repository.

## Mandatory owner consensus

The owner identified **product/project boundary contamination** as a core legacy problem.

Prior sessions sometimes copied instructions about how to maintain, research, hand off, or write ENA into ENA itself. Some of this may also have become embedded in legacy concepts and architecture.

Two owner analogies define the correction:

- exam paper: instructions such as "keep the paper clean" should improve the work, not be written as part of the answer;
- tree/coin: a foreign object can become deeply wrapped by later growth; deep embedding does not prove it intrinsically belongs to ENA.

Therefore:

- maintainer/build instructions are not ENA product content by default;
- desired qualities such as clear/practical/grounded writing should be demonstrated by the product rather than turned into product meta-doctrine;
- legacy ENA is not the next product blueprint;
- derive the new product from ENA purpose + real Agent problems first;
- consult legacy ENA afterward for meaningful omissions/regressions and costly lessons.

Mandatory deep-succession record:

`research/handoffs/records/2026-09-07-v040-clean-product-home/`

A deep successor must read `CONSENSUS-LOCK.md` before designing the new ENA.

## Repository roles

### `guytogay/ENA`
New ENA product home.

### `guytogay/evolution-native-agent-architecture`
Legacy v0.3.14 Current + research + experiments + evidence + history + provenance + maintainer succession.

### `guytogay/human-ai-workbench`
Canonical general human-AI project-working method. Handoff, continuation, coordination reduction, and similar general methods belong there rather than in the ENA product by default.

### `guytogay/ena-field-guide`
Disposition: `SUNSET_AS_INDEPENDENT_PRODUCT / PRESERVE_USEFUL_EVIDENCE_THEN_ARCHIVE`.

The old theory-vs-practical-HOW split is no longer desired. Practical HOW necessary to use ENA should live naturally in the ENA product rather than require a second product repository.

PR #6 remains a useful candidate/evidence occurrence. Re-evaluate its demonstrated capability value before bringing anything into the new ENA. Do not migrate Field Guide README/NOW/product-boundary structure.

## Cleanup already completed in legacy repo

- legacy coverage ledger moved out of active rebuild root into archive;
- historical repository-adoption record moved under `research/history/`;
- obsolete root `PROJECT-HUB.md`, `PROJECT-STRUCTURE.md`, and `PROJECT-ECOSYSTEM.md` removed;
- legacy collaboration entry demoted;
- root README shortened to product/adoption routing;
- `PROJECT-METADATA.yaml` minimized and retained only because v0.3.14 Current CI still reads it.

Continue archive/delete/transfer by actual role. Do not preserve live clutter merely because it has history; Git already preserves history.

## Active legacy occurrences

- Issue `#208` — Current field validation umbrella.
- Issue `#222` — design occurrence; re-evaluate only through clean-product lens.
- PR `#224` — contribution occurrence showing actionability/prose-rent problem; do not merge paragraph-scale rewrite into v0.3.14.
- Issue `#234` — practicality/prose-rent evidence.
- evolutionary-memory mechanism-discrimination campaign remains `CLOSED`.

## Immediate next action

`REDERIVE_MINIMUM_ENA_PRODUCT_IN_GUYTOGAY_ENA_FROM_REAL_AGENT_PROBLEMS`

Start with real Agent problems/opportunities in the clean product repository. Do not mechanically continue legacy Action Card families and do not recreate a separate Field Guide product.
