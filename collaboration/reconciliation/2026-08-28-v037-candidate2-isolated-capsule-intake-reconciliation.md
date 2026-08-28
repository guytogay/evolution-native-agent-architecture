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

A deterministic builder now produces two physically separate review carriers:

1. A-S semantic capsule — project context/history/oracles physically absent, declared semantic-preserving projections where exact files are mixed-role;
2. A-P supplement — exact frozen candidate.2 package, delivered only after A-S content seal.

## Build/audit evidence

Workflow run:

`33131665994` — SUCCESS

Observed PASS layers:

- frozen candidate and Current binding;
- isolated capsule build;
- forbidden project-surface absence;
- author/history priming sweep;
- Python executable AST projection equivalence;
- exact A-P frozen candidate package;
- deterministic rebuild/hash equality;
- artifact upload.

Deterministic inner hashes:

- `candidate2-as-capsule-r3.zip`
  - SHA-256 `ee80ac827dedff7a8de9d10f0a9cbcd70c66f3b7b885296f9e2335af6ec92131`
- `candidate2-ap-supplement-r3.zip`
  - SHA-256 `b3e2222c591a2760b976e6791f18e2494c17063ddfe539291f1cd8799fd54bcd`

GitHub Actions artifact:

- id `9670480727`
- outer artifact SHA-256 `104005b329cc042721da76a38f8a41c282c278bca3d2c424ecd7288ceeb1c357`

## Fresh review sequence

Do not create another GitHub issue as the mandatory fresh A-S entrypoint.

Fresh A-S receives only:

- the A-S ZIP;
- its expected SHA-256;
- a minimal instruction to read `INTAKE-A-S.md` inside the ZIP and not browse the project repository.

A-P ZIP must not be supplied or made directly accessible to that reviewer before A-S report content is sealed.

A-S seal for this carrier:

`SHA256(EXACT_COMPLETED_A_S_REPORT_BYTES)`

After the reviewer returns the A-S report and digest, the project manager verifies/persists them. Only then is the A-P supplement separately delivered to the same reviewer.

After A-P report completion the reviewer stops before Phase B.

## Decision boundary

- validation-interface defect alone does not require candidate.3;
- material candidate.2 byte defect found by valid independent review requires candidate.3;
- Current remains v0.3.6 until explicit later promotion;
- attack cardinality remains OPEN.
