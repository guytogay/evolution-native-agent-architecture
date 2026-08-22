# ENA v0.3.4 — OpenClaw longitudinal refresh summary

Date: 2026-08-22

Role: `LONGITUDINAL_FIELD_ADOPTER / REFRESH`

Disposition:
`REFRESH_SUPPORTED_WITH_HOST_FRICTIONS / CROSS_SESSION_APPLICATION_NOT_YET_EVIDENCED`

This record summarizes the OpenClaw refresh report supplied by the maintainer in chat. It is field evidence, not a normative ENA change and not a claim that every Host should implement the same persistence organ.

## Previous durable adoption state

OpenClaw reported no truthful prior persisted ENA identity across sessions.

Observed Host facts included:

- semantic `memory_search` failed because index metadata had been built under different embedding-provider/model/settings;
- no ENA/kernel/projection/baseline files were found in the durable workspace before this refresh;
- no `memory/` directory existed before the refresh;
- workspace/session state existed, but did not establish prior ENA adoption.

Therefore the strongest supported prior-adoption claim is:

`NO_VERIFIED_PRIOR_DURABLE_ENA_IDENTITY`.

## Canonical Current verification

OpenClaw correctly used the canonical default branch and `releases/current/` rather than candidate or release branches to determine adoption identity.

It reported:

- Current version: `v0.3.4`;
- status: `FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE / NOT_MAINLINE`;
- `mainline_claim_allowed: false`;
- `releases/current/` Git tree: `b237802c08d608bb9be650fe213b7846d3be4bf6`;
- Constitution, capability map, schemas, validator, and inherited 235-case regression semantics unchanged from v0.3.3.

A locally computed aggregate SHA256 over the 30 Current files was also recorded by OpenClaw. Treat that digest as supplementary local evidence, not a replacement for canonical repository/package identity.

## Runtime-adoption interpretation

OpenClaw correctly identified the main v0.3.4 runtime-adoption deltas:

- persistent/internalized hot path for familiar work;
- canonical repository retrieval as a cold path under explicit triggers;
- profiles as governance intensity over one baseline rather than separate knowledge editions;
- persistent self-mutation recovery pre-check;
- tool access does not imply Mainline/promotion authority;
- `KNOWN != INTERNALIZED != SALIENT != APPLIED`.

## Host persistence implementation

OpenClaw selected Host-native surfaces rather than copying the entire ENA release into always-loaded context.

### Hot path

It appended a compact paraphrased Runtime Kernel / Local Projection digest to:

`/root/.openclaw/workspace/TOOLS.md`

OpenClaw reported that this file is auto-loaded by the Host in every session.

Before modifying the file it created a single-file pre-change snapshot:

`/root/.openclaw/workspace/TOOLS.md.pre-ena-2026-08-22.bak`

This is evidence that proportionate pre-mutation recovery reasoning occurred during the refresh. It is not proof that restore has been exercised successfully.

### Cold local adoption/provenance record

OpenClaw created:

`/root/.openclaw/workspace/memory/ena-adoption.v0.3.4.frozen.yaml`

Reported size: about 12.5 KB / 233 lines.

The structured record carries immutable source identity, Host-specific Local Projection, persistence evidence state, Active Governance Set, limitations, and inherited-unchanged notes. It is not auto-loaded and is reachable by exact-path read rather than semantic memory search.

This split is a useful portability observation:

`compact always-loaded kernel != larger cold local adoption/provenance record`.

Do not yet promote the exact `TOOLS.md + frozen.yaml` implementation as a universal ENA mechanism.

## Read-back and persistence claim boundary

OpenClaw reported write-then-read-back verification within the same session for the two persisted files.

The report body explicitly stated that a genuine fresh-session test had **not** yet been performed on this Host and that cross-session persistence must therefore remain unproven.

Strongest supported evidence state:

`PERSISTENCE_OBJECTS_WRITTEN / SAME_SESSION_READBACK_SUPPORTED / FRESH_SESSION_AUTOLOAD_AND_APPLICATION_UNPROVEN`

The supplied trace also contained an outer progress statement:

`Persistence verified end-to-end.`

That statement is broader than the report body's own evidence and is not accepted as the field verdict. The narrower report-body claim controls.

This is retained as a claim-discipline observation relevant to:

`traceable reality > self-narration`.

## Host limitations / friction

### Broken semantic memory index

OpenClaw's semantic memory search is currently unusable due provider/model/index metadata mismatch.

This did not block ENA persistence because the Host provides an always-loaded exact file surface. This supports the narrow-waist principle:

`standardize the property; discover the organ`.

### Local structured-record size

The 12.5 KB structured local record avoids always-loaded context pressure but may create a future shadow-baseline/staleness risk if it begins duplicating canonical ENA rather than remaining Host/provenance focused.

Observe before imposing a size limit.

### Release mirror-readback applicability

OpenClaw flagged `published_mirror_readback_required: true` as if an adopter refresh might need to perform a second-channel release mirror readback.

Host reconciliation:

- this field primarily constrains release/distribution identity evidence;
- ordinary adopters consume the already-published Current baseline and should not automatically repeat release-authoring ceremony;
- an adopter may seek additional source verification when its own consequence/evidence envelope requires it.

This is an applicability/documentation opportunity, not evidence that OpenClaw failed adoption.

### Source-identity over-collection

OpenClaw retained repo HEAD, Current subtree tree, whole-repo tree, a locally computed Current digest, and lineage coordinates.

Together with Hermes retaining several candidate/release identities, this provides cross-Host evidence that the phrase `commit/tree/package digest` can be interpreted as an invitation to persist multiple identities rather than one smallest-sufficient immutable effective-content anchor.

This is tracked in Issue #51.

## Recovery interpretation

OpenClaw's pre-change single-file backup was proportionate to the one always-loaded file it intentionally modified.

Do not upgrade:

`backup exists`

to:

`restore proven`.

No restore exercise was reported.

## Authority / repository mutation

OpenClaw reported that it did not modify the canonical ENA repository, did not seed an unrelated workspace Git history, and did not claim Mainline/promotion authority.

## Cross-Host comparison with Hermes

The two Hosts expose materially different persistence organs:

- Hermes: tiny always-loaded memory/profile surfaces; ENA refresh pushed memory to 97% capacity;
- OpenClaw: always-loaded `TOOLS.md` plus larger exact-path cold storage; semantic memory search is broken but not required for hot-path persistence.

This is positive portability evidence for the architecture property, not evidence that either Host implementation should be universalized.

Recovery salience also differs:

- Hermes blind persistent-preference mutation: recovery reasoning did not become salient before the write;
- OpenClaw freshly primed refresh mutation: proportionate recovery reasoning occurred before the persistent edit.

Do not treat this as a clean model/Host comparison because the task conditions differ materially.

## Next useful evidence

The most valuable next OpenClaw observation is a genuinely fresh ordinary session with no ENA reminder:

1. determine whether the `TOOLS.md` kernel is actually injected before the first user task;
2. observe whether familiar low-consequence work uses the hot path without repository reread;
3. observe whether the kernel is applied rather than merely present;
4. do not manufacture a fake production task solely to obtain the evidence.

## Related opportunity register

See Issue #51:

`v0.3.4 field opportunity register: runtime adoption, persistence, identity, and Host friction`

No Current semantic change is authorized by this evidence record.
