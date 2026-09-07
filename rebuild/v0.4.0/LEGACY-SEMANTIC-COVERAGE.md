# ENA v0.4 Legacy Semantic Coverage + Dogfood Ledger

Status: `ACTIVE_REBUILD / NOT_CURRENT / NOT_PROMOTED`

This is a decision ledger, not a migration checklist. It exists to preserve decision-material value from v0.3.x without preserving the v0.3.x product shape.

Use this test for every legacy property:

1. What wrong action does it prevent?
2. What positive action/capability does it enable?
3. What is the cheapest representation that preserves that value?

A property may split across locations. For example, a compact action cue may live in `PRACTICAL_CORE` while represented state is protected by `MACHINE_GUARD` and external truth remains `EXTERNAL_CONTROL` or field evidence.

## Coverage ledger

| ID | Legacy property / failure | Wrong action prevented | Positive action enabled | v0.4 placement | Hot disposition | Main lineage |
|---|---|---|---|---|---|---|
| L01 | ENA exists for viable agency/evolution, not obedience or process | treating governance as the objective | explore, learn, vary, select, recover and become more capable | `PRACTICAL_CORE` | KEEP compact | Current Kernel; F-208-13 |
| L02 | `UNKNOWN` stays honest but need not imply paralysis | invented certainty or passive stopping | take cheap read/search/inspect/test actions that can change the decision | `PRACTICAL_CORE` | KEEP | Core contracts 5.11 |
| L03 | material opportunity needs a liveness disposition | accepted ideas disappearing into indefinite latency | `ACT_NOW / WAIT_FOR_SIGNAL / BLOCKED / DROP` with wake/unblock condition | `PRACTICAL_CORE` | KEEP as one compact rule | F-208-12 |
| L04 | claim / evidence / support / applicability are separate | treating available evidence as support for the current claim/scope | identify the missing layer and seek the smallest decision-changing evidence/applicability check | `ACTION_CARD` + `MACHINE_GUARD` where representable | no catalogue entry | Core contracts 5.1; composed validator |
| L05 | stored / expressed / applied / selected are different | treating a stored/imported/proposed candidate as active improvement | keep useful variation latent; trial/select only when reality contact is worth it | `PRACTICAL_CORE` + `MACHINE_GUARD` for represented state | KEEP only action consequence | Kernel; evolution-record.v2 |
| L06 | evolution requires an executable loop, not vocabulary | explaining evolution without changing anything, or forcing continuous self-editing | capture signal -> bounded trial -> observe -> select -> retain/reject | `PRACTICAL_CORE` + `COLD_HOW` | KEEP loop shape; procedure cold | OA-EVO-01; EVOLUTION-LOOP |
| L07 | source/local success does not establish receiver/universal fitness | importing an adaptation as local proof | perform differential receiver-local reality contact and select locally | `ACTION_CARD` + `MACHINE_GUARD` | KEEP adjacent to import action | Migration contracts; ENF-LOCAL-SELECTION |
| L08 | negative/null/unknown results remain evidence | rerunning for a preferred answer or converting failure into success by omission | narrow, reject, preserve unknowns and reuse negative evidence later | `PRACTICAL_CORE` + `COLD_HOW` | KEEP compact | EVOLUTION-LOOP; closed research discipline |
| L09 | backup/restore does not prove real recovery | relying on an untested backup or resuming into stale world state | preserve/drill the needed recovery path and reconcile only stale dimensions | `ACTION_CARD` + `EXTERNAL_CONTROL` | action-bearing cue only | Core contracts 5.3/5.4; ENF-RECOVERY |
| L10 | capability/credential/identity do not mint current external mandate | causing consequential effects with stale or self-created authority | verify real authority only when the contemplated effect depends on it | `PRACTICAL_CORE` + `EXTERNAL_CONTROL` | KEEP one consequential-effect check | Core contracts 5.5; ENF-AUTHORITY-REALITY |
| L11 | attempt / receipt / settlement and cancel / rollback / compensation differ | unsafe replay, duplicate effects, false completion | query actual effect state; use idempotency/fencing/compensation when needed | `ACTION_CARD` + `MACHINE_GUARD` + `EXTERNAL_CONTROL` | no inequality list | OA-EFF-01; ENF-EFFECT-REALITY |
| L12 | stored knowledge is not guaranteed retrieved/salient/applied | assuming a file or memory entry changed behavior | search/inspect when needed and use field evidence for future salience | `ACTION_CARD` + `COLD_HOW` | RETIRE as standalone hot distinction | OA-RET-01; ENF-RETRIEVAL-SUFFICIENCY |
| L13 | component success does not determine composed outcome | integrating components without observing interaction effects | test the composed subject when interaction can change the decision | `ACTION_CARD` | not hot by default | Core contracts 5.7; ENF-COMPOSITION |
| L14 | correlated agreement is not independent support | confidence inflation from copied/correlated sources | inspect provenance/dependency when independence matters | `ACTION_CARD` + `COLD_HOW` | not hot by default | ENF-CORRELATED-EVIDENCE |
| L15 | triggered material obligations must not disappear inside broad completion | claiming completion while a material duty is pending/failed/unknown | externalize only decision-material obligations and close them with evidence | `MACHINE_GUARD` + `COLD_HOW` | not hot by default | Core contracts 5.2 |
| L16 | occurrence truth and lawful retention are different concerns | rollback rewriting history, or provenance rules forcing unlawful retention | preserve minimum truthful lineage while allowing lawful deletion/redaction/expiry | `COLD_HOW` + `THEORY_ONLY` | cold | Core contracts 5.3 |
| L17 | recovery/control must survive relevant self-change when consequence warrants | mutation disabling every correction path or rewriting its own gate | place rescue/control outside the failure domain or use alternate recovery | `ACTION_CARD` + `EXTERNAL_CONTROL` | compact in self-change card | Core contracts 5.4 |
| L18 | Variation Space is proportional, not universal ceremony | forcing sandbox/review machinery onto ordinary low-consequence action | use the lightest real environment capable of answering the question | `PRACTICAL_CORE` + `COLD_HOW` | KEEP | Core contracts 5.6; EVOLUTION-LOOP |
| L19 | continuity is purpose-relative and dimensioned | metaphysical SAME_AGENT debates or blind reuse of stale outputs/authority | revalidate only dimensions that can change the next decision | `ACTION_CARD` + `COLD_HOW` | not separate hot theory | Core contracts 5.8 |
| L20 | standing/correction input is not sovereignty or authority | treating feedback as veto/mandate, or ignoring useful correction because it lacks authority | use correction as evidence/exploration input without transferring authority | `COLD_HOW` | cold unless recurring problem earns card | Core contracts 5.12; OA-STAND-01 |
| L21 | governance must pay rent and converge | controls/process surviving by inertia, or being retired by age alone | keep/simplify/dormant/retire from observed protection vs cost | `PRACTICAL_CORE` + `COLD_HOW` | KEEP practical card | Core contracts 5.10; ENF-CONTROL-RETIREMENT |
| L22 | semantic adoption does not require an ENA-specific tool stack | installing machinery just because ENA names a boundary | inspect Host-native coverage and add only a real missing mechanism | `PRACTICAL_CORE` | KEEP | v0.3.14 local operationalization |
| L23 | Local Projection is only a small cache of recurring Host facts | copying ENA baseline or maintaining a giant second state model | persist only repeatedly decision-changing Host facts and refresh affected facts | `COLD_HOW` | MOVE COLD; retire named concept from default core | v0.3.14 Local Projection |
| L24 | translation/structural parity does not prove behavioral equivalence | claiming cross-language behavior from file parity alone | machine-check represented parity; use bounded field evidence when behavior matters | `MACHINE_GUARD` + `COLD_HOW` | cold | ENF-LANGUAGE-PROJECTION |
| L25 | branch/self-description does not mint Current identity | candidate or stale prose being treated as canonical release | use one governed Current pointer + immutability/readback machinery | `MACHINE_GUARD` + `EXTERNAL_CONTROL` | not runtime hot | CURRENT-BASELINE; ENF-CANONICAL-STATUS |
| L26 | narrow bundled helpers are not universal lifecycle engines | treating `ena_evolve_v2.py` or any ENA tool as mandatory runtime | synthesize/use Host-native machinery that satisfies the real function | `COLD_HOW` | not hot | HOW-MAP; EVOLUTION-LOOP |
| L27 | 38 Constitution IDs, derivations and falsification history remain valuable | losing semantic provenance during simplification | audit, dispute, research and recover why a property exists | `THEORY_ONLY` | MOVE COLD | Constitution/research lineage |
| L28 | the 19-item durable-distinction catalogue as one product unit | prose rent and false sense that distinctions themselves are action | redistribute only decision-material consequences into action surfaces/guards | `RETIRE` | RETIRE from product interface | Runtime Kernel; PR #224; Issue #234 |
| L29 | mandatory semantic -> Cue Index -> HOW Map multi-hop path | requiring the Agent to invent an operational problem before getting practical value | start from the problem/action card and link a deeper HOW directly when needed | `RETIRE` as primary route; `COLD_HOW` indexes may remain | RETIRE from default path | F-208-14/15 |

