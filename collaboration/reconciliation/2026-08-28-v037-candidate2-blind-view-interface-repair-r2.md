# v0.3.7 candidate.2 blind-view interface repair — r2

Status: `VALIDATION_INTERFACE_DEFECT_CONFIRMED / ISSUE_137_ABORT_PERSISTED / R2_PHYSICAL_BLINDNESS_REPAIR_PREPARED / NOT_CANDIDATE_CHANGE / NOT_RELEASE_AUTHORITY`

## Exact frozen candidate remains unchanged

- identity: `v0.3.7-candidate.2`
- frozen source: `bda470e0a6b170cec61225a905957a501454a2fe`
- frozen candidate subtree: `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`
- Current remains `v0.3.6 / CURRENT / FIELD_VALIDATION`

This repair changes only the independent-validation projection/interface. It does not mutate candidate.2, does not create candidate.3, and does not grant release/promotion authority.

## Issue #137 outcome

The genuinely fresh reviewer correctly stopped before semantic A-S work after ordinary GitHub directory navigation auto-rendered `releases/v0.3.7-candidate/README.md`, exposing source lines 1-8 that the v1.2 view manifest had declared withheld.

The reviewer reported:

`A_S_ABORTED_BOUNDARY_CROSSING / VALIDATION_INTERFACE_DEFECT / NOT_SEALED / A_P_NOT_STARTED`

The externally produced report had SHA-256:

`803f34e4b9592d51266fa34b594496fac6ca44db412b21a8c1793466b837fd50`

It has now been persisted on the invalidated validation occurrence branch at:

`collaboration/reconciliation/2026-08-28-v037-candidate2-independent-a-s-primary.md`

Persistence commit:

`31d4d201fabe0180278ae6371e2f01ffda3de6b0`

That commit is **not** an A-S seal. It is occurrence truth for the interface-defect stop.

## Root cause

The v1.2 candidate.2 blind view still treated reviewer line-range discipline as part of the information boundary for mixed-role files.

That assumption is not robust on an ordinary repository UI:

- GitHub auto-renders a root `README.md` under a directory listing;
- a reviewer opening any physically present mixed-role file normally sees the whole file unless the client itself enforces a range;
- therefore `withhold lines X-Y` is not equivalent to physically withholding those bytes from the A-S information surface.

The reviewer did not fail the protocol. The validation interface failed to enforce its own declared information boundary.

## Additional method correction discovered during repair

Reinspection also showed that the v1.2 manifest's mixed-role classification was too optimistic in two ways:

1. `README.md` after line 8 still contains author-side machine evidence, lineage/freeze narrative, and remaining-gate/status material. It is not safely reducible to a simple `1-8 withheld / 9-EOF semantic` split for blind A-S.
2. `tools/validate_evolution_record_v2.py` contains `def exp_record(...)` beginning at source line 345, before the manifest's previously declared selftest-withheld range. The true A-S semantic core ends at source line 342 (`return errors`); test-helper/corpus/CLI material begins after that boundary.

Therefore the repair does not merely special-case GitHub README auto-rendering. It removes dependence on procedural ranged-read restraint for all mixed-role A-S surfaces.

## r2 blind semantic view

New branch:

`validation/v037-c2-blind-semantic-primary-r2`

Prepared r2 head before fresh intake:

`cdcd8f0dd450ebff12b600078c22fce31bf6cb2a`

Updated neutral entry:

`collaboration/reconciliation/2026-08-28-v037-candidate2-blind-semantic-entry.md`

Updated manifest:

`collaboration/reconciliation/2026-08-28-v037-candidate2-blind-semantic-view.yaml`

### Physical withholding

The r2 A-S view removes the full mixed-role files:

- `README.md`
- `00-READ-ME-FIRST.md`

along with the existing history/oracle/fixture/selftest/prior-probe exclusions.

### Declared derived projections

Two semantically important mixed-role files remain available only as physically blind-safe projections:

1. `RUNTIME-ADOPTION-KERNEL.md`
   - frozen blob: `8207494dc38c4ae5a14e4617ef58c72a1824ccc3`
   - r2 projection blob: `bbec859907c6a600c37c45f679968d582f91e26f`
   - derivation: exact frozen source lines `7-EOF`
   - removed role: package-status header

2. `tools/validate_evolution_record_v2.py`
   - frozen blob: `4a98306ee8bc0685ec6706aedb782381f57071bb`
   - r2 projection blob: `722c2496776b0b0b1ea604c4e2543b1b113314e5`
   - derivation: exact frozen source lines `1-342`
   - removed role: `exp_record` selftest helper, selftest corpus, and selftest/CLI tail
   - `validate_record` and its semantic dependencies remain in the A-S projection.

These projection bytes are validation-interface artifacts, not candidate-byte changes.

## Whole-tree shape

Frozen-source -> r2 compare yields exactly:

- `33` declared whole-file removals;
- `2` declared derived projection modifications;
- `2` intake files added outside candidate cargo;
- no other candidate-file modifications.

Counts are construction facts, not epistemic completeness claims.

## Strengthened boundary rule

For future A-S views:

`PROCEDURAL_RANGED_READ != INFORMATION_BOUNDARY`

Prefer:

`PHYSICALLY_WITHHELD_BYTES OR DECLARED_BLIND_SAFE_PROJECTION`

A fresh reviewer should be able to use ordinary/natural navigation inside the A-S view without accidentally encountering material the manifest says is withheld.

This does not mean every file must be duplicated or every author signal removed. It means a claimed blind boundary must be enforced by the exposed information surface rather than by reviewer self-restraint where natural tooling defeats that restraint.

## Next step

Before opening a replacement fresh intake:

1. mechanically verify the r2 projection bytes equal the declared frozen source slice/prefix;
2. verify all non-projected retained candidate files are byte-identical to frozen source;
3. verify all declared whole-file exclusions are absent;
4. then invalidate/close Issue #137 as interface-aborted occurrence truth;
5. create one new neutral fresh A-S -> A-P intake bound to the verified r2 head;
6. current project-manager session remains ineligible to perform fresh A-S.

`ATTACK_CARDINALITY = OPEN`
