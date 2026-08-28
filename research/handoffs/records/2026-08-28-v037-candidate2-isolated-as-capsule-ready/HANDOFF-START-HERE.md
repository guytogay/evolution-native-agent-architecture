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
`33131773164` — SUCCESS

A-S capsule SHA-256:
`dfe15a686668440138bfd624453059d61a0b28625bb9a5e0c185b33eccf9c2da`

A-P supplement SHA-256:
`427a1776aea199f5f27c4bea2827d3c827cf82fab2c8cd403da0e8cc1dd97649`

GitHub Actions artifact id:
`9670480727`

Outer artifact digest:
`A-S:146c15bed53826fe8cce4738540c471127bda7c15cf5616cd20387f7e3567def / A-P:d5b2b1d67f300c087d3d3869e4a93148a89d75cb5d3860025bb340bcdc6c65f2`

## Exact next action

Give a genuinely fresh reviewer **only** the A-S capsule and its expected hash. Do not provide the project repository as review material and do not provide the A-P supplement yet.

The reviewer reads `INTAKE-A-S.md` inside the capsule, performs A-S, writes `candidate2-independent-a-s-primary-r3.md`, computes SHA-256 of that exact completed report, reports the digest, and stops.

After the project manager verifies/persists the report + digest, separately give the same reviewer the A-P supplement. After A-P, stop before Phase B.

`ATTACK_CARDINALITY = OPEN`
