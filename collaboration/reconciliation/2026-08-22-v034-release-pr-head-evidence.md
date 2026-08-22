# ENA v0.3.4 — PR-head release evidence

Date: 2026-08-22

Status: `PR_HEAD_RELEASE_EVIDENCE_COMPLETE / READY_FOR_MERGE / NOT_MAINLINE`

PR: #48

Release branch: `release/v0.3.4`

Release authoring commit carrying canonical Current bytes:
`0d9ae4f28fd44a97b76814ac69f204d65aa3e000`

Release/Current Git tree:
`b237802c08d608bb9be650fe213b7846d3be4bf6`

`releases/current/` and `releases/v0.3.4/` point to the same tree.

Workflow-pointer correction commit:
`14a26ae5d6caf101e0f22068a293ea9b4d30e6d0`

The correction changed release tooling from v0.3.3 package identity/pointer assertions to v0.3.4. It did not mutate the canonical Current tree.

## PR-head CI

At head `14a26ae5d6caf101e0f22068a293ea9b4d30e6d0`:

- Main Gate run `32570873003`: SUCCESS
- Validate and package ENA Current run `32570873037`: SUCCESS
- CodeQL run `32570873001`: SUCCESS

The packaging run passed:
- JSON schema parse;
- v1 semantic selftests;
- inherited 164-case v2 corpus;
- D1/D2/D3 61-case closure corpus;
- deterministic inherited regression suite;
- CLI OK/BLOCK/UNKNOWN semantics;
- v0.3.4 Current baseline pointer validation;
- deterministic package build from canonical committed Current bytes;
- internal ZIP exact file-set and per-file read-back parity.

## Published PR-head artifact

Artifact ID:
`9475278201`

Artifact name:
`ENA-v0.3.4-release-package`

Outer GitHub artifact digest:
`sha256:44e93856273a66bf85fa69e609a767ff72379ce5e30eb3f516e6925df6521e3a`

The artifact was actually downloaded and inspected by the Host.

It contains:
- `ENA-v0.3.4-CURRENT.zip`
- `ENA-v0.3.4-CURRENT.zip.sha256`
- `ENA-v0.3.4-RELEASE-EVIDENCE.json`

Downloaded inner Current ZIP SHA-256:
`6821480334ac961f1becd8d0a824bd4a9bce22f6fad01da4870190321e657e33`

The downloaded sidecar reports the same digest.

Release evidence JSON reports:
- `ena_version: v0.3.4`
- `status: FIELD_VALIDATION`
- `complete_adoption_baseline: true`
- `mainline_claim_allowed: false`
- canonical Current source commit: `0d9ae4f28fd44a97b76814ac69f204d65aa3e000`
- file count: `30`
- source bytes from Git objects: true
- exact file-set parity: true
- per-file SHA-256 parity after ZIP read-back: true
- deterministic ZIP metadata: true

The downloaded inner ZIP was independently enumerated by the Host and contains exactly 30 files.

## Claim boundary

This evidence supports merging PR #48 as the v0.3.4 Current release change.

It does not support a Mainline claim.

Release workflow completion is still pending the merge itself and post-merge workflow/artifact verification on `main`.
