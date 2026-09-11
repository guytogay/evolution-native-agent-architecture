# ENA — NOW

This is maintainer/project status, not adopter/runtime content.

## Legacy Current

- repository: `guytogay/evolution-native-agent-architecture`
- `v0.3.14 / CURRENT / FIELD_VALIDATION`
- identity authority: `releases/current/CURRENT-BASELINE.yaml`
- effective package: `releases/current/`
- field stream: Issue `#208`

Do not mutate `releases/current/**` without successor identity.

## Clean product home

Repository: `guytogay/ENA`

State: `ACTIVE_DEVELOPMENT / NOT_CURRENT / NOT_PROMOTED`

Latest adopter-facing cleanup merged to `main` at:

`c45767d23b3aeeb086a1bb1104fddaed68518d55`

The product repo is intentionally independent of legacy handoff/research/project-management structure.

### Current direct use path

```text
FIRST-USE.md
→ A2A.md
→ SURVIVAL.md
→ SAFE-CHANGE.md
→ EVOLUTION.md
→ SLEEP-DREAM-QUICKSTART.md
```

Key outputs/mechanisms:

- `ENA.yaml` — confirmed timezone, language, home and stable pointers;
- `SYSTEM.yaml` — verified runtime/capability/communication/memory/recovery facts;
- A2A — reuse real Agent Card/discovery and keep a usable rescue peer;
- Survival — external restart/recovery path outside the main Agent process;
- Safe Change — preserve previous working state, prepare rollback, arm independent recovery and share `rescue.yaml` before important self-change;
- Evolution — candidate → baseline → reality → retain/revise/reject/restore → outcome back to experience;
- Sleep — reversible memory consolidation rather than summary generation;
- Dream — biased-random distant-memory recombination; generated material remains speculative until reality contact.

### 2026-09-12 adopter cleanup

Owner requested a final test: could a fresh Agent open `guytogay/ENA` and act without first learning internal project vocabulary or maintainer history?

Correction implemented:

- removed adopter-facing `ACMS` terminology; product file is now `SAFE-CHANGE.md`;
- removed the `BODY.yaml` metaphor; runtime map is now `SYSTEM.yaml`;
- removed branded `Divergent Explorer` wording; Dream describes direct divergent-exploration actions;
- removed repeated `working draft / not Current`, legacy release and maintainer-process prose from product files;
- shortened the major product instructions substantially rather than adding another explanatory layer;
- active Issues #8–#11 were aligned with the direct terminology.

Default-branch code search after merge returned no product-file matches for:

```text
ACMS
BODY.yaml
Divergent Explorer
working draft
not Current
legacy
owner
```

### Runnable reference tools

`guytogay/ENA/tools/` now includes standard-library Python examples:

```text
ena_init.py         create ENA.yaml, SYSTEM.yaml and working directories
change_scaffold.py  create a timestamped safe-change package skeleton
sleep_prepare.py    prepare a bounded Sleep input bundle
dream_sample.py     sample free/problem-guided Dream material with biased randomness/distance
self_test.py        smoke-test the included reference tools and sample data
```

Included JSONL examples let another Agent run Sleep/Dream preparation immediately.

PR #13 reference-tool CI passed before merge. The tools were also locally smoke-tested during authoring.

These tools are reference implementations, not a replacement for stronger Host-native snapshots, schedulers, memory systems or A2A mechanisms.

## Sleep / Dream v0.1 field use

Bounded field use is now desired.

Sleep:

```text
experience
→ consolidation plan
→ reversible pre-write state
→ memory update
→ verification / restore on failed verification
```

Dream:

```text
recent + old + underused + external/unresolved + distant + occasional random memory
→ delay convergence
→ remote structural connection / hybridization / inversion / cross-domain transfer / counterfactual
→ speculative candidates
→ normal reasoning + reality contact
```

`dream_sample.py` supports both `free` and `problem-guided` modes and uses vector middle-distance sampling when embeddings are supplied; otherwise it falls back to domain/source distance.

Collect concrete observations in `guytogay/ENA` Issue #12, including negative/null results.

## Product boundary

Still binding:

- ordinary capable-model reasoning is not automatically an ENA product gap;
- prefer concrete missing capabilities, durable mechanisms and executable systems;
- owner/maintainer explanations are project context unless they independently help an adopter act;
- legacy ENA is evidence/regression/omission-checking material, not the new product blueprint;
- do not re-import legacy structure, terminology, handoff machinery or closed research merely because it exists.

Mandatory deep-succession record remains:

`research/handoffs/records/2026-09-07-v040-clean-product-home/`

A deep successor reads `CONSENSUS-LOCK.md`, then applies the newer live state from this file and `CURRENT-HANDOFF.yaml`.

## Repository roles

- `guytogay/ENA` — clean product home.
- `guytogay/evolution-native-agent-architecture` — legacy Current + research/evidence/history + maintainer succession.
- `guytogay/human-ai-workbench` — general human-AI project-working method.
- `guytogay/ena-field-guide` — `SUNSET_AS_INDEPENDENT_PRODUCT / PRESERVE_USEFUL_EVIDENCE_THEN_ARCHIVE`.

Active legacy occurrences remain #208, #222, PR #224 and #234. Evolutionary-memory mechanism-discrimination remains `CLOSED`.

## Immediate next action

`FIELD_TRY_CLEAN_ENA_AND_SLEEP_DREAM_V01`

Give `https://github.com/guytogay/ENA` directly to fresh Agents/Hosts. Ask them to start from README/FIRST-USE rather than giving project history. Observe whether they can:

1. initialize/inspect themselves;
2. establish/reuse A2A and recovery;
3. prepare a safe self-change package;
4. run Sleep/Dream preparation;
5. produce useful candidates and bring them back to reality;
6. report confusion, missing dependencies, noise, cost and negative/null results.

Do not promote from novelty alone. Improve from actual adopter/Host evidence.
