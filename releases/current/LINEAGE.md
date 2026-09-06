# ENA v0.3.12 Lineage

Status: `CURRENT / FIELD_VALIDATION`

- predecessor Current: `v0.3.11`, tree `a299be149561321ce4e6d6ce71c405712a23b170`;
- source external contribution PR: `#216`;
- source contribution commit: `34f7adfeaebaa99defe2b0030f3e0b2067c9d72f`, author `LXC DSH <dsh@localhost>`;
- verified source issues: `#217`, `#218`;
- source release branch: `release/v0.3.12`;
- active field stream: Issue `#208`;
- release lane: `R0_FIELD_PATCH_EXTERNAL_CONTRIBUTION_COHERENCE`;
- primary field findings: `F-208-05` operational identity/gate coverage gap and `F-208-06` dead HOW-MAP fragment routing.

v0.3.11 remains immutable predecessor occurrence truth and rollback anchor. v0.3.12 does not rewrite it.

The contributor supplied the bounded operational/identity/routing patch and gate extensions. Maintainer review independently verified the findings, rejected direct mutation of the already-released v0.3.11 identity, added the v0.3.12 release projection, repaired the active field-template semantic-identity default, and narrowed the zh-CN recurrence rule so active identity drift is rejected without forbidding genuine historical provenance.

No Constitution IDs or core machine/evolution semantics are added or rewritten.

Future corrections that change effective content require a successor version identity.
