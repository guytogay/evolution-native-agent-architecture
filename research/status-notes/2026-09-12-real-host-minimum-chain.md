# 2026-09-12 — clean ENA real-host minimum runtime chain

Status: FIELD_EVIDENCE_MILESTONE / CLEAN_PRODUCT_ONLY / LEGACY_CURRENT_UNCHANGED

## Product home

Repository: `guytogay/ENA`

Latest clean-product main commit at this milestone:

`703b6e8847c389aeeb6fec42eb088d9ba58e8376`

The clean product remains `ACTIVE_DEVELOPMENT / NOT_CURRENT / NOT_PROMOTED`.

## Issue #14 adjudication

ENA Issue #14 (`Fresh-Agent field trial: prove the minimum runtime chain`) is closed as completed against its original acceptance criteria.

Real Linux session-Host evidence now covers:

1. First Use with real `ENA.yaml`, non-empty `SYSTEM.yaml`, explicit UNKNOWNs, a verified Host-appropriate recovery path and human rescuer.
2. One non-trivial live SAFE-CHANGE: a session-start gate, snapshot/verify wrapper, vendored preflight and crontab repointing were applied through the executable state gate.
3. SAFE-CHANGE transitions reached `preparing -> armed -> applied -> retained`; unresolved recovery fields and retain-without-evidence were actually rejected.
4. The retained result has explicit validation evidence (`validation-7a0a1dd2f957`).
5. A genuinely new headless session, without chat history, reconstructed the recovery path, retained change, evidence reference, rollback facts and important limitations from persisted disk state.

Important boundaries preserved:

- the Host does not expose a native universal session-start hook; the hard preflight gate applies to sessions routed through the wrapper, not all web-GUI sessions;
- live destructive restore has not been performed; evidence is prepared recovery plus dry-run/no-diff verification, not a claim of full restore execution;
- those are follow-up field boundaries, not retroactive acceptance criteria for Issue #14.

A separate Windows session Host also completed real First Use, routed ENA preflight through its session bootstrap, ran real Sleep/Dream material, and exposed candidate-artifact defects that were fixed in product PR #28.

## Candidate output defects found by real Dream use

A real Windows Dream run produced four candidates but only two artifacts survived because `candidate_record.py` used second-resolution filenames and unconditional overwrite. The same tool used Host local timezone rather than the ENA canonical timezone.

Product PR #28 / main `703b6e8847c389aeeb6fec42eb088d9ba58e8376` corrected both:

- candidate timestamps use `ENA.yaml` canonical timezone;
- filenames include microseconds plus a candidate UUID;
- writes use exclusive create, so a collision fails closed rather than overwriting;
- an uninitialized ENA home is rejected;
- regression tests prove rapid candidate preservation and canonical-time independence from Host `TZ` on Linux and Windows.

## Real recovery-verification value

First Use on the Linux Host exposed that an existing rescue snapshot job had silently degraded for several nights after an unreadable root-owned file entered the snapshot tree. The existing job could terminate before permission hardening / integrity checks and leave partial archives without surfacing the degradation.

The Host-local recovery mechanism was repaired and negative-tested. This is direct evidence that the existing First Use / SURVIVAL requirement to verify recovery facts has operational value. It is not a new ENA capability by itself.

## Sleep/Dream field state

Issue #12 remains open.

Two real Hosts have now run Dream against non-toy material. One Linux run produced a Dream-origin `prereg.py` candidate from a cross-domain link between distributed-system submission ambiguity and evaluation-rubric drift. Bounded reality contact showed that the candidate could detect a mismatch between a frozen comparison pair and later reporting, and detect post-hoc rubric mutation.

The candidate is therefore a Host-local `selected` candidate with this boundary:

`MECHANISM_VERIFIED / MARGINAL_FIELD_VALUE_NOT_YET_PROVEN`

Do not promote `prereg.py` into ENA product capability yet. The next useful evidence is whether a Dream-origin candidate changes a real future decision/outcome compared with what the Agent would otherwise have done, including null and negative results.

## New field-discovered design debt

ENA Issue #29 tracks a duplicated-truth problem between `ENA.yaml` and `SYSTEM.yaml`.

Current examples/generator expose recovery / communication facts in both files even though First Use says `ENA.yaml` should hold confirmed settings and stable pointers while `SYSTEM.yaml` is the refreshed live system map with `checked_at` / `valid_until`.

Target direction:

- `ENA.yaml`: stable configuration and pointers;
- `SYSTEM.yaml`: mutable Host/runtime facts that can drift and require freshness state.

Do not simply delete fields from current adopters. Define compatibility/precedence and migration first.

## Repository-governance debt

ENA Issue #26 remains open: `main` still needs repository-admin protection requiring PRs and the Reference tools status check. Repository-internal hygiene guards exist, but they do not substitute for GitHub branch protection.

## Project consequence

The clean product is no longer merely `READY_FOR_REAL_HOST_FIELD_TRIAL`; it now has a completed minimum real-host runtime-chain occurrence.

Do not describe the entire product as generally field validated yet. Evidence is still narrow in Host count and Sleep/Dream marginal value remains unproven.

Immediate product work should now prioritize:

1. natural real-world Sleep/Dream value evidence through Issue #12;
2. compatibility-safe resolution of Issue #29 live-fact authority;
3. repository-admin completion of Issue #26;
4. additional live-restore evidence only when a safe/natural opportunity exists, not by manufacturing destructive experiments;
5. no new mechanisms merely because another review can imagine them.
