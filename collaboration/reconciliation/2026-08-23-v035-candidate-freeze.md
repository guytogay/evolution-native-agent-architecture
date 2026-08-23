# ENA v0.3.5 Candidate Freeze — 2026-08-23

Status:

`FROZEN_CANDIDATE / AUTHOR_SELF_CHECKED / AWAITING_INDEPENDENT_FALSIFICATION / NOT_CURRENT / NOT_RELEASED`

This record freezes the first ENA v0.3.5 candidate after author-side semantic/tool hardening. It does **not** claim independent validation, release fitness, or Current status.

## 1. Frozen identity

Repository:
`guytogay/evolution-native-agent-architecture`

Base canonical `main` commit at candidate start:
`9d84e179aae9f5f5d8dbabc7be56dee4ae2f8724`

Frozen candidate source commit:
`eb6d7ba00894ed446903aebe61cd59f0bdb59af7`

Frozen candidate package path:
`releases/v0.3.5-candidate/`

Frozen candidate effective-content Git tree:
`f373e7695348c157dcd48d3ed243ea3079215b8f`

Frozen source root Git tree:
`791adc27aa5c1a57aaeee3e6f3a9a4534653672f`

Draft PR:
`#57 — candidate: ENA v0.3.5 evolutionary metabolism and language portability`

The branch name is a development pointer and is not the frozen semantic identity. Any later change to `releases/v0.3.5-candidate/` would invalidate this frozen identity and must be treated as a successor candidate (for example candidate.1), not as an invisible edit to this candidate.

## 2. Current isolation

`releases/current/` remains v0.3.4 and its tree remains:

`b237802c08d608bb9be650fe213b7846d3be4bf6`

A final compare from base commit `9d84e179...` to frozen source commit `eb6d7ba...` shows only the v0.3.5 candidate package and its candidate-validation workflow as new/changed surfaces; no `releases/current/**` path changed.

Therefore this freeze does not promote, replace, or mutate Current.

## 3. Candidate purpose

The candidate makes the ENA telos explicit:

> **ENA exists to make sustained self-evolution viable.**
>
> **Evolution is the purpose; governance protects evolvability.**

Its intended posture is exploration-forward: variation may precede certainty, but positive adaptation/improvement claims follow observed outcomes. Governance should protect truthful selection, owned consequence, recovery/correction capacity, and continued evolvability rather than suppress useful variation.

## 4. Major semantic/operational changes under test

- event + Host-chosen periodic/idle evolution wake; no forced mutation cadence;
- real evolution metabolism: observe -> wake -> vary -> experiment -> evaluate -> select -> integrate/prune -> migrate/recombine -> repeat;
- Variation Space for meaningful uncertain self-change;
- internal capability/permission topology may evolve inside a legitimate Variation Space, while external mandate cannot be self-minted;
- outcome-based variation/adaptation selection with mixed/unknown dimensions;
- Evolution Commons / adaptation migration with receiver-side differential validation;
- negative source results remain negative evidence across migration;
- composition treated as both a failure and positive-emergence search surface;
- Evolutionary Subject, Protected Subject, and Continuity Vector instead of an unbounded organism metaphor or mandatory binary same-Agent claim;
- governance closure semantics with finite review;
- anti-sovereign / anti-caste role framing;
- lawful redaction/minimization/deletion without using history preservation as a prohibited-payload retention mandate;
- effective-loaded-surface persistence semantics;
- 38 stable Constitution IDs retained with a concept map rather than renumbering/deleting rules;
- English canonical authoring + Simplified Chinese semantic projection with stable semantic IDs;
- paired English/Chinese decision-semantic fixtures;
- reference `tools/ena_evolve.py`, evolution-record schema/template, and adaptation-packet schema;
- proposed retirement of active adopter-facing `MAINLINE / NOT_MAINLINE` status beginning with v0.3.5 while preserving historical Mainline occurrence records;
- flattened v0.3.5 operational contracts: no active `05A` patch/composition layer is required for candidate semantics.

## 5. Author-side falsification findings and corrections before freeze

The author/orchestrator found and corrected the following before this freeze. These are not independent findings.

### A1 — positive selection could be recorded without enough represented outcome/evidence

Earlier `ena_evolve.py` allowed a caller to label a candidate `SUPPORTED` without requiring a represented outcome/evidence reference.

Correction:
- non-UNKNOWN selection requires represented outcome(s) and evidence reference(s);
- `SUPPORTED/PARTIAL` require at least one `IMPROVED` dimension;
- `HARMFUL` requires at least one `DEGRADED` dimension;
- the tool explicitly says referenced evidence is not externally verified by the tool.

### A2 — unresolved integration path was too broad

Earlier `--allow-unknown` could record integration even for a merely proposed candidate.

Correction:
- negatively selected candidates cannot be overridden into integration;
- unknown integration is allowed only after actual experiment plus explicit `UNKNOWN` evaluation;
- a merely `PROPOSED` candidate cannot use uncertainty to bypass reality contact.

### A3 — migration could obscure source selection state

Earlier migration packets did not elevate source selection status/purpose prominently enough.

