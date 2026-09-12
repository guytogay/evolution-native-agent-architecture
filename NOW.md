# ENA — NOW

This is maintainer/project status, not adopter/runtime content.

## Legacy Current

- repository: `guytogay/evolution-native-agent-architecture`
- state: `v0.3.14 / CURRENT / FIELD_VALIDATION`
- identity authority: `releases/current/CURRENT-BASELINE.yaml`
- effective package: `releases/current/`
- field stream: Issue `#208`

Legacy Current is unchanged.

## Clean product home

Repository: `guytogay/ENA`

State: `RELEASED_v1.0.0 / NOT_CURRENT / NOT_PROMOTED`

Release identity (stable fact): `v1.0.0` tag -> `ea8a313`

Current ENA `main` head: **read it from the ENA repository** (`guytogay/ENA`, branch `main`). It is
deliberately not copied here: a copied commit id becomes a drift source the moment the product
moves, and this file previously carried a stale one for that reason.

Promotion semantics (identity semantics of this repository, not a temporary note):

```text
PRODUCT RELEASE != CURRENT PROMOTION
guytogay/ENA v1.0.0 = RELEASED CLEAN PRODUCT
research Current    = v0.3.14 / FIELD_VALIDATION
Current changes only through an explicit USER promotion decision.
Publishing or tagging guytogay/ENA does not mutate releases/current/.
```

Adopter path:

`FIRST-USE.md -> A2A.md -> SURVIVAL.md -> SAFE-CHANGE.md -> EVOLUTION.md -> SLEEP-DREAM-QUICKSTART.md`

## Real-host minimum runtime chain

ENA Issue #14 is closed as completed against its original acceptance criteria.

Real Linux session-Host evidence now includes:

- First Use with real `ENA.yaml`, non-empty `SYSTEM.yaml`, explicit UNKNOWNs, recovery path and human rescuer;
- one non-trivial live SAFE-CHANGE through the executable state gate;
- `preparing -> armed -> applied -> retained` with evidence `validation-7a0a1dd2f957`;
- a genuinely new session continuing from persisted ENA/system/change/evolution state without chat reconstruction.

Boundaries remain explicit: the Host lacks a universal native session-start hook, and a live destructive restore was not executed. Those are follow-up field limits, not retroactive Issue #14 acceptance criteria.

Detailed evidence:

`research/status-notes/2026-09-12-real-host-minimum-chain.md`

## Real-use corrections

Real DSH adoption found and corrected concrete defects including timezone portability, Dream/Sleep provenance, missing-input boundaries, SAFE-CHANGE state semantics, candidate overwrite, candidate canonical-time handling, and repository hygiene coverage.

Product PR #28 made candidate artifacts collision-safe and canonical-time based at the time of that correction; the commit id is intentionally not repeated here, since the product has moved on and this file should not carry a second copy of its head.

## Sleep/Dream field state

ENA Issue #12 remains open.

Two real Hosts have run Dream against non-toy material. One Linux Dream-origin `prereg.py` candidate survived bounded reality contact and can detect evaluation-pair mismatch and post-hoc rubric mutation.

Current disposition:

`HOST_LOCAL_SELECTED / MECHANISM_VERIFIED / MARGINAL_FIELD_VALUE_NOT_YET_PROVEN`

The next evidence question is whether a Dream-origin candidate changes a real future decision or outcome compared with ordinary reasoning. Null and negative outcomes remain valid evidence.

## Field-discovered configuration debt

RESOLVED. ENA Issue #29 (closed 2026-09-12) recorded that `ENA.yaml` and `SYSTEM.yaml` overlapped on recovery / communication facts. The authority split was implemented in the clean product (PR #36) and verified on a real Host:

- `ENA.yaml`: stable configuration and stable pointers;
- `SYSTEM.yaml`: mutable Host/runtime facts with freshness state.

No third truth surface was introduced, and a moved/copied legacy home now fails closed instead of writing back into its previous location (PR #46).

## Repository-governance debt

RESOLVED. ENA Issue #26 (closed 2026-09-12) required repository-admin protection for `main`. Protection is in place and verified: pull requests required, the `Reference tools` checks required on both platforms, force pushes and deletions blocked, `enforce_admins=false`, branch deletion on merge enabled.

## Evidence state

The clean product now has a completed minimum real-host runtime-chain occurrence. This is stronger than CI/sandbox evidence but is not broad/general field validation: Host count is small, live restore is not executed, and Sleep/Dream marginal value is unresolved.

## Product boundary

Still binding:

- ENA adds missing runtime capabilities rather than rebuilding ordinary model judgment;
- reading or summarizing docs is not installation;
- human recovery is valid and A2A is not universal;
- resident and session Hosts may use different recovery paths;
- critical live change preserves previous working state and prepared recovery;
- deterministic checks prove only measured properties;
- Dream output stays speculative until reality contact;
- selected does not mean production-applied;
- advertised/discoverable capability is not verified live capability;
- negative/null results and repair trajectories are evidence;
- concrete execution findings outrank additional speculative mechanisms.

## Succession

Mandatory deep-succession record remains:

`research/handoffs/records/2026-09-07-v040-clean-product-home/`

A deep successor reads `CONSENSUS-LOCK.md`, then applies newer live state from this file and `research/handoffs/CURRENT-HANDOFF.yaml`.

Repository roles:

- `guytogay/ENA` — clean product home;
- `guytogay/evolution-native-agent-architecture` — legacy Current + research/evidence/history + succession;
- `guytogay/human-ai-workbench` — general human-AI project-working method;
- `guytogay/ena-field-guide` — sunset independent product, preserve useful evidence.

## Immediate next action

`MEASURE_SLEEP_DREAM_MARGINAL_VALUE_AND_RESOLVE_LIVE_FACT_AUTHORITY`

Priority:

1. continue Issue #12 through natural real work and record whether Dream-origin candidates change later decisions/outcomes;
2. ~~design a compatibility-safe resolution for Issue #29~~ — done 2026-09-12 (closed; see *Field-discovered configuration debt* above);
3. ~~owner/admin completes Issue #26 branch protection~~ — done 2026-09-12 (closed; see *Repository-governance debt* above);
4. collect additional recovery/restore evidence only when a safe natural opportunity occurs;
5. add new mechanisms only when concrete field evidence requires them.

Operational queue for the clean product itself lives with the product, not here: see the ENA
coordination issue (product repository, issue #34) for the current work item list, so this file does
not keep a second copy of it.
