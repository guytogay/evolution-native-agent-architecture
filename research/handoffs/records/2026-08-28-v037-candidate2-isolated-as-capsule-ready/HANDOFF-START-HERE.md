# ENA handoff — candidate.2 isolated A-S capsule ready

Status: `HANDOFF_READY / CANDIDATE2_FROZEN / ISSUE137_INTERFACE_ABORTED / ISOLATED_A-S_CAPSULE_READY / A-P_WITHHELD / NOT_CURRENT`

## Current

`v0.3.6 / CURRENT / FIELD_VALIDATION`

## Frozen candidate.2

- source `bda470e0a6b170cec61225a905957a501454a2fe`
- subtree `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`
- exact pre-freeze run `33095987843` — PASS
- immutable in place; material byte correction requires candidate.3.

## What invalidated the previous intake

Issue #137 is historical only. A fresh reviewer correctly aborted before A-S seal because normal GitHub README rendering crossed the declared blind boundary.

That was a validation-interface defect, not a candidate verdict.

Incident:
`research/methodology/incidents/2026-08-28-CANDIDATE2-GITHUB-NATURAL-NAVIGATION-PRIMING-INCIDENT.md`

## Active independent-validation carrier

A-S is no longer conducted through repository browsing.

Canonical carrier method:
`research/methodology/INDEPENDENT-VALIDATION-CAPSULE-CARRIER.md`

Build/audit run:
`33131665994` — SUCCESS

A-S capsule SHA-256:
`ee80ac827dedff7a8de9d10f0a9cbcd70c66f3b7b885296f9e2335af6ec92131`

A-P supplement SHA-256:
`b3e2222c591a2760b976e6791f18e2494c17063ddfe539291f1cd8799fd54bcd`

GitHub Actions artifact id:
`9670480727`

Outer artifact digest:
`104005b329cc042721da76a38f8a41c282c278bca3d2c424ecd7288ceeb1c357`

## Exact next action

Give a genuinely fresh reviewer **only** the A-S capsule and its expected hash. Do not provide the project repository as review material and do not provide the A-P supplement yet.

The reviewer reads `INTAKE-A-S.md` inside the capsule, performs A-S, writes `candidate2-independent-a-s-primary-r3.md`, computes SHA-256 of that exact completed report, reports the digest, and stops.

After the project manager verifies/persists the report + digest, separately give the same reviewer the A-P supplement. After A-P, stop before Phase B.

`ATTACK_CARDINALITY = OPEN`
