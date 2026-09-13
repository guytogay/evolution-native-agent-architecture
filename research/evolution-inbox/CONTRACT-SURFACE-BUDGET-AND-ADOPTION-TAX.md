# Contract-surface budget and adoption tax: why correctness pressure breeds latches, and what makes it stop

Status: `RESEARCH / NOT_PROMOTED` — a hypothesis with a measurement attached, not a control.
Date: 2026-09-13
Source: an external review of the clean product line by another model family, the owner's standing concern that the practical line gets pulled back into theory, and a controlled count over the release tags.

## 1. The observation

Two statements arrived from different directions on the same day and describe one mechanism:

- **External review**: "correctness is regrowing into a cathedral" — the five-field actor block, the UNKNOWN lifecycle, the rescue declarations, the YAML subset, exit codes, upgrade guidance, release gates: each has a field reason, and together they are an **adoption tax**. The reviewer's prescription was not "remove things" but "restrain the **breeding rate of latches**".
- **Owner**: the previous line drifted into being a theory/governance artefact rather than something useful, and repeated instruction has not held that drift back.

Both describe a **ratchet**: every addition is locally justified, so the aggregate moves without anyone ever voting for the aggregate.

## 2. The distinction that makes it measurable

"The product is getting bigger" is argued with file counts, and file counts conflate two opposite things:

```text
ADOPTER CONTRACT SURFACE   what a real adopter must read, declare, migrate or handle.
                           Growth here is a tax on adoption.
INTERNAL VERIFICATION SURFACE
                           tests, CI steps, probes. Growth here costs an adopter nothing
                           and makes the product safer to adopt.
META / PRACTICAL prose     why the system is shaped this way, versus what to do in order.
```

If the two surfaces are not separated, the natural corrective action is wrong in a specific and damaging way: a team told "the product is too complex" will eventually delete tests, because tests are the biggest legible pile. The reviewer's own numbers show the trap — "about 10 scripts to 30+" — when the measured movement is **+6 product tools and +8 regression tests**.

## 3. Why the ratchet turns even with good intentions

A selection argument, offered as a hypothesis rather than a law:

- **Additions are legible, removals are invisible.** A new required field shows up in a diff and answers an objection; the field it makes unnecessary shows up nowhere.
- **Correctness claims cannot be falsified quickly.** "This could prevent a bad case" survives review indefinitely; "we did not need this" requires field evidence that usually has not been collected.
- **A defect produces an artifact; restraint produces nothing.** The reviewer who demands a fix has a case to point at. The maintainer who declines to add a latch has only an argument.
- **Instructions do not bind; asymmetries do.** Telling a contributor "be restrained" loses to any concrete proposal with a plausible failure story. A rule that prices the addition changes the outcome without changing anyone's disposition.

If that is right, then the drift is not a defect of a particular model's character. Any agent optimizing for correctness and robustness under review will accumulate latches, because latches are what review can see.

## 4. The measurable form

`theory-drift-census.py` (published in the external audit repository, deliberately outside the product) counts, per revision: adopter-facing documents, upgrade command blocks, versioned machine contracts, documented exit codes, breaking/migration items, META and PRACTICAL prose words and their ratio, plus test files and non-test tools as the internal/product split.

First reading, v1.0.0 → v2.0.0 (19.6 hours apart, 11 commits):

| measure | v1.0.0 | v2.0.0 |
| --- | --- | --- |
| upgrade command blocks | 0 | 8 |
| versioned machine contracts | 0 | 1 |
| documented exit codes | 0 | 5 |
| breaking / migration items | 0 | 5 |
| META prose words | 4,372 | 6,317 |
| PRACTICAL prose words | 5,590 | 7,770 |
| META / PRACTICAL ratio | 0.782 | 0.813 |
| test files / non-test tools | 14 / 18 | 22 / 24 |

Honest reading: **the theory takeover is not visible yet** — PRACTICAL grew slightly more than META and the ratio moved 0.031. The tax is concentrated instead in the contract surface: five breaking migrations in under a day.

A caveat about the instrument itself, kept because it is the same failure the product fights: the first version of this census had two broken measures — a required-field counter that read zero everywhere, and a context-window regex that over-counted breaking items as 11 against a true 5. Both were fixed before any number was published. **A ruler that lies is worse than no ruler.**

## 5. The anti-ratchet mechanism

Applies to the contract surface only:

```text
1. Default budget for new adopter contract items per release: ZERO.
2. An addition is verified only if the proposer names all four:
     a. the FIELD FAILURE it prevents, observed on a real host;
     b. evidence for that failure, reproducible by someone who does not trust the author;
     c. what it RETIRES or replaces - one in, one out - or an explicit statement of why
        the surface may still grow;
     d. which LEGITIMATE positive cases it costs - the V2.2 precedent shows this is
        not hypothetical (14/19 preserved), and no adversarial scoreboard shows it.
3. Removals require none of the above and are fast-tracked.
4. The internal verification surface has no budget. Never delete a test to look simpler.
5. META prose growth in a release requires at least matching PRACTICAL growth.
```

