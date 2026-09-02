# Negative Boundaries 008 — External Convergence Map

Status: `RESEARCH INPUT MAP / NOT_CURRENT / NOT_NOVELTY_CLAIM`

Purpose: identify independent legal/control-theory structures that resemble the current ENA research branch, and prevent ENA from mistaking rediscovery or analogy for proof.

## 1. Legal maxim: open liberty vs positively grounded public power

A classic legal formulation distinguishes:

- individual liberty: conduct need not be individually enumerated in advance to be lawful;
- public power: authority over others requires a positive legal basis rather than arising merely from the absence of prohibition.

A widely cited formulation by Sir John Laws is:

> for the individual citizen, everything which is not forbidden is allowed; for public bodies/government, everything which is not allowed is forbidden.

ENA relevance:

```text
LOCAL / OWNED VARIATION
absence of a specific prohibition can leave room for novelty

EXTERNAL / UNOWNED CONSEQUENCE
absence of prohibition does not manufacture authority
```

Do not universalize this as a description of every jurisdiction or every legal domain.

Pointers:

- John Laws, discussions of the presumption of liberty / ultra vires distinction.
- General legal-maxim summaries under “everything which is not forbidden is allowed.”

## 2. Control Barrier Functions: boundary enforcement separated from nominal policy

Control Barrier Function (CBF) literature formalizes safety through forward invariance of a safe set.

A common pattern is:

```text
nominal controller pursues task objective
+
barrier constraint modifies action only as needed to keep state in safe set
```

This is structurally close to ENA's Minimum Sufficient Intervention and negative-boundary hypothesis:

```text
TASK / ADAPTATION POLICY
!=
SAFETY BOUNDARY
```

CBFs do not prove the Agent-level theory, but they provide a mature engineering example in which safety constraints are separated from the detailed performance policy.

Pointers:

- Aaron D. Ames et al., “Control Barrier Functions: Theory and Applications,” European Control Conference, 2019. DOI: `10.23919/ECC.2019.8796030`
- Mohit Srinivasan et al., “Extent-Compatible Control Barrier Functions,” Systems & Control Letters 150 (2021), 104895. DOI: `10.1016/j.sysconle.2021.104895`

## 3. Viability theory: not one optimal path, but existence of viable trajectories

Viability theory asks whether a dynamical system can continue to satisfy constraints over time while retaining at least one feasible evolution.

The **viability kernel** is the set of states from which at least one trajectory can remain within the constraint set indefinitely (or over the relevant horizon).

This is highly relevant to the user's intuition that the action space should remain larger than the prohibited space, but it also refines it:

> raw set size is not enough; the important question is whether viable trajectories still exist and remain reachable.

ENA relevance:

```text
FORMALLY ALLOWED STATE
!=
STATE WITH A VIABLE FUTURE TRAJECTORY
```

and:

```text
SAFE SET VOLUME
!=
VIABILITY KERNEL QUALITY
```

This supports the research focus on topology, reachability, recovery and future mutation paths rather than simple allow/deny counts.

Pointers:

- Jean-Pierre Aubin, viability theory / viability kernels.
- Viability Theory reference material: `https://viability-theory.org/`

## 4. Safety vs liveness

Computer science/control traditions often separate:

- safety: bad things do not happen;
- liveness: useful/good things can still eventually happen.

ENA relevance:

> an architecture that prevents all bad outcomes by preventing meaningful action is safe in a narrow sense but not viable agency.

Candidate distinction:

`SAFETY WITHOUT LIVENESS != VIABLE AGENCY`

This is one reason ENA's target is not maximum prevention.

## 5. What these traditions do NOT establish

They do not prove that:

- negative rules are generally better than positive rules;
- all Agent authority should use open-world semantics;
- a larger action space is always more viable;
- legal maxims transfer directly to autonomous Agents;
- control barrier functions solve memory inheritance or metamemory;
- viability theory defines ENA's exact governance metric.

They independently support a narrower structural observation:

> complex adaptive systems can be governed by preserving a viable constrained region and allowing multiple trajectories within it, rather than prescribing a single trajectory.

## 6. Current ENA novelty discipline

Do not claim novelty for:

- safe-set constraints;
- forward invariance;
- viability kernels;
- the legal maxim that unprohibited individual action may remain free while public authority requires legal basis;
- safety/liveness separation.

The current ENA-specific research combination is instead:

```text
negative consequence boundary
+
adaptive memory
+
counterexample-based scope learning
+
authority asymmetry
+
minimum sufficient intervention
+
viable action topology
+
developmental inheritance
+
future evolvability
```

Whether this combination contains a genuinely new decision-relevant natural law remains open.
