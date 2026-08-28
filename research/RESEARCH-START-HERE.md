# ENA Research — Start Here

Status: `ACTIVE_RESEARCH_BOOTSTRAP / HOT_ENTRYPOINT / V0_3_7_RELEASE_PACKAGING / NOT_RELEASE_AUTHORITY`

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

## Current posture — 2026-08-28

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
release preparation   = SUPPORTED
```

Release packaging live state:

```text
main checkpoint            = 280a8b0f7629d5deb013a5257cb74759213e8080
release branch             = release/v0.3.7
byte-exact transplant head = 8e4e25a8ba1940560fc55d7528ad31ef89a7f135
transplanted tree          = e3a9a20d16cecd78df7f32f19fca56e21159e810
identity/status transform  = pending
release PR                 = not open
promotion                  = not authorized
```

The transplant is intentionally candidate-shaped and is preserved as a separately auditable occurrence.

## Immediate next action

The current project-management step is to complete and merge the Project State Alignment checkpoint. After that:

`RELEASE_IDENTITY_STATUS_PACKAGING_ON_RELEASE_V0_3_7`

Then:

```text
identity/status-only projection
-> exact release gates / Main Gate / CodeQL / regressions
-> package/tree/readback evidence
-> exact-head release PR review
-> explicit authorization
-> merge
-> post-merge Current readback
-> history/control/handoff alignment
```

Do not modify frozen candidate.3. Candidate.4 requires new material candidate-byte evidence; it is not a ritual next generation.

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
```

## Reusable independent-validation infrastructure

`guytogay/independent-validation-cleanroom` is a reusable clean-room facility across ENA stages and across unrelated projects. Repository identity is infrastructure; stage contents are ephemeral. Reports/seals/occurrence truth return to the relevant source project.

## Record-first continuity

After material progress, update fast Progress, reconcile stale control surfaces, persist decision/evidence records, and update succession context when needed. A file being durable is not enough if future sessions cannot discover or correctly apply it.

> Inherit state, method, governance, decision lineage, open uncertainty, and the exact next permitted action — while giving each epistemic role only the context it should receive.
