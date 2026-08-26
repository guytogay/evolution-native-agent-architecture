# Version Selection 001 — Next operational architecture candidate

Status: `VERSION_SELECTION / NEXT_CANDIDATE_VERSION_ASSIGNED / CURRENT_UNCHANGED / NOT_RELEASE_AUTHORITY`

Date: 2026-08-27

Scope gate dependency:

`RELEASE-SCOPE-STABILITY-GATE-001.md = PASS`

## Decision

Assign the next candidate/release line:

```text
NEXT_VERSION = v0.3.7
CURRENT_VERSION = v0.3.6
CURRENT_CHANGE = NO
```

This assignment names the candidate line. It does not make v0.3.7 Current and does not authorize promotion.

## Why v0.3.7 rather than v0.4.0

The repository has no separate `VERSIONING.md` or published GitHub Release object defining a strict external SemVer contract. The durable project convention is visible in formal release history and changelogs.

Recent lineage:

```text
v0.3.3
-> v0.3.4
-> v0.3.5
-> v0.3.6
```

The project has repeatedly used patch-level increments for material but lineage-preserving architectural/adopter changes.

### v0.3.4 precedent

v0.3.4 added a persistent runtime-adoption model, Runtime Adoption Kernel, Compiled Local Projection, source-identity/persistence hardening, and real Hermes field evidence while explicitly leaving the Constitution and core composed validator/schema semantics unchanged.

It still advanced `v0.3.3 -> v0.3.4`.

### v0.3.5 precedent

v0.3.5 made sustained self-evolution the explicit telos and added executable evolution metabolism, migration/evolution machinery and language/adoption changes while retaining all 38 Constitution IDs.

It still advanced `v0.3.4 -> v0.3.5`.

### v0.3.6 precedent

v0.3.6 added Evolution Ecology, latent/expression semantics, adaptation-packet v2, Commons refinements and runtime hot/cold direction with zero new Constitution IDs.

It still advanced `v0.3.5 -> v0.3.6`.

The next candidate is similarly a substantial **operational/adoption architecture increment inside the same v0.3 lineage**, not evidence of a new 0.4 semantic generation.

## Relationship to #80 / #86

Earlier reconciliation correctly concluded:

```text
REAL_RELEASE_DELTA_COUNT = 0
V0.3.7_NECESSITY = NOT_ESTABLISHED
```

for the then-investigated question:

> Does post-v0.3.6 research require new canonical semantic/Core rules?

That conclusion remains intact:

```text
NEW_CORE_SEMANTIC_DELTA_REQUIRED = 0_DEMONSTRATED
```

The current release pressure was discovered at a different layer:

```text
mature concrete HOWs exist
but adopter cannot reliably discover/instantiate them
+
selected optional reference library
+
selected v2 practical tooling
+
selected operational language/adoption surface
-> MATERIAL_OPERATIONAL_RELEASE_VALUE
```

Therefore assigning `v0.3.7` does **not** retroactively claim #86 was wrong. It reflects a later, independently established operational release scope.

## v0.3.7 release thesis

Working description:

> **v0.3.7 makes ENA operationally inhabitable: keep the semantic trunk stable, expose concrete plural HOWs, bundle optional reference organs without making them mandatory, and provide a practical v2 evolution path.**

Candidate cargo is defined by release-scope records, not by this slogan.

## What the version number does not imply

```text
v0.3.7 assigned != candidate exists
candidate exists != frozen
frozen != validated
validated != reconciled
reconciled != released
released != promoted Current until exact promotion/readback succeeds
```

Current remains singularly:

`v0.3.6 / CURRENT / FIELD_VALIDATION`

## Reopen version choice only for a scope-level contradiction

Do not renumber merely because candidate implementation takes multiple iterations.

Revisit `v0.3.7` only if candidate construction reveals a material scope change that genuinely creates a new semantic generation or makes this numbering misleading under the repository's own history.

Otherwise candidate succession stays within the v0.3.7 line:

```text
v0.3.7 candidate.0
-> candidate.1 only if material correction is required
-> ...
```

Candidate numbering is development/evidence identity, not adopter version identity.

`CURRENT_CHANGE = NO`
