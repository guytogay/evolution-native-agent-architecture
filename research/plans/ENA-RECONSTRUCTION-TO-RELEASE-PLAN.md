# ENA Reconstruction-to-Release Master Plan

Status: `ACTIVE_MASTER_PLAN / RESEARCH_TO_RELEASE / CURRENT_UNCHANGED_UNTIL_PROMOTION`

Project goal:

> Continue ENA from the v0.3.6 semantic trunk into a usable operational architecture with concrete, plural HOWs, Host bindings, tools/processes, and evidence; integrate the mature result into the next Current release when release readiness is actually established.

This plan is the fixed durable planning entrypoint for future sessions.

Machine-readable current execution state: `research/plans/PROGRESS.yaml`.

Research bootstrap: `research/RESEARCH-START-HERE.md`.

Research methodology: `research/methodology/`.

## 1. Current baseline and release posture

Adopter-facing Current must always be verified from `releases/current/CURRENT-BASELINE.yaml` on the default branch.

At plan creation, Current is v0.3.6 / `CURRENT / FIELD_VALIDATION`.

Research work is occurring on PR #82 / branch `research/memory-metabolism-prototype` and does not itself mutate Current.

The eventual next release version is deliberately **UNASSIGNED** until scope stabilizes. Do not force `v0.3.7` or `v0.4.0` merely because research is large.

```text
RESEARCH_PROGRESS != RELEASE_DELTA
REFERENCE_ORGAN_EXISTS != CURRENT_MUTATION_REQUIRED
```

However, this project now has an explicit end goal of a new release once operational architecture and release gates support it.

## 2. Architectural direction

ENA is treated as a tree/ecology rather than a single compressed document:

```text
TELOS / PURPOSE
      |
      v
WHAT / WHY
semantic trunk; stable, compact, universal where justified
      |
      +--> HOW-A
      |     +--> concrete organ / process / tool / protocol
      |     +--> Host adapter / binding
      |     +--> failure / fallback behavior
      |     +--> evidence
      |
      +--> HOW-B
      +--> HOW-C
      +--> ...
```

The semantic trunk may converge. HOW should normally concretize and may branch divergently.

```text
ONE_WHAT_WHY -> 0..N_CONCRETE_HOW_BRANCHES
HOW_COUNT = DISCOVERED_NOT_PREALLOCATED
```

The final test is whether an Agent can actually live by the architecture, not merely explain it.

## 3. Repository information architecture

Canonical research surfaces:

```text
research/
├── RESEARCH-START-HERE.md          # small hot bootstrap / router
├── README.md                       # research directory map
├── methodology/                    # how ENA research is conducted
│   ├── README.md
│   ├── ENA-RESEARCH-DISCIPLINE.md
│   ├── HOW-GROWTH-DISCIPLINE.md
│   ├── CARDINALITY-DISCOVERY-GUARD.md
│   ├── SESSION-CONTINUITY-AND-COLLABORATION.md
│   └── METHOD-CHANGELOG.md
├── plans/                          # durable project plan + current execution state
│   ├── ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md
│   └── PROGRESS.yaml
├── reconstruction/                 # archaeology, retention ledgers, gap maps, audits
├── external-how/                   # external mechanism harvesting and ENA mapping
├── prototypes/                     # executable/reference organs
├── experiments/                    # experiments that can pay epistemic rent
├── adversarial-replay/             # historical adversarial/falsification material
├── evolution-inbox/                # unpromoted research intake
└── incidents/                      # research-process incidents / method failures
```

Older paths may remain as compatibility pointers when moving them would break lineage/references.

Directory neatness must not destroy history.

## 4. Work phase A — Research continuity and repo structure

Purpose: make the project inheritable before further large-scale research.

Actions:

- establish `RESEARCH-START-HERE.md`;
- canonicalize methodology under `research/methodology/`;
- add method changelog and session-continuity protocol;
- establish this master plan and `PROGRESS.yaml`;
- establish `research/external-how/`;
- update `PROJECT-HUB.md`, `PROJECT-STRUCTURE.md`, and `research/README.md` to point to canonical surfaces;
- retain compatibility pointers for moved method files.

