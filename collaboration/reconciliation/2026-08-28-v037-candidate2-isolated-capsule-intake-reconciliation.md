# ENA v0.3.7 candidate.2 — isolated capsule intake reconciliation

Date: 2026-08-28

Status: `CANDIDATE2_FROZEN / ISSUE137_INTERFACE_ABORTED / ISOLATED_A-S_CAPSULE_READY / A-P_WITHHELD / NOT_CURRENT / NOT_RELEASED`

## Frozen candidate unchanged

Candidate.2 remains frozen at:

- source `bda470e0a6b170cec61225a905957a501454a2fe`
- subtree `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`
- Current subtree at same source `7dcbb3934883ffa6cc5292a662588cafc1533cff`
- exact pre-freeze run `33095987843` — SUCCESS

No candidate.2 or Current byte changed during the validation-interface repair.

## Issue #137 occurrence truth

Issue #137's branch-based A-S intake was invalidated after a fresh reviewer encountered withheld author-status content through normal GitHub README rendering before A-S seal.

Reviewer result:

`A_S_ABORTED_BOUNDARY_CROSSING / VALIDATION_INTERFACE_DEFECT / NOT_SEALED / A_P_NOT_STARTED`

The reviewer report was persisted as interface-defect evidence only. It is not an A-S semantic seal and does not count as independent candidate validation.

Method incident:

`research/methodology/incidents/2026-08-28-CANDIDATE2-GITHUB-NATURAL-NAVIGATION-PRIMING-INCIDENT.md`

## Carrier repair

The project no longer treats same-repository GitHub navigation as the A-S review carrier.

Canonical companion method:

`research/methodology/INDEPENDENT-VALIDATION-CAPSULE-CARRIER.md`

A deterministic builder produces two physically separate review carriers:

1. A-S semantic capsule — project context/history/oracles physically absent, declared semantic-preserving projections where exact files are mixed-role;
2. A-P supplement — exact frozen candidate.2 package, delivered only after A-S content seal.

Generic semantic failure vocabulary remains part of A-S; the priming detector targets author/history/search-map signals rather than deleting the language of false block/failure itself.

## Final build/audit evidence

Authoritative final workflow:

`.github/workflows/v037-candidate2-r3-capsule-build.yml`

Run:

`33131773164` — SUCCESS

Observed PASS layers:

- history-specific priming detector;
- semantic failure vocabulary preserved;
- A-S physical isolation;
- A-S non-self payload inventory;
- exact A-P frozen candidate package;
- A-P non-self payload inventory;
- manifest self-hash explicitly excluded by definition;
- deterministic repeated rebuild/hash equality;
- attack cardinality OPEN.

Final deterministic inner hashes:

- `candidate2-as-capsule-r3.zip`
  - SHA-256 `dfe15a686668440138bfd624453059d61a0b28625bb9a5e0c185b33eccf9c2da`
- `candidate2-ap-supplement-r3.zip`
  - SHA-256 `427a1776aea199f5f27c4bea2827d3c827cf82fab2c8cd403da0e8cc1dd97649`

A-S manifest inventories 78 non-self payloads. A-P manifest inventories 119 non-self payloads. `MANIFEST_SELF_HASH = EXCLUDED_BY_DEFINITION`; the outer capsule digest binds the final manifest bytes.

The earlier build run `33131665994`, artifact id `9670480727`, and hashes `ee80ac...` / `b3e222...` are superseded carrier evidence because they predate the manifest inventory correction and must not be used as the fresh-review carrier identity.

## Fresh review sequence

Do not create or use another same-repository GitHub issue/branch as the mandatory fresh A-S review surface.

Fresh A-S receives only:

- `candidate2-as-capsule-r3.zip`;
- expected SHA-256 `dfe15a686668440138bfd624453059d61a0b28625bb9a5e0c185b33eccf9c2da`;
- a minimal instruction to read `INTAKE-A-S.md` inside the ZIP and not seek project history.

A-P ZIP must not be supplied or made directly accessible to that reviewer before A-S report content is sealed.

A-S seal for this carrier:

`SHA256(EXACT_COMPLETED_A_S_REPORT_BYTES)`

After the reviewer returns the A-S report and digest, the project manager verifies/persists them. Only then is `candidate2-ap-supplement-r3.zip` separately delivered to the same reviewer, with expected SHA-256 `427a1776aea199f5f27c4bea2827d3c827cf82fab2c8cd403da0e8cc1dd97649`.

After A-P report completion the reviewer stops before Phase B.

## Decision boundary

- validation-interface defect alone does not require candidate.3;
- material candidate.2 byte defect found by valid independent review requires candidate.3;
- Current remains v0.3.6 until explicit later promotion;
- attack cardinality remains OPEN.

Next action:

`DELIVER_CANDIDATE2_FINAL_ISOLATED_A_S_CAPSULE_ONLY`
