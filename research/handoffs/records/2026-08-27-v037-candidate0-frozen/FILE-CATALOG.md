# ENA Handoff — File Catalog and Takeover Map

Status: `HANDOFF_FILE_CATALOG / CLASSIFIED_PROJECT_MAP / NOT_AUTHORITY_BY_ITSELF`

Handoff ID: `2026-08-27-v037-candidate0-frozen`

This catalog is optimized for a fresh project-manager session. It distinguishes authority, bootstrap projections, research methods, plans, candidate lineage, evidence, and optional deep detail.

## A. Project entry and authority

### `PROJECT-HUB.md`

Role: stable top-level project entrypoint.

Read when: always, first.

Authority class: `PROJECT_ROUTING_AUTHORITY`.

### `releases/current/CURRENT-BASELINE.yaml`

Role: singular adopter-facing Current identity and machine-readable release status.

Observed handoff state: `v0.3.6 / CURRENT / FIELD_VALIDATION`.

Authority class: `CURRENT_IDENTITY_AUTHORITY`.

Do not infer Current from candidate/release/history directories.

### `research/ACTIVE-RESEARCH.yaml`

Role: main-visible pointer to the one active research integration branch and current research/release phase.

Authority class: `RESEARCH_ROUTING_AUTHORITY`.

Live branch heads must still be reverified before writing.

---

## B. Standardized session handoff system

### `research/methodology/SESSION-HANDOFF-DISCIPLINE.md`

Role: canonical method for outgoing and incoming project-manager/session handoff.

Authority class: `CANONICAL_RESEARCH_METHOD`.

Read when: every planned session rotation or context-instability handoff.

### `research/handoffs/README.md`

Role: explains handoff directory structure and authority boundary.

Authority class: `DIRECTORY_GUIDE`.

### `research/handoffs/CURRENT-HANDOFF.yaml`

Role: stable pointer to the latest intended handoff package.

Authority class: `HANDOFF_ROUTING_POINTER`.

Do not infer the active handoff from timestamps or directory names.

### `research/handoffs/2026-08-27-v037-candidate0-frozen/`

Role: current session handoff package.

Files:

```text
HANDOFF-START-HERE.md
PROJECT-STATE.md
RECENT-THREE-ROUNDS.md
FILE-CATALOG.md
PROJECT-MANAGEMENT-LESSONS.md
HANDOFF-MANIFEST.yaml
```

Authority class: `BOOTSTRAP_PROJECTION / CONTINUITY_AID`.

If this package conflicts with canonical state, canonical state wins and the package/control plane must be repaired.

---

## C. Canonical research methodology

Directory:

`research/methodology/`

Recommended read order for a new project-manager:

1. `README.md` — methodology index/read order.
2. `ENA-RESEARCH-DISCIPLINE.md` — open-cardinality master method ledger.
3. `SESSION-HANDOFF-DISCIPLINE.md` — standardized session succession.
4. `CONVERGENCE-DIVERGENCE-DISCIPLINE.md` — when to compress vs expand/preserve variation.
5. `PROJECT-STATE-ALIGNMENT-GATE.md` — repair current-state drift after material transitions.
6. `METHOD-CHANGELOG.md` — why method changed.
7. `incidents/` — concrete method failures/lessons.

Key current principles include:

```text
PROPERTY != ORGAN != HOST_BINDING != EVIDENCE != ADOPTION
ONE_WHAT_WHY -> 0..N_CONCRETE_HOW_BRANCHES
COMPRESS REPRESENTATION != COMPRESS POSSIBILITY SPACE
PROVEN_BEHAVIORAL_EQUIVALENCE -> MAY_COMPRESS
UNPROVEN_EQUIVALENCE -> DO_NOT_COLLAPSE
EXPERIMENTS_MUST_PAY_EPISTEMIC_RENT
MATERIAL_TRANSITION -> ALIGN -> RESUME
```

---

## D. Project plan and fast-moving progress

### `research/plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md`

Role: long-horizon phase model from reconstruction through release/promotion.

Authority class: `MASTER_PLAN`.

Use for: why phases exist, phase transition criteria, release discipline.

### `research/plans/PROGRESS.yaml`

Role: fast-moving current execution projection.

Authority class: `CURRENT_EXECUTION_PROJECTION` after alignment.

Use for: current phase, exact next actions, selected/deferred work, candidate/release state.

### `research/RESEARCH-START-HERE.md`

Role: active-branch hot bootstrap for research continuation.

Use for: how to continue work after main routes you to the active research branch.

---

## E. Operational Architecture and release-scope research

### `research/operational-architecture/`

Role: research-stage map from ordinary problem/WHAT-WHY into plural concrete HOWs.

Important surfaces include:

- `README.md` — architecture entry;
- `CUE-INDEX.md` — symptom/problem-to-node routing;
- `OPERATIONAL-ARCHITECTURE-MAP.md` — graph of operational nodes/HOW branches;
- `REFERENCE-POINTER-MATRIX.md` — exact paths to prototypes/procedures/Host mechanisms;
- bounded procedures and patterns linked from the map.

