# ENA v0.3.4 — DSH longitudinal refresh summary

Date: 2026-08-22

Role: experienced longitudinal field adopter / Host with prior deep ENA exposure.

Source: user-supplied DSH refresh report in conversation. This file is a Host reconciliation summary, not an independent validation report.

## Prior local state

DSH reported that its durable execution baseline remained ENA v0.2.11 MAINLINE, with references spread across `~/.dsh/AGENTS.md`, workspace `AGENTS.md`, `SESSION-HANDOVER.md`, and `evolution/ADOPTION-PROFILE.yaml`. It also reported a pre-existing local inconsistency: `ADOPTION-PROFILE.yaml` still carried `universal_version: 0.2.10` while comments pointed to v0.2.11.

The old local identity model relied mainly on version label + candidate revision rather than immutable Git/package identity.

## Canonical Current identity found during refresh

DSH verified:

- Current version: `v0.3.4`
- status: `CURRENT / FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE / NOT_MAINLINE`
- release merge commit: `26f171dbc1e6c09c3a504dd67480f04fcd08e4c7`
- `releases/current/` tree: `b237802c08d608bb9be650fe213b7846d3be4bf6`
- release package SHA-256: `6821480334ac961f1becd8d0a824bd4a9bce22f6fad01da4870190321e657e33`

DSH observed a later repository `main` HEAD (`068446d...`) and correctly used the Current subtree identity rather than version-number recency to determine effective Current content.

Host reconciliation: the later repo cleanup commit changed repository outer state but did **not** change the `releases/current/` subtree bytes/tree. Therefore `repo HEAD changed` must not be relabeled as `effective Current content changed`.

## Runtime refresh performed by DSH

DSH reported a minimal persistent update to its auto-loaded `~/.dsh/AGENTS.md`:

1. execution baseline changed from historical v0.2.11 MAINLINE to v0.3.4 Current with immutable identity and NOT_MAINLINE status;
2. compact v0.3.4 Runtime Kernel added, including hot/cold path triggers, profiles-as-intensity, persistence-boundary claim discipline, recovery distinction, and durable operating distinctions;
3. legacy semantic-numbering expectations were adjusted;
4. v0.1–v0.2.11 packages were removed from active execution-path status and retained as historical/rollback material.

DSH used its native host transaction/recovery mechanism before mutating the durable instruction surface and reported the mutation committed after its normal observation window.

It also wrote a knowledge-layer refresh record to Anytype.

## What DSH deliberately did not change

DSH did not modify the canonical ENA repository. It also did not automatically update workspace `AGENTS.md`, `SESSION-HANDOVER.md`, or `ADOPTION-PROFILE.yaml`, and did not wholesale re-derive legacy compliance evidence. It requested maintainer/Host direction before doing so.

## Persistence boundary

DSH correctly narrowed its claim to current-session durable write + current-session Host consumption. It did not claim a genuine fresh-session boundary had been re-evidenced for v0.3.4.

## Material field criticisms retained

### 1. Current vs historical Mainline vocabulary friction

DSH found `Current / FIELD_VALIDATION / NOT_MAINLINE` alongside historical `v0.2.11 MAINLINE` cognitively costly for an experienced adopter. This is a usability observation, not evidence that Current identity is ambiguous when the canonical pointer is followed.

### 2. Salience remains an application problem

DSH argued that persistent-self-mutation recovery reasoning is still dependent on runtime salience and may recur even when the rule exists. Host reconciliation: retain as a field hypothesis; do not accept the stronger claim that it is inherently unsolvable at the rule/mechanism layer.

### 3. Validator scope vs external-world truth

DSH noted that the composed validator can validate declared registry/evidence/support semantics but cannot independently establish the external-world truth of every evidence-support relation. This is a useful assurance-boundary clarification, not a new v0.3.4 regression.

### 4. Multiple local carriers can drift

DSH operates across auto-loaded AGENTS, workspace instruction/handover/profile files, and knowledge stores. Refreshing multiple copied kernels creates local shadow-baseline/drift risk. Prefer one authoritative compiled runtime projection plus small pointers/derived records where practical rather than full semantic duplication across carriers.

### 5. Release-authoring ceremony can be over-applied by adopters

DSH described release parity/read-back discipline as burdensome to an adopter. Host reconciliation: ordinary adopters are not required to repeat release-authoring/promotion ceremony merely to consume an already-published Current baseline. This overlaps Issue #51 O8.

### 6. Legacy semantic identifier migration

DSH reported old local compliance references to `ENA-VAL-*` identifiers that no longer exist in Current, while Governance Value and later hardening semantics are represented through current `ENA-CAP-*` / contract sections. This creates migration cost for long-lived adopters and may justify an explicit legacy-identifier mapping/migration note in a future release or external migration guide.

### 7. Self-digest expectation requires care

DSH observed that `CURRENT-BASELINE.yaml` does not carry a digest of the entire Current subtree inside itself. Host reconciliation: embedding the digest of a tree that includes the digest-bearing file creates a self-reference problem. Effective-content identity should instead use an external Git tree/package digest or another non-self-referential identity anchor. This reinforces Issue #51 O1/O9 rather than requiring a self-hash field.

## Host-side decision recorded by reconciliation

Recommended next Host action is **selective active-pointer convergence**, not blind rewriting of all history:

- if workspace `AGENTS.md`, `SESSION-HANDOVER.md`, or `ADOPTION-PROFILE.yaml` are active runtime/decision inputs, update their active Current pointer to v0.3.4 and remove contradictory live version claims;
- if any are historical evidence/snapshots, preserve them unchanged and mark/use them as historical rather than rewriting occurrence history;
- correct the reported `ADOPTION-PROFILE.yaml` v0.2.10/v0.2.11 internal inconsistency if that file remains an active current-state artifact;
- do **not** wholesale re-derive all historical v0.2.11 compliance evidence; re-derive only current claims whose semantics, identifier references, applicability, or decision use changed;
- preserve v0.2.11 as a read-only historical/rollback baseline.

A genuine fresh-session DSH test is useful but should be run at the next natural fresh-session boundary, without an ENA reminder before the first ordinary task. Do not manufacture a fake task solely to satisfy governance evidence.

## Disposition

`LONGITUDINAL_REFRESH_SUPPORTED_WITH_MIGRATION_AND_MULTI_CARRIER_FRICTION`

No v0.3.4 Current semantic change is authorized by this evidence alone.