Exit condition:

A fresh session can discover Current, methodology, project phase, current workstreams, external HOW registry, and next permitted actions from stable entrypoints without reconstructing them from chat history.

## 5. Work phase B — Anti-ablation archaeology / variation recovery

Purpose: recover the practical ENA research tree before further selection bias erases less visible organs.

Sources include:

- historical Issues/PRs/comments;
- prior release evolution;
- HAR/adversarial findings;
- prototypes and failed prototypes;
- Host evidence;
- prior conversation exports where durable GitHub state is incomplete;
- external patterns previously cited but not operationalized.

For each material topic reconstruct:

```text
WHAT
WHY
HOW — EXISTING BRANCHES
HOW — EXTERNAL / NEW CANDIDATE BRANCHES
EVIDENCE — PER BRANCH / HOST
STATUS: PROPERTY | ORGAN | HOST_BINDING | EVIDENCE | ADOPTION
LINEAGE / DISPOSITION
```

Do not use current #90–#94 workstreams as proof of a final ontology.

Exit condition:

Additional archaeology no longer reveals a material missing lineage likely to change the current engineering map. This is a decision-based closure condition, not a fixed topic count.

## 6. Work phase C — HOW branch expansion

Purpose: turn WHAT/WHY into usable operational architecture.

For each surviving branch:

- preserve existing HOWs;
- build/reference concrete mechanisms;
- search for materially different Host realizations where useful;
- define triggers/applicability;
- specify actual actions/state/protocol/tooling;
- specify failure/fallback/WAIT/REFUSE/recovery behavior;
- attach branch-specific evidence;
- preserve UNKNOWN honestly.

Do not search for one universal `THE HOW` unless evidence supports one.

Output may include:

- reference organs;
- decision procedures;
- state machines;
- schemas/contracts;
- scripts/validators/resolvers;
- Host adapters;
- operational playbooks;
- examples/counterexamples;
- external protocol mappings.

## 7. Work phase D — External HOW harvesting

Purpose: avoid reinventing mature mechanisms and enlarge the HOW possibility space.

Search current external sources including:

- AI agent runtimes/frameworks;
- AI memory systems;
- workflow/durable-execution systems;
- agent-to-agent protocols;
- AI engineering/research organizations;
- AI developer communities;
- security/identity systems;
- distributed systems/networking/databases where directly useful.

Record each candidate under `research/external-how/` with:

```text
source + date
mechanism observed
source evidence class
ENA WHAT/WHY/failure mapping
candidate HOW mapping
Host/applicability assumptions
known limitations
questions requiring falsification/reality contact
selection state
```

External popularity is not selection proof.

## 8. Work phase E — Host binding and lived usability

Purpose: prove that operational branches can inhabit real bodies.

Relevant Hosts may include current/future systems such as Hermes, OpenClaw, Codex, WorkBuddy, LangGraph/Temporal-style runtimes, Microsoft Agent Framework, Letta, or other materially distinct Hosts discovered during research.

For each selected Host binding, determine:

- existing native organ(s);
- mapping-only adoption where possible;
- missing adapter/tooling;
- context/persistence/authority/effect constraints;
- natural retrieval/salience behavior;
- operational burden;
- failure/recovery behavior.

Do not force every Host to instantiate every organ.

```text
DEFINED != APPLICABLE != IMPLEMENTED != ACTIVE != EVIDENCED
```

## 9. Work phase F — Cross-organ composition

Purpose: detect failures that only appear when individually valid organs interact.

Examples:

- Memory Metabolism × Retrieval × Decision Projection;
- Commitment/Settlement × Effect Lifecycle × Authority Lease;
- Recovery × authority expiry × external effect reconciliation;
- identity/epoch × commitment × reputation;
- multi-agent task/coordination × evidence independence;
- Tiny Hot Kernel × Host cold retrieval × language projection.