Where it lives matters as much as what it says: **not in the product**. Adding a governance document in order to stop governance drift is the joke telling itself, and any such document becomes one more latch. The rule lives in the coordination channel and binds through the verifier who signs off, because that is the only place where "addition costs three named items, removal costs nothing" is a fact rather than advice.

## 6. Precedent already in this repository, including its measured cost

The anti-ratchet rule is not a new principle invented for this note. The machine-contract hardening
line in `research/prototypes/v2-machine-contract-hardening/` (2026-08-20, baseline v0.3.2,
`UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED`) already stated the correct success criterion in its own
words:

> Success is not "more validation rules." Success is the cheapest machine contract that refuses to
> endorse a material false claim while preserving viable agency.

That line is the budget rule in different vocabulary. What was missing was not the principle but any
**price** on violating it, which is why the same thread then accumulated three cumulative rounds
(V2, V2.1, V2.2) each adding protections.

The same records also contain the cost measurement that this note otherwise only predicts. In V2.2's
cumulative replay:

```text
TOTAL_ADVERSARIAL_BLOCKED    29 / 29
TOTAL_POSITIVE_PRESERVED     14 / 19
```

Five of nineteen legitimate positive cases did not survive the hardening. That is the adoption tax
in its purest measured form: protection gained on one axis, **legitimate capability lost on the
other**, and the loss is exactly the quantity that no adversarial scoreboard shows. Any contract
budget that does not require the proposer to name the preserved-positive cost is measuring half the
trade.

This also sharpens one of the open questions below: the retirement rate is not merely unmeasured, it
appears to be **zero** across that line, since V2.1 and V2.2 compose V2's protections rather than
replacing them.

## 6a. First retirement audit — a negative result, recorded as one

Since removals are the fast-tracked direction, the obvious move is to hunt for enforced surface that
nothing consumes. One was run on the two largest machine-enforced blocks of the shipped product:

```text
UNKNOWN lifecycle required metadata   state, reason, resolution_path, owner, revisit_by, last_attempt_at
durable-artifact actor block          executor, initiated_by, channel, correlation_id, attribution_confidence
```

**Result: zero retirement candidates. All eleven fields have consumers.** The decisive evidence is
logic, not counts: the validator parses `last_attempt_at` as an aware timestamp and rejects a
`revisit_by` that is not later than it; `reason` / `resolution_path` / `owner` are checked for
real non-placeholder values and filled from an initial-text table; the actor fields are parsed from
the environment, carried through a dataclass, and written into durable artifacts.

Two things about this result are worth more than the result itself:

- **The instrument was wrong first, and it produced a plausible finding.** The first census stripped
  every quoted literal before counting occurrences, on the assumption that quoted means
  human-readable message. Field names are quoted in code too (`.get("field")`), so real reads were
  classified as messages and `last_attempt_at` appeared to be required-but-never-read. It was
  required, and it was read three lines later. A negative result that had been accepted on the first
  reading would have retired a live cross-field check.
- **A clean negative is the honest outcome here.** It says the enforced surface is not rotted, and it
  means the retirement backlog is empty *with evidence* rather than by assumption. It does not
  contradict the ratchet hypothesis: the hypothesis is about the growth rate of enforcement, not
  about whether existing enforcement is dead weight.

The one genuine zero-consumer finding is adjacent and weaker: `memory.sources` and `change_surfaces`
are written into the initialized home and read by nothing. They are **not enforced** — no validator
requires them, no tool rejects their absence — so they are not a retirement target either, and there
is no field failure to justify touching them. Recorded as an observation.

## 7. Open questions this raises for ENA theory

- Is there a natural law here, or only a project-management heuristic? Candidate form: *a system under continuous correctness pressure accumulates enforcement surfaces unless removal is cheaper than addition.* If it is a law, it should hold for other lineages, not just this one.
- What is the **retirement rate** of ENA's own controls, historically? If controls are added and never retired, the ratchet is confirmed regardless of intent, and the interesting quantity is the ratio of additions to retirements over a lineage.
- Does "one in, one out" survive contact? It may be that some additions genuinely replace nothing — the budget then forces an explicit statement, which is still the useful outcome, but the rule's value is unmeasured.
- Is the META/PRACTICAL ratio a leading indicator at all, or a lagging one that only moves after the drift is already a fact? One release is not evidence either way.

## 8. Falsifiers

The concern is overstated if, across the next releases: the contract surface stays flat while shipped capability grows; retirements keep pace with additions; and the META/PRACTICAL ratio does not rise. The concern is confirmed if the contract surface keeps growing in the absence of any new real-host field failure.

## 9. Provenance

- Counts: `theory-drift-census.py` over tags `v1.0.0`, `v2.0.0`, `main` of `guytogay/ENA`, 2026-09-13; published in `guytogay/ena-independent-audit` and verified by a fresh clone reproducing the same table.
- The measured enforcement case that motivated the "no product-side gate" half of this note is recorded as `HAR-014`.
- The rule is held by the external verifier side; the raw receipts are in the clean product's coordination issue.
