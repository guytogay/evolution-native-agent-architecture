# Evidence Applicability Boundary Audit

Status: `RESEARCH_PLAN / NOT_PROMOTED`

Primary case: `HAR-006`

## Question

Does ENA v0.2.11 already make it sufficiently explicit and machine-legible that valid evidence is applicable only to the subject/state/scope/interval actually observed unless transfer across a boundary is independently justified?

## Existing ingredients to audit

- `08-EVIDENCE-MODEL.md`
- `11-SESSION-REALITY-BOOTSTRAP.md`
- capability-evidence schema/template
- compliance-evidence schema/template
- Session Reality schema/template
- `ENA-CON-036` composition revalidation
- scoped trustworthiness / cross-domain transfer semantics

## Test vectors

1. `config default != current session override`
2. `gateway restart != session override necessarily cleared`
3. `one channel healthy != whole system healthy`
4. `runtime instance A evidence != runtime instance B evidence`
5. `old epoch evidence != current epoch evidence`
6. `test environment evidence != production environment evidence`
7. `one authority path verified != effect-equivalent path verified`

## Audit outputs

For each vector classify:

- field support: `EXPLICIT / DERIVABLE / MISSING`
- semantic prohibition of invalid transfer: `EXPLICIT / IMPLIED / ABSENT`
- validator support: `PRESENT / POSSIBLE / NOT_APPROPRIATE`
- likely fix layer: `NONE / EXAMPLE / CLARIFICATION / SCHEMA / VALIDATOR / NORMATIVE`

## Decision rule

Prefer the smallest layer that closes the false-claim path.

Do not add a Constitution principle if existing Evidence Model semantics plus explicit applicability fields/revalidation are sufficient.

Research formulation under test:

> Evidence validity does not imply evidence applicability.

> An observation supports only the subject, state, scope, and interval it actually observed.