## What this ledger says about the first v0.4 shape

The legacy value clusters into a much smaller product surface:

- **Practical Core**: agency-first default loop, cheap information gain, opportunity liveness, bounded experimentation, consequential authority/effect checks, recovery-aware self-change, governance retirement, Host-native machinery.
- **Initial Action Cards**: evidence/support, effect lifecycle, recovery/resume, adaptation migration, composition, evidence dependency.
- **Machine/external layers**: represented-state validators, release identity, external mandate/effect/recovery truth, language parity checks.
- **Cold HOW**: implementation patterns, continuity, retention/provenance, retrieval, Host-state caching, control retirement detail.
- **Theory only**: Constitution IDs, derivations, falsification/research lineage.
- **Retire as product units**: the durable-distinction catalogue and mandatory semantic->router->HOW traversal.

This is not a claim that retired prose was false. The semantic value is retained where it changes action or evidence; the old presentation is not retained merely because it existed.

## Dogfood pass — real work

### A. ENA rebuild work itself

Task: continue the handoff action without doing a full-repository audit, then build the semantic coverage ledger.

What the Practical Core changed:

- `I do not know something that matters` led to reading only the routed handoff surfaces, live mutable state and the six explicitly named Current mining surfaces before acting.
- `Repeated friction` and the control-retirement card prevented a one-for-one rewrite of the v0.3.x tree; the work classified legacy value instead.
- `I am changing durable parts` kept Current untouched and used the existing rebuild branch as the bounded change surface.
- The opportunity section exposed one real gap: a material idea that cannot move immediately still needed a wake/unblock disposition. The core was patched with the compact `ACT_NOW | WAIT_FOR_SIGNAL | BLOCKED | DROP` rule instead of adding a new framework.

