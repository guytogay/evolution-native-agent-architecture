# Handoff Readback

Status: `PREMERGE_CHECK / POSTMERGE_READBACK_PENDING`

## Premerge consistency checks completed

The outgoing session independently reverified before writing this record:

- ENA repository exists and `main` was observed at `e1e50ed1def69d4a088d670ca26dc54c3b747904` before this handoff branch;
- v0.3.7 remains Current and released bytes are unchanged;
- the latest field-validation archive is PR #177 / merge `e1e50ed1def69d4a088d670ca26dc54c3b747904`;
- old candidate.0 validation PR #115 was still open and was closed as historical/superseded;
- the repository had 41 pre-handoff branch refs;
- `research/ena-reconstruction` was not delete-safe because it retained three unique research artifacts;
- those three artifacts were read from the old branch and copied into this fresh main-based handoff branch;
- current live branch control files still described the older long-lived integration-branch model and are being aligned in this change;
- Human-AI Workbench exists separately and has only `main` before its planned update;
- `ena-field-guide` has not been created.

## Semantic/readback questions the merged state must answer

After merge, a fresh successor should be able to determine from main:

1. **What is Current?**
   - v0.3.7 / CURRENT / FIELD_VALIDATION.
2. **Did recent evolutionary-memory work change Current?**
   - No.
3. **What did A–H show?**
   - tested semantic relations were naturally reachable under GPT-5.6 Sol/high reasoning; no repair arm justified.
4. **What did I–L show?**
   - all four inheritance representations produced mechanism-good behavior; no relative boundary-memory advantage observed.
5. **What hypothesis was narrowed?**
   - superior transfer fitness of boundary-oriented inheritance.
6. **What research comes next?**
   - multi-stage Developmental Inheritance / MDS mechanism experiment.
7. **Does comprehensive coverage stop there?**
   - No; the Coverage Map preserves metamemory, sleep/dreaming, ecology, decay, propagation, purpose-relative selection, etc.
8. **What branch is current continuation authority?**
   - main; short-lived PR branches are temporary only.
9. **Can `research/ena-reconstruction` be deleted immediately?**
   - only after this PR merges/readback confirms its three unique artifacts are on main.
10. **Should the future Field Guide be created now?**
   - No; wait for reusable reality-backed HOW.

## Postmerge actions required

After this handoff PR merges:

- read `NOW.md`, `CURRENT-HANDOFF.yaml`, this record, branch cleanup audit, and the three migrated Agent Skills files from `main`;
- record the actual handoff PR number and merge SHA here or in a small follow-up readback commit;
- mark the manifest/readback as merged/read-back;
- verify no Current bytes changed;
- verify the old `research/ena-reconstruction` branch is now content-safe to delete;
- manually delete cleanup refs when convenient because the current connector lacks true delete-ref support;
- delete the temporary handoff branch after its lineage is durable.

## Current readback verdict

`PREMERGE_STRUCTURE_COMPLETE / POSTMERGE_READBACK_PENDING`