Correction:
- packets distinguish `ADAPTATION_CANDIDATE | NEGATIVE_EVIDENCE | UNRESOLVED_VARIATION`;
- preserve `source_status`, source environment/evaluations/dependencies;
- receiver import preserves negative/unresolved source character rather than silently becoming positive local proof.

### A4 — governance closure could manufacture false readiness

Earlier generic closure output could say `READY` merely because no blocker argument was supplied.

Correction:
- closure now declares `evidence_scope: REPRESENTED_INPUTS_ONLY`;
- `unrepresented_material_blockers: UNKNOWN`;
- `READY` means ready only on materially complete represented inputs, not proof that omitted blockers do not exist.

### A5 — candidate semantics were split across inherited core + v0.3.5 patch layer

Earlier candidate structure had `05-CORE-OPERATIONAL-CONTRACTS.md` plus `05-V035-OPERATIONAL-EXTENSIONS.md`, recreating a semantic composition burden.

Correction:
- v0.3.5 active operational semantics were flattened into one `05-CORE-OPERATIONAL-CONTRACTS.md`;
- the extension file was removed;
- inherited composed-validator implementation remains separately preserved/tested without requiring runtime document composition.

### A6 — structural language parity could be mistaken for behavioral semantic equivalence

Correction:
- added paired bilingual semantic fixtures;
- candidate CI checks only structural pairing/ID parity;
- Chinese projection manifest explicitly records behavioral conformance as `UNPROVEN_PENDING_MODEL_EXPERIMENT`.

### A7 — migration packet digest could be over-read as source authentication

Correction:
- packet digest is described only as internal-consistency / accidental-change detection;
- it is explicitly **not** source authentication or an external trust anchor;
- consequential source-authenticity claims require an external provenance/signature/trusted-channel mechanism appropriate to the decision.

## 6. Automated checks at frozen source commit

At source commit `eb6d7ba00894ed446903aebe61cd59f0bdb59af7`:

- Main Gate — run `32611654491` — `SUCCESS`;
- Validate ENA v0.3.5 candidate — run `32611654576` — `SUCCESS`;
- CodeQL — run `32611654552` — `SUCCESS`.

Candidate validation includes:

- parse candidate JSON/YAML;
- validate evolution-record template/schema;
- run inherited composed-validator regression suite;
- run `ena_evolve.py selftest`;
- compile candidate Python tools;
- exact English/Chinese Constitution ID parity (`ENA-CON-001..038`);
- bilingual semantic-fixture structural checks;
- baseline/projection pointer checks;
- superseded extension-layer absence;
- explicit structural-parity != behavioral-conformance boundary;
- Current-isolation/telos check.

Passing these checks is not an independent semantic verdict.

## 7. Known unvalidated boundaries at freeze

The following remain deliberately open for independent falsification/field evidence:

1. **Exploration-forward semantic safety/usefulness** — whether Variation Space and aggressive variation create enough innovation without silently expanding unowned consequence.
2. **Permission/mandate separation under adversarial composition** — whether internal permission mutation can still be laundered into external mandate through another path.
3. **Outcome-selection false confidence** — whether the reference tool/schema still permits misleading support/adaptation claims.
4. **Migration provenance/authenticity** — packet digest is not source authentication; external provenance remains Host/project-specific.
5. **Cross-language behavioral conformance** — English/zh-CN structural parity exists; actual model decision equivalence is unproven.
6. **Constitution concept-map compression** — whether adopters keep all universal invariants applicable rather than treating families/hot distinctions as permission to delete cold semantics.
7. **Continuity Vector usability** — whether it is simpler/more decision-useful than binary identity without hiding materially changed evidence/authority.
8. **Governance closure** — whether closure reduces recursion/ceremony without under-governing real blockers.
9. **Anti-sovereign semantics** — whether accountability remains possible without recreating castes or a self-sealing authority layer.
10. **Composition/emergence** — whether positive emergence attention adds useful search rather than encouraging post-hoc celebration.
11. **Status simplification** — whether retiring active Mainline/Not-Mainline reduces adopter confusion without removing decision-useful maturity information.
12. **Adoption/runtime economics** — token/context/memory/tool/user burden across real Hosts remains to be measured.
13. **Reference-tool realism** — the tool records state/evidence boundaries; it deliberately does not execute arbitrary self-mutation, verify external evidence truth, prove authority/recovery, or authenticate migration sources.
14. **Fresh Host application** — no fresh independent Host has yet adopted this frozen candidate and demonstrated natural runtime evolution behavior.

## 8. Freeze rule

From this record onward:

`releases/v0.3.5-candidate/ @ tree f373e7695348c157dcd48d3ed243ea3079215b8f`

is the immutable subject of independent validation.

Do not edit it in place to answer validator findings. If material correction is required, create a successor candidate identity (for example `v0.3.5-candidate.1`) with explicit lineage and targeted revalidation.

## 9. Current disposition

`FROZEN_CANDIDATE`

`AUTHOR_SELF_CHECKED = YES`

`AUTOMATED_CHECKS = PASS`

`INDEPENDENT_FALSIFICATION = PENDING`

`CURRENT = NO`

`RELEASED = NO`

`PROMOTION = NOT_AUTHORIZED`