Result: `PASS_WITH_ONE_COMPACT_PRODUCT_PATCH`.

### B. Non-ENA real task — Human-AI Workbench runner decision

Live task source: `guytogay/human-ai-workbench/NOW.md` asks whether recurring fresh-context transport will eventually justify an API/browser/Agent runner, while explicitly warning not to build one from a single campaign.

Applying the Practical Core:

1. Opportunity: a callable fresh-worker runner could reduce future human relay.
2. Existing evidence: one completed campaign exposed a residual manual fresh-context boundary, but repeated workload sufficient to justify persistent runner infrastructure has not been demonstrated.
3. Cheapest decision-changing move now: do **not** build a runner or manufacture another experiment. Continue ordinary use and observe whether the boundary recurs with meaningful volume/error cost.
4. Liveness: `WAIT_FOR_SIGNAL`.
5. Wake signals: repeated fresh-worker workload, recurring treatment-delivery/output-capture errors, or discovery of a callable execution surface that can preserve the required isolation.
6. First action after wake: inspect/test the smallest candidate execution surface before creating persistent orchestration.

Result: `PASS`. The Practical Core supported agency without turning proactivity into unnecessary construction or synthetic evidence gathering.

## Consequence for next build step

The ledger does not justify expanding `PRACTICAL-CORE.md` row by row. The next useful build is the smallest initial Action Card set for the legacy families that still require practical detail beyond the core:

`EVIDENCE/SUPPORT | EFFECT LIFECYCLE | RECOVERY/RESUME | ADAPTATION IMPORT | COMPOSITION`

Each card should exist only if it can outperform a direct cold link or Host-local synthesis on a real task.
