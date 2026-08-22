# ENA v0.3.4 — DSH active-state reconciliation summary

Date: 2026-08-22

Role: longitudinal field adopter / mature Host migration follow-up.

Source: user-supplied DSH reconciliation report plus three attached Host artifacts (`SESSION-HANDOVER.md`, workspace `AGENTS.md`, and `ENA-VAL-MIGRATION-MAPPING.yaml`). This is a Host reconciliation summary, not an independent semantic validation of all DSH-local claims.

## Disposition

`ACTIVE_STATE_RECONCILIATION_SUPPORTED_WITH_LOCAL_HOST_FRICTIONS`

DSH reports transaction `txn-0045` completed as `COMMITTED / NATIVE` after the Host's normal observation window. The migration strategy correctly converged active state while preserving historical occurrence evidence.

## Active artifacts reported updated

DSH classified the following as active runtime/decision inputs and updated them to reflect v0.3.4 Current:

- workspace `AGENTS.md`;
- `SESSION-HANDOVER.md`;
- `evolution/ADOPTION-PROFILE.yaml`;
- `evolution/COMPLIANCE-EVIDENCE.yaml` via an additive `delta_v0.3.4` block;
- new `evolution/ENA-VAL-MIGRATION-MAPPING.yaml`.

The attached workspace `AGENTS.md` visibly names canonical ENA Current as v0.3.4, records Current tree/package identity, distinguishes `CURRENT / FIELD_VALIDATION / NOT_MAINLINE`, and retains the v0.2.11 package as read-only historical Mainline / Host-mechanism baseline.

The attached `SESSION-HANDOVER.md` similarly records v0.3.4 as canonical Current while preserving historical v0.2.x adoption entries and explicitly retaining v0.2.11 as read-only historical Mainline / rollback material.

## Historical artifacts intentionally preserved

DSH reports leaving historical material unchanged, including:

- `Evolution-Native-Agent-Universal-Bootstrap-v0.2.11/`;
- older ENA archives and recovery snapshots;
- original capability/compliance evidence rows containing legacy identifiers;
- historical knowledge objects.

This is the desired migration property:

`current state convergence != historical occurrence rewrite`.

## Selective compliance re-derivation

DSH reports re-deriving only claims whose current interpretation could materially change:

- `ENA-CAP-048`: narrowed to Host-local machine-checkability; canonical composed claim-pack validation remains a separate Current mechanism and was not falsely claimed as adopted Host artifact validation.
- `ENA-CAP-046/047`: re-derived under v0.3.4 profiles-as-runtime-intensity framing; local conclusion unchanged.
- other retained `ENA-CON-001..038` / `ENA-CAP-001..071` claims were not wholesale re-derived solely for version ceremony.

This selective approach is consistent with governance-cost proportionality.

## Legacy ENA-VAL migration map

The attached `ENA-VAL-MIGRATION-MAPPING.yaml` parses successfully and is structurally complete for `ENA-VAL-001..032`:

- 32 rules total;
- 32 unique IDs;
- no missing IDs in `001..032`;
- no extra IDs;
- classifications: 26 `semantic_equivalent`, 6 `merged`, 0 `retired`, 0 `materially_changed`.

The file preserves original legacy identifiers and maps them to current contract/CAP destinations instead of rewriting historical evidence.

Important evidence boundary: this structural check does **not** independently prove that every one of the 32 semantic-equivalence judgments is historically exact. The `26 equivalent / 6 merged / 0 materially changed` conclusion remains DSH's Host migration analysis unless separately revalidated against the complete historical source set.

## New Host findings

### 1. Dual-baseline reality: canonical ENA vs Host implementation baseline

DSH now operates with:

- canonical governance/adoption baseline = ENA v0.3.4 Current;
- some Host mechanisms/tooling still implemented by the frozen v0.2.11 package.

This is not automatically inconsistent. A long-lived Host may adopt newer semantics while retaining older implementation machinery whose current scope is explicitly narrowed and evidenced.

Opportunity: distinguish `canonical semantic/adoption baseline` from `Host implementation/mechanism version` so adopters do not assume every Host tool must share the Current ENA release number.

### 2. Host transaction tool does not cover all target locations uniformly

DSH reports `begin-transaction.ps1` crashes on workspace-root files outside the `evolution/` subtree because of a substring/path assumption. DSH used a prior-compatible workaround: evolution targets entered the normal transaction target list while root-level files received explicit before-copies within the same transaction/recovery evidence set.

Classification: `HOST_FRICTION / TOOLING_DEFECT`, not an ENA Current semantic defect. Fixing the Host script requires separate Host/meta authority; no automatic ENA change follows.

### 3. Living-document metadata drift

The attached `SESSION-HANDOVER.md` now contains a 2026-08-22 v0.3.4 refresh entry, but its section heading still says `当前状态（2026-08-19）`.

Classification: low-consequence local documentation drift. It should be corrected opportunistically when that active document is next legitimately changed; it does not justify a separate governance ceremony.

### 4. Multi-carrier convergence remains a real maintenance cost

DSH successfully synchronized active pointers across global AGENTS, workspace AGENTS, handover, adoption profile, and compliance delta while preserving history. This is positive migration evidence, but it also reinforces the field hypothesis that multiple local carriers can become shadow baselines.

Prefer one authoritative always-loaded compiled runtime projection plus smaller pointers/derived records where practical; do not require identical full-kernel copies in every carrier.

## Fresh-session boundary

DSH correctly leaves the genuine v0.3.4 fresh-session boundary open. The next useful evidence is a naturally occurring new DSH session with no ENA reminder before the first ordinary task, observing whether the v0.3.4 Runtime Kernel / Current identity is automatically present and materially applied.

Do not manufacture a fake production task merely to satisfy evidence ceremony.

## Current project effect

This report does not modify or reopen `releases/current/` semantics.

It strengthens field evidence for:

- selective migration of active state;
- historical preservation;
- semantic-identifier migration cost;
- dual semantic-vs-implementation baselines on mature Hosts;
- multi-carrier drift risk;
- Host tooling edge cases during persistent self/runtime mutation.

No v0.3.5 or Constitution change is authorized by this evidence alone.
