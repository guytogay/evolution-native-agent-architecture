# Divergent Explorer — adoption gap and landing note

Status: `RESEARCH_METHOD_NOTE / VARIATION_HALF / ADOPTION_DECISION_OPEN`
Date: 2026-09-15
Companion text (verbatim, not a method rule): `DIVERGENT-EXPLORER-METHODOLOGY.md`

## 1. What this note is about

The owner wrote, in his own words, that a divergent-exploration methodology was produced for him
and that he had asked for it to be put into ENA as the mechanism that **produces variation on the
way to evolution** — and that it was then forgotten. This note records what checking turned up,
because "forgotten intent" is exactly the kind of thing that leaves an artefact claiming something
that is not true.

## 2. What checking found: a declared-but-absent mechanism

| Surface | What is actually there |
| --- | --- |
| `guytogay/ENA` product, `SLEEP-DREAM.md` | A section titled **Divergent exploration** with **eight lines**: seek remote structural similarities, combine mechanisms across memories/knowledge, reverse roles/assumptions/causal direction, transfer a mechanism across domains, combine a problem with a capability, change constraints counterfactually, follow a strange connection longer than normal retrieval, produce multiple variants. That is the whole shipped surface. |
| `guytogay/ENA` product, anywhere else | Nothing: no mutation operators, no exploration graph, no branch state, no novelty test, no scheduler, no stop rule. |
| `research/status-notes/2026-09-12-sleep-dream-v01.md` (this repository) | States that the clean v0.1 Sleep/Dream design uses **"the owner's Divergent Explorer pattern as the main Dream variation operator"**. |
| Host substrate (`vary.ps1`, `dream.ps1`, `govern.ps1`) | A variation generator that produces a signature and refuses exact repeats of known failures or existing proposals. Real, but far thinner than the pattern the status note names. |

So the repository claims the pattern **is** the main variation operator, while the thing that
exists is an eight-line summary of it. `DECLARED != ACTUAL`, in our own artefacts, on the exact
axis the owner cares about. Two honest ways out: land the pattern, or correct the claim. This note
is the second, immediately, and the first is a decision recorded in §5.

## 3. Why the methodology is not foreign to ENA

Reading it end to end, it is the **variation half of the loop ENA already names** — and it says
several things ENA says, in different words:

| Divergent Explorer | Already ENA vocabulary |
| --- | --- |
| "Surprise selects candidates. Evidence selects beliefs." | candidate ≠ reality contact; stored/expressed/applied are distinct |
| EXPLORER generates, CHALLENGER tries to kill; roles must not merge | generation and validation are separate; an author's own tests are not verification |
| Failed branches are kept as negative knowledge | negative evidence is not deleted |
| Structural novelty over semantic novelty; paraphrase collapse test | "changing the words is not a new discovery" |
| Falsifiability gradient F0–F5, maturity D0–D7 | explicit epistemic status enums instead of confident prose |
| Baseline comparison, complexity tax, ablation test, protocol pruning | a mechanism must pay rent; what does this retire |
| PARK / STOP / META_STOP are legitimate | dormancy and retirement are first-class; stopping is a legal move |
| Memory-blind pass before the memory pass | do not force every new thing into the old theory |
| Independent first output; consensus is not truth | independent verification by a differently-situated party |
| Frame lock → FRAME_ESCAPE; explorer bias | the method itself is subject to observation |

Its own conclusion is the most useful part for adoption: after ablation the author expects the
**minimal effective core** to be seven items — mechanism-first abstraction, structural search,
mutation operators, novelty detection, adversarial challenge, memory-blind inheritance, and stop
discipline — and says outright that if seven suffice, the remaining ritual should not be kept.

That matters because it means adopting this does **not** mean importing 113 sections into an
adopter-facing surface. The text is a reference; the core is small.

## 4. What was done here, and what was deliberately not done

Done (project-research surface only, no adopter contract change, no host mechanism change):

- the methodology is landed verbatim with provenance;
- this note records the gap between the status note's claim and the shipped surface;
- the method changelog records why.

Deliberately not done, with reasons — these are the parts that need authority this note does not
have:

1. **Product surface** (`SLEEP-DREAM.md` and friends). Adding the operators, the graph, the
   scheduler or the stop rules there is an adopter-facing contract change: our own budget rule
   requires a field failure on a real Host, reproducible evidence, a named thing it retires, and a
   stated cost to legitimate positives, with that cost independently reproduced. We do not have
   that evidence; what we have is an owner intent. Product surface is also written upstream, not
   by the execution side.
2. **Host mechanism** (`vary.ps1` operator set, a variation record, a frontier/state file). This is
   a mutation of the mechanism itself, which the iron rules lock behind a USER meta-write lease,
   an audit review, a ≥300 s observation window and a self-check. A concrete option is prepared in
   §5 rather than applied.
3. **Measuring it.** Any claim that these operators produce better variation needs a benchmark arm
   against the current thin version, i.e. the thing the methodology itself demands (§90–§98). No
   such measurement exists yet, and saying "this is better" without it would be the exact failure
   the text warns about.

## 5. The decision that is open

Three routes, ordered from cheapest to most consequential:

**A. Reference only (this note).** The methodology lives in the theory repository as research
material; the product keeps its eight-line version. Cost: zero. Limit: the variation half stays
thin, and the status note's claim stays corrected rather than fulfilled.

**B. Host mechanism (needs a USER meta-write lease).** Give the host's variation step the
methodology's *minimal core*: the mutation-operator set as named, explicitly chosen operators
(SCALE_SHIFT, TIME_SHIFT, ACTOR_SWAP, CAUSE_REVERSAL, EXTREME_CASE, FAILURE_MODE,
FUNCTION_INVERSION, MISSING_THIRD, BOUNDARY_SHIFT, REPRESENTATION_SHIFT, AGENCY_SHIFT,
SELECTION_PRESSURE); a branch/frontier state file with `ACTIVE/PARKED/EXHAUSTED/REJECTED/MERGED`
and a recorded reason for every park; novelty detection against existing proposals and known
failures (the generator already refuses exact repeats — this would extend it from "same signature"
to "same structure"); and an explicit stop rule. Then measure by ablation, as the text itself
demands. This is the route that actually delivers "a mechanism that produces variation", and it is
the route that needs the owner's meta-write lease.

**C. Product surface (needs an upstream ruling plus a budget slot).** Promote the minimal core into
the adopter-facing Sleep/Dream surface, ideally as an optional reference rather than hot-path
prose, and only with field evidence that the thin version fails. Highest cost, highest reach.

Recommendation: **B**, because it is where "produces variation" is actually true, it is measurable
by ablation, and it does not enlarge the adopter contract while we lack field evidence for that.
A stays in place regardless; C waits for evidence.

## 6. Boundary of this note

It asserts only what was read: one owner-provided file, the two product surfaces and one status
note named above, and the host's variation scripts as they exist on 2026-09-15. It does not claim
the methodology is original, nor that adopting any part of it improves outcomes — that is what the
benchmark in §5 would have to show.