### `research/release-scope/`

Role: evidence and decisions that stabilized the v0.3.7 candidate cargo.

Important files:

- `README.md`
- `RELEASE-SCOPE-ENTRY-GATE-001.md`
- `RELEASE-SCOPE-STABILITY-GATE-001.md`
- `VERSION-SELECTION-001.md`
- `CANDIDATE-SURFACE-DESIGN-001.md`
- `REFERENCE-LIBRARY-SELECTION-001.md`
- `RELEASE-TOOLING-RECONCILIATION-001.md`
- `LANGUAGE-SCOPE-001.md`
- `ANTI-ABLATION-SELECTION-AUDIT-001.md`

Use when: questioning why something is/is not bundled into candidate.0.

---

## F. Frozen v0.3.7 candidate.0

Candidate branch:

`candidate/v0.3.7-candidate.0`

Frozen candidate subtree path:

`releases/v0.3.7-candidate/`

Frozen identity is **not** the current branch head.

Exact identity:

```text
source commit = d0e793593184740d9732902e948afd48ed96ae2f
candidate subtree = cffbf76fe1448b020b637c78d1f7ae46e4c0115b
```

### External freeze record

`collaboration/reconciliation/2026-08-27-v037-candidate0-freeze.md`

Role: authoritative frozen source/tree binding and author-side validation lineage.

Authority class: `FROZEN_CANDIDATE_IDENTITY_AUTHORITY`.

### Author attack record

`collaboration/reconciliation/2026-08-27-v037-candidate0-author-attacks.md`

Role: author-side defects, oracle false positives, repairs, and final pre-freeze attack record.

Authority class: `AUTHOR_EVIDENCE / NOT_INDEPENDENT_VERDICT`.

### Independent falsification handoff

`collaboration/reconciliation/2026-08-27-v037-candidate0-independent-falsification-handoff.md`

Role: fixed instructions for a fresh independent validator.

Authority class: `VALIDATION_HANDOFF / NOT_VERDICT`.

Important: before using it to start independent validation, first complete the newer 1080 -> 188 anti-ablation audit required by this session handoff.

---

## G. Research prototypes and evidence

### `research/prototypes/`

Role: concrete machine/procedure HOW experiments and composition harnesses.

High-value current lineage includes:

- memory metabolism / Retrieval Obligation;
- commitment-settlement recovered reconstruction;
- migration-settlement composition;
- progressive evolution-record envelope;
- lineage compaction contract;
- compaction × retrieval composition;
- execution-surface fencing;
- minimal v2 evolution helper.

These are not automatically Current or required organs.

### `research/external-how/`

Role: external mechanism harvests and source registry.

Use when a concrete HOW gap remains and fresh external engineering evidence can expand the possibility space.

### `research/reconstruction/`

Role: anti-ablation maps, recovered variation, lineage-survival analysis, architecture reconstruction.

Use when checking whether a HOW/problem was omitted, simplified, deferred, or recovered.

---

## H. Issue-level workstream lineage

Master reconstruction ledger:

`#89`

Organizational workstream shelves:

```text
#90 Memory / Runtime / Retrieval
#91 Authority / Effects / Recovery / Settlement
#92 Identity / Lineage / Standing / Reputation
#93 Ecology / Coordination / Resource / Evolution
#94 Evidence / Applicability / Adoption / Language / Release / Tooling
```

These issue groups are organizational shelves, not a natural ENA ontology.

Archaeology continuation tracker:

`#104`

Historical accidental placeholders:

`#105–#108` are explicitly closed accidental placeholders and carry no ENA research meaning.

---

## I. Branch and repository governance

### `research/BRANCH-GOVERNANCE.md`

Role: branch naming, lifecycle, candidate/research authority boundaries.

### `research/BRANCH-INVENTORY.yaml`

Role: live/historical branch inventory and cleanup lineage.

Key rule:

```text
ACTIVE_RESEARCH_AUTHORITY = MAIN_VISIBLE_BRANCH_POINTER
CANDIDATE_BRANCH != FROZEN_IDENTITY
```

---

## J. Recommended reading by takeover task

### If you only need to continue the next planned action

Read:

1. `PROJECT-HUB.md`
2. `CURRENT-BASELINE.yaml`
3. `CURRENT-HANDOFF.yaml`
4. current `HANDOFF-START-HERE.md`
5. current `HANDOFF-MANIFEST.yaml`
6. current `PROJECT-STATE.md`
7. convergence/divergence method
8. Progress
9. freeze record
10. then execute the 1080 -> 188 anti-ablation audit.

### If you must question candidate cargo

Add:

- `research/release-scope/`
- `research/operational-architecture/`
- relevant prototypes/reconstruction files.

### If you must question methodology

Add:

- full `research/methodology/`
- relevant `research/methodology/incidents/`.

### If independent validation begins

Add:

- exact frozen candidate bytes at the frozen source/tree;
- independent falsification handoff;
- do Phase A before relying on author oracles.

### If candidate.1 becomes necessary

First preserve candidate.0 frozen lineage, then follow branch/release discipline. Never mutate candidate.0 in place.
