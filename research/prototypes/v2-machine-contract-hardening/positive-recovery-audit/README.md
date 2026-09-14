# Positive-recovery audit — were five legitimate positives really sacrificed?

**Status: RESEARCH — correction of two inbox claims. Nothing here promotes, retires or changes a
contract. `releases/current/` and the frozen v2.3/v2.4 candidates are read-only inputs.**

Date: 2026-09-14. Trigger: an external reviewer asked for the five sacrificed positives to be named
at fixture level rather than as an aggregate `14/19`, and two inbox notes
(`CONTRACT-SURFACE-BUDGET-AND-ADOPTION-TAX.md` §6b,
`OLD-LINE-SALVAGE-AUDIT-2026-09-14.md` §7) were checked while answering.

## What was claimed

```text
v2.2 (2026-08-20)  TOTAL_POSITIVE_PRESERVED 14/19.
                   The five failures are "the intended cost of ... not a contract bug"
                   (P1, P5, P6 BLOCKED; P7, P9 UNKNOWN).
v2.3               Same five fixtures, same `kind: POSITIVE`, but `expected_verdict` re-authored to
                   BLOCK (3) / UNKNOWN (2); the positive-preservation metric was replaced by
                   per-category verdict correctness.
v2.4 / v2.4.1      All five reported `preserved: True` — against the re-authored expectation.
Shipped corpus     releases/current/tools/contract-fixtures.v2.json still carries all five as
                   `kind: POSITIVE`, `provenance: DSH_HISTORICAL_V2`, with no expected verdict.
```

Two inbox notes then asserted that **an independent round classified three of the five as
`CONFIRMED_MATERIAL_DEFECT` (false BLOCK) and fixed them**. That assertion is false. The v2.4
reconciliation adjudicated its own independently authored corpus (`I01`–`I16`, `O01`–`O04`,
plus composition failures `CF-1..3` and an oracle challenge); a repository-wide search finds the five
ids **only** in the v2.2/v2.3/v2.4/v2.4.1 result files, the v2.3 manifest, the prototype fixture
module and the shipped corpus. No independent round ever examined them. The claim was a
misattribution between two different sets of fixtures — its own kind of unaudited cost claim.

## What was measured

`recovery_probe.py` (this directory, receipt in `recovery.json`). Hypothesis: each of the five
references an artifact its own payload never supplies, so supplying exactly the artifacts those
references name should make it pass. Falsification criteria are stated in the module docstring
before the results.

```text
fixture                                as-is                        completed
P1-supported-with-refs                 BLOCK SUPPORT_REF_UNRESOLVABLE      OK
P5-completion-satisfied                BLOCK SUPPORT_REF_UNRESOLVABLE      OK
P6-nonmaterial-obligation-ok           BLOCK SUPPORT_REF_UNRESOLVABLE      OK
P7-recovery-with-history-evidence      UNKNOWN PROVENANCE_REGISTRY_UNAVAILABLE  OK
P9-independence-distinct-roots         UNKNOWN ROOT_REGISTRY_UNAVAILABLE   OK

negative control (P1's supplied support bound to another claim)  BLOCK SUPPORT_TARGET_MISMATCH
```

* **F1** — the as-is control reproduces the recorded `3x BLOCK + 2x UNKNOWN`, so the harness is
  evaluating the frozen corpus.
* **F2** — every completed variant is accepted, with no field edited, removed or re-typed
  (structural check, machine-run).
* **F4** — the negative control still blocks with `SUPPORT_TARGET_MISMATCH`, so the acceptance comes
  from *resolving* the references, not from the mere presence of a registry.

## What this changes

1. **The adoption cost of the tightening was overstated.** The composed contract never refused those
   five legitimate cases. It refused five *incomplete payloads*: a SUPPORTED claim whose support
   relation, obligation-closure evidence or root registry the fixture never supplied. That is the
   documented intent — "missing registries must not silently degrade into trusting raw strings" —
   working as designed. The measurable loss is five *passing fixtures*, not five legitimate cases.
2. **The metric changed meaning without saying so.** After v2.3, `preserved: True` compares against an
   expectation authored *after* the outcome was known. Keeping `kind: POSITIVE` while writing
   `expected_verdict: BLOCK` leaves a fixture that is labelled a positive control and is scored as an
   adversarial one. That is how an untested cost claim became, two rounds later, evidence.
3. **Item four's obligation survives, with a second failure mode.** The first is *asserting* a cost
   instead of reproducing it. The second, measured here, is *encoding* the assertion as an
   expectation and letting later rounds inherit it as a preservation result. Both are satisfied by
   the same procedure: reproduce the claimed cost against the case as the claimant describes it,
   before it counts.

## Residual questions (not answered here)

* Whether an adopter can always *supply* the registries a legitimate positive requires — a
  maintenance burden, unmeasured, and the only part of v2.2's cost claim this probe does not retire.
* The five fixtures remain incomplete in the shipped corpus. Completing them is a change to a
  shipped artifact surface and is **not** proposed here.
* Whether the `kind: POSITIVE` label should be split from the expected verdict in the corpus schema,
  so that "this case should pass" cannot be silently re-authored into "this case should block".
