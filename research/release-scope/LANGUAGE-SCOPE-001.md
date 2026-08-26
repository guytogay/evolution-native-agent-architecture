# Language Scope 001 — Operational Architecture projection

Status: `RELEASE_SCOPE_DECISION / ZH_CN_COVERAGE_SELECTED / BEHAVIORAL_EQUIVALENCE_UNPROVEN / CURRENT_UNCHANGED`

Date: 2026-08-27

## Problem

The next candidate's main value is practical HOW discoverability. It would be incoherent to keep the semantic WHAT/WHY available in zh-CN while making the new HOW entry layer effectively English-only.

Current v0.3.6 already records a known gap that long-tail operational contracts remain primarily in the canonical authoring language.

The next candidate should reduce that gap where the new release itself creates material adopter-facing operational meaning.

## Selected zh-CN projection scope

Project the following new/changed adopter-facing surfaces into zh-CN:

### Hot / entry surfaces

- `00-READ-ME-FIRST.md`;
- `RUNTIME-ADOPTION-KERNEL.md`;
- `operational/README.md`;
- `operational/CUE-INDEX.md`.

### Cold but decision-bearing operational surfaces

- `operational/HOW-MAP.md`;
- Purpose-Relative Continuity procedure;
- Standing Input procedure;
- Control Retirement procedure;
- Evolution Commons pattern;
- Host-mapping guidance where wording changes applicability/decision meaning.

These are not required to stay hot, but Chinese-language adopters should not need to infer their practical meaning from English-only prose.

## Machine reference library language policy

Do **not** require literal translation of every schema, fixture, validator, code comment, or historical README.

Instead provide a release-local zh-CN reference guide covering each bundled reference's:

- WHAT / WHY;
- when it applies;
- when it does not apply;
- main state/result vocabulary;
- composition dependencies;
- evidence/trust boundary;
- exact stable reference ID/path.

Machine state identifiers may remain stable English-like protocol tokens where changing them would create cross-language drift.

```text
STABLE_MACHINE_ID
!= ENGLISH_ONLY_DECISION_INTERFACE
```

A Chinese Agent may operate the machine reference using stable identifiers while receiving the semantic decision guidance in zh-CN.

## Selected material fixture distinctions

Add paired EN/zh-CN decision fixtures for material new operational distinctions. The set should include at least the following decision shapes where wording can change behavior:

```text
bundled reference != required runtime organ
reference valid != reference applicable
cue index / HOW library != always-hot context
WAIT wake != authority to resume
non-authority-bearing action may legitimately use NOT_REQUIRED
source selection != receiver-local selection
no recent incident != control no longer needed
continuity for this decision != universal same-Agent identity
being heard / Standing != veto or sovereignty
```

The list is a current coverage set, not an ontological fixed count.

## Behavioral evidence boundary

Candidate structural checks may prove:

- files exist;
- stable IDs align;
- fixture structure is valid;
- manifest coverage is internally consistent.

They do not prove that one model/Host makes equivalent decisions in English and zh-CN.

```text
STRUCTURAL_PROJECTION_PASS
!= BEHAVIORAL_DECISION_EQUIVALENCE
```

Behavioral equivalence remains field/candidate validation evidence and should be reported as such.

## Projection manifest direction

The candidate zh-CN projection manifest should explicitly declare:

- source candidate/release semantic identity;
- operational entry/cue/HOW coverage;
- procedure/pattern coverage;
- reference-guide coverage;
- untranslated machine/reference internals;
- paired semantic fixture sets;
- structural validation status;
- behavioral semantic-conformance status.

Do not hide partial cold-reference translation behind a generic `CURRENT_SEMANTIC_PROJECTION` label without declaring the limitation.

## Why not translate the entire research/reference tree

The release should translate **decision-bearing adopter surfaces**, not every implementation artifact merely because it exists.

Full duplicate translations of validators, schemas and research histories would:

- increase drift/maintenance cost;
- create duplicate quasi-canonical sources;
- add little value where machine identifiers are already language-neutral enough;
- distract from the real requirement: preserve decision meaning.

## Candidate language acceptance

Before release promotion:

1. all selected hot/entry operational surfaces have zh-CN projections;
2. the HOW map/procedures/patterns are semantically accessible in zh-CN;
3. every bundled machine reference is covered by the zh-CN reference guide or explicitly marked uncovered/partial;
4. stable machine/reference IDs remain aligned;
5. paired fixtures cover material new operational distinctions;
6. behavioral conformance is not overclaimed.

`CURRENT_CHANGE = NO`