Prefer static composition analysis/deterministic fixtures where the failure is derivable. Use experiments only where reality can reveal unknown interaction or dynamics.

## 10. Work phase G — Operational architecture assembly

Purpose: turn the research tree into an adopter-usable ENA architecture without collapsing the HOW ecology.

Candidate release structure should distinguish at least conceptually:

```text
Semantic Core / WHAT-WHY trunk
Operational Architecture / HOW tree
Reference organs and Host adapters
Evidence and applicability guidance
Tooling / schemas / playbooks
Research/open questions outside release scope
```

The exact file structure and naming are selection outcomes, not pre-fixed ontology.

Important constraint:

`Repository knowledge breadth != always-loaded runtime context`.

Use hot routing + cold exact retrieval rather than shrinking the entire ENA repository into one prompt.

## 11. Work phase H — Release-scope reconciliation

Purpose: decide what actually belongs in the next adopter-facing release.

Classify mature research outputs as appropriate:

- Core semantic change;
- Operational Architecture addition;
- reference organ;
- Host adapter/example;
- tooling/schema;
- evidence/adoption guidance;
- retained research only;
- retirement/simplification.

`NO_CHANGE` remains a valid result for individual branches.

Release scope should be coherent enough that an adopter knows what is normative, what is reference implementation, what is optional/Host-conditional, and what remains research.

## 12. Work phase I — Candidate construction and validation

When release scope is stable enough to justify a candidate:

- construct candidate from a pinned committed tree;
- keep Current unchanged during candidate validation;
- run schema/tool/fixture/workflow validation;
- perform cross-document semantic consistency review;
- validate entrypoint/navigation and fresh-Agent usability;
- validate language projection where release claims it;
- freeze exact candidate identity;
- obtain independent review/falsification against the candidate rather than the author's expected oracle;
- repair and refreeze if decision-material defects are found.

No arbitrary pass percentage or reviewer count proves readiness.

## 13. Work phase J — Promotion / release

Promote only after:

- candidate identity and exact content are known;
- decision-material release claims are supported at their stated evidence level;
- critical operational HOW paths are usable enough for the declared release scope;
- known gaps/residuals are explicit rather than silently narrated as solved;
- repository/adoption routing is coherent;
- independent review no longer exposes an unresolved release-blocking contradiction;
- release build/readback/parity checks succeed.

Then:

- promote the selected candidate into the singular `releases/current/` baseline through the existing release discipline;
- update Current pointer/metadata/history;
- verify published readback and exact file/hash parity;
- open/continue field validation for the new Current.

## 14. Release readiness is scope-relative, not metaphysical completeness

The next release does not require every possible ENA problem to be solved forever.

It must truthfully define its scope and not claim operational closure where only WHAT/WHY exists.

A release may contain:

- mature concrete HOWs;
- multiple competing reference HOWs;
- Host-conditional branches;
- explicit UNKNOWN/open operational gaps.

What is forbidden is silently translating those gaps into abstract prose that sounds solved.

## 15. Research method gates

All phases follow `research/methodology/`.

Especially:

```text
EXPLANATION != SOLUTION
PROPERTY != ORGAN != HOST_BINDING != EVIDENCE != ADOPTION
RECOVER_VARIATION_BEFORE_SELECTION
HOW_CARDINALITY_IS_DISCOVERED
EXPERIMENTS_MUST_PAY_EPISTEMIC_RENT
N_OUTPUTS != N_INDEPENDENT_SUPPORTS
STOP_RESEARCH != SOLVED
NO_CHANGE_IS_VALID
REMOVE_FROM_ACTIVE != ERASE_LINEAGE
```

## 16. Progress and handoff rule

After material progress:

- update `research/plans/PROGRESS.yaml`;
- update methodology changelog only when research method changes;
- record external candidate HOWs under `research/external-how/`;
- update relevant Issue/PR/prototype evidence;
- keep `RESEARCH-START-HERE.md` small and update it only when routing changes.

A handoff summary is a pointer, not the project state.

> **The project should remain continuable even when the current session disappears.**
