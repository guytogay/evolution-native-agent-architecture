# ENA Research — Start Here

Status: `ACTIVE_RESEARCH_BOOTSTRAP / HOT_ENTRYPOINT / V0_3_7_PREPROMOTION_RELEASE_READINESS / NOT_RELEASE_AUTHORITY`

The canonical control plane lives on `main`. This active-branch bootstrap accelerates continuation but does not override Current or exact frozen/release identities.

## Project-manager continuation order

Before substantive work:

1. start from `main` and read `PROJECT-HUB.md`;
2. verify Current from `releases/current/CURRENT-BASELINE.yaml`;
3. read `research/handoffs/CURRENT-HANDOFF.yaml` and the canonical handoff framework;
4. read the current handoff record named by the pointer;
5. read required methodology under `research/methodology/`;
6. read `research/ACTIVE-RESEARCH.yaml`;
7. if current surfaces disagree, complete the Project State Alignment Gate;
8. read `research/plans/PROGRESS.yaml` and the master plan;
9. reverify live mutable refs and exact governed identities before writes.

A fresh independent validator is a different epistemic role and must not be sent through this full project-manager context before A-S seal.

## Current posture — 2026-08-28 pre-promotion

```text
Current = v0.3.6 / CURRENT / FIELD_VALIDATION
Current tree = 7dcbb3934883ffa6cc5292a662588cafc1533cff
```

Final frozen candidate:

```text
v0.3.7-candidate.3
source  = b7e88d7adb70396bd671ca97066daf2c120e0adc
subtree = e3a9a20d16cecd78df7f32f19fca56e21159e810
exact pre-freeze      = 33150269264 PASS
targeted post-freeze  = 33150553992 PASS
release hardening     = 33152201566 PASS
candidate succession  = STOP
candidate.4           = not justified by current evidence
```

Prospective v0.3.7 release state:

```text
release branch                  = release/v0.3.7
release PR                      = #144 / OPEN DRAFT / NOT PROMOTED
byte-exact transplant head      = 8e4e25a8ba1940560fc55d7528ad31ef89a7f135
prospective Current tree        = f33e73ed997c1b66a4572685ab5474182e136e97
exact validated release head    = bcda18a28141f572688f9a1b15cfd820dea02f97
prospective Current file count  = 118
package SHA-256                 = 40d4dde277d54ce8252e0402e32f900fa7ab4fb0aeaa638b898073d0f02f848c
Exact Release Gate              = 33161514271 PASS
Current validate/package        = 33161516641 PASS
Main Gate                       = 33161516581 PASS
Selection Qualification         = 33161516591 PASS
research helper                 = 33161516586 PASS
CodeQL                          = 33161516568 PASS
promotion                       = not authorized
```

The prospective release payload is release-ready in the bounded sense represented by those checks, but it is **not Current** until explicit authorization, merge, and post-merge readback.

## Main-visible alignment

The pre-promotion Project State Alignment checkpoint has been merged to `main` at:

`f5e031cd28b2f3fd3d697159b295b24e91e2820e`

That alignment records:

- release readiness without premature promotion;
- exact release tree/package/run evidence;
- Selection Qualification oracle drift as control failure rather than candidate defect;
- Exact Release Gate execution on every release-branch push;
- issue disposition for #70, #89-#94, and #104;
- branch lifecycle/cleanup disposition and the current lack of a true delete-ref connector action.

## Immediate next action

```text
sync aligned main into release/v0.3.7
-> rerun Exact Release Gate and ordinary PR checks on the resulting exact release head
-> verify prospective Current tree and deterministic package digest remain stable
-> present exact reviewed head + open evidence boundaries
-> obtain explicit promotion authorization
```

Only after explicit promotion authorization may PR #144 merge.

Post-promotion:

```text
merge
-> read back Current from main
-> align PROJECT-METADATA/history/field-validation issue routing
-> close release/candidate/temporary branch lifecycles when safe
-> update handoff/control surfaces
-> run Project State Alignment Gate again
```

Do not modify frozen candidate.3. Candidate.4 requires new material candidate-byte evidence; it is not a ritual next generation.

## Issue and branch reminder

Open research issues are durable work obligations, not a cleanliness score. Short-lived branch names are lifecycle surfaces, not archives. Preserve lineage first, then remove obsolete refs when their lifecycle closes. The currently available connector lacks genuine branch/ref deletion, so do not simulate deletion through force-moves.

## Method reminders

```text
WHAT / WHY -> abstraction may help
HOW -> concretize / branch / recombine
FAILURE SPACE -> remain open while materially distinct shapes remain plausible
PROVEN REPRESENTATION DUPLICATION -> may compress
```

```text
PROPERTY != ORGAN != HOST_BINDING != EVIDENCE != ADOPTION
COMPRESS REPRESENTATION != COMPRESS POSSIBILITY SPACE
RELEASE_READY != CURRENT
GREEN_GATE != PROMOTION_AUTHORITY
```

## Reusable independent-validation infrastructure

`guytogay/independent-validation-cleanroom` is a reusable clean-room facility across ENA stages and across unrelated projects. Repository identity is infrastructure; stage contents are ephemeral. Reports/seals/occurrence truth return to the relevant source project.

## Record-first continuity

After material progress, update fast Progress, reconcile stale control surfaces, persist decision/evidence records, and update succession context when needed. A file being durable is not enough if future sessions cannot discover or correctly apply it.

> Inherit state, method, governance, decision lineage, open uncertainty, and the exact next permitted action — while giving each epistemic role only the context it should receive.
